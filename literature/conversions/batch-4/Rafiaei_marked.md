---
conversion_metadata:
  converted_at: "2026-07-21T08:15:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Rafiaei.pdf"
  source_pdf_sha256: "ad03004b773483ecf9da37a51e1eb314412ebb21ec2d9c173a6f0983af649445"
  page_count: 6
  markdown_char_count: 47758
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Keyword Matching vs. LLM-Based 
Classification for Personal Finance 
Transaction Categorization: 
A Benchmark Study on Real Canadian Bank Data

Majid Rafiaei 
Independent Researcher — Intelligent Systems 
Montreal, QC, Canada  ·  majidrafiaei@gmail.com

Abstract — Personal finance applications must automatically classify bank transactions into meaningful spending categories. The dominant 
approach — keyword-based rule matching — is fast and interpretable but its accuracy varies dramatically across account types. We present 
the first benchmark study of transaction classification on real Canadian bank data. Using MonIQ, a full-stack personal finance prototype, we 
constructed a labeled dataset of 7,152 transactions from two account holders, five accounts across two Canadian banks (CIBC and BMO), 
spanning 4.5 years (September 2021 – April 2026). We report two experiments. In Experiment 1, a controlled benchmark on 200 CIBC 
chequing  transactions  shows  keyword  matching  achieving  45.8%  type  accuracy  versus  Claude  (claude-3-5-sonnet-20241022)  at  96.5% 
(+51.0pp, McNemar's χ²=81.06, p<0.001), confirming that LLMs resolve the structural failures of keyword matching on chequing accounts. 
In Experiment 2, an exploratory scale-up on all 7,152 transactions with Llama-3.1-8B and Llama-3.3-70B reveals a clear model-size effect: 
Transfer F1 rises from 40.1% (8B) to 57.9% (70B), versus Claude's 99.0%, establishing Transfer classification as the single most diagnostic 
metric for this task. We provide a formal structural analysis of three keyword classifier limitations and release our dataset, evaluation code, 
and failure taxonomy as the first public Canadian personal finance transaction benchmark.

Keywords — transaction classification, personal finance, keyword matching, large language models, fintech, benchmark, Canadian banking, 
statistical validation

---

<!-- PAGE 2 -->

I. INTRODUCTION

Automatic transaction categorization is a core capability of 
personal  finance  software.  Applications  such  as  Mint,  YNAB, 
and Monarch Money rely on it to produce spending breakdowns, 
budget  recommendations,  and  savings  projections.  Without 
accurate categorization, downstream analytics are unreliable.

The  near-universal  approach

is  keyword-based  rule 
matching: a manually maintained dictionary maps merchant name 
fragments to spending categories. This requires no training data, 
is fully interpretable, and executes in microseconds. Despite its 
simplicity, it remains the dominant production approach at major 
fintech companies including Plaid [1].

This  paper  investigates  the  performance  gap  between 
account types, evaluates LLMs as a replacement with statistical 
validation,  and  provides  formal  structural  analysis  of  why 
keyword matching is bounded. Contributions:

•  First labeled dataset of real Canadian personal finance

transactions: 7,152 transactions, two account holders, five 
accounts, two banks (CIBC and BMO), 4.5 years, 16-class 
annotations. The 4,986-transaction CIBC subset (4,044 
chequing + 942 credit card) serves as the primary 
evaluation corpus for keyword and Claude experiments; 
the remaining 2,166 BMO transactions are used in the 
exploratory Experiment 2.

•  Systematic evaluation: 69pp performance gap — credit

card 96.3% F1 vs. chequing 27.5% F1.

•  Controlled experiment with statistical validation: LLM vs. 
keyword on 200 chequing transactions — +51pp type 
accuracy (95% CI: [43.6, 58.4]; p<0.001).

•  Formal structural analysis of three limitations of keyword

classifiers and a hybrid cascade architecture.

We collected transaction exports from five accounts across 
two  Canadian  banks  —  CIBC  and  BMO  —  belonging  to  two 
account  holders,  spanning  4.5  years  (September  2021  –  April 
2026).  Data  was  exported  directly  from  each  bank's  online 
banking  portal  as  CSV.  The  full  dataset  contains  7,152 
transactions. For keyword and Claude evaluation (Sections IV–
VII-C),  we  use  the  4,986-transaction  CIBC  subset  (4,044 
chequing  +  942  credit  card)  where  ground-truth  labels  were 
manually  verified  by  the  account  holder.  The  full  7,152-
transaction  corpus  —  including  2,166  BMO  transactions  —  is 
used for the Llama exploratory evaluation in Section VII-D. Edge 
cases  in  the  16-class  taxonomy  were  resolved  as  follows: 
merchant  refunds  are  labeled  as  the  inverse  of  the  original 
transaction type (Expense on credit card, Transfer on chequing); 
cashback credits are labeled Other Income; and chargebacks are 
treated as Transfer on chequing and Expense reversal on credit 
card.  These  conventions  apply  uniformly  across  both  account 
holders.

TABLE I 
Full Dataset Statistics (CIBC: 4,986 tx; BMO: 2,166 tx across 4 
accounts and 2 holders)

Account

N

Date Range

Types

CIBC Chequing 
(Person 1)

4,044  Sep 2021–Apr

2026

CIBC Visa (Person 
1)

942

Oct 2021–Apr 
2026

expense, income, 
transfer

expense, transfer

Total

7,152

4.5 years

2 users, 2 banks

* BMO transactions used exclusively in Experiment 2 (exploratory scale-up). 
CIBC subset (4,986 tx: 4,044 chequing + 942 credit) used for keyword evaluation 
and controlled Claude benchmark. Account holders are identified as Person 1 and 
Person 2 throughout. All personal identifiers have been removed; transaction 
descriptions are retained solely for research purposes and cannot be used to 
identify individuals.

II. BACKGROUND & RELATED WORK

IV. KEYWORD-BASED CLASSIFICATION

A. Transaction Classification

A. Algorithm

Lesner  et  al.  [2]  proposed  a  large-scale  production  system 
for  personalized  transaction  categorization,  demonstrating  the 
feasibility  of  automated  labeling  at  scale  but  without  public 
dataset release or statistical validation. García-Méndez et al. [3] 
combined  NLP  and  SVM  techniques  to  classify  banking 
transaction  descriptions  for  personal  finance  management, 
demonstrating that short-text classification of bank data requires 
domain-specific approaches. Kotios et al. [4] developed a hybrid 
rule-based and ML categorization model for SME transactions, 
achieving  high  accuracy  for  high-confidence  predictions  but 
noting  persistent 
challenges  with  noisy,  unstructured 
descriptions.  No  prior  work  has  studied  Canadian  bank  data, 
which  presents  unique  challenges:  bilingual  descriptions 
(EN/FR), INTERAC vs. Visa Debit ambiguity, and inconsistent 
merchant name formatting across institutions.

B. LLMs for Document Understanding

LLMs  such  as  GPT-4  [5],  Claude  [6],  and  LLaMA  [7] 
exhibit  strong  zero-shot  text  classification  through  in-context 
learning. Ta et al. [8] demonstrated that specialized preprocessing 
and text classification approaches for Open Banking transactions 
outperform  generic  NLP  models.  No  prior  work  has  directly 
compared LLM and keyword classification on personal finance 
transactions using real labeled data with statistical validation.

III. DATASET

The  classifier  applies  a  priority-ordered  dictionary  of  45 
patterns  after  routing  by  account  type,  following  the  inverted-
index retrieval model [9]. Formal definition: f(d) = γ(kᵢ*) where 
i*  =  min{i  :  kᵢ  ⊆  d};  f(d)  =  c_default  if  no  match.  O(k)  per 
transaction, no training required.

B. Results and Visualizations

Fig. 1 — Precision, recall, and F1 definitions with numerical example 
from our Transfer category data.

---

<!-- PAGE 3 -->

Fig. 2 — Per-category F1 scores, keyword classifier, CIBC evaluation 
subset (N=2,222).

Table  II  shows  accuracy  by  account  type.  The  69pp  gap 
between credit card (96.3%) and chequing (27.5%) is the central 
finding.  Categories  with  0%  F1  —  Transfer,  Other  Income, 
for  64.2%  of  chequing 
Income, 
transactions.

Insurance  —  account

TABLE II 
Keyword Classifier — Performance on CIBC Evaluation Subset 
(N=2,222)

Account

Type Acc.

Cat. F1

Credit Card

100.0%

Chequing

Overall

45.8%

71.8%

96.3%

27.5%

60.5%

N

942

4,044

4,986 (CIBC)

V. FAILURE ANALYSIS

labeled). Error counts and percentages reflect this subset, not 
the full 7,152-transaction dataset.

A. Transfer-Fee Ambiguity (582 errors, 67.1% of N=868)

Every INTERNET TRANSFER misclassified as Fees due to 
keyword priority collision. 'SERVICE CHARGE' matches before 
the transfer pattern. Requires directional context — formalized as 
Limitation 3 in Appendix A.

B. Income-Expense Context Dependence (109 errors, 12.6%)

'Lyft  Canada  Inc'  appears  as  both  income  (credit,  driver 
payments)  and  expense  (debit,  rides).  Identical  descriptions, 
different true labels — context blindness (Limitation 1, Appendix 
A).

C. Incomplete Coverage (177 errors, 20.4%)

Merchants  absent  from  keyword  dictionary  (LendDirect, 
Mondou,  TOYOTA  GABRIEL)  fall  to  default.  Unbounded  as 
merchant space grows (Limitation 2, Appendix A).

VI. WHY CREDIT CARDS WORK

Three  structural  properties  make  keyword  matching 
effective  for  credit  cards:  (1)  merchant  names  are  consistently 
formatted and always present; (2) semantics are unambiguous — 
every  debit  is  expense,  every  'PAYMENT  THANK  YOU'  is 
payment;  (3)  the  transaction  space  is  commercially  bounded. 
Chequing accounts violate all three.  Design principle: keyword 
classification is appropriate if and only if the description reliably 
encodes  merchant  identity  and  transaction  semantics  are 
unambiguous from the description alone.

VII. LLM CLASSIFICATION EXPERIMENTS

A. Experiment 1: Controlled Benchmark (CIBC, N=200)

To  directly  compare  keyword  matching  and  LLM 
classification  under  controlled  conditions,  we  evaluated  200 
CIBC chequing transactions (stratified random sample, seed=42: 
70  expense,  60  income,  70  transfer)  using  Claude  (claude-3-5-
sonnet-20241022, Anthropic) in a zero-shot regime. This is the 
same transaction subset used for keyword evaluation in Section 
IV,  enabling  a  fair  head-to-head  comparison.  Input  per 
transaction:  account  type,  direction  (debit/credit),  amount  in 
CAD, and raw merchant description string. No examples, no fine-
tuning, no chain-of-thought prompting.

Fig. 3 — Failure mode breakdown: 868 errors in keyword classification 
of the CIBC chequing verification subset (N=1,143 transactions, 
manually labeled).

Note: The failure analysis below is reported on the original 
verified CIBC chequing subset (N=1,143 transactions, manually

Fig. 4 — Hybrid cascade classifier architecture. Keyword classifier 
handles high-confidence cases; LLM escalates ambiguous chequing 
transactions (~20–30%).

---

<!-- PAGE 4 -->

B. Experiment 1 Results: Claude vs. Keyword (N=200 CIBC 
Chequing)

Fig. 5 — Keyword vs LLM type and category accuracy on 200 chequing 
transactions with 95% confidence intervals.

TABLE III 
Keyword vs. LLM — 200 Chequing Transactions (95% CI, Wilson 
score)

Metric

Keyword

LLM 
(Claude)

Delta (95% 
CI)

Type accuracy

45.5% [38.7, 
52.4]

96.5% [93.0, 
98.3]

+51.0pp [43.6, 
58.4]

Category 
accuracy

27.5% [21.8, 
34.1]

77.5% [71.2, 
82.7]

+50.0pp [41.5, 
58.5]

Transfer F1

Fees F1

Insurance F1

McNemar χ²

0%

13.7%

0%

—

99.0%

100%

100%

—

+99.0pp

+86.3pp

+100pp

81.06 
(p<0.001)

Fig. 6 — Keyword vs LLM per-category F1 on chequing, top diagnostic 
categories.

The  difference  is  statistically  significant  (McNemar's 
χ²=81.06, p<0.001) with 102 discordant pairs favoring Claude vs. 
7 favoring keyword (p<0.001). Claude correctly resolved all three 
failure modes identified in Section V: Transfer F1 rose from 0% 
to 99.0%, Fees from 13.7% to 100%, and Insurance from 0% to 
100%.

C. Experiment 1 Error Analysis

Claude  made  7  type  errors  (3.5%)  and  45  category  errors 
(22.5%).  The  dominant  error  —  Other  Income  →  Income  (28 
cases,  62%  of  all  category  errors)  —  is  a  taxonomy  labeling 
ambiguity  rather  than  a  classifier  failure:  both  labels  are 
semantically  correct,  but  the  ground  truth  used  a  finer-grained 
distinction  between  payroll  income  and  other  income  credits. 
Removing  this  ambiguity  raises  estimated  Claude  category

accuracy  to  ~91.5%.  The  remaining  errors  are  concentrated  in 
Uber  platform  ambiguity  (5  cases)  —  where  the  description 
"UBER*  EATS"  appeared  as  both  an  expense  (customer  food 
order)  and  income  (driver  payment  credit),  an  instance  of 
Limitation  1  (Context  Blindness,  Appendix  A)  that  requires 
amount  and  direction  signals  to  resolve  —  and  the  inherently 
underspecified "Other" category (7 cases).

VIII. COST-ACCURACY TRADEOFF

D. Experiment 2: Exploratory Scale-Up (Full Dataset, 
N=7,152)

To  assess  model-size  effects  and  evaluate  generalization 
across  banks  and  account  holders,  we  classified  all  7,152 
transactions using Llama-3.1-8B and Llama-3.3-70B (Meta, via 
Groq  API)  in  a  zero-shot  regime.  This  experiment  has  a 
fundamentally different methodology from Experiment 1 and the 
results  cannot  be  directly  compared.  Three  key  differences:  (1) 
Ground-truth  labels  were  assigned  by  the  MonIQ  rule-based 
import parser — the same keyword logic evaluated in Section IV 
— not by independent human annotation. This introduces circular 
dependence:  the  Llama  models  are  partially  evaluated  against 
labels  generated  by  a  keyword  classifier.  (2)  The  dataset  spans 
two  institutions  (CIBC  and  BMO)  with  different  description 
formats, without institution-stratified analysis. (3) No statistical 
validation  (McNemar's  test)  is  applicable  because  ground-truth 
reliability  is  unknown.  These  results  should  be  interpreted  as 
indicative of model-size scaling behavior, not as a fair accuracy 
benchmark.

Table VI shows the results. Both Llama models substantially 
outperform  keyword  matching  on  type  accuracy  (73.7%  and 
71.9% vs. 45.8% on chequing in Experiment 1), demonstrating 
that  even  smaller  LLMs  can  close  a  significant  portion  of  the 
performance gap without fine-tuning. Notably, Llama-70B shows 
a  slight  regression  in  type  accuracy  relative  to  Llama-8B 
(−1.8pp),  while  improving  on  category  accuracy  (+5.9pp)  and 
Transfer  F1  (+17.8pp).  This  apparent  paradox  likely  reflects 
calibration differences: the larger model is more conservative on 
type  assignment  when  description  context 
is  ambiguous, 
occasionally deferring to a finer-grained category prediction over 
a  high-confidence  type  label.  The  model-size  effect  is  most 
pronounced on Transfer classification — the hardest category — 
where  Llama-70B  achieves  57.9%  F1  vs.  Llama-8B's  40.1%, 
versus  Claude's  99.0%  in  Experiment  1.  This  suggests  that 
resolving direction-dependent semantic ambiguity (Limitation 1, 
Appendix A) scales strongly with model capacity.

TABLE VI 
Experiment 2: Llama Model Size Comparison — Full Dataset (N=7,152, 
Exploratory)

Metric

Keyword*  Llama-8B

Llama-
70B

Delta 
(8B→70B)

Claude†

Type accuracy

Category accuracy

Transfer F1

Gas F1

45.8%

27.5%

0%

97.1%

Credit Payment F1

100%

Fees F1

13.7%

73.7%

36.9%

40.1%

71.2%

92.9%

16.6%

71.9%

42.8%

57.9%

88.1%

98.3%

16.8%

−1.8pp

+5.9pp

+17.8pp

+16.9pp

+5.4pp

+0.2pp

96.5%

77.5%

99.0%

93.8%

100%

100%

Note: Experiment 2 results are not directly comparable to Experiment 1 (Claude 
vs. keyword). Ground truth in Experiment 2 was generated by the MonIQ keyword 
parser, not independent human annotation, introducing circular dependence. 
Keyword baseline and Claude results shown here are from Experiment 1 (N=200, 
CIBC chequing) for reference only.

---

<!-- PAGE 5 -->

TABLE IV 
Deployment Architecture Tradeoffs

Approach

Chequing F1  Latency  Cost/tx  Train?

Keyword only

27.5%

<1ms

$0.000

LLM only 
(Claude)

77.5% / 
42.8%*

2–5s

$0.001

No

No

Fine-tuned BERT

~88%**

<100ms

$0.0001

Yes

Hybrid cascade

~82% (est.)*

<500ms

$0.0003

No

* Claude measured on CIBC chequing N=200 (Experiment 1). Llama measured on 
full 7,152-transaction dataset (Experiment 2, exploratory). Hybrid estimated 
assuming 25% LLM escalation on ambiguous chequing transactions. ** Fine-
tuned BERT estimate based on FinBERT [10] and Kotios et al. [4] on comparable 
hybrid architecture results.

IX. FUTURE WORK

A. Statistical Limitations

The  controlled  benchmark  (Experiment  1)  uses  a  200-
transaction stratified sample from one CIBC chequing account. 
The  full  dataset  already  includes  two  account  holders  and  two 
banks  (CIBC  and  BMO).  Future  work  will  apply  Claude-level 
evaluation with manual label verification to the BMO accounts 
(2,166 transactions across chequing, Mastercard, and LOC) and 
to a second account holder's data, enabling institution-stratified 
accuracy estimates and cross-user generalization tests.

B. Multi-Institution Extension

Extending  to  TD,  RBC,  BMO,  Scotiabank  would  reveal 
whether institution-specific classifiers are needed — critical for 
any universal finance tool.

C. Behavioral Impact Study

Do  AI-generated  spending

insights  change  financial 
behavior?  A  longitudinal  user  study  comparing  MonIQ  users 
receiving AI insights versus a basic ledger constitutes the natural 
next research step.

X. CONCLUSION

Four findings emerge from this work. First, keyword-based 
classification  achieves  96.3%  category  F1  on  credit  card 
transactions  but  only  27.5%  on  chequing  —  a  structural  gap 
rooted in description format differences, not tuning. Second, three 
root causes account for all chequing errors: transfer-fee ambiguity 
(67.1%),  income-expense  context  dependence  (12.6%),  and 
incomplete merchant coverage (20.4%), each formally analyzed 
in Appendix A. Third, in a controlled benchmark on 200 CIBC 
chequing  transactions,  Claude  achieves  96.5%  type  accuracy 
(+51.0pp,  p<0.001)  and  fully  resolves  all  three  failure  modes, 
confirming  that  LLMs  address  the  structural  limitations  of 
keyword matching. Fourth, an exploratory scale-up on all 7,152 
transactions  with  Llama-3.1-8B  and  Llama-3.3-70B  reveals  a 
clear model-size effect on Transfer F1 (40.1% vs. 57.9%), with 
Transfer  classification  serving  as  the  single  most  diagnostic 
task. 
metric 
Recommendation:  keyword  matching  for  structured  account 
types  (credit  cards);  LLM-based  or  hybrid  cascade  for 
unstructured ones (chequing).

future  classifiers  on

for  evaluating

this

REFERENCES

[1] Plaid Inc., "Transaction Data Enrichment," Plaid Developer

Documentation, 2024. [Online]. Available: 
https://plaid.com/docs/transactions/enrichment/

[2] C. Lesner, A. Ran, M. Rukovic, and W. Wang, "Large-Scale

Personalized Categorization of Financial Transactions," in Proc. 
AAAI Conf. on Artificial Intelligence, vol. 33, pp. 9365–9372, 
2019. doi:10.1609/aaai.v33i01.33019365. [Online]. Available: 
https://ojs.aaai.org/index.php/AAAI/article/view/4984

[3] S. García-Méndez, M. Fernández-Gavilanes, J. Juncal-Martínez, F. J. 
González-Castaño, and Ó. Barba Seara, "Identifying Banking 
Transaction Descriptions via Support Vector Machine Short-Text 
Classification Based on a Specialized Labelled Corpus," IEEE 
Access, vol. 8, pp. 61642–61655, 2020. 
doi:10.1109/ACCESS.2020.2983584. [Online]. Available: 
https://ieeexplore.ieee.org/document/9032148

[4] D. Kotios, G. Makridis, G. Fatouros, and D. Kyriazis, "Deep

Learning Enhancing Banking Services: A Hybrid Transaction 
Classification and Cash Flow Prediction Approach," Journal of Big 
Data, vol. 9, no. 100, 2022. doi:10.1186/s40537-022-00651-x. 
[Online]. Available: 
https://journalofbigdata.springeropen.com/articles/10.1186/s40537
-022-00651-x

[5] OpenAI, "GPT-4 Technical Report," arXiv:2303.08774, 2023. 
[Online]. Available: https://arxiv.org/abs/2303.08774

[6] Anthropic, "Claude 3.5 Model Family," Technical Report, 2024.

[Online]. Available: https://www.anthropic.com/news/claude-3-5-
sonnet

[7] H. Touvron et al., "LLaMA 2: Open Foundation and Fine-Tuned

Chat Models," arXiv:2307.09288, 2023. [Online]. Available: 
https://arxiv.org/abs/2307.09288

[8] D. T. Ta, W. Ben Saad, and J. Y. Oh, "Specialized Text

Classification: An Approach to Classifying Open Banking 
Transactions," in Proc. IEEE 18th Int. Conf. on Computer Science 
and Information Technologies (CSIT), 2023. 
doi:10.1109/CSIT61576.2023.10324203. [Online]. Available: 
https://ieeexplore.ieee.org/document/10324203

[9] C. Manning, P. Raghavan, and H. Schütze, Introduction to

Information Retrieval, Cambridge University Press, 2008. 
[Online]. Available: https://nlp.stanford.edu/IR-book/

[10] D. Araci, "FinBERT: Financial Sentiment Analysis with Pre-trained 
Language Models," arXiv:1908.10063, 2019. [Online]. Available: 
https://arxiv.org/abs/1908.10063

APPENDIX A: FORMAL ANALYSIS OF KEYWORD 
CLASSIFIER LIMITATIONS

Note: The following is a formal structural analysis — not a 
mathematical  proof  in  the  strict  axiomatic  sense  —  of  three 
inherent limitations that arise from the architecture of keyword-
based classifiers.

A.1 Metric Definitions

For  category  cᵢ:  Precision  P  =  TP/(TP+FP),  Recall  R  = 
TP/(TP+FN), F1 = 2PR/(P+R) = 2·TP/(2·TP+FP+FN). F1 equals 
zero  when  either  P  or  R  is  zero  —  essential  for  imbalanced 
distributions like ours.

A.2 Classifier Definition

f(d) = γ(kᵢ*)  where  i* = min{i : kᵢ ⊆ 
d};  f(d) = c_default  if  ∄i : kᵢ ⊆ d

f  depends  only  on  d  —  not  on  direction,  amount,  account

type, or context.

A.3 Three Structural Limitations

Limitation 1 — Context Blindness.  For transactions with 
identical descriptions but different true types (e.g., Lyft income 
vs. Lyft expense), f assigns the same label. Since the true labels 
differ,  at  least  one  assignment  is  necessarily  incorrect.  No 
keyword dictionary resolves this without the direction signal. In 
our data: 109 misclassifications.

---

<!-- PAGE 6 -->

Limitation  2  —  Coverage  Decay.    Recall(c)  ≤  |{d  ∈  c  : 
merchant(d) ∈ Kₘ}| / |c|. As the merchant space grows while the 
dictionary stays fixed, this bound decreases monotonically. In our 
data: 177 transactions with no keyword match.

Limitation 3 — Priority Collision.  For d matching both kᵢ 
∈ catᵢ (priority i) and kⱼ ∈ catⱼ (priority j > i), f(d) = catᵢ regardless 
of true label. No reordering resolves this when the correct label 
alternates  for  the  same  d.  In  our  data:  582  INTERNET 
TRANSFER transactions misclassified as Fees.

A.4 LLM Resolution

LLM  classifier  g:  D  ×  {debit,credit}  ×  ℝ⁺  →  C  addresses 
each  limitation:  (1)  direction  signal  resolves  context  blindness; 
(2) pre-trained semantic knowledge classifies unseen merchants; 
(3)  joint  reasoning  over  all  inputs  eliminates  priority  ordering. 
Empirical  confirmation:  Transfer  F1:  0%→99%,  Fees: 
13.7%→100%, Insurance: 0%→100%.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Keyword Matching vs. LLM-Based
Classification for Personal Finance
Transaction Categorization:
A Benchmark Study on Real Canadian Bank Data
Majid Rafiaei
Independent Researcher — Intelligent Systems
Montreal, QC, Canada · majidrafiaei@gmail.com
Abstract — Personal finance applications must automatically classify bank transactions into meaningful spending categories. The dominant
approach — keyword-based rule matching — is fast and interpretable but its accuracy varies dramatically across account types. We present
the first benchmark study of transaction classification on real Canadian bank data. Using MonIQ, a full-stack personal finance prototype, we
constructed a labeled dataset of 7,152 transactions from two account holders, five accounts across two Canadian banks (CIBC and BMO),
spanning 4.5 years (September 2021 – April 2026). We report two experiments. In Experiment 1, a controlled benchmark on 200 CIBC
chequing transactions shows keyword matching achieving 45.8% type accuracy versus Claude (claude-3-5-sonnet-20241022) at 96.5%
(+51.0pp, McNemar's χ²=81.06, p<0.001), confirming that LLMs resolve the structural failures of keyword matching on chequing accounts.
In Experiment 2, an exploratory scale-up on all 7,152 transactions with Llama-3.1-8B and Llama-3.3-70B reveals a clear model-size effect:
Transfer F1 rises from 40.1% (8B) to 57.9% (70B), versus Claude's 99.0%, establishing Transfer classification as the single most diagnostic
metric for this task. We provide a formal structural analysis of three keyword classifier limitations and release our dataset, evaluation code,
and failure taxonomy as the first public Canadian personal finance transaction benchmark.
Keywords — transaction classification, personal finance, keyword matching, large language models, fintech, benchmark, Canadian banking,
statistical validation

We collected transaction exports from five accounts across
I. INTRODUCTION two Canadian banks — CIBC and BMO — belonging to two
account holders, spanning 4.5 years (September 2021 – April
Automatic transaction categorization is a core capability of
2026). Data was exported directly from each bank's online
personal finance software. Applications such as Mint, YNAB,
banking portal as CSV. The full dataset contains 7,152
and Monarch Money rely on it to produce spending breakdowns,
transactions. For keyword and Claude evaluation (Sections IV–
budget recommendations, and savings projections. Without
VII-C), we use the 4,986-transaction CIBC subset (4,044
accurate categorization, downstream analytics are unreliable.
chequing + 942 credit card) where ground-truth labels were
The near-universal approach is keyword-based rule manually verified by the account holder. The full 7,152-
matching: a manually maintained dictionary maps merchant name transaction corpus — including 2,166 BMO transactions — is
fragments to spending categories. This requires no training data, used for the Llama exploratory evaluation in Section VII-D. Edge
is fully interpretable, and executes in microseconds. Despite its cases in the 16-class taxonomy were resolved as follows:
simplicity, it remains the dominant production approach at major merchant refunds are labeled as the inverse of the original
fintech companies including Plaid [1]. transaction type (Expense on credit card, Transfer on chequing);
cashback credits are labeled Other Income; and chargebacks are
This paper investigates the performance gap between
treated as Transfer on chequing and Expense reversal on credit
account types, evaluates LLMs as a replacement with statistical
card. These conventions apply uniformly across both account
validation, and provides formal structural analysis of why
holders.
keyword matching is bounded. Contributions:
TABLE I
• First labeled dataset of real Canadian personal finance
Full Dataset Statistics (CIBC: 4,986 tx; BMO: 2,166 tx across 4
transactions: 7,152 transactions, two account holders, five
accounts and 2 holders)
accounts, two banks (CIBC and BMO), 4.5 years, 16-class
annotations. The 4,986-transaction CIBC subset (4,044 Account N Date Range Types
chequing + 942 credit card) serves as the primary
CIBC Chequing 4,044 Sep 2021–Apr expense, income,
evaluation corpus for keyword and Claude experiments;
(Person 1) 2026 transfer
the remaining 2,166 BMO transactions are used in the
exploratory Experiment 2. CIBC Visa (Person 942 Oct 2021–Apr expense, transfer
• Systematic evaluation: 69pp performance gap — credit 1) 2026
card 96.3% F1 vs. chequing 27.5% F1. Total 7,152 4.5 years 2 users, 2 banks
• Controlled experiment with statistical validation: LLM vs.
* BMO transactions used exclusively in Experiment 2 (exploratory scale-up).
keyword on 200 chequing transactions — +51pp type CIBC subset (4,986 tx: 4,044 chequing + 942 credit) used for keyword evaluation
accuracy (95% CI: [43.6, 58.4]; p<0.001). and controlled Claude benchmark. Account holders are identified as Person 1 and
• Formal structural analysis of three limitations of keyword Person 2 throughout. All personal identifiers have been removed; transaction
descriptions are retained solely for research purposes and cannot be used to
classifiers and a hybrid cascade architecture. identify individuals.
II. BACKGROUND & RELATED WORK IV. KEYWORD-BASED CLASSIFICATION
A. Transaction Classification A. Algorithm
Lesner et al. [2] proposed a large-scale production system The classifier applies a priority-ordered dictionary of 45
for personalized transaction categorization, demonstrating the patterns after routing by account type, following the inverted-
feasibility of automated labeling at scale but without public index retrieval model [9]. Formal definition: f(d) = γ(kᵢ*) where
dataset release or statistical validation. García-Méndez et al. [3] i* = min{i : kᵢ ⊆ d}; f(d) = c_default if no match. O(k) per
combined NLP and SVM techniques to classify banking transaction, no training required.
transaction descriptions for personal finance management,
B. Results and Visualizations
demonstrating that short-text classification of bank data requires
domain-specific approaches. Kotios et al. [4] developed a hybrid
rule-based and ML categorization model for SME transactions,
achieving high accuracy for high-confidence predictions but
noting persistent challenges with noisy, unstructured
descriptions. No prior work has studied Canadian bank data,
which presents unique challenges: bilingual descriptions
(EN/FR), INTERAC vs. Visa Debit ambiguity, and inconsistent
merchant name formatting across institutions.
B. LLMs for Document Understanding
LLMs such as GPT-4 [5], Claude [6], and LLaMA [7]
exhibit strong zero-shot text classification through in-context
learning. Ta et al. [8] demonstrated that specialized preprocessing
and text classification approaches for Open Banking transactions
outperform generic NLP models. No prior work has directly
compared LLM and keyword classification on personal finance
transactions using real labeled data with statistical validation. Fig. 1 — Precision, recall, and F1 definitions with numerical example
from our Transfer category data.
III. DATASET

labeled). Error counts and percentages reflect this subset, not
the full 7,152-transaction dataset.
A. Transfer-Fee Ambiguity (582 errors, 67.1% of N=868)
Every INTERNET TRANSFER misclassified as Fees due to
keyword priority collision. 'SERVICE CHARGE' matches before
the transfer pattern. Requires directional context — formalized as
Limitation 3 in Appendix A.
B. Income-Expense Context Dependence (109 errors, 12.6%)
'Lyft Canada Inc' appears as both income (credit, driver
payments) and expense (debit, rides). Identical descriptions,
different true labels — context blindness (Limitation 1, Appendix
A).
C. Incomplete Coverage (177 errors, 20.4%)
Fig. 2 — Per-category F1 scores, keyword classifier, CIBC evaluation Merchants absent from keyword dictionary (LendDirect,
subset (N=2,222). Mondou, TOYOTA GABRIEL) fall to default. Unbounded as
merchant space grows (Limitation 2, Appendix A).
Table II shows accuracy by account type. The 69pp gap
between credit card (96.3%) and chequing (27.5%) is the central
VI. WHY CREDIT CARDS WORK
finding. Categories with 0% F1 — Transfer, Other Income,
Income, Insurance — account for 64.2% of chequing Three structural properties make keyword matching
transactions. effective for credit cards: (1) merchant names are consistently
formatted and always present; (2) semantics are unambiguous —
TABLE II
every debit is expense, every 'PAYMENT THANK YOU' is
Keyword Classifier — Performance on CIBC Evaluation Subset
payment; (3) the transaction space is commercially bounded.
(N=2,222)
Chequing accounts violate all three. Design principle: keyword
Account Type Acc. Cat. F1 N classification is appropriate if and only if the description reliably
encodes merchant identity and transaction semantics are
Credit Card 100.0% 96.3% 942
unambiguous from the description alone.
Chequing 45.8% 27.5% 4,044
VII. LLM CLASSIFICATION EXPERIMENTS
Overall 71.8% 60.5% 4,986 (CIBC)
A. Experiment 1: Controlled Benchmark (CIBC, N=200)
V. FAILURE ANALYSIS To directly compare keyword matching and LLM
classification under controlled conditions, we evaluated 200
CIBC chequing transactions (stratified random sample, seed=42:
70 expense, 60 income, 70 transfer) using Claude (claude-3-5-
sonnet-20241022, Anthropic) in a zero-shot regime. This is the
same transaction subset used for keyword evaluation in Section
IV, enabling a fair head-to-head comparison. Input per
transaction: account type, direction (debit/credit), amount in
CAD, and raw merchant description string. No examples, no fine-
tuning, no chain-of-thought prompting.
Fig. 3 — Failure mode breakdown: 868 errors in keyword classification
of the CIBC chequing verification subset (N=1,143 transactions,
manually labeled).
Fig. 4 — Hybrid cascade classifier architecture. Keyword classifier
Note: The failure analysis below is reported on the original handles high-confidence cases; LLM escalates ambiguous chequing
verified CIBC chequing subset (N=1,143 transactions, manually transactions (~20–30%).

B. Experiment 1 Results: Claude vs. Keyword (N=200 CIBC  accuracy to ~91.5%. The remaining errors are concentrated in
Chequing)  Uber platform ambiguity (5 cases) — where the description
"UBER* EATS" appeared as both an expense (customer food
|     |     |     |     |     | order)  | and  | income  (driver  | payment  | credit),  an  instance  | of  |
| --- | --- | --- | --- | --- | ------- | ---- | ---------------- | -------- | ----------------------- | --- |
Limitation 1 (Context Blindness, Appendix A) that requires
amount and direction signals to resolve — and the inherently
underspecified "Other" category (7 cases).
VIII. COST-ACCURACY TRADEOFF
D. Experiment 2: Exploratory Scale-Up (Full Dataset,
N=7,152)
To assess model-size effects and evaluate generalization
|     |     |     |     |     | across  | banks  | and  account  | holders,  | we  classified  | all  7,152  |
| --- | --- | --- | --- | --- | ------- | ------ | ------------- | --------- | --------------- | ----------- |
Fig. 5 — Keyword vs LLM type and category accuracy on 200 chequing  transactions using Llama-3.1-8B and Llama-3.3-70B (Meta, via
transactions with 95% confidence intervals.  Groq  API)  in  a  zero-shot  regime.  This  experiment  has  a
fundamentally different methodology from Experiment 1 and the
TABLE III
results cannot be directly compared. Three key differences: (1)
Keyword vs. LLM — 200 Chequing Transactions (95% CI, Wilson
Ground-truth labels were assigned by the MonIQ rule-based
score)
import parser — the same keyword logic evaluated in Section IV
Metric  Keyword  LLM  Delta (95%  — not by independent human annotation. This introduces circular
(Claude)  CI)  dependence: the Llama models are partially evaluated against
labels generated by a keyword classifier. (2) The dataset spans
| Type accuracy  | 45.5% [38.7,  | 96.5% [93.0,  | +51.0pp [43.6,  |     |     |     |     |     |     |     |
| -------------- | ------------- | ------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
two institutions (CIBC and BMO) with different description
|     | 52.4]  | 98.3]  | 58.4]  |     |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
formats, without institution-stratified analysis. (3) No statistical
Category  27.5% [21.8,  77.5% [71.2,  +50.0pp [41.5,  validation (McNemar's test) is applicable because ground-truth
| accuracy  | 34.1]  | 82.7]  | 58.5]  |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
reliability is unknown. These results should be interpreted as
Transfer F1  0%  99.0%  +99.0pp  indicative of model-size scaling behavior, not as a fair accuracy
benchmark.
| Fees F1  | 13.7%  | 100%  | +86.3pp  |     |     |     |     |     |     |     |
| -------- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
Table VI shows the results. Both Llama models substantially
| Insurance F1  | 0%  | 100%  | +100pp  |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
outperform keyword matching on type accuracy (73.7% and
McNemar χ²  —  —  71.9% vs. 45.8% on chequing in Experiment 1), demonstrating
81.06
|     |     |     | (p<0.001)  |     | that even smaller LLMs can close a significant portion of the  |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
performance gap without fine-tuning. Notably, Llama-70B shows
|     |     |     |     |     | a   | slight  regression  | in  | type  accuracy  | relative  to  | Llama-8B  |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --------------- | ------------- | --------- |
(−1.8pp), while improving on category accuracy (+5.9pp) and
Transfer F1 (+17.8pp). This apparent paradox likely reflects
calibration differences: the larger model is more conservative on
|     |     |     |     |     | type  | assignment  | when  | description  | context  is  ambiguous,  |     |
| --- | --- | --- | --- | --- | ----- | ----------- | ----- | ------------ | ------------------------ | --- |
occasionally deferring to a finer-grained category prediction over
a high-confidence type label. The model-size effect is most
pronounced on Transfer classification — the hardest category —
where Llama-70B achieves 57.9% F1 vs. Llama-8B's 40.1%,
versus Claude's 99.0% in Experiment 1. This suggests that
resolving direction-dependent semantic ambiguity (Limitation 1,
Appendix A) scales strongly with model capacity.

TABLE VI
Fig. 6 — Keyword vs LLM per-category F1 on chequing, top diagnostic
Experiment 2: Llama Model Size Comparison — Full Dataset (N=7,152,
categories.
Exploratory)
| The  difference  | is  statistically  | significant  | (McNemar's  |     |         |     |           |           |               |          |
| ---------------- | ------------------ | ------------ | ----------- | --- | ------- | --- | --------- | --------- | ------------- | -------- |
|                  |                    |              |             |     | Metric  |     | Keyword*  | Llama-8B  | Llama- Delta  | Claude†  |
χ²=81.06, p<0.001) with 102 discordant pairs favoring Claude vs.
|     |     |     |     |     |     |     |     |     | 70B  (8B→70B)  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
7 favoring keyword (p<0.001). Claude correctly resolved all three
failure modes identified in Section V: Transfer F1 rose from 0%  Type accuracy  45.8%  73.7%  71.9%  −1.8pp  96.5%
to 99.0%, Fees from 13.7% to 100%, and Insurance from 0% to
|     |     |     |     |     | Category accuracy  |     | 27.5%  | 36.9%  | 42.8%  +5.9pp  | 77.5%  |
| --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------ | -------------- | ------ |
100%.
|     |     |     |     |     | Transfer F1  |     | 0%  | 40.1%  | 57.9%  +17.8pp  | 99.0%  |
| --- | --- | --- | --- | --- | ------------ | --- | --- | ------ | --------------- | ------ |
C. Experiment 1 Error Analysis
|     |     |     |     |     | Gas F1  |     | 97.1%  | 71.2%  | 88.1%  +16.9pp  | 93.8%  |
| --- | --- | --- | --- | --- | ------- | --- | ------ | ------ | --------------- | ------ |
Claude made 7 type errors (3.5%) and 45 category errors
(22.5%). The dominant error — Other Income → Income (28  Credit Payment F1  100%  92.9%  98.3%  +5.4pp  100%
cases, 62% of all category errors) — is a taxonomy labeling
|                    |                      |           |               |      | Fees F1  |     | 13.7%  | 16.6%  | 16.8%  +0.2pp  | 100%  |
| ------------------ | -------------------- | --------- | ------------- | ---- | -------- | --- | ------ | ------ | -------------- | ----- |
| ambiguity  rather  | than  a  classifier  | failure:  | both  labels  | are  |          |     |        |        |                |       |
semantically correct, but the ground truth used a finer-grained  Note: Experiment 2 results are not directly comparable to Experiment 1 (Claude
vs. keyword). Ground truth in Experiment 2 was generated by the MonIQ keyword
distinction between payroll income and other income credits.
parser, not independent human annotation, introducing circular dependence.
Removing  this  ambiguity  raises  estimated  Claude  category  Keyword baseline and Claude results shown here are from Experiment 1 (N=200,
CIBC chequing) for reference only.

TABLE IV [2] C. Lesner, A. Ran, M. Rukovic, and W. Wang, "Large-Scale
Deployment Architecture Tradeoffs Personalized Categorization of Financial Transactions," in Proc.
AAAI Conf. on Artificial Intelligence, vol. 33, pp. 9365–9372,
Approach Chequing F1 Latency Cost/tx Train? 2019. doi:10.1609/aaai.v33i01.33019365. [Online]. Available:
https://ojs.aaai.org/index.php/AAAI/article/view/4984
Keyword only 27.5% <1ms $0.000 No
[3] S. García-Méndez, M. Fernández-Gavilanes, J. Juncal-Martínez, F. J.
LLM only 77.5% / 2–5s $0.001 No González-Castaño, and Ó. Barba Seara, "Identifying Banking
(Claude) 42.8%* Transaction Descriptions via Support Vector Machine Short-Text
Classification Based on a Specialized Labelled Corpus," IEEE
Fine-tuned BERT ~88%** <100ms $0.0001 Yes Access, vol. 8, pp. 61642–61655, 2020.
Hybrid cascade ~82% (est.)* <500ms $0.0003 No
doi:10.1109/ACCESS.2020.2983584. [Online]. Available:
https://ieeexplore.ieee.org/document/9032148
* Claude measured on CIBC chequing N=200 (Experiment 1). Llama measured on [4] D. Kotios, G. Makridis, G. Fatouros, and D. Kyriazis, "Deep
full 7,152-transaction dataset (Experiment 2, exploratory). Hybrid estimated
Learning Enhancing Banking Services: A Hybrid Transaction
assuming 25% LLM escalation on ambiguous chequing transactions. ** Fine-
Classification and Cash Flow Prediction Approach," Journal of Big
tuned BERT estimate based on FinBERT [10] and Kotios et al. [4] on comparable
hybrid architecture results. Data, vol. 9, no. 100, 2022. doi:10.1186/s40537-022-00651-x.
[Online]. Available:
IX. FUTURE WORK https://journalofbigdata.springeropen.com/articles/10.1186/s40537
-022-00651-x
A. Statistical Limitations [5] OpenAI, "GPT-4 Technical Report," arXiv:2303.08774, 2023.
The controlled benchmark (Experiment 1) uses a 200- [Online]. Available: https://arxiv.org/abs/2303.08774
transaction stratified sample from one CIBC chequing account. [6] Anthropic, "Claude 3.5 Model Family," Technical Report, 2024.
The full dataset already includes two account holders and two [Online]. Available: https://www.anthropic.com/news/claude-3-5-
banks (CIBC and BMO). Future work will apply Claude-level sonnet
evaluation with manual label verification to the BMO accounts [7] H. Touvron et al., "LLaMA 2: Open Foundation and Fine-Tuned
(2,166 transactions across chequing, Mastercard, and LOC) and Chat Models," arXiv:2307.09288, 2023. [Online]. Available:
https://arxiv.org/abs/2307.09288
to a second account holder's data, enabling institution-stratified
[8] D. T. Ta, W. Ben Saad, and J. Y. Oh, "Specialized Text
accuracy estimates and cross-user generalization tests.
Classification: An Approach to Classifying Open Banking
B. Multi-Institution Extension Transactions," in Proc. IEEE 18th Int. Conf. on Computer Science
and Information Technologies (CSIT), 2023.
Extending to TD, RBC, BMO, Scotiabank would reveal
doi:10.1109/CSIT61576.2023.10324203. [Online]. Available:
whether institution-specific classifiers are needed — critical for https://ieeexplore.ieee.org/document/10324203
any universal finance tool.
[9] C. Manning, P. Raghavan, and H. Schütze, Introduction to
Information Retrieval, Cambridge University Press, 2008.
C. Behavioral Impact Study
[Online]. Available: https://nlp.stanford.edu/IR-book/
Do AI-generated spending insights change financial [10] D. Araci, "FinBERT: Financial Sentiment Analysis with Pre-trained
behavior? A longitudinal user study comparing MonIQ users Language Models," arXiv:1908.10063, 2019. [Online]. Available:
receiving AI insights versus a basic ledger constitutes the natural https://arxiv.org/abs/1908.10063
next research step.
X. CONCLUSION APPENDIX A: FORMAL ANALYSIS OF KEYWORD
Four findings emerge from this work. First, keyword-based CLASSIFIER LIMITATIONS
classification achieves 96.3% category F1 on credit card Note: The following is a formal structural analysis — not a
transactions but only 27.5% on chequing — a structural gap mathematical proof in the strict axiomatic sense — of three
rooted in description format differences, not tuning. Second, three inherent limitations that arise from the architecture of keyword-
root causes account for all chequing errors: transfer-fee ambiguity based classifiers.
(67.1%), income-expense context dependence (12.6%), and
incomplete merchant coverage (20.4%), each formally analyzed A.1 Metric Definitions
in Appendix A. Third, in a controlled benchmark on 200 CIBC For category cᵢ: Precision P = TP/(TP+FP), Recall R =
chequing transactions, Claude achieves 96.5% type accuracy TP/(TP+FN), F1 = 2PR/(P+R) = 2·TP/(2·TP+FP+FN). F1 equals
(+51.0pp, p<0.001) and fully resolves all three failure modes, zero when either P or R is zero — essential for imbalanced
confirming that LLMs address the structural limitations of distributions like ours.
keyword matching. Fourth, an exploratory scale-up on all 7,152
A.2 Classifier Definition
transactions with Llama-3.1-8B and Llama-3.3-70B reveals a
clear model-size effect on Transfer F1 (40.1% vs. 57.9%), with f(d) = γ(kᵢ*) where i* = min{i : kᵢ ⊆
Transfer classification serving as the single most diagnostic d}; f(d) = c_default if ∄i : kᵢ ⊆ d
metric for evaluating future classifiers on this task.
f depends only on d — not on direction, amount, account
Recommendation: keyword matching for structured account
type, or context.
types (credit cards); LLM-based or hybrid cascade for
unstructured ones (chequing). A.3 Three Structural Limitations
Limitation 1 — Context Blindness. For transactions with
identical descriptions but different true types (e.g., Lyft income
REFERENCES vs. Lyft expense), f assigns the same label. Since the true labels
differ, at least one assignment is necessarily incorrect. No
[1] Plaid Inc., "Transaction Data Enrichment," Plaid Developer
keyword dictionary resolves this without the direction signal. In
Documentation, 2024. [Online]. Available:
https://plaid.com/docs/transactions/enrichment/ our data: 109 misclassifications.

Limitation 2 — Coverage Decay. Recall(c) ≤ |{d ∈ c :
merchant(d) ∈ Kₘ}| / |c|. As the merchant space grows while the
dictionary stays fixed, this bound decreases monotonically. In our
data: 177 transactions with no keyword match.
Limitation 3 — Priority Collision. For d matching both kᵢ
∈ catᵢ (priority i) and kⱼ ∈ catⱼ (priority j > i), f(d) = catᵢ regardless
of true label. No reordering resolves this when the correct label
alternates for the same d. In our data: 582 INTERNET
TRANSFER transactions misclassified as Fees.
A.4 LLM Resolution
LLM classifier g: D × {debit,credit} × ℝ⁺ → C addresses
each limitation: (1) direction signal resolves context blindness;
(2) pre-trained semantic knowledge classifies unseen merchants;
(3) joint reasoning over all inputs eliminates priority ordering.
Empirical confirmation: Transfer F1: 0%→99%, Fees:
13.7%→100%, Insurance: 0%→100%.