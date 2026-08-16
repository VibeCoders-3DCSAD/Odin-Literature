---
conversion_metadata:
  converted_at: "2026-07-22T13:04:32Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Das et al.pdf"
  source_pdf_sha256: "db2d7564ba834f691e6ac5fe644888356e771763829e1e72acc7c23ad385bc85"
  page_count: 22
  markdown_char_count: 124903
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Chapter  4

Recurrent  Neural  Networks  (RNNs):  Architectures,  Training 
Tricks,  and  Introduction  to  Inﬂuential  Research

Susmita  Das,  Amara  Tariq,  Thiago  Santos,  Sai  Sandeep  Kantareddy, 
and  Imon  Banerjee

Abstract

Recurrent  neural  networks  (RNNs)  are  neural  network  architectures  with  hidden  state  and  which  use 
feedback  loops  to  process  a  sequence  of  data  that  ultimately  informs  the  ﬁnal  output.  Therefore,  RNN 
models  can  recognize  sequential  characteristics  in  the  data  and  help  to  predict  the  next  likely  data  point  in 
the  data  sequence.  Leveraging  the  power  of  sequential  data  processing,  RNN  use  cases  tend  to  be 
language  models  or  time-series  data  analysis.  However,  multiple  popular  RNN 
connected  to  either 
architectures  have  been  introduced  in  the  ﬁeld,  starting  from  SimpleRNN  and  LSTM  to  deep  RNN,  and 
applied  in  different  experimental  settings.  In  this  chapter,  we  will  present  six  distinct  RNN  architectures  and 
will  highlight  the  pros  and  cons  of  each  model.  Afterward,  we  will  discuss  real-life  tips  and  tricks  for  training 
the  RNN  models.  Finally,  we  will  present  four  popular  language  modeling  applications  of  the  RNN 
models  –text  classiﬁcation,  summarization,  machine  translation,  and  image-to-text  translation–  thereby 
demonstrating  inﬂuential  research  in  the  ﬁeld.

Key  words  Recurrent  neural  network  (RNN),  LSTM,  GRU,  Bidirectional  RNN  (BRNN),  Deep 
RNN,  Language  modeling

1

Introduction

Recurrent  neural  network  (RNN)  is  a  specialized  neural  network 
with  feedback  connection  for  processing  sequential  data  or  time-
series  data  in  which  the  output  obtained  is  fed  back  into  it  as  input 
along  with  the  new  input  at  every  time  step.  The  feedback  connec-
tion  allows  the  neural  network  to  remember  the  past  data  when 
processing  the  next  output.  Such  processing  can  be  deﬁned  as  a 
recurring  process,  and  hence  the  architecture  is  also  known  as 
recurring  neural  network.

RNN  concept  was  ﬁrst  proposed  by  Rumelhart  et  al.  [1] in a  
letter  published  by  Nature  in  1986  to  describe  a  new  learning 
procedure  with  a  self-organizing  neural  network.  Another  impor-
tant  historical  moment  for  RNNs  is  the  (re-)discovery  of  Hopﬁeld

Olivier  Colliot  (ed.),  Machine  Learning  for  Brain  Disorders,  Neuromethods,  vol.  197,  https://doi.org/10.1007/978-1-0716-3195-9_4, 
©  The  Author(s)  2023

117

---

<!-- PAGE 2 -->

118

Susmita Das et al.

networks  which  is  a  special  kind  of  RNN  with  symmetric  connec-
tions  where  the  weight  from  one  node  to  another  and  from  the 
latter  to  the  former  are  the  same  (symmetric).  The  Hopﬁeld  net-
work  [2]  is  fully  connected,  so  every  neuron’s  output  is  an  input  to 
all  the  other  neurons,  and  updating  of  nodes  happens  in  a  binary 
way  (0/1).  These  types  of  networks  were  speciﬁcally  designed  to 
simulate  the  human  memory.

the

architectures,

The  other  types  of  RNNs  are  input-output  mapping  networks, 
which  are  used  for  classiﬁcation  and  prediction  of  sequential  data. 
In  1993,  Schmidhuber  et  al.  [3]  demonstrated  credit  assignment 
across  the  equivalent  of  1,200  layers  in  an  unfolded  RNN  and 
revolutionized  sequential  modeling.  In  1997,  one  of  the  most 
popular  RNN 
short-term  memory 
(LSTM)  network  which  can  process  long  sequences,  was  proposed. 
In  this  chapter,  we  summarize  the  six  most  popular  contempo-
rary  RNN  architectures  and  their  variations  and  highlight  the  pros 
and  cons  of  each.  We  also  discuss  real-life  tips  and  tricks  for  training 
the  RNN  models,  including  various  skip  connections  and  gradient 
clipping.  Finally,  we  highlight  four  popular  language  modeling 
applications  of  the  RNN  models  –text  classiﬁcation,  summariza-
tion,  machine  translation,  and  image-to-text  translation–  thereby 
demonstrating  inﬂuential  research  in  each  area.

long

2  Popular  RNN  Architectures

2.1  SimpleRNN

In  addition  to  the  SimpleRNN  architecture,  many  variations  were 
proposed  to  address  different  use  cases.  In  this  section,  we  will 
unwrap  some  of  the  popular  RNN  architectures 
like  LSTM, 
GRU,  bidirectional  RNN,  deep  RNN,  and  attention  models  and 
discuss  their  pros  and  cons.

SimpleRNN  architecture,  which 
is  also  known  as  SimpleRNN, 
contains  a  simple  neural  network  with  a  feedback  connection.  It 
has  the  capability  to  process  sequential  data  of  variable  length  due 
to  the  parameter  sharing  which  generalizes  the  model  to  process 
sequences  of  variable  length.  Unlike  feedforward  neural  networks 
which  have  separate  weights  for  each  input  feature,  RNN  shares  the 
same  weights  across  several  time  steps.  In  RNN,  the  output  of  a 
present  time  step  depends  on  the  previous  time  steps  and 
is 
obtained  by  the  same  update  rule  which  is  used  to  obtain  the 
previous  outputs.  As  we  will  see,  the  RNN  can  be  unfolded  into  a 
deep  computational  graph  in  which  the  weights  are  shared  across 
time  steps.

The  RNN  operating  on  an  input  sequence  x(t)  with  a  time  step 
index  t  ranging  from  1  to  τ  is  illustrated  in  Fig.  1.  The  time  step 
index  t  may  not  necessarily  refer  to  the  passage  of  time  in  the  real 
world;  it  can  refer  to  the  position  in  the  sequence.  The  cycles  in  the

---

<!-- PAGE 3 -->

RNN Architectures and Research

119

o(t-1)

o(t)

o(t+1)

Unfold

h(....)

h(t-1)

h(t)

h(t+1)

h(....)

x(t-1)

x(t)

x(t+1)

o

h

x

Fig.  1  (Left)  Circuit  diagram  for  SimpleRNN  with  input  x  being  incorporated  into  hidden  state  h  with  a  feedback 
connection  and  an  output  o.  (Right)  The  same  SimpleRNN  network  shown  as  an  unfolded  computational  graph 
with  nodes  at  every  time  step

computational  graph  represent  the  impact  of  the  past  value  of  a 
variable  on  the  present  time  step.  The  computational  graph  has  a 
repetitive  structure  that  unfolds  the  recursive  computation  of  the 
RNN  which  corresponds  to  a  chain  of  events.  It  shows  the  ﬂow  of 
the  information,  forward  in  the  time  of  computing  the  outputs  and 
losses  and  backward  when  computing  the  gradients.  The  unfolded 
computational  graph 
equation 
corresponding  to  the  computational  graph  is  h(t)  = f(h(t-1) ,  x(t) ; 
W),  where  h  is  the  hidden  state  of  the  network,  x  is  the  input,  t  is 
the  time  step,  and  W  denotes  the  weights  of  the  network  connec-
tions  comprising  of 
input-to-hidden,  hidden-to-hidden,  and 
hidden-to-output  connection  weights.

in  Fig.  1.  The

shown

is

Training

2.1.1 
Fundamentals

left  to  right  of  the  unrolled  graph

Training  is  performed  by  gradient  computation  of  the  loss  function 
with  respect  to  the  parameters  involved  in  forward  propagation 
from 
followed  by  back-
propagation  moving  from  right  to  left  through  the  graph.  Such 
gradient  computation  is  an  expensive  operation  as  the  runtime 
cannot  be  reduced  by  parallelism  because  the  forward  propagation 
is  sequential  in  nature.  The  states  computed  in  the  forward  pass  are 
stored  until  they  are  reused  in  the  back-propagation.  The  back-
propagation  algorithm  applied  to  RNN  is  known  as  back-propa-
gation  through  time  (BPTT)  [4].

The  following  computational  operations  are  performed 
in 
RNN  during  the  forward  propagation  to  calculate  the  output  and 
the  loss.

ðt - 1Þ þ  U xðtÞ

aðtÞ  = b  þ  W h
ðtÞ  = tanhðaðtÞÞ 
h
ðtÞ 
oðtÞ  = c  þ  V h
ðtÞ  = σðoðtÞÞ
^y

---

<!-- PAGE 4 -->

120

Susmita Das et al.

where  b  and  c  are  the  biases  and  U,  V ,  and  W  are  the  weight  matrix 
for 
input-to-hidden  connections,  hidden-to-output  connection, 
and  hidden-to-hidden  connections  respectively,  and  σ  is  a  sigmoid 
its 
function.  The  total 
corresponding  y  values  is  obtained  by  summing  up  the  losses  over 
all  time  steps.

for  a  sequence  of  x  values  and

loss

ðtÞ  = Lððxð1Þ, . . . . . ., x ðτÞÞ, ðy ð1Þ, . . . . . ., y ðτÞÞÞ

L

τ

t  = 1

loss  function

To  minimize  the

loss,  the  gradient  of  the

is 
calculated  with  respect  to  the  parameters  associated  with  it.  The 
parameters  associated  with  the  nodes  of  the  computational  graph 
are  U,  V  ,  W,  b,  c,  x(t) ,  h(t) ,  o(t) ,  and  L(t) .  The  output  o(t)  is  the 
argument  to  the  softmax  to  obtain  the  vector  ^y  of  probabilities  over 
the  output.  During  back-propagation,  the  gradient  for  each  node  is 
calculated  recursively  starting  with  the  nodes  preceding  the  ﬁnal 
loss.  It  is  then  iterated  backward  in  time  to  back-propagate  gradi-
ents  through  time.  tanh  is  a  popular  choice  for  activation  function 
as 
it  tends  to  avoid  vanishing  gradient  problem  by  retaining 
non-zero  value  longer  through  the  back-propagation  process.

SimpleRNN

2.1.2 
Architecture  Variations 
Based  on  Parameter 
Sharing

SimpleRNN

2.1.3 
Architecture  Variations 
Based  on  Inputs  and 
Outputs

Variations  of  SimpleRNN  can  be  designed  depending  upon  the 
style  of  graph  unrolling  and  parameter  sharing  [5]:

(cid:129) Connection  between  hidden  units.  The  RNN  produces  outputs  at 
every  time  step,  and  the  parameters  are  passed  between  hidden-
to-hidden  units  (Fig.  2a).  This  corresponds  to  the  standard 
SimpleRNN  presented  above  and  is  widely  used.

(cid:129) Connection  between  outputs  to  hidden  units.  The  RNN  produces 
outputs  at  every  time  step,  and  the  parameters  are  passed  from 
an  output  at  a  particular  time  step  to  the  hidden  unit  at  the  next 
time  step  (Fig.  2b).

(cid:129) Sequential  input  to  single  output.  The  RNN  produces  a  single 
output  at  the  end  after  reading  the  entire  sequence  and  has 
connections  between  the  hidden  units  at  every  time  step 
(Fig.  2c).

Different  variations  also  exist  depending  on  the  number  of  inputs 
and  outputs:
(cid:129) One-to-one:  The  traditional  RNN  has  one-to-one  input  to  out-

put  mapping  at  each  time  step  t  as  shown  in  Fig.  3a.

(cid:129) One-to-many:  One-to-many  RNN  has  one  input  at  a  time  step 
for  which  it  generates  a  sequence  of  outputs  at  consecutive  time 
steps  as  shown  in  Fig.  3b.  This  type  of  RNN  architecture  is  often 
used  for  image  captioning.

---

<!-- PAGE 5 -->

(a)

(b)

o(t-1)

o(t)

o(t+1)

o(....)

o(t-1)

o(t)

o(t+1)

RNN Architectures and Research

121

h(....)

h(t-1)

h(t)

h(t+1)

h(....)

h(....)

h(t-1)

h(t)

h(t+1)

h(....)

x(t-1)

x(t)

x(t+1)

x(t-1)

x(t)

x(t+1)

(c)

o

h(....)

h(t-1)

h(t)

h(t+1)

h(....)

x(t-1)

x(t)

x(t+1)

Fig.  2  Types  of  SimpleRNN  architectures  based  on  parameter  sharing:  (a)  SimpleRNN  with  connections 
between  hidden  units,  (b)  SimpleRNN  with  connections  from  output  to  hidden  units,  and  (c)  SimpleRNN  with 
connections  between  hidden  units  that  read  the  entire  sequence  and  produce  a  single  output

(cid:129) Many-to-one:  Many-to-one  RNN  has  many  inputs  and  one  out-
put,  at  each  time  step  as  shown  in  Fig.  3c.  This  type  of  RNN 
architecture  is  used  for  text  classiﬁcation.

(cid:129) Many-to-many:  Many-to-many  RNN  architecture  can  be 
designed  in  two  ways.  First,  the  input  is  taken  by  the  RNN  and 
the  corresponding  output  is  given  at  the  same  time  step  as 
illustrated  in  Fig.  3d.  This  type  of  RNN  is  used  for  named  entity 
recognition.  Second,  the  input  is  taken  by  the  RNN  at  each  time 
step  and  the  output  is  given  by  the  RNN  at  the  next  time  step 
depending  upon  all 
in 
input 
Fig.  3e.  Popular  uses  of  this  type  of  RNN  architecture  are  in 
machine  translation.

sequence  as

illustrated

the

2.1.4  Challenges  of 
Long-Term  Dependencies 
in  SimpleRNN

SimpleRNN  works  well  with  the  short-term  dependencies,  but 
when  it  comes  to  long-term  dependencies,  it  fails  to  remember 
the  long-term  information.  This  problem  arises  due  to  the  vanish-
ing  gradient  or  exploding  gradient  [6].  When  the  gradients  are 
propagated  over  many  stages,  it  tends  to  vanish  most  of  the  times 
or  sometimes  explodes.  The  difﬁculty  arises  due  to  the  exponen-
tially  smaller  weight  assigned  to  the  long-term  interactions  com-
pared  to  the  short-term  interactions.  It  takes  very  long  time  to  learn 
the  long-term  dependencies  as  the  signals  from  these  dependencies 
tend  to  be  hidden  by  the  small  ﬂuctuations  arising  from  the  short-
term  dependencies.

---

<!-- PAGE 6 -->

122

Susmita Das et al.

(a)

(b)

(c)

o(t)

h(t)

x(t)

o(t)

o(t+1)

o(t+2)

o(t)

h(t)

h(t+1)

h(t+2)

h(t–2)

h(t–1)

h(t)

x(t)

x(t–2)

x(t–1)

x(t)

(d)

(e)

o(t)

o(t+1)

o(t+2)

o(t)

o(t+1)

o(t+2)

h(t)

h(t+1)

h(t+2)

h(t–2)

h(t–1)

h(t)

h(t+1)

h(t+2)

x(t)

x(t+1)

x(t+2)

x(t–2)

x(t–1)

x(t)

Fig.  3  (a)  One-to-one  RNN.  (b)  One-to-many  RNN.  (c)  Many-to-one  RNN.  (d)  Many-to-many  RNN.  (e)  Many-to-
many  RNN.  x  represents  the  input  and  o  represents  the  output

Long  Short-Term

2.2 
Memory  (LSTM)

like

speech

in  many  applications

To  address  this  long-term  dependency  problem,  gated  RNNs  were 
proposed.  Long  short-term  memory  (LSTM)  is  a  type  of  gated 
RNN  which  was  proposed  in  1997  [7].  Due  to  the  property  of 
remembering  the  long-term  dependencies,  LSTM  has  been  a  suc-
cessful  model 
recognition, 
machine  translation,  image  captioning,  etc.  LSTM  has  an  inner 
self  loop  in  addition  to  the  outer  recurrence  of  the  RNN.  The 
gradients  in  the  inner  loop  can  ﬂow  for  longer  duration  and  are 
conditioned  on  the  context  rather  than  being  ﬁxed.  In  each  cell,  the 
input  and  output  is  the  same  as  that  of  ordinary  RNN  but  has  a 
system  of  gating  units  to  control  the  ﬂow  of  information.  Figure  4 
shows  the  ﬂow  of  the  information  in  LSTM  with  its  gating  units. 
There  are  three  gates  in  the  LSTM—the  external  input  gate, 
the  forget  gate,  and  the  output  gate.  The  forget  gate  at  time  t  and 
ðtÞ 
state  si  (f 
i  )  decides  which  information  should  be  removed  from 
the  cell  state.  The  gate  controls  the  self  loop  by  setting  the  weight 
between  0  and  1  via  a  sigmoid  function  σ.  When  the  value  is  near  to 
1,  the  information  of  the  past  is  retained,  and  if  the  value  is  near  to

---

<!-- PAGE 7 -->

RNN Architectures and Research

123

ot

ht

c(t–1)

X

+

X

tanh

s

s

tanh

s

X

h(t–1)

xt

ct

ht

Fig.  4  Long  short-term  memory  with  cell  state  ct ,  hidden  state  ht ,  input  xt ,  and  output  ot

ðtÞ 
i

is  updated.  Computation  for  external  input  gate  (g t

0,  the  information  is  discarded.  After  the  forget  gate,  the  internal 
state  s
i  ) is  
similar  to  that  of  forget  gate  with  a  sigmoid  function  to  obtain  a 
value  between  0  and  1  but  with  its  own  parameters.  The  output 
gate  of  the  LSTM  also  has  a  sigmoid  unit  which  determines 
whether  to  output  the  value  or  to  shut  off  the  value  ht 
i  via  the 
output  gate  qt 
i .

ðtÞ 
i

f

= σ

U f

i  , j xt 
j

þ

j

j

W f

i  , j h

ðt - 1Þ 
j

þ  bf 
i

ðtÞ 
i

s

= f  t 
i s

ðt - 1Þ 
i

þ  g t 
i

σ  bi  þ

g t 
i

= σ  bg 
i

þ

U g

i  , j xt 
j

þ

W i, j h

ðt - 1Þ 
j

U i, j x t 
j

þ

j

W g

i  , j h

ðt - 1Þ 
j

j

j

ht 
i

= tanhðs t 
i

qt 
i

= σ  bo 
i

þ

j 
Þqt 
i

j

U o

i , j xt 
i

þ  W o

i , j h

ðt - 1Þ 
j

xt  is  the  input  vector  at  time  t,  h(t)  is  the  hidden  layer  vector,  bi 
denote  the  biases,  and  Ui  and  Wi  represent  the  input  weights  and 
the  recurrent  weights,  respectively.

---

<!-- PAGE 8 -->

124

Susmita Das et al.

h(t–1)

ht

X

Reset 
gate

s

Update 
gate

X

1–

s

+

X

tanh

xt

Fig.  5  Gated  recurrent  neural  network  (GRU)  with  input  xt  and  hidden  unit  ht

2.3  Gated  Recurrent 
Unit  (GRU)

In  LSTM,  the  computation  time  is  large  as  there  are  a  lot  of 
parameters  involved  during  back-propagation.  To  reduce  the  com-
putation  time,  gated  recurrent  unit  (GRU)  was  proposed  in  the 
year  2014  by  Cho  et  al.  with  less  gates  than  in  LSTM  [8].  The 
functionality  of  the  GRU  is  similar  to  that  of  LSTM  but  with  a 
modiﬁed  architecture.  The  representation  diagram  for  GRU  can  be 
found  in  Fig.  5.  Like  LSTM,  GRU  also  solves  the  vanishing  and 
exploding  gradient  problem  by  capturing  the  long-term  dependen-
cies  with  the  help  of  gating  units.  There  are  two  gates  in  GRU,  the 
reset  gate  and  the  update  gate.  The  reset  gate  determines  how 
much  of  the  past  information  it  needs  to  forget,  and  the  update 
gate  determines  how  much  of  the  past  information  it  needs  to  carry 
forward.

The  computation  at  the  reset  gate  (r t

i), 
i)  and  the  at  time  t,  can  be represented  by  the

i)  and  the  update  gate  (ut

as well  as  hidden  state  (ht 
following:

W r

i,j h

ðtÞ 
j

Þ

W u

i,j h

ðtÞ 
j

Þ

j

j

ðtÞ 
i

r

= σðbr 
i

þ

U r

i,j x

ðtÞ 
j

þ

j

ðtÞ 
i

u

ðtÞ 
i

h

= σðbu 
i

þ

ðt - 1Þ 
i

j 
ðt - 1Þ 
= u
h
i 
×  σðbi  þ

j

Uu

i,j x

ðtÞ 
j

þ

þ ð1 - u iÞ 
ðt - 1Þ 
þ 
j

U i,j x

W i,j r

ðt - 1Þ 
j

ðt - 1Þ 
j

Þ

h

j

where  bi  denotes  biases  and  Ui  and  Wi  denote  initial  and  recurrent 
weights,  respectively.

---

<!-- PAGE 9 -->

RNN Architectures and Research

125

When  the  reset  gate  value  is  close  to  0,  the  previous  hidden 
state  value 
is  discarded  and  reset  with  the  present  value.  This 
enables  the  hidden  state  to  forget  the  past  information  that  is 
irrelevant  for  future.  The  update  gate  determines  how  much  of 
the  relevant  past  information  to  carry  forward  for  future.

The  property  of  the  update  gate  to  carry  forward  the  past 
information  allows  it  to  remember  the  long-term  dependencies. 
For  short-term  dependencies,  the  reset  gate  will  be  frequently 
active  to  reset  with  current  values  and  remove  the  previous  ones, 
while,  for  long-term  dependencies,  the  update  gate  will  be  often 
active  for  carrying  forward  the  previous  information.

The  LSTM  and  GRU  can  handle  the  vanishing  gradient  issue  of 
SimpleRNN  with  the  help  of  gating  units.  The  LSTM  and  GRU 
have  the  additive  feature  that  they  retain  the  past  information  by 
adding  the  relevant  past  information  to  the  present  state.  This 
additive  property  makes  it  possible  to  remember  a  speciﬁc  feature 
in  the  input  for  longer  time.  In  SimpleRNN,  the  past  information 
loses  its  relevance  when  new  input  is  seen.  In  LSTM  and  GRU,  any 
important  feature  is  not  overwritten  by  new  information.  Instead,  it 
is  added  along  with  the  new  information.

There  are  a  few  differences  between  LSTM  and  GRU  in  terms  of 
gating  mechanism  which  in  turn  result  in  differences  observed  in 
the  content  generated.  In  LSTM  unit,  the  amount  of  the  memory 
content  to  be  used  by  other  units  of  the  network  is  regulated  by  the 
output  gate,  whereas  in  GRU,  the  full  content  that  is  generated  is 
exposed  to  other  units.  Another  difference  is  that  the  LSTM  com-
putes  the  new  memory  content  without  controlling  the  amount  of 
previous  state  information  ﬂowing.  Instead,  it  controls  the  new 
memory  content  that  is  to  be  added  to  the  network.  On  the  other 
hand,  the  GRU  controls  the  ﬂow  of  the  past  information  when 
computing  the  new  candidate  without  controlling  the  candidate 
activation.

In  SimpleRNN,  the  output  of  a  state  at  time  t  only  depends  on  the 
information  of  the  past  x(1) , .. . .,  x (t-1)  and  the  present  input  x(t) . 
However,  for  many  sequence-to-sequence  applications,  the  present 
state  output  depends  on  the  whole  sequence  information.  For 
example,  in  language  translation,  the  correct  interpretation  of  the 
current  word  depends  on  the  past  words  as  well  as  the  next  words. 
To  overcome  this  limitation  of  SimpleRNN,  bidirectional  RNN 
(BRNN)  was  proposed  by  Schuster  and  Paliwal 
in  the  year 
1997  [9].

Bidirectional  RNNs  combine  an  RNN  which  moves  forward 
with  time,  beginning  from  the  start  of  the  sequence,  with  another 
RNN  that  moves  backward  through  time,  beginning  from  the  end 
of  the  sequence.  Figure  6  illustrates  a  bidirectional  RNN  with  h(t)

Advantage  of  LSTM

2.3.1 
and  GRU  over  SimpleRNN

2.3.2  Differences 
Between  LSTM  and  GRU

2.4  Bidirectional 
RNN  (BRNN)

---

<!-- PAGE 10 -->

126

Susmita Das et al.

o(t–1)

o(t)

o(t+1)

g(...)

g(t–1)

g(t)

g(t+1)

g(...)

h(...)

h(t–1)

h(t)

h(t+1)

h(...)

x(t–1)

x(t)

x(t+1)

Fig.  6  Bidirectional  RNN  with  forward  sub-RNN  having  ht  hidden  state  and 
backward  sub-RNN  having  gt  hidden  state

the  state  of  the  sub-RNN  that  moves  forward  through  time  and  g(t) 
the  state  of  the  sub-RNN  that  moves  backward  with  time.  The 
output  of  the  sub-RNN  that  moves  forward  is  not  connected  to 
the  inputs  of  sub-RNN  that  moves  backward  and  vice  versa.  The 
output  o(t)  depends  on  both  past  and  future  sequence  data  but  is 
sensitive  to  the  input  values  around  t.

2.5  Deep  RNN

Deep  models  are  more  efﬁcient  than  their  shallow  counterparts, 
and,  with  the  same  hypothesis,  deep  RNN  was  proposed  by 
Pascanu  et  al.  in  2014  [10].  In  “shallow”  RNN,  there  are  generally 
three  blocks  for  computation  of  parameters:  the  input  state,  the 
hidden  state,  and  the  output  state.  These  blocks  are  associated  with 
a  single  weight  matrix  corresponding  to  a  shallow  transformation 
which  can  be  represented  by  a  single-layer  multilayer  perceptron 
(MLP).  In  deep  RNN,  the  state  of  the  RNN  can  be  decomposed 
into  multiple  layers.  Figure  7  shows  in  general  a  deep  RNN  with 
multiple  deep  MLPs.  However,  different  types  of  depth  in  an  RNN 
can  be  considered  separately 
input-to-hidden,  hidden-to-
like 
hidden,  and  hidden-to-output  layer.  The  lower  layer  in  the  hierar-
chy  can  transform  the  input  into  an  appropriate  representation  for 
higher  levels  of  hidden  state.  In  hidden-to-hidden  state,  it  can  be 
constructed  with  a  previous  hidden  state  and  a  new  input.  This 
introduces  additional  non-linearity 
the  architecture  which 
becomes  easier  to  quickly  adapt  changing  modes  of  the  input.  By 
introducing  deep  MLP  in  hidden-to-output  state  makes  the  layer 
compact  which  helps  in  summarizing  the  previous  inputs  and  helps 
in  predicting  the  output  easily.  Due  to  the  deep  MLP  in  the  RNN 
architecture, 
is 
difﬁcult.

learning  becomes  slow  and  optimization

the

in

---

<!-- PAGE 11 -->

RNN Architectures and Research

127

o1

o2

o3

(n)

h1

(n)

h2

(n)

h3

(2)

h1

(1)

h1

(2)

h2

(1)

h2

(2)

h3

(1)

h3

x1

x2

x3

Fig.  7  Deep  recurrent  neural  network

ot

(n)

ht

(2)

ht

(1)

ht

xt

Encoder–

2.6 
Decoder

Encoder–decoder  architecture  was  proposed  by  Cho  et  al.  (2014) 
[8]  to  map  a  variable  length  input  sequence  to  a  variable  length 
output  sequence.  Therefore, 
is  also  known  as  sequence-to-
it 
sequence  architecture.  Before  encoder–decoder  was  introduced, 
there  were  RNN  models  which  were  used 
for  sequence-to-
sequence  applications,  but  they  had  limitations  as  the  input  and 
output  sequences  had  to  have  the  same  length.  Encoder–decoder 
was  used  for  addressing  variable  length  sequence-to-sequence  pro-
blems  such  as  machine  translation  or  speech  recognition  where  the 
input  sequence  and  output  sequence  lengths  may  not  be  the  same 
in  most  of  the  cases.  Encoder  and  decoder  are  both  RNNs  where 
the  encoder  RNN  encodes  the  whole  input  X  = x ð1Þ,  . . .::, x ðnx Þ 
into  a  context  vector  c  and  outputs  the  context  vector  c  which  is 
fed  as  an  input  to  the  decoder  RNN.  The  decoder  RNN  generates 
an  output  sequence  Y  = y ð1Þ,  . . .::, y ðny Þ.  In  the  encoder–decoder 
model,  the  input  length  xðnx Þ  and  the  output  length  y ðny Þ  can  be 
different  unlike  the  previous  RNN  models.  The  number  of  hidden 
layers  in  encoder  and  decoder  are  not  necessarily  be  the  same.  The 
limitation  of  this  architecture  is  that  it  fails  to  properly  summarize  a

---

<!-- PAGE 12 -->

128

Susmita Das et al.

long  sequence  if  the  context  vector  is  too  small.  This  problem  was 
solved  by  Bahdanau  et  al.  (2015)  [11]  by  making  the  context  vector 
a  variable  length  sequence  with  added  attention  mechanism.

2.7  Attention  Models 
(Transformers)

to

Due  to  the  sequential 
learning  mechanism,  the  context  vector 
generated  by  the  encoder  (see  Subheading  2.6)  is  more  focused 
on  the  later  part  of  the  sequence  than  on  the  earlier  part.  An 
the  encoder–decoder  model  was  proposed  by 
extension 
Bahdanau  et  al.  [11]  for  machine  translation  where  the  model 
generates  each  word  based  on  the  most  relevant  information  in 
the  source  sentence  and  previously  generated  words.  Unlike  the 
previous  encoder–decoder  model  where  the  whole  input  sequence 
is  encoded  into  a  single  context  vector,  this  extended  encoder– 
decoder  model  learns  to  give  attention  to  the  relevant  words  pres-
ent 
in  the 
sequence  by  encoding  the  input  sequence  into  sequences  of  vectors 
and  chooses  selectively  while  decoding  each  word.  This  mechanism 
of  paying  attention  to  the  relevant  information  that  are  related  to 
each  word  is  known  as  attention  mechanism.

in  the  source  sequence  regardless  of  the  position

Although  this  model  solves  the  problem  for  ﬁxed-length  con-
text  vectors,  the  sequential  decoding  problem  still  persists.  To 
decode  the  sequence  in  less  time  by  introducing  parallelism,  self-
attention  was  proposed  by  Google  Brain  team,  Ashish  Vaswani  et  al. 
[12].  They  invented  the  Transformer  model  which  is  based  on  self-
attention  mechanism  and  was  designed  to  reduce  the  computation 
time.  It  computes  the  representation  of  a  sequence  that  relates  to 
different  positions  of  the  same  sequence.  The  self-attention  mech-
anism  was  embedded  in  the  Transformer  model.  The  Transformer 
model  has  a  stack  of  six  identical  layers  each  for  encoding  the 
sequence  and  decoding  the  sequence  as  illustrated  in  Fig.  8.  Each 
layer  of  the  encoder  and  decoder  has  sub-layers  comprising  multi-
head  self-attention  mechanisms  and  position-wise  fully  connected 
layers.  There  is  a  residual  connection  around  the  two  sub-layers 
followed  by  normalization.  In  addition  to  the  two  sub-layers,  there 
is  a  third  layer  in  the  decoder  that  performs  multi-head  attention 
over  the  output  of  the  encoder  stack.  In  the  decoder,  the  multi-
head  attention  is  masked  to  prevent  the  position  from  attending  the 
later  part  of  the  sequence.  This  ensures  that  the  prediction  for  a 
position  p  depends  only  on  the  positions  less  than  p  in  the  sequence. 
The  attention  function  can  be  described  as  mapping  a  query  and 
key-value  pairs  to  an  output.  All  the  parameters  involved  in  the 
computation  are  all  vectors.  To  calculate 
the  output,  scalar 
dot  product  operation  is  performed  on  the  query  and  all  keys, 
and  divide  each  key  by 
is  the  dimension  on 
it  to  obtain  the 
the  keys).  Finally,  the  softmax 
weights  on  the  values.  The  computation  of  attention  function 
equation:
can

(where  dk 
is  applied  to

represented

following

the

by

be

dk

p

---

<!-- PAGE 13 -->

RNN Architectures and Research

129

Output

Decoder

Decoder

Decoder

Decoder

Decoder

Decoder

Encoder

Encoder

Encoder

Encoder

Encoder

Encoder

Input

Fig.  8  Transformer  with  six  layers  of  encoders  and  six  layers  of  decoders

AttentionðQ  , K , V Þ = sof  tmaxð QK T

p  ÞV ,  where  Q,  K,  and  V are

dk

all  matrices  corresponding  to  query,  keys,  and  values,  respectively.  A 
more  in-depth  coverage  of  Transformers  is  provided  in  Chap.  6.

3

Tips  and  Tricks  for  RNN  Training

As  previously  stated,  the  vanishing  gradient  and  exploding  gradient 
problems  are  well-known  concerns  when 
it  comes  to  properly 
training  RNN  models  [13,  14].  The  fundamental  challenge  arises 
from  the  fact  that  RNNs  can  be  naturally  unfolded,  allowing  their 
recurrent  connections  to  perform  feedforward  calculations,  which 
result  in  an  RNN  with  the  same  number  of  layers  as  the  number  of 
elements  in  the  sequence.  Two  major  issues  arise  as  a  result:

---

<!-- PAGE 14 -->

130

Susmita Das et al.

3.1  Skip  Connection

(cid:129) Gradient  vanishing  problem.  It  becomes  difﬁcult  to  effectively 
learn  long-term  dependencies  in  sequences  due  to  the  gradient 
vanishing  problem  [6].  As  a  result,  a  prospective  model  predic-
tion  will  be  essentially  unaffected  by  earlier  layers.

(cid:129) Exploding  gradient  problem.  Adding  more  layers  to  the  network 
ampliﬁes  the  effect  of  large  gradients,  increasing  the  risk  of  a 
learning  derailment  since  signiﬁcant  changes  to  the  network 
weights  can  be  performed  at  each  step,  potentially  causing  the 
gradients  to  blow  out  exponentially.  In  fact,  weights  that  are 
closer  to  the  input  layer  will  obtain  larger  updates  than  weights 
that  are  closer  to  the  output  layer,  and  the  network  may  become 
unable  to  learn  correlations  between  temporally  distant  events.

To  overcome  these  limitations,  we  need  to  create  solutions  so 
that  the  RNN  model  can  work  on  various  time  scales,  with  some 
sections  operating  on  ﬁne-grained  time  scales  and  handling  small 
details  and  others  operating  on  coarse  time  scales  and  efﬁciently 
transferring  information  from  the  distant  past  to  the  present.  In  this 
section,  we  discuss  several  popular  strategies  to  tackle  these  issues.

The  practice  of  skipping  layers  effectively  simpliﬁes  the  network  by 
using  fewer  direct  connected  layers  in  the  initial  training  stages. 
This  speeds  learning  by  reducing  the  impact  of  vanishing  gradients, 
as  there  are  fewer  layers  to  propagate  through.  As  the  network 
learns  the  feature  space  during  the  training  phase,  it  gradually 
restores  the  skipped  layers.  Lin  et  al.  [15]  proposed  the  use  of 
such  skip  connections,  which  follows  from  the  idea  of  incorporating 
delays  in  feedforward  neural  networks  from  Lang  et  al.  [16].  Con-
ceptually,  skip  connections  are  a  standard  module  in  deep  architec-
tures  and  are  commonly  referred  to  as  residual  networks,  as 
described  by  He  et  al.  [17].  They  are  responsible  to  skip  layers  in 
the  neural  network  and  feeding  the  output  of  one  layer  as  the  input 
to  the  next  layers.  This  technique  is  used  to  allow  gradients  to  ﬂow 
through  a  network  directly,  without  passing  through  non-linear 
activation  functions,  and  it  has  been  empirically  proven  that  these 
additional  steps  are  often  beneﬁcial  for  the  model  convergence 
[17].  Skip  connections  can  be  used  through  the  non-sequential 
layer  in  two  fundamental  ways  in  neural  networks:
(cid:129) Additive  Skip  Connections.  In  this  type  of  design,  the  data 
from  early  layers  is  transported  to  deeper  layers  via  matrix  addi-
tion,  causing  back-propagation 
to  be  done  via  addition 
(Fig.  9b).  This  procedure  does  not  require  any  additional  para-
meters  because  the  output  from  the  previous  layer  is  added  to 
the  layer  ahead.  One  of  the  most  common  techniques  used  in 
this  type  of  architecture  is  to  stack  the  skip  residual  blocks 
together  and  use  an  identity  function  to  preserve  the  gradient 
[18].  The  core  concept  is  to  use  a  vector  addition  to  back-

---

<!-- PAGE 15 -->

RNN Architectures and Research

131

Fig.  9  Skip  connection  residual  architectures:  (a)  concatenate  output  of  previous  layer  and  skip  connection;  (b) 
sum  of  the  output  of  previous  layer  and  skip  connection

propagate  through  the  identity  function.  The  gradient  is  then 
simply  multiplied  by  one,  and  its  value  is  preserved  in  the  earlier 
layers.

(cid:129) Concatenative  Skip  Connections.  Another  way  for  establish-
ing  skip  connections  is  to  concatenate  previous  feature  maps. 
The  aim  of  concatenation  is  to  leverage  characteristics  acquired 
in  prior  layers  to  deeper  layers.  In  addition,  concatenating  skip 
connections  provides  an  alternate  strategy  for  assuring  feature 
reusability  of  the  same  dimensionality  from  prior  layers  without 
the  need  to  learn  duplicate  maps.  Figure  9(a)  illustrates  a  dia-
gram  example  of  how  the  architecture  looks  like.  The  primary 
concept  of  the  architecture  is  to  allow  subsequent  layers  to  reuse 
intermediary  representations,  allowing  them  to  maintain  more 
information  and  enhance  long-term  dependency  performance.

3.2

Leaky  Units

One  of  the  major  challenges  when  training  RNNs  is  capturing 
long-term  dependencies  and  efﬁciently  transferring  information 
from  distant  past  to  present.  An  effective  method  to  obtain  coarse 
time  scales  is  to  employ  leaky  units  [19],  which  are  hidden  units 
with  linear  self-connections  and  a  weight  on  the  connections  that  is 
close  to  one.  In  a  leaky  RNN,  hidden  units  are  able  to  access  values 
from  prior  states  and  can  be  utilized  to  obtain  temporal  representa-
tions.  Formula  ht = α  ht-1 + (1 - α)  ht  expresses  the  state  update

(cid:2)

(cid:2)

---

<!-- PAGE 16 -->

132

Susmita Das et al.

3.3  Clipping 
Gradients

rule  of  a  leaky  unit,  where  α ∈ (0,  1)  is  an  example  of  a  linear  self-
connection  from  ht-1  to  ht,  and  it  is  a  parameter  to  be  learned 
during  the  training  stage.  Essentially,  α  controls  the  information 
ﬂow  in  the  state.  When  α  is  near  one,  the  state  is  almost  unchanged, 
and  information  about  the  past  is  retained  for  a  long  time,  and 
when  α  is  close  to  zero,  the  information  about  the  past  is  rapidly 
discarded,  and  the  state  is  largely  replaced  by  a  new  state  ht.

Gradient  clipping  is  a  technique  that  tries  to  overcome  the  explod-
ing  gradient  problem  in  RNN  training,  by  constraining  gradient 
norms  (element-wise)  to  a  predetermined  minimum  or  maximum 
threshold  value  since  the  exploding  gradients  are  clipped  and  the 
optimization  begins  to  converge  to  the  minimum  point.  Gradient 
clipping  can  be  used  in  two  fundamental  ways:

(cid:129) Clipping-by-value.  Using  this  technique,  we  deﬁne  a  minimum 
clip  value  and  a  maximum  clip  value.  If  a  gradient  exceeds  the 
threshold  value,  we  clip  the  gradient  to  the  maximum  threshold. 
If  the  gradient  is  less  than  the  lower  limit  of  the  threshold,  we 
clip  the  gradient  to  the  minimum  threshold.

(cid:129) Clipping-by-norm.  The

idea  behind  this  technique

is  very 
similar  to  clipping-by-value.  The  key  difference  is  that  we  clip 
the  gradients  by  multiplying  the  unit  vector  of  the  gradients  with 
the  threshold.  Gradient  descent  will  be  able  to  behave  properly 
even  if  the  loss  landscape  of  the  model  is  irregular  since  the 
weight  updates  will  also  be  rescaled.  This  signiﬁcantly  reduces 
the  likelihood  of  an  overﬂow  or  underﬂow  of  the  model.

4  RNN  Applications  in  Language  Modeling

Language  modeling  is  the  process  of  learning  meaningful  vector 
representations  for  language  or  text  using  sequence  information 
and  is  generally  trained  to  predict  the  next  token  or  word  given  the 
input  sequence  of  tokens  or  words.  Bengio  et  al.  [20]  proposed  a 
framework  for  neural  network-based  language  modeling.  RNN 
architecture  is  particularly  suited  to  processing  free-ﬂowing  natural 
language  due  to  its  sequential  nature.  As  described  by  Mikolov  et  al. 
[21],  RNNs  can  learn  to  compress  a  whole  sequence  as  opposed  to 
feedforward  neural  networks  that  compress  only  a  single  input 
item.  Language  modeling  can  be  an  independent  task  or  be  part 
of  a  language  processing  pipeline  with  downstream  prediction  or 
classiﬁcation  task.  In  this  section,  we  will  discuss  applications  of 
RNN  for  various  language  processing  tasks.

---

<!-- PAGE 17 -->

4.1 
Text 
Classiﬁcation

4.2 
Text 
Summarization

Extractive  Text

4.2.1 
Summarization

RNN Architectures and Research

133

Many  interesting  real-world  applications  concerning  language  data 
can  be  modeled  as  text  classiﬁcation.  Examples  include  sentiment 
classiﬁcation,  topic  or  author  identiﬁcation,  and  spam  detection 
from  marketing  to  query-answering 
with  applications  ranging 
[22,  23].  In  general,  models  for  text  classiﬁcation  include  some 
RNN  layers  to  process  sequential  input  text  [22,  23].  The  embed-
ding  of  the  input  learnt  by  these  layers  is  later  processed  through 
varying  classiﬁcation  layers  to  predict  the  ﬁnal  class  label.  Many-to-
one  RNN  architectures  are  often  employed  for  text  classiﬁcation.

As  a  recent  technical  innovation,  RNNs  have  been  combined 
with  convolutional  neural  networks  (CNNs),  thus  combining  the 
strengths  of  two  architectures,  to  process  textual  data  for  classiﬁca-
tion  tasks.  LSTMs  are  popular  RNN  architecture  for  processing 
textual  data  because  of  their  ability  to  track  patterns  over  long 
sequences,  while  CNNs  have  the  ability  to  learn  spatial  patterns 
from  data  with  two  or  more  dimensions.  Convolutional  LSTM 
(C-LSTM)  combines  these  two  architectures  to  form  a  powerful 
architecture  that  can  learn  local  phrase-level  patterns  as  well  as 
global  sentence-level  patterns  [24].  While  CNN  can  learn  local 
and  position-invariant  features  and  RNN  is  good  at  learning  global 
patterns,  another  variation  of  RNN  has  been  proposed  to  introduce 
position-invariant  local  feature  learning  into  RNN.  This  variation  is 
Information  ﬂow 
called  disconnected  RNN 
between  tokens/words  at  the  hidden  layer  is  limited  by  a  hyper-
parameter  called  window  size,  allowing  the  developer  to  choose  the 
width  of  the  context  to  be  considered  while  processing  text.  This 
architecture  has  shown  better  performance  than  both  RNN  and 
CNN  on  several  text  classiﬁcation  tasks  [25].

(DRNN)  [25].

Text  summarization  approaches  can  be  broadly  categorized  into 
(1)  extractive  and  (2)  abstractive  summarization.  The  ﬁrst  approach 
relies  on  selection  or  extraction  of  sentences  that  will  be  part  of  the 
summary,  while  the  latter  generates  new  text  to  build  a  summary. 
RNN  architectures  have  been  used  for  both  types  of  summarization 
techniques.

Extractive  summarization  frameworks  use  many-to-one  RNN  as  a 
classiﬁer  to  distinguish  sentences  that  should  be  part  of  the  sum-
mary.  For  example,  a  two-layer  RNN  architecture  is  presented  in 
[26]  where  one  layer  processes  words  in  one  sentence  and  the  other 
layer  processes  many  sentences  as  a  sequence.  The  model  generates 
sentence-level  labels  indicating  whether  the  sentence  should  be  part 
of  the  summary  or  not,  thus  producing  an  extractive  summary  of 
the  input  document.  Xu  et  al.  have  presented  a  more  sophisticated 
extractive  summarization  model  that  not  only  extracts  sentences  to 
be  part  of  the  summary  but  also  proposes  possible  syntactic  com-
pressions  for  those  sentences  [27].  Their  proposed  architecture  is  a

---

<!-- PAGE 18 -->

134

Susmita Das et al.

Abstractive  Text

4.2.2 
Summarization

4.3  Machine 
Translation

combination  of  CNN  and  bidirectional  LSTM,  while  a  neural 
classiﬁer  evaluates  possible  syntactic  compressions  in  the  context 
of  the  sentence  as  well  as  the  broader  context  of  the  document.

Abstractive  summarization  frameworks  expect  the  RNN  to  process 
input  text  and  generate  a  new  sequence  of  text  that  is  the  summary 
of  input  text,  effectively  using  many-to-many  RNN  as  a  text  gener-
ation  model.  While  it  is  relatively  straightforward  for  extractive 
summarizers  to  achieve  basic  grammatical  correctness  as  correct 
sentences  are  picked  from  the  document  to  generate  a  summary, 
it  has  been  a  major  challenge  for  abstractive  summarizers.  Gram-
matical  correctness  depends  on  the  quality  of  the  text  generation 
module.  Grammatical  correctness  of  abstractive  text  summarizers 
has 
in  contextual  text 
processing,  language  modeling,  as  well  as  availability  of  computa-
tional  power  to  process  large  amounts  of  text.

improved  recently  due  to  developments

Handling  of  rare  tokens/words  is  a  major  concern  for  modern 
abstractive  summarizers.  For  example,  proper  nouns  such  as  speciﬁc 
names  of  people  and  places  occur  less  frequently  in  the  text;  how-
ever,  generated  summaries  are  incomplete  and  incomprehensible  if 
such  tokens  are  ignored.  Nallapati  et  al.  proposed  a  novel  solution 
composed  of  GRU-RNN 
layers  with  attention  mechanism  by 
including  switching  decoder  in  their  abstractive  summarizer  archi-
tecture  [28]  where  the  text  generator  module  has  a  switch  which 
can  enable  the  module  to  choose  between  two  options:  (1)  generate 
a  word  from  the  vocabulary  and  (2)  point  to  one  of  the  words  in  the 
input  text.  Their  model  is  capable  of  handling  rare  tokens  by 
pointing  to  their  position  in  the  original  text.  They  also  employed 
large  vocabulary  trick  which  limits  the  vocabulary  of  the  generator 
module  to  tokens  of  the  source  text  only  and  then  adds  frequent 
tokens  to  the  vocabulary  set  until  its  size  reaches  a  certain  thresh-
old.  This  trick  is  useful  in  limiting  the  size  of  the  network.

Summaries  have  latent  structural  information,  i.e.,  they  convey 
information  following  certain  linguistic  structures  such  as  “What-
Happended”  or  “Who-Action-What.”  Li  et  al.  presented  a  recur-
rent  generative  decoder  based  on  variational  auto-encoder  (VAE) 
[29].  VAE  is  a  generative  model  that  takes  into  account  latent 
variables,  but  is  not  inherently  sequential  in  nature.  With  the  his-
torical  dependencies  in  latent  space,  it  can  be  transformed  into  a 
sequential  model  where  generative  output  is  taking  into  account 
history  of  latent  variables,  hence  producing  a  summary  following 
latent  structures.

Neural  machine  translation  (NMT)  models  are  trained  to  process 
input  sequence  of  text  and  generate  an  output  sequence  which  is 
language.  As 
the  translation  of  the 
is  a  classic 
in  Subheading  2.6,  machine  translation 
mentioned 
example  of  conversion  of  one  sequence  to  another  using  encoder–

input  sequence

in  another

---

<!-- PAGE 19 -->

Image-to-Text

4.4 
Translation

RNN Architectures and Research

135

decoder  architecture  where 
lengths  of  both  sequences  may  be 
different.  In  2014,  many-to-many  RNN-based  encoder–decoder 
architecture  was  proposed  where  one  RNN  encodes  the  input 
sequence  of  text  to  a  ﬁxed-length  vector  representation,  while 
another  RNN  decodes  the  ﬁxed-length  vector  to  the  target  trans-
lated  sequence  [30].  Both  RNNs  are  jointly  trained  to  maximize 
the  conditional  probability  of  the  target  sequence  given  the  input 
sequence.  Later,  attention-based  modeling  was  added  to  vanilla 
encoder–decoder  architecture 
for  machine  translation.  Luong 
et  al.  discussed  two  types  of  attention  mechanism  in  their  work 
on  NMT:  (i)  global  and  (ii)  local  attention  [31].  In  global  atten-
tion,  a  global  context  vector  is  estimated  by  learning  variable  length 
alignment  and  attention  scores  for  all  source  words.  In  local  atten-
tion,  the  model  predicts  a  single  aligned  position  for  the  current 
target  word  and  then  computes  a  local  context  vector  from  atten-
tion  predicted  for  source  words  within  a  small  window  of  the 
aligned  position.  Their  experiments  show  signiﬁcant  improvement 
in  translation  performance  over  models  without  attention.  Local 
attention  mechanism  has  the  advantage  of  being  computationally 
less  expensive  than  global  attention  mechanism.

Image-to-text  translation  models  are  expected  to  convert  visual 
data  (i.e.,  images)  into  textual  data  (i.e.,  words).  In  general,  the 
image  input  is  passed  through  some  convolutional  layers  to  gener-
ate  a  dense  representation  of  the  visual  data.  Then,  the  embedded 
representation  of  the  visual  data  is  fed  to  an  RNN  to  generate  a 
sequence  of  text.  Many-to-one  RNN  architectures  are  popular  for 
this  task.

In  2015,  Karpathy  et  al.  [32]  presented  their  inﬂuential  work 
on  training  region  convolutional  neural  network  (RCNN)  to  gen-
erate  representation  vectors  for  image  regions  and  bidirectional 
RNN  to  generate  representation  vectors  for  corresponding  caption 
in  semantic  alignment  with  each  other.  They  also  proposed  novel 
multi-modal  RNN  to  generate  a  caption  that  is  semantically  aligned 
with  the  input  image.  Image  regions  were  selected  based  on  the 
ranked  output  of  an  object  detection  CNN.

Xu  et  al.  proposed  an  attention-based  framework  to  generate 
image  caption  that  was  inspired  by  machine  translation  models 
[33].  They  used  image  representations  generated  by  lower  convo-
lutional 
last  fully 
layers  from  a  CNN  model  rather  than  the 
connected  layer  and  used  an  LSTM  to  generate  words  based  on 
hidden  state,  last  generated  word,  and  context  vector.  They  deﬁned 
the  context  vector  as  a  dynamic  representation  of  the  image  gener-
ated  by  applying  an  attention  mechanism  on  image  representation 
vectors  from  lower  convolutional  layers  of  CNN.  Attention  mech-
anism  allowed  the  model  to  dynamically  select  the  region  to  focus 
image  caption.  An  additional 
on  while  generating  a  word  for 
intuitive  visualization  of  the
advantage  of  their  approach  was

---

<!-- PAGE 20 -->

136

Susmita Das et al.

model’s  focus  for  generation  of  each  word.  Their  visualization 
experiments  showed  that  their  model  was  focused  on  the  right 
part  of  the  image  while  generating  each  important  word.

Such  inﬂuential  works  in  the  ﬁeld  of  automatic  image  caption-
ing  were  based  on 
image  representations  generated  by  CNNs 
designed  for  object  detection.  Some  recently  proposed  captioning 
models  have  sought  to  change  this  trend.  Biten  et  al.  proposed  a 
illustrate  new  articles 
captioning  model 
[34].  Their  caption  generation  LSTM  takes  into  account  both 
CNN-generated  image  features  and  semantic  embeddings  to  the 
text  of  corresponding  new  articles  to  generate  a  template  of  a 
caption.  This  template  contains  spaces  for  the  names  of  entities 
like  organizations  and  places.  These  places  are  ﬁlled  in  using  atten-
tion  mechanism  on  the  text  of  the  corresponding  article.

images  used

for

to

4.5  ChatBot  for 
Mental  Health  and 
Autism  Spectrum 
Disorder

ChatBots  are  automatic  conversation  tools  that  have  gained  vast 
popularity  in  e-commerce  and  as  digital  personal  assistants  like 
Apple’s  Siri  and  Amazon’s  Alexa.  ChatBots  represent  an  ideal  appli-
cation  for  RNN  models  as  conversations  with  ChatBots  represent 
sequential  data.  Questions  and  answers  in  a  conversation  should  be 
based  on  past  iterations  of  questions  and  answers  in  that  conversa-
tion  as  well  as  patterns  of  sequences  learned  from  other  conversa-
tions  in  the  dataset.

Recently,  ChatBots  have  found  application  in  screening  and 
intervention  for  mental  health  disorders  such  as  autism  spectrum 
disorder  (ASD).  Zhong  et  al.  designed  a  Chinese-language  Chat-
Bot  using  bidirectional  LSTM  in  sequence-to-sequence  framework 
which  showed  great  potential  for  conversation-mediated  interven-
tion  for  children  with  ASD  [35].  They  used  400,000  selected 
sentences 
in  many 
cases.  Rakib  et  al.  developed  similar  sequence-to-sequence  model 
based  on  Bi-LSTM  to  design  a  ChatBot  to  respond  empathetically 
to  mentally  ill  patients  [36].  A  detailed  survey  of  medical  ChatBots 
is  presented  in  [37].  This  survey  includes  references  to  ChatBots 
built  using  NLP  techniques,  knowledge  graphs,  as  well  as  modern 
RNN  for  a  variety  of  applications  including  diagnosis,  searching 
through  medical  databases,  dialog  with  patients,  etc.

from  chatting  histories

involving  children

5  Conclusion

text

summarization,

Due  to  the  sequential  nature  of  their  architecture,  RNNs  are 
applied  for  ordinal  or  temporal  problems,  such  as  language  transla-
tion, 
are 
and 
incorporated  into  popular  applications  such  as  Siri,  voice  search, 
and  Google  Translate.  In  addition,  they  are  also  often  used  to 
analyze  longitudinal  data  in  medical  applications  (i.e.,  cases  where 
repeated  observations  are  available  at  different  time  points  for  each

captioning,

image

and

---

<!-- PAGE 21 -->

RNN Architectures and Research

137

patient  of  a  dataset).  While  research  in  RNN  is  still  an  evolving  area 
and  new  architectures  are  being  proposed,  this  chapter  summarizes 
fundamentals  of  RNN  including  different  traditional  architectures, 
training  strategies,  and  inﬂuential  work.  It  may  serve  as  a  stepping 
stone  for  exploring  sequential  models  using  RNN  and  provides 
reference  pointers.

References

1.  Rumelhart  DE,  Hinton  GE,  Williams  RJ 
representations  by  back-
323(6088):

errors.  Nature

(1986)  Learning 
propagating 
533–536

2.  Hopﬁeld  JJ  (1982)  Neural  networks  and  phys-
ical  systems  with  emergent  collective  computa-
tional  abilities.  Proc  Natl  Acad  Sci  79(8): 
2554–2558

3.  Schmidhuber  J  (1993)  Netzwerkarchitekturen, 
Zielfunktionen  und  Kettenregel 
(Network 
architectures,  objective  functions,  and  chain 
rule),  Habilitation  thesis,  Institut  fu¨r  Informa-
tik,  Technische  Universitu¨t  Mu¨nchen

4.  Mozer  MC  (1995)  A  focused  backpropagation 
algorithm  for  temporal.  Backpropag  Theory 
Architect  Appl  137

5.  Goodfellow  I,  Bengio  Y,  Courville  A  (2016)

Deep  learning.  MIT  Press,  Cambridge

6.  Hochreiter  S  (1998)  The  vanishing  gradient 
problem  during  learning  recurrent  neural  nets 
and  problem  solutions.  Int  J  Uncertainty  Fuzz-
iness  Knowledge  Based  Syst  6(02):107–116 
7.  Hochreiter  S,  Schmidhuber  J  (1997)  Long 
short-term  memory.  Neural  Comput  9(8): 
1735–1780

8.  Cho  K,  Van  Merrie¨nboer  B,  Gulcehre  C, 
Bahdanau  D,  Bougares  F,  Schwenk  H,  Bengio 
representations 
(2014)  Learning  phrase 
Y 
using  RNN  encoder-decoder 
for  statistical 
machine  translation.  Preprint.  arXiv:14061078 
9.  Schuster  M,  Paliwal  KK  (1997)  Bidirectional 
recurrent  neural  networks.  IEEE  Trans  Signal 
Process  45(11):2673–2681

10.  Pascanu  R,  Gulcehre  C,  Cho  K,  Bengio  Y 
(2013)  How  to  construct  deep  recurrent  neu-
ral  networks.  Preprint.  arXiv:13126026

11.  Bahdanau  D,  Cho  K,  Bengio  Y  (2014)  Neural 
machine  translation  by  jointly  learning  to  align 
and  translate.  Preprint.  arXiv:14090473

12.  Vaswani  A,  Shazeer  N,  Parmar  N,  Uszkoreit  J, 
Jones  L,  Gomez  AN,  Kaiser  Ł,  Polosukhin  I 
(2017)  Attention  is  all  you  need.  In:  Advances 
in  neural  information  processing  systems,  pp 
5998–6008

13.  Bengio  Y,  Simard  P,  Frasconi  P

(1994) 
Learning  long-term  dependencies  with  gradi-
ent  descent 
is  difﬁcult.  IEEE  Trans  Neural 
Netw  5(2):157–166.  https://doi.org/10.110 
9/72.279181

14.  Pascanu  R,  Mikolov  T,  Bengio  Y  (2013)  On 
the  difﬁculty  of 
recurrent  neural 
training 
networks.  In:  Dasgupta  S,  McAllester  D  (eds) 
Proceedings  of  the  30th  international  confer-
ence  on  machine  learning,  PMLR,  Atlanta,  vol 
28,  pp  1310–1318

15.  Berger  AL,  Pietra  VJD,  Pietra  SAD  (1996)  A 
maximum  entropy  approach  to  natural 
lan-
guage  processing.  Comput  Linguist  22(1): 
39–71

surfaces

that  discovers

16.  Becker  S,  Hinton  G  (1992)  Self-organizing 
neural  network 
in 
random-dot  stereograms.  Nature  355:161– 
163.  https://doi.org/10.1038/355161a0 
17.  He  K,  Zhang  X,  Ren  S,  Sun  J  (2016)  Deep 
residual 
image  recognition.  In: 
2016  IEEE  conference  on  computer  vision 
pp 
recognition 
and 
770–778.  https://doi.org/10.1109/CVPR. 
2016.90

learning  for

(CVPR),

pattern

18.  Wu  H,  Zhang  J,  Zong  C  (2016)  An  empirical 
exploration  of  skip  connections  for  sequential 
tagging.  Preprint.  arXiv:161003167

19.  Jaeger  H  (2002)  Tutorial  on  training  recurrent 
neural  networks,  covering  BPPT,  RTRL,  EKF 
and 
approach. 
echo 
GMD-Forschungszentrum 
Informationstechnik  5

state  network

the

20.  Bengio  Y,  Ducharme  R,  Vincent  P  (2001)  A 
neural  probabilistic 
In: 
Advances  in  neural  information  processing  sys-
tems,  pp  932–938

language  model.

21.  Mikolov  T,  Karaﬁa´t  M,  Burget  L  et  al  (2010) 
language

Recurrent  neural  network  based 
model.  In:  INTERSPEECH  2010.  Citeseer 
22.  Jain  G,  Sharma  M,  Agarwal  B  (2019)  Optimiz-
ing  semantic  lstm  for  spam  detection.  Int  J 
Inform  Technol  11(2):239–250

---

<!-- PAGE 22 -->

138

Susmita Das et al.

23.  Bagnall  D  (2015)  Author  identiﬁcation  using 
multi-headed  recurrent  neural  networks.  Pre-
print.  arXiv:150604891

24.  Zhou  C,  Sun  C,  Liu  Z,  Lau  F  (2015)  A 
C-LSTM  neural  network  for  text  classiﬁcation. 
Preprint.  arXiv:151108630

25.  Wang  B  (2018)  Disconnected  recurrent  neural 
networks  for  text  categorization.  In:  Proceed-
ings  of  the  56th  annual  meeting  of  the  associa-
tion  for  computational  linguistics  (volume  1: 
long  papers),  pp  2311–2320

26.  Nallapati  R,  Zhai  F,  Zhou  B  (2017)  Summar-
unner:  a 
recurrent  neural  network  based 
sequence  model  for  extractive  summarization 
of  documents.  In:  Thirty-ﬁrst  AAAI  conference 
on  artiﬁcial  intelligence

27.  Xu  J,  Durrett  G  (2019)  Neural  extractive  text 
syntactic  compression.

summarization  with 
Preprint.  arXiv:190200863

28.  Nallapati  R,  Zhou  B,  dos  Santos  C,  Gulcehre 
C¸  ,  Xiang  B  (2016)  Abstractive  text  summariza-
tion  using 
rnns  and 
sequence-to-sequence 
beyond.  In:  Proceedings  of  the  20th  SIGNLL 
conference  on  computational  natural  language 
learning,  pp  280–290

29.  Li  P,  Lam  W,  Bing  L,  Wang  Z  (2017)  Deep 
recurrent  generative  decoder 
for  abstractive 
text  summarization.  In:  Proceedings  of  the 
2017  conference  on  empirical  methods  in  nat-
ural  language  processing,  pp  2091–2100 
30.  Cho  K,  van  Merrienboer  B,  Gu¨lc¸ehre  C¸ ,  
Bahdanau  D,  Bougares  F,  Schwenk  H,  Bengio 
representations 
Y 
(2014)  Learning  phrase 
for  statistical 
using  RNN  encoder-decoder 
machine  translation.  In:  The  2014  conference 
on  empirical  methods  in  natural  language  pro-
cessing  (EMNLP)

31.  Luong  MT,  Pham  H,  Manning  CD  (2015) 
Effective  approaches  to  attention-based  neural 
machine
Preprint. 
translation.
arXiv:150804025

32.  Karpathy  A,  Fei-Fei  L  (2015)  Deep  visual-
semantic  alignments 
image 
descriptions.  In:  Proceedings  of  the  IEEE  con-
ference  on  computer  vision  and  pattern  recog-
nition,  pp  3128–3137

for  generating

33.  Xu  K,  Ba  J,  Kiros  R,  Cho  K,  Courville  A, 
Salakhudinov  R,  Zemel  R,  Bengio  Y  (2015) 
Show,  attend  and  tell:  neural  image  caption 
generation  with  visual  attention.  In:  Interna-
tional  conference  on  machine  learning,  PMLR, 
pp  2048–2057

34.  Biten  AF,  Gomez  L,  Rusinol  M,  Karatzas  D 
(2019)  Good  news,  everyone!  context  driven 
entity-aware  captioning  for  news  images.  In: 
Proceedings  of  the  IEEE/CVF  conference  on 
computer  vision  and  pattern  recognition,  pp 
12466–12475

35.  Zhong  H,  Li  X,  Zhang  B,  Zhang  J  (2020)  A 
general  chinese  chatbot  based  on  deep  learning 
and  its’  application  for  children  with  ASD.  Int  J 
Mach  Learn  Comput  10:519–526.  https:// 
doi.org/10.18178/ijmlc.2020.10.4.967 
36.  Rakib  AB,  Rumky  EA,  Ashraf  AJ,  Hillas  MM, 
Rahman  MA  (2021)  Mental  healthcare  chatbot 
using 
and 
bilstm.  In:  Brain  informatics,  springer  interna-
tional  publishing,  pp  378–387

sequence-to-sequence

learning

37.  Tjiptomongsoguno  ARW,  Chen  A,  Sanyoto 
HM,  Irwansyah  E,  Kanigoro  B  (2020)  Medical 
chatbot  techniques:  a  review.  In:  Silhavy  R, 
Silhavy  P,  Prokopova  Z  (eds)  Software  engi-
neering  perspectives 
systems. 
in 
Springer  International  Publishing,  Cham,  pp 
346–356

intelligent

Open Access This chapter is licensed under the terms of the Creative Commons Attribution 4.0 International
License (
), which permits use, sharing, adaptation, distribution
and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons license and indicate if changes were made.

http://creativecommons.org/licenses/by/4.0/

The images or other third party material in this chapter are included in the chapter’s Creative Commons license,
unless indicated otherwise in a credit line to the material. If material is not included in the chapter’s Creative
Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Chapter 4
Recurrent Neural Networks (RNNs): Architectures, Training
Tricks, and Introduction to Influential Research
Susmita Das, Amara Tariq, Thiago Santos, Sai Sandeep Kantareddy,
and Imon Banerjee
Abstract
Recurrent neural networks (RNNs) are neural network architectures with hidden state and which use
feedback loops to process a sequence of data that ultimately informs the final output. Therefore, RNN
models can recognize sequential characteristics in the data and help to predict the next likely data point in
the data sequence. Leveraging the power of sequential data processing, RNN use cases tend to be
connected to either language models or time-series data analysis. However, multiple popular RNN
architectures have been introduced in the field, starting from SimpleRNN and LSTM to deep RNN, and
applied in different experimental settings. In this chapter, we will present six distinct RNN architectures and
will highlight the pros and cons of each model. Afterward, we will discuss real-life tips and tricks for training
the RNN models. Finally, we will present four popular language modeling applications of the RNN
models –text classification, summarization, machine translation, and image-to-text translation– thereby
demonstrating influential research in the field.
Key words Recurrent neural network (RNN), LSTM, GRU, Bidirectional RNN (BRNN), Deep
RNN, Language modeling
1 Introduction
Recurrent neural network (RNN) is a specialized neural network
with feedback connection for processing sequential data or time-
series data in which the output obtained is fed back into it as input
along with the new input at every time step. The feedback connec-
tion allows the neural network to remember the past data when
processing the next output. Such processing can be defined as a
recurring process, and hence the architecture is also known as
recurring neural network.
RNN concept was first proposed by Rumelhart et al. [1] in a
letter published by Nature in 1986 to describe a new learning
procedure with a self-organizing neural network. Another impor-
tant historical moment for RNNs is the (re-)discovery of Hopfield
Olivier Colliot (ed.), Machine Learning for Brain Disorders, Neuromethods, vol. 197, https://doi.org/10.1007/978-1-0716-3195-9_4,
© The Author(s) 2023
117

118 SusmitaDasetal.
networks which is a special kind of RNN with symmetric connec-
tions where the weight from one node to another and from the
latter to the former are the same (symmetric). The Hopfield net-
work [2] is fully connected, so every neuron’s output is an input to
all the other neurons, and updating of nodes happens in a binary
way (0/1). These types of networks were specifically designed to
simulate the human memory.
The other types of RNNs are input-output mapping networks,
which are used for classification and prediction of sequential data.
In 1993, Schmidhuber et al. [3] demonstrated credit assignment
across the equivalent of 1,200 layers in an unfolded RNN and
revolutionized sequential modeling. In 1997, one of the most
popular RNN architectures, the long short-term memory
(LSTM) network which can process long sequences, was proposed.
In this chapter, we summarize the six most popular contempo-
rary RNN architectures and their variations and highlight the pros
and cons of each. We also discuss real-life tips and tricks for training
the RNN models, including various skip connections and gradient
clipping. Finally, we highlight four popular language modeling
applications of the RNN models –text classification, summariza-
tion, machine translation, and image-to-text translation– thereby
demonstrating influential research in each area.
2 Popular RNN Architectures
In addition to the SimpleRNN architecture, many variations were
proposed to address different use cases. In this section, we will
unwrap some of the popular RNN architectures like LSTM,
GRU, bidirectional RNN, deep RNN, and attention models and
discuss their pros and cons.
2.1 SimpleRNN SimpleRNN architecture, which is also known as SimpleRNN,
contains a simple neural network with a feedback connection. It
has the capability to process sequential data of variable length due
to the parameter sharing which generalizes the model to process
sequences of variable length. Unlike feedforward neural networks
which have separate weights for each input feature, RNN shares the
same weights across several time steps. In RNN, the output of a
present time step depends on the previous time steps and is
obtained by the same update rule which is used to obtain the
previous outputs. As we will see, the RNN can be unfolded into a
deep computational graph in which the weights are shared across
time steps.
The RNN operating on an input sequence x(t) with a time step
index t ranging from 1 to τ is illustrated in Fig. 1. The time step
index t may not necessarily refer to the passage of time in the real
world; it can refer to the position in the sequence. The cycles in the

|     |     |     | RNNArchitecturesandResearch |      |         | 119 |
| --- | --- | --- | --------------------------- | ---- | ------- | --- |
| o   |     |     | o(t-1)                      | o(t) | o(t+1)  |     |
Unfold
| h   |     | h(....) | h(t-1) | h(t) | h(t+1)  | h(....) |
| --- | --- | ------- | ------ | ---- | ------- | ------- |
| x   |     |         | x(t-1) | x(t) | x(t+1)  |         |
Fig. 1 (Left) Circuit diagram for SimpleRNN with input x being incorporated into hidden state h with a feedback
connection and an output o. (Right) The same SimpleRNN network shown as an unfolded computational graph
with nodes at every time step
computational  graph  represent  the  impact  of  the  past  value  of  a
variable  on  the  present  time  step.  The  computational  graph  has  a
repetitive  structure  that  unfolds  the  recursive  computation  of  the
RNN which corresponds to a chain of events. It shows the flow  of
the information, forward in the time of computing the outputs and
losses and backward when computing the gradients. The unfolded
computational  graph  is  shown  in  Fig.  1.  The  equation
|     |                |          |                |        | h(t) =f(h(t-1) ,  | x(t) ;  |
| --- | -------------- | -------- | -------------- | ------ | ----------------- | ------- |
|     | corresponding  | to  the  | computational  | graph  | is                |         |
W),  where  h  is  the  hidden  state  of  the  network,  x  is  the  input,  t  is
the  time  step,  and  W  denotes  the  weights  of  the  network  connec-
tions  comprising  of  input-to-hidden,  hidden-to-hidden,  and
hidden-to-output connection weights.
2.1.1  Training  Training is performed by gradient computation of the loss function
Fundamentals  with  respect  to  the  parameters  involved  in  forward  propagation
from  left  to  right  of  the  unrolled  graph  followed  by  back-
propagation  moving  from  right  to  left  through  the  graph.  Such
gradient  computation  is  an  expensive  operation  as  the  runtime
cannot be reduced by parallelism because the forward propagation
is sequential in nature. The states computed in the forward pass are
stored  until  they  are  reused  in  the  back-propagation.  The  back-
propagation  algorithm  applied  to  RNN  is  known  as  back-propa-
gation through time (BPTT) [4].
|     | The  following  | computational  |     | operations  | are  performed  | in  |
| --- | --------------- | -------------- | --- | ----------- | --------------- | --- |
RNN  during  the  forward  propagation  to  calculate  the  output  and
the loss.
|     |     | ðtÞ =b þ    |       | ðt-1Þþ  | ðtÞ  |     |
| --- | --- | ----------- | ----- | ------- | ---- | --- |
|     |     | a           | Wh    |         | Ux   |     |
|     |     | ðtÞ =tanhða | ðtÞÞ  |         |      |     |
h
ðtÞ
|     |     | o ðtÞ =c þ  | Vh   |     |     |     |
| --- | --- | ----------- | ---- | --- | --- | --- |
|     |     | y^ðtÞ =σðo  | ðtÞÞ |     |     |     |

120 SusmitaDasetal.
where b and c are the biases and U, V, and W are the weight matrix
for input-to-hidden connections, hidden-to-output connection,
and hidden-to-hidden connections respectively, and σ is a sigmoid
function. The total loss for a sequence of x values and its
corresponding y values is obtained by summing up the losses over
all time steps.
τ ð Þ
L ðtÞ =L ðx ð1Þ , ......,x ðτÞÞ,ðy ð1Þ , ......,y ðτÞÞ
t =1
To minimize the loss, the gradient of the loss function is
calculated with respect to the parameters associated with it. The
parameters associated with the nodes of the computational graph
are U, V , W, b, c, x(t) , h(t) , o(t), and L(t) . The output o(t) is the
argument to the softmax to obtain the vector y^ of probabilities over
the output. During back-propagation, the gradient for each node is
calculated recursively starting with the nodes preceding the final
loss. It is then iterated backward in time to back-propagate gradi-
ents through time. tanh is a popular choice for activation function
as it tends to avoid vanishing gradient problem by retaining
non-zero value longer through the back-propagation process.
2.1.2 SimpleRNN Variations of SimpleRNN can be designed depending upon the
Architecture Variations style of graph unrolling and parameter sharing [5]:
Based on Parameter
Sharing
(cid:129) Connection between hidden units. The RNN produces outputs at
every time step, and the parameters are passed between hidden-
to-hidden units (Fig. 2a). This corresponds to the standard
SimpleRNN presented above and is widely used.
(cid:129) Connection between outputs to hidden units. The RNN produces
outputs at every time step, and the parameters are passed from
an output at a particular time step to the hidden unit at the next
time step (Fig. 2b).
(cid:129) Sequential input to single output. The RNN produces a single
output at the end after reading the entire sequence and has
connections between the hidden units at every time step
(Fig. 2c).
2.1.3 SimpleRNN Different variations also exist depending on the number of inputs
Architecture Variations and outputs:
Based on Inputs and
(cid:129) One-to-one: The traditional RNN has one-to-one input to out-
Outputs
put mapping at each time step t as shown in Fig. 3a.
(cid:129) One-to-many: One-to-many RNN has one input at a time step
for which it generates a sequence of outputs at consecutive time
steps as shown in Fig. 3b. This type of RNN architecture is often
used for image captioning.

RNNArchitecturesandResearch 121
(a) (b)
o(t-1) o(t) o(t+1) o(....) o(t-1) o(t) o(t+1)
h(....) h(t-1) h(t) h(t+1) h(....) h(....) h(t-1) h(t) h(t+1) h(....)
x(t-1) x(t) x(t+1) x(t-1) x(t) x(t+1)
(c)
o
h(....) h(t-1) h(t) h(t+1) h(....)
x(t-1) x(t) x(t+1)
Fig. 2 Types of SimpleRNN architectures based on parameter sharing: (a) SimpleRNN with connections
between hidden units, (b) SimpleRNN with connections from output to hidden units, and (c) SimpleRNN with
connections between hidden units that read the entire sequence and produce a single output
(cid:129) Many-to-one: Many-to-one RNN has many inputs and one out-
put, at each time step as shown in Fig. 3c. This type of RNN
architecture is used for text classification.
(cid:129) Many-to-many: Many-to-many RNN architecture can be
designed in two ways. First, the input is taken by the RNN and
the corresponding output is given at the same time step as
illustrated in Fig. 3d. This type of RNN is used for named entity
recognition. Second, the input is taken by the RNN at each time
step and the output is given by the RNN at the next time step
depending upon all the input sequence as illustrated in
Fig. 3e. Popular uses of this type of RNN architecture are in
machine translation.
2.1.4 Challenges of SimpleRNN works well with the short-term dependencies, but
Long-Term Dependencies when it comes to long-term dependencies, it fails to remember
in SimpleRNN the long-term information. This problem arises due to the vanish-
ing gradient or exploding gradient [6]. When the gradients are
propagated over many stages, it tends to vanish most of the times
or sometimes explodes. The difficulty arises due to the exponen-
tially smaller weight assigned to the long-term interactions com-
pared to the short-term interactions. It takes very long time to learn
the long-term dependencies as the signals from these dependencies
tend to be hidden by the small fluctuations arising from the short-
term dependencies.

122 SusmitaDasetal.
| (a)   | (b)            |        |         |        | (c)     |         |         |
| ----- | -------------- | ------ | ------- | ------ | ------- | ------- | ------- |
| o(t)  | o(t)           | o(t+1) | o(t+2)  |        |         |         | o(t)    |
| h(t)  | h(t)           | h(t+1) | h(t+2)  |        | h(t–2)  | h(t–1)  | h(t)    |
|       |                |        |         |        |         | x(t–1)  | x(t)    |
| x(t)  | x(t)           |        |         |        | x(t–2)  |         |         |
| (d)   |                |        | (e)     |        |         |         |         |
| o(t)  | o(t+1) o(t+2)  |        |         |        | o(t)    | o(t+1)  | o(t+2)  |
| h(t)  | h(t+1) h(t+2)  |        | h(t–2)  | h(t–1) | h(t)    | h(t+1)  | h(t+2)  |
| x(t)  | x(t+1) x(t+2)  |        | x(t–2)  | x(t–1) | x(t)    |         |         |
Fig. 3 (a) One-to-one RNN. (b) One-to-many RNN. (c) Many-to-one RNN. (d) Many-to-many RNN. (e) Many-to-
many RNN. x represents the input and o represents the output
2.2  Long Short-Term  To address this long-term dependency problem, gated RNNs were
proposed.  Long  short-term  memory  (LSTM)  is  a  type  of  gated
Memory (LSTM)
RNN  which  was  proposed  in  1997  [7].  Due  to  the  property  of
remembering  the  long-term  dependencies,  LSTM  has  been  a  suc-
cessful  model  in  many  applications  like  speech  recognition,
machine  translation,  image  captioning,  etc.  LSTM  has  an  inner
self  loop  in  addition  to  the  outer  recurrence  of  the  RNN.  The
gradients  in  the  inner  loop  can  flow  for  longer  duration  and  are
conditioned on the context rather than being fixed. In each cell, the
input  and  output  is  the  same  as  that  of  ordinary  RNN  but  has  a
system of gating units to control the flow of information. Figure 4
shows the flow of the information in LSTM with its gating units.
LSTM—the
|     |     | There  are  | three  gates  | in  the  |     | external  | input  gate,  |
| --- | --- | ----------- | ------------- | -------- | --- | --------- | ------------- |
the forget gate, and the output gate. The forget gate at time t and
ðtÞ
state  s (f  )  decides  which  information  should  be  removed  from
i  i
the cell  state.  The  gate controls the  self loop by setting  the weight
between 0 and 1 via a sigmoid function σ. When the value is near to
1, the information of the past is retained, and if the value is near  to

RNNArchitecturesandResearch 123
ot
ht
c(t–1) ct
X +
tanh
X
s s tanh s X
h(t–1) ht
xt
Fig. 4 Long short-term memory with cell state ct, hidden state ht , input xt, and output ot
0, the information is discarded. After the forget gate, the internal
state s
ðtÞ
is updated. Computation for external input gate (gt ) is
i i
similar to that of forget gate with a sigmoid function to obtain a
value between 0 and 1 but with its own parameters. The output
gate of the LSTM also has a sigmoid unit which determines
whether to output the value or to shut off the value ht via the
i
output gate qt .
i
f ðtÞ =σ Uf , xt þ Wf , h ðt-1Þ þ bf
i i j j i j j i
j j
s ðtÞ =f t s ðt-1Þ þ gt σ b þ U , xt þ W , h ðt-1Þ
i i i i i i j j i j j
j j
gt =σ bg þ Ug , xt þ Wg , h ðt-1Þ
i i i j j i j j
j j
ht =tanhðst Þqt
i i i
qt =σ bo þ Uo , xt þ Wo , h ðt-1Þ
i i i j i i j j
j
xt is the input vector at time t, h(t) is the hidden layer vector, b
i
denote the biases, and U and W represent the input weights and
i i
the recurrent weights, respectively.

124 SusmitaDasetal.
ht
h(t–1)
X +
Update
1–
Reset gate
X
gate
X
s s
tanh
xt
Fig. 5 Gated recurrent neural network (GRU) with input xt and hidden unit ht
2.3 Gated Recurrent In LSTM, the computation time is large as there are a lot of
Unit (GRU) parameters involved during back-propagation. To reduce the com-
putation time, gated recurrent unit (GRU) was proposed in the
year 2014 by Cho et al. with less gates than in LSTM [8]. The
functionality of the GRU is similar to that of LSTM but with a
modified architecture. The representation diagram for GRU can be
found in Fig. 5. Like LSTM, GRU also solves the vanishing and
exploding gradient problem by capturing the long-term dependen-
cies with the help of gating units. There are two gates in GRU, the
reset gate and the update gate. The reset gate determines how
much of the past information it needs to forget, and the update
gate determines how much of the past information it needs to carry
forward.
The computation at the reset gate (rt ) and the update gate (ut ),
i i
aswell as hidden state (ht ) and the at time t, can berepresented by the
i
following:
r ðtÞ =σðbr þ Ur x ðtÞ þ Wr h ðtÞ Þ
i i i,j j i,j j
j j
u ðtÞ =σðbu þ Uu x ðtÞ þ Wu h ðtÞ Þ
i i i,j j i,j j
j j
h ðtÞ =u ðt-1Þ h ðt-1Þ þð1-u Þ
i i i i
× σðb þ U x ðt-1Þ þ W r ðt-1Þ h ðt-1Þ Þ
i i,j j i,j j j
j j
where b denotes biases and U and W denote initial and recurrent
i i i
weights, respectively.

RNNArchitecturesandResearch 125
When the reset gate value is close to 0, the previous hidden
state value is discarded and reset with the present value. This
enables the hidden state to forget the past information that is
irrelevant for future. The update gate determines how much of
the relevant past information to carry forward for future.
The property of the update gate to carry forward the past
information allows it to remember the long-term dependencies.
For short-term dependencies, the reset gate will be frequently
active to reset with current values and remove the previous ones,
while, for long-term dependencies, the update gate will be often
active for carrying forward the previous information.
2.3.1 Advantage of LSTM The LSTM and GRU can handle the vanishing gradient issue of
and GRU over SimpleRNN SimpleRNN with the help of gating units. The LSTM and GRU
have the additive feature that they retain the past information by
adding the relevant past information to the present state. This
additive property makes it possible to remember a specific feature
in the input for longer time. In SimpleRNN, the past information
loses its relevance when new input is seen. In LSTM and GRU, any
important feature is not overwritten by new information. Instead, it
is added along with the new information.
2.3.2 Differences There are a few differences between LSTM and GRU in terms of
Between LSTM and GRU gating mechanism which in turn result in differences observed in
the content generated. In LSTM unit, the amount of the memory
content to be used by other units of the network is regulated by the
output gate, whereas in GRU, the full content that is generated is
exposed to other units. Another difference is that the LSTM com-
putes the new memory content without controlling the amount of
previous state information flowing. Instead, it controls the new
memory content that is to be added to the network. On the other
hand, the GRU controls the flow of the past information when
computing the new candidate without controlling the candidate
activation.
2.4 Bidirectional In SimpleRNN, the output of a state at time t only depends on the
RNN (BRNN) information of the past x(1), ...., x (t-1) and the present input x(t) .
However, for many sequence-to-sequence applications, the present
state output depends on the whole sequence information. For
example, in language translation, the correct interpretation of the
current word depends on the past words as well as the next words.
To overcome this limitation of SimpleRNN, bidirectional RNN
(BRNN) was proposed by Schuster and Paliwal in the year
1997 [9].
Bidirectional RNNs combine an RNN which moves forward
with time, beginning from the start of the sequence, with another
RNN that moves backward through time, beginning from the end
of the sequence. Figure 6 illustrates a bidirectional RNN with h(t)

126 SusmitaDasetal.
o(t–1) o(t) o(t+1)
g(...) g(t–1) g(t) g(t+1) g(...)
h(...) h(t–1) h(t) h(t+1) h(...)
x(t–1) x(t) x(t+1)
Fig. 6 Bidirectional RNN with forward sub-RNN having ht hidden state and
backward sub-RNN having gt hidden state
the state of the sub-RNN that moves forward through time and g(t)
the state of the sub-RNN that moves backward with time. The
output of the sub-RNN that moves forward is not connected to
the inputs of sub-RNN that moves backward and vice versa. The
output o(t) depends on both past and future sequence data but is
sensitive to the input values around t.
2.5 Deep RNN Deep models are more efficient than their shallow counterparts,
and, with the same hypothesis, deep RNN was proposed by
Pascanu et al. in 2014 [10]. In “shallow” RNN, there are generally
three blocks for computation of parameters: the input state, the
hidden state, and the output state. These blocks are associated with
a single weight matrix corresponding to a shallow transformation
which can be represented by a single-layer multilayer perceptron
(MLP). In deep RNN, the state of the RNN can be decomposed
into multiple layers. Figure 7 shows in general a deep RNN with
multiple deep MLPs. However, different types of depth in an RNN
can be considered separately like input-to-hidden, hidden-to-
hidden, and hidden-to-output layer. The lower layer in the hierar-
chy can transform the input into an appropriate representation for
higher levels of hidden state. In hidden-to-hidden state, it can be
constructed with a previous hidden state and a new input. This
introduces additional non-linearity in the architecture which
becomes easier to quickly adapt changing modes of the input. By
introducing deep MLP in hidden-to-output state makes the layer
compact which helps in summarizing the previous inputs and helps
in predicting the output easily. Due to the deep MLP in the RNN
architecture, the learning becomes slow and optimization is
difficult.

|     |      |     |      |     |      | RNNArchitecturesandResearch |     |       | 127 |
| --- | ---- | --- | ---- | --- | ---- | --------------------------- | --- | ----- | --- |
|     | o    |     | o    |     | o    |                             |     | o     |     |
|     | 1    |     | 2    |     | 3    |                             |     | t     |     |
|     | h(n) |     | h(n) |     | h(n) |                             |     | h(n)  |     |
|     | 1    |     | 2    |     | 3    |                             |     | t     |     |
|     | h(2) |     | h(2) |     | h(2) |                             |     | h(2)  |     |
|     | 1    |     | 2    |     | 3    |                             |     | t     |     |
|     | h(1) |     | h(1) |     | h(1) |                             |     | h(1)  |     |
|     | 1    |     | 2    |     | 3    |                             |     | t     |     |
|     | x    |     | x    |     | x    |                             |     | x     |     |
|     | 1    |     | 2    |     | 3    |                             |     | t     |     |
Fig. 7 Deep recurrent neural network
| Encoder–  |     | Encoder–decoder  |     |     |               |                |     |          |                  |
| --------- | --- | ---------------- | --- | --- | ------------- | -------------- | --- | -------- | ---------------- |
| 2.6       |     |                  |     |     | architecture  | was  proposed  |     | by  Cho  | et  al.  (2014)  |
Decoder  [8]  to  map  a  variable  length  input  sequence  to  a  variable  length
output  sequence.  Therefore,  it  is  also  known  as  sequence-to-
sequence  architecture.  Before  encoder–decoder  was  introduced,
there  were  RNN  models  which  were  used  for  sequence-to-
sequence  applications,  but  they  had  limitations  as  the  input  and
Encoder–decoder
|     |     | output  | sequences  |     | had  to  | have  the  same  | length.  |     |     |
| --- | --- | ------- | ---------- | --- | -------- | ---------------- | -------- | --- | --- |
was used for addressing variable length sequence-to-sequence pro-
blems such as machine translation or speech recognition where the
input  sequence  and  output  sequence  lengths  may  not  be  the  same
in  most  of  the  cases.  Encoder  and  decoder  are  both  RNNs  where
|     |     |      |          |      |          |             |        | =x  | ð1Þ ...::,x ðnx Þ  |
| --- | --- | ---- | -------- | ---- | -------- | ----------- | ------ | --- | ------------------ |
|     |     | the  | encoder  | RNN  | encodes  | the  whole  | input  | X   | ,                  |
into  a  context  vector  c  and  outputs  the  context  vector  c  which  is
fed as an input to the decoder RNN. The decoder RNN generates
an  output  sequence  Y  =y ð1Þ ,  ...::,y ðny Þ .  In  the  encoder–decoder
|     |     |     |     |     |     | ðnx Þ  |     |     | ðny Þ  |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | ------ |
model,  the  input  length  x and  the  output  length  y can  be
different unlike the previous RNN models. The number of hidden
layers in encoder and decoder are not necessarily be the same. The
limitation of this architecture is that it fails to properly summarize a

128 SusmitaDasetal.
long sequence if the context vector is too small. This problem was
solved by Bahdanau et al. (2015) [11] by making the context vector
a variable length sequence with added attention mechanism.
2.7 Attention Models Due to the sequential learning mechanism, the context vector
(Transformers) generated by the encoder (see Subheading 2.6) is more focused
on the later part of the sequence than on the earlier part. An
extension to the encoder–decoder model was proposed by
Bahdanau et al. [11] for machine translation where the model
generates each word based on the most relevant information in
the source sentence and previously generated words. Unlike the
previous encoder–decoder model where the whole input sequence
is encoded into a single context vector, this extended encoder–
decoder model learns to give attention to the relevant words pres-
ent in the source sequence regardless of the position in the
sequence by encoding the input sequence into sequences of vectors
and chooses selectively while decoding each word. This mechanism
of paying attention to the relevant information that are related to
each word is known as attention mechanism.
Although this model solves the problem for fixed-length con-
text vectors, the sequential decoding problem still persists. To
decode the sequence in less time by introducing parallelism, self-
attention was proposed by Google Brain team, Ashish Vaswani et al.
[12]. They invented the Transformer model which is based on self-
attention mechanism and was designed to reduce the computation
time. It computes the representation of a sequence that relates to
different positions of the same sequence. The self-attention mech-
anism was embedded in the Transformer model. The Transformer
model has a stack of six identical layers each for encoding the
sequence and decoding the sequence as illustrated in Fig. 8. Each
layer of the encoder and decoder has sub-layers comprising multi-
head self-attention mechanisms and position-wise fully connected
layers. There is a residual connection around the two sub-layers
followed by normalization. In addition to the two sub-layers, there
is a third layer in the decoder that performs multi-head attention
over the output of the encoder stack. In the decoder, the multi-
head attention is masked to prevent the position from attending the
later part of the sequence. This ensures that the prediction for a
position p depends only on the positions less than p in the sequence.
The attention function can be described as mapping a query and
key-value pairs to an output. All the parameters involved in the
computation are all vectors. To calculate the output, scalar
dot product operation is pperformed on the query and all keys,
and divide each key by d (where d is the dimension on
k k
the keys). Finally, the softmax is applied to it to obtain the
weights on the values. The computation of attention function
can be represented by the following equation:

RNNArchitecturesandResearch 129
Output
Encoder Decoder
Encoder Decoder
Encoder Decoder
Encoder Decoder
Encoder Decoder
Encoder Decoder
Input
Fig. 8 Transformer with six layers of encoders and six layers of decoders
ð Þ
AttentionðQ ,K,VÞ=sof tmax QpK T V, where Q, K, and Vare
dk
all matrices corresponding to query, keys, and values, respectively. A
more in-depth coverage of Transformers is provided in Chap. 6.
3 Tips and Tricks for RNN Training
As previously stated, the vanishing gradient and exploding gradient
problems are well-known concerns when it comes to properly
training RNN models [13, 14]. The fundamental challenge arises
from the fact that RNNs can be naturally unfolded, allowing their
recurrent connections to perform feedforward calculations, which
result in an RNN with the same number of layers as the number of
elements in the sequence. Two major issues arise as a result:

130 SusmitaDasetal.
(cid:129) Gradient vanishing problem. It becomes difficult to effectively
learn long-term dependencies in sequences due to the gradient
vanishing problem [6]. As a result, a prospective model predic-
tion will be essentially unaffected by earlier layers.
(cid:129) Exploding gradient problem. Adding more layers to the network
amplifies the effect of large gradients, increasing the risk of a
learning derailment since significant changes to the network
weights can be performed at each step, potentially causing the
gradients to blow out exponentially. In fact, weights that are
closer to the input layer will obtain larger updates than weights
that are closer to the output layer, and the network may become
unable to learn correlations between temporally distant events.
To overcome these limitations, we need to create solutions so
that the RNN model can work on various time scales, with some
sections operating on fine-grained time scales and handling small
details and others operating on coarse time scales and efficiently
transferring information from the distant past to the present. In this
section, we discuss several popular strategies to tackle these issues.
3.1 Skip Connection The practice of skipping layers effectively simplifies the network by
using fewer direct connected layers in the initial training stages.
This speeds learning by reducing the impact of vanishing gradients,
as there are fewer layers to propagate through. As the network
learns the feature space during the training phase, it gradually
restores the skipped layers. Lin et al. [15] proposed the use of
such skip connections, which follows from the idea of incorporating
delays in feedforward neural networks from Lang et al. [16]. Con-
ceptually, skip connections are a standard module in deep architec-
tures and are commonly referred to as residual networks, as
described by He et al. [17]. They are responsible to skip layers in
the neural network and feeding the output of one layer as the input
to the next layers. This technique is used to allow gradients to flow
through a network directly, without passing through non-linear
activation functions, and it has been empirically proven that these
additional steps are often beneficial for the model convergence
[17]. Skip connections can be used through the non-sequential
layer in two fundamental ways in neural networks:
(cid:129) Additive Skip Connections. In this type of design, the data
from early layers is transported to deeper layers via matrix addi-
tion, causing back-propagation to be done via addition
(Fig. 9b). This procedure does not require any additional para-
meters because the output from the previous layer is added to
the layer ahead. One of the most common techniques used in
this type of architecture is to stack the skip residual blocks
together and use an identity function to preserve the gradient
[18]. The core concept is to use a vector addition to back-

RNNArchitecturesandResearch 131
Fig. 9 Skip connection residual architectures: (a) concatenate output of previous layer and skip connection; (b)
sum of the output of previous layer and skip connection
propagate through the identity function. The gradient is then
simply multiplied by one, and its value is preserved in the earlier
layers.
(cid:129) Concatenative Skip Connections. Another way for establish-
ing skip connections is to concatenate previous feature maps.
The aim of concatenation is to leverage characteristics acquired
in prior layers to deeper layers. In addition, concatenating skip
connections provides an alternate strategy for assuring feature
reusability of the same dimensionality from prior layers without
the need to learn duplicate maps. Figure 9(a) illustrates a dia-
gram example of how the architecture looks like. The primary
concept of the architecture is to allow subsequent layers to reuse
intermediary representations, allowing them to maintain more
information and enhance long-term dependency performance.
3.2 Leaky Units One of the major challenges when training RNNs is capturing
long-term dependencies and efficiently transferring information
from distant past to present. An effective method to obtain coarse
time scales is to employ leaky units [19], which are hidden units
with linear self-connections and a weight on the connections that is
close to one. In a leaky RNN, hidden units are able to access values
from prior states and can be utilized to obtain temporal representa-
tions. Formula h t =α (cid:2)h t-1 +(1-α) (cid:2)h t expresses the state update

132 SusmitaDasetal.
rule of a leaky unit, where α∈(0, 1) is an example of a linear self-
connection from h t-1 to h t , and it is a parameter to be learned
during the training stage. Essentially, α controls the information
flow in the state. When α is near one, the state is almost unchanged,
and information about the past is retained for a long time, and
when α is close to zero, the information about the past is rapidly
discarded, and the state is largely replaced by a new state h.
t
3.3 Clipping Gradient clipping is a technique that tries to overcome the explod-
Gradients ing gradient problem in RNN training, by constraining gradient
norms (element-wise) to a predetermined minimum or maximum
threshold value since the exploding gradients are clipped and the
optimization begins to converge to the minimum point. Gradient
clipping can be used in two fundamental ways:
(cid:129) Clipping-by-value. Using this technique, we define a minimum
clip value and a maximum clip value. If a gradient exceeds the
threshold value, we clip the gradient to the maximum threshold.
If the gradient is less than the lower limit of the threshold, we
clip the gradient to the minimum threshold.
(cid:129) Clipping-by-norm. The idea behind this technique is very
similar to clipping-by-value. The key difference is that we clip
the gradients by multiplying the unit vector of the gradients with
the threshold. Gradient descent will be able to behave properly
even if the loss landscape of the model is irregular since the
weight updates will also be rescaled. This significantly reduces
the likelihood of an overflow or underflow of the model.
4 RNN Applications in Language Modeling
Language modeling is the process of learning meaningful vector
representations for language or text using sequence information
and is generally trained to predict the next token or word given the
input sequence of tokens or words. Bengio et al. [20] proposed a
framework for neural network-based language modeling. RNN
architecture is particularly suited to processing free-flowing natural
language due to its sequential nature. As described by Mikolov et al.
[21], RNNs can learn to compress a whole sequence as opposed to
feedforward neural networks that compress only a single input
item. Language modeling can be an independent task or be part
of a language processing pipeline with downstream prediction or
classification task. In this section, we will discuss applications of
RNN for various language processing tasks.

RNNArchitecturesandResearch 133
4.1 Text Many interesting real-world applications concerning language data
Classification can be modeled as text classification. Examples include sentiment
classification, topic or author identification, and spam detection
with applications ranging from marketing to query-answering
[22, 23]. In general, models for text classification include some
RNN layers to process sequential input text [22, 23]. The embed-
ding of the input learnt by these layers is later processed through
varying classification layers to predict the final class label. Many-to-
one RNN architectures are often employed for text classification.
As a recent technical innovation, RNNs have been combined
with convolutional neural networks (CNNs), thus combining the
strengths of two architectures, to process textual data for classifica-
tion tasks. LSTMs are popular RNN architecture for processing
textual data because of their ability to track patterns over long
sequences, while CNNs have the ability to learn spatial patterns
from data with two or more dimensions. Convolutional LSTM
(C-LSTM) combines these two architectures to form a powerful
architecture that can learn local phrase-level patterns as well as
global sentence-level patterns [24]. While CNN can learn local
and position-invariant features and RNN is good at learning global
patterns, another variation of RNN has been proposed to introduce
position-invariant local feature learning into RNN. This variation is
called disconnected RNN (DRNN) [25]. Information flow
between tokens/words at the hidden layer is limited by a hyper-
parameter called window size, allowing the developer to choose the
width of the context to be considered while processing text. This
architecture has shown better performance than both RNN and
CNN on several text classification tasks [25].
4.2 Text Text summarization approaches can be broadly categorized into
Summarization (1) extractive and (2) abstractive summarization. The first approach
relies on selection or extraction of sentences that will be part of the
summary, while the latter generates new text to build a summary.
RNN architectures have been used for both types of summarization
techniques.
4.2.1 Extractive Text Extractive summarization frameworks use many-to-one RNN as a
Summarization classifier to distinguish sentences that should be part of the sum-
mary. For example, a two-layer RNN architecture is presented in
[26] where one layer processes words in one sentence and the other
layer processes many sentences as a sequence. The model generates
sentence-level labels indicating whether the sentence should be part
of the summary or not, thus producing an extractive summary of
the input document. Xu et al. have presented a more sophisticated
extractive summarization model that not only extracts sentences to
be part of the summary but also proposes possible syntactic com-
pressions for those sentences [27]. Their proposed architecture is a

134 SusmitaDasetal.
combination of CNN and bidirectional LSTM, while a neural
classifier evaluates possible syntactic compressions in the context
of the sentence as well as the broader context of the document.
4.2.2 Abstractive Text Abstractive summarization frameworks expect the RNN to process
Summarization input text and generate a new sequence of text that is the summary
of input text, effectively using many-to-many RNN as a text gener-
ation model. While it is relatively straightforward for extractive
summarizers to achieve basic grammatical correctness as correct
sentences are picked from the document to generate a summary,
it has been a major challenge for abstractive summarizers. Gram-
matical correctness depends on the quality of the text generation
module. Grammatical correctness of abstractive text summarizers
has improved recently due to developments in contextual text
processing, language modeling, as well as availability of computa-
tional power to process large amounts of text.
Handling of rare tokens/words is a major concern for modern
abstractive summarizers. For example, proper nouns such as specific
names of people and places occur less frequently in the text; how-
ever, generated summaries are incomplete and incomprehensible if
such tokens are ignored. Nallapati et al. proposed a novel solution
composed of GRU-RNN layers with attention mechanism by
including switching decoder in their abstractive summarizer archi-
tecture [28] where the text generator module has a switch which
can enable the module to choose between two options: (1) generate
a word from the vocabulary and (2) point to one of the words in the
input text. Their model is capable of handling rare tokens by
pointing to their position in the original text. They also employed
large vocabulary trick which limits the vocabulary of the generator
module to tokens of the source text only and then adds frequent
tokens to the vocabulary set until its size reaches a certain thresh-
old. This trick is useful in limiting the size of the network.
Summaries have latent structural information, i.e., they convey
information following certain linguistic structures such as “What-
Happended” or “Who-Action-What.” Li et al. presented a recur-
rent generative decoder based on variational auto-encoder (VAE)
[29]. VAE is a generative model that takes into account latent
variables, but is not inherently sequential in nature. With the his-
torical dependencies in latent space, it can be transformed into a
sequential model where generative output is taking into account
history of latent variables, hence producing a summary following
latent structures.
4.3 Machine Neural machine translation (NMT) models are trained to process
Translation input sequence of text and generate an output sequence which is
the translation of the input sequence in another language. As
mentioned in Subheading 2.6, machine translation is a classic
example of conversion of one sequence to another using encoder–

RNNArchitecturesandResearch 135
decoder architecture where lengths of both sequences may be
different. In 2014, many-to-many RNN-based encoder–decoder
architecture was proposed where one RNN encodes the input
sequence of text to a fixed-length vector representation, while
another RNN decodes the fixed-length vector to the target trans-
lated sequence [30]. Both RNNs are jointly trained to maximize
the conditional probability of the target sequence given the input
sequence. Later, attention-based modeling was added to vanilla
encoder–decoder architecture for machine translation. Luong
et al. discussed two types of attention mechanism in their work
on NMT: (i) global and (ii) local attention [31]. In global atten-
tion, a global context vector is estimated by learning variable length
alignment and attention scores for all source words. In local atten-
tion, the model predicts a single aligned position for the current
target word and then computes a local context vector from atten-
tion predicted for source words within a small window of the
aligned position. Their experiments show significant improvement
in translation performance over models without attention. Local
attention mechanism has the advantage of being computationally
less expensive than global attention mechanism.
4.4 Image-to-Text Image-to-text translation models are expected to convert visual
Translation data (i.e., images) into textual data (i.e., words). In general, the
image input is passed through some convolutional layers to gener-
ate a dense representation of the visual data. Then, the embedded
representation of the visual data is fed to an RNN to generate a
sequence of text. Many-to-one RNN architectures are popular for
this task.
In 2015, Karpathy et al. [32] presented their influential work
on training region convolutional neural network (RCNN) to gen-
erate representation vectors for image regions and bidirectional
RNN to generate representation vectors for corresponding caption
in semantic alignment with each other. They also proposed novel
multi-modal RNN to generate a caption that is semantically aligned
with the input image. Image regions were selected based on the
ranked output of an object detection CNN.
Xu et al. proposed an attention-based framework to generate
image caption that was inspired by machine translation models
[33]. They used image representations generated by lower convo-
lutional layers from a CNN model rather than the last fully
connected layer and used an LSTM to generate words based on
hidden state, last generated word, and context vector. They defined
the context vector as a dynamic representation of the image gener-
ated by applying an attention mechanism on image representation
vectors from lower convolutional layers of CNN. Attention mech-
anism allowed the model to dynamically select the region to focus
on while generating a word for image caption. An additional
advantage of their approach was intuitive visualization of the

136 SusmitaDasetal.
model’s focus for generation of each word. Their visualization
experiments showed that their model was focused on the right
part of the image while generating each important word.
Such influential works in the field of automatic image caption-
ing were based on image representations generated by CNNs
designed for object detection. Some recently proposed captioning
models have sought to change this trend. Biten et al. proposed a
captioning model for images used to illustrate new articles
[34]. Their caption generation LSTM takes into account both
CNN-generated image features and semantic embeddings to the
text of corresponding new articles to generate a template of a
caption. This template contains spaces for the names of entities
like organizations and places. These places are filled in using atten-
tion mechanism on the text of the corresponding article.
4.5 ChatBot for ChatBots are automatic conversation tools that have gained vast
Mental Health and popularity in e-commerce and as digital personal assistants like
Autism Spectrum Apple’s Siri and Amazon’s Alexa. ChatBots represent an ideal appli-
Disorder cation for RNN models as conversations with ChatBots represent
sequential data. Questions and answers in a conversation should be
based on past iterations of questions and answers in that conversa-
tion as well as patterns of sequences learned from other conversa-
tions in the dataset.
Recently, ChatBots have found application in screening and
intervention for mental health disorders such as autism spectrum
disorder (ASD). Zhong et al. designed a Chinese-language Chat-
Bot using bidirectional LSTM in sequence-to-sequence framework
which showed great potential for conversation-mediated interven-
tion for children with ASD [35]. They used 400,000 selected
sentences from chatting histories involving children in many
cases. Rakib et al. developed similar sequence-to-sequence model
based on Bi-LSTM to design a ChatBot to respond empathetically
to mentally ill patients [36]. A detailed survey of medical ChatBots
is presented in [37]. This survey includes references to ChatBots
built using NLP techniques, knowledge graphs, as well as modern
RNN for a variety of applications including diagnosis, searching
through medical databases, dialog with patients, etc.
5 Conclusion
Due to the sequential nature of their architecture, RNNs are
applied for ordinal or temporal problems, such as language transla-
tion, text summarization, and image captioning, and are
incorporated into popular applications such as Siri, voice search,
and Google Translate. In addition, they are also often used to
analyze longitudinal data in medical applications (i.e., cases where
repeated observations are available at different time points for each

|     |     |     |     |     |     | RNNArchitecturesandResearch |     |     |     |     |     | 137 |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
patient of a dataset). While research in RNN is still an evolving area
and new architectures are being proposed, this chapter summarizes
fundamentals of RNN including different traditional architectures,
training  strategies,  and  influential  work.  It  may  serve  as  a  stepping
stone  for  exploring  sequential  models  using  RNN  and  provides
reference pointers.
References
1. Rumelhart  DE,  Hinton  GE,  Williams  RJ  13. Bengio  Y,  Simard  P,  Frasconi  P  (1994)
(1986)  Learning  representations  by  back- Learning  long-term  dependencies  with  gradi-
propagating  errors.  Nature  323(6088):  ent  descent  is  difficult.  IEEE  Trans  Neural
| 533–536                                         |     |     |     |     |     | Netw         | 5(2):157–166.  |     | https://doi.org/10.110  |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | ----------------------- | --- | --- | --- |
| 2. Hopfield JJ (1982) Neural networks and phys- |     |     |     |     |     | 9/72.279181  |                |     |                         |     |     |     |
ical systems with emergent collective computa- 14. Pascanu  R,  Mikolov  T,  Bengio  Y  (2013)  On
tional  abilities.  Proc  Natl  Acad  Sci  79(8):  the  difficulty  of  training  recurrent  neural
2554–2558  networks.  In:  Dasgupta  S,  McAllester  D  (eds)
|     |     |     |     |     |     | Proceedings  |     | of  the  | 30th  | international  |     | confer- |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ----- | -------------- | --- | ------- |
3. Schmidhuber J (1993) Netzwerkarchitekturen,
ence on machine learning, PMLR, Atlanta, vol
| Zielfunktionen  |     | und  | Kettenregel  | (Network  |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
28, pp 1310–1318
| architectures,  |     | objective  | functions,  | and  | chain  |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | ----------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
rule), Habilitation thesis, Institut fu¨r Informa- 15. Berger  AL,  Pietra  VJD,  Pietra  SAD  (1996)  A
tik, Technische Universitu¨t Mu¨nchen  maximum  entropy  approach  to  natural  lan-
4. Mozer MC (1995) A focused backpropagation  guage  processing.  Comput  Linguist  22(1):
39–71
| algorithm  | for  | temporal.  | Backpropag  |     | Theory  |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Architect Appl 137  16. Becker  S,  Hinton  G  (1992)  Self-organizing
5. Goodfellow  I,  Bengio  Y,  Courville  A  (2016)  neural  network  that  discovers  surfaces  in
Deep learning. MIT Press, Cambridge  random-dot  stereograms.  Nature  355:161–
163. https://doi.org/10.1038/355161a0
| 6. Hochreiter  |     | S  (1998)  | The  vanishing  | gradient  |     |         |            |     |          |         |         |       |
| -------------- | --- | ---------- | --------------- | --------- | --- | ------- | ---------- | --- | -------- | ------- | ------- | ----- |
|                |     |            |                 |           |     | 17. He  | K,  Zhang  | X,  | Ren  S,  | Sun  J  | (2016)  | Deep  |
problem during learning recurrent neural nets
|     |     |     |     |     |     | residual  | learning  |     | for  image  | recognition.  |     | In:  |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ----------- | ------------- | --- | ---- |
and problem solutions. Int J Uncertainty Fuzz-
iness Knowledge Based Syst 6(02):107–116  2016  IEEE  conference  on  computer  vision
|                |     |                  |         |         |        | and       | pattern  | recognition                    |     |     | (CVPR),  | pp  |
| -------------- | --- | ---------------- | ------- | ------- | ------ | --------- | -------- | ------------------------------ | --- | --- | -------- | --- |
| 7. Hochreiter  |     | S,  Schmidhuber  | J       | (1997)  | Long   |           |          |                                |     |     |          |     |
|                |     |                  |         |         |        | 770–778.  |          | https://doi.org/10.1109/CVPR.  |     |     |          |     |
| short-term     |     | memory.          | Neural  | Comput  | 9(8):  |           |          |                                |     |     |          |     |
2016.90
1735–1780
18. Wu H, Zhang J, Zong C (2016) An empirical
| 8. Cho  | K,  Van  | Merrie¨nboer  | B,  | Gulcehre  | C,  |              |     |           |              |     |                  |     |
| ------- | -------- | ------------- | --- | --------- | --- | ------------ | --- | --------- | ------------ | --- | ---------------- | --- |
|         |          |               |     |           |     | exploration  |     | of  skip  | connections  |     | for  sequential  |     |
Bahdanau D, Bougares F, Schwenk H, Bengio
tagging. Preprint. arXiv:161003167
| Y  (2014)  |     | Learning  | phrase  | representations  |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
19. Jaeger H (2002) Tutorial on training recurrent
| using  | RNN  | encoder-decoder  |     | for  statistical  |     |         |            |           |     |        |        |      |
| ------ | ---- | ---------------- | --- | ----------------- | --- | ------- | ---------- | --------- | --- | ------ | ------ | ---- |
|        |      |                  |     |                   |     | neural  | networks,  | covering  |     | BPPT,  | RTRL,  | EKF  |
machine translation. Preprint. arXiv:14061078
|              |     |              |         |                |     | and  | the  | echo  | state  | network  | approach.  |     |
| ------------ | --- | ------------ | ------- | -------------- | --- | ---- | ---- | ----- | ------ | -------- | ---------- | --- |
| 9. Schuster  | M,  | Paliwal  KK  | (1997)  | Bidirectional  |     |      |      |       |        |          |            |     |
GMD-Forschungszentrum
| recurrent                 | neural  | networks.  | IEEE     | Trans       | Signal  |                        |                |           |           |          |            |      |
| ------------------------- | ------- | ---------- | -------- | ----------- | ------- | ---------------------- | -------------- | --------- | --------- | -------- | ---------- | ---- |
| Process 45(11):2673–2681  |         |            |          |             |         | Informationstechnik 5  |                |           |           |          |            |      |
|                           |         |            |          |             |         | 20. Bengio             | Y,             | Ducharme  | R,        | Vincent  | P  (2001)  | A    |
| 10. Pascanu               | R,      | Gulcehre   | C,  Cho  | K,  Bengio  | Y       |                        |                |           |           |          |            |      |
|                           |         |            |          |             |         | neural                 | probabilistic  |           | language  |          | model.     | In:  |
(2013) How to construct deep recurrent neu-
Advances in neural information processing sys-
ral networks. Preprint. arXiv:13126026
tems, pp 932–938
11. Bahdanau D, Cho K, Bengio Y (2014) Neural
|     |     |     |     |     |     | 21. Mikolov  | T,  | Karafia´t  | M,  Burget  |     | L  et  al  | (2010)  |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----------- | --- | ---------- | ------- |
machine translation by jointly learning to align
|     |     |     |     |     |     | Recurrent  |     | neural  | network  | based  | language  |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | -------- | ------ | --------- | --- |
and translate. Preprint. arXiv:14090473
model. In: INTERSPEECH 2010. Citeseer
12. Vaswani A, Shazeer N, Parmar N, Uszkoreit J,
22. Jain G, Sharma M, Agarwal B (2019) Optimiz-
| Jones  | L,  Gomez  | AN,  | Kaiser  Ł,  | Polosukhin  | I   |      |           |       |            |             |     |         |
| ------ | ---------- | ---- | ----------- | ----------- | --- | ---- | --------- | ----- | ---------- | ----------- | --- | ------- |
|        |            |      |             |             |     | ing  | semantic  | lstm  | for  spam  | detection.  |     | Int  J  |
(2017) Attention is all you need. In: Advances
Inform Technol 11(2):239–250
| in  neural  | information  |     | processing  | systems,  | pp  |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
5998–6008

138 SusmitaDasetal.
23. Bagnall  D  (2015)  Author  identification  using  31. Luong  MT,  Pham  H,  Manning  CD  (2015)
multi-headed  recurrent  neural  networks.  Pre- Effective approaches to attention-based neural
| print. arXiv:150604891  |     |     |     |     |     | machine |     | translation. |     | Preprint.  |     |
| ----------------------- | --- | --- | --- | --- | --- | ------- | --- | ------------ | --- | ---------- | --- |
arXiv:150804025
| 24. Zhou  | C,  Sun  | C,  | Liu  Z,  | Lau  F  (2015)  | A   |     |     |     |     |     |     |
| --------- | -------- | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
C-LSTM neural network for text classification.  32. Karpathy  A,  Fei-Fei  L  (2015)  Deep  visual-
Preprint. arXiv:151108630  semantic  alignments  for  generating  image
25. Wang B (2018) Disconnected recurrent neural  descriptions. In: Proceedings of the IEEE con-
networks  for  text  categorization.  In:  Proceed- ference on computer vision and pattern recog-
nition, pp 3128–3137
ings of the 56th annual meeting of the associa-
tion  for  computational  linguistics  (volume  1:  33. Xu  K,  Ba  J,  Kiros  R,  Cho  K,  Courville  A,
long papers), pp 2311–2320  Salakhudinov  R,  Zemel  R,  Bengio  Y  (2015)
26. Nallapati R, Zhai F, Zhou B (2017) Summar- Show,  attend  and  tell:  neural  image  caption
unner:  a  recurrent  neural  network  based  generation  with  visual  attention.  In:  Interna-
sequence  model  for  extractive  summarization  tional conference on machine learning, PMLR,
| of documents. In: Thirty-first AAAI conference  |     |     |     |     |     | pp 2048–2057  |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
on artificial intelligence  34. Biten  AF,  Gomez  L,  Rusinol  M,  Karatzas  D
|     |     |     |     |     |     | (2019)  Good  | news,  | everyone!  |     | context  | driven  |
| --- | --- | --- | --- | --- | --- | ------------- | ------ | ---------- | --- | -------- | ------- |
27. Xu J, Durrett G (2019) Neural extractive text
|                |     |       |            |               |     | entity-aware  | captioning  |               | for  news  | images.        | In:  |
| -------------- | --- | ----- | ---------- | ------------- | --- | ------------- | ----------- | ------------- | ---------- | -------------- | ---- |
| summarization  |     | with  | syntactic  | compression.  |     |               |             |               |            |                |      |
|                |     |       |            |               |     | Proceedings   | of          | the IEEE/CVF  |            | conference on  |      |
Preprint. arXiv:190200863
|                |     |           |              |               |     | computer  | vision  | and  pattern  | recognition,  |     | pp  |
| -------------- | --- | --------- | ------------ | ------------- | --- | --------- | ------- | ------------- | ------------- | --- | --- |
| 28. Nallapati  | R,  | Zhou  B,  | dos  Santos  | C,  Gulcehre  |     |           |         |               |               |     |     |
12466–12475
C¸ , Xiang B (2016) Abstractive text summariza-
tion  using  sequence-to-sequence  rnns  and  35. Zhong  H,  Li  X,  Zhang  B,  Zhang  J  (2020)  A
beyond. In: Proceedings of the 20th SIGNLL  general chinese chatbot based on deep learning
conference on computational natural language  and its’ application for children with ASD. Int J
10:519–526.
| learning, pp 280–290  |     |     |     |     |     | Mach  Learn  | Comput  |     |     |     | https://  |
| --------------------- | --- | --- | --- | --- | --- | ------------ | ------- | --- | --- | --- | --------- |
doi.org/10.18178/ijmlc.2020.10.4.967
| 29. Li  P,  | Lam  W,  | Bing  | L,  Wang  | Z  (2017)  | Deep  |     |     |     |     |     |     |
| ----------- | -------- | ----- | --------- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
recurrent  generative  decoder  for  abstractive  36. Rakib  AB, Rumky  EA, Ashraf  AJ,  Hillas MM,
text  summarization.  In:  Proceedings  of  the  Rahman MA (2021) Mental healthcare chatbot
2017 conference on empirical methods in nat- using  sequence-to-sequence  learning  and
ural language processing, pp 2091–2100  bilstm. In: Brain informatics, springer interna-
tional publishing, pp 378–387
| 30. Cho  | K,  van  | Merrienboer  |     | B,  Gu¨lc¸ehre  | C¸,  |                       |     |       |       |     |          |
| -------- | -------- | ------------ | --- | --------------- | ---- | --------------------- | --- | ----- | ----- | --- | -------- |
|          |          |              |     |                 |      | 37. Tjiptomongsoguno  |     | ARW,  | Chen  | A,  | Sanyoto  |
Bahdanau D, Bougares F, Schwenk H, Bengio
HM, Irwansyah E, Kanigoro B (2020) Medical
| Y  (2014)  |               | Learning         | phrase    | representations   |     |              |               |     |              |               |       |
| ---------- | ------------- | ---------------- | --------- | ----------------- | --- | ------------ | ------------- | --- | ------------ | ------------- | ----- |
|            |               |                  |           |                   |     | chatbot      | techniques:   | a   | review.      | In:  Silhavy  | R,    |
| using      | RNN           | encoder-decoder  |           | for  statistical  |     |              |               |     |              |               |       |
|            |               |                  |           |                   |     | Silhavy  P,  | Prokopova     | Z   | (eds)        | Software      | engi- |
| machine    | translation.  |                  | In:  The  | 2014  conference  |     |              |               |     |              |               |       |
|            |               |                  |           |                   |     | neering      | perspectives  | in  | intelligent  | systems.      |       |
on empirical methods in natural language pro-
|     |     |     |     |     |     | Springer  | International  | Publishing,  |     | Cham,  | pp  |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | ------------ | --- | ------ | --- |
cessing (EMNLP)
346–356
OpenAccess ThischapterislicensedunderthetermsoftheCreativeCommonsAttribution4.0International
License(http://creativecommons.org/licenses/by/4.0/),whichpermitsuse,sharing,adaptation,distribution
andreproductioninanymediumorformat,aslongasyougiveappropriatecredittotheoriginalauthor(s)andthe
source,providealinktotheCreativeCommonslicenseandindicateifchangesweremade.
Theimagesorotherthirdpartymaterialinthischapterareincludedinthechapter’sCreativeCommonslicense,
unless indicated otherwise in acredit line tothe material. Ifmaterialis notincludedin the chapter’s Creative
Commonslicenseandyourintendeduseisnotpermittedbystatutoryregulationorexceedsthepermitteduse,
youwillneedtoobtainpermissiondirectlyfromthecopyrightholder.