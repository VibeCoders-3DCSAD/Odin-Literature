---
conversion_metadata:
  converted_at: "2026-07-21T13:41:58Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kashif & Naseer.pdf"
  source_pdf_sha256: "c778cf2223723a68306bde49caeb55907434ad314446c13e7fc7b53399f93146"
  page_count: 20
  markdown_char_count: 148866
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

ISSN (e) 3007-3138 (p) 3007-312X

COMPREHENSIVE ANALYSIS OF FRAUD DETECTION PREVENTION
SYSTEMS FOR ACCURACY AND EFFICACY

Hasnain Kashif*1, Fawad Naseer 2

*1Computer Science Department, University of South Asia, Lahore, 54000, Pakistan;
2Department of Computer Science and Software Engineering, Beaconhouse International College, Pakistan

*1hasnain.kashif@usa.edu.pk, 2fawad.naseer@bic.edu.pk

DOI: https://doi.org/10.5281/zenodo.15081246

Keywords
Fraud Detection, Prevention
System, System Accuracy, System
Efficacy, Artificial Intelligence

Article History
Received on 18 February 2025
Accepted on 18 March 2025
Published on 25 March 2025

Copyright @Author
Corresponding Author: *

Abstract
Financial fraud, waste, and abuse cost global economies an estimated $5.4
trillion annually, with digital payment platforms experiencing unprecedented
vulnerability. This study presents a systematic evaluation of contemporary fraud
detection and prevention systems across major financial institutions, analyzing
their accuracy, efficacy, and scalability in high-volume transaction environments.
The mixed-methods approach combined quantitative performance metrics from
financial institutions with qualitative assessments from cybersecurity specialists to
evaluate detection algorithms across four dimensions: detection accuracy (false
efficiency, adaptability to emerging
positive/negative rates),
computational
threats, and implementation feasibility. Results demonstrate
that hybrid
approaches combining supervised machine learning with unsupervised anomaly
detection achieved superior performance (92.7% detection accuracy) compared to
traditional rule-based systems (78.3%). Notably, models integrating graph-based
network analysis with deep learning techniques showed particular promise in
identifying sophisticated organized fraud schemes, reducing false positives by 34%
while increasing true positive rates by 27% compared to standalone approaches.
The rise of cloud computing and mobile transactions has fundamentally altered
the fraud landscape, requiring detection systems that can process and analyze real-
time streaming data at unprecedented scale. The comprehensive classification
framework categorizes existing detection systems based on algorithmic approach,
fraud typology, and quantitative performance metrics across diverse financial
contexts. The study identify critical challenges
implementations,
including the increasing sophistication of adversarial attacks, computational
constraints in real-time environments, and the dynamic nature of fraudulent
behaviors. Based on our findings, we propose a next-generation architectural
framework for financial fraud detection that emphasizes real-time adaptability,
explainable AI components, and cross-institutional collaboration, potentially
reducing overall fraud losses by an estimated 41% when implemented at scale.

in current

INTRODUCTION
In today’s era, fraud is very common in all aspects of
intentional unlawful
life. Fraud refers
in an
exploitation of a system that outcomes

to the

oblivious entity's injury. Financial fraud includes the
exploitation of
too
deficient to maintain financial resources, which is

that are

financial

systems

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 382

---

<!-- PAGE 2 -->

ISSN (e) 3007-3138 (p) 3007-312X

scan

blessings

competed

the maximum outstanding money. However,
different damages along with a lacking condition are
possible. Fraud, waste, and abuse in lots of financial
systems wait to provoke massive annual losses in the
billions of US dollars. Robbing a bank with a gun
has now turned out
to be obsolete. Now the
fraudster devotes theft simply with the aid of using
seating at their home. Frauds are one of the big
challenges for the finance industry. Credit card fraud
is the maximum not unusual place sort of fraud and
as per the report, 270,000 instances had been
reported in 2019 [1]. Some research proposes that in
the USA on my own a lack of 17-billion-dollar credit
card fraud turned into associated. There have been
1,387,615 reports of identification robbery in 2020.
According to this scam viewpoint, the year 2020 can
be the nastiest year on the highest
rank. The
numbers of identification robberies ascended and
fecund
authorities
throughout the epidemic [2].
Financial fraud is a difficulty that has huge attaining
effects on the finance industry and everyday life.
Fraud can lessen self-belief in industry, destabilize
economies, and affect an effect on people's value of
living. Traditional methods of
trusted manual
techniques including auditing might be inefficient
the
and unreliable because of
problem. Data mining-primarily based methods had
been proven to be beneficial because of their capacity
to discover small anomalies in huge facts sets [3].
There are several kinds of frauds and different kinds
of data mining methods which are under research to
get the best optimum.
Financial fraud is an extensive term with diverse
capability meanings, however, for our purposes, it
may be described because of the intentional use of
unlawful strategies to acquire financial gain [4].
Fraud has a massive terrible effect on business and
society: credit score card fraud on my debts for
billions of dollars of misplaced revenue every year [5],
and a few figures propose that the overall every year
price to the U.S. could be an extra $400 billion [6].
At the same time, the research indicates that UK
insurers are out 1.6 billion pounds a year because of
fraudulent claims [7]. Financial fraud additionally
has broader ramifications for the industry, which
includes offering investment for illicit activities like
drug trafficking and organized crime [5]. For credit

the difficulty of

card approval,

score card fraud, the price is typically worn through
the merchants, who emerge as paying shipping,
chargeback, and administrative costs in addition to
dropping patron self-belief after being a sufferer to a
fraudulent transaction [8]. In this manner, we will
see the huge effects that fraud will have and the
significance of reducing it.
Advancements in current technology along with the
internet and cellular computing have caused a
growth in financial fraud in the latest years [9]. Social
elements such as the improved distribution of credit
score playing cards have improved spending however
additionally led to a growth in fraud [10]. Fraudsters
are usually refining their strategies, and as such there
may be a demand for detection strategies which will
evolve accordingly [5]. Data mining has already been
proven to be beneficial in comparable domain names
along with credit
bankruptcy
prediction, and evaluation of percentage markets [11].
Fraud detection is taken into consideration to be
comparable class trouble however with a tremendous
imbalance in fraudulent to valid transactions, and a
widespread distinction in value for misclassifying
them [12]. Data mining methods also are relevant to
fraud detection of her performance at processing big
datasets and their capacity to paintings without
requiring information of the input variables [13].
A beneficial framework for making use of records
mining for fraud detection is to apply it as a method
for classifying suspicious transactions or samples for
similar consideration. Studies display that reviewing
2% of credit score card transactions should lessen
fraud losses to 1% of the whole price of all purchases,
with extra exams ensuing in smaller losses, however
with growth in auditing costs. A multilayer pipeline
technique can be used with every step making use of
an extra rigorous technique to discover fraud. Data
mining can be utilized to efficaciously clear out extra
apparent fraud instances withinside the preliminary
levels and go away the extra diffused ones to be
reviewed manually [8].
extensive
In this project, we
terminologies which can be described for clarity.
Data mining refers to any technique that approaches
huge portions of data to derive an underlying
meaning. Within this category, we cannot forget
classes of data mining: statistical and computational.
We outline the statistical strategies as the ones which

can use

some

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 383

---

<!-- PAGE 3 -->

ISSN (e) 3007-3138 (p) 3007-312X

that

techniques,

consisting of

can be primarily based totally on traditional
mathematical
logistic
regression and Bayesian theory. Computational
techniques are the ones which use present-day
intelligence techniques, such as neural networks and
assist vector machines. Though those classes share
many similarities, we cannot forget that the principal
computational
distinction among them is
techniques can study from and adapt to the problem
domain, even as statistical techniques are extra rigid.
Both forms of data mining may be researched in this
project.
Financial
institutions attempt many strategies to
protect against fraud. But fraudsters are very adaptive
to these strategies, over time they find out how to
conquer those protective models. Fraudsters are very
smart and rapid learners. Precisely, we will say that
the exceptional strategies carried out with the aid of
using financial institutions for fraud detection fail
and fraud continues. Development
in the new
technology era in artificial intelligence and machine
learning is gambling vital function in detecting and
stopping fraud.

financial

classification of

The objective of this project is to deliver an existing
literature review in financial fraud detection and
compare their findings. The focus of this project is
on the reported performance of detection techniques
for specific fraud types and focus on the systems and
tools for security provisions. Some mathematical
equations are formalized and analyzed. This will
provide a clear indication to future researchers in
that given field and discuss the improvement.
The
fraud has not
established an agreement since the kinds of financial
research
fraud are diverse and increasing. This
proposes
categorization
financial
methodology based on the main financial institution
involved. Securities and commodity fraud, as well as
financial statement fraud, are examples of securities
fraud. Mortgage fraud, loan default, credit card fraud,
and money laundering are just a few examples of
include e-commerce
bank-related scams. Others
and
transaction fraud, mass marketing
unlawful
include
health care fraud, automotive insurance fraud,
corporate insurance fraud, and so on. Figure 1 shows
the categorization framework.

fund-raising.

Insurance

fraud,

scams

fraud

a

Figure 1: Classification of Financial Institution and its types

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 384

---

<!-- PAGE 4 -->

ISSN (e) 3007-3138 (p) 3007-312X

fraudsters

the threats

sufferers of

Literature Review

from a distance. This

I.
Fraud is a standard phrase for the unlawful use of
a system to attain a few benefits, typically ensuing
in damage to any other person. Frauds are
numerous in addition to fraud methods. Financial
fraud is fraud inside the financial industry that
typically includes money. The financial industries
fraudulent
had been the major
activities. According to [14], billions or likely
trillions of US bucks had been misplaced to
coverage fraud. The proliferation of internet use
has made it less complicated to speak and join
from a distance. It has additionally made it less
to goal economic
complicated for
similarly
establishments
complicates
to protection systems;
accordingly, fraud prevention and detection are
essential troubles for all financial institutions. By
many estimates, a minimum of 10 per cent of
coverage enterprise payments are for fraudulent
claims and the worldwide sum of those fraudulent
payments quantities to billions or likely trillions of
bucks. Fraud prevention refers to all measures
installed region to protect fraud from happening,
even as Fraud detection refers to mechanisms to
hit upon Fraud while prevention fails, [15]. A vital
their
requirement
precision. Much situation is given to enhancing
the precision of such systems. Detection systems,
on the opposite hand, want
to evolve to the
consistent evolution of threats. Therefore, further
to feasible predictiveness, Fraud detection systems
want
to be adaptive. An associated situation
typically classified below feasible predictiveness is
the time required to locate fraudulent transactions.
Certain structures
to real-time
close
require
indicators of suspicious transactions.
Prior research has already been done on a few
factors of smart financial fraud detection. Initial
fraud detection research targeted closely statistical
models including logistic regression, in addition to
neural networks [16], [17]. The researchers located
that neural networks were used for
financial
programs including forecasting because 1988 [18].
In 1995,
anticipated financial
the usage of a back-
declaration fraud was
propagation neural community [19]. In this paper,
a
techniques
they

for preventive

the primary

throughout

compared

systems

is

techniques

they reviewed the look at

statistical and
quantitative spectrum such as
computational
including regression
and neural networks [20]. In 1998, researchers
used a neural community primarily based totally
on different
financial ratios and variables and
discovered it compared favourably to discriminant
evaluation and logistic regression [21]. In 2001 and
2002, they have done a few trendy evaluations on
focusing mainly on statistical
fraud detection,
[23], and investigated financial
learning [22],
declaration fraud in depth [24]. Recent
fraud
detection studies have been some distance extra
numerous in strategies studied, even though the
previous techniques are nevertheless popular. In
trendy fraud
2004,
detection through the usage of analytic techniques
such as neural networks [25]. In this paper, they
investigated a unique technique the usage of the
game principle in 2005, which modelled fraudsters
and detection techniques as opposing gamers in a
sport, every striving to achieve the best financial
advantage [26]. They studied healthcare fraud
through the usage of a system mining technique
[27].
In 2007,
they studied logistic regression with
coverage fraud, targeting a database of Spanish car
coverage claims [28], [29]. Researchers as compared
statistical strategies with neural networks to pick
out fraudulent Greek production organizations [6]
and targeted class and regression trees to remedy
financial declaration fraud in a choice of Chinese
organizations
in 2007 delivered a
genetic set of rules on Accounting and Auditing
Enforcement Releases to come across fraudulent
organizations in the US [17] and evaluate present
fraud detection literature. They claimed that the
most effective hit strategies of fraud detection to
in addition to the maximum generally
date,
researched, have been class-primarily based totally
[16]. Researchers used decision trees to look at
financial declaration fraud for a choice of Chinese
in 2008 [31]. They took a statistical
groups
technique to cover fraud detection, the usage of
the equal samples that have been used previously
[32]. Both researchers checked out visualizing
credit score card fraud with self-organizing maps,
that specialize in real-global samples from the
Singaporean department of a global bank [8]. They

[30]. Also,

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 385

---

<!-- PAGE 5 -->

ISSN (e) 3007-3138 (p) 3007-312X

et

to

to

and

pick

studied

probable

synthetic

personnel

changed the usual
immune system
technique with a coevolutionary technique, the
usage of it to remedy transactional fraud with the
automated teller and point-of-sale information for
a financial organization [33].
In 2009, applied a combination of text mining and
Bayesian perception networks
out
dedicate
disgruntled
company fraud [34]. This paper mixed a Dempster-
Schaefer adder with a Bayesian learner to remedy
credit
score card fraud with their very own
al.
synthesized information [11]. Sánchez
targeted credit score playing cards supplied with
the aid of using a multinational branch store, and
the usage of self-organizing maps to cluster and
visualize fraudulent patterns [10]. In this newsletter,
they as compared help vector machines with
decision trees in fixing credit score card fraud, with
a focal point on aggregating not unusual place
transactional variables to create new inputs [35]. In
2010,
Auditing
Accounting
Enforcement Releases (AAER) with their very own
textual content mining and help vector device
hybrid to are expecting economic declaration fraud
in US groups [36].
In 2011, as compared the capacity of
logistic
regression, help vector machines, and random
forests on a massive pattern of credit score card
to pick out which have been
transactions
fraudulent
[7]. Both researchers mixed the
strengths of genetic algorithms and scatter seek to
create their very own hybrid technique. They used
to tune customer spending with a massive
it
the
Turkish bank, as a resource to predict
incidence of credit score card fraud [11]. In this
paper, they created text-mining hybrids with the
aid of using making use of different not unusual
place strategies to behave because of the classifier.
With a help vector machine, decision tree, and
Bayesian belief network they
controlled to
effectively perceive fraud in the company’s 10-K
report filings [37]. Both researchers additionally
studied sections of 10-K files
for US groups
recognized to be fraudulent, processing the text
with a novel validation decomposition vector to
[38]. They carried out
categorize the samples
system mining to the inner logs created with the
aid of using a European financial institution to

they

logistic

checked out

come across company fraud [39] and did a huge
evaluation of present fraud detection [7]. Also, in
2011, as compared a massive variety of techniques
financial declaration fraud inside
to discover
to helping
Chinese organizations. In addition,
vector machines,
genetic
programming,
regression, organization
technique of information handling, and a lot of
neural networks [13]. This newsletter created a
universal framework for financial declaration fraud
detection through the usage of response floor
methodology [4], then in 2012 with the aid of
using making use of an artificial immune system to
expect credit
score card fraud for a first-rate
Australian bank [40].
In 2013 Huang investigated financial declaration
fraud in a chain of Taiwanese organizations
through the usage of logistic regression and a help
vector machine [41]. Both scientists took an extra
direct technique and targeted the litigation phase
of
the Securities and Exchange Commission
website, making use of their very own text-mining
set of rules to categorize financial declaration fraud
[42]. In this paper, they studied the capacity of
decision trees to pick out fraudulent credit score
card transactions, and the usage of a six-month
In 2014
pattern from a first-rate bank [43].
researchers used text mining to look at AAERs for
Chinese groups that have been buying and selling
publicly in the US [44]. researcher visualized credit
scorecard fraud with self-organizing maps, focusing
most effectively on accounts held with the aid of
using citizens of Warsaw, Poland [45] researchers
applied an artificial immune system to pick out
credit scorecard fraud for a nameless Brazilian
bank [46] and investigated the prevailing kingdom
of fraud detection studies [47].
are
In 2015,
mentioned for fraud detection, which is based on
the kind of consumer clustering and for every
cluster representing a certain kind of consumer,
the system could have distinct behaviour. Finally,
also studied through a decision tree set of rules
and a neural network model. Models can extract
associated with consumer
numerous policies
the
chosen withinside
behaviour which are
corresponding table and have a chance per cent to
discover the suspected cases [48]. In 2016, k-means

the data mining

techniques

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 386

---

<!-- PAGE 6 -->

ISSN (e) 3007-3138 (p) 3007-312X

regular

supervised learning

clustering is used for credit card fraud detection.
Data is growing haphazardly for credit cards and
the k-means set of rules is used for coming across
transactions whether it is fraud transaction or a
valid transaction [49]. In 2017, researchers checked
various detection techniques primarily based
totally on credit cards in phrases of Parameter
Speed of detection and provides a survey of diverse
techniques utilized in credit card fraud detection
and prevention [50]. In 2018, there are two main
focuses, first on fraud instances that cannot be
detected primarily based totally on preceding
records or
and secondly
producing a model of deep Auto-encoder and
restricted Boltzmann machine (RBM) that may
reconstruct
to search out
anomalies from regular patterns [51].
In 2019, this paper could be very vital for ATM
card issuers to select the best optimum solution for
fraud detection problem, additionally permit us to
construct a hybrid technique for growing a few
optimum algorithms that can carry out nicely on
In 2020,
fraud detection mechanism [52].
been developed
numerous
primarily based totally on Artificial
intelligence,
Machine
learning, Data mining, Genetic
programming, Fuzzy logic etc. for detecting credit
card fraudulent activities. On the other hand, the
K-Nearest Neighbour
algorithm and outlier
detection techniques are applied to optimize the
fraud detection
for
exceptional
problem [53]. In 2021, develop a model to analyze
the imbalanced credit card fraud dataset [54].

techniques have

transactions

answer

the

fraud

Fraud Detection and Prevention

II.
Fraud Detection and Prevention is a system-
installed software program that may analyze any
inappropriate activity, offering risk mitigation and
safety monitoring.
from a network
It differs
protection strategy and enables the computer to
identify suspicious activity before theft or other
crimes are committed. Tools for detecting and
preventing
investigative
techniques to find and stop fraud on a company
device. These algorithms examine data from many
different sources to look for probable errors like
anomalies or illusions. It is utilized by a variety of
businesses and organizations, including those in
and
the
government work. It is used to prevent cybercrimes
that harm a company or organization, including
account theft, malware, hacking, DDoS, phishing,
and credit card identity theft.

healthcare,

sciences,

travel,

used

life

are

as

Fraud Detection

A.
The system of the fraud detection which can be
detect and also manages scammers from getting
cash or possessions means wrong. It is a collection
of actions designed to disclose and prevent
attempts from scammers to acquire money or
assets fraudulently. Fraud detection is popular in
banks, insurance, healthcare, government, and the
public
regulation
enforcement
overall working
scenario is shown in Figure 2.

agencies. The

addition

sectors,

in

to

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 387

---

<!-- PAGE 7 -->

ISSN (e) 3007-3138 (p) 3007-312X

Figure 2: Fraud Detection Working Scenario

Laundering of money, cyberattacks, fake monetary
privileges, bogus financial-bank cheques, burglary
identification and lots of greater illegal moves that
are the cases of duplicitous movement. From now,
to respond the upward thrust in deceitful dealings
corporations adapt
throughout diverse stages,
front-line fraud detection and prevention methods
in addition to the strategies of risk management.
B.
Types of Fraud Detection Techniques
The techniques based on data analysis are generally
applied to detect fraud. The particular approaches

may be roughly grouped into different categories
such as artificial intelligence-based, and statistical
data analysis or computational methods. Imagine
artificial
intelligence, machine learning, neural
networks, and deep learning as russian-nesting
dolls [55] as shown in Figure 3. This is maybe the
simplest way to conceptualize these concepts. Every
one of them functions as a part of the previous
work.

Figure 3: Count Nested

In other words, artificial intelligence includes the
field of machine learning. The algorithms of deep
learning which is the foundation of the neural
networks and these are the branch of machine
learning. In actuality, the neural network depth,
the node layers having wide variety that splits it
from a deep learning approach are requires greater

than three layers. The detection techniques as
given below,

Artificial Immune System (AIS)

a)
The data mining strategy is the artificial immune
systems which detects antigens through mimicking
the biological immune system behavior [56]. The

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 388

---

<!-- PAGE 8 -->

ISSN (e) 3007-3138 (p) 3007-312X

in

traits, but

the majority of

artificial immune system may imitate a wide range
of biological
them
revolve around the detector cells formation and
having potential capability to recognize external
things. The cells of detector are created at random,
and reproduction is used to check and assess their
efficacy,
how other
comparable with
classification systems train.
Clonal selection is a typical kind that produces the
cells of detector which at most exist for the brief
period. When a cell identifies an antibody that
the invader and can
lives
transform such as an outcome of the battle. The
cells that survive after the imitation are the finest
prepared to recognize the antitoxins. Negative
selection is one more frequent method that the
random producing cells and
whole thing at

to combat

longer

defining how they interact with another epidemic
cells in the system. In general, it has deleted and
leaving
capable of detecting
intruders [57].

remaining

the

Neural Network (NN)

b)
This is a computer model of the human brain
which is named as neural network that represents
neuronal and synapsis using the vertices and edges
graphs [3]. The network works by modeling the
enter variables as a layer of vertices after which
making use of a weight to every link withinside the
graph, whereas the ultimate vertices are located at
distinctive layers primarily based totally on their
distance from the enter nodes [58] as shown in
Figure 4.

Figure 4: Simple Neural Network

Each node bases its input on the associated vertices
to it preceding layer. The received signal through
each neuron

is given by

shows the link weight of neurons

Where
and

=  × 
 

and
represents the input. If the result exceeds
a certain threshold, the existing neuron fires and

develops an input for the following layer.
Training a back proliferation neural network
involves putting trials from the training data set
through the system and compared the outcomes.
At
selected
arbitrarily for first iteration, and when the results
is lightly changed
are computed, every weight
through the following sequence [59]. The process
is repeated until either the network's error has

each edge weights are generally

been decreased to an acceptable level or a
predefined iteration limit has remained achieved.
Following iteration, the network's performance can
be evaluated using a set of validation data [3].
Overtraining
through
backpropagation the neural network, causing the
network to emphasis on trends specific to the set
of training data rather than broader challenge [59].

typical

issue

is

a

employ

the notion of

Genetic Algorithm (GA)

c)
To iteratively enhance issue solutions, genetic
algorithms
resident
development. It works by establishing a beginning
group at random, then repeatedly replicating every
resident utilizing various methods and choosing
strength.
survivors
taking two
Reproduction is accomplished by

depending

upon

their

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 389

---

<!-- PAGE 9 -->

ISSN (e) 3007-3138 (p) 3007-312X

exiting generation parents and employing crossover
on dual places, at that time arbitrarily transforming
a individual element of the resultant successors. A
fitness function is used to assess the capacity of the
offspring, and the results determine whose parents
and kids are chosen as the future generation's
representatives. The proportion of samples that the
kids properly classify can be utilized to gauge their

level of strength. The method finishes when it
achieves the desired strength, even though to
prevent indefinite looping, a limit on the number
of iterations can be stated, as illustrated in Figure 5.
Similar to neural networks, genetic algorithms may
uncover underlying correlations among the data
without the need for advance information of the
issue domain. [60].

Figure 5: Flowchart of Genetic Algorithm Process

Hidden Markov Model (HMM)

d)
The is a statistical model named as hidden markov
model in which the represented system is believed
to remain a markov process through an unseen
state [61].
fraud by analyzing user
spending profiles, which are classified into three
types [62]:

It detects

I.
II.
III.

lower profile
middle profile
higher profile

Figures 6 depict the training and detection and
preventive phases [63] [64] of the procedure. In

this setup, launch the bank server and the HMM
server first. When a transaction is initiated by the
client, HMM begins watching and comparing the
process. If fraud is detected, the transaction is
stopped. The user responds with a password on a
cellphone through Bluetooth to the similar ATM
of bank, otherwise via message/sms. The passkey is
validated for authorization, and the transaction is
permitted. After three failed tries, the transaction
is completely halted.

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 390

---

<!-- PAGE 10 -->

ISSN (e) 3007-3138 (p) 3007-312X

Figure 6: Flow chart of Training and Detection Phase in HMM

Bayesian Belief Network (BBN)

e)
A statistical categorization approach is the bayesian
belief network which employs the theorem of bayes,
which is a way of determining the likelihood
having a given hypothesis is true. According to
theorem, the probability
. For
may be categorized inside a certain type
example,
that specified as

for a hypothesis

χ

χ  =

χ  ()
(χ)

χ

and inserts

for
A network uses a classifier to calculate
into the class
all possible classes
  χ
. In this way, the network
with the highest

is demonstrated to categorize each sample into the
  χ
class to which it is most likely to belong [6].
A network may be represented graphically as a
focused on acyclic graph, having nodes which is
representing
a
fundamental relationship among them as shown in
Figure 7. The absence of missing edges may thus
be used to exhibit in which two variables are
unrelated of each other [3].

representing

and edges

trials

Figure 7:BNN Graphical Representation

Cluster Method (CM)

f)
The cluster method is the procedure of organizing
information within classes of things that are alike.
Several cluster algorithms existing in classes of the
dataset produce different grouping outcomes. The

approach used will be determined by the intended
outcome [65]. The clustering of k-means is a
modest and effective approach to data clustering.
Figure 8 depicts the clustering-based approach's
system architecture [66].

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 391

---

<!-- PAGE 11 -->

ISSN (e) 3007-3138 (p) 3007-312X

Figure 8: System Architecture of Cluster Method

the accuracy of

Firstly, the parameters utilised in the programme,
like transaction award, credit/debit
just
card
number, current
transaction time,
transaction,
mercantile group id, transaction category id and
transaction state, are declared. The validation
mechanism then verifies
the
transaction information. The previously prepared
data table is now inserted within the database. The
information that is being removed from counter
and now inserted to take transaction info. The
transaction information is then produced row by
row using an array. Following that, the cluster is
labelled as down, up, or moderate dangerous. The
current transaction information was obtained to
detect fraud or real transactions using the k-means
clustering method. Uncertainty, the transaction is
deceitful, the notification says "fraud transaction,"
or else it will say "legal transaction."

Self-Organizing Map (SOM)

g)
The main type of artificial neural network is self-
organizing map that consists of a single neural
matrix. Inputs from a high-dimensional space are
mapped to a two-dimensional array of neurons, a

non-linear method is utilized. The mapping is
intended to model comparable input vectors as
neurons which are nearer together in the final
matrix, allowing the inputs to be seen. To group
the nodes, a distance or neighborhood function,
just like the euclidean distance formula or the
gaussian formula, is utilized [63]. The clustering
subjected to is
function that each neuron is
provided by:

Where
represents the specific node present
+1 =  + ( − −1)
represents the present input vector
weighting,

represents the preferred the function of
and
distance. Before the process
the
clustering phase is
repeated a predetermined
number of times [67].

finished,

is

Decision Tree (DT)

h)
Decision trees are a classification or prediction
approach that utilizes a tree with internal nodes
reflecting binary options on characteristics and
branches expressing the result of that decision [59]
as shown in Figure 9. Now trial travels the tree, it
is segregated within the subsets though it is finally
categorized within a jointly special subclass.

Figure 9:Decision Tree Representation

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 392

---

<!-- PAGE 12 -->

ISSN (e) 3007-3138 (p) 3007-312X

A decision forest, sometimes known as a random
forests that is a decision tree collection intended to
prevent the unstableness and risk of exaggerate in
which an individual tree may cause [5]. Random
forests employ distinct training info among tree
and limit the characteristics pool presented to each
internal node at random [5]. Pruning is another
strategy for decreasing overfitting in decision trees,
which includes removing decision nodes without
affecting the tree's overall accuracy [6]. These
approaches
to
exaggerate and noise. Because every tree is created
randomly, the computing complexity is minimal.
Furthermore, the only two factors that must be
adjusted are the number of trees and the collection
of characteristics from which to create each node,
making decision forests straightforward to generate
[5].

random forest

resistant

render

Super Vector Machine (SVM)

i)
Support Vector Machines (SVM) are statistical
learning approaches that have been successfully
idea
used for a variety of issues. The essential
behind the SVM sorting method is to build a
hyperplane known the decision plane, maximizing
the distance among the positive and negative
[68]. SVM is a well-known machine
modes
learning approach for
sorting, regression, and
additional problems. LIB-SVM is a Support Vector
Machines library (SVM). LIBSVM is often used in
two stages: first, setting a training sequence to
generate a model. After that utilizing the model to
guess information from a testing info set. The
SVM have major functions are as follows:

model development.

produced dataset and refer it to SVM training.

point in the big dataset.

the SVM Predictor predicts the learned data.

SVM Trainer, which trains every single data

After the dataset has been entirely trained,

Next, arrange SVM elements for the newly

First, set up the training information for

the same time as the opposite does not. This is a
significant difference and there are several factors
areas where one of the two approaches performs
better than the other, although the two strategies
do differ somewhat from one another.

Supervised Learning

a.
The supervised learning method to machine
learning is prominent by the utilize of labelled
datasets. Classification and regression are two
main types that may be used to classify supervised
learning when applying data mining.

Classification

i)
The Classification issues utilize an algorithm to
exactly distribute test data into various classes, just
like distinctive among apples and oranges. An
alternative is to segregate spam from your email in
supervised learning
a
techniques. Decision
vector
machines, random forests, and linear classifiers are
examples of common classification approaches.

folder using

separate

support

trees,

to

get

learning

technique,

Regression

ii)
An algorithm is utilized in regression, a distinct
supervised
the
relationship among dependent and independent
parameters. Regression models are beneficial while
expecting numbers based on a species of data
sources, just like sales revenue estimations for a
and
particular
polynomial regressions are a few mutual regression
methods.

organization. Logistic,

linear

Unsupervised Learning

b.
Unsupervised learning investigates and classifies
unlabeled statistical sets using machine learning
methods. Without the support of humans, these
algorithms look for statistics that point to hidden
elegances.
and
dimensionality lessening were the three main
learning
functions
paradigms.

in unsupervised

association,

Clustering,

applied

C.
Supervised and Unsupervised Learning
There are important strategies utilized in machine
intelligence which are
learning and artificial
supervised and unsupervised learning. One employ
labelled data to support in outcome estimation, at

Clustering

i)
Unlabeled data may be characterized utilizing the
statistics mining method, in which clusters objects
only based upon their resemblances or alterations.

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 393

---

<!-- PAGE 13 -->

ISSN (e) 3007-3138 (p) 3007-312X

K-means clustering approaches
split associated
statistical elements within clusters based upon
the
comparations, and the k-means
identifies
the
dimensions and amount of granularity of
clusters. Various parameters, consisting market
segmentation and image reduction, build this
tactic attractive.

Association

a diversity of measures

ii)
The association shape of unsupervised learning
utilizes
to novelty
in a provided
associations among parameters
dataset. Both the marketplace basket evaluation
and the "Customers who bought this item also
bought" recommendation engine frequently utilize
those approaches.

iii) Dimensionality Reduction
Dimensionality reduction is a learning method
utilized when a dataset has excessive properties (or

dimensions). It mitigates the info inputs volume to
a well-behaved level whereas retaining the data
integrity. This method is broadly utilized for pre-
processing data, just like whenever autoencoders
enhance the video quality of resultant images.

and

politicians have

Fraud Prevention

D.
adopted
Corporations
technologies
like data analytics and artificial
intelligence to significantly reduce and even avoid
the economic, social, and financial consequences
of fraud. Consequently, analysts and researchers
eliminate barriers, discover and rank severity-based
alerts, and then present high-priority indications
for further analysis.
Advances in fraud detection technology serve as a
precise and effective weapon against scammers.
There are eight steps for fraud prevention as
shown in Figure 10.

Figure 10: Fraud Prevention Steps

executing

Institution's

The fraud prevention strategy presents a high-level
fraud
the
plan for
prevention policy. In view of the fact that the
approach is the supreme important factor of the
fraud prevention plan, it should be simple and
realistic. The fraud risk management policy and
the fraud risk profile of the institution determine
the fraud prevention approach. There are some
fraud prevention strategies as follows [69] [70].

Identification and Evaluation of Sensitive

a)
Regions
To develop and implement a fraud prevention
the organization should firstly define
strategy,
wherever
in the Institution's
fraud risks exist
present operational systems and processes. Only

when these exposures have been recognized will it
be feasible to take corrective action and, if possible,
avoid or minimize the occurrence of fraud in the
future.

Fraud Risk Ownership

b)
To some extent, all
staff are accountable for
managing fraud risk, although the Accounting
Officer / Authority has final accountability. Line
managers in certain areas of the Institution may be
delegated authority by the Accounting Officer /
Authority. The Accounting Officer / Authority has
the authority to transfer responsibilities for fraud
risk management as well as the flow of operations
from the strategic to the operational level.

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 394

---

<!-- PAGE 14 -->

ISSN (e) 3007-3138 (p) 3007-312X

Plan of Action

c)
The Institution should define clear processes for
dealing with control deficiencies as part of the
response plan. The organization must establish
clean reporting forms for scam. Scam reporting
must be incorporated into the respond strategy or
investigative policy. The rejoinder proposal must
include define the actions and persons in charge of
each response activity.

The Legal Framework

d)
The necessary legislation for dealing with civil and
criminal offences against the Institution should be
defined and properly construed.
should be
obvious what defines a fraudulent or corrupt
behaviour.

It

Culture of Anti-Fraud

e)
should
The Accounting Officer / Authority
establish frameworks
to promote and educate
stakeholders about the Institution's anti-fraud and
anti-corruption culture. As part of an anti-fraud
strategy, management might be entrusted with the
obligation of teaching other employees under their
supervision on fraud and corruption.

III. Analysis and Discussion
We will categorize the financial fraud detection
techniques described in this area based on their

existing

patterns

success rate, the method used, and the fraud type
to
analyzed. This classification will allow us
illustrate
research
in
methodologies. The study's objectives were to
ascertain the operational response of various fraud
detection methods. We conducted a comparative
study on fraud detection methods to analyze the
results. For comparison, we considered the most
important parameters such as accuracy, speed, and
cost. A comparison table has been created to
compare different ATM card fraud detection
the ATM card fraud
mechanisms. Each of
detection techniques described in this study has its
own set of benefits and drawbacks. Table 1 shows
the comparison results obtained from this study
[71], [72], [73], [74],[75], [76].
This study examined the performance of various
ATM cards fraud detection techniques such as
algorithms, Hidden
neural networks,
Markov models, Bayesian networks, decision trees,
clustering methods,
vector machines
(SVM), and artificial immune systems. As a result,
each method has benefits and drawbacks. At the
same time, the support vector machine has a low
detection speed and the artificial immune system
has a high detection speed. So, based on the results,
the best method among these techniques is AIS,
NN, GA, HMM, BBN, CN, SOM, DT and SVM.

support

genetic

Table 1: Benefits and Drawbacks of various Fraud Detection Techniques

Techniques
Artificial
(AIS)

Immune

System

Neural Networks (NN)

Genetic Algorithm (GA)

Markov

Hidden
(HMM)
Bayesian Belief Network (BBN)

Model

ease

Benefits
Self-organization,
of
integration with other systems,
and fault tolerance
High
detection
portability, and speed
Detection is inexpensive and
quick.

accuracy,

Rapid detection.

To operate, data must be
trained and a high processing
speed is required. More precise
than a neural
and faster

Drawbacks
In the NSA, extensive training
is required.

format

cost/data

High
sensitivity
Setup and operation require
extensive tool knowledge and
are difficult to understand.
Low accuracy/incapability to
handle large data sets
Excessive training is required,
and BBN's are slower to apply
to new instances.

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 395

---

<!-- PAGE 15 -->

ISSN (e) 3007-3138 (p) 3007-312X

network.

Clustering method (CN)

Self-Organizing Map (SOM)

Decision Tree (DT)

into

Clustering assists in grouping
clusters,
data
allowing
data
retrieval.

similar

simple

for

To reduce incredibly complex
problems
easily
down
interpreted data mappings
High
adaptability/ease
implementation

to

of

Support
(SVM)

Vector Machine

SVMs can be robust even if the
training sample is biased.

non-fraudulent
Numerous
were mistakenly
activities
to
frauds. So,
identified as
and
fraud accurately
detect
efficiently, real data must be
available.
Requires neuron weights to be
necessary
to
cluster inputs.
Each
be
The
checked
transaction condition is used
in fraud detection.
performance
Expensive/poor
when processing large datasets.

condition must
individually.

and sufficient

This paper presents a comparative study of various
credit
card fraud detection techniques. The
this paper is to examine the
primary goal of
methodology of various credit card detection

methods. The survey-based comparison of
the
mentioned approaches in terms of parameters such
as detection speed, accuracy, and the cost is shown
in Table 2.

Table 2: Comparison of various Fraud Detection Techniques

Techniques

AIS
NN
GA
HMM

BBN
CM
SOM
DT
SVM

Detection
Speed
Very Fast
Fast
Good
Fast

Very Fast
High
Fast
Fast
Low

IV. Conclusion
Fraud detection is an essential component of the
modern financial business. This
the
literature focused on research on statistical and
computational
intelligence techniques for fraud
detection. Despite differences in effectiveness, each
approach was demonstrated to be relatively capable
of identifying various types of financial fraud. The

study of

Accuracy

Cost

Good
Medium
Medium
Low

High
Medium
Medium
Medium
Medium

Inexpensive
Expensive
Inexpensive
High
Expensive
Expensive
Expensive
Expensive
Expensive
Expensive
capacity of computational approaches
such as
neural networks and support vector machines to
learn and adapt to new strategies is extremely
useful in fraudsters growing strategies.
The main objective of
this work is to review
various fraud detection methods. Fraud detection
and prevention should be a key concern for every
company. A well-planned and implemented fraud

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 396

---

<!-- PAGE 16 -->

ISSN (e) 3007-3138 (p) 3007-312X

a

inside

company

detection system may lower the likelihood of fraud
occurring
dramatically.
Furthermore, the quick discovery of fraud has a
direct beneficial impact on the firm by lowering
future potential
losses. AI and statistical data
analysis are effective detection approaches that act
as a deterrent to potential scammers. As legal
and regulatory demands have
requirements
increased, it has become more critical to create an
effective fraud detection and prevention program.
All the fraud detection techniques presented in
this project have both strengths and disadvantages.
Some approaches have a high detection speed but
a low accuracy. Some approaches offer high
accuracy but are prohibitively costly.

financial

Future Work and Challenges

V.
Although data-driven artificial intelligence systems
have demonstrated remarkable performance in the
detection of financial fraud, significant concerns
remain unresolved as
fraud schemes
evolve to adapt to this new digital environment. As
follows, we present the primary problems and offer
future work directions from task-oriented, data-
oriented, and model-oriented perspectives.
Financial fraud is becoming more difficult to

detect due to its increasing secrecy and complexity.
The secrecy of financial fraud causes natural

inaccuracy in sampling.
processes
of

necessitates the involvement of large amounts of
data.

fraud detection is vast, yet it is dispersed.

address.

large-scale data processing.

more adaptable and interpretable.




The issue of model bias must be addressed.
Robustness should be improved.
Improved interpretability is required.

Data isolation is a challenging problem to

Model training is made more difficult by

The amount of financial data available for

Models for detecting financial fraud must be

financial

intricacy

The

References
https://legaljobs.io/blog/credit-card-fraud-statistics/ -

Jenifer Kuadli - 2022

https://www.fool.com/the-ascent/research/identity-
theft-credit-card-fraud-statistics/ - Lyle Daly
and Jack Caporal, 2022.

Ngai E., Hu Y., Wong Y., Chen Y., and Sun X., “The
application of data mining techniques in
fraud detection: A classification
financial
framework and an academic
review of
literature,” Decision Support Systems 50, 559-
69, 2011.

Zhou W. and Kapoor G., “Detecting evolutionary
financial statement fraud,” Decision Support
Systems 50, 570-5, 2011.

Bhattacharyya S.,

Jha S., Tharakunnel K., and
Westland J. C., “Data mining for credit card
fraud: A comparative study,” Decision Support
Systems 50, 602-13, 2011.

for

financial

Kirkos E., Spathis C. and Manolopoulos Y., “Data
the detection of
mining techniques
statements,” Expert
fraudulent
Systems with Applications 32, 995-1003, 2007.
Ngai E., Hu Y., Wong Y., Chen Y. and Sun X., “The
application of data mining techniques in
financial
fraud detection: A classification
review of
framework and an academic
literature,” Decision Support Systems 50, 559-
69, 2011.

Quah J. T. and Sriganesh M., “Real-time credit card
fraud
computational
intelligence,” Expert Systems with Applications
35, 1721-32, 2008.

detection

using

techniques

Yeh I. and Lien C. H. “The comparisons of data
mining
predictive
accuracy of probability of default of credit
card clients,” Expert Systems with Applications
36, 2473-80, 2009.

the

for

Sánchez D., Vila M., Cerda L. and Serrano J. M.,
“Association rules applied to credit card
Systems with
fraud
Applications 36, 3630-40, 2009.

detection,”

Expert

Panigrahi S, Kundu A, Sural S, and Majumdar AK,
“Credit card fraud detection: A fusion
approach using Dempster Shafer theory and
Bayesian learning,” Information Fusion 10,
354-63, 2009.

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 397

---

<!-- PAGE 17 -->

ISSN (e) 3007-3138 (p) 3007-312X

Duman E. and Ozcelik M. H., “Detecting credit card
fraud by genetic algorithm and scatter
search,” Expert Systems with Applications 38,
13057-63, 2011.

Ravisankar P., Ravi V., Raghava Rao G., and Bose I.,
“Detection of financial statement fraud and
feature
data mining
techniques,” Decision Support Systems 50, 491-
500, 2011.

selection

using

Judith Hurwitz, Alan Nugent, Fern Halper, and
Marcia Kaufman, “How Big Data Analytics
Can Prevent Fraud,” chapter 22, page 260.
Big Data for Dummies. John Wiley & Sons,
2013.

Richard J. Bolton and David J. Hand, “Statistical
Fraud Detection: A Review,” Journal of
Statistical Science, 17:235-255, 2002.
Yue D., Wu. X., Wang Y., Li Y., and Chu C. H, “A
review of data mining based financial fraud
detection
Wireless
Communications, Networking
and Mobile
Computing, WiCom. International Conference
on. (ed.), Vol. pp. 5519-22, IEEE, 2007.

research,”

In

Hoogs B., Kiehl T, Lacomb C., and Senturk D., “A
genetic algorithm approach to detecting
temporal patterns
financial
fraud,”
statement
in
Accounting, Finance and Management 15, 41-
56, 2007.

indicative of
Intelligent

Systems

Zhang G., Eddy Patuwo B., and Y. Hu M.,
“Forecasting with artificial neural networks:
The state of the art,” International journal of
forecasting 14, 35-62, 1998.

Sohl J. E. and Venkatachalam A., “A neural network
approach to forecasting model selection,”
Information & Management 29, 297-303, 1995.
Fraser I. A., Hatherly D. J., and Lin K. Z., “AN
EMPIRICAL INVESTIGATIONOF THE
USE OF ANALYTICAL REVIEW BY
EXTERNAL AUDITORS,” The British
Accounting Review 29, 35-47, 1997.

Fanning K. M. and Cogger K. O., “Neural network
fraud using
International
in Accounting,

detection of management
financial
published
data,”
Intelligent Systems
Journal of
Finance & Management 7, 21-41, 1998.

Bolton R.

J. and Hand D. J., “Statistical

fraud
detection: A review,” Statistical Science 235-
49, 2002.

Bolton R. J. and Hand D. J., “Unsupervised profiling
methods for fraud detection,” Credit Scoring
and Credit Control VII 235-55, 2001.
Rezaee Z., “In Financial statement fraud: prevention and
detection,” Vol. pp. John Wiley & Sons, 2002.
Kou Y., Lu C. T., Sirwongwattana S., and Huang Y.
P., “Survey of fraud detection techniques,”
In Networking,
IEEE
international conference on. (ed.), Vol. 2, pp.
749-54, IEEE, 2004.

sensing and control,

Vatsa V., Sural S., and Majumdar AK., “A game
theoretic approach to credit card fraud
detection,” In Information Systems Security.
Vol. pp. 263-76. Springer, 2005.

Yang W. S. and Hwang S. Y., “A process mining
framework for the detection of healthcare
fraud and abuse,” Expert
Systems with
Applications 31, 56-68, 2006.

Pinquet J., Ayuso M., and Guillen M., “Selection
insurance
bias and auditing policies
claims,” Journal of Risk and Insurance 74, 425-
40, 2007.

for

in

for

the

claims

“Strategies

Viaene S., Ayuso M., Guillen M., Van Gheel D., and
detecting
automobile
of

Dedene G.,
fraudulent
insurance industry,” European Journal
Operational Research 176, 565-83, 2007.
Bose I. and Wang J., “Data mining for detection of
financial
in Chinese
Companies,” International Conference on
Administration,
Electronic Commerce,
Society and Education, Hong Kong, 2007.

statement

fraud

Bai B., Yen J., and Yang X., “False financial
statements: characteristics of China's listed
companies and CART detecting approach,”
International Journal of Information Technology
& Decision Making 7, 339-59, 2008.
Bermúdez L., Pérez J., Ayuso M., Gómez E., and
Vázquez F., “A Bayesian dichotomous model
in
with
link
insurance,”
and
Economics 42, 779-86, 2008.

Insurance: Mathematics

asymmetric

fraud

for

Wu S. X. and Banzhaf W., “Combatting financial
fraud: a coevolutionary anomaly detection

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 398

---

<!-- PAGE 18 -->

ISSN (e) 3007-3138 (p) 3007-312X

approach,” In Proceedings of the 10th annual
conference
evolutionary
computation. (ed.), Vol. pp. 1673-80, ACM,
2008.
Holton C.,

on Genetic

and

“Identifying disgruntled employee
systems fraud risk through text mining: A
simple solution for a multi-billion-dollar
problem,” Decision Support Systems 46, 853-64,
2009.

Whitrow C., Hand D. J., Juszczak P., Weston D., and
Adams N. M., “Transaction aggregation as a
strategy for credit card fraud detection,”
Data Mining and Knowledge Discovery 18, 30-
55, 2009.

Cecchini M., Aytug H., Koehler G. J., and Pathak P.,
“Making words work: Using financial text as
a predictor of
financial events,” Decision
Support Systems 50, 164-75, 2010.

Humpherys S. L., Moffitt K. C., Burns M. B.,
F.,
Burgoon
financial
“Identification
statements
credibility
analysis.,” Decision Support Systems 50, 585-94,
2011.

and
fraudulent
linguistic

J. K.,
of
using

Felix W.

Glancy F. H. and Yadav S. B., “A computational
model
fraud
detection,” Decision Support Systems 50, 595-
601, 2011.

reporting

financial

for

Jans M., vander Werf J. M., Lybaert N. and Vanhoof
K., “A business process mining application
for internal transaction fraud mitigation,”
Expert Systems with Applications 38, 13351-9,
2011.

Wong N., Ray P., Stephens G. and Lewis L.,
“Artificial immune systems for the detection
an architecture,
of
credit
prototype
results,”
Information Systems Journal 22, 53-76, 2012.

card fraud:
and

preliminary

Huang S. Y., “Fraud Detection Model by Using
Support Vector Machine Techniques,”
JDCTA: International Journal of Digital Content
Technology and its Applications 7, 32- 42, 2013.
Zaki M. and Theodoulidis B., “Analyzing Financial
Fraud Cases Using a Linguistics Based Text
Mining Approach,” Available
SSRN
2353834, 2013.

at

Sahin Y., Bulkan S., and Duman E., “A cost-sensitive
decision tree approach for fraud detection,”
Expert Systems with Applications 40, 5916-23,
2013.

Dong W., Liao S. S., Fang B., Cheng X., Chen Z.,
and Fan W., “The Detection of Fraudulent
Financial
Integrated
Statements:
Language Model,” 2014.

An

Olszewski D., “Fraud detection using self-organizing
map visualizing the user profiles,” Knowledge
Based Systems, 2014.

Soltani Halvaiee N. and Akbari M. K., “A novel
model for credit card fraud detection using
Artificial
Immune Systems,” Applied Soft
Computing, 2014.

West J., Bhattacharya M. and Islam R., “Intelligent
Financial Fraud Detection Practices: An
Investigation”,
International
10th
Conference on Security and Privacy in
Communication Networks, 2014.

Singh, P. and Singh, M., “Fraud Detection by
Monitoring Customer
and
Activities,” International Journal of Computer
Applications, 111, 23-32, 2015.

Behavior

Sonawane, Y.B., Gadgil, A.S., More, A.E. and Jathar,
N.K., “Credit Card Fraud Detection Using
Clustering Based Approach,” International
Journal of Advance Research and Innovative
Ideas in Education, 2, 1773-1776, 2016.
Gupta, Surbhi, Mrs. and Nitima Malsa. “Credit Card
Fraud Detection & Prevention – A Survey,”
International Journal for Innovative Research in
Science & Technology, vol.1, 4, 2017.
Pumsirirat, A. and Liu, Y., “Credit Card Fraud
Detection Using Deep Learning based on
Auto-Encoder and Restricted Boltzmann
Machine,” International Journal of Advanced
Computer Science and Application, 9, 18-25,
2018.

Rahman, M. and Saha, A., “A Comparative Study
and Performance Analysis of ATM Card
Fraud Detection Techniques,” Journal of
Information Security, 10, 188-197, 2019.
Pooja, Dr. Ashlesha, "Review on Credit Card Fraud
Detection using Machine Learning Algorithms,"
International Journal of Computer Trends and
Technology, 68.6, 77-81, 2020.

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 399

---

<!-- PAGE 19 -->

ISSN (e) 3007-3138 (p) 3007-312X

Panda, A., Yadlapalli, B., & Zhou, Z., “Credit card
fraud detection through machine learning
algorithm,” Big data and computing visions, 1
(3), 140-145, 2021.

B.

Jiang and Y. Mu,

Learning Nested Networks
Adaptive Dynamic
IEEE/CVF
Computer Vision Workshops
336-344, 2021.

"Russian Doll Network:
for Sample-
2021
on
(ICCVW), pp.

International Conference

Inference,"

coevolutionary

Wu SX and Banzhaf W, “Combatting financial fraud:
detection
a
approach,” In Proceedings of the 10th annual
conference
evolution-ary
computation. (ed.), Vol. pp. 1673-80, ACM,
2008.

on Genetic

anomaly

and

Soltani Halvaiee N and Akbari MK,” A novel model
card fraud detection using
Immune Systems,” Applied Soft

credit

for
Artificial
Computing, 2014.

Koh HC and Low CK, “Going concern prediction
using data mining techniques,” Managerial
Auditing Journal 19, 462-76, 2004.

Zhang D and Zhou L, “Discovering golden nuggets:
data mining in financial application,” Systems,
Man, and Cybernetics, Part C: Applications and
Reviews, IEEE Transac-tions on 34, 513-22,
2004.

Su, Jianhai & Havens, Timothy., “Fuzzy community
detection in social networks using a genetic
algortihm.” IEEE International Conference
on
2039-2046.
Systems.
10.1109/FUZZ-IEEE.2014.6891611, 2014.

Fuzzy

Sonawne, V.D., Gupta, P., Raut, A. and Saudagar, F.,
“ATM Card Fraud Detection Using Hidden
Journal of
Markov Model,” International
Innovative Research in Computer
and
Communication Engineering, 4, 8742-8747,
2016.

Patidar, R. and Sharma, L., “Credit Card Fraud
Using
Network,”
Journal of Soft Computing

Detection
International
and Engineering , 1, 32-38, 2011.

Neural

Mhamane, S.S. and Lobo, L.M.R.J., “Use of Hidden
Markov Model as Internet Banking Fraud
Detection,”
of
Journal
International
Computer Applications, 45, 5-10, 2012.

Bhingarde, A., Bangar, A., Gupta, P. and Karambe,
S., “Credit Card Fraud Detection Using
Hidden Markov Model,”
International
Journal of Advanced Research in Computer
and Communication Engineering, 4, 169-
170, 2015.

Vaishali, “Fraud Detection in Credit Card by
Clustering Approach,” International Journal
of Computer Applications, 98, 29-32, 2014.
Sonawane, Y.B., Gadgil, A.S., More, A.E. and Jathar,
N.K., “Credit Card Fraud Detection Using
Clustering Based Approach,” International
Journal of Advance Research and Innovative
Ideas in Education, 2, 1773-1776, 2016.

Quah JT and Sriganesh M, “Real-time credit card
fraud
computational
intelligence,” Expert Systems with Applications
35, 1721-32, 2008.

detection

using

Olszewski D, “Fraud detection using self-organizing
map visualizing the user profiles,” Knowledge-
Based Systems, 2014.

S. Surbhi and D. S. Kumar, "Fraud Detection During
Money Transaction and Prevention," 2019
International Conference
and
Challenges in Intelligent Computing Techniques
(ICICT), pp. 1-4, 2019.

Issues

on

in

an

S. Hoyer, H. Zakhariya, T. Sandner and M. H.
Breitner, "Fraud Prediction and the Human
Factor: An Approach to Include Human
Fraud
Behavior
Audit," 2012 45th Hawaii
International
Conference on System Sciences, 2012, pp. 2382-
2391, 2018.
Zareapoor, M., Seeja, K.R.

Automated

and Alam, M.A.,
“Analysis of Credit Card Fraud Detection
Techniques: Based on Certain Design
Criteria,”
of
International
Computer Applications, 52, 35-42, 2012.

Journal

Kumari, S. and Choubey, A. “A Review on Various
Techniques and Approaches for Credit Card
Fraud Detection,” International Journal of
Engineering &
Scientific
Technology, 6, 485-489, 2017.

Research

Bhatia, S., Bajaj, R. and Hazari, S., “Analysis of
Credit Card Fraud Detection Techniques,”
International
and
Research, 5, 1302-1307, 2016.

Science

Journal

of

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 400

---

<!-- PAGE 20 -->

ISSN (e) 3007-3138 (p) 3007-312X

Singh, P. and Singh, M., “Fraud Detection by
and
of

Monitoring Customer
Activities,”
International
Computer Applications, 111, 23-32, 2015.

Behavior

Journal

Pumsirirat, A. and Liu, Y., “Credit Card Fraud
Detection Using Deep Learning based on
Auto-Encoder and Restricted Boltzmann
of
Machine,”
Advanced
and
Applications, 9, 18-25, 2018.

International
Computer

Science

Journal

Gupta, S. and Malsa, N. “Credit Card Fraud
Prevention—A Survey,”
Detection
International
Innovative
Research in Science & Technology, 4,1-7,
2017.

Journal

and

for

https://sesjournal.com

| Kashif & Naseer, 2025 |

Page 401

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| ISSN (e) 3007-3138 | (p) 3007-312X |          |     |           |              |     |           |          |     |            |     |     |
| ------------------ | ------------- | -------- | --- | --------- | ------------ | --- | --------- | -------- | --- | ---------- | --- | --- |
| COMPREHENSIVE      |               | ANALYSIS |     | OF        | FRAUD        |     | DETECTION |          |     | PREVENTION |     |     |
|                    | SYSTEMS       |          | FOR | ACCURACY  |              | AND |           | EFFICACY |     |            |     |     |
|                    |               | Hasnain  |     | Kashif*1, | FawadNaseer2 |     |           |          |     |            |     |     |
*1ComputerScienceDepartment,UniversityofSouthAsia,Lahore,54000,Pakistan;
2DepartmentofComputerScienceandSoftwareEngineering,BeaconhouseInternationalCollege,Pakistan
*1hasnain.kashif@usa.edu.pk,2fawad.naseer@bic.edu.pk
DOI: https://doi.org/10.5281/zenodo.15081246
Abstract
Keywords Financial fraud, waste, and abuse cost global economies an estimated $5.4
FraudDetection,Prevention trillion annually, with digital payment platforms experiencing unprecedented
System,SystemAccuracy,System vulnerability. This study presents a systematic evaluation of contemporary fraud
Efficacy,ArtificialIntelligence detection and prevention systems across major financial institutions, analyzing
|     |     | their | accuracy,     | efficacy, |          | and scalability |     | in high-volume |     | transaction | environments. |      |
| --- | --- | ----- | ------------- | --------- | -------- | --------------- | --- | -------------- | --- | ----------- | ------------- | ---- |
|     |     | The   | mixed-methods |           | approach | combined        |     | quantitative   |     | performance | metrics       | from |
ArticleHistory
|     |     | financial |     | institutions | with | qualitative | assessments |     | from | cybersecurity | specialists | to  |
| --- | --- | --------- | --- | ------------ | ---- | ----------- | ----------- | --- | ---- | ------------- | ----------- | --- |
Receivedon18February2025 evaluate detection algorithms across four dimensions: detection accuracy (false
Acceptedon18March2025 positive/negative rates), computational efficiency, adaptability to emerging
Publishedon25March2025 threats, and implementation feasibility. Results demonstrate that hybrid
|     |     | approaches |     | combining | supervised |     | machine | learning | with | unsupervised |     | anomaly |
| --- | --- | ---------- | --- | --------- | ---------- | --- | ------- | -------- | ---- | ------------ | --- | ------- |
Copyright@Author
|     |     | detection |     | achieved | superior | performance |     | (92.7% | detection | accuracy) | compared | to  |
| --- | --- | --------- | --- | -------- | -------- | ----------- | --- | ------ | --------- | --------- | -------- | --- |
CorrespondingAuthor:* traditional rule-based systems (78.3%). Notably, models integrating graph-based
|     |     | network     | analysis   |               | with          | deep learning |        | techniques   | showed   | particular        |           | promise in  |
| --- | --- | ----------- | ---------- | ------------- | ------------- | ------------- | ------ | ------------ | -------- | ----------------- | --------- | ----------- |
|     |     | identifying |            | sophisticated |               | organized     | fraud  | schemes,     | reducing | false             | positives | by 34%      |
|     |     | while       | increasing |               | true positive | rates         | by 27% | compared     |          | to standalone     |           | approaches. |
|     |     | The         | rise of    | cloud         | computing     | and           | mobile | transactions |          | has fundamentally |           | altered     |
thefraudlandscape,requiringdetectionsystemsthatcanprocessandanalyzereal-
|     |     | time        | streaming |                | data at          | unprecedented  |                     | scale.         | The comprehensive |                | classification   |             |
| --- | --- | ----------- | --------- | -------------- | ---------------- | -------------- | ------------------- | -------------- | ----------------- | -------------- | ---------------- | ----------- |
|     |     | framework   |           | categorizes    | existing         | detection      |                     | systems        | based             | on algorithmic |                  | approach,   |
|     |     | fraud       | typology, |                | and quantitative |                | performance         |                | metrics           | across         | diverse          | financial   |
|     |     | contexts.   |           | The study      | identify         | critical       |                     | challenges     | in                | current        | implementations, |             |
|     |     | including   |           | the increasing |                  | sophistication |                     | of adversarial |                   | attacks,       | computational    |             |
|     |     | constraints |           | in real-time   |                  | environments,  |                     | and the        | dynamic           | nature         | of               | fraudulent  |
|     |     | behaviors.  |           | Based          | on our           | findings,      | we                  | propose        | a next-generation |                | architectural    |             |
|     |     | framework   |           | for financial  |                  | fraud          | detection           | that           | emphasizes        | real-time      | adaptability,    |             |
|     |     | explainable |           | AI             | components,      | and            | cross-institutional |                |                   | collaboration, |                  | potentially |
reducingoverallfraudlossesbyanestimated41%whenimplementedatscale.
INTRODUCTION
In today’s era, fraud is very common in all aspects of oblivious entity's injury. Financial fraud includes the
life. Fraud refers to the intentional unlawful exploitation of financial systems that are too
exploitation of a system that outcomes in an deficient to maintain financial resources, which is
| https://sesjournal.com |     |     | |Kashif |     | & Naseer,2025| |     |     |     |     |     |     | Page382 |
| ---------------------- | --- | --- | ------- | --- | -------------- | --- | --- | --- | --- | --- | --- | ------- |

ISSN (e)3007-3138 (p) 3007-312X
the maximum outstanding money. However, score card fraud, the price is typically worn through
different damages along with a lacking condition are the merchants, who emerge as paying shipping,
possible. Fraud, waste, and abuse in lots of financial chargeback, and administrative costs in addition to
systems wait to provoke massive annual losses in the dropping patron self-belief after being a sufferer to a
billions of US dollars. Robbing a bank with a gun fraudulent transaction [8]. In this manner, we will
has now turned out to be obsolete. Now the see the huge effects that fraud will have and the
fraudster devotes theft simply with the aid of using significanceofreducingit.
seating at their home. Frauds are one of the big Advancements in current technology along with the
challengesforthefinanceindustry.Creditcardfraud internet and cellular computing have caused a
is the maximum not unusual place sort of fraud and growthinfinancialfraudinthelatestyears[9].Social
as per the report, 270,000 instances had been elements such as the improved distribution of credit
reported in 2019 [1]. Some research proposes that in score playing cards have improved spending however
the USA on my own a lack of 17-billion-dollar credit additionally led to a growth in fraud [10]. Fraudsters
card fraud turned into associated. There have been are usually refining their strategies, and assuch there
1,387,615 reports of identification robbery in 2020. may be a demand for detection strategies which will
According to this scam viewpoint, the year 2020 can evolve accordingly [5]. Data mining has already been
be the nastiest year on the highest rank. The proventobebeneficialincomparabledomainnames
numbers of identification robberies ascended and along with credit card approval, bankruptcy
authorities blessings scan competed fecund prediction,andevaluationofpercentagemarkets[11].
throughouttheepidemic[2]. Fraud detection is taken into consideration to be
Financial fraud is a difficulty that has huge attaining comparable classtrouble however with a tremendous
effects on the finance industry and everyday life. imbalance in fraudulent to valid transactions, and a
Fraud can lessen self-belief in industry, destabilize widespread distinction in value for misclassifying
economies, and affect an effect on people's value of them [12]. Data mining methods also are relevant to
living. Traditional methods of trusted manual fraud detection of her performance at processing big
techniques including auditing might be inefficient datasets and their capacity to paintings without
and unreliable because of the difficulty of the requiringinformationoftheinputvariables[13].
problem. Data mining-primarily based methods had A beneficial framework for making use of records
beenproventobebeneficialbecauseoftheircapacity mining for fraud detection is to apply it as a method
to discover small anomalies in huge facts sets [3]. for classifying suspicious transactions or samples for
There are several kinds of frauds and different kinds similar consideration. Studies display that reviewing
of data mining methods which are under research to 2% of credit score card transactions should lessen
getthebestoptimum. fraudlossesto1%ofthewholepriceofallpurchases,
Financial fraud is an extensive term with diverse with extra exams ensuing in smaller losses, however
capability meanings, however, for our purposes, it with growth in auditing costs. A multilayer pipeline
may be described because of the intentional use of technique can be used with every step making use of
unlawful strategies to acquire financial gain [4]. an extra rigorous technique to discover fraud. Data
Fraud has a massive terrible effect on business and mining can be utilized to efficaciously clear out extra
society: credit score card fraud on my debts for apparent fraud instances withinside the preliminary
billionsofdollarsofmisplacedrevenueeveryyear[5], levels and go away the extra diffused ones to be
and a few figures propose that the overall every year reviewedmanually[8].
price to the U.S. could be an extra $400 billion [6]. In this project, we can use some extensive
At the same time, the research indicates that UK terminologies which can be described for clarity.
insurers are out 1.6 billion pounds a year because of Data mining refers to any technique that approaches
fraudulent claims [7]. Financial fraud additionally huge portions of data to derive an underlying
has broader ramifications for the industry, which meaning. Within this category, we cannot forget
includes offering investment for illicit activities like classes of data mining: statistical and computational.
drug trafficking and organized crime [5]. For credit Weoutlinethestatisticalstrategiesastheoneswhich
https://sesjournal.com |Kashif & Naseer,2025| Page383

ISSN (e)3007-3138 (p) 3007-312X
can be primarily based totally on traditional The objective of this project is to deliver an existing
mathematical techniques, consisting of logistic literature review in financial fraud detection and
regression and Bayesian theory. Computational compare their findings. The focus of this project is
techniques are the ones which use present-day onthereportedperformanceofdetectiontechniques
intelligence techniques, such as neural networks and for specific fraud types and focus on the systems and
assist vector machines. Though those classes share tools for security provisions. Some mathematical
many similarities,we cannot forget thatthe principal equations are formalized and analyzed. This will
distinction among them is that computational provide a clear indication to future researchers in
techniques can study from and adapt to the problem thatgivenfieldanddiscusstheimprovement.
domain, even as statistical techniques are extra rigid. The classification of financial fraud has not
Both forms of data mining maybe researched in this established an agreement since the kinds of financial
project. fraud are diverse and increasing. This research
Financial institutions attempt many strategies to proposes a financial fraud categorization
protectagainstfraud.Butfraudstersareveryadaptive methodology based on the main financial institution
to these strategies, over time they find out how to involved. Securities and commodity fraud, as well as
conquer those protective models. Fraudsters are very financial statement fraud, are examples of securities
smart and rapid learners. Precisely, we will say that fraud.Mortgagefraud,loandefault,creditcardfraud,
the exceptional strategies carried out with the aid of and money laundering are just a few examples of
using financial institutions for fraud detection fail bank-related scams. Others include e-commerce
and fraud continues. Development in the new transaction fraud, mass marketing fraud, and
technology era in artificial intelligence and machine unlawful fund-raising. Insurance scams include
learning is gambling vital function in detecting and health care fraud, automotive insurance fraud,
stoppingfraud. corporateinsurancefraud,andsoon.Figure1shows
thecategorizationframework.
Figure1:ClassificationofFinancialInstitutionanditstypes
https://sesjournal.com |Kashif & Naseer,2025| Page384

ISSN (e)3007-3138 (p) 3007-312X
I. LiteratureReview quantitative spectrum such as statistical and
Fraud is a standard phrase for the unlawful use of computational techniques including regression
a system to attain a few benefits, typically ensuing and neural networks [20]. In 1998, researchers
in damage to any other person. Frauds are used a neural community primarily based totally
numerous in addition to fraud methods. Financial on different financial ratios and variables and
fraud is fraud inside the financial industry that discovered it compared favourably to discriminant
typically includes money. The financial industries evaluationandlogisticregression[21].In2001and
had been the major sufferers of fraudulent 2002, they have done a few trendy evaluations on
activities. According to [14], billions or likely fraud detection, focusing mainly on statistical
trillions of US bucks had been misplaced to learning [22], [23], and investigated financial
coverage fraud. The proliferation of internet use declaration fraud in depth [24]. Recent fraud
has made it less complicated to speak and join detection studies have been some distance extra
from a distance. It has additionally made it less numerous in strategies studied, even though the
complicated for fraudsters to goal economic previous techniques are nevertheless popular. In
establishments from a distance. This similarly 2004, they reviewed the look at trendy fraud
complicates the threats to protection systems; detection through the usage of analytic techniques
accordingly, fraud prevention and detection are such as neural networks [25]. In this paper, they
essential troubles for all financial institutions. By investigated a unique technique the usage of the
many estimates, a minimum of 10 per cent of gameprinciple in 2005,which modelled fraudsters
coverage enterprise payments are for fraudulent and detection techniques as opposing gamers in a
claims and the worldwide sum of those fraudulent sport, every striving to achieve the best financial
payments quantities to billions or likely trillions of advantage [26]. They studied healthcare fraud
bucks. Fraud prevention refers to all measures through the usage of a system mining technique
installed region to protect fraud from happening, [27].
even as Fraud detection refers to mechanisms to In 2007, they studied logistic regression with
hit upon Fraud while prevention fails, [15]. A vital coverage fraud, targeting a database of Spanish car
requirement for preventive systems is their coverageclaims[28],[29].Researchersascompared
precision. Much situation is given to enhancing statistical strategies with neural networks to pick
the precision of such systems. Detection systems, out fraudulent Greek production organizations [6]
on the opposite hand, want to evolve to the and targeted class and regression trees to remedy
consistent evolution of threats. Therefore, further financial declaration fraud in a choice of Chinese
to feasible predictiveness, Fraud detection systems organizations [30]. Also, in 2007 delivered a
want to be adaptive. An associated situation genetic set of rules on Accounting and Auditing
typically classified below feasible predictiveness is Enforcement Releases to come across fraudulent
thetimerequiredtolocatefraudulenttransactions. organizations in the US [17] and evaluate present
Certain structures require close to real-time fraud detection literature. They claimed that the
indicatorsofsuspicioustransactions. most effective hit strategies of fraud detection to
Prior research has already been done on a few date, in addition to the maximum generally
factors of smart financial fraud detection. Initial researched, have been class-primarily based totally
fraud detection research targeted closely statistical [16]. Researchers used decision trees to look at
models including logistic regression, in addition to financial declaration fraud for a choice of Chinese
neural networks [16], [17]. The researchers located groups in 2008 [31]. They took a statistical
that neural networks were used for financial technique to cover fraud detection, the usage of
programs including forecasting because 1988 [18]. the equal samples that have been used previously
In 1995, the primary anticipated financial [32]. Both researchers checked out visualizing
declaration fraud was the usage of a back- credit score card fraud with self-organizing maps,
propagation neural community [19]. In this paper, that specialize in real-global samples from the
they compared techniques throughout a Singaporean department ofa global bank[8]. They
https://sesjournal.com |Kashif & Naseer,2025| Page385

ISSN (e)3007-3138 (p) 3007-312X
changed the usual synthetic immune system come across company fraud [39] and did a huge
technique with a coevolutionary technique, the evaluation of present fraud detection [7]. Also, in
usage of it to remedy transactional fraud with the 2011, as compared a massive variety of techniques
automated teller and point-of-sale information for to discover financial declaration fraud inside
afinancialorganization[33]. Chinese organizations. In addition, to helping
In2009,appliedacombinationoftextminingand vector machines, they checked out genetic
Bayesian perception networks to pick out programming, logistic regression, organization
disgruntled personnel probable to dedicate technique of information handling, and a lot of
company fraud [34].Thispaper mixeda Dempster- neural networks [13]. This newsletter created a
Schaefer adder with a Bayesian learner to remedy universalframeworkfor financialdeclarationfraud
credit score card fraud with their very own detection through the usage of response floor
synthesized information [11]. Sánchez et al. methodology [4], then in 2012 with the aid of
targeted credit score playing cards supplied with usingmakinguse ofanartificialimmunesystemto
the aid of using a multinational branch store, and expect credit score card fraud for a first-rate
the usage of self-organizing maps to cluster and Australianbank[40].
visualizefraudulentpatterns[10].Inthisnewsletter, In 2013 Huang investigated financial declaration
they as compared help vector machines with fraud in a chain of Taiwanese organizations
decisiontreesinfixingcreditscorecardfraud,with through the usage of logistic regression and a help
a focal point on aggregating not unusual place vector machine [41]. Both scientists took an extra
transactionalvariablestocreatenewinputs[35].In direct technique and targeted the litigation phase
2010, studied Accounting and Auditing of the Securities and Exchange Commission
Enforcement Releases (AAER) with their very own website, making use of their very own text-mining
textual content mining and help vector device setofrulestocategorize financialdeclarationfraud
hybridtoareexpectingeconomicdeclarationfraud [42]. In this paper, they studied the capacity of
inUSgroups[36]. decision trees to pick out fraudulent credit score
In 2011, as compared the capacity of logistic card transactions, and the usage of a six-month
regression, help vector machines, and random pattern from a first-rate bank [43]. In 2014
forests on a massive pattern of credit score card researchers used text mining to look at AAERs for
transactions to pick out which have been Chinese groups that have been buying and selling
fraudulent [7]. Both researchers mixed the publicly in theUS [44]. researcher visualized credit
strengths of genetic algorithms and scatter seek to scorecard fraud with self-organizing maps, focusing
create their very own hybrid technique. They used most effectively on accounts held with the aid of
it to tune customer spending with a massive using citizens of Warsaw, Poland [45] researchers
Turkish bank, as a resource to predict the applied an artificial immune system to pick out
incidence of credit score card fraud [11]. In this credit scorecard fraud for a nameless Brazilian
paper, they created text-mining hybrids with the bank [46] and investigated the prevailing kingdom
aid of using making use of different not unusual offrauddetectionstudies[47].
place strategies to behave because of the classifier. In 2015, the data mining techniques are
With a help vector machine, decision tree, and mentioned for fraud detection, which is based on
Bayesian belief network they controlled to the kind of consumer clustering and for every
effectively perceive fraud in the company’s 10-K cluster representing a certain kind of consumer,
report filings [37]. Both researchers additionally the system could have distinct behaviour. Finally,
studied sections of 10-K files for US groups also studied through a decision tree set of rules
recognized to be fraudulent, processing the text and a neural network model. Models can extract
with a novel validation decomposition vector to numerous policies associated with consumer
categorize the samples [38]. They carried out behaviour which are chosen withinside the
system mining to the inner logs created with the corresponding table and have a chance per cent to
aid of using a European financial institution to discover the suspected cases[48]. In 2016, k-means
https://sesjournal.com |Kashif & Naseer,2025| Page386

ISSN (e)3007-3138 (p) 3007-312X
clustering is used for credit card fraud detection. II. FraudDetectionandPrevention
Data is growing haphazardly for credit cards and Fraud Detection and Prevention is a system-
the k-means set of rules is used for coming across installed software program that may analyze any
transactions whether it is fraud transaction or a inappropriate activity, offering risk mitigation and
validtransaction[49].In2017,researcherschecked safety monitoring. It differs from a network
various detection techniques primarily based protection strategy and enables the computer to
totally on credit cards in phrases of Parameter identify suspicious activity before theft or other
Speed ofdetection andprovidesa surveyofdiverse crimes are committed. Tools for detecting and
techniques utilized in credit card fraud detection preventing fraud are used as investigative
and prevention [50]. In 2018, there are two main techniques to find and stop fraud on a company
focuses, first on fraud instances that cannot be device. These algorithms examine data from many
detected primarily based totally on preceding different sources to look for probable errors like
records or supervised learning and secondly anomalies or illusions. It is utilized by a variety of
producing a model of deep Auto-encoder and businesses and organizations, including those in
restricted Boltzmann machine (RBM) that may the life sciences, healthcare, travel, and
reconstruct regular transactions to search out governmentwork.Itisusedtopreventcybercrimes
anomaliesfromregularpatterns[51]. that harm a company or organization, including
In 2019, this paper could be very vital for ATM account theft, malware, hacking, DDoS, phishing,
cardissuerstoselectthebestoptimumsolution for andcreditcardidentitytheft.
fraud detection problem, additionally permit us to
construct a hybrid technique for growing a few A. FraudDetection
optimum algorithms that can carry out nicely on The system of the fraud detection which can be
fraud detection mechanism [52]. In 2020, detect and also manages scammers from getting
numerous techniques have been developed cash or possessions means wrong. It is a collection
primarily based totally on Artificial intelligence, of actions designed to disclose and prevent
Machine learning, Data mining, Genetic attempts from scammers to acquire money or
programming, Fuzzy logic etc. for detecting credit assets fraudulently. Fraud detection is popular in
card fraudulent activities. On the other hand, the banks, insurance, healthcare, government, and the
K-Nearest Neighbour algorithm and outlier public sectors, in addition to regulation
detection techniques are applied to optimize the enforcement agencies. The overall working
exceptional answer for the fraud detection scenarioisshowninFigure2.
problem [53]. In 2021, develop a model to analyze
theimbalancedcreditcardfrauddataset[54].
https://sesjournal.com |Kashif & Naseer,2025| Page387

| ISSN (e)3007-3138 | (p) 3007-312X |     |     |     |     |
| ----------------- | ------------- | --- | --- | --- | --- |
Figure2:FraudDetectionWorkingScenario
Laundering of money, cyberattacks, fake monetary may be roughly grouped into different categories
privileges, bogus financial-bank cheques, burglary such as artificial intelligence-based, and statistical
identification and lots of greater illegal moves that data analysis or computational methods. Imagine
are the cases of duplicitous movement. From now, artificial intelligence, machine learning, neural
to respond the upward thrust in deceitful dealings networks, and deep learning as russian-nesting
throughout diverse stages, corporations adapt dolls [55] as shown in Figure 3. This is maybe the
front-line fraud detection and prevention methods simplestwaytoconceptualizetheseconcepts.Every
inadditiontothestrategiesofriskmanagement. one of them functions as a part of the previous
| B. TypesofFraudDetectionTechniques |     |     |     | work. |     |
| ---------------------------------- | --- | --- | --- | ----- | --- |
Thetechniquesbasedondataanalysisaregenerally
| applied to detect | fraud. The | particular approaches |     |     |     |
| ----------------- | ---------- | --------------------- | --- | --- | --- |
Figure3:CountNested
In other words, artificial intelligence includes the than three layers. The detection techniques as
| field of machine | learning.         | The algorithms | of deep | givenbelow, |     |
| ---------------- | ----------------- | -------------- | ------- | ----------- | --- |
| learning which   | is the foundation | of the         | neural  |             |     |
networks and these are the branch of machine a) ArtificialImmuneSystem(AIS)
learning. In actuality, the neural network depth, The data mining strategy is the artificial immune
the node layers having wide variety that splits it systems which detects antigens through mimicking
from a deep learning approach are requires greater the biological immune system behavior [56]. The
| https://sesjournal.com |     | |Kashif | & Naseer,2025| |     | Page388 |
| ---------------------- | --- | ------- | -------------- | --- | ------- |

| ISSN (e)3007-3138 |     | (p) 3007-312X |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
artificial immune system may imitate a wide range defining how they interact with another epidemic
of biological traits, but the majority of them cells in the system. In general, it has deleted and
revolve around the detector cells formation and leaving the remaining capable of detecting
| having potential          |     | capability | to         | recognize |           | external | intruders[57]. |     |     |     |     |     |
| ------------------------- | --- | ---------- | ---------- | --------- | --------- | -------- | -------------- | --- | --- | --- | --- | --- |
| things.Thecellsofdetector |     |            | arecreated |           | atrandom, |          |                |     |     |     |     |     |
and reproduction is used to check and assess their b) NeuralNetwork(NN)
efficacy, in comparable with how other This is a computer model of the human brain
classificationsystemstrain. which is named as neural network that represents
Clonal selection is a typical kind that produces the neuronal and synapsis using the vertices and edges
cells of detector which at most exist for the brief graphs [3]. The network works by modeling the
period. When a cell identifies an antibody that enter variables as a layer of vertices after which
lives longer to combat the invader and can makinguse of a weight toevery linkwithinsidethe
transform such as an outcome of the battle. The graph, whereas the ultimate vertices are located at
cells that survive after the imitation are the finest distinctive layers primarily based totally on their
prepared to recognize the antitoxins. Negative distance from the enter nodes [58] as shown in
| selection   | is one | more   | frequent  | method |       | that the | Figure4. |     |     |     |     |     |
| ----------- | ------ | ------ | --------- | ------ | ----- | -------- | -------- | --- | --- | --- | --- | --- |
| whole thing | at     | random | producing |        | cells | and      |          |     |     |     |     |     |
Figure4:SimpleNeuralNetwork
Eachnodebasesitsinputontheassociatedvertices been decreased to an acceptable level or a
to it preceding layer. The received signal through predefined iteration limit has remained achieved.
eachneuron isgivenby Followingiteration,thenetwork'sperformancecan
|     |     |     |     |     |     |     | be evaluated |     | using a | set of | validation | data [3]. |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------ | ---------- | --------- |

|     |     |     |     |     |     |     | Overtraining |     | is a | typical |     | issue through |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ------- | --- | ------------- |
Where showsthelinkweightofneurons      and backpropagation the neural network, causing the
|     |     | =   |     | ×   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and represents the input. If the result exceeds network to emphasis on trends specific to the set
|           |            |     |          |        |       |     |     |     |     |     |     |     |
| --------- | ---------- | --- | -------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| a certain | threshold, | the | existing | neuron | fires | and |     |     |     |     |     |     |
oftrainingdataratherthanbroaderchallenge[59].
|           |                              |               |     |        |     |         |     |     |     |     |     |     |
| --------- | ---------------------------- | ------------- | --- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- |
| develo ps | aninputforthefollowinglayer. |               |     |        |     |         |     |     |     |     |     |     |
| Training  | a back                       | proliferation |     | neural |     | network |     |     |     |     |     |     |
c) GeneticAlgorithm(GA)
| involves | putting | trials from | the | training |     | data set |                |     |         |       |            |         |
| -------- | ------- | ----------- | --- | -------- | --- | -------- | -------------- | --- | ------- | ----- | ---------- | ------- |
|          |         |             |     |          |     |          | To iteratively |     | enhance | issue | solutions, | genetic |
through the system and compared the outcomes. algorithms employ the notion of resident
| At each     | edge      | weights    | are | generally |     | selected |              |         |          |                 |     |                   |
| ----------- | --------- | ---------- | --- | --------- | --- | -------- | ------------ | ------- | -------- | --------------- | --- | ----------------- |
|             |           |            |     |           |     |          | development. |         | It works | by establishing |     | a beginning       |
| arbitrarily | for first | iteration, | and | when      | the | results  |              |         |          |                 |     |                   |
|             |           |            |     |           |     |          | group at     | random, | then     | repeatedly      |     | replicating every |
are computed, every weight is lightly changed resident utilizing various methods and choosing
| through | the following | sequence |     | [59]. | The | process |           |           |     |      |       |           |
| ------- | ------------- | -------- | --- | ----- | --- | ------- | --------- | --------- | --- | ---- | ----- | --------- |
|         |               |          |     |       |     |         | survivors | depending |     | upon | their | strength. |
is repeated until either the network's error has Reproduction is accomplished by taking two
| https://sesjournal.com |     |     |     |     | |Kashif | & Naseer,2025| |     |     |     |     |     | Page389 |
| ---------------------- | --- | --- | --- | --- | ------- | -------------- | --- | --- | --- | --- | --- | ------- |

| ISSN (e)3007-3138 |     | (p) 3007-312X |     |     |     |     |     |
| ----------------- | --- | ------------- | --- | --- | --- | --- | --- |
exitinggenerationparentsandemployingcrossover level of strength. The method finishes when it
ondualplaces,atthattimearbitrarilytransforming achieves the desired strength, even though to
a individual element of the resultant successors. A prevent indefinite looping, a limit on the number
fitnessfunction isused toassessthecapacityof the ofiterationscanbestated,asillustratedinFigure5.
offspring, and the results determine whose parents Similar to neural networks,genetic algorithms may
and kids are chosen as the future generation's uncover underlying correlations among the data
representatives.Theproportionofsamplesthatthe without the need for advance information of the
kids properly classify can be utilized to gauge their issuedomain.[60].
Figure5:FlowchartofGeneticAlgorithmProcess
d) HiddenMarkovModel(HMM) this setup, launch the bank server and the HMM
The is a statisticalmodel named as hidden markov server first. When a transaction is initiated by the
model in which the represented system is believed client, HMM begins watching and comparing the
to remain a markov process through an unseen process. If fraud is detected, the transaction is
state [61]. It detects fraud by analyzing user stopped. The user responds with a password on a
spending profiles, which are classified into three cellphone through Bluetooth to the similar ATM
| types[62]: |     |     |     |     | ofbank,otherwise | via message/sms.Thepasskey | is  |
| ---------- | --- | --- | --- | --- | ---------------- | -------------------------- | --- |
I. lowerprofile validated for authorization, and the transaction is
II. middleprofile permitted. After three failed tries, the transaction
| III. higherprofile     |              |              |                |                | iscompletelyhalted. |     |         |
| ---------------------- | ------------ | ------------ | -------------- | -------------- | ------------------- | --- | ------- |
| Figures                | 6 depict the | training and | detection      | and            |                     |     |         |
| preventive             | phases [63]  | [64] of      | the procedure. | In             |                     |     |         |
| https://sesjournal.com |              |              | |Kashif        | & Naseer,2025| |                     |     | Page390 |

| ISSN (e)3007-3138 | (p) 3007-312X |     |     |     |     |     |     |
| ----------------- | ------------- | --- | --- | --- | --- | --- | --- |
Figure6:FlowchartofTrainingandDetectionPhaseinHMM
e) BayesianBeliefNetwork(BBN) A network uses a classifier to calculate for
Astatisticalcategorization approachisthebayesian all possible classes and inserts into the class

beliefnetworkwhichemploysthetheoremofbayes, with the highest . In this way, t  he  n eχtwork

which is a way of determining the likelihood is demonstrated to  ca tegorize eachχsample into the
   sχtlikelytobelong[6].
having a given hypothesis is true. According to classtowhichiti sm o
theorem, the probability for a hypothesis . For A network may be represented graphically as a
example, may be categorized inside a certain type focused on acyclic graph, having nodes which is
|                 |     |     |              |        |           |              |     |
| --------------- | --- | --- | ------------ | ------ | --------- | ------------ | --- |
| thatspecifiedas |     |     | representing | trials | and edges | representing | a   |
χ fundamentalrelationshipamongthemasshownin
|     |     |      | Figure 7. | The absence | of missing   | edges may | thus |
| --- | --- | ---- | --------- | ----------- | ------------ | --------- | ---- |
|     | χ   | (  ) | be used   | to exhibit  | in which two | variables | are  |
 χ  =
 (χ) unrelatedofeachother[3].
Figure7:BNNGraphicalRepresentation
f) ClusterMethod(CM) approach used will be determined by the intended
The cluster method is the procedure of organizing outcome [65]. The clustering of k-means is a
information within classes of things that are alike. modest and effective approach to data clustering.
Several cluster algorithms existing in classes of the Figure 8 depicts the clustering-based approach's
dataset produce different grouping outcomes. The systemarchitecture[66].
| https://sesjournal.com |     | |Kashif | & Naseer,2025| |     |     | Page391 |     |
| ---------------------- | --- | ------- | -------------- | --- | --- | ------- | --- |

| ISSN (e)3007-3138 | (p) | 3007-312X |     |     |     |     |
| ----------------- | --- | --------- | --- | --- | --- | --- |
Figure8:SystemArchitectureofClusterMethod
Firstly, the parameters utilised in the programme, non-linear method is utilized. The mapping is
just like transaction award, credit/debit card intended to model comparable input vectors as
number, current transaction, transaction time, neurons which are nearer together in the final
mercantile group id, transaction category id and matrix, allowing the inputs to be seen. To group
transaction state, are declared. The validation the nodes, a distance or neighborhood function,
mechanism then verifies the accuracy of the just like the euclidean distance formula or the
transaction information. The previously prepared gaussian formula, is utilized [63]. The clustering
data tableisnowinserted within thedatabase.The function that each neuron is subjected to is
| information | that is being | removed          | from counter | providedby: |     |     |
| ----------- | ------------- | ---------------- | ------------ | ----------- | --- | --- |
| and now     | inserted to   | take transaction | info.        | The         |     |     |
transaction information is then produced row by Where represents the specific node present
|     |     |     |     |     | + 1 ep=res   +ts  th(e   p−re | − 1 t)input |
| --- | --- | --- | --- | --- | ----------------------------- | ----------- |
row using an array. Following that, the cluster is weighting, r en se n vector

labelled as down, up, or moderate dangerous. The and  r epresents the preferred the function of

current transaction information was obtained to distance. B e fore the process is finished, the

detect fraud or real transactions using the k-means cluste ring phase is repeated a predetermined
clustering method. Uncertainty, the transaction is numberoftimes[67].
| deceitful, | the notification | says "fraud | transaction," |     |     |     |
| ---------- | ---------------- | ----------- | ------------- | --- | --- | --- |
h) DecisionTree(DT)
orelseitwillsay"legaltransaction."
|     |     |     |     | Decision trees | are a classification | or prediction |
| --- | --- | --- | --- | -------------- | -------------------- | ------------- |
g) Self-OrganizingMap(SOM) approach that utilizes a tree with internal nodes
The main type of artificial neural network is self- reflecting binary options on characteristics and
organizing map that consists of a single neural branches expressing the result of that decision [59]
matrix. Inputs from a high-dimensional space are as shown in Figure 9. Now trial travels the tree, it
mapped to a two-dimensional array of neurons, a is segregated within the subsets though it is finally
categorizedwithinajointlyspecialsubclass.
Figure9:DecisionTreeRepresentation
| https://sesjournal.com |     |     | |Kashif | & Naseer,2025| |     | Page392 |
| ---------------------- | --- | --- | ------- | -------------- | --- | ------- |

ISSN (e)3007-3138 (p) 3007-312X
A decision forest, sometimes known as a random the same time as the opposite does not. This is a
foreststhatisadecisiontreecollectionintendedto significant difference and there are several factors
prevent the unstableness and risk of exaggerate in areas where one of the two approaches performs
which an individual tree may cause [5]. Random better than the other, although the two strategies
forests employ distinct training info among tree dodiffersomewhatfromoneanother.
andlimit thecharacteristicspoolpresentedtoeach
internal node at random [5]. Pruning is another a. SupervisedLearning
strategy for decreasing overfitting in decision trees, The supervised learning method to machine
which includes removing decision nodes without learning is prominent by the utilize of labelled
affecting the tree's overall accuracy [6]. These datasets. Classification and regression are two
approaches render random forest resistant to main types that may be used to classify supervised
exaggerate and noise. Because every tree is created learningwhenapplyingdatamining.
randomly, the computing complexity is minimal.
Furthermore, the only two factors that must be i) Classification
adjustedarethenumberoftreesandthecollection The Classification issues utilize an algorithm to
of characteristics from which to create each node, exactly distribute test data into various classes, just
makingdecision forestsstraightforwardtogenerate like distinctive among apples and oranges. An
[5]. alternative is to segregate spam from your email in
a separate folder using supervised learning
i) SuperVectorMachine(SVM) techniques. Decision trees, support vector
Support Vector Machines (SVM) are statistical machines,random forests, and linear classifiersare
learning approaches that have been successfully examplesofcommonclassificationapproaches.
used for a variety of issues. The essential idea
behind the SVM sorting method is to build a ii) Regression
hyperplane known the decision plane, maximizing An algorithm is utilized in regression, a distinct
the distance among the positive and negative supervised learning technique, to get the
modes [68]. SVM is a well-known machine relationship among dependent and independent
learning approach for sorting, regression, and parameters. Regression models are beneficial while
additional problems. LIB-SVM is a Support Vector expecting numbers based on a species of data
Machines library (SVM). LIBSVM is often used in sources, just like sales revenue estimations for a
two stages: first, setting a training sequence to particular organization. Logistic, linear and
generate a model. After that utilizing the model to polynomial regressions are a few mutual regression
guess information from a testing info set. The methods.
SVMhavemajorfunctionsareasfollows:
 First, set up the training information for b. UnsupervisedLearning
modeldevelopment. Unsupervised learning investigates and classifies
 Next, arrange SVM elements for the newly unlabeled statistical sets using machine learning
produceddatasetandreferittoSVMtraining. methods. Without the support of humans, these
 SVM Trainer, which trains every single data algorithms look for statistics that point to hidden
pointinthebigdataset. elegances. Clustering, association, and
 After the dataset has been entirely trained, dimensionality lessening were the three main
theSVMPredictorpredictsthelearneddata. functions applied in unsupervised learning
paradigms.
C. SupervisedandUnsupervisedLearning
There are important strategies utilized in machine i) Clustering
learning and artificial intelligence which are Unlabeled data may be characterized utilizing the
supervisedandunsupervisedlearning.Oneemploy statistics mining method, in which clusters objects
labelled data to support in outcome estimation, at only based upon their resemblances or alterations.
https://sesjournal.com |Kashif & Naseer,2025| Page393

| ISSN (e)3007-3138 |     | (p) | 3007-312X |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
K-means clustering approaches split associated dimensions).It mitigatestheinfoinputsvolume to
statistical elements within clusters based upon a well-behaved level whereas retaining the data
comparations, and the k-means identifies the integrity. This method is broadly utilized for pre-
dimensions and amount of granularity of the processing data, just like whenever autoencoders
clusters. Various parameters, consisting market enhancethevideoqualityofresultantimages.
| segmentation      |     | and image | reduction, |     | build | this |                    |                 |     |      |         |
| ----------------- | --- | --------- | ---------- | --- | ----- | ---- | ------------------ | --------------- | --- | ---- | ------- |
| tacticattractive. |     |           |            |     |       |      | D. FraudPrevention |                 |     |      |         |
|                   |     |           |            |     |       |      | Corporations       | and politicians |     | have | adopted |
ii) Association technologies like data analytics and artificial
The association shape of unsupervised learning intelligence to significantly reduce and even avoid
utilizes a diversity of measures to novelty the economic, social, and financial consequences
associations among parameters in a provided of fraud. Consequently, analysts and researchers
dataset. Both the marketplace basket evaluation eliminate barriers, discover and rank severity-based
and the "Customers who bought this item also alerts, and then present high-priority indications
bought" recommendation engine frequently utilize forfurtheranalysis.
thoseapproaches. Advances in fraud detection technology serve as a
|     |     |     |     |     |     |     | precise | and effective weapon |     | against | scammers. |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------------- | --- | ------- | --------- |
iii) DimensionalityReduction There are eight steps for fraud prevention as
Dimensionality reduction is a learning method showninFigure10.
| utilized when |     | a dataset | has excessive | properties |     | (or |     |     |     |     |     |
| ------------- | --- | --------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Figure10:FraudPreventionSteps
The fraud prevention strategy presents a high-level when these exposures have been recognized will it
plan for executing the Institution's fraud befeasibletotakecorrectiveactionand,ifpossible,
prevention policy. In view of the fact that the avoid or minimize the occurrence of fraud in the
| approach         | is the | supreme | important | factor    | of  | the | future. |     |     |     |     |
| ---------------- | ------ | ------- | --------- | --------- | --- | --- | ------- | --- | --- | --- | --- |
| fraud prevention |        | plan,   | it should | be simple |     | and |         |     |     |     |     |
realistic. The fraud risk management policy and b) FraudRiskOwnership
the fraud risk profile of the institution determine To some extent, all staff are accountable for
the fraud prevention approach. There are some managing fraud risk, although the Accounting
fraudpreventionstrategiesasfollows[69][70]. Officer / Authority has final accountability. Line
|     |     |     |     |     |     |     | managersin | certainareasof | theInstitution |     | maybe |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | -------------- | --- | ----- |
a) IdentificationandEvaluationofSensitive delegated authority by the Accounting Officer /
| Regions |     |     |     |     |     |     | Authority.TheAccountingOfficer/Authorityhas |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
To develop and implement a fraud prevention the authority to transfer responsibilities for fraud
strategy, the organization should firstly define risk management as well as the flow of operations
wherever fraud risks exist in the Institution's fromthestrategictotheoperationallevel.
| present                | operational | systems | and | processes. | Only |                |     |     |     |     |         |
| ---------------------- | ----------- | ------- | --- | ---------- | ---- | -------------- | --- | --- | --- | --- | ------- |
| https://sesjournal.com |             |         |     | |Kashif    |      | & Naseer,2025| |     |     |     |     | Page394 |

| ISSN (e)3007-3138 | (p) | 3007-312X |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c) PlanofAction success rate, the method used, and the fraud type
The Institution should define clear processes for analyzed. This classification will allow us to
dealing with control deficiencies as part of the illustrate patterns in existing research
response plan. The organization must establish methodologies. The study's objectives were to
clean reporting forms for scam. Scam reporting ascertain the operational response of various fraud
must be incorporated into the respond strategy or detection methods. We conducted a comparative
investigative policy. The rejoinder proposal must study on fraud detection methods to analyze the
includedefinetheactionsandpersonsinchargeof results. For comparison, we considered the most
eachresponseactivity. important parameters such as accuracy, speed, and
|     |     |     |     |     | cost. | A   | comparison | table | has been | created | to  |
| --- | --- | --- | --- | --- | ----- | --- | ---------- | ----- | -------- | ------- | --- |
d) TheLegalFramework compare different ATM card fraud detection
The necessary legislation for dealing with civil and mechanisms. Each of the ATM card fraud
criminal offences against the Institution should be detection techniques described in this study has its
defined and properly construed. It should be own set of benefits and drawbacks. Table 1 shows
obvious what defines a fraudulent or corrupt the comparison results obtained from this study
| behaviour. |     |     |     |     | [71],[72],[73],[74],[75],[76]. |       |          |     |             |     |         |
| ---------- | --- | --- | --- | --- | ------------------------------ | ----- | -------- | --- | ----------- | --- | ------- |
|            |     |     |     |     | This                           | study | examined | the | performance | of  | various |
e) CultureofAnti-Fraud ATM cards fraud detection techniques such as
The Accounting Officer / Authority should neural networks, genetic algorithms, Hidden
establish frameworks to promote and educate Markov models, Bayesian networks, decision trees,
stakeholders about the Institution's anti-fraud and clustering methods, support vector machines
anti-corruption culture. As part of an anti-fraud (SVM), and artificial immune systems. As a result,
strategy, management might be entrusted with the each method has benefits and drawbacks. At the
obligation of teaching other employees under their same time, the support vector machine has a low
supervisiononfraudandcorruption. detection speed and the artificial immune system
hasahighdetectionspeed.So,basedontheresults,
III. AnalysisandDiscussion the best method among these techniques is AIS,
We will categorize the financial fraud detection NN,GA,HMM,BBN,CN,SOM,DTandSVM.
| techniques | described | in this area | based on their |     |     |     |     |     |     |     |     |
| ---------- | --------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table1:BenefitsandDrawbacksofvariousFraudDetectionTechniques
| Techniques |     |     | Benefits |     |     |     | Drawbacks |     |     |     |     |
| ---------- | --- | --- | -------- | --- | --- | --- | --------- | --- | --- | --- | --- |
Artificial Immune System Self-organization, ease of In the NSA, extensive training
| (AIS) |     |     | integration | with      | other | systems, | is  | required. |     |     |     |
| ----- | --- | --- | ----------- | --------- | ----- | -------- | --- | --------- | --- | --- | --- |
|       |     |     | andfault    | tolerance |       |          |     |           |     |     |     |
NeuralNetworks (NN) High detection accuracy, High cost/data format
|     |     |     | portability, | andspeed |     |     | sensitivity |     |     |     |     |
| --- | --- | --- | ------------ | -------- | --- | --- | ----------- | --- | --- | --- | --- |
Genetic Algorithm (GA) Detection is inexpensive and Setup and operation require
|     |     |     | quick. |     |     |     | extensive |           | tool knowledge |     | and |
| --- | --- | --- | ------ | --- | --- | --- | --------- | --------- | -------------- | --- | --- |
|     |     |     |        |     |     |     | are       | difficult | tounderstand.  |     |     |
Hidden Markov Model Rapid detection. Low accuracy/incapability to
| (HMM) |     |     |     |     |     |     | handle | large | data | sets |     |
| ----- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---- | ---- | --- |
Bayesian BeliefNetwork (BBN) To operate, data must be Excessive training is required,
|                        |     |     | trained    | and a          | high | processing | and | BBN's         | are slower | to      | apply |
| ---------------------- | --- | --- | ---------- | -------------- | ---- | ---------- | --- | ------------- | ---------- | ------- | ----- |
|                        |     |     | speed is   | required.      | More | precise    | to  | newinstances. |            |         |       |
|                        |     |     | and faster |                | than | a neural   |     |               |            |         |       |
| https://sesjournal.com |     |     | |Kashif    | & Naseer,2025| |      |            |     |               |            | Page395 |       |

| ISSN (e)3007-3138 | (p) | 3007-312X |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
network.
Clusteringmethod (CN) Clustering assists in grouping Numerous non-fraudulent
|     |     |     | data into  | similar |        | clusters, | activities   | were             | mistakenly |        |
| --- | --- | --- | ---------- | ------- | ------ | --------- | ------------ | ---------------- | ---------- | ------ |
|     |     |     | allowing   | for     | simple | data      | identified   | as frauds.       |            | So, to |
|     |     |     | retrieval. |         |        |           | detect       | fraud accurately |            | and    |
|     |     |     |            |         |        |           | efficiently, | real data        | must       | be     |
available.
Self-Organizing Map (SOM) To reduce incredibly complex Requires neuron weights to be
|     |     |     | problems        | down | to       | easily | necessary       | and | sufficient | to  |
| --- | --- | --- | --------------- | ---- | -------- | ------ | --------------- | --- | ---------- | --- |
|     |     |     | interpreteddata |      | mappings |        | cluster inputs. |     |            |     |
Decision Tree(DT) High adaptability/ease of Each condition must be
|     |     |     | implementation |     |     |     | checked     | individually. |     | The     |
| --- | --- | --- | -------------- | --- | --- | --- | ----------- | ------------- | --- | ------- |
|     |     |     |                |     |     |     | transaction | condition     |     | is used |
|     |     |     |                |     |     |     | in fraud    | detection.    |     |         |
Support Vector Machine SVMs can be robust even if the Expensive/poor performance
(SVM) training sample is biased. when processing large datasets.
This paper presents a comparative study of various methods. The survey-based comparison of the
credit card fraud detection techniques. The mentionedapproachesintermsofparameterssuch
primary goal of this paper is to examine the as detection speed, accuracy,and the cost is shown
| methodology | of various | credit | card detection |     | inTable2. |     |     |     |     |     |
| ----------- | ---------- | ------ | -------------- | --- | --------- | --- | --- | --- | --- | --- |
Table2:ComparisonofvariousFraudDetectionTechniques
|     | Techniques |     | Detection |     | Accuracy |     | Cost |     |     |     |
| --- | ---------- | --- | --------- | --- | -------- | --- | ---- | --- | --- | --- |
Speed
|     | AIS |     | VeryFast |     | Good   |     | Inexpensive |     |     |     |
| --- | --- | --- | -------- | --- | ------ | --- | ----------- | --- | --- | --- |
|     | NN  |     | Fast     |     | Medium |     | Expensive   |     |     |     |
|     | GA  |     | Good     |     | Medium |     | Inexpensive |     |     |     |
|     | HMM |     | Fast     |     | Low    |     | High        |     |     |     |
Expensive
|                | BBN |     | VeryFast |     | High     |     | Expensive        |            |     |         |
| -------------- | --- | --- | -------- | --- | -------- | --- | ---------------- | ---------- | --- | ------- |
|                | CM  |     | High     |     | Medium   |     | Expensive        |            |     |         |
|                | SOM |     | Fast     |     | Medium   |     | Expensive        |            |     |         |
|                | DT  |     | Fast     |     | Medium   |     | Expensive        |            |     |         |
|                | SVM |     | Low      |     | Medium   |     | Expensive        |            |     |         |
| IV. Conclusion |     |     |          |     | capacity |     | of computational | approaches |     | such as |
Fraud detection is an essential component of the neural networks and support vector machines to
modern financial business. This study of the learn and adapt to new strategies is extremely
literature focused on research on statistical and usefulinfraudstersgrowingstrategies.
computational intelligence techniques for fraud The main objective of this work is to review
detection.Despitedifferencesineffectiveness,each various fraud detection methods. Fraud detection
approachwasdemonstratedtoberelativelycapable and prevention should be a key concern for every
of identifying various types of financial fraud. The company. A well-planned and implemented fraud
| https://sesjournal.com |     |     | |Kashif | & Naseer,2025| |     |     |     |     | Page396 |     |
| ---------------------- | --- | --- | ------- | -------------- | --- | --- | --- | --- | ------- | --- |

ISSN (e)3007-3138 (p) 3007-312X
detection system may lower the likelihood of fraud References
occurring inside a company dramatically. https://legaljobs.io/blog/credit-card-fraud-statistics/-
Furthermore, the quick discovery of fraud has a JeniferKuadli-2022
direct beneficial impact on the firm by lowering https://www.fool.com/the-ascent/research/identity-
future potential losses. AI and statistical data theft-credit-card-fraud-statistics/ - Lyle Daly
analysis are effective detection approaches that act andJackCaporal,2022.
as a deterrent to potential scammers. As legal NgaiE.,HuY.,WongY.,ChenY.,andSunX.,“The
requirements and regulatory demands have application of data mining techniques in
increased, it has become more critical to create an financial fraud detection: A classification
effective fraud detection and prevention program. framework and an academic review of
All the fraud detection techniques presented in literature,” Decision Support Systems 50, 559-
this project have both strengthsand disadvantages. 69,2011.
Some approaches have a high detection speed but Zhou W. and Kapoor G., “Detecting evolutionary
a low accuracy. Some approaches offer high financial statement fraud,” Decision Support
accuracybutareprohibitivelycostly. Systems50,570-5,2011.
Bhattacharyya S., Jha S., Tharakunnel K., and
V. FutureWorkandChallenges Westland J. C., “Data mining for credit card
Although data-driven artificial intelligence systems fraud: A comparative study,” Decision Support
have demonstrated remarkable performance in the Systems50,602-13,2011.
detection of financial fraud, significant concerns Kirkos E., Spathis C. and Manolopoulos Y., “Data
remain unresolved as financial fraud schemes mining techniques for the detection of
evolve toadapttothisnewdigitalenvironment.As fraudulent financial statements,” Expert
follows, wepresenttheprimaryproblemsandoffer
SystemswithApplications32,995-1003,2007.
future work directions from task-oriented, data-
NgaiE.,Hu Y., Wong Y.,ChenY.and Sun X.,“The
oriented,andmodel-orientedperspectives.
application of data mining techniques in
 Financialfraudisbecomingmoredifficultto financial fraud detection: A classification
detectduetoitsincreasingsecrecyandcomplexity.
framework and an academic review of
 The secrecy of financial fraud causes natural
literature,” Decision Support Systems 50, 559-
inaccuracyinsampling.
69,2011.
 The intricacy of financial processes
Quah J. T. and Sriganesh M., “Real-time credit card
necessitates the involvement of large amounts of
fraud detection using computational
data.
intelligence,” Expert Systems with Applications
 The amount of financial data available for
35,1721-32,2008.
frauddetectionisvast,yetitisdispersed.
Yeh I. and Lien C. H. “The comparisons of data
 Data isolation is a challenging problem to
mining techniques for the predictive
address.
accuracy of probability of default of credit
 Model training is made more difficult by
card clients,” Expert Systems with Applications
large-scaledataprocessing.
36,2473-80,2009.
 Models for detecting financialfraud must be
Sánchez D., Vila M., Cerda L. and Serrano J. M.,
moreadaptableandinterpretable.
“Association rules applied to credit card
 Theissueofmodelbiasmustbeaddressed.
fraud detection,” Expert Systems with
 Robustnessshouldbeimproved.
Applications36,3630-40,2009.
 Improvedinterpretabilityisrequired.
Panigrahi S, Kundu A, Sural S, and Majumdar AK,
“Credit card fraud detection: A fusion
approach using Dempster Shafer theory and
Bayesian learning,” Information Fusion 10,
354-63,2009.
https://sesjournal.com |Kashif & Naseer,2025| Page397

| ISSN | (e)3007-3138 |     | (p) | 3007-312X |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Duman E. and Ozcelik M.H., “Detecting credit card Bolton R. J. and Hand D. J., “Statistical fraud
|     | fraud          | by     | genetic | algorithm |      | and          | scatter |                                              |            |     |            |     | Statistical | Science |      |
| --- | -------------- | ------ | ------- | --------- | ---- | ------------ | ------- | -------------------------------------------- | ---------- | --- | ---------- | --- | ----------- | ------- | ---- |
|     |                |        |         |           |      |              |         |                                              | detection: |     | A review,” |     |             |         | 235- |
|     | search,”       | Expert |         | Systems   | with | Applications | 38,     |                                              | 49,2002.   |     |            |     |             |         |      |
|     | 13057-63,2011. |        |         |           |      |              |         | BoltonR.J.andHandD.J.,“Unsupervisedprofiling |            |     |            |     |             |         |      |
Ravisankar P.,RaviV., Raghava RaoG., andBoseI., methods for fraud detection,” Credit Scoring
“Detection of financial statement fraud and andCreditControlVII235-55,2001.
feature selection using data mining Rezaee Z., “In Financial statement fraud: prevention and
|     | techniques,” |     | Decision | Support |     | Systems | 50, 491- |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | -------- | ------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
detection,”Vol.pp.JohnWiley&Sons,2002.
|     | 500,2011. |     |     |     |     |     |     | Kou | Y., Lu | C. T., | Sirwongwattana |     | S., | and Huang | Y.  |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------------- | --- | --- | --------- | --- |
Judith Hurwitz, Alan Nugent, Fern Halper, and P., “Survey of fraud detection techniques,”
|     | Marcia | Kaufman, |     | “How | Big | Data | Analytics |     |     |             |     |         |     |          |      |
| --- | ------ | -------- | --- | ---- | --- | ---- | --------- | --- | --- | ----------- | --- | ------- | --- | -------- | ---- |
|     |        |          |     |      |     |      |           |     | In  | Networking, |     | sensing | and | control, | IEEE |
Can Prevent Fraud,” chapter 22, page 260. international conference on. (ed.), Vol. 2, pp.
|     | Big Data | for | Dummies. |     | John | Wiley | & Sons, |     | 749-54,IEEE,2004. |     |     |     |     |     |     |
| --- | -------- | --- | -------- | --- | ---- | ----- | ------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
2013.
|     |     |     |     |     |     |     |     | Vatsa | V., | Sural S., | and | Majumdar |     | AK., “A | game |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | --- | -------- | --- | ------- | ---- |
Richard J. Bolton and David J. Hand, “Statistical theoretic approach to credit card fraud
Fraud Detection: A Review,” Journal of detection,” In Information Systems Security.
StatisticalScience,17:235-255,2002.
Vol.pp.263-76.Springer,2005.
Yue D., Wu. X., Wang Y., Li Y., and Chu C. H, “A Yang W. S. and Hwang S. Y., “A process mining
|     | review          | of  | data mining |            | based | financial | fraud    |     |           |     |         |           |        |               |      |
| --- | --------------- | --- | ----------- | ---------- | ----- | --------- | -------- | --- | --------- | --- | ------- | --------- | ------ | ------------- | ---- |
|     |                 |     |             |            |       |           |          |     | framework |     | for the | detection |        | of healthcare |      |
|     | detection       |     | research,”  |            |       | In        | Wireless |     |           |     |         |           |        |               |      |
|     |                 |     |             |            |       |           |          |     | fraud     | and | abuse,” |           | Expert | Systems       | with |
|     | Communications, |     |             | Networking |       | and       | Mobile   |     |           |     |         |           |        |               |      |
Applications31,56-68,2006.
Computing, WiCom. International Conference Pinquet J., Ayuso M., and Guillen M., “Selection
on.(ed.),Vol.pp.5519-22,IEEE,2007.
|       |           |           |        |          |     |         |           |     | bias     | and     | auditing | policies |               | for insurance |          |
| ----- | --------- | --------- | ------ | -------- | --- | ------- | --------- | --- | -------- | ------- | -------- | -------- | ------------- | ------------- | -------- |
| Hoogs | B., Kiehl | T,        | Lacomb | C.,      | and | Senturk | D., “A    |     |          |         |          |          |               |               |          |
|       |           |           |        |          |     |         |           |     | claims,” | Journal | of       | Risk     | and Insurance |               | 74, 425- |
|       | genetic   | algorithm |        | approach |     | to      | detecting |     |          |         |          |          |               |               |          |
40,2007.
|     | temporal |     | patterns | indicative |     | of  | financial |     |     |     |     |     |     |     |     |
| --- | -------- | --- | -------- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ViaeneS.,AyusoM.,GuillenM.,VanGheelD.,and
statement fraud,” Intelligent Systems in Dedene G., “Strategies for detecting
Accounting, Finance and Management 15, 41- fraudulent claims in the automobile
56,2007.
|       |     |      |        |     |     |     |        |     | insurance |     | industry,” |     | European | Journal | of  |
| ----- | --- | ---- | ------ | --- | --- | --- | ------ | --- | --------- | --- | ---------- | --- | -------- | ------- | --- |
| Zhang | G., | Eddy | Patuwo | B., | and | Y.  | Hu M., |     |           |     |            |     |          |         |     |
OperationalResearch176,565-83,2007.
“Forecasting with artificial neural networks: Bose I. and Wang J., “Data mining for detection of
|     | The | state | of the | art,” | International |     | journal of |     |           |     |           |     |       |     |         |
| --- | --- | ----- | ------ | ----- | ------------- | --- | ---------- | --- | --------- | --- | --------- | --- | ----- | --- | ------- |
|     |     |       |        |       |               |     |            |     | financial |     | statement |     | fraud | in  | Chinese |
forecasting14,35-62,1998. Companies,” International Conference on
Sohl J. E. and VenkatachalamA., “A neural network Electronic Commerce, Administration,
|     | approach |     | to forecasting |     | model | selection,” |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | -------------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SocietyandEducation,HongKong,2007.
Information&Management29,297-303,1995. Bai B., Yen J., and Yang X., “False financial
Fraser I. A., Hatherly D. J., and Lin K. Z., “AN statements: characteristics of China's listed
|     | EMPIRICAL |     | INVESTIGATIONOF |     |     |     | THE |     |           |     |          |     |           |            |     |
| --- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | --------- | ---------- | --- |
|     |           |     |                 |     |     |     |     |     | companies |     | and CART |     | detecting | approach,” |     |
USE OF ANALYTICAL REVIEW BY International Journal of Information Technology
EXTERNAL AUDITORS,” The British &DecisionMaking7,339-59,2008.
AccountingReview29,35-47,1997.
|     |     |     |     |     |     |     |     | Bermúdez |     | L., Pérez | J., Ayuso |     | M., Gómez |     | E., and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | --------- | --- | --------- | --- | ------- |
Fanning K. M. and Cogger K. O., “Neural network VázquezF.,“ABayesiandichotomous model
detection of management fraud using with asymmetric link for fraud in
|     | published |     | financial |     | data,” | International |     |     |             |     |            |     |             |     |     |
| --- | --------- | --- | --------- | --- | ------ | ------------- | --- | --- | ----------- | --- | ---------- | --- | ----------- | --- | --- |
|     |           |     |           |     |        |               |     |     | insurance,” |     | Insurance: |     | Mathematics |     | and |
Journal of Intelligent Systems in Accounting, Economics42,779-86,2008.
Finance&Management7,21-41,1998. Wu S. X. and Banzhaf W., “Combatting financial
|                        |     |     |     |     |     |         |                |     | fraud: | a   | coevolutionary |     | anomaly | detection |     |
| ---------------------- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------ | --- | -------------- | --- | ------- | --------- | --- |
| https://sesjournal.com |     |     |     |     |     | |Kashif | & Naseer,2025| |     |        |     |                |     |         | Page398   |     |

| ISSN | (e)3007-3138 |     | (p) 3007-312X |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
approach,” In Proceedings of the 10th annual SahinY.,BulkanS.,andDuman E.,“Acost-sensitive
|     |            |     |            |     |              |     |     | decision |     | tree approach |     | for fraud | detection,” |     |
| --- | ---------- | --- | ---------- | --- | ------------ | --- | --- | -------- | --- | ------------- | --- | --------- | ----------- | --- |
|     | conference |     | on Genetic | and | evolutionary |     |     |          |     |               |     |           |             |     |
computation. (ed.), Vol. pp. 1673-80, ACM, Expert Systems with Applications 40, 5916-23,
|     | 2008. |     |     |     |     |     |     | 2013. |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Holton C., “Identifying disgruntled employee Dong W., Liao S. S., Fang B., Cheng X., Chen Z.,
systems fraud risk through text mining: A and Fan W., “The Detection of Fraudulent
simple solution for a multi-billion-dollar Financial Statements: An Integrated
LanguageModel,”2014.
problem,”DecisionSupportSystems46,853-64,
|     | 2009. |     |     |     |     |     | Olszewski |     | D., “Fraud | detection |     | using | self-organizing |     |
| --- | ----- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --------- | --- | ----- | --------------- | --- |
WhitrowC.,HandD.J.,JuszczakP.,WestonD.,and map visualizing the user profiles,” Knowledge
Adams N. M., “Transaction aggregation as a BasedSystems,2014.
strategy for credit card fraud detection,” Soltani Halvaiee N. and Akbari M. K., “A novel
Data Mining and Knowledge Discovery 18, 30- model for credit card fraud detection using
|     | 55,2009. |     |     |     |     |     |     | Artificial |     | Immune | Systems,” |     | Applied | Soft |
| --- | -------- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | --------- | --- | ------- | ---- |
CecchiniM.,Aytug H.,KoehlerG. J.,andPathakP., Computing,2014.
“Making words work: Using financial text as West J., Bhattacharya M. and Islam R., “Intelligent
a predictor of financial events,” Decision Financial Fraud Detection Practices: An
SupportSystems50,164-75,2010. Investigation”, 10th International
Humpherys S. L., Moffitt K. C., Burns M. B., Conference on Security and Privacy in
|     | Burgoon |     | J. K., and | Felix | W.  | F., |     | CommunicationNetworks,2014. |     |     |     |     |     |     |
| --- | ------- | --- | ---------- | ----- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
“Identification of fraudulent financial Singh, P. and Singh, M., “Fraud Detection by
statements using linguistic credibility Monitoring Customer Behavior and
analysis.,”DecisionSupport Systems50,585-94, Activities,” International Journal of Computer
|     | 2011. |     |     |     |     |     |     | Applications,111,23-32,2015. |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
Glancy F. H. and Yadav S. B., “A computational Sonawane,Y.B.,Gadgil,A.S., More,A.E.andJathar,
model for financial reporting fraud N.K., “Credit Card Fraud Detection Using
detection,” Decision Support Systems 50, 595- Clustering Based Approach,” International
|      | 601,2011.  |      |                |     |             |     |     | Journal | of  | Advance | Research |     | and Innovative |     |
| ---- | ---------- | ---- | -------------- | --- | ----------- | --- | --- | ------- | --- | ------- | -------- | --- | -------------- | --- |
| Jans | M., vander | Werf | J. M., Lybaert | N.  | and Vanhoof |     |     |         |     |         |          |     |                |     |
IdeasinEducation,2,1773-1776,2016.
K., “A business process mining application Gupta,Surbhi,Mrs.andNitimaMalsa.“CreditCard
for internal transaction fraud mitigation,” Fraud Detection & Prevention – A Survey,”
|     | Expert | Systems | with Applications |     | 38, 13351-9, |     |     |                                  |     |         |     |            |          |     |
| --- | ------ | ------- | ----------------- | --- | ------------ | --- | --- | -------------------------------- | --- | ------- | --- | ---------- | -------- | --- |
|     |        |         |                   |     |              |     |     | International                    |     | Journal | for | Innovative | Research | in  |
|     | 2011.  |         |                   |     |              |     |     | Science&Technology,vol.1,4,2017. |     |         |     |            |          |     |
Wong N., Ray P., Stephens G. and Lewis L., Pumsirirat, A. and Liu, Y., “Credit Card Fraud
“Artificial immune systems for the detection Detection Using Deep Learning based on
of credit card fraud: an architecture, Auto-Encoder and Restricted Boltzmann
prototype and preliminary results,” Machine,” International Journal of Advanced
InformationSystemsJournal22,53-76,2012.
|       |        |        |           |       |     |       |     | Computer |     | Science | and Application, |     | 9,  | 18-25, |
| ----- | ------ | ------ | --------- | ----- | --- | ----- | --- | -------- | --- | ------- | ---------------- | --- | --- | ------ |
| Huang | S. Y., | “Fraud | Detection | Model | by  | Using |     | 2018.    |     |         |                  |     |     |        |
Support Vector Machine Techniques,” Rahman, M. and Saha, A., “A Comparative Study
JDCTA:InternationalJournalofDigitalContent and Performance Analysis of ATM Card
TechnologyanditsApplications7,32-42,2013. Fraud Detection Techniques,” Journal of
Zaki M. and Theodoulidis B., “Analyzing Financial InformationSecurity,10,188-197,2019.
|     | Fraud | Cases | Using a Linguistics |     | Based | Text |        |     |           |         |     |        |      |       |
| --- | ----- | ----- | ------------------- | --- | ----- | ---- | ------ | --- | --------- | ------- | --- | ------ | ---- | ----- |
|     |       |       |                     |     |       |      | Pooja, | Dr. | Ashlesha, | "Review | on  | Credit | Card | Fraud |
Mining Approach,” Available at SSRN Detection using Machine Learning Algorithms,"
|     | 2353834,2013. |     |     |     |     |     |     | International |     | Journal | of  | Computer | Trends | and |
| --- | ------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --- | -------- | ------ | --- |
Technology,68.6,77-81,2020.
| https://sesjournal.com |     |     |     |     | |Kashif | & Naseer,2025| |     |     |     |     |     |     | Page399 |     |
| ---------------------- | --- | --- | --- | --- | ------- | -------------- | --- | --- | --- | --- | --- | --- | ------- | --- |

ISSN (e)3007-3138 (p) 3007-312X
Panda, A., Yadlapalli, B., & Zhou, Z., “Credit card Bhingarde, A., Bangar, A., Gupta, P. and Karambe,
fraud detection through machine learning S., “Credit Card Fraud Detection Using
algorithm,” Big data and computing visions, 1 Hidden Markov Model,” International
(3),140-145,2021. Journal of Advanced Research in Computer
B. Jiang and Y. Mu, "Russian Doll Network: and Communication Engineering, 4, 169-
Learning Nested Networks for Sample- 170,2015.
Adaptive Dynamic Inference," 2021 Vaishali, “Fraud Detection in Credit Card by
IEEE/CVF International Conference on Clustering Approach,” International Journal
Computer Vision Workshops (ICCVW), pp. ofComputerApplications,98,29-32,2014.
336-344,2021. Sonawane,Y.B.,Gadgil,A.S., More,A.E.andJathar,
WuSXandBanzhafW,“Combattingfinancialfraud: N.K., “Credit Card Fraud Detection Using
a coevolutionary anomaly detection Clustering Based Approach,” International
approach,” In Proceedings of the 10th annual Journal of Advance Research and Innovative
conference on Genetic and evolution-ary IdeasinEducation,2,1773-1776,2016.
computation. (ed.), Vol. pp. 1673-80, ACM, Quah JT and Sriganesh M, “Real-time credit card
2008. fraud detection using computational
Soltani Halvaiee N and Akbari MK,” A novel model intelligence,” Expert Systems with Applications
for credit card fraud detection using 35,1721-32,2008.
Artificial Immune Systems,” Applied Soft Olszewski D, “Fraud detection using self-organizing
Computing,2014. map visualizing the user profiles,” Knowledge-
Koh HC and Low CK, “Going concern prediction BasedSystems,2014.
using data mining techniques,” Managerial S.SurbhiandD.S.Kumar,"FraudDetectionDuring
AuditingJournal19,462-76,2004. Money Transaction and Prevention," 2019
Zhang D and Zhou L, “Discovering golden nuggets: International Conference on Issues and
datamininginfinancialapplication,”Systems, Challenges in Intelligent Computing Techniques
Man, and Cybernetics, Part C: Applications and (ICICT),pp.1-4,2019.
Reviews, IEEE Transac-tions on 34, 513-22, S. Hoyer, H. Zakhariya, T. Sandner and M. H.
2004. Breitner, "Fraud Prediction and the Human
Su, Jianhai & Havens, Timothy., “Fuzzy community Factor: An Approach to Include Human
detection in social networks using a genetic Behavior in an Automated Fraud
algortihm.” IEEE International Conference Audit," 2012 45th Hawaii International
on Fuzzy Systems. 2039-2046. Conference on System Sciences, 2012, pp. 2382-
10.1109/FUZZ-IEEE.2014.6891611,2014. 2391,2018.
Sonawne,V.D.,Gupta,P.,Raut,A.andSaudagar,F., Zareapoor, M., Seeja, K.R. and Alam, M.A.,
“ATM Card Fraud Detection Using Hidden “Analysis of Credit Card Fraud Detection
Markov Model,” International Journal of Techniques: Based on Certain Design
Innovative Research in Computer and Criteria,” International Journal of
Communication Engineering, 4, 8742-8747, ComputerApplications,52,35-42,2012.
2016. Kumari, S. and Choubey, A. “A Review on Various
Patidar, R. and Sharma, L., “Credit Card Fraud TechniquesandApproachesforCreditCard
Detection Using Neural Network,” Fraud Detection,” International Journal of
International Journal of Soft Computing Scientific Research Engineering &
andEngineering,1,32-38,2011. Technology,6,485-489,2017.
Mhamane, S.S. and Lobo, L.M.R.J., “Use of Hidden Bhatia, S., Bajaj, R. and Hazari, S., “Analysis of
Markov Model as Internet Banking Fraud Credit Card Fraud Detection Techniques,”
Detection,” International Journal of International Journal of Science and
ComputerApplications,45,5-10,2012. Research,5,1302-1307,2016.
https://sesjournal.com |Kashif & Naseer,2025| Page400

| ISSN   | (e)3007-3138 | (p) 3007-312X |        |           |     |     |     |
| ------ | ------------ | ------------- | ------ | --------- | --- | --- | --- |
| Singh, | P. and       | Singh, M.,    | “Fraud | Detection |     | by  |     |
|        | Monitoring   | Customer      |        | Behavior  |     | and |     |
|        | Activities,” | International |        | Journal   |     | of  |     |
ComputerApplications,111,23-32,2015.
| Pumsirirat, | A.           | and Liu, Y.,  | “Credit    | Card      | Fraud |     |     |
| ----------- | ------------ | ------------- | ---------- | --------- | ----- | --- | --- |
|             | Detection    | Using Deep    | Learning   |           | based | on  |     |
|             | Auto-Encoder | and           | Restricted | Boltzmann |       |     |     |
|             | Machine,”    | International |            | Journal   |       | of  |     |
|             | Advanced     | Computer      |            | Science   |       | and |     |
Applications,9,18-25,2018.
| Gupta, | S. and        | Malsa, N.        | “Credit       | Card       | Fraud    |     |     |
| ------ | ------------- | ---------------- | ------------- | ---------- | -------- | --- | --- |
|        | Detection     | and Prevention—A |               |            | Survey,” |     |     |
|        | International | Journal          | for           | Innovative |          |     |     |
|        | Research      | in Science       | & Technology, |            | 4,1-7,   |     |     |
2017.
| https://sesjournal.com |     |     |     | |Kashif |     | & Naseer,2025| | Page401 |
| ---------------------- | --- | --- | --- | ------- | --- | -------------- | ------- |