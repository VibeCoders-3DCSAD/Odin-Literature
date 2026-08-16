---
conversion_metadata:
  converted_at: "2026-07-22T11:54:50Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Alenazi & Sas.pdf"
  source_pdf_sha256: "2bc492ff8ea110793eb3737c314cdbfcc93fde0933c3f613f02771cd99962697"
  page_count: 12
  markdown_char_count: 130944
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

http://dx.doi.org/10.14236/ewic/BCSHCI2023.1

Evaluating Budgeting Apps: Limited Support 
for Budgeting Compared to Tracking

Mariam Alenazi 
Lancaster University 
Lancaster, UK 
m.alenazi@lancaster.ac.uk

Corina Sas 
Lancaster University 
Lancaster, UK

c.sas@lancaster.ac.uk

Financial  behaviour  is  deeply  embedded  in  our  lives,  yet  for  many  people  its  success  remains 
problematic.  The  need  for  supporting  tools  in  this  space  is  reflected  in  the  growing  number  and 
popularity of  budgeting apps, albeit limited research has focused on evaluating them. This paper 
describes a functionality review from the lens of mental accounting theory of 45 top-rated budgeting 
apps selected from 1335 apps on Google Play Store and Apple Store. Findings indicate that while all 
apps support tracking of transactions, one third of the apps do not support budgeting informed by 
money envelopes. We also report challenges regarding the meaning of key concepts of “accounts” 
and  “transactions”  for  which  we  proposed  novel  design  implications  including  a  more  nuanced 
vocabulary to talk about accounts and transaction types, new knowledge to have better support for 
budgeting  through  mental  accounting  theory  and  grounding  budgeting  as  cognitive  process  in 
actual financial behaviour.

Financial behaviours. Budgeting apps. Money envelopes

1.

INTRODUCTION

HCI research on money and financial practices  has 
focused mostly on exploratory studies (Kaye et al., 
2014;  Vines,  Dunphy  and  Monk,  2014;  Snow  and 
Vyas,  2015b;  Vyas  et  al.,  2016;  Lewis  and  Perry, 
2019),  whose  findings  indicate  that  people  tend  to 
use digital tools to a limited extent. As a result, we 
have little understanding of how digital tools such as 
mobile  apps  for  personal  budgeting  could  facilitate 
the tracking and monitoring of financial behaviours 
such  as 
for  daily 
tracking  and  budgeting 
expenditures. In addition to mobile banking, financial 
management  apps  supporting  users 
track 
expenses  and  create  budgets,  have  also 
experienced rapid growth in the recent years as one 
of  the  fastest  growing  categories  of  finance  apps 
(Bitrián, Buil and Catalán, 2021). In 2018, the global 
revenue for the such tools was over $1.4 million and 
estimated  to  at  least  double  its  value  by  2025 
(QYResearch,  no  date).    While  previous  HCI 
research  has  explored  functionalities  of  publicly 
available apps on marketplaces in domains such as 
fitness  (Chung  et  al.,  2018),  diet  (Zaidan  and 
Roehrer,  2016),  depression  (Qu  et  al.,  2020), 
personal  goals  (Lolla  and  Sas,  2023)  or  digital 
wellbeing  (Almoallim  and  Sas,  2022),  limited  such 
work has looked at budgeting apps.

to

To address this  gap,  we  explore the functionalities 
of top-rated budgeting apps by employing a mental 
accounting lens. Mental accounting is a behavioural

© Alenazi et al. Published by BCS 
Learning and Development Ltd. 
Proceedings of BCS HCI 2023, UK

1

economics theory (Thaler, 1999) according to which 
people  commonly  partition  and  budget  money 
separately  in  mental  accounts  usually  materialized 
through money envelopes for specific purposes. As 
the economist Thaler (Thaler, 1999) stated the main 
purpose  of  mental  accounting  is  to  use  labelled 
categories for sources such as regular income and 
uses of funds such as food, to help individuals and 
households  organize, 
their 
spending.  Our  findings  indicate  insufficient  support 
for budgeting functionality and important challenges 
of such apps due to the overlapping meanings and 
insufficient clarity of the key  concepts. We discuss 
new  design 
them 
including a more nuanced vocabulary to talk about 
accounts, 
transactions  and  budgeting,  better 
support for budgeting in addition to tracking and in 
particular for multiple rather than single budgets.

track  and  monitor

for  addressing

implications

2.  BACKGROUND

Most HCI work on financial behaviour has focused 
on  tracking  such  practices  for  individuals  (Kaye  et 
al., 2014; Vines, Dunphy and Monk, 2014; Lewis and 
Perry,  2019)  and  households  (Snow  and  Vyas, 
2015b,  2015a;  Vyas  et  al.,  2015,  2016)  and  their 
preferred  tools.  To  track  their  spending,  most  of 
previous findings emphasize analogue tools such as 
coin jars (Snow and Vyas, 2015a; Vyas et al., 2016), 
enabling people to see how much they have spent.

---

<!-- PAGE 2 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

In addition to coin jars, envelops  (Snow and Vyas, 
2015a; Vyas et al., 2015) are also commonly used 
budgeting  tools  for  monitoring  expenses  as  their  
names  reflect  the  purpose  of  money  stored  in 
specific  envelopes,  such  as  grocery  money.  There 
have  been  other  common  analogue  tools  for 
budgeting  and  tracking  spending,  such  as  wall 
organizers,  bills  attached  to  refrigerators,  folders 
and  handwritten  diaries  (Kaye  et  al.,  2014;  Snow 
and Vyas, 2015b, 2015a; Vyas et al., 2015, 2016), 
which are preferred due to their simplicity.

for

tool

tracking 
third  of

In contrast to such rich use of analogue tools, HCI 
research has reported limited digital tools supporting 
financial  practices  and  in  particular  of  budgeting 
apps. For instance, Snow and Vyas’s study  (Snow 
and  Vyas,  2015a)  showed  banking  apps  as  more 
financial 
common  digital 
the  15 
transactions,  with  only  one 
participants having used budgeting apps which they 
tend to discontinue after a short period of time due 
to the perceived challenge of entering expense and 
of  lack  of  adequate  control  over  their  spending. 
Spreadsheets  were  another  common  tools  mostly 
for tracking transactions (Kaye et al., 2014; Vyas et 
al., 2016), rather than budgeting purposes. Despite 
the  growing  HCI  interest  in  personal  finances,  we 
have  seen  limited  theoretical  underpinning  of  such 
work, especially from the lens of mental accounting 
theory, although the value of behavioural economics 
has  been  previously  suggested  (Stockinger  et  al., 
2013) for healthy choices (Lee, Kiesler and Forlizzi, 
2011), digital wellbeing (Park, Lee and Park, 2021) 
or retirement savings (Gunaratne and Nov, 2015).

To summarize, HCI research on financial practices 
has highlighted mostly the use of analogue tools and 
limited  use  of  digital  ones,  especially  budgeting 
apps. Most of such work has also limitedly engaged 
the mental accounting theory (Thaler, 1999) despite 
initial acknowledgments of the value of behavioural 
economics in HCI.

3.  METHOD

To identify the budgeting apps, we searched the two 
marketplaces  in  the  UK:  Google  Play  Store  (for 
Android)  and  Apple  Store  (for  iOS)  using  three 
keywords: budget, budgeting and finance. From the 
total of 1335 apps as shown in Figure 1, we removed 
duplicates, apps that were not free, apps not related 
to budgeting, those requiring access to one’s bank 
accounts  and  retained  top-rated  apps  with  an 
average rating score of four out of five and with at 
least  1000  reviews.  This  led  to  45  apps  being 
included  in  the  analysis  (Table  1,  col  1):    21  apps 
available  only  on  Google  Play  Store  and  24  apps 
available  on  both  platforms.  The  functionalities  of 
these  45  apps  were  iteratively  reviewed  to  identify 
functionalities, firstly through analysing all the apps’

2

descriptions,  followed  by  expert  evaluation.  The 
analysis  of  apps’  descriptions, 
the 
identification of main functionalities such as tracking 
transactions  and  monitoring  budgets.  The  limited 
information  available  in  the  apps’  descriptions  was 
rather restricted to these broad functionalities.

led

to

the  expert  evaluation  we

For 
leveraged  key 
concepts  from  mental  accounting  theory  (Thaler, 
1999) to identify functionalities pertaining to funds, 
i.e. sources and uses; expenditures and categories 
for  grouping 
them  and  mental  accounts  or 
envelopes for allocating budgets to such categories. 
Additional  functionalities  identified  in  the  reviewed 
apps  include  create  transaction  accounts,  link  the 
app to real bank account, as well as set date, time 
and  currency  for  transactions.  The  identification  of 
these functionalities involved iterations that the two 
authors discussed over several months.

While most  functionalities  were  easily  identified  by 
each of them from apps' descriptions, functionalities 
reflecting 
required 
transactions  and  accounts 
through  weekly 
additional  clarification  reached 
conversations:  transactions  are  to  be  considered 
broadly  as  encompassing  income,  expense  and 
transfer  of  money  between  accounts.  Other 
clarification  concerned  transaction  accounts  as 
containers  holding  each  of  the  three  types  of 
transactions.  Additional  functionalities  have  been 
also identified through this iterative process, namely 
linking  a  transaction  to  a  transaction  account  and 
differentiating  existing  categories  for  both  income 
and  expense  categories.  Appendix  A  shows  the 
complete set of functionalities.

the  apps’  descriptions  was 
While  analysis  of 
completed  by  the  first  author,  who  also  completed 
the  expert  evaluation  of  all  45  apps  using  Galaxy 
S21+.  Second  author  also  performed  expert 
evaluation of five apps on an iPhone 12, in order to 
discuss  and  reconcile  the  identified  functionalities. 
As the second author used iOS platform, these five 
apps  were  randomly  selected  from  the  24  apps 
available on Apple Store.

4.  RESULTS

terminology

inconsistent

The  45  identified  apps  belong  mostly  to  Finance 
category on marketplaces (44 apps) and one app to 
Business category. Findings indicate different types 
of  accounts  and 
for 
labelling  them.  Outcomes  also  indicate  two  main 
that  provide 
types  of  budgeting  apps, 
functionality of tracking expenses without monitoring 
(8 apps) and those that provide also, in addition to 
tracking  expenses,  the  budgeting  functionality  for 
monitoring expenses against their allocated budget 
(33 apps). The latter use either single budget for all 
expenses irrespectively of their different categories

those

---

<!-- PAGE 3 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

1335 apps identified from

Google Play (n= 742)

Apple Store (n= 593)

404 apps excluded:

Duplicated apps= 326 (Google Play: n=191, Apple 
Store: n=128, both: n= 7)

Not  free  apps=  78  (Google  Play:  n=18,  Apple 
Store: n= 60)

810 apps excluded:

Apps  with  less  than  1000  reviews  and  lower 
than 4.0 in rating score (Google Play: n=439, 
Apple Store: n= 371)

71 apps excluded:

Apps not related to budgeting (Google 
Play: n=44, Apple Store: n= 27)

931 Remaining

Google Play (n=533),

Apple Store (n=398)

121 Remaining

(Google Play: n= 94, Apple 
Store: n= 27)

50 Remaining

(Google Play only)

Eligible apps for analysis Google 
Play: n= 45

5 apps excluded:

Apps  required  access  to  one's  bank 
account.

n
o
i
t
a
c
i
f
i
t
n
e
d
I

i

g
n
n
e
e
r
c
S

d
e
d
u
c
n
I

l

Figure 1. PRISMA diagram describing the process of apps’ selection.

(seven  apps-  Table  2,  col  10)  or  multiple  budgets 
using a different budget for each expense category 
such as bills, rent, groceries (26 apps- Table 2, col 
11,  albeit  4  of  these  provide  budgeting  only  as 
premium, subscription-based functionality). Most of 
the apps show limited theoretical underpinning, with 
only two apps Goodbudget (Partners, no date) and 
SimpleBudget (Tanu, 2011) explicitly mentioning in 
their  description  that  their  design  was  informed  by 
money  envelope  systems, albeit  specific  reference 
to  mental  accounting  theory  (Thaler,  1999)  is  not 
made.  Also,  no  app’s  description  reports 
its 
evaluation though users' studies.

4.1  Accounts: Types and Terminology

A  significant  finding  is  the  concept  of  accounts 
partially employed by our explored apps in order to 
support  the  organization  of  transactions.  Mental 
accounting  theory  (Thaler,  1999)  identifies  three 
types of accounts, namely those for depositing and

storing available funds such as monthly income (i.e. 
money-in), those for depositing and storing assets or 
wealth such as saving accounts and those for using 
or  spending  the  available  funds  (i.e.  money-out)  . 
With  regard  to  the  latter,  the  theory  also  specifies 
that  people  create  mental  accounts  for  allocating 
money  for  specific  purposes  or  in  other  words  for 
budgeting  for  specific  categories  of  expenses, 
similar to money envelopes which will be discussed 
later. With regard to these three types of accounts 
proposed  by  mental  accounting  theory,  findings 
indicate  that  most  of  the  apps  support  depositing 
funds (44 apps) and paying for expenses (45 apps), 
with fewer apps support saving (11 apps- Table 2, 
col 3).

However, while most of the apps (41 apps- Table 2, 
col  2)  have  accounts  for  depositing  funds  or  for 
paying  for  expenses  ,  the  remaining  four  apps 
(DAILY  POCKET  (Yjteam,  2017),  EasyBudget 
(Letondor,  2015),  Expense  Tracker 
-  Money 
Manager & Budget (Labs, 2019) and Budget App -

3

---

<!-- PAGE 4 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

Expense  Tracker  (HG  Group  Inc.,  2020))  merely 
support the depositing of money on the app’s home 
screen  rather  than  in  dedicated  income  account. 
This  is  problematic  as  these  four  apps  also  fail  to 
provide  the  option  of linking individual transactions 
to  specific  accounts,  as  they  are  all  stored  directly 
on  the  home  screen.  Even  for  the  remaining  apps 
providing  the  option  of  creating  income,  saving  or 
expense  accounts, 
income  and  expense, 
although  conceptually  distinct,  they  support  the 
depositing and spending of the funds from the same 
container, respectively.  In other words, for most of 
the  apps,  the  income  and  expense  accounts, 
although conceptually distinct, in practice they tend 
to be  one and the same account similar  to a bank 
account or a wallet where money are both deposited 
in and spent from.

the

for

Findings also indicate various terms for referring to 
such accounts, inconsistently used across the apps. 
The employed terminology appears to draw from two 
different  sources:  banking  domain  and  everyday 
financial  practices.  A  significant  outcome  is  that 
most  of  the  apps  employed  terms  from  banking 
domain  for  naming  or  labelling  accounts.  Such 
terms,  used 
income,  saving  or  expense 
accounts, include: virtual bank accounts (nine apps), 
virtual cash accounts (17 apps), saving accounts (11 
apps),  investment  accounts  (seven  apps),  virtual 
credit card  account (17  apps), virtual debt  account 
(13  apps),  with  many  apps  (18  apps)  employing 
more than one of these terms for organizing funds, 
wealth  and  expenses.  While  such  terminology  for 
banking domain can be useful as it builds on users’ 
familiarity  with  banking  practices, 
the  direct 
association  with  banking  practices  is  limited  since 
only  seven  apps  support  the  integration  of  the 
budgeting apps with users’ online banking services 
and only as premium feature (Table 2, col 9). This 
terminology  from  banking  domain  also  fails  to 
provide specific types of expense accounts such as 
those  for  different  categories  of  expenses  or  the 
equivalent of money envelopes (Thaler, 1999), since 
banking  accounts  capturing  spending 
relate 
exclusively to debt repayment such as credit or debit 
card  or  mortgage,  but  not  for  instance  to  monthly 
grocery, bills or rent budgets.

Other  terms  to  label  accounts  are  borrowed  from 
everyday  financial  practices  and  include  wallet 
(three  apps:  Expense  Tracker  &  Budget  App 
(Estimate, 2019), Easy Home Finance (VoPo, 2015) 
and Spendee Budget & Money Tracker (A.s., 2013)), 
financial account (one app: Family budget-spending 
tracker  (DigitLeaf,  2017)),  payment  account  (one 
app – Money pro (LLC, 2017)) or even budget (two 
apps:  Fudget:  Budget  and  expense  tracking  app 
(Connell, 2017) and Home Budget - Money Manager 
(Softs, no date)). Interestingly, with respect to terms 
from everyday practices, findings indicate that clear 
ones  for  distinguishing  among  available  funds, 
wealth and expense accounts or between money-in

4

and money-out are not employed by any of the apps 
except  one  app:  GnuCash  which  uses  multiple 
accounts such as income, expenses and assets.

4.2  Creating and Tracking Transactions:

Income, Expenses, Transfer

Study findings also highlight the important distinction 
between  accounts  and  transactions.  We  suggest 
that  accounts  are  similar  to  containers  for  the 
organization of transactions, while each transaction 
represents the movement of money from a source to 
a  destination,  in  other  words,  transactions  are  the 
ones  that  allow  accounts  to  be  replenished  with 
funds or depleted  of funds. Findings indicate three 
types  of  transactions  for  (i)  depositing  funds,  (ii) 
paying for expenses or (iii) transferring money from 
income  to  expense  accounts  which  are  further 
from  one  app 
detailed.  All  apps  apart 
(SimpleBudget:  Envelope  Budget)  allow  users  to 
deposit  funds,  through  income  transactions  (44 
apps- Table 1, col 2) by specifying the name or label 
of the transactions, usually referring to the source of 
money  such  as  salary,  together  with  the  specific 
amount of money being deposited, the date (all but 
two apps- Table 1, col 5) and time (18 apps- Table 
1, col 6) of the income transaction and its currency 
(40 apps – Table 1, col 4).

From the 40 apps supporting the specification of the 
currency of deposited funds, 12 apps provide a pre-
defined  list  of  currencies  allowing  users  to  choose 
different  one  for  each  income  transaction  being 
created, while 28 apps provide a pre-defined list of 
currencies  albeit  in  the  app  settings  so  each 
transaction  with  a  different  currency  requires 
changing  it  in  the  app  setting.  These  two  options 
prioritize either the ease of changing currency or of 
keeping  it  constant  across  transactions.  Unlike  the 
rest of the apps, SimpleBudget app does not support 
the  creation  of  an  income  account;  instead,  it 
supports  users  to  create  multiple  envelopes,  each 
with  its  own  budget  or  available  fund,  without 
specifying the total amount of available funds to be 
allocated  across  all  the  envelopes.  This  can  be 
problematic in terms of the cognitive load needed to 
ensure that the available funds not captured by the 
app,  do  not  exceed  the  cumulative  value  of  the 
money envelopes.

With  respect  to  expense  transactions,  all  apps 
support  users  to  create  them  (Table  1,  col  7),  by 
specifying the names or labels of these transactions, 
usually  the  destination  of  money  such  as  grocery 
expense,  together  with  the  specific  amount  of 
money  being  paid  (45  apps),  the  date  (45  apps- 
Table 1, col 10) and time (18 apps- Table 1, col 11) 
of the expense transaction and its currency (41 apps 
–  Table  1,  col  9)  with  similar  ease  of  changing 
currency  or  of  keeping  constant  characterizing 
income transactions.

---

<!-- PAGE 5 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

Finding  show 
the 
specification  of  the  payment  method  for  expense 
transactions, i.e., cash, credit/debit card or cheque.

four  apps  also  allow

that

to

respect

the  mode  of  entering

With 
the 
transactions, most apps support the creation of both 
income and expense transactions through the same 
interaction  by  tapping  on  the  plus  icon  on  app’s 
home screen (35 apps), by clicking on income button 
or expense button on the app’s home screen (eight 
apps)  or  by  tapping  on  “register”  button  on  app’s 
home  screen  which  opens  another  page  to  create 
the  income  or  expense  (one  app  –  MoneyWise 
(North,  2011).  One  remaining  app  (CoinKeeper: 
expense, money manager, budget planner) provides 
different  interactions  for  entering  income,  i.e.,  by 
tapping on the plus icon on app’s home screen and 
for entering expense, i.e., by dragging a transaction 
account icon into expense category then specify the 
expense  amount 
the  dragged  account. 
Arguably,  the  simple  interaction  for  tapping  on  the 
plus icon on app’s home screen to enter both income 
and  expense  transaction  is  preferrable  in  terms  of 
increased usability.

from

In  addition  to  income  and  expense  transactions, 
findings also indicate the third type, namely transfer 
transactions  (35  apps-  Table  2,  col  5),  which  we 
define as transfer of money from a source (available 
income) to a destination (for expense or saving). In 
addition 
to  specifying  source  and  destination 
accounts (35 apps), transfer transactions could also 
specify the amount of money being transferred (35 
apps), transfer date (30 apps- Table 2, col 6), time 
(11 apps- Table 2, col 7), currency (25 apps) as well 
as  label  or  receipt  which  can  be  attached  to  the 
transfer (five apps and three apps premium- Table 
2, col 8).  Interestingly, most of the apps supporting 
transfer  transactions  allow  them  without  sufficient 
funds in the source account (33 apps out of 35). Two 
exceptions  include  the  Family  budget-spending 
tracker app, where if the transferred amount is larger 
than the available funds, the message of “insufficient 
amount”  is  shown  in  red  colour  and  the  transfer 
cannot  be  completed.  For 
the  other  app 
(MoneyWise), the transfer transaction is a premium 
feature.

An important finding is that similar transactions can 
also be grouped in categories, for both income and 
expenses transactions. This functionality aligns with 
the cognitive operations of grouping different income 
and expenditures into categories mentioned by the 
mental  accounting  theory  (Thaler,  1999).  These 
categories  could  be  of  two  types:  provided  by  the 
app or defined by the user. The former consists of a 
list of categories for income such as salary, bonus, 
gift, refund, business and interest (38/45 apps) and 
for  expense 
(40/45  apps)  such  as  grocery, 
shopping,  transportation,  bills,  education  and  rent. 
The user defined categories allow users to specify 
new  ones  if  those  provided  by  the  app  are  not

5

re-used

adequate, both for income (36/45 apps and two apps 
premium) and for expense transactions (42/45 apps 
and  one  app  premium)  and  once  crated,  these 
categories  could  be 
later  with  new 
transactions.  However,  some  apps  provide  the 
limited option of one-off categories for income (four 
apps) and expense (two apps). Therefore, with each 
new transaction, the user needs to enter the source 
of income and the expense name. While most apps 
provided one level of categories, 15 apps provided 
option 
transactions.  For 
example,  car  expense  category  can  have  sub-
categories such as fines, fuel, parking and repairs.

for  subcategories  of

Finally, all transactions can be entered manually (45 
apps), they can also be automatically imported from 
online banking accounts linked to the budgeting app 
(seven  apps),  with  few  apps  encouraging  users  to 
compare  their  entered  transactions  with  those  of 
their bank statements (seven apps).

4.3  Budgeting: Tracking Balance vs Money

Envelopes

Findings  indicate  that  all  apps  support  budgeting 
functionality  and 
the  monitoring  of 
therefore 
expenses against the allocated budgets (45 apps), 
although they do so in different ways. While most of 
these  apps  support  budgeting  under  mental 
accounts or money envelopes (26 apps), others do 
not (19 apps). We called the latter form of budgeting 
as single budget and the former as multiple budgets, 
as further detailed.

Apps supporting single budget (19 apps) rely on only 
one main budget (usually the same amount as the 
available funds) from which all expenses are to be 
covered.  In  these  apps,  expense  transactions  are  
not  grouped  under  specific  money  envelops  with 
allocated  budgets  for  each  envelope,  which  would 
be consistent with mental accounting theory (Thaler, 
1999).  Although  these  apps  have  a  single  budget, 
they do support a high-level monitoring of expenses 
and  do  so  in  two  ways.  While  all  19  apps  use  the 
account  balance  to  represent  the  overspent  of 
available funds using the minus symbol, eight apps 
do not change the colour  of this information, albeit 
seven  apps  use  colour  red 
this 
information of overspent.

to  provide

Although  single  budget  apps  depend  on  the  total 
funds, some of these apps allow to set that fund as 
explicit budget for all expense (five out of 19 apps). 
These five apps do not have a specific budget name 
by the user, it was named by the app as budget and 
the  user  can  set  the  budget  amount  and  budget 
period (Table 2, col 13) as daily (one app - Spending 
Tracker),  weekly  (two  apps  -  DAILY  POCKET  - 
Budget  Manager  and  Spending  Tracker),  monthly 
(four apps), yearly (one app - Spending Tracker) or 
defined by the user (one app - Monny).

---

<!-- PAGE 6 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

the

Four of these 19 apps support also multiple budgets 
but  only  as  a  premium  functionality.  In  contrast  to 
single  budgets,  26  apps  support  the  creation  of 
multiple  budgets  which  aligns  with  mental 
accounting  theory  (Thaler,  1999).  These  apps 
functionality  of  creating  money 
support 
envelopes  by  allowing  users  to  allocate  different 
budgets to distinct expense categories, for instance 
for  groceries,  transport  or  bills.  Furthermore,  15  of 
the  26  apps  provide  the  option  to  personalize  the 
name  of  the  budget,  i.e.,  budget  for  bills  category 
can  be  called  for  instance  household  bill  budget, 
while  the  remaining  11  apps  use  the  name  of  the 
expense  category  as  the  name  the  budget,  i.e., 
budget for bills category is bills budget.

(seven  apps),  monthly

In addition, the budget period could be also set for 
all these 26 apps from predefined  periods such as 
daily  (provided  by  seven  apps),  weekly  (15  apps), 
fortnight 
(26  apps), 
biannually (three apps) and annually (14 apps), with 
17  apps  providing  multiple  predefined  budgeting 
periods. The budgeting periods can also be defined 
by  users  with  six  apps  providing  the  option  of 
entering a specific date.

5.  DISCUSSION AND DESIGN IMPLICATIONS

in

We reviewed the functionalities of  the 45 top-rated 
budgeting  apps  to  explore  if  and  how  these 
functionalities  are  grounded 
the  mental 
accounting  theory  (Thaler,  1999).  Our  findings 
indicate  limited  clarity  regarding  the  two  important 
terms  of  accounts  and  transactions  and  limited 
support for budgeting functionality. We suggest four 
design  implications  including  the  recommendation 
for developers to use clearer terminology  to define 
and differentiate accounts and transactions and their 
specific  types,  for  better  supporting  budgeting 
through  money  envelopes,  and 
for  grounding 
budgeting  as  mental  activity  in  the  actual  financial 
practices.

suggest  the  use  of  consistent  terminology  for 
accounts that clearly defines accounts as containers 
of transactions distinguishing accounts for available 
funds, wealth and expenses (Thaler, 1999).

5.2  Defining Transactions and their Types:

Income, Expenses, Transfer

Related  to  the  three  types  of  accounts,  findings 
indicate  transactions  reflecting  the  flow  of  money 
and their three types for depositing funds, paying for 
expenses  or  transferring  money  from  income  to 
expense  accounts,  which  however  are  not 
supported  by  all  apps.  We  suggest  defining 
transactions and providing options to create each of 
them, with the following details of transaction name, 
category,  amount,  currency,  date,  time,  supported 
by  most  but  not  all  apps.  Based  on  the  mental 
accounting  theory  (Thaler,  1999),  the  funds  and 
expenses should be labelled as such and grouped 
into  categories  according 
financial 
practices. Study findings show limited functionalities 
supporting  the  allocation  of  income  and  expenses 
into  specific  categories.  This  is  problematic  as 
spending  money  from  a  general  pot  rather  than 
specific  pots  for  different  expense  categories,  can 
more  easily  lead  to  over  expenditure.  To  address 
income  and  expense 
this 
transactions should be grouped into categories and 
subcategories,  such  as 
income  and  salary, 
respectively. These could be both predefined by the 
system or defined by the user.

limitation,  both

to  people

it:

for  each

For currency, findings indicate two exclusive ways of 
selecting 
transaction  or  across 
transactions  through  app  settings.  We  suggest  a 
flexible approach allowing users to choose between 
these  two  modes  of  selecting  the  currency.  For 
entering  transactions,  the  simplest  interaction  that 
we  suggest  is  tapping  on  the  plus  icon  on  app’s 
home screen, while for transfer transactions, those 
with 
funds  should  be 
consistently prevented.

insufficient  available

5.1  Defining Accounts and their Types:

Available Fund, Wealth, Expenses

5.3  Supporting Budgeting through Money

Envelopes

Findings show that not all top-rated budgeting apps 
provide the option of creating each of the three types 
of accounts advocated by mental accounting theory 
funds,  wealth  and 
(Thaler,  1999):  available 
expenses and those which do use diverse terms for 
these  accounts,  informed  mostly  by  banking  or 
everyday financial practices. The lack of support for 
differentiating among these distinct types of account 
is problematic.

To  address  this,  we  suggest  the  importance  of 
making clear the distinction between what accounts 
for storage of income, i.e. money-in, for expenses, 
i.e.  money-out  and  for  saving  as  supported  by 
mental  account  theory  (Thaler,  1999).  We  also

While  all  budgeting  apps  support  the  tracking 
expenses, a few do not support budgeting and from 
those  that  do,  only  26  apps  do  that  following  the 
mental  accounts  or  money  envelopes  for  specific 
expense  categories  as  advocated  by  mental 
accounting theory (Thaler, 1999) rather than through 
merely single budgets. This is an important finding 
indicating limitations of these apps and the value of 
employing  more  consistently  multiple  budgets  for 
each  of  the  expense  categories.  We  also  suggest 
the  use  of  money  envelopes  for  the  budgets 
to 
allocated 
differentiate  them  from  expense  categories  which 
merely track expense transactions of a specific type. 
Multiple  budgets  or  money  envelopes  are  defined

to  specific  expense  categories,

6

---

<!-- PAGE 7 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

through  the  amount  being  budgeted,  budget  name 
and  budget  period  using  both  system-  and  user-
defined  periods,  although  not  all  apps  provide 
support  for  each  of  these  details. We  suggest  that 
budgeting apps  support such a complete definition 
of  budgets  and  their  allocation  to  specific  expense 
categories. Although the use of envelopes and jars 
has been noticed in previous HCI work on financial 
practices  (Snow and Vyas, 2015a; Vyas et al., 2015, 
2016), this was mostly as a way to store money for 
specific  purposes, 
for  digital 
rather 
materialization  of  mental  accounts.  Therefore,  we 
strongly  call  for  better  design  for  budgeting  app 
articulating  the  concept  of  mental  accounting  and 
support the use of money envelopes with allocated 
budget  to  help  users  organize,  track  and  more 
importantly keep their spending under control.

than

5.4  Grounding Budgeting as Cognitive Process

in Actual Financial Behaviour

the

than

Budgeting  apps  support  the  tracking  of  expenses 
and  monitoring  them  against  available  funds  or 
allocated budget. Such functions however prioritize 
cognitive  operations  rather 
financial 
behaviours themselves. This is reflected in the small 
number  of  budgeting  apps 
integrating  online 
banking to support for instance automatic import of 
the real transactions. This indicates limited support 
for  encouraging  users  to  compare  their  entered 
transactions  with  those  in  bank  statements.  Such 
grounding in actual financial behaviours is crucial for 
infusing practical value and realism to the otherwise 
cognitive exercise of budgeting. We suggest the use 
of clear terminology differentiating banking accounts 
and 
the 
budgeting app.

those  created

transactions

from

in

6.  CONCLUSION

We  report  on  functionality  review  of  45  top-rated 
budgeting apps. Findings suggest the value of more 
nuanced vocabulary for describing the key concepts 
of accounts, transactions and budgets as informed 
by  mental  accounting  theory  and  for  differentiating 
between  tracking  the  transactions  and  monitoring 
the  allocated  budgets  through  money  envelopes. 
We  conclude  with  four  design  implications  for 
financial  technologies  such  as  budgeting  apps 
including  clear  definitions  of  accounts  and 
transaction  and  their  different  types,  supporting 
for 
budgeting 
through  money  envelopes  and 
in 
grounding  budgeting  as  cognitive  process 
financial behaviour.

REFERENCES

A.s., S. (2013) Spendee Budget & Money Tracker, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.cleevio.spendee%0A (Accessed: 1 April 2022).

Available

Play.

Almoallim, S. and Sas, C. (2022) ‘Toward Research-
Informed  Design  Implications  for  Interventions 
Limiting Smartphone Use: Functionalities Review 
of  Digital  Well-being  Apps’,  JMIR  Formative 
Research, 6(4). doi: 10.2196/31730.

Bitrián,  P.,  Buil,  I.  and  Catalán,  S.  (2021)  ‘Making 
finance fun: the gamification of personal financial 
management apps’, International Journal of Bank 
Marketing, 
doi: 
pp. 
10.1108/IJBM-02-2021-0074.

1310–1332.

39(7),

Chung, A. E. et al. (2018) ‘Health and fitness apps 
for hands-free voice-activated assistants: Content 
analysis’, JMIR mHealth and uHealth, 6(9), pp. 1–
13. doi: 10.2196/mhealth.9705.

Connell,  D.  (2017)  Fudget:  Budget  and  expense 
tracking  app,  Google  Play.  Available  at: 
https://play.google.com/store/apps/details?id=co
m.dannyconnell.android.fudget%0A (Accessed: 1 
April 2022).

Google

llc  (2016)  Budget  planner—Expense 
at:

DigitLeaf, 
tracker, 
https://play.google.com/store/apps/details?id=co
m.colpit.diamondcoming.isavemoney  (Accessed: 
1 April 2022).

Available

Play.

DigitLeaf, L. (2017) Family budget-spending tracker, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.colpit.diamondcoming.isavemoneygo%0A 
(Accessed: 1 April 2022).

Available

Play.

Google

Estimate,  B.-B.  (2019)  Expense  Tracker  &  Budget 
at:

Play. 
App, 
https://play.google.com/store/apps/details?id=ex
pense.tracker.income.receipt.budget  (Accessed: 
1 April 2022).

Available

Gunaratne,  J.  and  Nov,  O.  (2015)  ‘Informing  and 
improving  retirement  saving  performance  using 
behavioral 
user 
interfaces’,  Conference  on  Human  Factors  in 
Computing  Systems  -  Proceedings,  2015-April, 
pp. 917–920. doi: 10.1145/2702123.2702408.

theory-driven

economics

Google

HG  Group  Inc.  (2020)  Budget  App  -  Expense 
at:

Tracker, 
https://play.google.com/store/apps/details?id=co
m.hg.moneymanager.budgetapp  (Accessed:  1 
April 2022).

Available

Play.

ACKNOWLEDGMENTS

First  author’s  work  was  supported  by  Taibah 
University,  Saudi  Arabia  and  the  Saudi  Arabian 
Cultural Bureau, London.

Kaye,  J.  J.  et  al.  (2014)  ‘Money  talks:  Tracking 
finances’,  Conference  on  Human 
personal 
Factors in Computing Systems - Proceedings, pp. 
521–530. doi: 10.1145/2556288.2556975.

7

---

<!-- PAGE 8 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

Labs, V. (2019) Expense Tracker - Money Manager 
at:

&  Budget,  Google  Play.  Available 
https://play.google.com/store/apps/details?id=co
m.vlab.expense.tracker (Accessed: 1 April 2022).

Lee, M. K., Kiesler, S. and Forlizzi, J. (2011) ‘Mining 
behavioral  economics 
to  design  persuasive 
technology  for  healthy  choices’,  Conference  on 
- 
Human  Factors 
Proceedings, 
doi: 
10.1145/1978942.1978989.

in  Computing  Systems 
pp.

325–334.

Letondor, B. (2015) EasyBudget - Personal budget 
planning made simple, Google Play. Available at: 
https://play.google.com/store/apps/details?id=co
m.benoitletondor.easybudgetapp  (Accessed:  1 
April 2022).

Lewis, M. and Perry, M. (2019) ‘Follow the money: 
Managing personal finance digitally’, Conference 
on  Human  Factors  in  Computing  Systems  - 
Proceedings, 
doi: 
10.1145/3290605.3300620.

1–14.

pp.

LLC, Ib. (2017) Money pro, Google Play. Available 
at: https://play.google.com/store/apps/details?id= 
com.ibearsoft.moneyproandroid%0A  (Accessed: 
1 April 2022).

Lolla, S. and Sas, C. (2023) ‘Evaluating Mobile Apps 
Targeting  Personal  Goals’,  Conference  on 
Human  Factors 
- 
in  Computing  Systems 
Proceedings. doi: 10.1145/3544549.3585725

North,  H.

(2011)  MoneyWise,  Google  Play. 
Available  at:  https://play.google.com/store/apps/ 
details?id=com.handynorth.moneywise_free% 
0A (Accessed: 1 April 2022).

Park,  J.,  Lee,  H.  and  Park,  S.  (2021)  ‘Goldentime: 
Exploring  system-driven  timeboxing  and  micro-
financial incentives for self-regulated phone use’, 
Conf. on Human Factors in Computing Systems - 
Proceedings. doi: 10.1145/3411764.3445489.

Partners,  D.  (no  date)  Goodbudget:  Budget  & 
at:

Finance,  Google 
https://play.google.com/store/apps/details?id=co
m.dayspringtech.envelopes%0A 
April 2022).

(Accessed:  1

Available

Play.

Qu, C. et al. (2020) ‘Functionality of top-rated mobile 
apps  for  depression:  Systematic  search  and 
evaluation’, JMIR Mental Health, 7(1), pp. 1–13. 
doi: 10.2196/15321.

QYResearch  (no  date)  Global  Personal  Financial 
Management  Tools  Market  Size,  Status  and 
at: 
Forecast 
https://www.marketresearch.com/QYResearch-
Group-v3531/Global-Personal-Financial-
Management-Tools-12732938/ 
December 2022).

(Accessed:  26

2019-2025.

Available

Snow,  S.  and  Vyas,  D.  (2015a)

the 
alignment: An exploration of budgeting practices

‘Fixing

in  the  home’,  Conference  on  Human  Factors  in 
Computing Systems - Proceedings, 18, pp. 2271–
2276. doi: 10.1145/2702613.2732808.

Snow,  S.  and  Vyas,  D.

‘Fostering 
family 
collaboration 
finances’,  OzCHI  2015:  Being  Human 
- 
Conference  Proceedings,  pp.  380–387.  doi: 
10.1145/2838739.2838746.

the  management  of

(2015b)

in

Softs, E. (no date) Home Budget - Money Manager, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.easysoftsalahi.app.appFree%0A (Accessed: 1 
April 2022).

Available

Play.

Stockinger,  T.  et  al.  (2013)  ‘SmartPiggy:  A  piggy 
bank that talks to your smartphone’, Proceedings 
of  the  12th  International  Conference  on  Mobile 
and  Ubiquitous  Multimedia,  MUM  2013,  43,  pp. 
5–6. doi: 10.1145/2541831.2541869.

Tanu,  F.  (2011)  SimpleBudget  (Envelope  Budget), 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.simplebudget%0A (Accessed: 1 April 2022).

Available

Play.

Thaler,  R.  H.  (1999)  ‘Mental  accounting  matters’, 
Journal 
Decision  Ma, 
Behavioral 
206(September  1998),  pp.  241–268.  doi: 
10.1017/CBO9780511803475.015.

of

Vines, J., Dunphy, P. and Monk, A. (2014) ‘Pay or 
delay: The role of technology  when managing  a 
low  income’,  Conference  on  Human  Factors  in 
Computing Systems - Proceedings, pp. 501–510. 
doi: 10.1145/2556288.2556961.

VoPo  (2015)  Easy  Home  Finance,  Google  Play. 
Available  at:  https://play.google.com/store/apps/ 
details?id=vopo.easyhomefinance  (Accessed:  1 
April 2022).

Vyas, D. et al. (2015) ‘Being thrifty on a $100K wage: 
Austerity  in  family  finances’,  Proceedings  of  the 
ACM  Conference  on  Computer  Supported 
Cooperative Work, CSCW, 2015-Janua, pp. 167–
170. doi: 10.1145/2685553.2698998.

Vyas,  D.  et  al.  (2016)  ‘Social  organization  of 
household finance: Understanding artful financial 
systems in the home’, in Proceedings of the ACM 
Conference on Computer Supported Cooperative 
for  Computing 
Work,  CSCW.  Association 
Machinery, 
doi: 
10.1145/2818048.2819937.

1777–1789.

pp.

Yjteam (2017) DAILY POCKET - Budget Manager, 
at:

Google 
https://play.google.com/store/apps/details?id=kr.
co.yjteam.dailypay (Accessed: 1 April 2022).

Available

Play.

Zaidan, S. and Roehrer, E. (2016) ‘Popular mobile 
phone  apps  for  diet  and  weight  loss:  A  content 
analysis’,  JMIR  mHealth  and  uHealth,  4(3).  doi: 
10.2196/mhealth.5406.

8

---

<!-- PAGE 9 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

Appendix A

1 
App name

1 Money  (PixelRush, 2017)

Alzex Finance (Anna Shirokova, 
2015) 
AndroMoney (AndroMoney, 
2011) 
Bills Reminder (TimelyBills, 
2015) 
Bluecoins Finance (Mabuhay 
Software, 2016) 
Budget App (HG Group Inc., 
2020) 
Budget planner (DigitLeaf, 2016) 
CoinKeeper (LLC, 2015) 
DAILY POCKET (Yjteam, 2017) 
Easy Home (VoPo, 2015) 
EasyBudget (Letondor, 2015) 
Expense Manager (Bishinews, 
2010) 
Expense Manager (Manager, 
2012) 
Expense Tracker (Labs, 2019) 
Expense Tracker (Estimate, 
2019) 
Expense Tracker (Tracker, 2016) 
Family budget (DigitLeaf, 2017) 
Fast Budget (SRL, 2014) 
Fudget (Connell, 2017) 
GnuCash (GnuCash, 2012)     
Goodbudget (Partners, no date) 
Home Budget (Softs, no date) 
Home Budget (SIRI, 2013) 
Home Finance (SoftMobile, 
2015) 
Income Expense (SARAF, 
2019) 
Mobills (M. Inc., 2013) 
Monefy (Reflectly, 2014)  
Money Manager (R. Inc., 2013) 
Money manager (Exp, 2020)  
Money Manager (Apps, 2014) 
Money pro (LLC, 2017) 
Money Tracker (Notes, 2021)  
Money+ (Studios, 2020) 
MoneyWise (North, 2011) 
Monny (Greamer, 2017) 
Monthly Expenses (Baruah, 
2016) 
My Expenses  (Totschnig, 
2012) 
My Finances (7csolutions, 
2015) 
SimpleBudget (Tanu, 2011) 
Spendee Budget (A.s., 2013) 
Spending Tracker (Ltd, 2014) 
Toshl Finance (Inc., no date) 
Vault (Tubin, 2013) 
Wallet (BudgetBakers, 2011) 
YNAB (YouNeedABudget, 
2015)

Tracking transaction: funds

Tracking transaction: expenses

2  
Create 
Funds

3      
Create 
funds 
category

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

4 
Enter 
funds 
currency 
√

5 
Set 
 funds 
date 
√ 
√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

6 
Set  
 funds 
 time

7 
Create  
Expense

8 
Create 
 expense  
category

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√ 
√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

9 
Enter 
expense 
currency 
√ 
√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

10 
Set 
 date for  
expense

11 
Set 
 time for  
expense

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√ 
√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

Table 1: The main functionalities and subfunctionalities of funds and expenses for the 45 top-rated budgeting 
apps.

9

---

<!-- PAGE 10 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

1 
App name

2 
Transaction 
account

3 
Saving 
account

1 Money  (PixelRush, 2017) 
Alzex Finance (Anna Shirokova, 
2015) 
AndroMoney (AndroMoney, 
2011) 
Bills Reminder (TimelyBills, 
2015) 
Bluecoins Finance (Mabuhay 
Software, 2016) 
Budget App (HG Group Inc., 
2020) 
Budget planner (DigitLeaf, 2016) 
CoinKeeper (LLC, 2015) 
DAILY POCKET (Yjteam, 2017)

Easy Home (VoPo, 2015)

EasyBudget (Letondor, 2015) 
Expense Manager (Bishinews, 
2010) 
Expense Manager (Manager, 
2012) 
Expense Tracker (Labs, 2019) 
Expense Tracker (Estimate, 
2019) 
Expense Tracker (Tracker, 2016)

Family budget (DigitLeaf, 2017)

Fast Budget (SRL, 2014)

Fudget (Connell, 2017) 
GnuCash (GnuCash, 2012)     
Goodbudget (Partners, no date)

Home Budget (Softs, no date)

Home Budget (SIRI, 2013) 
Home Finance (SoftMobile, 
2015) 
Income Expense (SARAF, 
2019) 
Mobills (M. Inc., 2013)

Monefy (Reflectly, 2014)

Money Manager (R. Inc., 2013)

Money manager (Exp, 2020)

Money Manager (Apps, 2014)

Money pro (LLC, 2017)

Money Tracker (Notes, 2021)

Money+ (Studios, 2020)

MoneyWise (North, 2011)

Monny (Greamer, 2017) 
Monthly Expenses (Baruah, 
2016) 
My Expenses  (Totschnig, 
2012) 
My Finances (7csolutions, 
2015) 
SimpleBudget (Tanu, 2011)

Spendee Budget (A.s., 2013)

Spending Tracker (Ltd, 2014)

Toshl Finance (Inc., no date)

Vault (Tubin, 2013)

Wallet (BudgetBakers, 2011) 
YNAB (YouNeedABudget, 
2015)

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

*

√

√

√

Tracking transaction accounts

Monitoring budgets

4 
Link 
transaction 
to account 
√

5    
Transfer 
between 
accounts 
          √

6 
Set 
date for 
transfer 
√

7 
Set 
time for  
transfer

8 
Transac-
tion 
attachment

9 
Link app 
to bank 
account

10 
Create 
single 
budget

11 
Create 
multiple 
budgets 
√

12 
Enter 
budget 
name 
√

13 
Set 
budget 
period 
√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

*

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

*

√

√

*

*

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

*

√

√

√

√

*

√

√

√

*

*

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

√

*

*

*

*

*

*

*

Table 2: The main functionalities and subfunctionalities of transaction accounts, transfer between them, and the 
types of provided budgets of the 45 top-rated budgeting apps (* refers to the premium feature in the apps).

10

---

<!-- PAGE 11 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

REFERENCES FOR APPENDIX A

7csolutions  (2015)  My  Finances,  Google  Play. 
at:

Available 
https://play.google.com/store/apps/details?id=co
m.sevencsolutions.myfinances%0A (Accessed: 1 
April 2022).

AndroMoney (2011) AndroMoney (Expense Track), 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.kpmoney.android (Accessed: 1 April 2022).

Available

Play.

Anna Shirokova (2015) Alzex Finance, Google Play. 
at:

Available 
https://play.google.com/store/apps/details?id=co
m.alzex.finance (Accessed: 1 April 2022).

Apps,  A.  P.  (2014)  Money  Manager:  AZV  Money 
at:

Play. 
Pro, 
https://play.google.com/store/apps/details?id=co
m.azv.money%0A (Accessed: 1 April 2022).

Available

Google

Google

Baruah,  B.  (2016)  Monthly  Expenses:  Manage 
at:

Money, 
https://play.google.com/store/apps/details?id=co
m.kaushikbaruah.quickexpensemanagerfree%0
A (Accessed: 1 April 2022).

Available

Play.

Bishinews  (2010)  Expense  Manager,  Google  Play. 
at:

Available 
https://play.google.com/store/apps/details?id=co
m.expensemanager (Accessed: 1 April 2022).

Google

(2011)  Wallet:  Budget  Planner 
at:

BudgetBakers 
Tracker, 
https://play.google.com/store/apps/details?id=co
m.droid4you.application.wallet%0A (Accessed: 1 
April 2022).

Available

Play.

Google

llc  (2016)  Budget  planner—Expense 
at:

DigitLeaf, 
tracker, 
https://play.google.com/store/apps/details?id=co
m.colpit.diamondcoming.isavemoney  (Accessed: 
1 April 2022).

Available

Play.

Exp, I. M. (2020) Money manager, expense tracker, 
budget,  wallet,  Google  Play.  Available  at: 
https://play.google.com/store/apps/details?id=ru.i
nnim.my_finance%0A (Accessed: 1 April 2022).

GnuCash (2012) GnuCash, Google Play. Available 
at:https://play.google.com/store/apps/details?id=
org.gnucash.android%0A 
2022).

(Accessed:  1  April

Greamer (2017) Monny, Google Play. Available at: 
https://play.google.com/store/apps/details?id=co
m.greamer.monny.android%0A 
April 2022).

(Accessed:  1

Inc.,  M.  (2013)  Mobills:  Budget  Planner,  Google 
at:

Play. 
https://play.google.com/store/apps/details?id=br.

Available

11

com.gerenciadorfinanceiro.controller%0A 
(Accessed: 1 April 2022).

Inc., R. (2013) Money Manager Expense & Budget, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.realbyteapps.moneymanagerfree%0A 
(Accessed: 1 April 2022).

Available

Play.

Inc., T. (no date) Toshl Finance - Personal Budget & 
Expense  Tracker,  Google  Play.  Available  at: 
https://play.google.com/store/apps/details?id=co
m.thirdframestudios.android.expensoor%0A 
(Accessed: 1 April 2022).

LLC,  D.  (2015)  CoinKeeper:  expense,  money 
manager, budget planner, Google Play. Available 
at: 
https://play.google.com/store/apps/details?id=co
m.disrapp.coinkeeper.material (Accessed: 1 April 
2022).

Ltd,  M.  R.  (2014)  Spending  Tracker,  Google  Play. 
at:

Available 
https://play.google.com/store/apps/details?id=co
m.mhriley.spendingtracker%0A 
April 2022).

(Accessed:  1

Mabuhay  Software  (2016)  Bluecoins  Finance: 
Budget,  Mon,  Google  Play.  Available  at: 
https://play.google.com/store/apps/details?id=co
m.rammigsoftware.bluecoins  (Accessed:  1  April 
2022).

Manager,  H.  E.  (2012)  Expense  Manager,  Google 
Play. 
at: 
https://play.google.com/store/apps/details?id=me
diavision.handwallet (Accessed: 1 April 2022).

Available

Notes,  Q.  S.  &  Q.  C.  G.  &  R.  &  (2021)  Money 
Tracker:  Expense  Tracker,  Wallet,  Budget  App, 
Google 
at: 
https://play.google.com/store/apps/details?id=mo
neytracker.expensetracker.budgetplanner.spendi
ngtracker%0A (Accessed: 1 April 2022).

Available

Play.

PixelRush (2017) 1Money: expense tracker budget, 
at:

Google 
https://play.google.com/store/apps/details?id=or
g.pixelrush.moneyiq (Accessed: 1 April 2022).

Available

Play.

Reflectly  (2014)  Monefy  -  Budget  Manager  and 
Expense Tracker app, Google Play. Available at: 
https://play.google.com/store/apps/details?id=co
m.monefy.app.lite%0A (Accessed: 1 April 2022).

SARAF, A. (2019) Income Expense- daily expenses, 
Google 
at: 
https://play.google.com/store/apps/details?id=inc
omeexpense.incomeexpense&hl=en_GB&gl=US
%0A (Accessed: 1 April 2022).

Available

Play.

SIRI (2013) Home Budget Manager Lite With Sync, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.siri.budgetdemo%0A (Accessed: 1 April 2022).

Available

Play.

---

<!-- PAGE 12 -->

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking 
Alenazi • Sas

Totschnig,  M.  (2012)  My  Expenses,  Google  Play. 
at:

Available 
https://play.google.com/store/apps/details?id=or
g.totschnig.myexpenses%0A  (Accessed:  1  April 
2022).

Tracker,  F.-E.  (2016)  Expense  Tracker,  Family 
at:

Budget, 
https://play.google.com/store/apps/details?id=co
m.finart%0A (Accessed: 1 April 2022).

Available

Google

Play.

Tubin,  S.  (2013)  Vault  -  Budget  Planner,  Google 
at:

Play. 
https://play.google.com/store/apps/details?id=ru.
tubin.bp%0A (Accessed: 1 April 2022).

Available

Google

YouNeedABudget  (2015)  YNAB  (You  Need  A 
at:

Budget), 
https://play.google.com/store/apps/details?id=co
m.youneedabudget.evergreen.app%0A 
(Accessed: 1 April 2022).

Available

Play.

SoftMobile  (2015)  Home  Finance,  Google  Play. 
at:

Available 
https://play.google.com/store/apps/details?id=co
m.mec.homefinance (Accessed: 1 April 2022).

SRL,  A.  (2014)  Fast  Budget  -  Expense  Manager, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.blodhgard.easybudget%0A (Accessed: 1 April 
2022).

Available

Play.

Studios, Z. (2020)  Money+ Cute Expense Tracker, 
at:

Google 
https://play.google.com/store/apps/details?id=co
m.zotiger.accountbook%0A  (Accessed:  1  April 
2022).

Available

Play.

TimelyBills (2015)  Bills Reminder, Budget Planner, 
at:

Google 
https://play.google.com/store/apps/details?id=in.
usefulapp.timelybills (Accessed: 1 April 2022).

Available

Play.

12

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

http://dx.doi.org/10.14236/ewic/BCSHCI2023.1
Evaluating Budgeting Apps: Limited Support
for Budgeting Compared to Tracking
Mariam Alenazi Corina Sas
Lancaster University Lancaster University
Lancaster, UK Lancaster, UK
m.alenazi@lancaster.ac.uk c.sas@lancaster.ac.uk
Financial behaviour is deeply embedded in our lives, yet for many people its success remains
problematic. The need for supporting tools in this space is reflected in the growing number and
popularity of budgeting apps, albeit limited research has focused on evaluating them. This paper
describes a functionality review from the lens of mental accounting theory of 45 top-rated budgeting
apps selected from 1335 apps on Google Play Store and Apple Store. Findings indicate that while all
apps support tracking of transactions, one third of the apps do not support budgeting informed by
money envelopes. We also report challenges regarding the meaning of key concepts of “accounts”
and “transactions” for which we proposed novel design implications including a more nuanced
vocabulary to talk about accounts and transaction types, new knowledge to have better support for
budgeting through mental accounting theory and grounding budgeting as cognitive process in
actual financial behaviour.
Financial behaviours. Budgeting apps. Money envelopes
1. INTRODUCTION economics theory (Thaler, 1999) according to which
people commonly partition and budget money
HCI research on money and financial practices has separately in mental accounts usually materialized
focused mostly on exploratory studies (Kaye et al., through money envelopes for specific purposes. As
2014; Vines, Dunphy and Monk, 2014; Snow and the economist Thaler (Thaler, 1999) stated the main
Vyas, 2015b; Vyas et al., 2016; Lewis and Perry, purpose of mental accounting is to use labelled
2019), whose findings indicate that people tend to categories for sources such as regular income and
use digital tools to a limited extent. As a result, we uses of funds such as food, to help individuals and
have little understanding of how digital tools such as households organize, track and monitor their
mobile apps for personal budgeting could facilitate spending. Our findings indicate insufficient support
the tracking and monitoring of financial behaviours for budgeting functionality and important challenges
such as tracking and budgeting for daily of such apps due to the overlapping meanings and
expenditures. In addition to mobile banking, financial insufficient clarity of the key concepts. We discuss
management apps supporting users to track new design implications for addressing them
expenses and create budgets, have also including a more nuanced vocabulary to talk about
experienced rapid growth in the recent years as one accounts, transactions and budgeting, better
of the fastest growing categories of finance apps support for budgeting in addition to tracking and in
(Bitrián, Buil and Catalán, 2021). In 2018, the global particular for multiple rather than single budgets.
revenue for the such tools was over $1.4 million and
estimated to at least double its value by 2025
(QYResearch, no date). While previous HCI 2. BACKGROUND
research has explored functionalities of publicly
available apps on marketplaces in domains such as Most HCI work on financial behaviour has focused
fitness (Chung et al., 2018), diet (Zaidan and on tracking such practices for individuals (Kaye et
Roehrer, 2016), depression (Qu et al., 2020), al., 2014; Vines, Dunphy and Monk, 2014; Lewis and
personal goals (Lolla and Sas, 2023) or digital Perry, 2019) and households (Snow and Vyas,
wellbeing (Almoallim and Sas, 2022), limited such 2015b, 2015a; Vyas et al., 2015, 2016) and their
preferred tools. To track their spending, most of
work has looked at budgeting apps.
previous findings emphasize analogue tools such as
To address this gap, we explore the functionalities coin jars (Snow and Vyas, 2015a; Vyas et al., 2016),
of top-rated budgeting apps by employing a mental enabling people to see how much they have spent.
accounting lens. Mental accounting is a behavioural
© Alenazi et al. Published by BCS
1
Learning and Development Ltd.
Proceedings of BCS HCI 2023, UK

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
In addition to coin jars, envelops (Snow and Vyas, descriptions, followed by expert evaluation. The
2015a; Vyas et al., 2015) are also commonly used analysis of apps’ descriptions, led to the
budgeting tools for monitoring expenses as their identification of main functionalities such as tracking
names reflect the purpose of money stored in transactions and monitoring budgets. The limited
specific envelopes, such as grocery money. There information available in the apps’ descriptions was
have been other common analogue tools for rather restricted to these broad functionalities.
budgeting and tracking spending, such as wall
For the expert evaluation we leveraged key
organizers, bills attached to refrigerators, folders
concepts from mental accounting theory (Thaler,
and handwritten diaries (Kaye et al., 2014; Snow
and Vyas, 2015b, 2015a; Vyas et al., 2015, 2016), 1999) to identify functionalities pertaining to funds,
which are preferred due to their simplicity. i.e. sources and uses; expenditures and categories
for grouping them and mental accounts or
In contrast to such rich use of analogue tools, HCI
envelopes for allocating budgets to such categories.
research has reported limited digital tools supporting
Additional functionalities identified in the reviewed
financial practices and in particular of budgeting
apps include create transaction accounts, link the
apps. For instance, Snow and Vyas’s study (Snow
app to real bank account, as well as set date, time
and Vyas, 2015a) showed banking apps as more
and currency for transactions. The identification of
common digital tool for tracking financial
these functionalities involved iterations that the two
transactions, with only one third of the 15
authors discussed over several months.
participants having used budgeting apps which they
tend to discontinue after a short period of time due While most functionalities were easily identified by
to the perceived challenge of entering expense and each of them from apps' descriptions, functionalities
of lack of adequate control over their spending. reflecting transactions and accounts required
Spreadsheets were another common tools mostly additional clarification reached through weekly
for tracking transactions (Kaye et al., 2014; Vyas et conversations: transactions are to be considered
al., 2016), rather than budgeting purposes. Despite broadly as encompassing income, expense and
the growing HCI interest in personal finances, we transfer of money between accounts. Other
have seen limited theoretical underpinning of such clarification concerned transaction accounts as
work, especially from the lens of mental accounting containers holding each of the three types of
theory, although the value of behavioural economics transactions. Additional functionalities have been
has been previously suggested (Stockinger et al., also identified through this iterative process, namely
2013) for healthy choices (Lee, Kiesler and Forlizzi, linking a transaction to a transaction account and
2011), digital wellbeing (Park, Lee and Park, 2021) differentiating existing categories for both income
or retirement savings (Gunaratne and Nov, 2015). and expense categories. Appendix A shows the
complete set of functionalities.
To summarize, HCI research on financial practices
has highlighted mostly the use of analogue tools and While analysis of the apps’ descriptions was
limited use of digital ones, especially budgeting completed by the first author, who also completed
apps. Most of such work has also limitedly engaged the expert evaluation of all 45 apps using Galaxy
the mental accounting theory (Thaler, 1999) despite S21+. Second author also performed expert
initial acknowledgments of the value of behavioural evaluation of five apps on an iPhone 12, in order to
economics in HCI. discuss and reconcile the identified functionalities.
As the second author used iOS platform, these five
apps were randomly selected from the 24 apps
3. METHOD available on Apple Store.
To identify the budgeting apps, we searched the two
marketplaces in the UK: Google Play Store (for 4. RESULTS
Android) and Apple Store (for iOS) using three
keywords: budget, budgeting and finance. From the The 45 identified apps belong mostly to Finance
total of 1335 apps as shown in Figure 1, we removed category on marketplaces (44 apps) and one app to
duplicates, apps that were not free, apps not related Business category. Findings indicate different types
to budgeting, those requiring access to one’s bank of accounts and inconsistent terminology for
accounts and retained top-rated apps with an labelling them. Outcomes also indicate two main
average rating score of four out of five and with at types of budgeting apps, those that provide
least 1000 reviews. This led to 45 apps being functionality of tracking expenses without monitoring
included in the analysis (Table 1, col 1): 21 apps (8 apps) and those that provide also, in addition to
available only on Google Play Store and 24 apps tracking expenses, the budgeting functionality for
available on both platforms. The functionalities of monitoring expenses against their allocated budget
these 45 apps were iteratively reviewed to identify (33 apps). The latter use either single budget for all
functionalities, firstly through analysing all the apps’ expenses irrespectively of their different categories
2

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas

|     |     | 1335 apps identified from  |     |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | --- | --- | --- |
|     |  n  |                            |     |     |     |     |     |
|     | o   | Google Play (n= 742)       |     |     |     |     |     |
ita

c
|     | ifitn | Apple Store (n= 593)  |     | 404 apps excluded:   |     |     |     |
| --- | ----- | --------------------- | --- | -------------------- | --- | --- | --- |

|     | e   |     |     | Duplicated apps= 326 (Google Play: n=191, Apple  |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
d
|     | I   |     |     | Store: n=128, both: n= 7)  |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | --- |

Not free apps= 78 (Google Play: n=18, Apple
|     |     | 931 Remaining  |     | Store: n= 60)  |     |     |     |
| --- | --- | -------------- | --- | -------------- | --- | --- | --- |

|     |     | Google Play (n=533),  |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- | --- |
Apple Store (n=398)

810 apps excluded:
|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |

|     | g   |     |     | Apps with less than 1000 reviews and lower  |     |     |     |
| --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- |
n
|     | in  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
than 4.0 in rating score (Google Play: n=439,
e
|     | e   |     |     | Apple Store: n= 371)  |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- |
r
c
|     | S   | 121 Remaining               |     |     |     |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --- |
|     |     |                             |     |     |     |     |     |
|     |     | (Google Play: n= 94, Apple  |     |     |     |     |     |
Store: n= 27)
|     |     |     |     | 71 apps excluded:   |     |     |     |
| --- | --- | --- | --- | ------------------- | --- | --- | --- |

Apps not related to budgeting (Google
Play: n=44, Apple Store: n= 27)

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
50 Remaining

(Google Play only)
|     | d   |     |     |                    |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- |
|     | e   |     |     | 5 apps excluded:   |     |     |     |
d
|     | u   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
lc
Apps required access to one's bank
|     | n   |                                    |     |           |     |     |     |
| --- | --- | ---------------------------------- | --- | --------- | --- | --- | --- |
|     | I   |                                    |     | account.  |     |     |     |
|     |     | Eligible apps for analysis Google  |     |           |     |     |     |
|     |     | Play: n= 45                        |     |           |     |     |     |

                                          Figure 1. PRISMA diagram describing the process of apps’ selection.

(seven apps- Table 2, col 10) or multiple budgets  storing available funds such as monthly income (i.e.
using a different budget for each expense category  money-in), those for depositing and storing assets or
such as bills, rent, groceries (26 apps- Table 2, col  wealth such as saving accounts and those for using
11,  albeit  4  of  these  provide  budgeting  only  as  or spending the available funds (i.e. money-out) .
premium, subscription-based functionality). Most of  With regard to the latter, the theory also specifies
the apps show limited theoretical underpinning, with  that people create mental accounts for allocating
only two apps Goodbudget (Partners, no date) and  money for specific purposes or in other words for
SimpleBudget (Tanu, 2011) explicitly mentioning in  budgeting  for  specific  categories  of  expenses,
their description that their design was informed by  similar to money envelopes which will be discussed
money envelope systems, albeit specific reference  later. With regard to these three types of accounts
to mental accounting theory (Thaler, 1999) is not  proposed  by  mental  accounting  theory,  findings
made.  Also,  no  app’s  description  reports  its  indicate that most of the apps support depositing
evaluation though users' studies.   funds (44 apps) and paying for expenses (45 apps),
with fewer apps support saving (11 apps- Table 2,
| 4.1 Accounts: Types and Terminology   |     |     |     | col 3).   |     |     |     |
| ------------------------------------- | --- | --- | --- | --------- | --- | --- | --- |
A  significant  finding  is  the  concept  of  accounts  However, while most of the apps (41 apps- Table 2,
col 2) have accounts for depositing funds or for
partially employed by our explored apps in order to
|          |                    |                    |         | paying  | for  expenses  | ,  the  remaining  | four  apps  |
| -------- | ------------------ | ------------------ | ------- | ------- | -------------- | ------------------ | ----------- |
| support  | the  organization  | of  transactions.  | Mental  |         |                |                    |             |
accounting  theory  (Thaler,  1999)  identifies  three  (DAILY  POCKET  (Yjteam,  2017),  EasyBudget
|     |     |     |     | (Letondor,  | 2015),  | Expense  Tracker  | -  Money  |
| --- | --- | --- | --- | ----------- | ------- | ----------------- | --------- |
types of accounts, namely those for depositing and
Manager & Budget (Labs, 2019) and Budget App -
3

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
Expense Tracker (HG Group Inc., 2020)) merely  and money-out are not employed by any of the apps
support the depositing of money on the app’s home  except  one  app:  GnuCash  which  uses  multiple
screen rather than in dedicated income account.  accounts such as income, expenses and assets.
This is problematic as these four apps also fail to
provide the option of linking individual transactions  4.2 Creating and Tracking Transactions:
to specific accounts, as they are all stored directly  Income, Expenses, Transfer
on the home screen. Even for the remaining apps
Study findings also highlight the important distinction
providing the option of creating income, saving or
expense  accounts,  the  income  and  expense,  between accounts and transactions. We suggest
|           |               |     |            |       |          |      | that  accounts  | are  | similar  | to  containers  | for  | the  |
| --------- | ------------- | --- | ---------- | ----- | -------- | ---- | --------------- | ---- | -------- | --------------- | ---- | ---- |
| although  | conceptually  |     | distinct,  | they  | support  | the  |                 |      |          |                 |      |      |
organization of transactions, while each transaction
depositing and spending of the funds from the same
container, respectively.  In other words, for most of  represents the movement of money from a source to
a destination, in other words, transactions are the
| the  apps,  | the  | income  | and  | expense  | accounts,  |     |     |     |     |     |     |     |
| ----------- | ---- | ------- | ---- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
ones that allow accounts to be replenished with
although conceptually distinct, in practice they tend
funds or depleted of funds. Findings indicate three
to be one and the same account similar to a bank
account or a wallet where money are both deposited  types of transactions for (i) depositing funds, (ii)
paying for expenses or (iii) transferring money from
in and spent from.
|     |     |     |     |     |     |     | income  | to  expense  | accounts  | which  | are  further  |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --------- | ------ | ------------- | --- |
Findings also indicate various terms for referring to
|     |     |     |     |     |     |     | detailed.  | All  | apps  | apart  from  | one  | app  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----- | ------------ | ---- | ---- |
such accounts, inconsistently used across the apps.  (SimpleBudget: Envelope Budget) allow users to
The employed terminology appears to draw from two  deposit  funds,  through  income  transactions  (44
| different  | sources:  | banking  | domain  |     | and  | everyday  |     |     |     |     |     |     |
| ---------- | --------- | -------- | ------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- |
apps- Table 1, col 2) by specifying the name or label
| financial  | practices.  | A   | significant  | outcome  |     | is  that  |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------------ | -------- | --- | --------- | --- | --- | --- | --- | --- | --- |
of the transactions, usually referring to the source of
most of the apps employed terms from banking  money such as salary, together with the specific
| domain  | for  naming  |     | or  labelling  | accounts.  |     | Such  |     |     |     |     |     |     |
| ------- | ------------ | --- | -------------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- |
amount of money being deposited, the date (all but
| terms,  | used  | for  income,  |     | saving  | or  | expense  |     |     |     |     |     |     |
| ------- | ----- | ------------- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
two apps- Table 1, col 5) and time (18 apps- Table
accounts, include: virtual bank accounts (nine apps),  1, col 6) of the income transaction and its currency
virtual cash accounts (17 apps), saving accounts (11  (40 apps – Table 1, col 4).
apps), investment accounts (seven apps), virtual
From the 40 apps supporting the specification of the
credit card account (17 apps), virtual debt account
currency of deposited funds, 12 apps provide a pre-
(13 apps), with many apps (18 apps) employing
more than one of these terms for organizing funds,  defined list of currencies allowing users to choose
wealth and expenses. While such terminology for  different  one  for  each  income  transaction  being
created, while 28 apps provide a pre-defined list of
banking domain can be useful as it builds on users’
|              |       |          |             |     |      |         | currencies  | albeit  | in  the  | app  settings  | so  | each  |
| ------------ | ----- | -------- | ----------- | --- | ---- | ------- | ----------- | ------- | -------- | -------------- | --- | ----- |
| familiarity  | with  | banking  | practices,  |     | the  | direct  |             |         |          |                |     |       |
association with banking practices is limited since  transaction  with  a  different  currency  requires
changing it in the app setting. These two options
| only  seven  | apps  | support  | the  | integration  |     | of  the  |     |     |     |     |     |     |
| ------------ | ----- | -------- | ---- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
prioritize either the ease of changing currency or of
budgeting apps with users’ online banking services
and only as premium feature (Table 2, col 9). This  keeping it constant across transactions. Unlike the
terminology  from  banking  domain  also  fails  to  rest of the apps, SimpleBudget app does not support
|     |     |     |     |     |     |     | the  creation  | of  | an  income  | account;  | instead,  | it  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --------- | --------- | --- |
provide specific types of expense accounts such as
those for different categories of expenses or the  supports users to create multiple envelopes, each
equivalent of money envelopes (Thaler, 1999), since  with  its  own  budget  or  available  fund,  without
specifying the total amount of available funds to be
| banking  | accounts  |     | capturing  | spending  |     | relate  |     |     |     |     |     |     |
| -------- | --------- | --- | ---------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
allocated across all the envelopes. This can be
exclusively to debt repayment such as credit or debit
card or mortgage, but not for instance to monthly  problematic in terms of the cognitive load needed to
ensure that the available funds not captured by the
grocery, bills or rent budgets.
app, do not exceed the cumulative value of the
Other terms to label accounts are borrowed from
money envelopes.
| everyday  | financial  | practices  |          | and  | include  | wallet  |                |     |          |                |      |       |
| --------- | ---------- | ---------- | -------- | ---- | -------- | ------- | -------------- | --- | -------- | -------------- | ---- | ----- |
|           |            |            |          |      |          |         | With  respect  | to  | expense  | transactions,  | all  | apps  |
| (three    | apps:      | Expense    | Tracker  | &    | Budget   | App     |                |     |          |                |      |       |
support users to create them (Table 1, col 7), by
(Estimate, 2019), Easy Home Finance (VoPo, 2015)
and Spendee Budget & Money Tracker (A.s., 2013)),  specifying the names or labels of these transactions,
usually the destination of money such as grocery
financial account (one app: Family budget-spending
|     |     |     |     |     |     |     | expense,  | together  | with  | the  specific  | amount  | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ----- | -------------- | ------- | --- |
tracker (DigitLeaf, 2017)), payment account (one
app – Money pro (LLC, 2017)) or even budget (two  money being paid (45 apps), the date (45 apps-
apps: Fudget: Budget and expense tracking app  Table 1, col 10) and time (18 apps- Table 1, col 11)
of the expense transaction and its currency (41 apps
(Connell, 2017) and Home Budget - Money Manager
(Softs, no date)). Interestingly, with respect to terms  – Table 1, col 9) with similar ease of changing
from everyday practices, findings indicate that clear  currency  or  of  keeping  constant  characterizing
income transactions.
| ones  for  | distinguishing  |     | among  | available  |     | funds,  |     |     |     |     |     |     |
| ---------- | --------------- | --- | ------ | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
wealth and expense accounts or between money-in
4

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
Finding show that four apps also allow the adequate, both for income (36/45 apps and two apps
specification of the payment method for expense premium) and for expense transactions (42/45 apps
transactions, i.e., cash, credit/debit card or cheque. and one app premium) and once crated, these
categories could be re-used later with new
With respect to the mode of entering the
transactions. However, some apps provide the
transactions, most apps support the creation of both
limited option of one-off categories for income (four
income and expense transactions through the same
apps) and expense (two apps). Therefore, with each
interaction by tapping on the plus icon on app’s
new transaction, the user needs to enter the source
home screen (35 apps), by clicking on income button
of income and the expense name. While most apps
or expense button on the app’s home screen (eight
provided one level of categories, 15 apps provided
apps) or by tapping on “register” button on app’s
option for subcategories of transactions. For
home screen which opens another page to create
example, car expense category can have sub-
the income or expense (one app – MoneyWise
categories such as fines, fuel, parking and repairs.
(North, 2011). One remaining app (CoinKeeper:
expense, money manager, budget planner) provides Finally, all transactions can be entered manually (45
different interactions for entering income, i.e., by apps), they can also be automatically imported from
tapping on the plus icon on app’s home screen and online banking accounts linked to the budgeting app
for entering expense, i.e., by dragging a transaction (seven apps), with few apps encouraging users to
account icon into expense category then specify the compare their entered transactions with those of
expense amount from the dragged account. their bank statements (seven apps).
Arguably, the simple interaction for tapping on the
plus icon on app’s home screen to enter both income 4.3 Budgeting: Tracking Balance vs Money
and expense transaction is preferrable in terms of Envelopes
increased usability.
Findings indicate that all apps support budgeting
In addition to income and expense transactions, functionality and therefore the monitoring of
findings also indicate the third type, namely transfer expenses against the allocated budgets (45 apps),
transactions (35 apps- Table 2, col 5), which we although they do so in different ways. While most of
define as transfer of money from a source (available these apps support budgeting under mental
income) to a destination (for expense or saving). In accounts or money envelopes (26 apps), others do
addition to specifying source and destination not (19 apps). We called the latter form of budgeting
accounts (35 apps), transfer transactions could also as single budget and the former as multiple budgets,
specify the amount of money being transferred (35 as further detailed.
apps), transfer date (30 apps- Table 2, col 6), time
(11 apps- Table 2, col 7), currency (25 apps) as well Apps supporting single budget (19 apps) rely on only
as label or receipt which can be attached to the one main budget (usually the same amount as the
transfer (five apps and three apps premium- Table available funds) from which all expenses are to be
2, col 8). Interestingly, most of the apps supporting covered. In these apps, expense transactions are
transfer transactions allow them without sufficient not grouped under specific money envelops with
funds in the source account (33 apps out of 35). Two allocated budgets for each envelope, which would
exceptions include the Family budget-spending be consistent with mental accounting theory (Thaler,
tracker app, where if the transferred amount is larger 1999). Although these apps have a single budget,
they do support a high-level monitoring of expenses
than the available funds, the message of “insufficient
and do so in two ways. While all 19 apps use the
amount” is shown in red colour and the transfer
cannot be completed. For the other app account balance to represent the overspent of
(MoneyWise), the transfer transaction is a premium available funds using the minus symbol, eight apps
feature. do not change the colour of this information, albeit
seven apps use colour red to provide this
An important finding is that similar transactions can information of overspent.
also be grouped in categories, for both income and
expenses transactions. This functionality aligns with Although single budget apps depend on the total
the cognitive operations of grouping different income funds, some of these apps allow to set that fund as
and expenditures into categories mentioned by the explicit budget for all expense (five out of 19 apps).
mental accounting theory (Thaler, 1999). These These five apps do not have a specific budget name
categories could be of two types: provided by the by the user, it was named by the app as budget and
app or defined by the user. The former consists of a the user can set the budget amount and budget
list of categories for income such as salary, bonus, period (Table 2, col 13) as daily (one app - Spending
gift, refund, business and interest (38/45 apps) and Tracker), weekly (two apps - DAILY POCKET -
for expense (40/45 apps) such as grocery, Budget Manager and Spending Tracker), monthly
shopping, transportation, bills, education and rent. (four apps), yearly (one app - Spending Tracker) or
The user defined categories allow users to specify defined by the user (one app - Monny).
new ones if those provided by the app are not
5

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
Four of these 19 apps support also multiple budgets  suggest  the  use  of  consistent  terminology  for
but only as a premium functionality. In contrast to  accounts that clearly defines accounts as containers
single budgets, 26 apps support the creation of  of transactions distinguishing accounts for available
multiple  budgets  which  aligns  with  mental  funds, wealth and expenses (Thaler, 1999).
| accounting  | theory  | (Thaler,  | 1999).  | These  | apps  |     |     |     |     |     |     |     |     |
| ----------- | ------- | --------- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
support  the  functionality  of  creating  money  5.2 Defining Transactions and their Types:
Income, Expenses, Transfer
envelopes by allowing users to allocate different
budgets to distinct expense categories, for instance
for groceries, transport or bills. Furthermore, 15 of  Related to the three types of accounts, findings
indicate transactions reflecting the flow of money
the 26 apps provide the option to personalize the
and their three types for depositing funds, paying for
name of the budget, i.e., budget for bills category
can be called for instance household bill budget,  expenses  or  transferring  money  from  income  to
|     |     |     |     |     |     | expense  | accounts,  |     | which  | however  |     | are  | not  |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------ | -------- | --- | ---- | ---- |
while the remaining 11 apps use the name of the
|                                           |     |     |     |     |        | supported  | by  | all  | apps.  | We  | suggest  | defining  |     |
| ----------------------------------------- | --- | --- | --- | --- | ------ | ---------- | --- | ---- | ------ | --- | -------- | --------- | --- |
| expense category as the name the budget,  |     |     |     |     | i.e.,  |            |     |      |        |     |          |           |     |
transactions and providing options to create each of
budget for bills category is bills budget.
them, with the following details of transaction name,
In addition, the budget period could be also set for  category, amount, currency, date, time, supported
all these 26 apps from predefined periods such as  by most but not all apps. Based on the mental
daily (provided by seven apps), weekly (15 apps),
|     |     |     |     |     |     | accounting theory  |     |     | (Thaler, 1999),  |     | the funds  |     | and  |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ---------------- | --- | ---------- | --- | ---- |
fortnight  (seven  apps),  monthly  (26  apps),  expenses should be labelled as such and grouped
biannually (three apps) and annually (14 apps), with  into  categories  according  to  people  financial
| 17  apps  | providing  | multiple  | predefined  | budgeting  |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
practices. Study findings show limited functionalities
periods. The budgeting periods can also be defined
supporting the allocation of income and expenses
by  users  with  six  apps  providing  the  option  of  into  specific  categories.  This  is  problematic  as
entering a specific date.
spending money from a general pot rather than
specific pots for different expense categories, can
more easily lead to over expenditure. To address
5.  DISCUSSION AND DESIGN IMPLICATIONS
|     |     |     |     |     |     | this  limitation,  |     |     | both  | income  | and  | expense  |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ----- | ------- | ---- | -------- | --- |
transactions should be grouped into categories and
We reviewed the functionalities of the 45 top-rated
|            |       |              |          |      |        | subcategories,  |     | such  | as  | income  |     | and  | salary,  |
| ---------- | ----- | ------------ | -------- | ---- | ------ | --------------- | --- | ----- | --- | ------- | --- | ---- | -------- |
| budgeting  | apps  | to  explore  | if  and  | how  | these  |                 |     |       |     |         |     |      |          |
respectively. These could be both predefined by the
| functionalities  |     | are  grounded  | in  | the  | mental  |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
system or defined by the user.
| accounting  | theory  | (Thaler,  | 1999).  | Our  | findings  |     |     |     |     |     |     |     |     |
| ----------- | ------- | --------- | ------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
indicate limited clarity regarding the two important  For currency, findings indicate two exclusive ways of
terms  of  accounts  and  transactions  and  limited  selecting  it:  for  each  transaction  or  across
support for budgeting functionality. We suggest four
transactions through app settings. We suggest a
design implications including the recommendation  flexible approach allowing users to choose between
for developers to use clearer terminology to define  these  two modes of selecting the currency. For
and differentiate accounts and transactions and their
entering transactions, the simplest interaction that
specific  types,  for  better  supporting  budgeting  we suggest is tapping on the plus icon on app’s
through  money  envelopes,  and  for  grounding  home screen, while for transfer transactions, those
budgeting as mental activity in the actual financial
|     |     |     |     |     |     | with  insufficient  |     |     | available  | funds  |     | should  | be  |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------- | ------ | --- | ------- | --- |
practices.
consistently prevented.
5.1 Defining Accounts and their Types:  5.3 Supporting Budgeting through Money
| Available Fund, Wealth, Expenses  |     |     |     |     |     | Envelopes  |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Findings show that not all top-rated budgeting apps
|     |     |     |     |     |     | While  | all  budgeting  |     | apps  | support  |     | the  tracking  |     |
| --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | ----- | -------- | --- | -------------- | --- |
provide the option of creating each of the three types  expenses, a few do not support budgeting and from
of accounts advocated by mental accounting theory  those that do, only 26 apps do that following the
| (Thaler,  | 1999):  | available  | funds,  | wealth  | and  |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
mental accounts or money envelopes for specific
expenses and those which do use diverse terms for  expense  categories  as  advocated  by  mental
these  accounts,  informed  mostly  by  banking  or  accounting theory (Thaler, 1999) rather than through
everyday financial practices. The lack of support for
merely single budgets. This is an important finding
differentiating among these distinct types of account  indicating limitations of these apps and the value of
is problematic.   employing more consistently multiple budgets for
each of the expense categories. We also suggest
| To  address  |     | this,  we  suggest  | the  importance  |     | of  |           |     |        |            |     |      |               |     |
| ------------ | --- | ------------------- | ---------------- | --- | --- | --------- | --- | ------ | ---------- | --- | ---- | ------------- | --- |
|              |     |                     |                  |     |     | the  use  | of  | money  | envelopes  |     | for  | the  budgets  |     |
making clear the distinction between what accounts
|     |     |     |     |     |     | allocated  | to  | specific  |     | expense  | categories,  |     | to  |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | -------- | ------------ | --- | --- |
for storage of income, i.e. money-in, for expenses,
differentiate them from expense categories which
| i.e.  money-out  |     | and  for  | saving  as  | supported  | by  |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
merely track expense transactions of a specific type.
| mental  | account  | theory  (Thaler,  | 1999).  | We  | also  |     |     |     |     |     |     |     |     |
| ------- | -------- | ----------------- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Multiple budgets or money envelopes are defined
6

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
| through the amount being budgeted, budget name  |     |     |     |     |     |     | REFERENCES  |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
and budget period using both system- and user-
A.s., S. (2013) Spendee Budget & Money Tracker,
| defined  | periods,  | although  |     | not  | all  apps  | provide  |     |     |     |     |     |     |     |
| -------- | --------- | --------- | --- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
support for each of these details. We suggest that  Google  Play.  Available  at:
budgeting apps support such a complete definition  https://play.google.com/store/apps/details?id=co
of budgets and their allocation to specific expense  m.cleevio.spendee%0A (Accessed: 1 April 2022).
categories. Although the use of envelopes and jars
Almoallim, S. and Sas, C. (2022) ‘Toward Research-
has been noticed in previous HCI work on financial
|     |     |     |     |     |     |     | Informed  | Design  | Implications  |     | for  | Interventions  |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------------- | --- | ---- | -------------- | --- |
practices  (Snow and Vyas, 2015a; Vyas et al., 2015,
Limiting Smartphone Use: Functionalities Review
2016), this was mostly as a way to store money for
|           |            |     |         |       |      |          | of  Digital  | Well-being  |     | Apps’,  | JMIR  | Formative  |     |
| --------- | ---------- | --- | ------- | ----- | ---- | -------- | ------------ | ----------- | --- | ------- | ----- | ---------- | --- |
| specific  | purposes,  |     | rather  | than  | for  | digital  |              |             |     |         |       |            |     |
Research, 6(4). doi: 10.2196/31730.
materialization of mental accounts. Therefore, we
Bitrián, P., Buil, I. and Catalán, S. (2021) ‘Making
strongly call for better design for budgeting app
articulating the concept of mental accounting and  finance fun: the gamification of personal financial
support the use of money envelopes with allocated  management apps’, International Journal of Bank
budget  to  help  users  organize,  track  and  more  Marketing,  39(7),  pp.  1310–1332.  doi:
importantly keep their spending under control.  10.1108/IJBM-02-2021-0074.
Chung, A. E. et al. (2018) ‘Health and fitness apps
5.4 Grounding Budgeting as Cognitive Process
for hands-free voice-activated assistants: Content
in Actual Financial Behaviour
analysis’, JMIR mHealth and uHealth, 6(9), pp. 1–
13. doi: 10.2196/mhealth.9705.
Budgeting apps support the tracking of expenses
and  monitoring  them  against  available  funds  or  Connell, D. (2017) Fudget: Budget and expense
allocated budget. Such functions however prioritize
|     |     |     |     |     |     |     | tracking  | app,  | Google  | Play.  |     | Available  | at:  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------- | ------ | --- | ---------- | ---- |
cognitive  operations  rather  than  the  financial  https://play.google.com/store/apps/details?id=co
behaviours themselves. This is reflected in the small  m.dannyconnell.android.fudget%0A (Accessed: 1
| number  | of  | budgeting  | apps  | integrating  |     | online  |     |     |     |     |     |     |     |
| ------- | --- | ---------- | ----- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
April 2022).
banking to support for instance automatic import of
|     |     |     |     |     |     |     | DigitLeaf,  | llc  | (2016)  | Budget  | planner—Expense  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------- | ------- | ---------------- | --- | --- |
the real transactions. This indicates limited support
|                   |     |        |     |          |        |          | tracker,  | Google  |     | Play.  | Available  |     | at:  |
| ----------------- | --- | ------ | --- | -------- | ------ | -------- | --------- | ------- | --- | ------ | ---------- | --- | ---- |
| for  encouraging  |     | users  | to  | compare  | their  | entered  |           |         |     |        |            |     |      |
transactions with those in bank statements. Such  https://play.google.com/store/apps/details?id=co
m.colpit.diamondcoming.isavemoney (Accessed:
grounding in actual financial behaviours is crucial for
1 April 2022).
infusing practical value and realism to the otherwise
cognitive exercise of budgeting. We suggest the use
DigitLeaf, L. (2017) Family budget-spending tracker,
of clear terminology differentiating banking accounts  Google  Play.  Available  at:
and  transactions  from  those  created  in  the  https://play.google.com/store/apps/details?id=co
budgeting app.
m.colpit.diamondcoming.isavemoneygo%0A
(Accessed: 1 April 2022).
6.  CONCLUSION  Estimate, B.-B. (2019) Expense Tracker & Budget
|     |     |     |     |     |     |     | App,  | Google  |     | Play.  | Available  |     | at:  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --- | ------ | ---------- | --- | ---- |
We report on functionality review of 45 top-rated  https://play.google.com/store/apps/details?id=ex
budgeting apps. Findings suggest the value of more  pense.tracker.income.receipt.budget  (Accessed:
nuanced vocabulary for describing the key concepts
1 April 2022).
of accounts, transactions and budgets as informed
Gunaratne, J. and Nov, O. (2015) ‘Informing and
by mental accounting theory and for differentiating
improving retirement saving performance using
between tracking the transactions and monitoring
the allocated budgets through money envelopes.  behavioral  economics  theory-driven  user
|               |     |       |       |         |               |      | interfaces’,  | Conference  |     | on  | Human  | Factors  | in  |
| ------------- | --- | ----- | ----- | ------- | ------------- | ---- | ------------- | ----------- | --- | --- | ------ | -------- | --- |
| We  conclude  |     | with  | four  | design  | implications  | for  |               |             |     |     |        |          |     |
Computing Systems - Proceedings, 2015-April,
| financial  | technologies  |     | such  | as  | budgeting  | apps  |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | ----- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
including  clear  definitions  of  accounts  and  pp. 917–920. doi: 10.1145/2702123.2702408.
transaction  and  their  different  types,  supporting  HG  Group  Inc.  (2020)  Budget  App  -  Expense
| budgeting  | through    |     | money  | envelopes  |          | and  for  |           |         |     |        |            |     |      |
| ---------- | ---------- | --- | ------ | ---------- | -------- | --------- | --------- | ------- | --- | ------ | ---------- | --- | ---- |
|            |            |     |        |            |          |           | Tracker,  | Google  |     | Play.  | Available  |     | at:  |
| grounding  | budgeting  |     | as     | cognitive  | process  | in        |           |         |     |        |            |     |      |
https://play.google.com/store/apps/details?id=co
financial behaviour.  m.hg.moneymanager.budgetapp  (Accessed:  1
April 2022).
 ACKNOWLEDGMENTS   Kaye, J. J. et al.  (2014) ‘Money talks: Tracking
|                  |     |       |      |            |     |         | personal  | finances’,  |     | Conference  |     | on  Human  |     |
| ---------------- | --- | ----- | ---- | ---------- | --- | ------- | --------- | ----------- | --- | ----------- | --- | ---------- | --- |
| First  author’s  |     | work  | was  | supported  | by  | Taibah  |           |             |     |             |     |            |     |
Factors in Computing Systems - Proceedings, pp.
| University,  | Saudi  |     | Arabia  | and  the  | Saudi  | Arabian  |     |     |     |     |     |     |     |
| ------------ | ------ | --- | ------- | --------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
521–530. doi: 10.1145/2556288.2556975.
Cultural Bureau, London.
7

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
Labs, V. (2019) Expense Tracker - Money Manager in the home’, Conference on Human Factors in
& Budget, Google Play. Available at: Computing Systems - Proceedings, 18, pp. 2271–
https://play.google.com/store/apps/details?id=co 2276. doi: 10.1145/2702613.2732808.
m.vlab.expense.tracker (Accessed: 1 April 2022).
Snow, S. and Vyas, D. (2015b) ‘Fostering
Lee, M. K., Kiesler, S. and Forlizzi, J. (2011) ‘Mining collaboration in the management of family
behavioral economics to design persuasive finances’, OzCHI 2015: Being Human -
technology for healthy choices’, Conference on Conference Proceedings, pp. 380–387. doi:
Human Factors in Computing Systems - 10.1145/2838739.2838746.
Proceedings, pp. 325–334. doi:
Softs, E. (no date) Home Budget - Money Manager,
10.1145/1978942.1978989.
Google Play. Available at:
Letondor, B. (2015) EasyBudget - Personal budget https://play.google.com/store/apps/details?id=co
planning made simple, Google Play. Available at: m.easysoftsalahi.app.appFree%0A (Accessed: 1
https://play.google.com/store/apps/details?id=co April 2022).
m.benoitletondor.easybudgetapp (Accessed: 1
Stockinger, T. et al. (2013) ‘SmartPiggy: A piggy
April 2022).
bank that talks to your smartphone’, Proceedings
Lewis, M. and Perry, M. (2019) ‘Follow the money: of the 12th International Conference on Mobile
Managing personal finance digitally’, Conference and Ubiquitous Multimedia, MUM 2013, 43, pp.
on Human Factors in Computing Systems - 5–6. doi: 10.1145/2541831.2541869.
Proceedings, pp. 1–14. doi:
Tanu, F. (2011) SimpleBudget (Envelope Budget),
10.1145/3290605.3300620.
Google Play. Available at:
LLC, Ib. (2017) Money pro, Google Play. Available https://play.google.com/store/apps/details?id=co
at: https://play.google.com/store/apps/details?id= m.simplebudget%0A (Accessed: 1 April 2022).
com.ibearsoft.moneyproandroid%0A (Accessed:
Thaler, R. H. (1999) ‘Mental accounting matters’,
1 April 2022).
Journal of Behavioral Decision Ma,
Lolla, S. and Sas, C. (2023) ‘Evaluating Mobile Apps 206(September 1998), pp. 241–268. doi:
Targeting Personal Goals’, Conference on 10.1017/CBO9780511803475.015.
Human Factors in Computing Systems -
Vines, J., Dunphy, P. and Monk, A. (2014) ‘Pay or
Proceedings. doi: 10.1145/3544549.3585725
delay: The role of technology when managing a
North, H. (2011) MoneyWise, Google Play. low income’, Conference on Human Factors in
Available at: https://play.google.com/store/apps/ Computing Systems - Proceedings, pp. 501–510.
details?id=com.handynorth.moneywise_free% doi: 10.1145/2556288.2556961.
0A (Accessed: 1 April 2022).
VoPo (2015) Easy Home Finance, Google Play.
Park, J., Lee, H. and Park, S. (2021) ‘Goldentime: Available at: https://play.google.com/store/apps/
Exploring system-driven timeboxing and micro- details?id=vopo.easyhomefinance (Accessed: 1
financial incentives for self-regulated phone use’, April 2022).
Conf. on Human Factors in Computing Systems -
Vyas, D. et al. (2015) ‘Being thrifty on a $100K wage:
Proceedings. doi: 10.1145/3411764.3445489.
Austerity in family finances’, Proceedings of the
Partners, D. (no date) Goodbudget: Budget & ACM Conference on Computer Supported
Finance, Google Play. Available at: Cooperative Work, CSCW, 2015-Janua, pp. 167–
https://play.google.com/store/apps/details?id=co 170. doi: 10.1145/2685553.2698998.
m.dayspringtech.envelopes%0A (Accessed: 1
Vyas, D. et al. (2016) ‘Social organization of
April 2022).
household finance: Understanding artful financial
Qu, C. et al. (2020) ‘Functionality of top-rated mobile systems in the home’, in Proceedings of the ACM
apps for depression: Systematic search and Conference on Computer Supported Cooperative
evaluation’, JMIR Mental Health, 7(1), pp. 1–13. Work, CSCW. Association for Computing
doi: 10.2196/15321. Machinery, pp. 1777–1789. doi:
10.1145/2818048.2819937.
QYResearch (no date) Global Personal Financial
Management Tools Market Size, Status and Yjteam (2017) DAILY POCKET - Budget Manager,
Forecast 2019-2025. Available at: Google Play. Available at:
https://www.marketresearch.com/QYResearch- https://play.google.com/store/apps/details?id=kr.
Group-v3531/Global-Personal-Financial- co.yjteam.dailypay (Accessed: 1 April 2022).
Management-Tools-12732938/ (Accessed: 26
Zaidan, S. and Roehrer, E. (2016) ‘Popular mobile
December 2022).
phone apps for diet and weight loss: A content
Snow, S. and Vyas, D. (2015a) ‘Fixing the analysis’, JMIR mHealth and uHealth, 4(3). doi:
alignment: An exploration of budgeting practices 10.2196/mhealth.5406.
8

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas

Appendix A
|     | Tracking transaction: funds  |     |     | Tracking transaction: expenses  |     |     |
| --- | ---------------------------- | --- | --- | ------------------------------- | --- | --- |
1  2
| App name  |     | 3       4  |    5  6  | 7   | 8  9  | 10  11  |
| --------- | --- | ---------- | -------- | --- | ----- | ------- |
Create  Create  Enter  Set  Set   Create   Create  Enter  Set  Set

Funds  funds  funds   funds   funds  Expense   expense   expense   date for   time for
  category  currency  date   time     category  currency  expense  expense
| 1 Money  (PixelRush, 2017)  | √   | √  √  | √     | √   | √  √  | √     |
| --------------------------- | --- | ----- | ----- | --- | ----- | ----- |
|                             |     |       | √  √  | √   |   √   | √  √  |
Alzex Finance (Anna Shirokova,
| 2015)  | √   |   √  | √  √  | √   | √  √  | √  √  |
| ------ | --- | ---- | ----- | --- | ----- | ----- |
AndroMoney (AndroMoney,
|     | √   | √  √  | √    | √   | √  √  | √    |
| --- | --- | ----- | ---- | --- | ----- | ---- |
2011)
Bills Reminder (TimelyBills,
| 2015)  | √   | √  √  | √  √  | √   | √  √  | √  √  |
| ------ | --- | ----- | ----- | --- | ----- | ----- |
Bluecoins Finance (Mabuhay
|     | √   | √  √  | √  √  | √   | √    | √  √  |
| --- | --- | ----- | ----- | --- | ---- | ----- |
Software, 2016)
Budget App (HG Group Inc.,
| 2020)                             | √   | √     | √  √  | √   |   √   | √  √  |
| --------------------------------- | --- | ----- | ----- | --- | ----- | ----- |
| Budget planner (DigitLeaf, 2016)  | √   | √  √  |       | √   | √  √  | √     |
| CoinKeeper (LLC, 2015)            | √   |   √   | √  √  | √   | √  √  | √  √  |
| DAILY POCKET (Yjteam, 2017)       | √   | √  √  | √     | √   | √  √  | √     |
| Easy Home (VoPo, 2015)            | √   | √  √  | √     | √   |   √   | √     |
| EasyBudget (Letondor, 2015)       | √   |   √   | √  √  | √   | √     | √  √  |
Expense Manager (Bishinews,
|     | √   | √    | √    | √   | √  √  | √    |
| --- | --- | ---- | ---- | --- | ----- | ---- |
2010)
Expense Manager (Manager,
| 2012)                         | √   | √  √  | √  √  | √   | √  √  | √  √  |
| ----------------------------- | --- | ----- | ----- | --- | ----- | ----- |
| Expense Tracker (Labs, 2019)  | √   | √  √  | √     | √   | √  √  | √     |
Expense Tracker (Estimate,
|     | √   | √  √  | √    | √   | √  √  | √    |
| --- | --- | ----- | ---- | --- | ----- | ---- |
2019)
| Expense Tracker (Tracker, 2016)  | √   |   √   | √  √  | √   |   √   | √  √  |
| -------------------------------- | --- | ----- | ----- | --- | ----- | ----- |
| Family budget (DigitLeaf, 2017)  | √   | √  √  | √     | √   | √  √  | √     |
| Fast Budget (SRL, 2014)          | √   | √  √  | √     | √   |   √   | √     |
| Fudget (Connell, 2017)           | √   |   √   | √  √  | √   | √  √  | √  √  |
| GnuCash (GnuCash, 2012)          | √   | √  √  | √     | √   |       | √     |
Goodbudget (Partners, no date)
|     | √   |     | √    | √   | √    | √    |
| --- | --- | --- | ---- | --- | ---- | ---- |
Home Budget (Softs, no date)
|     | √   | √    | √    | √   | √  √  | √    |
| --- | --- | ---- | ---- | --- | ----- | ---- |
Home Budget (SIRI, 2013)  √  √        √  √  √  √  √  √  √  √
Home Finance (SoftMobile,  √  √        √  √  √  √  √    √  √
2015)
Income Expense (SARAF,
| 2019)  | √   | √    | √    | √   | √  √  | √    |
| ------ | --- | ---- | ---- | --- | ----- | ---- |
Mobills (M. Inc., 2013)
|     | √   | √        √  | √    | √   | √  √  | √    |
| --- | --- | ----------- | ---- | --- | ----- | ---- |
Monefy (Reflectly, 2014)
|     | √   | √        √  | √  √  | √   | √  √  | √  √  |
| --- | --- | ----------- | ----- | --- | ----- | ----- |
Money Manager (R. Inc., 2013)  √  √        √  √    √  √  √  √
Money manager (Exp, 2020)   √  √        √  √  √  √  √  √  √  √
Money Manager (Apps, 2014)  √  √        √  √  √  √  √  √  √  √
| Money pro (LLC, 2017)  | √   | √        √  | √    | √   | √  √  | √    |
| ---------------------- | --- | ----------- | ---- | --- | ----- | ---- |
Money Tracker (Notes, 2021)   √  √        √  √    √  √  √  √
| Money+ (Studios, 2020)   | √   | √        √  | √    | √   | √  √  | √    |
| ------------------------ | --- | ----------- | ---- | --- | ----- | ---- |
| MoneyWise (North, 2011)  | √   | √        √  | √    | √   | √  √  | √    |
Monny (Greamer, 2017)
|     | √   | √        √  | √  √  | √   | √  √  | √  √  |
| --- | --- | ----------- | ----- | --- | ----- | ----- |
Monthly Expenses (Baruah,
|     | √   | √        √  | √  √  | √   | √  √  | √  √  |
| --- | --- | ----------- | ----- | --- | ----- | ----- |
2016)
My Expenses  (Totschnig,
| 2012)  | √   | √        √  | √    | √   | √  √  | √    |
| ------ | --- | ----------- | ---- | --- | ----- | ---- |
My Finances (7csolutions,
|     | √   | √        √  |     | √   |   √  | √    |
| --- | --- | ----------- | --- | --- | ---- | ---- |
2015)
SimpleBudget (Tanu, 2011)
|     |     |     | √    | √   | √  √  | √    |
| --- | --- | --- | ---- | --- | ----- | ---- |
Spendee Budget (A.s., 2013)  √  √         √  √    √  √  √  √
Spending Tracker (Ltd, 2014)  √  √         √  √    √  √  √  √
Toshl Finance (Inc., no date)  √  √         √  √    √  √  √  √
| Vault (Tubin, 2013)  | √   | √         √  | √  √  | √   | √  √  | √  √  |
| -------------------- | --- | ------------ | ----- | --- | ----- | ----- |
Wallet (BudgetBakers, 2011)  √  √         √  √    √  √  √  √
YNAB (YouNeedABudget,
|     | √   | √         √  | √    | √   | √  √  | √    |
| --- | --- | ------------ | ---- | --- | ----- | ---- |
2015)
Table 1: The main functionalities and subfunctionalities of funds and expenses for the 45 top-rated budgeting
apps.

9

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
|     |     |     | Tracking transaction accounts  |     |     |     |     | Monitoring budgets  |     |
| --- | --- | --- | ------------------------------ | --- | --- | --- | --- | ------------------- | --- |
1
|     | 2   | 3   | 4  5     | 6   | 7   | 8   | 9   | 10  11  | 12  13  |
| --- | --- | --- | -------- | --- | --- | --- | --- | ------- | ------- |
App name
Transaction  Saving  Link  Transfer  Set  Set  Transac- Link app  Create  Create  Enter  Set

account  account  transaction between  date for  time for   tion  to bank  single multiple budget  budget
    to account accounts  transfer  transfer attachment  account  budget budgets  name  period
1 Money  (PixelRush, 2017)  √  √  √            √    √          √  √  √
| Alzex Finance (Anna Shirokova,  |     |     |        |     |     |     |     |      |       |
| ------------------------------- | --- | --- | ------ | --- | --- | --- | --- | ---- | ----- |
| 2015)                           | √   |     | √  √   | √   | √   |     |     |   √  | √  √  |
| AndroMoney (AndroMoney,         |     |     |        |     |     |     |     |      |       |
|                                 | √   |     | √   √  | √   | √   |     |     |   √  |   √   |
2011)
| Bills Reminder (TimelyBills,  |     |         √  |           |              |     |        |     |      |      |
| ----------------------------- | --- | ---------- | --------- | ------------ | --- | ------ | --- | ---- | ---- |
| 2015)                         | √   |            | √      √  | √            |     |        |     |   √  |   √  |
| Bluecoins Finance (Mabuhay    |     | √          |           |              |     |     √  |     |      |      |
|                               | √   |            | √  √      |          √   | √   |        |     |   √  |   √  |
Software, 2016)
| Budget App (HG Group Inc.,        |     |     |            |     |     |     |     |      |       |
| --------------------------------- | --- | --- | ---------- | --- | --- | --- | --- | ---- | ----- |
| 2020)                             |     |     |            |     |     |     |     |      |   √   |
| Budget planner (DigitLeaf, 2016)  |     | √   |            |     |     |     |     |      |       |
|                                   | √   |     | √   √      | √   | √   |     |     |   √  | √  √  |
| CoinKeeper (LLC, 2015)            |     |     |            |     |     |     |     |      |       |
|                                   | √   |     | √      √   | √   |     |     |     |   √  | √  √  |
| DAILY POCKET (Yjteam, 2017)       |     |     |            |     |     |     |     |      |       |
|                                   |     |     |            |     |     |     |     |      |   √   |
| Easy Home (VoPo, 2015)            | √   |     | √       √  |     |     |     |     |      |       |
| EasyBudget (Letondor, 2015)       |     |     |            |     |     |     |     | √    |       |
| Expense Manager (Bishinews,       |     | √   |            |     |     |     |     |      |       |
|                                   | √   |     | √  √       | √   |     |     |     |   √  |   √   |
2010)
| Expense Manager (Manager,     |     |     |       |     |     |     |     |      |      |
| ----------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ---- |
| 2012)                         | √   |     | √  √  |     |     |     |     |      |      |
| Expense Tracker (Labs, 2019)  |     |     |       |     |     |     |     |      |      |
|                               |     |     |       |     |     |     |     |      |      |
| Expense Tracker (Estimate,    |     |     |       |     |     |     |     |      |      |
|                               | √   |     | √  √  | √   |     |     | *   |   √  |   √  |
2019)
Expense Tracker (Tracker, 2016)  √    √  √           √            √      √    √
| Family budget (DigitLeaf, 2017)  |     |     |       |     |     |     |     |      |       |
| -------------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ----- |
|                                  | √   |     | √  √  |     |     |     |     |   √  | √  √  |
|                                  |     |     |       |     |     | *   |     |      |       |
Fast Budget (SRL, 2014)  √  √  √               √    *    √    √
| Fudget (Connell, 2017)       | √   |     | √    |     |     |     |     |      |     |
| ---------------------------- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- |
| GnuCash (GnuCash, 2012)      | √   |     | √    |     |     |     |     | √    |     |
Goodbudget (Partners, no date)  √  √  √  √  √          √  √  √
| Home Budget (Softs, no date)  | √   |     | √     |     |     |     |     | √    |      |
| ----------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ---- |
|                               |     |     |       |     |     |     |     |      |      |
| Home Budget (SIRI, 2013)      | √   |     | √  √  | √   |     |     |     |   √  |   √  |
| Home Finance (SoftMobile,     |     |     |       |     |     |     |     |      |      |
| 2015)                         | √   |     | √  √  | √   | √   |     |     |   *  |      |
| Income Expense (SARAF,        | √   |     |       | √   |     |     |     |      |      |
|                               |     |     | √  √  |     |     |     |     |   √  |   √  |
2019)
|                                |     | √   |       |     |     |     |     |      |       |
| ------------------------------ | --- | --- | ----- | --- | --- | --- | --- | ---- | ----- |
| Mobills (M. Inc., 2013)        | √   |     | √  √  | √   |     |     |     |   √  |   √   |
| Monefy (Reflectly, 2014)       | √   |     | √  √  | √   |     |     |     | √    |   √   |
|                                |     | √   |       |     |     | √   |     |      |       |
| Money Manager (R. Inc., 2013)  | √   |     | √  √  | √   | √   |     |     |   √  |   √   |
| Money manager (Exp, 2020)      | √   |     | √  √  | √   |     |     |     | √    |       |
| Money Manager (Apps, 2014)     | √   |     | √  √  | √   | √   |     |     |   √  | √  √  |
|                                |     | *   |       |     |     |     |     |      |       |
| Money pro (LLC, 2017)          | √   |     | √  √  | √   | √   |     | *   |   *  |       |
Money Tracker (Notes, 2021)   √    √  √  √    √      √  √  √
| Money+ (Studios, 2020)     |     |     |       |     |     | *   |     |      |       |
| -------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ----- |
|                            | √   |     | √  √  | √   |     |     |     |   √  |   √   |
| MoneyWise (North, 2011)    | √   |     | √  *  |     |     |     |     |   √  | √  √  |
| Monny (Greamer, 2017)      | √   |     | √     |     |     |     |     | √    |   √   |
| Monthly Expenses (Baruah,  |     | √   |       |     |     |     |     |      |       |
|                            | √   |     | √  √  | √   | √   |     |     |   *  |       |
2016)
| My Expenses  (Totschnig,   |     |     |       |     |     | *   |     |      |      |
| -------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ---- |
| 2012)                      | √   |     | √  √  | √   | √   |     |     |   *  | √    |
| My Finances (7csolutions,  |     |     |       |     |     |     |     |      |      |
|                            | √   |     | √  √  | √   |     |     |     |      |      |
2015)
|                               |     |     |       |     |     |     |     |      |       |
| ----------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ----- |
| SimpleBudget (Tanu, 2011)     | √   |     | √  √  |     |     |     |     |   √  | √  √  |
| Spendee Budget (A.s., 2013)   | √   |     | √  √  | √   |     |     | *   |   √  | √  √  |
| Spending Tracker (Ltd, 2014)  |     |     |       |     |     |     |     |      |       |
|                               | √   |     | √  √  | √   |     |     |     |      |   √   |
Toshl Finance (Inc., no date)  √         √  √  √      *    √  √  √
| Vault (Tubin, 2013)          | √   |     |       |     |     |     |     | √    |       |
| ---------------------------- | --- | --- | ----- | --- | --- | --- | --- | ---- | ----- |
|                              |     | √   |       |     |     | √   |     |      |       |
| Wallet (BudgetBakers, 2011)  | √   |     | √  √  | √   | √   |     | *   |   √  | √  √  |
| YNAB (YouNeedABudget,        |     | √   |       |     |     |     |     |      |       |
| 2015)                        | √   |     | √  √  |     |     |     | *   |   √  | √  √  |
Table 2: The main functionalities and subfunctionalities of transaction accounts, transfer between them, and the
types of provided budgets of the 45 top-rated budgeting apps (* refers to the premium feature in the apps).
10

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
com.gerenciadorfinanceiro.controller%0A
| REFERENCES FOR APPENDIX A  |     |     |     |     |     |     | (Accessed: 1 April 2022).  |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
7csolutions  (2015)  My  Finances,  Google  Play.  Inc., R. (2013) Money Manager Expense & Budget,
| Available  |     |     |     |     |     | at:  | Google  | Play.  |     | Available  |     | at:  |
| ---------- | --- | --- | --- | --- | --- | ---- | ------- | ------ | --- | ---------- | --- | ---- |
https://play.google.com/store/apps/details?id=co
https://play.google.com/store/apps/details?id=co
m.sevencsolutions.myfinances%0A (Accessed: 1  m.realbyteapps.moneymanagerfree%0A
| April 2022).  |     |     |     |     |     |     | (Accessed: 1 April 2022).  |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
Inc., T. (no date) Toshl Finance - Personal Budget &
AndroMoney (2011) AndroMoney (Expense Track),
Google  Play.  Available  at:  Expense  Tracker,  Google  Play.  Available  at:
https://play.google.com/store/apps/details?id=co https://play.google.com/store/apps/details?id=co
m.thirdframestudios.android.expensoor%0A
m.kpmoney.android (Accessed: 1 April 2022).
(Accessed: 1 April 2022).
Anna Shirokova (2015) Alzex Finance, Google Play.
|            |     |     |     |     |     |      | LLC,  D.  (2015)  |     | CoinKeeper:  |     | expense,  | money  |
| ---------- | --- | --- | --- | --- | --- | ---- | ----------------- | --- | ------------ | --- | --------- | ------ |
| Available  |     |     |     |     |     | at:  |                   |     |              |     |           |        |
manager, budget planner, Google Play. Available
https://play.google.com/store/apps/details?id=co
| m.alzex.finance (Accessed: 1 April 2022).  |     |     |     |     |     |     | at:  |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
https://play.google.com/store/apps/details?id=co
Apps, A. P. (2014) Money Manager: AZV Money  m.disrapp.coinkeeper.material (Accessed: 1 April
| Pro,  | Google  | Play.  |     | Available  |     | at:  |     |     |     |     |     |     |
| ----- | ------- | ------ | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- |
2022).
https://play.google.com/store/apps/details?id=co
Ltd, M. R. (2014) Spending Tracker, Google Play.
m.azv.money%0A (Accessed: 1 April 2022).
|          |             |          |            |     |         |     | Available  |     |     |     |     | at:  |
| -------- | ----------- | -------- | ---------- | --- | ------- | --- | ---------- | --- | --- | --- | --- | ---- |
| Baruah,  | B.  (2016)  | Monthly  | Expenses:  |     | Manage  |     |            |     |     |     |     |      |
https://play.google.com/store/apps/details?id=co
| Money,                                           | Google  | Play.  |     | Available  |     | at:  |                               |     |     |     |             |     |
| ------------------------------------------------ | ------- | ------ | --- | ---------- | --- | ---- | ----------------------------- | --- | --- | --- | ----------- | --- |
|                                                  |         |        |     |            |     |      | m.mhriley.spendingtracker%0A  |     |     |     | (Accessed:  | 1   |
| https://play.google.com/store/apps/details?id=co |         |        |     |            |     |      | April 2022).                  |     |     |     |             |     |
m.kaushikbaruah.quickexpensemanagerfree%0
A (Accessed: 1 April 2022).  Mabuhay  Software  (2016)  Bluecoins  Finance:
|     |     |     |     |     |     |     | Budget,  Mon,  |     | Google  | Play.  | Available  | at:  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ------ | ---------- | ---- |
Bishinews (2010) Expense Manager, Google Play.  https://play.google.com/store/apps/details?id=co
| Available  |     |     |     |     |     | at:  |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
m.rammigsoftware.bluecoins (Accessed: 1 April
https://play.google.com/store/apps/details?id=co
2022).
m.expensemanager (Accessed: 1 April 2022).
Manager, H. E. (2012) Expense Manager, Google
| BudgetBakers  |         | (2011)  Wallet:  |     | Budget     | Planner  |      |        |     |            |     |     |      |
| ------------- | ------- | ---------------- | --- | ---------- | -------- | ---- | ------ | --- | ---------- | --- | --- | ---- |
|               |         |                  |     |            |          |      | Play.  |     | Available  |     |     | at:  |
| Tracker,      | Google  | Play.            |     | Available  |          | at:  |        |     |            |     |     |      |
https://play.google.com/store/apps/details?id=me
https://play.google.com/store/apps/details?id=co diavision.handwallet (Accessed: 1 April 2022).
m.droid4you.application.wallet%0A (Accessed: 1
| April 2022).  |     |     |     |     |     |     | Notes, Q. S. & Q. C. G. & R. & (2021)  |     |     |     |     | Money  |
| ------------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ------ |
Tracker: Expense Tracker, Wallet, Budget App,
DigitLeaf,  llc  (2016)  Budget  planner—Expense  Google  Play.  Available  at:
| tracker,  | Google  | Play.  |     | Available  |     | at:  |     |     |     |     |     |     |
| --------- | ------- | ------ | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- |
https://play.google.com/store/apps/details?id=mo
https://play.google.com/store/apps/details?id=co neytracker.expensetracker.budgetplanner.spendi
m.colpit.diamondcoming.isavemoney (Accessed:  ngtracker%0A (Accessed: 1 April 2022).
1 April 2022).
PixelRush (2017) 1Money: expense tracker budget,
Exp, I. M. (2020) Money manager, expense tracker,  Google  Play.  Available  at:
| budget,  | wallet,  | Google  | Play.  | Available  |     | at:  |     |     |     |     |     |     |
| -------- | -------- | ------- | ------ | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- |
https://play.google.com/store/apps/details?id=or
https://play.google.com/store/apps/details?id=ru.i
g.pixelrush.moneyiq (Accessed: 1 April 2022).
nnim.my_finance%0A (Accessed: 1 April 2022).
|     |     |     |     |     |     |     | Reflectly  (2014)  | Monefy  | -   | Budget  | Manager  | and  |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ------- | --- | ------- | -------- | ---- |
GnuCash (2012) GnuCash, Google Play. Available
Expense Tracker app, Google Play. Available at:
at:https://play.google.com/store/apps/details?id=
https://play.google.com/store/apps/details?id=co
org.gnucash.android%0A  (Accessed:  1  April  m.monefy.app.lite%0A (Accessed: 1 April 2022).
2022).
SARAF, A. (2019) Income Expense- daily expenses,
Greamer (2017) Monny, Google Play. Available at:
|     |     |     |     |     |     |     | Google  | Play.  |     | Available  |     | at:  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --- | ---------- | --- | ---- |
https://play.google.com/store/apps/details?id=co https://play.google.com/store/apps/details?id=inc
| m.greamer.monny.android%0A  |     |     |     | (Accessed:  |     | 1   |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
omeexpense.incomeexpense&hl=en_GB&gl=US
April 2022).
%0A (Accessed: 1 April 2022).
Inc., M. (2013)  Mobills: Budget Planner, Google  SIRI (2013) Home Budget Manager Lite With Sync,
| Play.  |     | Available  |     |     |     | at:  |         |        |     |            |     |      |
| ------ | --- | ---------- | --- | --- | --- | ---- | ------- | ------ | --- | ---------- | --- | ---- |
|        |     |            |     |     |     |      | Google  | Play.  |     | Available  |     | at:  |
https://play.google.com/store/apps/details?id=br.
https://play.google.com/store/apps/details?id=co
m.siri.budgetdemo%0A (Accessed: 1 April 2022).
11

Evaluating Budgeting Apps: Limited Support for Budgeting Compared to Tracking
Alenazi • Sas
SoftMobile (2015) Home Finance, Google Play. Totschnig, M. (2012) My Expenses, Google Play.
Available at: Available at:
https://play.google.com/store/apps/details?id=co https://play.google.com/store/apps/details?id=or
m.mec.homefinance (Accessed: 1 April 2022). g.totschnig.myexpenses%0A (Accessed: 1 April
2022).
SRL, A. (2014) Fast Budget - Expense Manager,
Google Play. Available at: Tracker, F.-E. (2016) Expense Tracker, Family
https://play.google.com/store/apps/details?id=co Budget, Google Play. Available at:
m.blodhgard.easybudget%0A (Accessed: 1 April https://play.google.com/store/apps/details?id=co
2022). m.finart%0A (Accessed: 1 April 2022).
Studios, Z. (2020) Money+ Cute Expense Tracker, Tubin, S. (2013) Vault - Budget Planner, Google
Google Play. Available at: Play. Available at:
https://play.google.com/store/apps/details?id=co https://play.google.com/store/apps/details?id=ru.
m.zotiger.accountbook%0A (Accessed: 1 April tubin.bp%0A (Accessed: 1 April 2022).
2022).
YouNeedABudget (2015) YNAB (You Need A
TimelyBills (2015) Bills Reminder, Budget Planner, Budget), Google Play. Available at:
Google Play. Available at: https://play.google.com/store/apps/details?id=co
https://play.google.com/store/apps/details?id=in. m.youneedabudget.evergreen.app%0A
usefulapp.timelybills (Accessed: 1 April 2022). (Accessed: 1 April 2022).
12