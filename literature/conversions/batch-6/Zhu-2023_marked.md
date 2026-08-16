---
conversion_metadata:
  converted_at: "2026-07-21T10:08:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Zhu-2023.pdf"
  source_pdf_sha256: "080f8420c1cbabf9b877d98bc1e1c5ac0cb12fb1158649ade3abcc0a60ab69ad"
  page_count: 20
  markdown_char_count: 140542
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received: 24 March 2023

|  Accepted: 30 September 2023

DOI: 10.1111/bjet.13401

O R I G I N A L   A R T I C L E

Upgrading financial education by adding 
Python- based personalized financial 
projection: A randomized control trial

Alex Yue Feng Zhu

Department of Social Sciences and Policy 
Studies, The Education University of Hong 
Kong, Hong Kong, China

Correspondence
Alex Yue Feng Zhu, Department of 
Social Sciences and Policy Studies, The 
Education University of Hong Kong, 10 Lo 
Ping Road, Tai Po, N.T., Hong Kong, China.
Email: yfzhu@eduhk.hk

Funding information
The Investor and Financial Education 
Council in Hong Kong, China

Abstract
Research has shown that even though standardized 
financial  education  has  gained  prevalence  to  pro-
mote  financial  literacy  over  the  past  decade,  it  has 
had  little  effect  on  personal  financial  planning.  The 
present study used a randomized control trial to ex-
amine the effectiveness of a Python- based person-
alized  financial  projection  on  young  working  adults 
in Hong Kong, to examine if and how this approach 
improves  their  financial  planning.  Participants  as-
signed  to  the  experiment  group  received  standard-
ized financial education and Python- based financial 
projections,  while  those  in  the  control  group  only 
received  standardized  financial  education.  The  as-
sessment based on the two- wave data showed that 
Python- based  financial  projection  promoted  future 
time  perspectives,  reduced  temporal  discounting, 
and  improved  financial  planning  via  the  full  media-
tion of promoting financial attitudes. Although numer-
ous applications for personal financial planning exist 
(such as Wallet, Walnut, Monefy, and Money View), 
our Python- based financial projection stands out as 
the pioneering solution tailored for the hands- on ma-
nipulation  of  programming  code  to  effectively  man-
age  personal  finances.  Our  findings  suggest  a  new 
track  to  upgrade  personalized  financial  projection 
and standardized financial education and contribute 
generously  to  the  development  of  personal  finance 
education.

This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits 
use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial 
purposes.
© 2023 The Authors. British Journal of Educational Technology published by John Wiley & Sons Ltd on behalf of British 
Educational Research Association.

Br J Educ Technol. 2024;55:731–750.

wileyonlinelibrary.com/journal/bjet

|  731

---

<!-- PAGE 2 -->

732

|

K E Y W O R D S
financial planning, personal finance education, personalized 
financial projection, Python, standardized financial education, 
temporal discounting

Practitioner notes

What is already known about this topic

•  Standardized financial education promotes objective financial knowledge.
•  Standardized  financial  education  has  a  limited  effect  on  personal  financial

planning.

•  Classical personalized financial projection promotes personal financial planning,

but the effect is small.

What this paper adds

•  Introduction of a novel Python- based personalized financial projection by manipu-

lating projection code.

•  The evidence that Python- based personalized financial projection more strongly 
improves personal financial planning, compared to the classical personalized fi-
nancial projection.

•  The  evidence  why  Python- based  personalized  financial  projection  can  improve

personal financial planning.

Implications for practice and/or policy

•  Facilitating engagement of young working adults with personalized finance plan-

ning through the use of a Python- based intervention.

•  Integrating  Python- based  personalized  financial  projection  into  standardized  fi-

nancial education in the school setting.

•  Using  Python  as  the  platform  to  design  more  topic- specific  financial  education

module.

I NTRO DUCTI O N

There  has  been  a  surge  in  access  to  financial  technology  and  diversified  financial  prod-
ucts and services in modern societies, such as Hong Kong. The rise in financial respon-
sibility among individual consumers necessitates the equipment of basic financial literacy. 
Recently, the personal finance literature described financial literacy as a multidimensional 
construct  rather  than  objective  financial  knowledge  alone  (Hizgilov  &  Silber,  2020;  Lyons 
& Kass- Hanna, 2021). Consumers with high financial literacy refer to those who develop a 
sound understanding of personal finance terms, hold positive attitudes toward healthy finan-
cial habits, have self- esteem in financial practice and actively engage in financial planning 
(Rai  et  al.,  2019;  Xiao  &  O'Neill,  2016).  Understanding  financial  literacy  as  a  multidimen-
sional  construct  carries  significant  importance  because  personal  financial  outcomes  are 
influenced by a combination of factors, including financial knowledge, attitudes, confidence, 
planning, and decision- making (Douissa, 2020; Hizgilov & Silber, 2020). Isolating any one 
of these factors overlooks the intricate interplay between them and their collective impact 
on financial well- being. This multidimensional view has a profound impact on how financial 
literacy should be assessed, and places heightened emphasis on the necessity for financial 
education programs to be comprehensive.

---

<!-- PAGE 3 -->

|  733

Standardized financial education has gained prevalence among practitioners in the last 
decade  to  promote  financial  literacy  (Amagir  et  al.,  2018).  However,  it  has  little  effect  on 
personal  financial  planning,  although  it  improves  objective  financial  knowledge  (Kaiser  & 
Menkhoff, 2020). The main limitation of a generic intervention is that it cannot be flexibly 
adjusted to fit an individualized financial status and needs. On the other hand, personalized 
financial intervention is more potent in shaping financial planning because it can affect par-
ticipants' underlying psychology (Bartels & Urminsky, 2015; Wiener & Doescher, 2008). In 
particular,  personalization  harnesses  the  power  of  intrinsic  motivation  by  aligning  with  an 
individual's personal values and aspirations (Li et al., 2020, 2023). When financial advice 
deeply resonates with a person's goals, it sparks a heightened motivation to actively engage 
in personal financial management. Furthermore, the act of tailoring advice to suit each indi-
vidual's distinct circumstances fosters a robust sense of self- efficacy (Li et al., 2020). This, 
in  turn,  empowers  them  to  embark  on  proactive  measures  within  their  financial  planning 
journey.

Behavioural  scientists  have  developed  psychological  models  that  explain  why  people 
actively  join  in  personal  financial  planning  (Serido  et  al.,  2013;  Tomar  et  al.,  2021).  Two 
models  were  tested  and  validated  by  our  team  in  Hong  Kong  using  data  collected  from 
adolescents  and  working  adults  (Zhu,  2018;  Chou  et  al.,  2015).  Our  results  suggest  that 
future perspective, temporal discounting, and financial attitudes play significant mediational 
roles in the pathway toward skilful financial planning. There are hierarchical relationships 
among future time perspectives, temporal discounting, and financial attitudes. Future time 
perspectives  only  capture  attitudes  toward  the  future,  while  temporal  discounting  reflects 
intertemporal choices (ie, how a consumer will choose between the present and the future) 
(Chapman, 1996; Seaman et al., 2022). When consumers perceive that the future is more 
valuable than the present (ie, low temporal discounting), there will be a willingness to save 
and invest for the future and to engage in budget and consumption control in the present (ie, 
positive financial attitudes). Therefore, a personalized financial intervention manipulating fu-
ture time perspectives, temporal discounting, and financial attitudes may promote the skills 
and intentions of financial planning.

Temporal discounting theory suggests that people normally devalue the future because 
of their psychological disconnectedness from the future (Bartels & Urminsky, 2015). Without 
cognitive intervention, people can hardly establish the vividness of and a connection to the 
future self, not to mention sacrificing immediate temptation for the benefit of the future self 
(eg, controlling immediate spending and saving for the future). That is why behavioural sci-
entists resort to computer- based interventions to promote the vividness of the future, such 
as age- progressed renderings with virtual reality technologies, discussion with future self- 
produced AI technology, and remarkably personalized financial projection with simulation 
techniques (Goda et al., 2014; Hershfield et al., 2011; Marques et al., 2018).

Recently, our team conducted a three- arm experiment to examine the effectiveness of 
a computer- based personalized financial projection among working adults in Hong Kong. 
The projection simulates the financial resources accumulated in the distant future based on 
a working adult's current earnings, savings and investment behaviours (Zhu et al., 2023). 
We masked the working mechanism of the projection and created a mobile application that 
showed the projected financial outcomes to the participants after they input their current fi-
nancial choices. The experimental results showed that the personalized financial projection 
significantly reduced temporal discounting, but the effect was small (b* = −0.11). The find-
ings also revealed that the projection did not significantly shape future time perspectives. 
Both limitations are likely  due to  a direct connection  between  the present and the  future, 
without  vivid  guidance  on  how  the  present  and  future  selves  are  connected  (Oyserman 
et al., 2004). One potential solution could involve introducing participants to the coding of 
a  computer- based  personalized  financial  projection.  This  approach  would  grant  them  the 
opportunity  to  manipulate  projection  code,  thus  enabling  the  forecasting  of  individualized

---

<!-- PAGE 4 -->

734

|

financial trajectories. This process would serve to elucidate the intricate interplay and con-
nection between the present and the future.

Python,  created  by  Guido  van  Rossum  and  released  in  1991,  was  recognized  as  the 
most  popular  coding  tool  in  the  world  by  the  Popularity  of  Programming  Language  Index 
(PYPI, 2020). Python has been observed to have a low threshold for learners and powerful 
computing,  design  and  simulation  functions.  Humber  (2018)  adopted  Python  as  a  coding 
tool to simulate personal financial planning. Considering that Python is user- friendly, in this 
study, we used Python as the coding language to develop a personalized financial projection 
program. Specifically, we created an experimental condition in which we taught young work-
ing adults basic Python grammatical rules and how to manipulate projection code developed 
by us to create “their” financial projections. The primary objective of this study was to test 
whether Python- based personalized financial projection could achieve the following:

1.  More  strongly  reduce  temporal  discounting  compared  to  our  previous  financial  pro-

jection,  which  masks  the  coding.

2. Promote future time perspectives and financial attitudes.
3. Improve financial planning via the mediation of temporal discounting, future time perspec-

tives and financial attitudes.

LITER ATUR E R E V I E W

The motivation for upgrading standardized financial education

There is a shared sense of lifelong financial education that educators should start introduc-
ing basic financial knowledge in primary schools, delivering standardized and comprehen-
sive financial education in secondary schools, and offering topic- specific financial training 
among  college  students  and  working  adults  (Amagir  et  al.,  2018;  Garcia,  2013;  Walstad 
et al., 2017). Financial education has even been extended to older adults to assist them in 
managing their healthcare choices (MacLeod et al., 2017).

By the end of 2017, more than 70 countries had developed national strategies to compre-
hensively promote the financial literacy of the next generation of young adults (OECD, 2017). 
Educational  authorities  have  added  standardized  financial  training  to  the  secondary- level 
curriculum structure in 15 of the 17 Asia- Pacific Economic Cooperation (APEC) economies 
(OECD, 2019). Considering that there has been no standardized financial education in sec-
ondary schools in Hong Kong, our team introduced an international standardized financial 
curriculum, the Financial Fitness for Life (FFFL), to Hong Kong adolescents and conducted 
the  first  randomized  control  trial  in  Asia  to  assess  its  impacts  on  multiple  dimensions  of 
financial literacy (Zhu, 2020; Zhu et al., 2021). The FFFL was developed by the Council for 
Economic Education in the U.S. and was appraised as the most comprehensive standard-
ized financial education in the international community (Batty et al., 2015; Berry et al., 2018; 
Walstad  et  al.,  2010).  The  FFFL  teaches  participants  basic  concepts  to  make  sound  de-
cisions  regarding  earning  income,  spending,  saving,  borrowing,  investing  and  managing 
money.

Our experiment showed that the FFFL was sufficiently powerful to enhance the objective 
financial knowledge of participants but inadequate to bring positive change to their financial 
planning  (ie,  saving,  budgeting  and  spending  control;  Author,  2020;  Author  et  al.,  2021). 
Recent systematic reviews and meta- analyses consistently suggest that standardized finan-
cial education is more potent in shaping objective financial knowledge than financial plan-
ning behaviours (Amagir et al., 2018; Kaiser & Menkhoff, 2020). Hence, this paper proposes 
intelligent  solutions  to  upgrade  standardized  financial  education  to  promote  participants' 
financial planning. In this study, we designed and conducted a Python- based personalized

---

<!-- PAGE 5 -->

|  735

financial projection and examined its intervention mechanism (ie, how it promoted financial 
planning  for  participants  by  changing  future  time  perspectives,  temporal  discounting  and 
financial attitudes).

Python- based personalized financial projection, future time 
perspectives and temporal discounting

Individuals experience multiple events that break the life course into several independent 
sections (Rutt & Löckenhoff, 2016). Typical events include going to college as a freshman, 
getting married, studying overseas and relocating family. People may perceive these events 
as turning points that reduce the discontinuity of the whole life course (Hershfield & Bartels, 
2018). When there is inadequate continuity between the present and the future, people do 
not believe that the future quality of life is related to the present sacrifice. They would rather 
believe  that  these  turning  points  (ie,  life  events)  determine  future  well- being  in  a  random 
walk.  The  future  can  never  be  valuable  when  vague,  uncertain  and  obscure  (Hershfield 
et al., 2011; Pronin & Ross, 2006).

Unlike financial projection without presenting coding details (eg, Fajnzylber & Reyes, 2015; 
Fuentes et al., 2022; Goda et al., 2014), Python- based financial projection can reduce tem-
poral discounting more strongly and improve future time perspectives. Python- based coding 
links the present to the future by convincing users that current financial choices determine 
future financial outcomes, thereby increasing the perceived continuity of life courses. The 
coding  presents  a  detailed  simulation  model  illustrating  how  financial  status  and  choice 
develop into future financial outcomes. The perceived value of the future automatically in-
creases when the future is no longer an ambiguous object but a predictable outcome follow-
ing a clear development track. Therefore, we propose the following hypotheses:

H1.  Python- based  financial  projection  reduces  temporal  discounting  more 
strongly.

H2.  Python- based financial projection promotes future time perspectives.

H3a  &  H3b.  Python- based  financial  projection  improves  personal  financial 
planning by the mediation of reducing temporal discounting and promoting future 
time perspectives, respectively.

Python- based personalized financial projection and financial attitudes

Experiential learning theory (ELT) constructs a holistic model that fits the learning process 
and  human  development  in  different  fields  (Kolb  et  al.,  2014),  such  as  financial  literacy 
(composed  of  knowledge,  attitudes  and  behaviours).  People  must  experience  two  stages 
to  develop  sound  financial  literacy:  grasping  experience  and  transformation  experience 
(Noh, 2022). The grasping experience contains substantial financial experience (eg, by fre-
quent  financial  practice)  and  abstract  concepts  (eg,  by  standardized  financial  education). 
To  gain  transformation  experience,  learners  must  develop  reflective  observation  (eg,  by 
observing the financial practices of others) or active experimentation (eg, by trial and error).
Our  previously  validated  model  among  youth  in  Hong  Kong  reveals  that  when  people 
engage in a type of financial practice with high frequency (ie, substantial financial experi-
ence  in  the  grasping  experience  of  ELT),  they  develop  financial  habits  without  promoting 
corresponding financial attitudes (Zhu, 2018). Additionally, our previous experiment showed 
that standardized financial education (ie, abstract concepts in the grasping experience of

---

<!-- PAGE 6 -->

736

|

ELT) helped participants acquire financial concepts but failed to shape their positive finan-
cial  attitudes  (Zhu,  2020).  Hence,  scholars  should  seek  solutions  to  improve  financial  at-
titudes  by  promoting  a  transformation  experience  of  ELT  (reflective  observation  or  active 
experimentation).

The  Python- based  personalized  financial  projection  design  allows  participants  to  be 
observers  and  practitioners  simultaneously.  Participants  may  adjust  the  parameters  (eg, 
interest  rate,  inflation  rate,  investment  rate  of  return)  and  the  inputs  in  the  program  (eg, 
salary, age, expenses) to review the financial details of others and themselves. They may 
adjust these variables multiple times to identify the best planning strategy to achieve their 
ideal financial outcomes (eg, experimentation). In comparison, classical personalized finan-
cial  projections  do  not  allow  for  the  adjustment  of  parameters  and  present  a  simple  and 
friendly interactive window (eg, a mobile application) for participants to adjust inputs only 
(Fajnzylber & Reyes, 2015; Fuentes et al., 2022; Goda et al., 2014). Furthermore, the utiliza-
tion of Python- based financial projection empowers participants with the capability to refine 
the  projection  process.  This  is  achieved  through  the  revision  of  pre- existing  code  or  the 
incorporation of entirely new code elements, thereby fostering robust experimentations and 
explorations. In summary, Python- based financial projection motivates participants to “play” 
the model and immerse themselves in concrete realities to learn and develop financial liter-
acy, which utilizes the core advantage of ELT. Therefore, we offer the following hypotheses:

H4.  Python- based financial projection improves financial attitudes.

H5.  Python- based financial projection promotes personal financial planning by 
the mediation of improved financial attitudes.

M ETHO D

General design

This study aimed to upgrade standardized financial education by adding a Python- based 
personalized financial projection. To justify this, we designed a randomized control trial to 
test  how  and  to  what  extent  the  Python- based  financial  projection  improved  financial  lit-
eracy. Participants in the experimental group received standardized financial education as 
well as Python- based financial projections, whereas participants in the control group solely 
received standardized financial education. This design enabled us to examine the unique 
effect of Python- based financial personalized projection on three mediators (ie, future time 
perspectives, temporal discounting and financial attitudes) and one outcome (ie, financial 
planning of participants).

Standardized financial education

We  implemented  FFFL  modules  to  conduct  standardized  financial  education.  The  FFFL 
has  been  validated  among  young  people  in  Hong  Kong  (Zhu  et  al.,  2021).  Financial  top-
ics in the FFFL (ie, earning income, spending, saving, borrowing, investing and managing 
money) were seamlessly connected using the life course financial planning model (Salignac 
et al., 2020). For example, savings and investment are necessary to establish financial well- 
being throughout life, while budgeting and spending control are prerequisites to saving and 
engaging in investment. We integrated multiple teaching strategies into the two- hour train-
ing, including lectures, case studies, group discussions, videos, games and role- playing.

---

<!-- PAGE 7 -->

|  737

Python- based personalized financial projection

The Python- based personalized financial projection is the core component of our interven-
tion. It is composed of five hours of training in basic Python grammatical rules, two hours of 
coding skills for beginners and applying two financial projection models to facilitate financial 
planning.  This  intervention  entails  the  manipulation  of  projection  code  developed  by  our 
team to cater to individualized circumstances. Mosh (2022) developed a short course to fa-
miliarize beginners with Python skills in around 10 hours. We used it to train the participants 
in Python grammar, but shortened it to five hours because we needed to cover coding skills 
related to two financial projection models only. The details are reported in Table 1.

Bearing in mind that we aimed to improve the financial planning of participants by pro-
moting  their  future  time  perspectives  and  weakening  temporal  discounting,  we  designed 
two financial projection models to more vividly demonstrate the time value of money. The 
first model (ie, the money management model) simulated an individual's earning, spending, 
saving and investment behaviours in the upcoming years to show that compound interest 
could appreciate wealth and build financial well- being in the future. With a foundational un-
derstanding of Python- based coding at their disposal, participants were encouraged to ac-
tively calibrate economic parameters (such as interest rates, inflation rates and investment 
returns) and individual inputs (including monthly expenditures and saving rates) in the pro-
jection code we developed to simulate the progressive accumulation of wealth. Furthermore, 
participants were allowed to introduce new code elements if they deemed it beneficial in mir-
roring their personalized financial trajectory. Paramount to this experience was the iterative 
nature of the model, which vividly underscored the far- reaching consequences of contem-
porary decisions on future quality of life. Beyond this, participants were notably encouraged 
to factor in the appreciation of money over time when arriving at financial decisions. The 
structural flow of the first model is visually expounded upon in Figure 1.

Next,  we  developed  the  second  model  (eg,  debt  management  with  a  credit  card)  to 
help  participants  learn  about  the  substantial  future  cost  after  falling  into  the  “revolving 
credit”  trap  when  using  a  credit  card  for  consumption.  The  model  aimed  to  effectively 
show that the total cost of consumption with revolving credit would be much higher than 
the  original  price  of  the  commodity,  and  the  considerable  pressure  of  repayment  may 
seriously lower the quality of life in the future. Analogous to the preceding model, partic-
ipants were invited to try multiple scenarios by adjusting the economic parameters (eg, 
interest rates for borrowing, the most prolonged borrowing period) and personal inputs 
(eg, monthly payments, loan periods without a contract). Concurrently, participants were 
encouraged  to  refine  existing  code  elements  or  even  forge  new  ones  if  they  believed 
such  modifications  would  enhance  the  personalization  of  the  projection.  Significantly, 
these explorations underscored the pivotal link between present- day repayment actions 
and future financial well- being. The procedural trajectory of the second model is visually 
illustrated in Figure 2.

Participants

Python- based financial projection belongs to topic- specific financial education. According 
to the life course financial education landscape, it best fits the working adult group (Walstad 
et al., 2017). Young working adults are digital natives surrounded by computers and digital 
devices  and  maintain  a  shorter  psychological  distance  with  a  programming  tool  such  as 
Python. Therefore, we believe it is beneficial to limit the participants to young working adults 
to maximize the potential effect of our intervention. Considering that personal financial sta-
tus is the fundamental condition for engaging in financial activities, there is a motivation to

---

<!-- PAGE 8 -->

738

|

e
m
T

i

r
u
o
 h
1

r
u
o
 h
5
.
0

r
u
o
 h
5
.
0

r
u
o
 h
5
.
0

r
u
o
 h
5
.
0

r
u
o
 h
4
.
0

r
u
o
 h
4
.
0

r
u
o
 h
4
.
0

r
u
o
 h
4
.
0

r
u
o
 h
4
.
0

l

r
e
d
o
h
e
c
a
p

l

'

s
g
n
i
r
t
s

e
h
t

e
d
s
n

i

i

m
e
h
t

t
r
e
s
n

i

d
n
a

)
s
(
e
u
a
v

l

d
e
i
f
i

c
e
p
s

e
h
t

g
n
i
t
t
a
m
r
o
F

)
r
e
s
u

e
h
t

m
o
r
f

y

l
l

a
u
s
u
(

t
u
p
n

i

e
h
t

m
o
r
f

e
n

i
l

a

i

g
n
d
a
e
R

r
e
h
t
o
n
a

o
t

e
p
y
t

a
t
a
d

e
n
o
m
o
r
f

i

n
o
s
r
e
v
n
o
c

i

g
n
m
r
o
f
r
e
P

t
c
e
b
o

j

n
a

o
t

r
e
t
n
o
p

i

a

s

i

t
a
h
t

e
m
a
n

c

i
l

o
b
m
y
s
A

l

o
o
b

d
n
a

,
g
n
i
r
t
s

i

,
t
n
o
p

g
n
i
t
a
o
l
f

,
r
e
g
e
t
n
I

e
p
y
t

a
t
a
d

i

g
n
m
r
o
f
s
n
a
r
T

g
n
i
r
t

S

t
a
m
r
o
F

n
o
i
t
c
n
u

f

t
u
p
n
I

a
t
a
d
f
o

e
p
y
T

l

e
b
a
i
r
a
V

i

g
n
d
o
c

d
e
s
a
 b
-
n
o
h
t
y
P
g
n
n
n
u
r

i

d
n
a
m
r
a
h
C
y
P
g
n

i
l
l

a
t
s
n
I

t

l

n
e
m
p
o
e
v
e
d
m
a
r
g
o
r
p
f
o
t
n
e
m
n
o
r
i
v
n
E

n
o

i
t
p

i
r
c
s
e
D

c

i

p
o
T

.

i

g
n
d
o
c

n
o
h
t
y
P
c
s
a
B

i

1

E
L
B
A
T

,
)

%

(

i

r
e
d
n
a
m
e
r

,
)
*
(

n
o
i
t
a
c

i
l

p
i
t
l
u
m

,
)
/
(

i

n
o
s
v
d

i

i

,
)
−
(

n
o
i
t
c
a
r
t
b
u
s

,
)

+

(

n
o
i
t
i
d
d
A

l

e
u
r

e
c
n
e
d
e
c
e
r
p

s
r
o

t

a
r
e
p
o

d
n
a

l

n
o
i
t
a
u
c
a
c

l

l

a
c
i
t
a
m
e
h

t

a
M

.
t
o
n

r
o

d
e
t
u
c
e
x
e

e
b

o
t

d
e
e
n
s
t
n
e
m
e
t
a
t
s

i

n
a
t
r
e
c

r
e
h
t
e
h
w
g
n
d
c
e
D

i

i

s
n
o
i
t
a
r
e
p
o
T
O
N

l

i

a
c
g
o
L

d
n
a
R
O

l

i

a
c
g
o
L

,

D
N
A

l

i

a
c
g
o
L

t
e
m
s

i

n
o
i
t
i
d
n
o
c

i

n
a
t
r
e
c

a

l
i
t
n
u

e
d
o
c

k
c
o
b

l

a

i

g
n
n
n
u
R

l

e
b
a
e
g
n
a
h
c

d
n
a

d
e
r
e
d
r
o

s

i

i

h
c
h
w
n
o
i
t
c
e

l
l

o
c
A

)
t
s

i
l

a

,
g
e
(

e
c
n
e
u
q
e
s

a

r
e
v
o

g
n
i
t
a
r
e
t
I

)
/
/
(

i

n
o
s
v
d

i

i

r
e
g
e
t
n

i

d
n
a

,
)
*
*
(

e
r
a
u
q
s

s
e
u
a
v

l

d
n
a

s
y
e
k

f
o

s
r
i
a
p

s
u
o
i
r
a
v

f
o

e
r
u
t
c
u
r
t
s

d
e
h
s
a
h
A

d
e

l
l

a
c

s

i

t
i

n
e
h
w
s
n
u
r

l

y
n
o

i

h
c
h
w
e
d
o
c

f
o

k
c
o
b
A

l

l

e
b
a
i
r
a
v

l

e
g
n
s

i

a

n

i

s
m
e
t
i

l

e
p
i
t
l
u
m
g
n
i
r
o
t
S

.
)
6
1
0
2
(

s
a
P

l

r
e
d
n
a
V
m
o
r
f

d
e
t
c
a
r
t
x
e

s
a
w
n
o
i
t
p
i
r
c
s
e
d

e
h
T

:

e

t

o
N

t
n
e
m
e
t
a
t
s

”
f
i
“

e
h
T

s
r
o
t
a
r
e
p
o

l

i

a
c
g
o
L

p
o
o

l

”
e

l
i

h
w

“

e
h
T

p
o
o

l

”
r
o
f
“

e
h
T

y
r
a
n
o

i
t
c
D

i

s
n
o
i
t
c
n
u
F

l

e
p
u
T

t
s
L

i

---

<!-- PAGE 9 -->

|  739

F I G U R E   1   Model of the money management.

F I G U R E   2   Model of the debt management with a credit card.

further limit the participant to those with solid earning power. Overall, the participant has to 
meet the following criteria:

1.  Aged  18– 35 years.
2. Full- time  administrative  staff  at  public  universities  in  Hong  Kong,  with  a  stable  monthly

income above the median in Hong Kong.

3. Not holding a degree in finance or computer science.
4.  Not having taken any standardized financial courses.
5. Not a Python coder.

---

<!-- PAGE 10 -->

740

|

Procedures

We emphasize the quantitative nature of our study, which hinges on the collection of first- 
hand data to rigorously evaluate a two- arm experimental model. The ensuing sections de-
lineate the meticulous procedure we employed, elucidating our efforts to ensure robustness 
in our experimental design and data collection.

The research team appointed two part- time research officers. The first was responsible 
for recruiting participants, preparing assessment instruments and managing research data. 
The second staff member was assigned duties related to Python and FFFL (ie, preparing 
intervention materials and developing the Python- based financial projection program). We 
used  “Wix.com  (a  free  online  website  builder)”  to  create  a  public  platform  that  published 
comprehensive  information  regarding  our  intervention,  including  indicative  contents,  our 
team members and the confirmed timetable. To fit the timetable of the university staff, we 
offered experimental conditions on Friday night and daytime on the following Saturday. The 
arrangement ensured that there was a low likelihood of attrition during the intervention. All 
teaching and learning activities were arranged online via Zoom meetings.

The  email  contacts  of  full- time  administrative  staff  in  eight  publicly  funded  universities 
in Hong Kong are open. We created the registration link using Qualtrics XM and attached 
it to the mass email invitation. In the invitation, we detailed the research objective and the 
significance of this study in the personal finance landscape in Hong Kong and guaranteed 
that those who completed the training and two tests (ie, pretest and post- test) would get a 
supermarket cash coupon worth HK$100 (= US$12.90).

People who registered for the intervention received a pretest link. We randomly assigned 
participants who completed the pretest to either the experiment or the control group. For 
the experiment group, we offered the intervention in two rounds (ie, on the first and second 
weekends of January 2023). In each round, we accepted at most 25 participants to ensure 
adequate communication between the trainer and each trainee. We conducted the post- test 
after they completed both the FFFL and Python- based financial projections. The training in 
the experimental group lasted 9 hours in total.

In the control group, we only taught the FFFL module (ie, standardized financial education 
lasting for only 2 hours) between the pretest and post- test. The FFFL was delivered on the 
third weekend of January 2023. However, for ethical considerations, we offered the same 
Python- based financial projection to the control group participants after they completed the 
post- test. In other words, the Python- based financial projection in the control group was not 
part of our randomized control trial. It was only a gift to the participants in the control group.

Measurements

In the pretest and post- test, we adopted assessment instruments that have been validated 
among working adults in Hong Kong to measure potential mediators (ie, future time perspec-
tive,  temporal  discounting  and  financial  attitudes)  and  one  outcome  variable  (ie,  financial 
planning)  (Chou  et  al.,  2015,  Zhu  et  al.,  2021,  2023).  Future  time  perspectives  were  as-
sessed using six items on a five- point scale (1 = highly disagree; 5 = highly agree) extracted 
from Tomar et al. (2021), with excellent internal consistency reliability in the pretest and post- 
test (α = 0.88 and 0.90). The six items included the following:

•  “I like to think about what the future will hold.”
•  “I enjoy thinking about how I will live years from now in the future.”
•  “I look forward to life in the distant future.”
•  “According to me, it is important to have a long- term perspective in life.”

---

<!-- PAGE 11 -->

|  741

•  “My close friend would describe me as future- oriented.”
•  “I look forward to a long journal toward the distant future.”

We  invited  participants  to  play  two  games  to  assess  temporal  discounting  (ie,  making 
hypothetical choices between an immediate reward and a delayed fixed reward) (Basile & 
Toplak, 2015). In the first game, we asked participants to choose between HK$10,000 now 
and HK$10,000 one month later. We gradually reduced the amount that could be obtained 
now  and  created  an  additional  11  scenarios  for  participants  to  choose  from  two  options. 
Once a turning point occurred (ie, participants switched to get the amount one month later), 
the present value of HK$10,000 one month later (ie, the reversed temporal discounting) was 
identified. In the second game, we repeatedly asked participants to make 12 hypothetical 
choices but adjusted the delayed period from one month to one year. The total 24 items in 
the two games are presented in Table 2. We identified the temporal discounting shortly and 
in the distant future by reviewing participants' choices.

Financial  attitudes  were  assessed  with  three  items  developed  and  used  in  Shim 
et  al.'s  (2015)  study.  We  asked  participants  to  report  their  agreement  with  three  financial 
behaviours on a five- point scale (1 = highly disagree; 5 = highly agree), including:

•  “You should make sure there is a sufficient balance in your bank account.”
•  “You should clean the debts in your credit card every month.”
•  “You should save to prepare for emergencies.”

The internal consistency across the three items was adequate (pretest: α = 0.87; post- test: 
α = 0.85). Financial planning was measured by a single item, “Please report your financial 
planning activities (Salignac et al., 2019).” The answers were calibrated on a four- point scale 
(1 = In the current financial status, it is impossible for me to engage in any financial planning 
activity; 4 = In the current financial status, it is effortless to plan for my finance).

In  addition  to  the  mediators  and  the  outcome  variable,  we  assessed  the  background 
variables, ie, educational achievement, monthly personal income, monthly family income, 
and total family assets. We asked participants to report their educational achievements by 
choosing from 1 (no formal schooling) to 6 (a postgraduate degree or above). Financial sta-
tus is a critical prerequisite to financial planning, so it must be measured among participants 
and added as the control in main analysis. Considering that financial status was sensitive 
information to participants, we invited them to choose a range rather than report specific 
amounts when measuring monthly personal income, monthly family income, and total family 
assets. The results were as follows:

•  Monthly personal income ranged from 1 (HK$18,700 − HK$19,999, UD$1 = HK$7.75) to 6

(HK$60,000 or above).

•  Monthly  family  income  ranged  from  1  (HK$18,700 − HK$19,999)  to  6  (HK$100,000  or

above).

•  Total family assets ranged from 1 (HK$0 − HK$ 499,999) to 11 (HK$5,000,000 or above).

Data analysis

Following  the  standardized  procedures  of  experiment- based  intervention  research,  we 
checked whether the group assignment (ie, assigning participants to either the experiment 
or control group) was adequately random by examining whether there was a significant dif-
ference in mediators, outcome variables and background variables (Becchetti et al., 2013; 
Kalwij et al., 2019). Specifically, we conducted an independent t- test to compare the means

---

<!-- PAGE 12 -->

742

|

T A B L E   2

Items in the simulation games.

Option 1

Option 2

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

Option 1: Get HK$ 10,000 now option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 9000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 8000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 7000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 6000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 5000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 4000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 3000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 2000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 1000 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 500 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 100 now Option 2: Get HK$

10,000 one month later

Option 1: Get HK$ 10,000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 9000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 8000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 7000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 6000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 5000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 4000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 3000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 2000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 1000 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 500 now Option 2: Get HK$

10,000 one year later

Option 1: Get HK$ 100 now Option 2: Get HK$

10,000 one year later

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

1

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

---

<!-- PAGE 13 -->

|  743

across two groups in age, educational achievement, monthly personal income, monthly fam-
ily income, family assets, future time perspectives (mediator), temporal discounting shortly 
(mediator), temporal discounting in the distant future (mediator), financial attitudes (media-
tor) and financial planning (outcome variable). We used the Chi- square test to compare the 
male proportion differences between the experimental and control groups.

In the main analysis, we used multiple regression to investigate whether participants in 
the experimental group reported higher future time perspectives, lower temporal discount-
ing, more positive financial attitudes and better financial planning than those in the control 
group when controlling for the baseline status of these focal constructs. In the next step, we 
added background variables to the regression model to validate the results.

Finally, we used the structural model to confirm whether the Python- based financial pro-
jection could promote the outcome variable (ie, financial planning) via four mediators: future 
time perspectives, temporal discounting shortly, temporal discounting in the distant future, 
and financial attitudes. In the structural model, we controlled for the status of the four me-
diators and the outcome in the pretest. Additionally, we linked the Python- based financial 
projection to the four mediators and the outcome measured in the post- test. Moreover, we 
added pathways from four mediators to the outcome variable in the post- test.

R ESULTS

The Chi- square and t- tests showed no significant differences in all variables (mediators, 
outcome and background variables) between the experiment and the control group (see 
Table 3), suggesting that our group assignment was successful. The experimental results 
reported  in  Table  4  show  that  Python- based  financial  projection  expectedly  influenced 
all  mediators  and  the  outcome  variable.  Before  controlling  for  background  variables, 
the  Python- based  financial  projection  significantly  promoted  future  time  perspectives 
(β = 0.18, p < 0.05), financial attitudes (β = 0.22, p < 0.05), and financial planning (β = 0.24,

T A B L E   3   Descriptive statistics in the experimental and control groups.

Mean (standard deviation), %

Control group (N = 17)

Experimental group (N = 44)

Background variables

Gender, being male (%)

Age

Educational achievement

Monthly personal income

Monthly family income

Family asset

Mediators

Future time perspective

Temporal discounting shortly

46.7

29.23 (4.69)

5.47 (0.52)

2.57 (2.06)

4.14 (2.21)

2.62 (1.19)

3.69 (0.61)

667 (1371)

Temporal discounting in the distant future

1727 (1902)

Positive financial attitudes

4.26 (0.83)

32.6

30.09 (7.87)

5.39 (0.49)

2.73 (1.06)

4.17 (1.96)

2.35 (1.53)

3.70 (0.71)

360 (762)

1750 (1795)

4.20 (0.61)

Outcome variable

Financial planning

2.86 (0.77)

3.24 (0.88)

Note: The Chi- square and independent sample t- test showed no significant difference in all variables.

---

<!-- PAGE 14 -->

Temporal 
discounting in the 
distance futurea

−0.27

−0.29*

0.35*

0.10

−0.16

0.34

−0.04

0.23

−0.66**

0.26

744

|

T A B L E   4   Results of multiple linear regressions.

Experimental group

Pretest

Gender, being male (%)

Age

Educational achievement

Monthly personal income

Monthly family income

Family asset

Experimental group

Pretest

Gender, being male (%)

Age

Educational achievement

Monthly personal income

Monthly family income

Family asset

Future time 
perspectivea

Temporal 
discounting shortlya

0.18*

0.80***

0.18*

−0.21

0.81***

0.37*

−0.16*

−0.01

0.17*

−0.12

−0.010

0.10

−0.31*

0.37*

−0.14

0.25

0.06

−0.20

−0.39*

0.36*

Financial attitudesa

Financial planninga

0.22*

0.63***

0.21*

0.24*

0.19*

0.66***

0.67***

0.65***

−0.15

0.28*

−0.01

−0.28

0.05

−0.07

−0.09

0.26*

−0.05

−0.11

0.18

−0.26*

aPosttest scores. Standardized estimated coefficients are reported.
*p < 0.05; **p < 0.01; ***p < 0.001.

p < 0.05).  After  adding  the  background  variables  as  the  control,  the  participants  in  the 
experimental  group  reported  significant  improvement  in  all  mediator  and  outcome  vari-
ables  (ie,  increased  future  time  perspectives  (β = 0.18, p < 0.05),  reduced  temporal  dis-
counting shortly (β = −0.31, p < 0.05), reduced temporal discounting in the distance future 
(β = −0.29, p < 0.05), improved financial attitudes (β = 0.21, p < 0.05) and better financial 
planning (β = 0.19, p < 0.05)). Notably, the standardized effect of our Python- based finan-
cial  projection  on  temporal  discounting  was  much  larger  than  that  of  our  previous  per-
sonalized financial projection (−0.31 vs. −0.11), in which we did not present the projection 
design and coding to participants (ie, only showing them the projection outcomes in the 
mobile application).

Due to the limited sample size, we could not add background variables as controls in the 
structural  model.  Considering  that  the  experiment's  effects  on  two  temporal  discounting 
measures were significant only after adding control variables, we excluded them from the 
structural model as mediators. In the structural model, we tested the mediational effects of 
future  time  perspectives  and  financial  attitudes  on  financial  planning  among  participants. 
Based  on  the  results  shown  in  Figure  3,  financial  attitudes,  rather  than  future  time  per-
spectives, were a significant mediator. Specifically, positive financial attitudes fully mediated 
the impact of Python- based financial projection on financial planning. After practicing with 
the Python- based financial projection, participants showed more positive financial attitudes 
(β = 0.24, p < 0.05), which in turn reminded them that they could further optimize their finan-
cial planning and increase their intention to plan for personal finance (β = 0.57, p < 0.001). 
After modelling the mediational effect, we noticed that the direct effect of the Python- based 
financial projection on financial planning disappeared.

---

<!-- PAGE 15 -->

|  745

F I G U R E   3   Results of experiment- based structural model. *p < 0.05; **p < 0.01; ***p < 0.001.

D I SCUSS I O N

Research calls for upgrading standardized financial education, as its generic curriculum can 
only  promote  objective  financial  knowledge  but  is  insufficient  to  change  participants'  un-
derlying psychology and financial planning (Amagir et al., 2018; Kaiser & Menkhoff, 2020). 
Computer- based personalized financial projection could provide a solution, but our previous 
financial  projection  that  masked  its  working  mechanism  had  limited  effects  on  changing 
the participants' underlying psychology (Zhu et al., 2023). In response, this study upgraded 
our previous financial projection by using Python to disclose its coding. We added Python- 
based personalized financial projections to the standardized financial education. Then, we 
conducted  a  randomized  control  trial  among  a  sample  of  young  working  adults  in  Hong 
Kong to determine whether this newly added component could promote participants' finan-
cial planning by affecting their psychology (ie, promoting their future time perspectives and 
financial attitudes and reducing their temporal discounting).

We found that the Python- based personalized  financial  projection transformed  the  un-
derlying psychology of participants expectedly and overwhelmingly in several ways. First, 
although both Python- based and our previous financial projection (masking the coding de-
tails) were found to decrease temporal discounting, the former's standardized effect was al-
most three times as large as that of the latter (ie, Hypothesis 1 is supported). Python- based 
coding presents the design of financial projections and elaborates on why current financial 
choices determine future  financial status.  The coding  serves as a  bridge to  establish  the 
participants' psychological connectedness to their future selves. When participants are well 
guided from the present to the future, the future becomes less obscure, more vivid and more 
valuable. In contrast, our previous financial projection masked the design of the projection 
program  and  only  made  the  participants  learn  about  their  financial  status  covariates  with 
their current choice. The specific mechanism that links the present to the future remains a 
black box.

Second, the Python- based financial projection was found to significantly promote future 
time  perspectives  (ie,  Hypothesis  2  is  supported),  but  the  same  effect  was  not  found  in 
our previous financial projection masking the coding (Zhu et al., 2023). Our previous pro-
jection  only  allows  users  to  adjust  personal  inputs  (eg,  salary,  expenditure,  saving  rate), 
while Python- based projection enables participants to adjust personal inputs, background 
economic parameters (eg, interest rate, salary growth, inflation), and even the logic of the

---

<!-- PAGE 16 -->

746

|

projection program. In other words, the Python- based financial projection encourages par-
ticipants to project their financial status in the future based on their perceptions of economic 
prospects  in  society.  For  the  participant,  the  “the  projected  future”  no  longer  means  the 
future self alone but the future self in the future society. Python- based projection presents a 
more comprehensive simulation than the previous projection (that sets background parame-
ters as default and does not allow participants to integrate their perceptions of the economic 
environment into the financial projection). Unsurprisingly, therefore, Python- based projec-
tion significantly promoted future time perspectives by taking participants to see a more vivid 
and realistic future. In contrast, our previous financial projection (masking the coding) failed 
to do so (Zhu et al., 2023).

Third, we found that Python- based financial projections could significantly promote the 
financial attitudes of participants, supporting Hypothesis 4. In our previous experiment, stan-
dardized  financial  education  could  not  significantly  shape  financial  attitudes  (Zhu,  2020). 
Our previous investigation did not test the effect of personalized financial projection (mask-
ing the coding) on financial attitudes (Zhu et al., 2023). In this study, the Python- based fi-
nancial projection maximized participants' opportunity to engage in “active experimentation” 
highlighted in the ELT (Kolb et al., 2014). Participants have the opportunity to engage in a 
multitude of experiments through the dynamic adjustment of individual inputs— such as the 
proportion of salary dedicated to savings and personal investment— as well as broader eco-
nomic parameters like interest rates and inflation. The flexibility extends even to the code 
employed for projection. Within this framework, participants gain a comprehensive grasp of 
critical financial concepts, most notably compound interest. This understanding transcends 
different macroeconomic landscapes and diverse projection models tailored to individual life 
trajectories. In essence, this underscores the robustness of healthy financial practices— like 
consistent savings and prudent asset allocation for investment. These practices consistently 
contribute to the enhancement of future financial well- being, irrespective of an economy's 
macroeconomic fluctuations and the personalized course of one's life journey. In contrast, 
our preceding financial projection (masking the coding) limited participants to the realm of 
trial and error by solely adjusting personal inputs. Regrettably, this restricted approach may 
inadvertently propagate a misperception. Namely, participants might wrongly assume that 
prudent financial planning solely impacts long- term financial well- being within the confined 
scenario established by the projection system.

Finally,  we  stress  that  our  Python- based  financial  projection  significantly  promoted  fi-
nancial planning among participants and that positive financial attitudes fully mediated this 
effect, indicating Hypothesis 5 is supported. The entire mediation well echoes the theoreti-
cal foundation of personalized financial projection that it affects the financial behaviours of 
participants by changing their underlying psychology (Bartels & Urminsky, 2015; Wiener & 
Doescher, 2008). Our findings justified adding Python- based personalized financial projec-
tions to standardized financial education. Future research may examine financial education 
composed of two components and determine whether it  can simultaneously promote  ob-
jective  financial  knowledge,  financial  attitudes  and  financial  planning,  and  whether  stan-
dardized  financial  education  and  Python- based  financial  projection  interact  to  strengthen 
all effects.

While the Python- based financial projection training does encompass a substantial time 
investment— a comprehensive 5- hour instruction on Python basics followed by an additional 
2- hour training session focused on manipulating projection code— we firmly assert that this 
allocation of time and resources proves exceptionally efficient. This efficiency stems from 
the  profound  and  wide- ranging  positive  impacts  that  extend  beyond  the  confines  of  the 
outcome  variables  we  directly  measured.  The  personalized  projection  serves  as  a  vivid 
testament to the immense power of Python within the realm of financial management. This 
exposure often acts as a catalyst, motivating participants to delve deeper into the realm of

---

<!-- PAGE 17 -->

|  747

Python's capabilities. Some may be inspired to explore its applications in diverse financial 
calculations and planning scenarios, thereby broadening their horizons. It is not inconceiv-
able that participants could experience a transformation in their approach to understanding 
the financial landscape once they harness Python's prowess to discern the consequences 
of various financial activities.

In an era marked by pervasive digitization, where programming and algorithms drive 
enhanced production efficiency, familiarity with Python basics emerges as a definite ad-
vantage. The newfound grasp of Python programming might even spur some participants 
to contemplate its applicability beyond the financial realm. This could potentially extend to 
assisting with the execution of their occupational responsibilities, tapping into the versa-
tility of coding to streamline their professional tasks. In essence, despite the investment 
of  time,  the  Python- based  financial  projection  training  acts  as  a  gateway  to  a  realm  of 
practical skills and insights that have the potential to resonate far beyond the immediate 
training period.

LI M ITATI O NS

Two limitations should be stressed and both motivate future research to continue investigat-
ing the impact of Python- based financial projections on multidimensional financial literacy. 
First, our data did not show the significant mediational role of future time perspectives (ie, 
Hypothesis  3b  is  not  supported),  which  might  be  due  to  the  imperfect  design  of  the  data 
collection. With the two- wave data, the “effects” of mediators on the outcome variable are 
the cross- sectional associations. Adding a third wave may alter the findings and report the 
significant effect of the future time perspective on financial planning. Second, we did not test 
the mediational role of temporal discounting in financial planning (ie, Hypothesis 3a was not 
examined) due to the limited sample size. Our findings showed that Python- based finan-
cial projections significantly reduced temporal discounting after controlling for background 
variables. Unfortunately, however, we could not add background variables to the structural 
model  due  to  an  inadequate  degree  of  freedom  with  a  small  sample  size.  Extending  the 
sample size in future research could be a solution.

CO NCLUS I O NS

This  study  is  the  first  worldwide  to  integrate  Python  into  personal  finance  education.  We 
conducted a randomized control trial to examine the effectiveness of Python- based financial 
projection (experiment group: standardized financial education plus Python- based financial 
projection;  control  group:  standardized  financial  education).  We  found  that  Python- based 
financial projection promoted future time perspectives, financial attitudes and financial plan-
ning of young working adults in Hong Kong and reduced their temporal discounting. Positive 
financial attitudes fully mediated the positive effect of Python- based financial projections on 
financial planning. We also concluded that exposing the coding to participants strengthened 
the effect of personalized financial projection by comparing our results to those in our previ-
ous investigation. Inspired by these findings, we call for more Python- based themed finan-
cial projections (eg, housing planning and health planning) and believe they may benefit the 
overall financial planning of working adults. More importantly, our findings suggest upgrad-
ing  standardized  financial  education  (ie,  combining  standardized  financial  education  with 
Python- based  personalized  financial  projection).  The  former  promotes  objective  financial 
knowledge, while the latter works by changing underlying psychology and affecting financial 
planning.

---

<!-- PAGE 18 -->

748

|

F U N D I N G   I N F O R M AT I O N
The  work  described  in  this  paper  was  fully  supported  by  a  grant  from  the  Investor  and 
Financial Education Council in Hong Kong, China.

C O N F L I C T   O F   I N T E R E S T   S TAT E M E N T
The author declares no potential conflicts of interest with respect to the research, authorship 
and/or publication of this article.

D ATA   AVA I L A B I L I T Y   S TAT E M E N T
The data that support the findings of this study are available from the corresponding author 
upon reasonable request.

E T H I C S   S TAT E M E N T
The ethical approval was obtained from the Human Research Ethics Committee (HREC) of 
The Lingnan University (Hong Kong) before the data collection.

I N F O R M E D   C O N S E N T
Informed consent was obtained from all individual participants included in the study.

O R C I D
Alex Yue Feng Zhu

https://orcid.org/0000-0002-0056-7387

R E F E R E N C E S
Amagir, A., Groot, W., Maassen van den Brink, H., & Wilschut, A. (2018). A review of financial- literacy education

programs for children and adolescents. Citizenship, Social and Economics Education, 17(1), 56–80.

Bartels, D. M., & Urminsky, O. (2015). To know and to care: How awareness and valuation of the future jointly

shape consumer spending. Journal of Consumer Research, 41(6), 1469–1485.

Basile,  A.  G.,  &  Toplak,  M.  E.  (2015).  Four  converging  measures  of  temporal  discounting  and  their  relation-
ships  with  intelligence,  executive  functions,  thinking  dispositions,  and  behavioral  outcomes.  Frontiers  in 
Psychology, 6, 728–741.

Batty, M., Collins, J. M., & Odders- White, E. (2015). Experimental evidence on the effects of financial education 
on  elementary  school  students'  knowledge,  behavior,  and  attitudes.  Journal  of  Consumer  Affairs,  49(1), 
69–96.

Becchetti, L., Caiazza, S., & Coviello, D. (2013). Financial education and investment attitudes in high schools:

Evidence from a randomized experiment. Applied Financial Economics, 23(10), 817–836.

Berry,  J.,  Karlan,  D.,  &  Pradhan,  M.  (2018).  The  impact  of  financial  education  for  youth  in  Ghana.  World

Development, 102, 71–89.

Chapman,  G.  B.  (1996).  Temporal  discounting  and  utility  for  health  and  money.  Journal  of  Experimental

Psychology: Learning, Memory, and Cognition, 22(3), 771–791.

Chou, K. L., Yu, K. M., Chan, W. S., Wu, A. M., Zhu, A. Y., & Lou, V. W. (2015). Perceived retirement savings 
adequacy in Hong Kong: An interdisciplinary financial planning model. Ageing & Society, 35(8), 1565–1586.
Douissa, I. B. (2020). Factors affecting college students' multidimensional financial literacy in the Middle East.

International Review of Economics Education, 35, 100173.

Fajnzylber, E., & Reyes, G. (2015). Knowledge, information, and retirement saving decisions: Evidence from a

large- scale intervention in Chile. Economia, 15(2), 83–117.

Fuentes, O., Lafortune, J., Riutort, J., Tessada, J., & Villatorok, F. (2022). Personalized information as a tool to im-
prove pension savings: Results from a randomized control trial in Chile. Economic Development and Cultural 
Change. Advanced access online.

Garcia, M. J. R. (2013). Financial education and behavioral finance: New insights into the role of information in

financial decisions. Journal of Economic Surveys, 27(2), 297–315.

Goda, G. S., Manchester, C. F., & Sojourner, A. J. (2014). What will my account really be worth? Experimental 
evidence on how retirement income projections affect saving. Journal of Public Economics, 119, 80–92.
Hershfield, H. E., Goldstein, D. G., Sharpe, W. F., Fox, J., Yeykelis, L., Carstensen, L. L., & Bailenson, J. N. (2011). 
Increasing  saving  behavior  through  age- progressed  renderings  of  the  future  self.  Journal  of  Marketing 
Research, 48(Spl), S23–S37.

---

<!-- PAGE 19 -->

|  749

Hershfield, H. E., & Bartels, D. M. (2018). The future self. In G. Oettingen, A. T. Sevincer, & P. M. Gollwitzer (Eds.),

The psychology of thinking about the future (pp. 89–109). Guilford.

Hizgilov,  A.,  &  Silber,  J.  (2020).  On  multidimensional  approaches  to  financial  literacy  measurement.  Social

Indicators Research, 148(3), 787–830.

Humber, M. (2018). Personal finance with python: Using pandas, requests, and recurrent. Apress.
Kaiser,  T.,  &  Menkhoff,  L.  (2020).  Financial  education  in  schools:  A  meta- analysis  of  experimental  studies.

Economics of Education Review, 78, 101930.

Kalwij, A., Alessie, R., Dinkova, M., Schonewille, G., Van der Schors, A., & Van der Werf, M. (2019). The effects 
of financial education on financial literacy and savings behavior: Evidence from a controlled field experiment 
in Dutch primary schools. Journal of Consumer Affairs, 53(3), 699–730.

Kolb, D. A., Boyatzis, R. E., & Mainemelis, C. (2014). Experiential learning theory: Previous research and new 
directions. In R. J. Sternberg & L. F. Zhang (Eds.), Perspectives on thinking, learning, and cognitive styles 
(pp. 227–248). Routledge.

Li, J., Hodgson, N., Lyons, M. M., Chen, K. C., Yu, F., & Gooneratne, N. S. (2020). A personalized behavioral 
intervention implementing mHealth technologies for older adults: A pilot feasibility study. Geriatric Nursing, 
41(3), 313–319.

Li, Q., Mintz, Y., Gavin, K., & Voils, C. (2023). An adaptive optimization approach to personalized financial incen-

tives in mobile behavioral weight loss interventions. arXiv Preprint. arXiv:2307.00444.

Lyons, A. C., & Kass- Hanna, J. (2021). A multidimensional approach to defining and measuring financial literacy 
in the digital age. In G. Nicolini & B. J. Cude (Eds.), The Routledge handbook of financial literacy (pp. 61–76). 
Routledge.

MacLeod, S., Musich, S., Hawkins, K., & Armstrong, D. G. (2017). The growing need for resources to help older

adults manage their financial and healthcare choices. BMC Geriatrics, 17(1), 1–9.

Marques, S., Mariano, J., Lima, M. L., & Abrams, D. (2018). Are you talking to the future me? The moderator role 
of  future  self- relevance  on  the  effects  of  aging  salience  in  retirement  savings.  Journal  of  Applied  Social 
Psychology, 48(7), 360–368.
Mosh. (2022). https://codew ithmo sh.com/
Noh,  M.  (2022).  Effect  of  parental  financial  teaching  on  college  students'  financial  attitude  and  behavior:  The

mediating role of self- esteem. Journal of Business Research, 143, 298–304.

OECD. (2017). PISA 2015 Results (Volume IV). OECD Publishing.
OECD. (2019). OECD/INFE report on financial education in APEC economies. OECD Publishing.
Oyserman, D., Bybee, D., Terry, K., & Hart- Johnson, T. (2004). Possible selves as roadmaps. Journal of Research

in Personality, 38, 130–149.

Pronin,  E.,  &  Ross,  L.  (2006).  Temporal  differences  in  trait  self- ascription:  When  the  self  is  seen  as  an  other.

Journal of Personality and Social Psychology, 90(2), 197–209.

PYPI. (2020). PYPL PopularitY of programming language. https://pypl.github.io/PYPL.html
Rai, K., Dua, S., & Yadav, M. (2019). Association of financial attitude, financial behaviour and financial knowledge 
towards financial literacy: A structural equation modeling approach. FIIB Business Review, 8(1), 51–60.
Rutt, J. L., & Löckenhoff, C. E. (2016). From past to future: Temporal self- continuity across the life span. Psychology

and Aging, 31(6), 631–639.

Salignac, F., Hamilton, M., Noone, J., Marjolin, A., & Muir, K. (2020). Conceptualizing financial wellbeing: An eco-

logical life- course approach. Journal of Happiness Studies, 21, 1581–1602.

Salignac,  F.,  Marjolin,  A.,  Reeve,  R.,  &  Muir,  K.  (2019).  Conceptualizing  and  measuring  financial  resilience:  A

multidimensional framework. Social Indicators Research, 145, 17–38.

Seaman, K. L., Abiodun, S. J., Fenn, Z., Samanez- Larkin, G. R., & Mata, R. (2022). Temporal discounting across

adulthood: A systematic review and meta- analysis. Psychology and Aging, 37(1), 111–124.

Serido, J., Shim, S., & Tang, C. (2013). A developmental model of financial capability: A framework for promoting 
a successful transition to adulthood. International Journal of Behavioral Development, 37(4), 287–297.
Shim, S., Serido, J., Tang, C., & Card, N. (2015). Socialization processes and pathways to healthy financial devel-

opment for emerging young adults. Journal of Applied Developmental Psychology, 38, 29–38.

Tomar, S., Baker, H. K., Kumar, S., & Hoffmann, A. O. (2021). Psychological determinants of retirement financial

planning behavior. Journal of Business Research, 133, 432–449.

VanderPlas, J. (2016). Python data science handbook: Essential tools for working with data. O'Reilly Media,

Inc.

Walstad, W., Urban, C., Asarta, C. J., Breitbach, E., Bosshardt, W., Heath, J., O'Neill, B., Wagner, J., & Xiao, J. 
J. (2017). Perspectives on evaluation in financial education: Landscape, issues, and studies. The Journal of 
Economic Education, 48(2), 93–112.

Walstad, W. B., Rebeck, K., & MacDonald, R. A. (2010). The effects of financial education on the financial knowl-

edge of high school students. Journal of Consumer Affairs, 44(2), 336–357.

Wiener, J., & Doescher, T. (2008). A framework for promoting retirement savings. Journal of Consumer Affairs,

42(2), 137–164.

---

<!-- PAGE 20 -->

750

|

Xiao, J. J., & O'Neill, B. (2016). Consumer financial education and financial capability. International Journal of

Consumer Studies, 40(6), 712–721.

Zhu, A. Y. F. (2018). Parental socialization and financial capability among Chinese adolescents in Hong Kong.

Journal of Family and Economic Issues, 39(4), 566–576.

Zhu, A. Y. F., Fung, H. H. L., Chan, W. S., & Chou, K. L. (2023). Promoting financial preparation for retirement of 
working adults: A temporal discounting intervention. Under review by Journal of Applied Gerontology.
Zhu, A. Y. F., Yu, C. W. M., & Chou, K. L. (2021). Improving financial literacy in secondary school students: An

randomized experiment. Youth & Society, 53(4), 539–562.

Zhu, A. Y. F. (2020). Impact of financial education on adolescent financial capability: Evidence from a pilot ran-

domized experiment. Child Indicators Research, 13(4), 1371–1386.

How to cite this article: Zhu, A. Y. F. (2024). Upgrading financial education by adding 
Python- based personalized financial projection: A randomized control trial. British 
Journal of Educational Technology, 55, 731–750. https://doi.org/10.1111/bjet.13401

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received: 24 March 2023 | Accepted: 30 September 2023
DOI: 10.1111/bjet.13401
ORIGINAL ARTICLE
Upgrading financial education by adding
Python- based personalized financial
projection: A randomized control trial
Alex Yue Feng Zhu
Department of Social Sciences and Policy
Studies, The Education University of Hong Abstract
Kong, Hong Kong, China Research has shown that even though standardized
financial education has gained prevalence to pro-
Correspondence
Alex Yue Feng Zhu, Department of mote financial literacy over the past decade, it has
Social Sciences and Policy Studies, The had little effect on personal financial planning. The
Education University of Hong Kong, 10 Lo
present study used a randomized control trial to ex-
Ping Road, Tai Po, N.T., Hong Kong, China.
Email: yfzhu@eduhk.hk amine the effectiveness of a Python- based person-
alized financial projection on young working adults
Funding information
The Investor and Financial Education in Hong Kong, to examine if and how this approach
Council in Hong Kong, China improves their financial planning. Participants as-
signed to the experiment group received standard-
ized financial education and Python- based financial
projections, while those in the control group only
received standardized financial education. The as-
sessment based on the two- wave data showed that
Python- based financial projection promoted future
time perspectives, reduced temporal discounting,
and improved financial planning via the full media-
tion of promoting financial attitudes. Although numer-
ous applications for personal financial planning exist
(such as Wallet, Walnut, Monefy, and Money View),
our Python- based financial projection stands out as
the pioneering solution tailored for the hands- on ma-
nipulation of programming code to effectively man-
age personal finances. Our findings suggest a new
track to upgrade personalized financial projection
and standardized financial education and contribute
generously to the development of personal finance
education.
This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits
use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial
purposes.
© 2023 The Authors. British Journal of Educational Technology published by John Wiley & Sons Ltd on behalf of British
Educational Research Association.
|
Br J Educ Technol. 2024;55:731–750. wileyonlinelibrary.com/journal/bjet 731

732 | ZHU
KEYWORDS
financial planning, personal finance education, personalized
financial projection, Python, standardized financial education,
temporal discounting
Practitioner notes
What is already known about this topic
• Standardized financial education promotes objective financial knowledge.
• Standardized financial education has a limited effect on personal financial
planning.
• Classical personalized financial projection promotes personal financial planning,
but the effect is small.
What this paper adds
• Introduction of a novel Python- based personalized financial projection by manipu-
lating projection code.
• The evidence that Python- based personalized financial projection more strongly
improves personal financial planning, compared to the classical personalized fi-
nancial projection.
• The evidence why Python- based personalized financial projection can improve
personal financial planning.
Implications for practice and/or policy
• Facilitating engagement of young working adults with personalized finance plan-
ning through the use of a Python- based intervention.
• Integrating Python- based personalized financial projection into standardized fi-
nancial education in the school setting.
• Using Python as the platform to design more topic- specific financial education
module.
INTRODUCTION
There has been a surge in access to financial technology and diversified financial prod-
ucts and services in modern societies, such as Hong Kong. The rise in financial respon-
sibility among individual consumers necessitates the equipment of basic financial literacy.
Recently, the personal finance literature described financial literacy as a multidimensional
construct rather than objective financial knowledge alone (Hizgilov & Silber, 2020; Lyons
& Kass- Hanna, 2021). Consumers with high financial literacy refer to those who develop a
sound understanding of personal finance terms, hold positive attitudes toward healthy finan-
cial habits, have self- esteem in financial practice and actively engage in financial planning
(Rai et al., 2019; Xiao & O'Neill, 2016). Understanding financial literacy as a multidimen-
sional construct carries significant importance because personal financial outcomes are
influenced by a combination of factors, including financial knowledge, attitudes, confidence,
planning, and decision- making (Douissa, 2020; Hizgilov & Silber, 2020). Isolating any one
of these factors overlooks the intricate interplay between them and their collective impact
on financial well- being. This multidimensional view has a profound impact on how financial
literacy should be assessed, and places heightened emphasis on the necessity for financial
education programs to be comprehensive.
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 733
Standardized financial education has gained prevalence among practitioners in the last
decade to promote financial literacy (Amagir et al., 2018). However, it has little effect on
personal financial planning, although it improves objective financial knowledge (Kaiser &
Menkhoff, 2020). The main limitation of a generic intervention is that it cannot be flexibly
adjusted to fit an individualized financial status and needs. On the other hand, personalized
financial intervention is more potent in shaping financial planning because it can affect par-
ticipants' underlying psychology (Bartels & Urminsky, 2015; Wiener & Doescher, 2008). In
particular, personalization harnesses the power of intrinsic motivation by aligning with an
individual's personal values and aspirations (Li et al., 2020, 2023). When financial advice
deeply resonates with a person's goals, it sparks a heightened motivation to actively engage
in personal financial management. Furthermore, the act of tailoring advice to suit each indi-
vidual's distinct circumstances fosters a robust sense of self- efficacy (Li et al., 2020). This,
in turn, empowers them to embark on proactive measures within their financial planning
journey.
Behavioural scientists have developed psychological models that explain why people
actively join in personal financial planning (Serido et al., 2013; Tomar et al., 2021). Two
models were tested and validated by our team in Hong Kong using data collected from
adolescents and working adults (Zhu, 2018; Chou et al., 2015). Our results suggest that
future perspective, temporal discounting, and financial attitudes play significant mediational
roles in the pathway toward skilful financial planning. There are hierarchical relationships
among future time perspectives, temporal discounting, and financial attitudes. Future time
perspectives only capture attitudes toward the future, while temporal discounting reflects
intertemporal choices (ie, how a consumer will choose between the present and the future)
(Chapman, 1996; Seaman et al., 2022). When consumers perceive that the future is more
valuable than the present (ie, low temporal discounting), there will be a willingness to save
and invest for the future and to engage in budget and consumption control in the present (ie,
positive financial attitudes). Therefore, a personalized financial intervention manipulating fu-
ture time perspectives, temporal discounting, and financial attitudes may promote the skills
and intentions of financial planning.
Temporal discounting theory suggests that people normally devalue the future because
of their psychological disconnectedness from the future (Bartels & Urminsky, 2015). Without
cognitive intervention, people can hardly establish the vividness of and a connection to the
future self, not to mention sacrificing immediate temptation for the benefit of the future self
(eg, controlling immediate spending and saving for the future). That is why behavioural sci-
entists resort to computer- based interventions to promote the vividness of the future, such
as age- progressed renderings with virtual reality technologies, discussion with future self-
produced AI technology, and remarkably personalized financial projection with simulation
techniques (Goda et al., 2014; Hershfield et al., 2011; Marques et al., 2018).
Recently, our team conducted a three- arm experiment to examine the effectiveness of
a computer- based personalized financial projection among working adults in Hong Kong.
The projection simulates the financial resources accumulated in the distant future based on
a working adult's current earnings, savings and investment behaviours (Zhu et al., 2023).
We masked the working mechanism of the projection and created a mobile application that
showed the projected financial outcomes to the participants after they input their current fi-
nancial choices. The experimental results showed that the personalized financial projection
significantly reduced temporal discounting, but the effect was small (b* = −0.11). The find-
ings also revealed that the projection did not significantly shape future time perspectives.
Both limitations are likely due to a direct connection between the present and the future,
without vivid guidance on how the present and future selves are connected (Oyserman
et al., 2004). One potential solution could involve introducing participants to the coding of
a computer- based personalized financial projection. This approach would grant them the
opportunity to manipulate projection code, thus enabling the forecasting of individualized
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

734 | ZHU
financial trajectories. This process would serve to elucidate the intricate interplay and con-
nection between the present and the future.
Python, created by Guido van Rossum and released in 1991, was recognized as the
most popular coding tool in the world by the Popularity of Programming Language Index
(PYPI, 2020). Python has been observed to have a low threshold for learners and powerful
computing, design and simulation functions. Humber (2018) adopted Python as a coding
tool to simulate personal financial planning. Considering that Python is user- friendly, in this
study, we used Python as the coding language to develop a personalized financial projection
program. Specifically, we created an experimental condition in which we taught young work-
ing adults basic Python grammatical rules and how to manipulate projection code developed
by us to create “their” financial projections. The primary objective of this study was to test
whether Python- based personalized financial projection could achieve the following:
1. More strongly reduce temporal discounting compared to our previous financial pro-
jection, which masks the coding.
2. Promote future time perspectives and financial attitudes.
3. Improve financial planning via the mediation of temporal discounting, future time perspec-
tives and financial attitudes.
LITERATURE REVIEW
The motivation for upgrading standardized financial education
There is a shared sense of lifelong financial education that educators should start introduc-
ing basic financial knowledge in primary schools, delivering standardized and comprehen-
sive financial education in secondary schools, and offering topic- specific financial training
among college students and working adults (Amagir et al., 2018; Garcia, 2013; Walstad
et al., 2017). Financial education has even been extended to older adults to assist them in
managing their healthcare choices (MacLeod et al., 2017).
By the end of 2017, more than 70 countries had developed national strategies to compre-
hensively promote the financial literacy of the next generation of young adults (OECD, 2017).
Educational authorities have added standardized financial training to the secondary- level
curriculum structure in 15 of the 17 Asia- Pacific Economic Cooperation (APEC) economies
(OECD, 2019). Considering that there has been no standardized financial education in sec-
ondary schools in Hong Kong, our team introduced an international standardized financial
curriculum, the Financial Fitness for Life (FFFL), to Hong Kong adolescents and conducted
the first randomized control trial in Asia to assess its impacts on multiple dimensions of
financial literacy (Zhu, 2020; Zhu et al., 2021). The FFFL was developed by the Council for
Economic Education in the U.S. and was appraised as the most comprehensive standard-
ized financial education in the international community (Batty et al., 2015; Berry et al., 2018;
Walstad et al., 2010). The FFFL teaches participants basic concepts to make sound de-
cisions regarding earning income, spending, saving, borrowing, investing and managing
money.
Our experiment showed that the FFFL was sufficiently powerful to enhance the objective
financial knowledge of participants but inadequate to bring positive change to their financial
planning (ie, saving, budgeting and spending control; Author, 2020; Author et al., 2021).
Recent systematic reviews and meta- analyses consistently suggest that standardized finan-
cial education is more potent in shaping objective financial knowledge than financial plan-
ning behaviours (Amagir et al., 2018; Kaiser & Menkhoff, 2020). Hence, this paper proposes
intelligent solutions to upgrade standardized financial education to promote participants'
financial planning. In this study, we designed and conducted a Python- based personalized
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 735
financial projection and examined its intervention mechanism (ie, how it promoted financial
planning for participants by changing future time perspectives, temporal discounting and
financial attitudes).
Python- based personalized financial projection, future time
perspectives and temporal discounting
Individuals experience multiple events that break the life course into several independent
sections (Rutt & Löckenhoff, 2016). Typical events include going to college as a freshman,
getting married, studying overseas and relocating family. People may perceive these events
as turning points that reduce the discontinuity of the whole life course (Hershfield & Bartels,
2018). When there is inadequate continuity between the present and the future, people do
not believe that the future quality of life is related to the present sacrifice. They would rather
believe that these turning points (ie, life events) determine future well- being in a random
walk. The future can never be valuable when vague, uncertain and obscure (Hershfield
et al., 2011; Pronin & Ross, 2006).
Unlike financial projection without presenting coding details (eg, Fajnzylber & Reyes, 2015;
Fuentes et al., 2022; Goda et al., 2014), Python- based financial projection can reduce tem-
poral discounting more strongly and improve future time perspectives. Python- based coding
links the present to the future by convincing users that current financial choices determine
future financial outcomes, thereby increasing the perceived continuity of life courses. The
coding presents a detailed simulation model illustrating how financial status and choice
develop into future financial outcomes. The perceived value of the future automatically in-
creases when the future is no longer an ambiguous object but a predictable outcome follow-
ing a clear development track. Therefore, we propose the following hypotheses:
H1. Python- based financial projection reduces temporal discounting more
strongly.
H2. Python- based financial projection promotes future time perspectives.
H3a & H3b. Python- based financial projection improves personal financial
planning by the mediation of reducing temporal discounting and promoting future
time perspectives, respectively.
Python- based personalized financial projection and financial attitudes
Experiential learning theory (ELT) constructs a holistic model that fits the learning process
and human development in different fields (Kolb et al., 2014), such as financial literacy
(composed of knowledge, attitudes and behaviours). People must experience two stages
to develop sound financial literacy: grasping experience and transformation experience
(Noh, 2022). The grasping experience contains substantial financial experience (eg, by fre-
quent financial practice) and abstract concepts (eg, by standardized financial education).
To gain transformation experience, learners must develop reflective observation (eg, by
observing the financial practices of others) or active experimentation (eg, by trial and error).
Our previously validated model among youth in Hong Kong reveals that when people
engage in a type of financial practice with high frequency (ie, substantial financial experi-
ence in the grasping experience of ELT), they develop financial habits without promoting
corresponding financial attitudes (Zhu, 2018). Additionally, our previous experiment showed
that standardized financial education (ie, abstract concepts in the grasping experience of
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

736 | ZHU
ELT) helped participants acquire financial concepts but failed to shape their positive finan-
cial attitudes (Zhu, 2020). Hence, scholars should seek solutions to improve financial at-
titudes by promoting a transformation experience of ELT (reflective observation or active
experimentation).
The Python- based personalized financial projection design allows participants to be
observers and practitioners simultaneously. Participants may adjust the parameters (eg,
interest rate, inflation rate, investment rate of return) and the inputs in the program (eg,
salary, age, expenses) to review the financial details of others and themselves. They may
adjust these variables multiple times to identify the best planning strategy to achieve their
ideal financial outcomes (eg, experimentation). In comparison, classical personalized finan-
cial projections do not allow for the adjustment of parameters and present a simple and
friendly interactive window (eg, a mobile application) for participants to adjust inputs only
(Fajnzylber & Reyes, 2015; Fuentes et al., 2022; Goda et al., 2014). Furthermore, the utiliza-
tion of Python- based financial projection empowers participants with the capability to refine
the projection process. This is achieved through the revision of pre- existing code or the
incorporation of entirely new code elements, thereby fostering robust experimentations and
explorations. In summary, Python- based financial projection motivates participants to “play”
the model and immerse themselves in concrete realities to learn and develop financial liter-
acy, which utilizes the core advantage of ELT. Therefore, we offer the following hypotheses:
H4. Python- based financial projection improves financial attitudes.
H5. Python- based financial projection promotes personal financial planning by
the mediation of improved financial attitudes.
METHOD
General design
This study aimed to upgrade standardized financial education by adding a Python- based
personalized financial projection. To justify this, we designed a randomized control trial to
test how and to what extent the Python- based financial projection improved financial lit-
eracy. Participants in the experimental group received standardized financial education as
well as Python- based financial projections, whereas participants in the control group solely
received standardized financial education. This design enabled us to examine the unique
effect of Python- based financial personalized projection on three mediators (ie, future time
perspectives, temporal discounting and financial attitudes) and one outcome (ie, financial
planning of participants).
Standardized financial education
We implemented FFFL modules to conduct standardized financial education. The FFFL
has been validated among young people in Hong Kong (Zhu et al., 2021). Financial top-
ics in the FFFL (ie, earning income, spending, saving, borrowing, investing and managing
money) were seamlessly connected using the life course financial planning model (Salignac
et al., 2020). For example, savings and investment are necessary to establish financial well-
being throughout life, while budgeting and spending control are prerequisites to saving and
engaging in investment. We integrated multiple teaching strategies into the two- hour train-
ing, including lectures, case studies, group discussions, videos, games and role- playing.
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 737
Python- based personalized financial projection
The Python- based personalized financial projection is the core component of our interven-
tion. It is composed of five hours of training in basic Python grammatical rules, two hours of
coding skills for beginners and applying two financial projection models to facilitate financial
planning. This intervention entails the manipulation of projection code developed by our
team to cater to individualized circumstances. Mosh (2022) developed a short course to fa-
miliarize beginners with Python skills in around 10 hours. We used it to train the participants
in Python grammar, but shortened it to five hours because we needed to cover coding skills
related to two financial projection models only. The details are reported in Table 1.
Bearing in mind that we aimed to improve the financial planning of participants by pro-
moting their future time perspectives and weakening temporal discounting, we designed
two financial projection models to more vividly demonstrate the time value of money. The
first model (ie, the money management model) simulated an individual's earning, spending,
saving and investment behaviours in the upcoming years to show that compound interest
could appreciate wealth and build financial well- being in the future. With a foundational un-
derstanding of Python- based coding at their disposal, participants were encouraged to ac-
tively calibrate economic parameters (such as interest rates, inflation rates and investment
returns) and individual inputs (including monthly expenditures and saving rates) in the pro-
jection code we developed to simulate the progressive accumulation of wealth. Furthermore,
participants were allowed to introduce new code elements if they deemed it beneficial in mir-
roring their personalized financial trajectory. Paramount to this experience was the iterative
nature of the model, which vividly underscored the far- reaching consequences of contem-
porary decisions on future quality of life. Beyond this, participants were notably encouraged
to factor in the appreciation of money over time when arriving at financial decisions. The
structural flow of the first model is visually expounded upon in Figure 1.
Next, we developed the second model (eg, debt management with a credit card) to
help participants learn about the substantial future cost after falling into the “revolving
credit” trap when using a credit card for consumption. The model aimed to effectively
show that the total cost of consumption with revolving credit would be much higher than
the original price of the commodity, and the considerable pressure of repayment may
seriously lower the quality of life in the future. Analogous to the preceding model, partic-
ipants were invited to try multiple scenarios by adjusting the economic parameters (eg,
interest rates for borrowing, the most prolonged borrowing period) and personal inputs
(eg, monthly payments, loan periods without a contract). Concurrently, participants were
encouraged to refine existing code elements or even forge new ones if they believed
such modifications would enhance the personalization of the projection. Significantly,
these explorations underscored the pivotal link between present- day repayment actions
and future financial well- being. The procedural trajectory of the second model is visually
illustrated in Figure 2.
Participants
Python- based financial projection belongs to topic- specific financial education. According
to the life course financial education landscape, it best fits the working adult group (Walstad
et al., 2017). Young working adults are digital natives surrounded by computers and digital
devices and maintain a shorter psychological distance with a programming tool such as
Python. Therefore, we believe it is beneficial to limit the participants to young working adults
to maximize the potential effect of our intervention. Considering that personal financial sta-
tus is the fundamental condition for engaging in financial activities, there is a motivation to
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

738 | ZHU
.gnidoc
nohtyP
cisaB
1
ELBAT
emiT
noitpircseD
cipoT
ruoh
1
gnidoc
desab
-nohtyP
gninnur
dna mrahCyP
gnillatsnI
tnempoleved
margorp
fo
tnemnorivnE
tcejbo
na ot
retniop
a si taht
eman
cilobmys
A
elbairaV
loob
dna
,gnirts
,tniop
gnitaolf
,regetnI
atad
fo
epyT
)resu
eht
morf yllausu(
tupni
eht morf
enil
a gnidaeR
noitcnuf
tupnI
rehtona
ot
epyt atad
eno
morf
noisrevnoc
gnimrofreP
epyt
atad
gnimrofsnarT
s'gnirts
eht
edisni
meht
tresni dna
)s(eulav
deificeps
eht
gnittamroF
gnirtS
tamroF
redlohecalp
ruoh
5.0
,)%(
redniamer
,)*(
noitacilpitlum
,)/( noisivid
,)−(
noitcartbus
,)+( noitiddA
elur
ecnedecerp
srotarepo
dna
noitaluclac
lacitamehtaM
)//( noisivid
regetni dna
,)**(
erauqs
ruoh
5.0
.ton
ro
detucexe
eb
ot
deen stnemetats
niatrec
rehtehw
gnidiceD
tnemetats
”fi“
ehT
ruoh
5.0
snoitarepo
TON lacigoL
dna
RO lacigoL
,DNA lacigoL
srotarepo
lacigoL
ruoh
5.0
tem
si
noitidnoc
niatrec
a
litnu edoc
kcolb
a gninnuR
pool
”elihw“
ehT
ruoh
4.0
)tsil
a
,ge(
ecneuqes
a
revo gnitaretI
pool
”rof“
ehT
ruoh
4.0
elbaegnahc
dna
deredro
si
hcihw
noitcelloc
A
tsiL
ruoh
4.0
elbairav
elgnis
a ni smeti
elpitlum
gnirotS
elpuT
ruoh
4.0
seulav
dna
syek fo sriap
suoirav
fo erutcurts
dehsah
A
yranoitciD
ruoh
4.0
dellac
si ti nehw
snur
ylno hcihw
edoc
fo kcolb
A
snoitcnuF
.)6102(
salPrednaV
morf
detcartxe
saw
noitpircsed
ehT
:etoN
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by Cochrane
Philippines,
Wiley
Online
Library on [24/06/2026].
See the Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 739
FIGURE 1 Model of the money management.
FIGURE 2 Model of the debt management with a credit card.
further limit the participant to those with solid earning power. Overall, the participant has to
meet the following criteria:
1. Aged 18– 35 years.
2. Full- time administrative staff at public universities in Hong Kong, with a stable monthly
income above the median in Hong Kong.
3. Not holding a degree in finance or computer science.
4. Not having taken any standardized financial courses.
5. Not a Python coder.
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

740 | ZHU
Procedures
We emphasize the quantitative nature of our study, which hinges on the collection of first-
hand data to rigorously evaluate a two- arm experimental model. The ensuing sections de-
lineate the meticulous procedure we employed, elucidating our efforts to ensure robustness
in our experimental design and data collection.
The research team appointed two part- time research officers. The first was responsible
for recruiting participants, preparing assessment instruments and managing research data.
The second staff member was assigned duties related to Python and FFFL (ie, preparing
intervention materials and developing the Python- based financial projection program). We
used “Wix.com (a free online website builder)” to create a public platform that published
comprehensive information regarding our intervention, including indicative contents, our
team members and the confirmed timetable. To fit the timetable of the university staff, we
offered experimental conditions on Friday night and daytime on the following Saturday. The
arrangement ensured that there was a low likelihood of attrition during the intervention. All
teaching and learning activities were arranged online via Zoom meetings.
The email contacts of full- time administrative staff in eight publicly funded universities
in Hong Kong are open. We created the registration link using Qualtrics XM and attached
it to the mass email invitation. In the invitation, we detailed the research objective and the
significance of this study in the personal finance landscape in Hong Kong and guaranteed
that those who completed the training and two tests (ie, pretest and post- test) would get a
supermarket cash coupon worth HK$100 (= US$12.90).
People who registered for the intervention received a pretest link. We randomly assigned
participants who completed the pretest to either the experiment or the control group. For
the experiment group, we offered the intervention in two rounds (ie, on the first and second
weekends of January 2023). In each round, we accepted at most 25 participants to ensure
adequate communication between the trainer and each trainee. We conducted the post- test
after they completed both the FFFL and Python- based financial projections. The training in
the experimental group lasted 9 hours in total.
In the control group, we only taught the FFFL module (ie, standardized financial education
lasting for only 2 hours) between the pretest and post- test. The FFFL was delivered on the
third weekend of January 2023. However, for ethical considerations, we offered the same
Python- based financial projection to the control group participants after they completed the
post- test. In other words, the Python- based financial projection in the control group was not
part of our randomized control trial. It was only a gift to the participants in the control group.
Measurements
In the pretest and post- test, we adopted assessment instruments that have been validated
among working adults in Hong Kong to measure potential mediators (ie, future time perspec-
tive, temporal discounting and financial attitudes) and one outcome variable (ie, financial
planning) (Chou et al., 2015, Zhu et al., 2021, 2023). Future time perspectives were as-
sessed using six items on a five- point scale (1 = highly disagree; 5 = highly agree) extracted
from Tomar et al. (2021), with excellent internal consistency reliability in the pretest and post-
test (α = 0.88 and 0.90). The six items included the following:
• “I like to think about what the future will hold.”
• “I enjoy thinking about how I will live years from now in the future.”
• “I look forward to life in the distant future.”
• “According to me, it is important to have a long- term perspective in life.”
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 741
• “My close friend would describe me as future- oriented.”
• “I look forward to a long journal toward the distant future.”
We invited participants to play two games to assess temporal discounting (ie, making
hypothetical choices between an immediate reward and a delayed fixed reward) (Basile &
Toplak, 2015). In the first game, we asked participants to choose between HK$10,000 now
and HK$10,000 one month later. We gradually reduced the amount that could be obtained
now and created an additional 11 scenarios for participants to choose from two options.
Once a turning point occurred (ie, participants switched to get the amount one month later),
the present value of HK$10,000 one month later (ie, the reversed temporal discounting) was
identified. In the second game, we repeatedly asked participants to make 12 hypothetical
choices but adjusted the delayed period from one month to one year. The total 24 items in
the two games are presented in Table 2. We identified the temporal discounting shortly and
in the distant future by reviewing participants' choices.
Financial attitudes were assessed with three items developed and used in Shim
et al.'s (2015) study. We asked participants to report their agreement with three financial
behaviours on a five- point scale (1 = highly disagree; 5 = highly agree), including:
• “You should make sure there is a sufficient balance in your bank account.”
• “You should clean the debts in your credit card every month.”
• “You should save to prepare for emergencies.”
The internal consistency across the three items was adequate (pretest: α = 0.87; post- test:
α = 0.85). Financial planning was measured by a single item, “Please report your financial
planning activities (Salignac et al., 2019).” The answers were calibrated on a four- point scale
(1 = In the current financial status, it is impossible for me to engage in any financial planning
activity; 4 = In the current financial status, it is effortless to plan for my finance).
In addition to the mediators and the outcome variable, we assessed the background
variables, ie, educational achievement, monthly personal income, monthly family income,
and total family assets. We asked participants to report their educational achievements by
choosing from 1 (no formal schooling) to 6 (a postgraduate degree or above). Financial sta-
tus is a critical prerequisite to financial planning, so it must be measured among participants
and added as the control in main analysis. Considering that financial status was sensitive
information to participants, we invited them to choose a range rather than report specific
amounts when measuring monthly personal income, monthly family income, and total family
assets. The results were as follows:
• Monthly personal income ranged from 1 (HK$18,700 − HK$19,999, UD$1 = HK$7.75) to 6
(HK$60,000 or above).
• Monthly family income ranged from 1 (HK$18,700 − HK$19,999) to 6 (HK$100,000 or
above).
• Total family assets ranged from 1 (HK$0 − HK$ 499,999) to 11 (HK$5,000,000 or above).
Data analysis
Following the standardized procedures of experiment- based intervention research, we
checked whether the group assignment (ie, assigning participants to either the experiment
or control group) was adequately random by examining whether there was a significant dif-
ference in mediators, outcome variables and background variables (Becchetti et al., 2013;
Kalwij et al., 2019). Specifically, we conducted an independent t- test to compare the means
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 14678535, 2024, 2, Downloaded from https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401 by Cochrane Philippines, Wiley Online Library on [24/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|
| 742                                     |     |          | ZHU      |
| --------------------------------------- | --- | -------- | -------- |
| TABLE 2  Items in the simulation games. |     |          |          |
|                                         |     | Option 1 | Option 2 |
Option 1: Get HK$ 10,000 now option 2: Get HK$
| 1   | 10,000 one month later                        | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
| 2   | Option 1: Get HK$ 9000 now Option 2: Get HK$  | 1   | 2   |
10,000 one month later
| 3   | Option 1: Get HK$ 8000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 4   | Option 1: Get HK$ 7000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 5   | Option 1: Get HK$ 6000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 6   | Option 1: Get HK$ 5000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 7   | Option 1: Get HK$ 4000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 8   | Option 1: Get HK$ 3000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 9   | Option 1: Get HK$ 2000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 10  | Option 1: Get HK$ 1000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one month later
| 11  | Option 1: Get HK$ 500 now Option 2: Get HK$  | 1   | 2   |
| --- | -------------------------------------------- | --- | --- |
10,000 one month later
| 12  | Option 1: Get HK$ 100 now Option 2: Get HK$  | 1   | 2   |
| --- | -------------------------------------------- | --- | --- |
10,000 one month later
| 13  | Option 1: Get HK$ 10,000 now Option 2: Get HK$  | 1   | 2   |
| --- | ----------------------------------------------- | --- | --- |
10,000 one year later
| 14  | Option 1: Get HK$ 9000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 15  | Option 1: Get HK$ 8000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 16  | Option 1: Get HK$ 7000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 17  | Option 1: Get HK$ 6000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 18  | Option 1: Get HK$ 5000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 19  | Option 1: Get HK$ 4000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 20  | Option 1: Get HK$ 3000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 21  | Option 1: Get HK$ 2000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 22  | Option 1: Get HK$ 1000 now Option 2: Get HK$  | 1   | 2   |
| --- | --------------------------------------------- | --- | --- |
10,000 one year later
| 23  | Option 1: Get HK$ 500 now Option 2: Get HK$  | 1   | 2   |
| --- | -------------------------------------------- | --- | --- |
10,000 one year later
| 24  | Option 1: Get HK$ 100 now Option 2: Get HK$  | 1   | 2   |
| --- | -------------------------------------------- | --- | --- |
10,000 one year later

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED   14678535, 2024, 2, Downloaded from https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401 by Cochrane Philippines, Wiley Online Library on [24/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|
PERSONALIZED FINANCIAL PROJECTION       743
across two groups in age, educational achievement, monthly personal income, monthly fam-
ily income, family assets, future time perspectives (mediator), temporal discounting shortly
(mediator), temporal discounting in the distant future (mediator), financial attitudes (media-
tor) and financial planning (outcome variable). We used the Chi- square test to compare the
male proportion differences between the experimental and control groups.
In the main analysis, we used multiple regression to investigate whether participants in
the experimental group reported higher future time perspectives, lower temporal discount-
ing, more positive financial attitudes and better financial planning than those in the control
group when controlling for the baseline status of these focal constructs. In the next step, we
added background variables to the regression model to validate the results.
Finally, we used the structural model to confirm whether the Python- based financial pro-
jection could promote the outcome variable (ie, financial planning) via four mediators: future
time perspectives, temporal discounting shortly, temporal discounting in the distant future,
and financial attitudes. In the structural model, we controlled for the status of the four me-
diators and the outcome in the pretest. Additionally, we linked the Python- based financial
projection to the four mediators and the outcome measured in the post- test. Moreover, we
added pathways from four mediators to the outcome variable in the post- test.
RESULTS
The Chi- square and t- tests showed no significant differences in all variables (mediators,
outcome and background variables) between the experiment and the control group (see
Table 3), suggesting that our group assignment was successful. The experimental results
reported in Table 4 show that Python- based financial projection expectedly influenced
all mediators and the outcome variable. Before controlling for background variables,
the Python- based financial projection significantly promoted future time perspectives
(β = 0.18, p < 0.05), financial attitudes (β = 0.22, p < 0.05), and financial planning (β = 0.24,
TABLE 3  Descriptive statistics in the experimental and control groups.
Mean (standard deviation), %
|     | Control group (N = 17) | Experimental group (N = 44) |
| --- | ---------------------- | --------------------------- |
Background variables
| Gender, being male (%)  | 46.7         | 32.6         |
| ----------------------- | ------------ | ------------ |
| Age                     | 29.23 (4.69) | 30.09 (7.87) |
| Educational achievement | 5.47 (0.52)  | 5.39 (0.49)  |
| Monthly personal income | 2.57 (2.06)  | 2.73 (1.06)  |
| Monthly family income   | 4.14 (2.21)  | 4.17 (1.96)  |
| Family asset            | 2.62 (1.19)  | 2.35 (1.53)  |
Mediators
| Future time perspective      | 3.69 (0.61) | 3.70 (0.71) |
| ---------------------------- | ----------- | ----------- |
| Temporal discounting shortly | 667 (1371)  | 360 (762)   |
Temporal discounting in the distant future 1727 (1902) 1750 (1795)
| Positive financial attitudes | 4.26 (0.83) | 4.20 (0.61) |
| ---------------------------- | ----------- | ----------- |
Outcome variable
| Financial planning | 2.86 (0.77) | 3.24 (0.88) |
| ------------------ | ----------- | ----------- |
Note: The Chi- square and independent sample t- test showed no significant difference in all variables.

 14678535, 2024, 2, Downloaded from https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401 by Cochrane Philippines, Wiley Online Library on [24/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
|
| 744      |     |     |     | ZHU |
| -------- | --- | --- | --- | --- |
TABLE 4  Results of multiple linear regressions.
Temporal
Future time  Temporal  discounting in the
perspectivea discounting shortlya distance futurea
| Experimental group      | 0.18*   | 0.18* −0.21   | −0.31* −0.27 | −0.29*  |
| ----------------------- | ------- | ------------- | ------------ | ------- |
| Pretest                 | 0.80*** | 0.81*** 0.37* | 0.37* 0.35*  | 0.10    |
| Gender, being male (%)  |         | −0.16*        | −0.14        | −0.16   |
| Age                     |         | −0.01         | 0.25         | 0.34    |
| Educational achievement |         | 0.17*         | 0.06         | −0.04   |
| Monthly personal income |         | −0.12         | −0.20        | 0.23    |
| Monthly family income   |         | −0.010        | −0.39*       | −0.66** |
| Family asset            |         | 0.10          | 0.36*        | 0.26    |
Financial attitudesa Financial planninga
| Experimental group      | 0.22*   | 0.21* 0.24*     | 0.19*   |     |
| ----------------------- | ------- | --------------- | ------- | --- |
| Pretest                 | 0.63*** | 0.66*** 0.67*** | 0.65*** |     |
| Gender, being male (%)  |         | −0.15           | −0.09   |     |
| Age                     |         | 0.28*           | 0.26*   |     |
| Educational achievement |         | −0.01           | −0.05   |     |
| Monthly personal income |         | −0.28           | −0.11   |     |
| Monthly family income   |         | 0.05            | 0.18    |     |
| Family asset            |         | −0.07           | −0.26*  |     |
aPosttest scores. Standardized estimated coefficients are reported.
*p < 0.05; **p < 0.01; ***p < 0.001.
p < 0.05). After adding the background variables as the control, the participants in the
experimental group reported significant improvement in all mediator and outcome vari-
ables (ie, increased future time perspectives (β = 0.18, p < 0.05), reduced temporal dis-
counting shortly (β = −0.31, p < 0.05), reduced temporal discounting in the distance future
(β = −0.29, p < 0.05), improved financial attitudes (β = 0.21, p < 0.05) and better financial
planning (β = 0.19, p < 0.05)). Notably, the standardized effect of our Python- based finan-
cial projection on temporal discounting was much larger than that of our previous per-
sonalized financial projection (−0.31 vs. −0.11), in which we did not present the projection
design and coding to participants (ie, only showing them the projection outcomes in the
mobile application).
Due to the limited sample size, we could not add background variables as controls in the
structural model. Considering that the experiment's effects on two temporal discounting
measures were significant only after adding control variables, we excluded them from the
structural model as mediators. In the structural model, we tested the mediational effects of
future time perspectives and financial attitudes on financial planning among participants.
Based on the results shown in Figure 3, financial attitudes, rather than future time per-
spectives, were a significant mediator. Specifically, positive financial attitudes fully mediated
the impact of Python- based financial projection on financial planning. After practicing with
the Python- based financial projection, participants showed more positive financial attitudes
(β = 0.24, p < 0.05), which in turn reminded them that they could further optimize their finan-
cial planning and increase their intention to plan for personal finance (β = 0.57, p < 0.001).
After modelling the mediational effect, we noticed that the direct effect of the Python- based
financial projection on financial planning disappeared.

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 745
FIGURE 3 Results of experiment- based structural model. *p < 0.05; **p < 0.01; ***p < 0.001.
DISCUSSION
Research calls for upgrading standardized financial education, as its generic curriculum can
only promote objective financial knowledge but is insufficient to change participants' un-
derlying psychology and financial planning (Amagir et al., 2018; Kaiser & Menkhoff, 2020).
Computer- based personalized financial projection could provide a solution, but our previous
financial projection that masked its working mechanism had limited effects on changing
the participants' underlying psychology (Zhu et al., 2023). In response, this study upgraded
our previous financial projection by using Python to disclose its coding. We added Python-
based personalized financial projections to the standardized financial education. Then, we
conducted a randomized control trial among a sample of young working adults in Hong
Kong to determine whether this newly added component could promote participants' finan-
cial planning by affecting their psychology (ie, promoting their future time perspectives and
financial attitudes and reducing their temporal discounting).
We found that the Python- based personalized financial projection transformed the un-
derlying psychology of participants expectedly and overwhelmingly in several ways. First,
although both Python- based and our previous financial projection (masking the coding de-
tails) were found to decrease temporal discounting, the former's standardized effect was al-
most three times as large as that of the latter (ie, Hypothesis 1 is supported). Python- based
coding presents the design of financial projections and elaborates on why current financial
choices determine future financial status. The coding serves as a bridge to establish the
participants' psychological connectedness to their future selves. When participants are well
guided from the present to the future, the future becomes less obscure, more vivid and more
valuable. In contrast, our previous financial projection masked the design of the projection
program and only made the participants learn about their financial status covariates with
their current choice. The specific mechanism that links the present to the future remains a
black box.
Second, the Python- based financial projection was found to significantly promote future
time perspectives (ie, Hypothesis 2 is supported), but the same effect was not found in
our previous financial projection masking the coding (Zhu et al., 2023). Our previous pro-
jection only allows users to adjust personal inputs (eg, salary, expenditure, saving rate),
while Python- based projection enables participants to adjust personal inputs, background
economic parameters (eg, interest rate, salary growth, inflation), and even the logic of the
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

746 | ZHU
projection program. In other words, the Python- based financial projection encourages par-
ticipants to project their financial status in the future based on their perceptions of economic
prospects in society. For the participant, the “the projected future” no longer means the
future self alone but the future self in the future society. Python- based projection presents a
more comprehensive simulation than the previous projection (that sets background parame-
ters as default and does not allow participants to integrate their perceptions of the economic
environment into the financial projection). Unsurprisingly, therefore, Python- based projec-
tion significantly promoted future time perspectives by taking participants to see a more vivid
and realistic future. In contrast, our previous financial projection (masking the coding) failed
to do so (Zhu et al., 2023).
Third, we found that Python- based financial projections could significantly promote the
financial attitudes of participants, supporting Hypothesis 4. In our previous experiment, stan-
dardized financial education could not significantly shape financial attitudes (Zhu, 2020).
Our previous investigation did not test the effect of personalized financial projection (mask-
ing the coding) on financial attitudes (Zhu et al., 2023). In this study, the Python- based fi-
nancial projection maximized participants' opportunity to engage in “active experimentation”
highlighted in the ELT (Kolb et al., 2014). Participants have the opportunity to engage in a
multitude of experiments through the dynamic adjustment of individual inputs— such as the
proportion of salary dedicated to savings and personal investment— as well as broader eco-
nomic parameters like interest rates and inflation. The flexibility extends even to the code
employed for projection. Within this framework, participants gain a comprehensive grasp of
critical financial concepts, most notably compound interest. This understanding transcends
different macroeconomic landscapes and diverse projection models tailored to individual life
trajectories. In essence, this underscores the robustness of healthy financial practices— like
consistent savings and prudent asset allocation for investment. These practices consistently
contribute to the enhancement of future financial well- being, irrespective of an economy's
macroeconomic fluctuations and the personalized course of one's life journey. In contrast,
our preceding financial projection (masking the coding) limited participants to the realm of
trial and error by solely adjusting personal inputs. Regrettably, this restricted approach may
inadvertently propagate a misperception. Namely, participants might wrongly assume that
prudent financial planning solely impacts long- term financial well- being within the confined
scenario established by the projection system.
Finally, we stress that our Python- based financial projection significantly promoted fi-
nancial planning among participants and that positive financial attitudes fully mediated this
effect, indicating Hypothesis 5 is supported. The entire mediation well echoes the theoreti-
cal foundation of personalized financial projection that it affects the financial behaviours of
participants by changing their underlying psychology (Bartels & Urminsky, 2015; Wiener &
Doescher, 2008). Our findings justified adding Python- based personalized financial projec-
tions to standardized financial education. Future research may examine financial education
composed of two components and determine whether it can simultaneously promote ob-
jective financial knowledge, financial attitudes and financial planning, and whether stan-
dardized financial education and Python- based financial projection interact to strengthen
all effects.
While the Python- based financial projection training does encompass a substantial time
investment— a comprehensive 5- hour instruction on Python basics followed by an additional
2- hour training session focused on manipulating projection code— we firmly assert that this
allocation of time and resources proves exceptionally efficient. This efficiency stems from
the profound and wide- ranging positive impacts that extend beyond the confines of the
outcome variables we directly measured. The personalized projection serves as a vivid
testament to the immense power of Python within the realm of financial management. This
exposure often acts as a catalyst, motivating participants to delve deeper into the realm of
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 747
Python's capabilities. Some may be inspired to explore its applications in diverse financial
calculations and planning scenarios, thereby broadening their horizons. It is not inconceiv-
able that participants could experience a transformation in their approach to understanding
the financial landscape once they harness Python's prowess to discern the consequences
of various financial activities.
In an era marked by pervasive digitization, where programming and algorithms drive
enhanced production efficiency, familiarity with Python basics emerges as a definite ad-
vantage. The newfound grasp of Python programming might even spur some participants
to contemplate its applicability beyond the financial realm. This could potentially extend to
assisting with the execution of their occupational responsibilities, tapping into the versa-
tility of coding to streamline their professional tasks. In essence, despite the investment
of time, the Python- based financial projection training acts as a gateway to a realm of
practical skills and insights that have the potential to resonate far beyond the immediate
training period.
LIMITATIONS
Two limitations should be stressed and both motivate future research to continue investigat-
ing the impact of Python- based financial projections on multidimensional financial literacy.
First, our data did not show the significant mediational role of future time perspectives (ie,
Hypothesis 3b is not supported), which might be due to the imperfect design of the data
collection. With the two- wave data, the “effects” of mediators on the outcome variable are
the cross- sectional associations. Adding a third wave may alter the findings and report the
significant effect of the future time perspective on financial planning. Second, we did not test
the mediational role of temporal discounting in financial planning (ie, Hypothesis 3a was not
examined) due to the limited sample size. Our findings showed that Python- based finan-
cial projections significantly reduced temporal discounting after controlling for background
variables. Unfortunately, however, we could not add background variables to the structural
model due to an inadequate degree of freedom with a small sample size. Extending the
sample size in future research could be a solution.
CONCLUSIONS
This study is the first worldwide to integrate Python into personal finance education. We
conducted a randomized control trial to examine the effectiveness of Python- based financial
projection (experiment group: standardized financial education plus Python- based financial
projection; control group: standardized financial education). We found that Python- based
financial projection promoted future time perspectives, financial attitudes and financial plan-
ning of young working adults in Hong Kong and reduced their temporal discounting. Positive
financial attitudes fully mediated the positive effect of Python- based financial projections on
financial planning. We also concluded that exposing the coding to participants strengthened
the effect of personalized financial projection by comparing our results to those in our previ-
ous investigation. Inspired by these findings, we call for more Python- based themed finan-
cial projections (eg, housing planning and health planning) and believe they may benefit the
overall financial planning of working adults. More importantly, our findings suggest upgrad-
ing standardized financial education (ie, combining standardized financial education with
Python- based personalized financial projection). The former promotes objective financial
knowledge, while the latter works by changing underlying psychology and affecting financial
planning.
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

748 | ZHU
FUNDING INFORMATION
The work described in this paper was fully supported by a grant from the Investor and
Financial Education Council in Hong Kong, China.
CONFLICT OF INTEREST STATEMENT
The author declares no potential conflicts of interest with respect to the research, authorship
and/or publication of this article.
DATA AVAILABILITY STATEMENT
The data that support the findings of this study are available from the corresponding author
upon reasonable request.
ETHICS STATEMENT
The ethical approval was obtained from the Human Research Ethics Committee (HREC) of
The Lingnan University (Hong Kong) before the data collection.
INFORMED CONSENT
Informed consent was obtained from all individual participants included in the study.
ORCID
Alex Yue Feng Zhu https://orcid.org/0000-0002-0056-7387
REFERENCES
Amagir, A., Groot, W., Maassen van den Brink, H., & Wilschut, A. (2018). A review of financial- literacy education
programs for children and adolescents. Citizenship, Social and Economics Education, 17(1), 56–80.
Bartels, D. M., & Urminsky, O. (2015). To know and to care: How awareness and valuation of the future jointly
shape consumer spending. Journal of Consumer Research, 41(6), 1469–1485.
Basile, A. G., & Toplak, M. E. (2015). Four converging measures of temporal discounting and their relation-
ships with intelligence, executive functions, thinking dispositions, and behavioral outcomes. Frontiers in
Psychology, 6, 728–741.
Batty, M., Collins, J. M., & Odders- White, E. (2015). Experimental evidence on the effects of financial education
on elementary school students' knowledge, behavior, and attitudes. Journal of Consumer Affairs, 49(1),
69–96.
Becchetti, L., Caiazza, S., & Coviello, D. (2013). Financial education and investment attitudes in high schools:
Evidence from a randomized experiment. Applied Financial Economics, 23(10), 817–836.
Berry, J., Karlan, D., & Pradhan, M. (2018). The impact of financial education for youth in Ghana. World
Development, 102, 71–89.
Chapman, G. B. (1996). Temporal discounting and utility for health and money. Journal of Experimental
Psychology: Learning, Memory, and Cognition, 22(3), 771–791.
Chou, K. L., Yu, K. M., Chan, W. S., Wu, A. M., Zhu, A. Y., & Lou, V. W. (2015). Perceived retirement savings
adequacy in Hong Kong: An interdisciplinary financial planning model. Ageing & Society, 35(8), 1565–1586.
Douissa, I. B. (2020). Factors affecting college students' multidimensional financial literacy in the Middle East.
International Review of Economics Education, 35, 100173.
Fajnzylber, E., & Reyes, G. (2015). Knowledge, information, and retirement saving decisions: Evidence from a
large- scale intervention in Chile. Economia, 15(2), 83–117.
Fuentes, O., Lafortune, J., Riutort, J., Tessada, J., & Villatorok, F. (2022). Personalized information as a tool to im-
prove pension savings: Results from a randomized control trial in Chile. Economic Development and Cultural
Change. Advanced access online.
Garcia, M. J. R. (2013). Financial education and behavioral finance: New insights into the role of information in
financial decisions. Journal of Economic Surveys, 27(2), 297–315.
Goda, G. S., Manchester, C. F., & Sojourner, A. J. (2014). What will my account really be worth? Experimental
evidence on how retirement income projections affect saving. Journal of Public Economics, 119, 80–92.
Hershfield, H. E., Goldstein, D. G., Sharpe, W. F., Fox, J., Yeykelis, L., Carstensen, L. L., & Bailenson, J. N. (2011).
Increasing saving behavior through age- progressed renderings of the future self. Journal of Marketing
Research, 48(Spl), S23–S37.
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

UPGRADING FINANCIAL EDUCATION BY ADDING PYTHON- BASED
PERSONALIZED FINANCIAL PROJECTION | 749
Hershfield, H. E., & Bartels, D. M. (2018). The future self. In G. Oettingen, A. T. Sevincer, & P. M. Gollwitzer (Eds.),
The psychology of thinking about the future (pp. 89–109). Guilford.
Hizgilov, A., & Silber, J. (2020). On multidimensional approaches to financial literacy measurement. Social
Indicators Research, 148(3), 787–830.
Humber, M. (2018). Personal finance with python: Using pandas, requests, and recurrent. Apress.
Kaiser, T., & Menkhoff, L. (2020). Financial education in schools: A meta- analysis of experimental studies.
Economics of Education Review, 78, 101930.
Kalwij, A., Alessie, R., Dinkova, M., Schonewille, G., Van der Schors, A., & Van der Werf, M. (2019). The effects
of financial education on financial literacy and savings behavior: Evidence from a controlled field experiment
in Dutch primary schools. Journal of Consumer Affairs, 53(3), 699–730.
Kolb, D. A., Boyatzis, R. E., & Mainemelis, C. (2014). Experiential learning theory: Previous research and new
directions. In R. J. Sternberg & L. F. Zhang (Eds.), Perspectives on thinking, learning, and cognitive styles
(pp. 227–248). Routledge.
Li, J., Hodgson, N., Lyons, M. M., Chen, K. C., Yu, F., & Gooneratne, N. S. (2020). A personalized behavioral
intervention implementing mHealth technologies for older adults: A pilot feasibility study. Geriatric Nursing,
41(3), 313–319.
Li, Q., Mintz, Y., Gavin, K., & Voils, C. (2023). An adaptive optimization approach to personalized financial incen-
tives in mobile behavioral weight loss interventions. arXiv Preprint. arXiv:2307.00444.
Lyons, A. C., & Kass- Hanna, J. (2021). A multidimensional approach to defining and measuring financial literacy
in the digital age. In G. Nicolini & B. J. Cude (Eds.), The Routledge handbook of financial literacy (pp. 61–76).
Routledge.
MacLeod, S., Musich, S., Hawkins, K., & Armstrong, D. G. (2017). The growing need for resources to help older
adults manage their financial and healthcare choices. BMC Geriatrics, 17(1), 1–9.
Marques, S., Mariano, J., Lima, M. L., & Abrams, D. (2018). Are you talking to the future me? The moderator role
of future self- relevance on the effects of aging salience in retirement savings. Journal of Applied Social
Psychology, 48(7), 360–368.
Mosh. (2022). https://codewi thmos h.com/
Noh, M. (2022). Effect of parental financial teaching on college students' financial attitude and behavior: The
mediating role of self- esteem. Journal of Business Research, 143, 298–304.
OECD. (2017). PISA 2015 Results (Volume IV). OECD Publishing.
OECD. (2019). OECD/INFE report on financial education in APEC economies. OECD Publishing.
Oyserman, D., Bybee, D., Terry, K., & Hart- Johnson, T. (2004). Possible selves as roadmaps. Journal of Research
in Personality, 38, 130–149.
Pronin, E., & Ross, L. (2006). Temporal differences in trait self- ascription: When the self is seen as an other.
Journal of Personality and Social Psychology, 90(2), 197–209.
PYPI. (2020). PYPL PopularitY of programming language. https://pypl.github.io/PYPL.html
Rai, K., Dua, S., & Yadav, M. (2019). Association of financial attitude, financial behaviour and financial knowledge
towards financial literacy: A structural equation modeling approach. FIIB Business Review, 8(1), 51–60.
Rutt, J. L., & Löckenhoff, C. E. (2016). From past to future: Temporal self- continuity across the life span. Psychology
and Aging, 31(6), 631–639.
Salignac, F., Hamilton, M., Noone, J., Marjolin, A., & Muir, K. (2020). Conceptualizing financial wellbeing: An eco-
logical life- course approach. Journal of Happiness Studies, 21, 1581–1602.
Salignac, F., Marjolin, A., Reeve, R., & Muir, K. (2019). Conceptualizing and measuring financial resilience: A
multidimensional framework. Social Indicators Research, 145, 17–38.
Seaman, K. L., Abiodun, S. J., Fenn, Z., Samanez- Larkin, G. R., & Mata, R. (2022). Temporal discounting across
adulthood: A systematic review and meta- analysis. Psychology and Aging, 37(1), 111–124.
Serido, J., Shim, S., & Tang, C. (2013). A developmental model of financial capability: A framework for promoting
a successful transition to adulthood. International Journal of Behavioral Development, 37(4), 287–297.
Shim, S., Serido, J., Tang, C., & Card, N. (2015). Socialization processes and pathways to healthy financial devel-
opment for emerging young adults. Journal of Applied Developmental Psychology, 38, 29–38.
Tomar, S., Baker, H. K., Kumar, S., & Hoffmann, A. O. (2021). Psychological determinants of retirement financial
planning behavior. Journal of Business Research, 133, 432–449.
VanderPlas, J. (2016). Python data science handbook: Essential tools for working with data. O'Reilly Media,
Inc.
Walstad, W., Urban, C., Asarta, C. J., Breitbach, E., Bosshardt, W., Heath, J., O'Neill, B., Wagner, J., & Xiao, J.
J. (2017). Perspectives on evaluation in financial education: Landscape, issues, and studies. The Journal of
Economic Education, 48(2), 93–112.
Walstad, W. B., Rebeck, K., & MacDonald, R. A. (2010). The effects of financial education on the financial knowl-
edge of high school students. Journal of Consumer Affairs, 44(2), 336–357.
Wiener, J., & Doescher, T. (2008). A framework for promoting retirement savings. Journal of Consumer Affairs,
42(2), 137–164.
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

750 | ZHU
Xiao, J. J., & O'Neill, B. (2016). Consumer financial education and financial capability. International Journal of
Consumer Studies, 40(6), 712–721.
Zhu, A. Y. F. (2018). Parental socialization and financial capability among Chinese adolescents in Hong Kong.
Journal of Family and Economic Issues, 39(4), 566–576.
Zhu, A. Y. F., Fung, H. H. L., Chan, W. S., & Chou, K. L. (2023). Promoting financial preparation for retirement of
working adults: A temporal discounting intervention. Under review by Journal of Applied Gerontology.
Zhu, A. Y. F., Yu, C. W. M., & Chou, K. L. (2021). Improving financial literacy in secondary school students: An
randomized experiment. Youth & Society, 53(4), 539–562.
Zhu, A. Y. F. (2020). Impact of financial education on adolescent financial capability: Evidence from a pilot ran-
domized experiment. Child Indicators Research, 13(4), 1371–1386.
How to cite this article: Zhu, A. Y. F. (2024). Upgrading financial education by adding
Python- based personalized financial projection: A randomized control trial. British
Journal of Educational Technology, 55, 731–750. https://doi.org/10.1111/bjet.13401
14678535,
2024,
2,
Downloaded
from
https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13401
by
Cochrane
Philippines,
Wiley
Online
Library
on
[24/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License