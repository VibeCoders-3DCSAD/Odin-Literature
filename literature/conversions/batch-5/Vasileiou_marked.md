---
conversion_metadata:
  converted_at: "2026-07-21T09:09:35Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Vasileiou.pdf"
  source_pdf_sha256: "cc492cee9df09ee59ee9376d221de78455ed055450231a302062c8f4864453e3"
  page_count: 9
  markdown_char_count: 136929
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

A Logic-based Framework for Explainable Agent
Scheduling Problems
Stylianos Loukas Vasileioua;*, Borong Xua and William Yeoha

aWashington University in St. Louis

Abstract. Agent Scheduling Problems (ASPs) are common in var-
ious real-world situations, requiring explainable decision-making
processes to effectively allocate resources to multiple agents while
fostering understanding and trust. To address this need, this paper
presents a logic-based framework for providing explainable deci-
sions in ASPs. Speciﬁcally, the framework addresses two types of
queries: reason-seeking queries, which explain the reasoning behind
scheduling decisions, and modiﬁcation-seeking queries, which offer
guidance on making infeasible decisions feasible. Acknowledging
the importance of privacy in multi-agent scheduling, we introduce
a privacy-loss function that measures the disclosure of private in-
formation in explanations, enabling a privacy-preserving aspect in
our framework. By using this function, we introduce the notion of
privacy-aware explanations and present an algorithm for computing
them. Empirical evaluations demonstrate the effectiveness and ver-
satility of our approach.

1

Introduction

Agent scheduling problems (ASPs) involve allocating a ﬁnite set of
resources to multiple agents over a speciﬁc time frame. These prob-
lems are pervasive in real-world scheduling systems, ranging from
personnel shift assignments [34] to machine job allocation [38], and
even scheduling awake and asleep periods for Mars rovers [8]. Apart
from generating a schedule that allocates resources to agents, it is
crucial to ensure that both the schedule and the underlying decision-
making process are explainable. An agent may require an expla-
nation for why certain scheduling decisions were not satisﬁed or
why a schedule could not be generated at all. In such cases, un-
derstanding the reasons behind these issues is not only enlighten-
ing but also necessary for rectifying the problem. Additionally, pri-
vacy plays a signiﬁcant role due to the sensitive nature of personal
information that may be included in ASPs, such as agents’ con-
straints and preferences. Preserving privacy helps protect individ-
ual agents from potential discrimination or unauthorized access to
their information, fostering trust and willingness to participate in the
scheduling process. Therefore, incorporating explanation generation
modalities with privacy-preserving considerations into ASP systems
is highly desirable.

To address this need, this paper presents a logic-based framework
aimed at making ASPs explainable. The framework accommodates
two types of queries: reason-seeking queries, which clarify why a
scheduling decision was (or not) derived, and modiﬁcation-seeking

queries, which offer guidance on rendering infeasible scheduling de-
cisions feasible. Recognizing the importance of privacy in multi-
agent scheduling, we use the concept of agent access rights to dis-
tinguish between public and private information, and introduce a
straightforward privacy-loss function to quantify the amount of pri-
vate information disclosed in explanations. Using this function, we
then deﬁne the notion of privacy-aware explanations and present the
Query Understanding and Efﬁcient Response with Intelligible Ex-
planations of Schedules (QUERIES) algorithm for computing them.
This approach ensures that the explanations provided maintain the
conﬁdentiality of sensitive information while still offering valuable
insights into the scheduling decisions.

In summary, our

framework advances existing explainable
scheduling methods, which typically focus on speciﬁc scheduling
problems [1, 3, 28], by providing a general solution applicable to a
broader range of ASPs. Our main contributions are as follows:

•

•

•

We introduce a general logic-based explanation generation frame-
work for ASPs that addresses both reason-seeking queries and
modiﬁcation-seeking queries.
We propose a privacy-loss function to quantify the amount of pri-
vate information included in an explanation and deﬁne the concept
of privacy-aware explanations.
We present the QUERIES algorithm for computing explanations.
Empirical evaluations demonstrate the effectiveness and versatility
of our approach.

2 Motivating Thought Experiment

To better understand the challenges faced by agent scheduling prob-
lems and the importance of generating effective explanations, let us
engage in a thought experiment inspired by a simpliﬁed version of the
employee shift assignment problem [34]. Consider a scenario based
on the employee shift assignment problem [34]. In this scenario, an
automated scheduling agent named Alice is responsible for assign-
ing shifts to employees at a company. Speciﬁcally, there are three
shift types – morning, afternoon, and evening – and four employees
– Thanos, Irene, Vicky, and Rose – who need to be assigned shifts
over three days from Monday to Wednesday.

The scheduling problem consists of the following domain con-

straints:
C1: All employees must be assigned a total of two shifts.
C2: Employees cannot be assigned multiple shifts per day.
C3: No two employees can be assigned the same shift the same day.
C4: Employees cannot be assigned a morning shift right after an

∗ Corresponding Author. Email: v.stylianos@wustl.edu.

evening shift.

---

<!-- PAGE 2 -->

3 Background

We now provide some background on the satisﬁability (SAT) prob-
lem, a general agent scheduling problem (ASP) deﬁnition, and our
logic-based representation of that problem.

3.1

Satisﬁability

We assume familiarity with propositional logic. A knowledge base
KB is a set of constraints, where each constraint is built up recur-
sively from literals (i.e., variables or its negations) using the usual
logical connectives.

Satisﬁability (SAT) [9] is the prototypical NP-complete problem
of ﬁnding an assignment of truth values to variables in order to make
a knowledge base KB true. If there exists a truth value assignment µ
that makes KB true, then we say that µ is a model of KB and KB is
satisﬁable, otherwise KB is unsatisﬁable, denoted by KB
. A
KB entails a constraint ϕ, denoted KB
.
⊥
Partial weighted MaxSAT [24] is an extension of SAT in which
constraints are partitioned into hard and soft constraints, where each
soft constraints is given a weight. Hard constraints must always be
satisﬁed in a solution, whereas soft constraints may not. The goal of
MaxSAT is to ﬁnd an assignment that satisﬁes the hard clauses and
maximizes the sum of weights of the satisﬁed soft clauses.

= ϕ, iff KB
|

=
|
ϕ

∪ {¬

⊥
=

} |

3.2 Agent Scheduling Problem

In general, the goal of an agent scheduling problem (ASP) is to dis-
tribute a set of resources to a set of agents over a scheduling hori-
, where
zon. Formally, it can be deﬁned as a tuple
A
(cid:105)
m
n
A =
rj
i=1 is a set of agents, R =
j=1 is a set of resources,
}
}
{
h
S =
t=1 is a set of time steps, and C is a set of constraints that
}
consists of domain constraints, which are intrinsic and describe the
problem’s dynamics, as well as agent constraints, which are extrinsic
and describe the agents’ personal constraints.

A, R, S, C
(cid:104)

ai
{
st
{

=

A

A solution to an ASP

is a schedule Σ, that is an

S
|
matrix, where each cell Σ[i, j, t] = 1 if agent ai is assigned resource
rj at time step st and Σ[i, j, t] = 0 otherwise. A schedule is feasible
if all the domain constraints, which are treated as hard constraints,
are satisﬁed. A schedule is optimal if it is feasible and all the agent
constraints, which are treated as soft constraints, are maximized.

| × |

| × |

R

A

|

3.3 Logic-based Agent Scheduling Problems

A

A

as a logic-based problem, that
In this paper, we model an ASP
is, we encode
into a set of logical constraints for which satis-
ﬁability can be decided. By using an appropriate logical language,
the problem’s dynamics are encoded into a knowledge base KB
that expresses all the scheduling constraints that a desired schedule
should satisfy. Speciﬁcally, the knowledge base KB consists of do-
main constraints CD and agent constraints CA, where CD are treated
as hard constraints and CA as weighted soft constraints. As such, the
scheduling problem turns into a MaxSAT problem, where the quality
of a feasible schedule depends on the degree to which the soft clauses
are satisﬁed. The objective function of a candidate schedule is then
deﬁned as the sum of weights of satisﬁed soft constraints, and an
optimal schedule is the solution with the highest possible objective
value. A plethora of scheduling problems has been modeled using
logic-based approaches [2, 5, 10, 14, 18, 21, 23, 27].

For ease of presentation, in this paper we will use propositional
logic to encode ASPs. We formally deﬁne a logic-based ASP (L-
ASP) as follows:

Figure 1: Instance of the thought experiment with Alice and Thanos.

Moreover, each employee has personal constraints:
CT : Thanos wants only morning or afternoon shifts.
CI : Irene does not want evening shifts.
CV : Vicky wants the afternoon shift on Tue. and Wed.
CR: Rose wants the morning shift on Tue. and Wed.

Here, Alice’s objective is to ﬁnd a schedule that satisﬁes all do-
main constraints and, as much as possible, accommodates the em-
ployee constraints according to their weights, which in this example
are based on the employees’ seniority levels.

Let us assume that Alice ﬁnds a feasible schedule, but it does
not meet Thanos’ constraint of being assigned morning or afternoon
shifts. Thanos, in turn, may inquire about the reason for this assign-
ment. To generate an effective explanation, Alice needs a framework
that can generate explanations that are informative and tailored to the
speciﬁc needs of the explainee, that is, Alice must ﬁrst recognize the
nature of the explainee’s query.

In our thought experiment, Thanos’ query is a reason-seeking
query, as he wants to know “why” his constraint was unsatisﬁed in
the schedule. In response, Alice should provide a (reason-seeking)
explanation that identiﬁes the reasons behind her (scheduling) deci-
sion. For example, Alice might explain that due to the constraints of
the problem and the higher priority given to the preferences of Rose
and Vicky, it was not possible to assign Thanos morning shifts on
Tuesday or Wednesday without affecting the overall quality of the
allocation.

However, providing a reason-seeking explanation alone may not
be sufﬁcient in all scenarios. Suppose Alice could not create a fea-
sible schedule at all due to conﬂicting constraints. In this case, a
higher-level employee, such as a manager, may want to understand
“how” to adjust the scheduling problem to derive a feasible schedule.
This type of query is a modiﬁcation-seeking query, which requires an
explanation that helps the manager identify issues preventing a fea-
sible schedule and suggest potential modiﬁcations.

In addition to addressing these two types of queries, Alice’s expla-
nations should respect the privacy of the other employees. To achieve
this, Alice could only reveal information according to the employees’
access rights. In doing so, Alice distinguishes between public infor-
mation (information that can be revealed to employees with access
rights) and private information (information that cannot be revealed
to employees without access rights).

This thought experiment demonstrates some of the challenges of
generating explanations in the context of agent scheduling problems.
Indeed, in Section 4 we present an explanation generation frame-
work that can handle the complexity of the problem, account for the
explainee’s needs and access rights, and produce informative expla-
nations.

---

<!-- PAGE 3 -->

Figure 2: Overview of Our Explainable Logic-based Agent Scheduling Problem Pipeline.

∪

Deﬁnition 1 (L-ASP). An L-ASP is a tuple
where KB = CD

CA and:

=

(cid:104)

L

A, R, S, KB

,
(cid:105)

•

•

CD is the set of domain-speciﬁc (hard) constraints. These con-
straints are intrinsic to the problem and must be satisﬁed by a
solution.
CA = (cid:83)n
Each Ci =
ated with agent ai and wk is its corresponding weight.

i=1 Ci is the set of agent (weighted soft) constraints.
k is a constraint associ-

k=1, where each ci
l

(wk, ci

k)

{

}

A schedule can be derived by using off-the-shelf SAT solvers [4]
to search for a model µ of KB that satisﬁes all of the constraints
in CD and possibly some of the constraints in CA. If a model µ
exists, then a feasible schedule Σµ is derived by extracting from µ the
truth values of the variables corresponding to agents, resources, and
time steps. Otherwise, the scheduling problem is infeasible, i.e., no
feasible schedule exists. Finally, a schedule Σµ is deemed optimal if
a model µ exists and maximizes the cumulative sum of weights of
satisﬁed soft constraints in CA.

∪

Note that the knowledge base KB = CD

CA may be unsatis-
ﬁable due to inconsistencies in the domain constraints and/or agent
constraints. However, if a schedule Σµ exists, then that means that
Σµ logically follows from a satisﬁable subset KBµ
KB . In the
next section, we use KB to denote the knowledge base from which
explanations are derived. Depending on the context, KB could re-
fer to either a satisﬁable subset of the original knowledge base (i.e.,
KBµ) or the overall unsatisﬁable knowledge base.

⊆

4 Explainable Agent Scheduling Problems

We now present our explanation generation framework for agent
scheduling problems. We particularly address the following problem:

and a query ϕ
Given a logic-based L-ASP
=
with respect to KB , the goal is to ﬁnd an explanation for ϕ that
can be inferred from KB .

A, R, S, KB

L

(cid:104)

(cid:105)

As discussed in Section 2, we are interested in a framework that
can generate explanations for agent scheduling problems that are not
only informative but also tailored to the speciﬁc needs of the ex-
plainee. Such a framework should in principle:

•

Address two general types of queries: reason-seeking queries,
which aim to uncover why certain scheduling decisions were (or
not) made, and modiﬁcation-seeking queries, which focus on iden-
tifying potential modiﬁcations to the problem.

•

•

Generate informative and concise explanations for the two query
types.
Preserve the privacy of other agents by only revealing information
with respect to access-rights.
A general pipeline is shown in Figure 2. We now describe how to

generate explanations for the two query types.

4.1 Explaining Reason-Seeking Queries

A reason-seeking query, denoted by ϕr, aims to uncover why certain
scheduling decisions were made. Recall from Section 2 that Thanos
wants to know why Alice did not assign him only morning shifts.
Alternatively, a higher-level employee (e.g., a manager) may want to
understand why a feasible schedule cannot be generated.

To explain reason-seeking queries, we assume that KB

There are two possible scenarios to consider:

= ϕr.
|

•

•

∈

∈ ¬

CA (or ϕr

Agent Constraints in a Schedule: If the query ϕr captures an
unsatisﬁed (or satisﬁed) agent constraint in a schedule Σµ, then
CA).1 In this scenario, an explanation should
ϕr
identify the reasons why the constraint holds true with respect to
the schedule. Note that the knowledge base KB here is satisﬁable
(see Section 3.3).
Infeasible Scheduling Problems: If the query ϕr is aimed at cap-
turing why a problem is infeasible, i.e., why a feasible schedule
cannot be generated, then generally ϕr =
. In this case, the ex-
planation should identify the inconsistencies within the scheduling
constraints that lead to infeasible schedules. Note that the knowl-
edge base KB here is unsatisﬁable, i.e., there is no model of KB
from which a feasible schedule can be extracted.

⊥

Formally now, an explanation for a reason-seeking query is deﬁned
as follows:

Deﬁnition 2 (Reason-seeking Explanation). Given a knowledge
base KB that encodes an L-ASP
and a reason-seeking query ϕr,
L
we consider an explanation (cid:15)r
KB to be a reason-seeking expla-
nation for ϕr if:

⊆

= ϕr, meaning that the explanation (cid:15)r entails
|

•

•

(cid:15)r is sufﬁcient: (cid:15)r
the query ϕr.
(cid:15)r is minimal: For all proper subsets (cid:15)(cid:48)
r ⊂
that no smaller subset of (cid:15)r are sufﬁcient.

(cid:15)r, (cid:15)(cid:48)

r (cid:54)|

= ϕr, indicating

1 Note that ¬CA denotes the logical negation of all the constraints in CA.

---

<!-- PAGE 4 -->

These conditions ensure that the reason-seeking explanation is both
sufﬁcient and minimal in addressing the query.

4.2 Explaining Modiﬁcation-Seeking Queries

Modiﬁcation-seeking queries, denoted by ϕm, focus on identifying
potential modiﬁcations to a scheduling problem to address speciﬁc
issues. For example, Thanos may want to know how to incorporate
his unsatisﬁed constraint in Alice’s schedule, or a manager may seek
ways to adjust the scheduling problem to generate a feasible sched-
ule.

•

To explain modiﬁcation-seeking queries, we assume that KB
=
(cid:54)|
ϕm. Speciﬁcally, to explain these query types, we seek to identify a
set of constraints from the knowledge base KB that, when retracted,
= ϕm. Like before, there are two possible scenarios to consider:
KB
|
Unsatisﬁed Agent Constraints in a Schedule: If the query ϕm
concerns accommodating an unsatisﬁed agent constraint in a
schedule Σµ, then ϕm
Infeasible Scheduling Problems: If the query ϕm is aimed at ex-
plaining how a problem can be modiﬁed such that a feasible sched-
ule can be found, then ϕm =
.
(cid:62)
We now deﬁne an explanation for a modiﬁcation-seeking query as
follows:

CA.

∈

•

L

Deﬁnition 3 (Modiﬁcation-seeking Explanation). Given a knowl-
and a modiﬁcation-
edge base KB that encodes an L-ASP
seeking query ϕm, we consider an explanation (cid:15)m
KB to be a
modiﬁcation-seeking explanation for ϕm if:
(cid:15)m enables the entailment of ϕm: KB
= ϕm, meaning that
|
the query ϕm is entailed when the constraints in (cid:15)m are removed
from the knowledge base.
(cid:15)m is minimal: For all proper subsets (cid:15)(cid:48)
= ϕm,
indicating that no smaller subset of (cid:15)m can satisfy the query when
removed from the knowledge base.

(cid:15)(cid:48)
m (cid:54)|

(cid:15)m, KB

m ⊂

(cid:15)m

⊆

\

\

•

•

These conditions ensure that the modiﬁcation-seeking explanation is
both effective and minimal in addressing the query.

4.3 Privacy-Aware Explanations

It is reasonable to assume that individuals might prefer explanations
for scheduling decisions that only encompass public information, as
they could perceive these as more satisfying and equitable compared
to explanations that incorporate private information as well. To ex-
plore this possibility and incorporate potential privacy preferences
into our framework, we propose that agents have access rights on the
different pieces of information about the scheduling problem. Specif-
ically, we assume an access-rights function:

α : A

KB

0, 1

}

→ {

×

(1)

∈

that determines whether an agent ai
straint c

∈
KB , returning 1 if ai has access to c and 0 otherwise.

A has access rights to a con-

While we have motivated access rights through the lens of pri-
vacy, note that the function can also encode access rights through
other means as well (e.g., security clearances and other administra-
tive compartmentalization protocols).

Given an agent ai and the function α, we deﬁne the privacy loss ρi
of an explanation (cid:15) with regard to the agent as the count of constraints
inaccessible to it:

ρi((cid:15)) =

(cid:15)

|

| −

(cid:88)

α(ai, c)

c∈(cid:15)

(2)

Lastly, we deﬁne an explanation (cid:15)i as being privacy-aware in rela-
tion to agent ai and query ϕ if it incurs the least privacy loss among
all possible explanations E for the query ϕ:

(cid:15)i = argmin

ρi((cid:15))

(cid:15)∈E

(3)

4.4

Illustrating Example

∈

Consider the employee shift assignment problem presented in Sec-
tion 2. To represent the problem using (propositional) logic, we em-
R, and
ploy Boolean decision variables xi,j,t for all ai
st
S, where each variable is set to true if and only if agent ai is
assigned shift rj on day st. Otherwise, it is set to false. These vari-
ables comprise the domain constraints CD and agent constraints CA
which make up the knowledge base KB . Note that we assume the fol-
lowing weights for employee constraints CA: w(CR) = w(CV ) >
w(CT ) > w(CI ). 2

A, rj

∈

∈

•

}

¬

{¬

∨ ¬

∨ ¬

x1,1,2

x1,2,2

x1,1,2

x4,1,2,
{

Recall from Section 2 that Alice has generated a schedule (see
Figure 1) that does not satisfy Thanos’ constraint, prompting him to
ask Alice a reason-seeking query. In our logic-based framework, this
translates to the query ϕr =
. There are two
reason-seeking explanations for this query:
x4,1,2

(cid:15)r1 =
, stating that only one employee
}
can be assigned a morning shift on the same day (domain con-
straint) and that Rose’s preference was given a higher priority that
day.
(cid:15)r2 =
, stating that only one employee
}
can be assigned an afternoon shift on the same day (domain con-
straint) and that Vicky’s preference was given a higher priority that
day.
Now, assume that the access-rights function α is deﬁned such that
Thanos has access-rights to the domain constraints and Rose’s con-
straints, but not to the constraints of other agents. In this case, the pri-
vacy loss ρ1 of both explanations would be calculated as follows:

x3,2,2,
{

x3,2,2

x1,2,2

∨ ¬

¬

•

•

•

(cid:80)
c∈(cid:15)r1

(cid:80)
c∈(cid:15)r2

ρ1((cid:15)r1) =

(cid:15)r1

|

| −

α(1, c) = 2

−

2 = 0, since Thanos has

access to Rose’s information.
(cid:15)r2
ρ1((cid:15)r2) =

α(1, c) = 2

1 = 1, since Thanos does

|

| −

−
not have access to Vicky’s information.
As ρ1((cid:15)r1) < ρ1((cid:15)r2), the privacy-aware explanation in this case

would be (cid:15)r1.

5 QUERIES: Computing Explanations

We now present the Question Understanding and Efﬁcient Response
with Intelligible Explanations of Schedules (QUERIES) algorithm,
which generates privacy-aware explanations (cid:15)∗
i for reason-seeking
and modiﬁcation-seeking queries ϕ of an agent ai. The core of
QUERIES is based on reasoning via inconsistency. In particular, it
leverages a set of methods that are directly applicable to logic-based
explanation generation problems, namely, minimal unsatisﬁable sets
(MUS) and minimal correction sets (MCS) [25, 29], both of which
emerge when a set of clauses is unsatisﬁable. Particularly, an MUS

2 For more details on the encoding, please refer to the supplement available

at https://github.com/YODA-Lab/QUERIES.

---

<!-- PAGE 5 -->

Algorithm 1: QUERIES Algorithm
Input: KB , ϕ, ai, α, k
Result: privacy-aware explanation (cid:15) for ϕ for ai

1 forall c
2

KB do
if α(ai, c) = 1 then

∈

3

assign weight k to c

(cid:15)

4 if ϕ is a reason-seeking query then
5
6 else if ϕ is a modiﬁcation-seeking query then
7

getM U S(KB , ϕ)

getM CS(KB , ϕ)

←

(cid:15)

←
8 return (cid:15)

can be interpreted as explaining why a set of clauses is unsatisﬁ-
able by identifying a minimal set of conﬂicting clauses that cause the
unsatisﬁability. An MUS can then be used to ﬁnd a reason-seeking
explanation:

Proposition 1. Given a knowledge base KB and a reason-seeking
is a reason-seeking explanation for ϕr
query ϕr, (cid:15)r = M
if M is an MUS of KB
ϕr

\ {¬

ϕr

.

}
∪ {¬

}

=

ϕr

} |

∪ {¬

PROOF (SKETCH). The existence of a reason-seeking query ϕr im-
= ϕr, which in turn implies that KB
plies that KB
⊥
|
according to the deﬁnition of entailment. That is, the negation of ϕr
is inconsistent with a set of constraints from KB and, as such, an
MUS M of KB
is satisﬁable and M
reason-seeking explanation for ϕr.

ϕr
}
is a
(cid:50)
Similarly, an MCS explains how to restore consistency in an in-
consistent KB by identifying a minimal set of clauses from KB such
that when removed, KB becomes satisﬁable. A modiﬁcation-seeking
explanation can be then be generated via an MCS:

= ϕr. Therefore, M

}
ϕr
\ {¬

M , then M

\ {¬
ϕr
}

exists. If

∪ {¬

\ {¬

} |

ϕr

ϕr

¬

∈

Proposition 2. Given a knowledge base KB and a modiﬁcation-
seeking query ϕm, C is a modiﬁcation-seeking explanation for ϕm
if C is an MCS of KB

and ϕm

ϕm

C.

∪ {

}

(cid:54)∈

The proof of Proposition 2 follows from the fact

that a

.

}

{

∪

modiﬁcation-seeking explanation for ϕm is indeed an MCS of KB
ϕm
Algorithm 1 presents the pseudocode of QUERIES, which gener-
ates explanations for an agent ai. At a high level, it iterates over all
constraints in KB and assigns large weights k >> 1 to constraints
that are public to agent ai with respect to access-rights function α.
Then, the MUS (or MCS) solver prioritizes the constraints with the
largest weights, which means that the output of the solver is a set of
constraints with the largest cumulative sum of weights (i.e., privacy-
aware explanation).

The completeness of QUERIES lies in the assumption we made
for the two query types, which is that an explanation for both query
types always exists. The correctness of QUERIES lies in the cor-
rectness of the MUS and MCS solvers and the assumption that k is
sufﬁciently large such that explanations with the largest cumulative
sum of weights are privacy-aware explanations.

6 Empirical Evaluations

We now empirically evaluate our approach both in simulated compu-
tational experiments as well as in a human user study.

6.1 Computational Evaluation

We now present a computational evaluation of QUERIES for the fol-
lowing four queries, two for each query type, where Ca is an agent’s
clause and Σ an infeasible schedule:3

•
•
•
•

Reason-seeking query (agent): Why is Ca unsatisﬁed?
Modiﬁcation-seeking query (agent): How to satisfy Ca?
Reason-seeking query (schedule): Why is Σ infeasible?
Modiﬁcation-seeking query (schedule): How to make Σ feasible?
We ran our experiments on a MacBook Pro machine comprising
an M1 Max processor with 32GB of memory. The time limit was
set to 500s. Our implementation of QUERIES is written in Python
and integrates calls to MUS and MCS oracles through the PySAT
toolkit [20].4

To comprehensively evaluate our approach, we ran three sets of
experiments: (1) To demonstrate the scalability of our approach, we
evaluated it on our motivating employee shift assignment problem
of varying size; (2) To demonstrate the impact of privacy or access
rights, we evaluated our algorithm on the same scheduling problem,
but agents have varying access rights; and (3) To demonstrate the
generality of our approach, we evaluated it on an SMT-based encod-
ing of the job-shop scheduling problem.

·

|

|

·

|

|

|

R

R

S
|

A
|

A
|

= 10

= 10

i agents,

i resources, and

, resources
|

, and time steps
|

Experiment 1: Scalability: In this experiment, we vary the scale
and complexity of the agent scheduling problem by varying the num-
ber of agents
in the problem.
Speciﬁcally, we created 14 random instances, where each instance
has
= 10 time
steps, with i taking the values 1, 1.5, 2, . . . , 7.5. For the domain con-
straints, we extended the ones described in Section 2 to include more
agents, shift types, and time steps, as well as included an additional
constraint describing the maximum number of consecutive shifts an
employee can undertake without a day off. For the agent constraints,
we generated 5 types of constraints to reﬂect different kinds of prefer-
ences similar to those presented in Section 2, and randomly assigned
them to the agents. We set the fraction p = 0.5 of agents that each
agent has access rights to. If an agent ai has access rights to agent
aj, then ai is aware of all of agent aj’s constraints.

S
|

|

|

(cid:15)
|

KB

Figures 3(a) and 3(b) plot the runtimes of QUERIES as a function
and the explana-
of the cardinalities of the knowledge base
tion
found, respectively. Unsurprisingly, the runtimes increase as
the cardinalities increase. The reason is that the search space grows
. Also, modiﬁcation-seeking queries
with
took longer to solve than reason-seeking queries. The reason is that
our off-the-shelf MCS solver, used for modiﬁcation-seeking queries,
is less efﬁcient than our off-the-shelf MUS solver, used for reason-
seeking queries.

, also reﬂected in

KB

(cid:15)

|

|

|

|

|

|

Experiment 2: Access Rights: In this experiment, we use the same
employee shift assignment problem, where we set the number of
A
S
agents
= 5. We
|
|
vary the fraction p =
of other agents that each
agent has access rights to.

|
0, 0.1, 0.2, . . . , 1
}
{

= 40, and time steps

= 40, resources

R

|

|

|

Figures 4(a), 4(b), and 4(c) plot, as a function of access rights
fraction p, the runtimes of QUERIES, privacy losses ρi((cid:15)) of ex-
planations, and cardinality of explanations
, respectively. Similar
to the previous experiment, the runtimes are larger for modiﬁcation-

(cid:15)
|

|

3 Ca was randomly selected from a pool of unsatisﬁed clauses of agent a
and Σ was generated by randomly ﬂipping 20% of the values of a feasible
schedule.

4 The

code

repository

is

available

at

https://github.com/YODA-

Lab/QUERIES.

---

<!-- PAGE 6 -->

(a)

(b)

Figure 3: Results of Experiment 1 on the Scalability of QUERIES

(a)

(b)

(c)

Figure 4: Results of Experiment 2 on the Impact of Privacy and Access Rights

(a)

(b)

Figure 5: Results of Experiment 3 on SMT-based Encoding of Job-Shop Scheduling

seeking queries than reason-seeking queries. However, unlike the
previous experiment, there is a signiﬁcant difference in
for the
different queries in this experiment. As the modiﬁcation-seeking
queries required longer explanations, they took longer to solve than
reason-seeking queries.

(cid:15)

|

|

Additionally, the runtimes stay relatively constant for all values of
p, reﬂecting the fact that the runtimes for the MCS and MUS com-
putations are independent of the weights of the clauses. Also, as ex-
pected, the privacy loss decreases as p increases since fewer clauses
are private as p increases. Finally, as p increases,
either decreases
or remains constant, indicating that the solver can ﬁnd shorter (i.e.,
better) explanations when the explanation space expands with larger
values of p.

(cid:15)

|

|

Experiment 3: SMT and Job-Shop Scheduling: Finally, to demon-
strate that our explainable scheduling framework and algorithm can
be generalized to other scheduling problems as well as other types
of logic aside from propositional logic, we evaluate our approach

on a Satisfability Modulo Theory (SMT) encoding of the job-shop
scheduling problem [30]. SMT is a decision problem that extends
Boolean logic and allows for richer representations of real-world
problems with logical formulae that are based on a combination of
background theories such as integers and reals [13].

The job-shop scheduling problem involves assigning a set of jobs,
each with its own processing time, to machines in a way that ensures
all jobs are completed. We encoded this problem in Python using
the Z3 solver [12], and generated 11 instances by varying the num-
ber of jobs, processing times, and machines. For the MUS and MCS
solvers, we used off-the-shelf implementations available within Z3.
Similar to the previous experiment, we generated queries with an un-
satisﬁed constraint and an infeasible schedule.

Figures 5(a) and 5(b) plot the runtimes of QUERIES as a function
(cid:15)
of the cardinalities
, respectively. We observed trends
|
similar to those in Experiment 1, attributable to the same reasons
described earlier."

KB

and

|

|

|

---

<!-- PAGE 7 -->

be included, while the remaining participants (12%) suggested a
combination of both public and private information.

In conclusion, our study supports the hypothesis that individuals
prefer explanations containing only public information, which they
perceive as not only more satisfactory but also more equitable.. Based
on these ﬁndings, our explanation generation framework is designed
to align with people’s expectations for a scheduling decision expla-
nation in this particular context.

7 Related Work

There is a small body of literature on explainable scheduling, with
EXPRES [28] being the most relevant related work. It uses a MILP
to ﬁnd explanations for unsatisﬁed user preferences. Nevertheless, it
is limited to only identifying a set of reasons for unsatisﬁed user
preferences, thus lacking the ability to address and explain other
types of queries, such as how (or why) a schedule can be (or is)
(in)feasible. With regards to privacy, EXPRES preserves privacy
by post-processing explanations to remove identifying reference to
agents. In contrast, we give a more thorough treatment on this is-
sue as we found that it is key to users in our user study. On a sim-
ilar thread, Cyras et al. [11] proposed an argumentation-based ap-
proach for explaining why a schedule is (or not) feasible and why a
preference was unsatisﬁed in the schedule, as we also tackle in this
paper. The key differences between their approach and ours is that
they do not consider any privacy preservation strategies, they are re-
stricted to makespan scheduling problems, and they did not provide
any experimental evaluation of their approach. Finally, Agrawal et
al. [1] and Bertolucci et al. [3] also consider the problem of explain-
ing scheduling decisions, however, their scope is limited to speciﬁc
domain applications – scheduling Mars rovers and operating rooms,
respectively.

A related research area is explainable planning, which has a
larger body of work. Most of the approaches in this area aim at
explaining planning-speciﬁc queries, such as why a plan is feasi-
ble/optimal and why a particular action is (or not) included in a
plan [7, 16, 31, 32, 37, 39]. Closely related is the work by Vasileiou
et al. [35], which also uses minimal correction sets (MCS) and mini-
mal unsatisﬁable sets (MUS) to ﬁnd explanations. However, the key
differences between their approach and ours is that they do not con-
sider privacy preservation and they take a philosophically different
approach of ﬁnding explanations by reconciling the differences be-
tween the mental models of the explainer and explainee. Finally, for
a further exposition on the relationship between our approach and
previous works such as diagnosis and MUS generation, we refer the
reader to the work by Vasileiou et al. [35, 36].

8 Discussion

Privacy: Despite optimizing for privacy, explanations may still con-
tain private constraints with respect to the explainee. As such, pri-
vacy leakage can occur when these explanations are relayed to the
explainee. To address this issue and preserve the agents’ privacy, we
can post-process the explanation by abstracting away the remaining
private constraints. This process can take different forms, such as
masking all identifying references to the agents’ whose private con-
straints are included in the explanation or by completely retracting
the private constraints from the explanation.

As an example, consider that Thanos has no access rights to
any of the agent constraints. Then, the reason-seeking explanation

Figure 6: Human user study results from 60 users: (a) Percentage
of users that selected generic and privacy-aware explanations; and
(b) Percentage of users that were satisﬁed, indifferent, or unsatisﬁed
with the privacy-aware explanation.

6.2 Human User Study

We now present a user study aimed at examining the assumptions
made in our framework. In particular, we hypothesize:

Within agent scheduling problems, individuals prefer expla-
nations containing only public information (e.g., publicly ac-
knowledged rules and constraints) over those including private
information (e.g., other employees’ names and personal con-
straints), as they perceive them as more satisfactory.

To evaluate this hypothesis, we conducted a human user study in-
volving 60 English-speaking participants recruited through the on-
line platform Proliﬁc [26]. The study is centered around the em-
ployee shift assignment problem introduced earlier, with participants
engaging in a thought experiment by assuming the role of an em-
ployee in a hypothetical company.

We informed the participants that Alice, an automated schedul-
ing agent, was responsible for creating a schedule under the previ-
ously described domain constraints, ensuring that this information
was public and known to all users. Participants were asked to choose
a personal constraint from four available options, making them aware
of only their own personal constraint, while the remaining agent con-
straints were considered private information. The participants then
received their shift assignments, and were notiﬁed that their personal
constraint was not satisﬁed in Alice’s schedule.

Their primary task was to select an explanation out of two op-
tions: a generic explanation, which contained another employee’s
name and private constraint as the reason for their unsatisﬁed con-
straint, and a privacy-aware explanation, which included only a pub-
lic domain constraint. Participants then answered questions about
their choice of explanation and their satisfaction levels.

Figure 6 presents the main results of the study. The majority
(83.4%) of participants preferred the privacy-aware explanation (Fig-
ure 6(a)). Among those who chose the privacy-aware explanation,
54% were satisﬁed, while the remaining participants were either in-
different (22%) or unsatisﬁed (24%), as shown in Figure 6(b). In the
analysis of responses to the justiﬁcation question, i.e., “why they se-
lected the particular explanation”, we observed a common trend: the
privacy-aware explanation was considered more “informative” and
“equitable” to all employees. Here, informative meant that it con-
tained well-justiﬁed rules (i.e., constraints known to them), while
“equitable” implied that it was not personal in the sense that it did not
disclose other employees’ information. Finally, when asked whether
an explanation for a scheduling decision should include only public
information, only private information, or a combination of both, the
vast majority (88%) responded that only public information should

---

<!-- PAGE 8 -->

{

¬

∨ ¬

x1,1,2

x4,1,2

x4,1,2,

(cid:15)r =
that is generated for him unfor-
}
tunately includes Rose’s identity and private constraint (= x4,1,2).
Post-processing (cid:15)r will allow us to retract x4,1,2 from (cid:15)r and
mask the identity of Rose from the remaining clause

∨
x1,1,2, for example, by transforming the clause to its general-
x1,j,t, x2,j,t, x3,j,t, x4,j,t
) ∀rj ∈R,st∈S (do-
{
}

¬
ized form atmost1(
main constraint C3).

x4,1,2

¬

Explanation Delivery: After the (potential) abstraction phase, the
(post-processed) explanation needs to be communicated to the agent.
Unless the explainee agent is a domain expert, the explanation should
not be communicated in a logical representation, but rather in a
human-understandable format such as natural language. A trivial di-
rection could be to leverage the expressivity and symbolic nature of
logic. That is, we can deﬁne natural language templates and use them
to map the generated explanations. In particular, notice that each con-
straint “symbolizes” a speciﬁc constraint type and is grounded on
(propositional) variables, with each variable denoting a scheduling
element such as an agent, a resource, or a time step. For instance,
(cid:15)r =
says that Rose is assigned the morn-
ing shift on Tuesday (x4,1,2), and that either Rose or Thanos can be
assigned a morning shift on Tuesday (
). As such,
a logic-based explanation can be transformed into a natural language
explanation by identifying and mapping the constraints to their re-
spective pre-deﬁned, natural language templates. Another possibility
is to leverage Large Language Models (LLMs) [6] to translate logical
explanations into natural language. However, the accuracy of such
translations will need to be validated through additional research as
LLMs have been shown to have hallucination issues [40]. Another
approach is through visualization systems [22, 33], though these sys-
tems will likely need to be crafted with signiﬁcant domain expertise.

x4,1,2,
{

x4,1,2

x1,1,2

x4,1,2

x1,1,2

∨ ¬

∨¬

{¬

¬

}

}

Ethical Considerations: It is paramount to assess the ethical im-
plications of our work. In our context, two ethical considerations
emerge – the explanation unavoidably involves private information,
and the fair resolution of conﬂicting agent constraints. The former
concern can be addressed by the post-processing mechanisms de-
scribed above. For the latter, while we do not address the issue di-
rectly in our work, we imagine that fairness could be achieved by
employing multi-objective optimization techniques [15, 17, 19] that
seek a balance among conﬂicting constraints.

Although our current framework does not present deﬁnitive solu-
tions to these complex issues, these potential directions could guide
the future trajectory of research in this ﬁeld. Subsequent iterations
should integrate these considerations, working towards not just prac-
tical but also ethically robust AI explanation systems.

9 Conclusions

In this paper, we tackled the challenge of generating explanations for
agent scheduling problems. We proposed a logic-based framework
capable of generating privacy-aware explanations for reason-seeking
and modiﬁcation-seeking queries. To the best of our knowledge, our
framework is the ﬁrst to present a general approach that tackles a
broad spectrum of agent scheduling problems while quantifying and
optimizing for privacy. Our experimental results demonstrate the ef-
ﬁcacy of our framework, and our user study supports the importance
of privacy, fairness, and informativeness in explanation generation
for scheduling systems.

Acknowledgments

This research is partially supported by the National Science Founda-
tion under awards 1812619 and 2232055. The views and conclusions
contained in this document are those of the authors and should not
be interpreted as representing the ofﬁcial policies, either expressed
or implied, of the sponsoring organizations, agencies, or the United
States government.

References

[1]

Jagriti Agrawal, Amruta Yelamanchili, and Steve Chien, ‘Using ex-
plainable scheduling for the Mars 2020 rover mission’, arXiv preprint
arXiv:2011.08733, (2020).

[2] Carlos Ansótegui, Miquel Boﬁll, Miquel Palahí, Josep Suy, and Ma-
teu Villaret, ‘Satisﬁability modulo theories: An efﬁcient approach for
the resource-constrained project scheduling problem’, in Proceedings
of the Symposium on Abstraction, Reformulation and Approximation
(SARA), pp. 2–9, (2011).

[3] Riccardo Bertolucci, Carmine Dodaro, Giuseppe Galatà, Marco
Maratea, Ivan Porro, and Francesco Ricca, ‘Explaining ASP-based op-
erating room schedules’, in Proceedings of the Workshop on Explain-
able Logic-Based Knowledge Representation, (2021).

[4] Armin Biere, Marijn Heule, Hans van Maaren, and Toby Walsh, Hand-

book of Satisﬁability, volume 336, IOS press, 2021.

[5] Miquel Boﬁll, Marc Garcia, Josep Suy, and Mateu Villaret, ‘MaxSAT-
based scheduling of B2B meetings’, in Proceedings of the International
Conference on Integration of AI and OR Techniques in Constraint Pro-
gramming (CPAIOR), pp. 65–73, (2015).

[6] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran
Arora, Sydney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine
Bosselut, Emma Brunskill, et al., ‘On the opportunities and risks of
foundation models’, arXiv preprint arXiv:2108.07258, (2021).

[7] Tathagata Chakraborti, Sarath Sreedharan, Yu Zhang, and Subbarao
Kambhampati, ‘Plan explanations as model reconciliation: Moving
the Interna-
beyond explanation as soliloquy’,
tional Joint Conference on Artiﬁcial Intelligence (IJCAI), pp. 156–163,
(2017).

in Proceedings of

[8] Wayne Chi, Steve Chien, and Jagriti Agrawal, ‘Scheduling with com-
plex consumptive resources for a planetary rover’, in Proceedings of
the International Conference on Automated Planning and Scheduling
(ICAPS), pp. 348–356, (2020).

[10]

[9] Stephen Cook, ‘The complexity of theorem-proving procedures’, in
ACM Symposium on Theory of Computing (STOC), pp. 151–158,
(1971).
James Crawford and Andrew Baker, ‘Experimental results on the appli-
cation of satisﬁability algorithms to scheduling problems’, in Proceed-
ings of the National Conference on Artiﬁcial Intelligence (AAAI), pp.
1092–1097, (1994).

[11] Kristijonas Cyras, Dimitrios Letsios, Ruth Misener, and Francesca
Toni, ‘Argumentation for explainable scheduling’, in Proceedings of
the AAAI Conference on Artiﬁcial Intelligence (AAAI), pp. 2752–2759,
(2019).

[12] Leonardo De Moura and Nikolaj Bjørner, ‘Z3: An efﬁcient SMT
solver’, in Proceedings of International Conference on Tools and Al-
gorithms for the Construction and Analysis of Systems (TACAS), pp.
337–340, (2008).

[13] Leonardo De Moura and Nikolaj Bjørner, ‘Satisﬁability modulo the-
ories: introduction and applications’, Communications of the ACM,
54(9), 69–77, (2011).

[14] Emir Demirovi´c, Nysret Musliu, and Felix Winter, ‘Modeling and solv-
ing staff scheduling with partial weighted MaxSAT’, Annals of Opera-
tions Research, 275, 79–99, (2019).

[15] Michael Emmerich and André Deutz, ‘A tutorial on multiobjective op-
timization: Fundamentals and evolutionary methods’, Natural Comput-
ing, 17(3), 585–609, (2018).

[16] Maria Fox, Derek Long, and Daniele Magazzeni, ‘Explainable plan-

ning’, arXiv preprint arXiv:1709.10256, (2017).

[17] Nyoman Gunantara, ‘A review of multi-objective optimization: Meth-
ods and its applications’, Cogent Engineering, 5(1), 1502242, (2018).
[18] Stefaan Haspeslagh, Tommy Messelis, Greet Vanden Berghe, and
Patrick De Causmaecker, ‘An efﬁcient translation scheme for represent-
ing nurse rostering problems as satisﬁability problems’, in Proceedings

---

<!-- PAGE 9 -->

of the International Conference on Agents and Artiﬁcial Intelligence
(ICAART), pp. 303–310, (2013).

[38]

Jean-Paul Watson, J. Christopher Beck, Adele Howe, and L. Darrell
Whitley, ‘Problem difﬁculty for tabu search in job-shop scheduling’,
Artiﬁcial Intelligence, 143(2), 189–217, (2003).

[39] Yu Zhang, Sarath Sreedharan, Anagha Kulkarni, Tathagata Chakraborti,
Hankz Hankui Zhuo, and Subbarao Kambhampati, ‘Plan explicability
and predictability for robot task planning’, in Proceedings of the Inter-
national Conference on Robotics and Automation (ICRA), pp. 1313–
1320, (2017).

[40] Terry Yue Zhuo, Yujin Huang, Chunyang Chen, and Zhenchang Xing,
‘Red teaming ChatGPT via jailbreaking: Bias, robustness, reliability
and toxicity’, arXiv preprint arXiv:2301.12867, (2023).

[19] Carlos Hernández, William Yeoh, Jorge A. Baier, Han Zhang, Luis
Suazo, Sven Koenig, and Oren Salzman, ‘Simple and efﬁcient bi-
objective search algorithms via fast dominance checks’, Artiﬁcial In-
telligence, 314, 103807, (2023).

[20] Alexey Ignatiev, Antonio Morgado, and Joao Marques-Silva, ‘PySAT:
A Python toolkit for prototyping with SAT oracles’, in Proceedings of
the International Conference on Theory and Applications of Satisﬁabil-
ity Testing (SAT), pp. 428–437, (2018).

[21] Miyuki Koshimura, Hidetomo Nabeshima, Hiroshi Fujita, and Ryuzo
Hasegawa, ‘Solving open job-shop scheduling problems by SAT en-
coding’, IEICE Transactions on Information and Systems, 93(8), 2316–
2318, (2010).

[22] Ashwin Kumar, Stylianos Loukas Vasileiou, Melanie Bancilhon,
Alvitta Ottley, and William Yeoh, ‘VizXP: A visualization framework
for conveying explanations to users in model reconciliation problems’,
in Proceedings of the International Conference on Automated Planning
and Scheduling (ICAPS), pp. 701–709, (2022).

[23] Sudip Kundu and Sriyankar Acharyya, ‘Stochastic local search ap-
proaches in solving the nurse scheduling problem’, in Proceedings of
the International Confernece on Computer Information Systems - Anal-
ysis and Technologies (CISIM), pp. 202–211.

[24] Chu Min Li and Felip Manya, ‘MaxSAT, hard and soft constraints’, in

[25]

Handbook of Satisﬁability, 903–927, IOS press, (2021).
João Marques-Silva, Federico Heras, Mikolás Janota, Alessandro
Previti, and Anton Belov, ‘On computing minimal correction subsets’,
in Proceedings of the International Joint Conference on Artiﬁcial Intel-
ligence (IJCAI), pp. 615–622, (2013).

[26] Stefan Palan and Christian Schitter, ‘Proliﬁc: A subject pool for on-
line experiments’, Journal of Behavioral and Experimental Finance,
17, 22–27, (2018).
Jose Pinto and Ignacio Grossmann, ‘A logic-based approach to schedul-
ing problems with resource constraints’, Computers & Chemical Engi-
neering, 21(8), 801–818, (1997).

[27]

[28] Alberto Pozanco, Francesca Mosca, Parisa Zehtabi, Daniele Maga-
zzeni, and Sarit Kraus, ‘Explaining preference-driven schedules: the
expres framework’, in Proceedings of the International Conference on
Automated Planning and Scheduling, pp. 710–718, (2022).

[29] Alessandro Previti and João Marques-Silva, ‘Partial MUS enumera-
tion’, in Proceedings of the AAAI Conference of Artiﬁcial Intelligence
(AAAI), pp. 818–825, (2013).

[30] Sabino Francesco Roselli, Kristofer Bengtsson, and Knut Åkesson,
‘SMT solvers for job-shop scheduling problems: Models comparison
and performance evaluation’, in International Conference on Automa-
tion Science and Engineering (CASE), pp. 547–552, (2018).

[31] Tran Cao Son, Van Nguyen, Stylianos Loukas Vasileiou, and William
Yeoh, ‘Model reconciliation in logic programs’, in European Confer-
ence on Logics in Artiﬁcial Intelligence (JELIA), pp. 393–406, (2021).
[32] Sarath Sreedharan, Tathagata Chakraborti, and Subbarao Kambham-
pati, ‘The emerging landscape of explainable automated planning &
decision making’, in Proceedings of the International Joint Conference
on Artiﬁcial Intelligence (IJCAI), pp. 4803–4811, (2020).

[33] Karthik Valmeekam, Sarath Sreedharan, Sailik Sengupta, and Subbarao
Kambhampati, ‘RADAR-X: an interactive mixed initiative planning in-
terface pairing contrastive explanations and revised plan suggestions’,
in Proceedings of the International Conference on Automated Planning
and Scheduling (ICAPS), pp. 508–517, (2022).
Jorne Van den Bergh, Jeroen Beliën, Philippe De Bruecker, Erik De-
meulemeester, and Liesje De Boeck, ‘Personnel scheduling: A litera-
ture review’, European Journal of Operational Research, 226(3), 367–
385, (2013).

[34]

[35] Stylianos Loukas Vasileiou, Alessandro Previti, and William Yeoh, ‘On
exploiting hitting sets for model reconciliation’, in Proceedings of the
AAAI Conference on Artiﬁcial Intelligence (AAAI), pp. 6514–6521,
(2021).

[36] Stylianos Loukas Vasileiou, William Yeoh, and Tran Cao Son, ‘On the
relationship between KR approaches for explainable planning’, arXiv
preprint arXiv:2011.09006, (2020).

[37] Stylianos Loukas Vasileiou, William Yeoh, Tran Cao Son, Ashwin
Kumar, Michael Cashmore, and Daniele Magazzeni, ‘A logic-based
explanation generation framework for classical and hybrid planning
problems’, Journal of Artiﬁcial Intelligence Research, 73, 1473–1534,
(2022).

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

|     | A   | Logic-based |     |                                       |     | Framework  |     | for      | Explainable     |     |     | Agent |     |
| --- | --- | ----------- | --- | ------------------------------------- | --- | ---------- | --- | -------- | --------------- | --- | --- | ----- | --- |
|     |     |             |     |                                       |     | Scheduling |     | Problems |                 |     |     |       |     |
|     |     |             |     | StylianosLoukasVasileioua;*,BorongXua |     |            |     |          | andWilliamYeoha |     |     |       |     |
aWashingtonUniversityinSt.Louis
Abstract. AgentSchedulingProblems(ASPs)arecommoninvar- queries,whichofferguidanceonrenderinginfeasibleschedulingde-
ious real-world situations, requiring explainable decision-making cisions feasible. Recognizing the importance of privacy in multi-
processes to effectively allocate resources to multiple agents while agentscheduling,weusetheconceptofagentaccessrightstodis-
fostering understanding and trust. To address this need, this paper tinguish between public and private information, and introduce a
presents a logic-based framework for providing explainable deci- straightforwardprivacy-lossfunctiontoquantifytheamountofpri-
sions in ASPs. Specifically, the framework addresses two types of vateinformationdisclosedinexplanations.Usingthisfunction,we
queries:reason-seekingqueries,whichexplainthereasoningbehind thendefinethenotionofprivacy-awareexplanationsandpresentthe
schedulingdecisions,andmodification-seekingqueries,whichoffer Query Understanding and Efficient Response with Intelligible Ex-
guidance on making infeasible decisions feasible. Acknowledging planationsofSchedules(QUERIES)algorithmforcomputingthem.
the importance of privacy in multi-agent scheduling, we introduce This approach ensures that the explanations provided maintain the
a privacy-loss function that measures the disclosure of private in- confidentialityofsensitiveinformationwhilestillofferingvaluable
formation in explanations, enabling a privacy-preserving aspect in insightsintotheschedulingdecisions.
our framework. By using this function, we introduce the notion of In summary, our framework advances existing explainable
privacy-awareexplanationsandpresentanalgorithmforcomputing scheduling methods, which typically focus on specific scheduling
them. Empirical evaluations demonstrate the effectiveness and ver- problems[1,3,28],by providingageneralsolutionapplicabletoa
satilityofourapproach. broaderrangeofASPs.Ourmaincontributionsareasfollows:
Weintroduceagenerallogic-basedexplanationgenerationframe-
•
|     |     |     |     |     |     |     |     | work for | ASPs that | addresses | both | reason-seeking | queries and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | ---- | -------------- | ----------- |
1 Introduction
modification-seekingqueries.
Weproposeaprivacy-lossfunctiontoquantifytheamountofpri-
| Agentschedulingproblems(ASPs)involveallocatingafinitesetof |     |     |     |     |     |     |     | •   |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vateinformationincludedinanexplanationanddefinetheconcept
resourcestomultipleagentsoveraspecifictimeframe.Theseprob-
ofprivacy-awareexplanations.
| lems | are pervasive | in  | real-world | scheduling |     | systems, | ranging from |     |     |     |     |     |     |
| ---- | ------------- | --- | ---------- | ---------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
WepresenttheQUERIESalgorithmforcomputingexplanations.
| personnelshiftassignments[34]tomachinejoballocation[38],and |     |     |     |     |     |     |     | •   |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Empiricalevaluationsdemonstratetheeffectivenessandversatility
evenschedulingawakeandasleepperiodsforMarsrovers[8].Apart
ofourapproach.
| from | generating | a schedule |     | that allocates | resources |     | to agents, it is |     |     |     |     |     |     |
| ---- | ---------- | ---------- | --- | -------------- | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
crucialtoensurethatboththescheduleandtheunderlyingdecision-
making process are explainable. An agent may require an expla- 2 MotivatingThoughtExperiment
| nation | for why | certain | scheduling | decisions |     | were not | satisfied or |     |     |     |     |     |     |
| ------ | ------- | ------- | ---------- | --------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
Tobetterunderstandthechallengesfacedbyagentschedulingprob-
| why | a schedule | could | not | be generated | at  | all. In such | cases, un- |     |     |     |     |     |     |
| --- | ---------- | ----- | --- | ------------ | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- |
lemsandtheimportanceofgeneratingeffectiveexplanations,letus
| derstanding |     | the reasons | behind | these | issues | is not only | enlighten- |     |     |     |     |     |     |
| ----------- | --- | ----------- | ------ | ----- | ------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
engageinathoughtexperimentinspiredbyasimplifiedversionofthe
ingbutalsonecessaryforrectifyingtheproblem.Additionally,pri-
employeeshiftassignmentproblem[34].Considerascenariobased
vacyplaysasignificantroleduetothesensitivenatureofpersonal
ontheemployeeshiftassignmentproblem[34].Inthisscenario,an
| information |     | that may | be included | in  | ASPs, | such as | agents’ con- |     |     |     |     |     |     |
| ----------- | --- | -------- | ----------- | --- | ----- | ------- | ------------ | --- | --- | --- | --- | --- | --- |
automatedschedulingagentnamedAliceisresponsibleforassign-
| straints   | and  | preferences. | Preserving     |     | privacy | helps protect | individ-  |               |           |      |          |               |                 |
| ---------- | ---- | ------------ | -------------- | --- | ------- | ------------- | --------- | ------------- | --------- | ---- | -------- | ------------- | --------------- |
|            |      |              |                |     |         |               |           | ing shifts to | employees | at a | company. | Specifically, | there are three |
| ual agents | from | potential    | discrimination |     | or      | unauthorized  | access to |               |           |      |          |               |                 |
shifttypes–morning,afternoon,andevening–andfouremployees
theirinformation,fosteringtrustandwillingnesstoparticipateinthe
|     |     |     |     |     |     |     |     | – Thanos, Irene, | Vicky, | and Rose | – who | need to | be assigned shifts |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------ | -------- | ----- | ------- | ------------------ |
schedulingprocess.Therefore,incorporatingexplanationgeneration
modalitieswithprivacy-preservingconsiderationsintoASPsystems overthreedaysfromMondaytoWednesday.
|     |     |     |     |     |     |     |     | The scheduling | problem | consists | of  | the following | domain con- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | --- | ------------- | ----------- |
ishighlydesirable.
straints:
Toaddressthisneed,thispaperpresentsalogic-basedframework
C Allemployeesmustbeassignedatotaloftwoshifts.
| aimedatmakingASPsexplainable.Theframeworkaccommodates |     |     |     |     |     |     |     | 1 : |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two types of queries: reason-seeking queries, which clarify why a C : Employeescannotbeassignedmultipleshiftsperday.
2
scheduling decision was (or not) derived, and modification-seeking C : Notwoemployeescanbeassignedthesameshiftthesameday.
3
|     |     |     |     |     |     |     |     | C 4 : Employees | cannot | be assigned | a   | morning | shift right after an |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ----------- | --- | ------- | -------------------- |
∗CorrespondingAuthor.Email:v.stylianos@wustl.edu. eveningshift.

3 Background
Wenowprovidesomebackgroundonthesatisfiability(SAT)prob-
lem,ageneralagentschedulingproblem(ASP)definition,andour
logic-basedrepresentationofthatproblem.
3.1 Satisfiability
|     |     |     |     | We assume | familiarity         |        | with propositional | logic.         | A knowledge | base      |
| --- | --- | --- | --- | --------- | ------------------- | ------ | ------------------ | -------------- | ----------- | --------- |
|     |     |     |     | KB is     | aset ofconstraints, |        | whereeach          | constraintis   | built       | uprecur-  |
|     |     |     |     | sively    | from literals       | (i.e., | variables or       | its negations) | using       | the usual |
logicalconnectives.
Figure1:InstanceofthethoughtexperimentwithAliceandThanos. Satisfiability(SAT)[9]istheprototypicalNP-completeproblem
offindinganassignmentoftruthvaluestovariablesinordertomake
|     |     |     |     | aknowledgebaseKB |     |     | true.Ifthereexistsatruthvalueassignmentµ |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | --- | ---------------------------------------- | --- | --- | --- |
Moreover,eachemployeehaspersonalconstraints:
|     |     |     |     | thatmakesKB |     | true,thenwesaythatµisamodelofKB |     |     |     | andKB is |
| --- | --- | --- | --- | ----------- | --- | ------------------------------- | --- | --- | --- | -------- |
C T : Thanoswantsonlymorningorafternoonshifts. satisfiable,otherwiseKB isunsatisfiable,denotedbyKB = .A
|     |     |     |     |     |     |     |     |     |     | | ⊥ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C : Irenedoesnotwanteveningshifts. KB entailsaconstraintϕ,denotedKB =ϕ,iffKB ϕ = .
I
|     |     |     |     | Partial | weighted | MaxSAT | [24] is | an | extension | of ∪{¬ SAT | in }| which ⊥ |
| --- | --- | --- | --- | ------- | -------- | ------ | ------- | -------------- | ---------- | ------------- |
C V : VickywantstheafternoonshiftonTue.andWed.
C : RosewantsthemorningshiftonTue.andWed. constraintsarepartitionedintohardandsoftconstraints,whereeach
R
softconstraintsisgivenaweight.Hardconstraintsmustalwaysbe
Here, Alice’s objective is to find a schedule that satisfies all do- satisfiedinasolution,whereassoftconstraintsmaynot.Thegoalof
main constraints and, as much as possible, accommodates the em- MaxSATistofindanassignmentthatsatisfiesthehardclausesand
ployeeconstraintsaccordingtotheirweights,whichinthisexample maximizesthesumofweightsofthesatisfiedsoftclauses.
arebasedontheemployees’senioritylevels.
Let us assume that Alice finds a feasible schedule, but it does 3.2 AgentSchedulingProblem
notmeetThanos’constraintofbeingassignedmorningorafternoon
shifts.Thanos,inturn,mayinquireaboutthereasonforthisassign- Ingeneral,thegoalofanagentschedulingproblem(ASP)istodis-
ment.Togenerateaneffectiveexplanation,Aliceneedsaframework tribute a set of resources to a set of agents over a scheduling hori-
thatcangenerateexplanationsthatareinformativeandtailoredtothe zon.Formally,itcanbedefinedasatuple = A,R,S,C ,where
|     |     |     |     |     | n   |     |     | A m | (cid:104) | (cid:105) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- |
s p e c i fic ne e ds o f t h e e x p l ai n e e , thatis,Alicemustfirstrecognizethe A = a i i = 1 i s a s e t o f a ge n t s , R = r j j = 1 i s a se t o f r e s o u rc e s ,
|     |     |     |     |     | { }h |     |     | { } |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
n a tu r e of th e ex p l a i ne e ’ s q u e r y . S = s t i s a s e t o f ti m e s t e p s, and C i s a s e t of c on s t r a in t s th a t
|     |     |     |     |     | { } t = 1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
In our thought experiment, Thanos’ query is a reason-seeking consistsofdomainconstraints,whichareintrinsicanddescribethe
query,ashewantstoknow“why”hisconstraintwasunsatisfiedin problem’sdynamics,aswellasagentconstraints,whichareextrinsic
the schedule. In response, Alice should provide a (reason-seeking) anddescribetheagents’personalconstraints.
|     |     |     |     |     |     |     | isascheduleΣ,thatisan |     | A   | R S |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
explanationthatidentifiesthereasonsbehindher(scheduling)deci- AsolutiontoanASP
|     |     |     |     |     |     |     | A   |     | |   | |×| |×| | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
sion.Forexample,Alicemightexplainthatduetotheconstraintsof matrix,whereeachcellΣ[i,j,t]=1ifagenta i isassignedresource
theproblemandthehigherprioritygiventothepreferencesofRose r attimesteps andΣ[i,j,t]=0otherwise.Ascheduleisfeasible
|     |     |     |     | j   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and Vicky, it was not possible to assign Thanos morning shifts on ifallthedomainconstraints,whicharetreatedashardconstraints,
Tuesday or Wednesday without affecting the overall quality of the aresatisfied.Ascheduleisoptimalifitisfeasibleandalltheagent
allocation. constraints,whicharetreatedassoftconstraints,aremaximized.
| However, | providing a reason-seeking | explanation | alone may not |     |     |     |     |     |     |     |
| -------- | -------------------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
besufficientinallscenarios.SupposeAlicecouldnotcreateafea- 3.3 Logic-basedAgentSchedulingProblems
| sible schedule | at all due to conflicting | constraints. | In this case, a |     |     |     |     |     |     |     |
| -------------- | ------------------------- | ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- |
higher-levelemployee,suchasamanager,maywanttounderstand In this paper, we model an ASP as a logic-based problem, that
A
“how”toadjusttheschedulingproblemtoderiveafeasibleschedule. is, we encode into a set of logical constraints for which satis-
|     |     |     |     | fiability | can be | A decided. | By using an | appropriate | logical | language, |
| --- | --- | --- | --- | --------- | ------ | ---------- | ----------- | ----------- | ------- | --------- |
Thistypeofqueryisamodification-seekingquery,whichrequiresan
explanationthathelpsthemanageridentifyissuespreventingafea- the problem’s dynamics are encoded into a knowledge base KB
siblescheduleandsuggestpotentialmodifications. thatexpressesalltheschedulingconstraintsthatadesiredschedule
Inadditiontoaddressingthesetwotypesofqueries,Alice’sexpla- shouldsatisfy.Specifically,theknowledgebaseKB consistsofdo-
nationsshouldrespecttheprivacyoftheotheremployees.Toachieve mainconstraintsC andagentconstraintsC ,whereC aretreated
|     |     |     |     |                       |     | D   |                                      | A   |     | D   |
| --- | --- | --- | --- | --------------------- | --- | --- | ------------------------------------ | --- | --- | --- |
|     |     |     |     | ashardconstraintsandC |     |     | asweightedsoftconstraints.Assuch,the |     |     |     |
this,Alicecouldonlyrevealinformationaccordingtotheemployees’ A
accessrights.Indoingso,Alicedistinguishesbetweenpublicinfor- schedulingproblemturnsintoaMaxSATproblem,wherethequality
mation(informationthatcanberevealedtoemployeeswithaccess ofafeasiblescheduledependsonthedegreetowhichthesoftclauses
rights)andprivateinformation(informationthatcannotberevealed aresatisfied.Theobjectivefunctionofacandidatescheduleisthen
toemployeeswithoutaccessrights). defined as the sum of weights of satisfied soft constraints, and an
optimalscheduleisthesolutionwiththehighestpossibleobjective
Thisthoughtexperimentdemonstratessomeofthechallengesof
generatingexplanationsinthecontextofagentschedulingproblems. value. A plethora of scheduling problems has been modeled using
Indeed, in Section 4 we present an explanation generation frame- logic-basedapproaches[2,5,10,14,18,21,23,27].
workthatcanhandlethecomplexityoftheproblem,accountforthe For ease of presentation, in this paper we will use propositional
explainee’sneedsandaccessrights,andproduceinformativeexpla- logic to encode ASPs. We formally define a logic-based ASP (L-
ASP)asfollows:
nations.

Figure2:OverviewofOurExplainableLogic-basedAgentSchedulingProblemPipeline.
Definition 1 (L-ASP). An L-ASP is a tuple = A,R,S,KB , Generateinformativeandconciseexplanationsforthetwoquery
|         |     |        |     |     | L (cid:104) | (cid:105) | •      |     |     |     |     |     |
| ------- | --- | ------ | --- | --- | ----------- | --------- | ------ | --- | --- | --- | --- | --- |
| whereKB | =C  | C and: |     |     |             |           | types. |     |     |     |     |     |
|         |     | D ∪ A  |     |     |             |           |        |     |     |     |     |     |
C is the set of domain-specific (hard) constraints. These con- Preservetheprivacyofotheragentsbyonlyrevealinginformation
D
| •   |           |              |             |          |              |      | • withrespecttoaccess-rights. |     |     |     |     |     |
| --- | --------- | ------------ | ----------- | -------- | ------------ | ---- | ----------------------------- | --- | --- | --- | --- | --- |
| str | aints are | intrinsic to | the problem | and must | be satisfied | by a |                               |     |     |     |     |     |
solution. AgeneralpipelineisshowninFigure2.Wenowdescribehowto
C = (cid:83) n C i s t h e se t o f a g en t ( we i gh te d s o f t) c o n st r a i n ts . generateexplanationsforthetwoquerytypes.
| A              | i=   | 1 i     |                             |              |                 |                     |     |     |     |     |     |     |
| -------------- | ---- | ------- | --------------------------- | ------------ | --------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| • Ea           | ch C | w , c i | l , w h er                  | e e ac h c i | is a c o n s tr | a in t a s s o c i- |     |     |     |     |     |     |
|                | i =  | ( k k ) | k= 1                        | k            |                 |                     |     |     |     |     |     |     |
|                | {    | }       |                             |              |                 |                     |     |     |     |     |     |     |
| atedwithagenta |      | i andw  | k isitscorrespondingweight. |              |                 |                     |     |     |     |     |     |     |
4.1 ExplainingReason-SeekingQueries
Aschedulecanbederivedbyusingoff-the-shelfSATsolvers[4]
to search for a model µ of KB that satisfies all of the constraints Areason-seekingquery,denotedbyϕ ,aimstouncoverwhycertain
r
schedulingdecisionsweremade.RecallfromSection2thatThanos
| in C | D and possibly | some | of the constraints |     | in C A . If | a model µ |     |     |     |     |     |     |
| ---- | -------------- | ---- | ------------------ | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
exists,thenafeasiblescheduleΣµ isderivedbyextractingfromµthe wants to know why Alice did not assign him only morning shifts.
truthvaluesofthevariablescorrespondingtoagents,resources,and Alternatively,ahigher-levelemployee(e.g.,amanager)maywantto
timesteps.Otherwise,theschedulingproblemisinfeasible,i.e.,no understandwhyafeasibleschedulecannotbegenerated.
feasiblescheduleexists.Finally,ascheduleΣµ isdeemedoptimalif To explain reason-seeking queries, we assume that KB = ϕ .
| r
Therearetwopossiblescenariostoconsider:
amodelµexistsandmaximizesthecumulativesumofweightsof
satisfiedsoftconstraintsinC A . Agent Constraints in a Schedule: If the query ϕ r captures an
•
NotethattheknowledgebaseKB = C C maybeunsatis- unsatisfied (or satisfied) agent constraint in a schedule Σµ , then
D ∪ A
fiableduetoinconsistenciesinthedomainco nstraintsand/oragent ϕ C (orϕ C ).1Inthisscenario,anexplanationshould
|     |     |     |     |     |     |     | r ∈¬ | A r ∈ A |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- |
constraints.However,ifascheduleΣµ exists,thenthatmeansthat identifythereasonswhytheconstraintholdstruewithrespectto
Σµ logicallyfollowsfromasatisfiablesubsetKB µ KB.Inthe theschedule.NotethattheknowledgebaseKB hereissatisfiable
⊆
nextsection,weuseKB todenotetheknowledgebasefromwhich (seeSection3.3).
explanations are derived. Depending on the context, KB could re- InfeasibleSchedulingProblems:Ifthequeryϕ isaimedatcap-
|     |     |     |     |     |     |     | •   |     |     | r   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fertoeitherasatisfiablesubsetoftheoriginalknowledgebase(i.e., turing why a problem is infeasible, i.e., why a feasible schedule
KB )ortheoverallunsatisfiableknowledgebase. cannotbegenerated,thengenerallyϕ
| µ   |     |     |     |     |     |     |     |     |     | r = .Inthiscase,theex- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
⊥
planationshouldidentifytheinconsistencieswithinthescheduling
4 ExplainableAgentSchedulingProblems constraintsthatleadtoinfeasibleschedules.Notethattheknowl-
|     |     |     |     |     |     |     | edgebaseKB | hereisunsatisfiable,i.e.,thereisnomodelofKB |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------------------------- | --- | --- | --- | --- |
We now present our explanation generation framework for agent fromwhichafeasibleschedulecanbeextracted.
schedulingproblems.Weparticularlyaddressthefollowingproblem:
Formallynow,anexplanationforareason-seekingqueryisdefined
asfollows:
| Givenalogic-basedL-ASP |     |     | =   | A,R,S,KB  | andaqueryϕ |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|                        |     |     | L   | (cid:104) | (cid:105)  |     |     |     |     |     |     |     |
withrespecttoKB,thegoalistofindanexplanationforϕthat
|     |     |     |     |     |     |     | Definition | 2 (Reason-seeking | Explanation). | Given | a knowledge |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | ------------- | ----- | ----------- | --- |
canbeinferredfromKB.
|     |     |     |     |     |     |     | baseKB | thatencodesanL-ASP | andareason-seekingqueryϕ |     |     | ,   |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------------ | ------------------------ | --- | --- | --- |
r
|                                                       |     |     |     |     |     |     | weconsideranexplanation(cid:15) |     | L KB | tobeareason-seekingexpla- |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | ---- | ------------------------- | --- | --- |
| AsdiscussedinSection2,weareinterestedinaframeworkthat |     |     |     |     |     |     |                                 |     | r    |                           |     |     |
⊆
| cangenerateexplanationsforagentschedulingproblemsthatarenot |     |     |     |     |     |     | nationforϕ | r if: |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- | --- | --- |
only informative but also tailored to the specific needs of the ex- (cid:15) issufficient:(cid:15) = ϕ ,meaningthattheexplanation(cid:15) entails
|                                          |     |     |     |     |     |     | • r       | r | r |     |     | r   |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- |
| plainee.Suchaframeworkshouldinprinciple: |     |     |     |     |     |     | thequeryϕ | .     |     |     |     |     |
r
|     |     |     |     |     |     |     | isminimal:Forallpropersubsets(cid:15)(cid:48) |     |     | ,(cid:15)(cid:48) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | ----------------- | --- | --- |
Address two general types of queries: reason-seeking queries, (cid:15) r r (cid:15) r r =ϕ r ,indicating
| •   |     |     |     |     |     |     | •   |     |     | ⊂ (cid:54)| |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
whichaimtouncoverwhycertainschedulingdecisionswere(or thatnosmallersubsetof(cid:15) r aresufficient.
not)made,andmodification-seekingqueries,whichfocusoniden-
tifyingpotentialmodificationstotheproblem. 1Notethat¬CAdenotesthelogicalnegationofalltheconstraintsinCA.

Theseconditionsensurethatthereason-seekingexplanationisboth
| sufficientandminimalinaddressingthequery. |     |     |     |     |     |     |                |          | (cid:88) |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | -------- | -------- | --- | --- | --- |
|                                           |     |     |     |     |     |     | ρ i((cid:15))= | (cid:15) | α(a      | ,c) |     | (2) |
|                                           |     |     |     |     |     |     |                | | |−     | i        |     |     |     |
c∈(cid:15)
4.2 ExplainingModification-SeekingQueries
|                                        |     |     |     |                     | Lastly,wedefineanexplanation(cid:15)  |     |                                             |     | i asbeingprivacy-awareinrela- |     |     |     |
| -------------------------------------- | --- | --- | --- | ------------------- | ------------------------------------- | --- | ------------------------------------------- | --- | ----------------------------- | --- | --- | --- |
|                                        |     |     |     |                     | tiontoagenta                          |     | andqueryϕifitincurstheleastprivacylossamong |     |                               |     |     |     |
| Modification-seekingqueries,denotedbyϕ |     |     |     | ,focusonidentifying |                                       | i   |                                             |     |                               |     |     |     |
|                                        |     |     | m   |                     | allpossibleexplanationsEforthequeryϕ: |     |                                             |     |                               |     |     |     |
potentialmodificationstoaschedulingproblemtoaddressspecific
issues.Forexample,Thanosmaywanttoknowhowtoincorporate (cid:15) =argmin ρ i((cid:15)) (3)
i
hisunsatisfiedconstraintinAlice’sschedule,oramanagermayseek (cid:15)∈E
waystoadjusttheschedulingproblemtogenerateafeasiblesched-
ule.
4.4 IllustratingExample
| Toexplainmodification-seekingqueries,weassumethatKB |     |     |     | =   |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:54)|
ϕ m .Specifically,toexplainthesequerytypes,weseektoidentifya ConsidertheemployeeshiftassignmentproblempresentedinSec-
setofconstraintsfromtheknowledgebaseKB that,whenretracted, tion2.Torepresenttheproblemusing(propositional)logic,weem-
KB =ϕ .Likebefore,therearetwopossiblescenariostoconsider: ployBooleandecisionvariablesx foralla A,r R,and
| | m |     |     |     |     |     |     |     | i,j,t |     | i   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
UnsatisfiedAgentConstraintsinaSchedule:Ifthequeryϕ s S,whereeachvariableissettotrueifandonlyifagenta ∈ ∈ is
|     |     |     |     | m   | t   |     |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| •   |     |     |     |     | ∈   |     |     |     |     |     |     |     |
concerns accommodating an unsatisfied agent constraint in a assignedshiftr j ondays t .Otherwise,itissettofalse.Thesevari-
scheduleΣµ ,thenϕ C . ablescomprisethedomainconstraintsC D andagentconstraintsC A
|     | m ∈ | A   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
InfeasibleSchedulingProblems:Ifthequeryϕ isaimedatex- whichmakeuptheknowledgebaseKB.Notethatweassumethefol-
m
• plaininghowaproblemcanbemodifiedsuchthatafeasiblesched- lowingweightsforemployeeconstraintsC :w(C R) = w(C V) >
A
|                     |     |       |     |     | w(C T)>w(C |     | I).2 |     |     |     |     |     |
| ------------------- | --- | ----- | --- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
| ulecanbefound,thenϕ |     | m = . |     |     |            |     |      |     |     |     |     |     |
(cid:62)
We now define an explanation f or a modification-seeking query as Recall from Section 2 that Alice has generated a schedule (see
follows: Figure1)thatdoesnotsatisfyThanos’constraint,promptinghimto
askAliceareason-seekingquery.Inourlogic-basedframework,this
Definition 3 (Modification-seeking Explanation). Given a knowl- translates to the query ϕ = x x . There are two
|     |     |     |     |     |     |     | r   | {¬  | 1,1,2 ∨¬ | 1,2,2 | }   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- |
reason-seekingexplanationsforthisquery:
| edge base | KB that encodes | an  | L-ASP | and a modification- |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ----- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
L
seeking query ϕ m , we consider an explanation (cid:15) m KB to be a (cid:15) r1 = x 4,1,2 , x 4,1,2 x 1,1,2 ,statingthatonlyoneemployee
|     |     |     |     | ⊆   | •   | {   | ¬ ∨¬ |     | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
modification-seekingexplanationforϕ if: can be assigned a morning shift on the same day (domain con-
m
(cid:15) enablestheentailmentofϕ :KB (cid:15) =ϕ ,meaningthat straint)andthatRose’spreferencewasgivenahigherprioritythat
| m         |                                          | m   | m   | m            |      |     |     |     |     |     |     |     |
| --------- | ---------------------------------------- | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
| •         |                                          |     | \   | |            | day. |     |     |     |     |     |     |     |
| thequeryϕ | m isentailedwhentheconstraintsin(cid:15) |     |     | m areremoved |      |     |     |     |     |     |     |     |
fromtheknowledgebase. (cid:15) r2 = x 3,2,2 , x 3,2,2 x 1,2,2 ,statingthatonlyoneemployee
|     |     |     |     |     | •   | {   | ¬ ∨¬ |     | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
(cid:15) isminimal:Forallpropersubsets(cid:15)(cid:48) (cid:15) ,KB (cid:15)(cid:48) =ϕ , canbeassignedanafternoonshiftonthesameday(domaincon-
| m   |     |     | m   | m m m |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
• indicatingthatnosmallersubsetof(cid:15) cansatisfythequerywhen ⊂ \ (cid:54)| straint)andthatVicky’spreferencewasgivenahigherprioritythat
m
day.
removedfromtheknowledgebase.
Now,assumethattheaccess-rightsfunctionαisdefinedsuchthat
Theseconditionsensurethatthemodification-seekingexplanationis Thanoshasaccess-rightstothedomainconstraintsandRose’scon-
botheffectiveandminimalinaddressingthequery. straints,butnottotheconstraintsofotheragents.Inthiscase,thepri-
|     |     |     |     |     | vacylossρ | ofbothexplanationswouldbecalculatedasfollows: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
1
(cid:80)
|                               |     |     |     |     | ρ 1((cid:15) r1) | = (cid:15) |       | α(1,c) | = 2 2 | = 0,sinceThanoshas |     |     |
| ----------------------------- | --- | --- | --- | --- | ---------------- | ---------- | ----- | ------ | ----- | ------------------ | --- | --- |
| 4.3 Privacy-AwareExplanations |     |     |     |     | •                | |          | r1 |− |        | −     |                    |     |     |
c∈(cid:15)r1
accesstoRose’sinformation.
Itisreasonabletoassumethatindividualsmightpreferexplanations (cid:80)
|     |     |     |     |     | ρ 1((cid:15) r2)= | (cid:15) | r2 α(1,c)=2 |     | 1=1,sinceThanosdoes |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | -------- | ----------- | --- | ------------------- | --- | --- | --- |
forschedulingdecisionsthatonlyencompasspublicinformation,as • | |− −
c∈(cid:15)r2
nothaveaccesstoVicky’sinformation.
theycouldperceivetheseasmoresatisfyingandequitablecompared
toexplanationsthatincorporateprivateinformationaswell.Toex- Asρ 1((cid:15) r1)<ρ 1((cid:15) r2),theprivacy-awareexplanationinthiscase
| plore this possibility | and incorporate |     | potential | privacy preferences | wouldbe(cid:15) | r1 . |     |     |     |     |     |     |
| ---------------------- | --------------- | --- | --------- | ------------------- | --------------- | ---- | --- | --- | --- | --- | --- | --- |
intoourframework,weproposethatagentshaveaccessrightsonthe
differentpiecesofinformationabouttheschedulingproblem.Specif-
5 QUERIES:ComputingExplanations
ically,weassumeanaccess-rightsfunction:
WenowpresenttheQuestionUnderstandingandEfficientResponse
α:A KB 0,1 (1) with Intelligible Explanations of Schedules (QUERIES) algorithm,
|     |     | ×   | →{ } |     |                 |     |               |              |     |               |                |     |
| --- | --- | --- | ---- | --- | --------------- | --- | ------------- | ------------ | --- | ------------- | -------------- | --- |
|     |     |     |      |     | which generates |     | privacy-aware | explanations |     | (cid:15)∗ for | reason-seeking |     |
i
| thatdetermineswhetheranagenta |     |     | Ahasaccessrightstoacon- |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i ∈ and modification-seeking queries ϕ of an agent a i . The core of
| straintc KB,returning1ifa |                | hasaccesstocand0otherwise. |                |                  |                                                           |     |     |     |     |     |     |     |
| ------------------------- | -------------- | -------------------------- | -------------- | ---------------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                           |                | i                          |                |                  | QUERIESisbasedonreasoningviainconsistency.Inparticular,it |     |     |     |     |     |     |     |
| While ∈ we                | have motivated | access                     | rights through | the lens of pri- |                                                           |     |     |     |     |     |     |     |
leveragesasetofmethodsthataredirectlyapplicabletologic-based
vacy, note that the function can also encode access rights through explanationgenerationproblems,namely,minimalunsatisfiablesets
othermeansaswell(e.g.,securityclearancesandotheradministra- (MUS)andminimalcorrectionsets(MCS)[25,29],bothofwhich
tivecompartmentalizationprotocols).
emergewhenasetofclausesisunsatisfiable.Particularly,anMUS
| Givenanagenta | andthefunctionα,wedefinetheprivacylossρ |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|               | i                                       |     |     | i   |     |     |     |     |     |     |     |     |
ofanexplanation(cid:15)withregardtotheagentasthecountofconstraints 2Formoredetailsontheencoding,pleaserefertothesupplementavailable
athttps://github.com/YODA-Lab/QUERIES.
inaccessibletoit:

6.1 ComputationalEvaluation
Algorithm1:QUERIESAlgorithm
Input:KB,ϕ,a i ,α,k WenowpresentacomputationalevaluationofQUERIESforthefol-
Result:privacy-awareexplanation(cid:15)forϕfora lowingfourqueries,twoforeachquerytype,whereC isanagent’s
|         |       | i   |     |                                  |     |     |     |     | a   |
| ------- | ----- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| forallc | KB do |     |     | clauseandΣaninfeasibleschedule:3 |     |     |     |     |     |
1 ∈
| ifα(a            | ,c)=1then |     |     |                                                |     |     |     |                |     |
| ---------------- | --------- | --- | --- | ---------------------------------------------- | --- | --- | --- | -------------- | --- |
| 2                | i         |     |     | Reason-seekingquery(agent):WhyisC              |     |     |     | a unsatisfied? |     |
| assignweightktoc |           |     |     | •                                              |     |     |     |                |     |
| 3                |           |     |     | Modification-seekingquery(agent):HowtosatisfyC |     |     |     |                | ?   |
|                  |           |     |     | •                                              |     |     |     |                | a   |
Reason-seekingquery(schedule):WhyisΣinfeasible?
ifϕisareason-seekingquerythen
| 4   |     |     |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:15) getMUS(KB,ϕ) Modification-seekingquery(schedule):HowtomakeΣfeasible?
| 5   |     |     |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
elseifϕisamodification-seekingquerythen ← WeranourexperimentsonaMacBookPromachinecomprising
6
7 (cid:15) getMCS(KB,ϕ) an M1 Max processor with 32GB of memory. The time limit was
←
setto500s.OurimplementationofQUERIESiswritteninPython
8 return(cid:15)
|     |     |     |     | and integrates | calls | to MUS and | MCS oracles | through | the PySAT |
| --- | --- | --- | --- | -------------- | ----- | ---------- | ----------- | ------- | --------- |
toolkit[20].4
can be interpreted as explaining why a set of clauses is unsatisfi- To comprehensively evaluate our approach, we ran three sets of
ablebyidentifyingaminimalsetofconflictingclausesthatcausethe
experiments:(1)Todemonstratethescalabilityofourapproach,we
unsatisfiability.AnMUScanthenbeusedtofindareason-seeking
|     |     |     |     | evaluated | it on our | motivating employee |     | shift assignment | problem |
| --- | --- | --- | --- | --------- | --------- | ------------------- | --- | ---------------- | ------- |
explanation: ofvaryingsize;(2)Todemonstratetheimpactofprivacyoraccess
rights,weevaluatedouralgorithmonthesameschedulingproblem,
Proposition1. GivenaknowledgebaseKB andareason-seeking but agents have varying access rights; and (3) To demonstrate the
| queryϕ ,(cid:15) | =M ϕ isareason-seekingexplanationforϕ |     |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
r r \{¬ r } r generalityofourapproach,weevaluateditonanSMT-basedencod-
| ifM isanMUSofKB | ϕ   | .   |     |                                    |     |     |     |     |     |
| --------------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
|                 | ∪{¬ | r } |     | ingofthejob-shopschedulingproblem. |     |     |     |     |     |
PROOF (SKETCH).Theexistenceofareason-seekingqueryϕ im- Experiment 1: Scalability: In this experiment, we vary the scale
r
pliesthatKB =ϕ ,whichinturnimpliesthatKB ϕ = andcomplexityoftheagentschedulingproblembyvaryingthenum-
|     | r   |     | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ∪{¬ }| ⊥ berofagents A,resources R,andtimesteps S intheproblem.
| accordingtothedefinitionofentailment.Thatis,thenegationofϕ |     |     | r   |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                            |     |     |     |     | | | | | | |     | |   | |   |
is inconsistent with a set of constraints from KB and, as such, an Specifically, we created 14 random instances, where each instance
MUS M of KB ϕ exists. If ϕ M, then M ϕ has A = 10 iagents, R = 10 iresources,and S = 10time
|     | ∪{¬ r } | ¬ r ∈ | \{¬ r } | | | | ·   | | | | ·   |     | | | |
| --- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
is satisfiable and M ϕ = ϕ . Therefore, M ϕ is a steps,withitakingthevalues1,1.5,2,...,7.5.Forthedomaincon-
|     | r   | r   | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reason-seekingexplan \ at { io ¬ nfo } rϕ | . \{¬ } (cid:50) straints,weextendedtheonesdescribedinSection2toincludemore
r
agents,shifttypes,andtimesteps,aswellasincludedanadditional
| Similarly, | an MCS explains | how to restore consistency | in an in- |     |     |     |     |     |     |
| ---------- | --------------- | -------------------------- | --------- | --- | --- | --- | --- | --- | --- |
consistentKBbyidentifyingaminimalsetofclausesfromKBsuch constraintdescribingthemaximumnumberofconsecutiveshiftsan
thatwhenremoved,KBbecomessatisfiable.Amodification-seeking employeecanundertakewithoutadayoff.Fortheagentconstraints,
explanationcanbethenbegeneratedviaanMCS: wegenerated5typesofconstraintstoreflectdifferentkindsofprefer-
encessimilartothosepresentedinSection2,andrandomlyassigned
Proposition 2. Given a knowledge base KB and a modification- themtotheagents.Wesetthefractionp = 0.5ofagentsthateach
| seekingqueryϕ | ,C isamodification-seekingexplanationforϕ |     |     |     |     |     |     |     |     |
| ------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
m m agenthasaccessrightsto.Ifanagenta i hasaccessrightstoagent
ifCisanMCSofKB ϕ m andϕ m C. a j ,thena i isawareofallofagenta j ’sconstraints.
|     | ∪{ } | (cid:54)∈ |     |     |     |     |     |     |     |
| --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
Figures3(a)and3(b)plottheruntimesofQUERIESasafunction
The proof of Proposition 2 follows from the fact that a of the cardinalities of the knowledge base KB and the explana-
| |
modification-seekingexplanationforϕ isindeedanMCSofKB tion (cid:15) found,respectively.Unsurprisingly,t heru ntimesincreaseas
|     |     | m   | ∪   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ϕ . |     |     |     | | | |     |     |     |     |     |
{ m } thec ar dinalitiesincrease.Thereasonisthatthesearchspacegrows
Algorithm1presentsthepseudocodeofQUERIES,whichgener-
|     |     |     |     | with KB | ,alsoreflectedin | (cid:15).Also,modification-seekingqueries |     |     |     |
| --- | --- | --- | --- | ------- | ---------------- | ----------------------------------------- | --- | --- | --- |
atesexplanationsforanagenta .Atahighlevel,ititeratesoverall | | | |
i tookl onge rtosolvethanreas o n-seekingqueries.Thereasonisthat
constraintsinKB andassignslargeweightsk >> 1toconstraints ouroff-the-shelfMCSsolver,usedformodification-seekingqueries,
thatarepublictoagenta i withrespecttoaccess-rightsfunctionα. islessefficientthanouroff-the-shelfMUSsolver,usedforreason-
| Then,theMUS(orMCS)solverprioritizestheconstraintswiththe |     |     |     | seekingqueries. |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
largestweights,whichmeansthattheoutputofthesolverisasetof
constraintswiththelargestcumulativesumofweights(i.e.,privacy- Experiment2:AccessRights:Inthisexperiment,weusethesame
|     |     |     |     | employee | shift assignment | problem, | where | we set | the number of |
| --- | --- | --- | --- | -------- | ---------------- | -------- | ----- | ------ | ------------- |
awareexplanation).
|                  |            |                        |         | agents A           | = 40,resources | R                     | = 40,andtimesteps |                       | S = 5.We |
| ---------------- | ---------- | ---------------------- | ------- | ------------------ | -------------- | --------------------- | ----------------- | --------------------- | -------- |
| The completeness | of QUERIES | lies in the assumption | we made |                    |                |                       |                   |                       |          |
|                  |            |                        |         | varythefractionp | | |              | = 0,0.1,0.2,...,1 | | |                   | ofotheragentsthateach | | |      |
forthetwoquerytypes,whichisthatanexplanationforbothquery
|     |     |     |     |     |     | {   | }   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
types always exists. The correctness of QUERIES lies in the cor- agenthasaccessrightsto.
rectnessoftheMUSandMCSsolversandtheassumptionthatkis Figures 4(a), 4(b), and 4(c) plot, as a function of access rights
|     |     |     |     | fraction | p, the runtimes | of QUERIES, | privacy | losses | ρ i((cid:15)) of ex- |
| --- | --- | --- | --- | -------- | --------------- | ----------- | ------- | ------ | -------------------- |
sufficientlylargesuchthatexplanationswiththelargestcumulative
|     |     |     |     | planations,andcardinalityofexplanations |     |     |     | (cid:15),respectively.Similar |     |
| --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | ----------------------------- | --- |
sumofweightsareprivacy-awareexplanations.
|     |     |     |     | tothepreviousexperiment,theruntimesarelargerformodification- |     |     |     | | | |     |
| --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
3 Ca wasrandomlyselectedfromapoolofunsatisfiedclausesofagenta
6 EmpiricalEvaluations
andΣwasgeneratedbyrandomlyflipping20%ofthevaluesofafeasible
schedule.
| Wenowempiricallyevaluateourapproachbothinsimulatedcompu- |     |     |     | 4            |                 |              |     |                          |     |
| -------------------------------------------------------- | --- | --- | --- | ------------ | --------------- | ------------ | --- | ------------------------ | --- |
|                                                          |     |     |     | The          | code repository | is available | at  | https://github.com/YODA- |     |
| tationalexperimentsaswellasinahumanuserstudy.            |     |     |     | Lab/QUERIES. |                 |              |     |                          |     |

|     |     |         | Why(agent)                    |     |        |         |      | Why(agent)                  |     |             |     |     |
| --- | --- | ------- | ----------------------------- | --- | ------ | ------- | ---- | --------------------------- | --- | ----------- | --- | --- |
|     |     | 102     | How(agent)                    |     |        |         | 102  | How(agent)                  |     |             |     |     |
|     |     |         | Why(schedule)                 |     |        |         |      | Why(schedule)               |     |             |     |     |
|     |     | 101     | How(schedule)                 |     |        |         | 101  | How(schedule)               |     |             |     |     |
|     |     | )s(emiT |                               |     |        | )s(emiT |      |                             |     |             |     |     |
|     |     | 100     |                               |     |        |         | 100  |                             |     |             |     |     |
|     |     | 10−1    |                               |     |        |         | 10−1 |                             |     |             |     |     |
|     |     | 10−2    |                               |     |        |         | 10−2 |                             |     |             |     |     |
|     |     | 103     | 104                           | 105 | 106    |         | 100  |                             | 101 |             |     |     |
|     |     |         | CardinalityoftheKnowledgeBase |     | | KB | |         |      | CardinalityoftheExplanation |     | || (cid:15) |     |     |
|     |     |         |                               | (a) |        |         |      |                             | (b) |             |     |     |
Figure3:ResultsofExperiment1ontheScalabilityofQUERIES
| 35  |     |     |     |     |     |     |            |     |          | 45    |     |            |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ----- | --- | ---------- |
|     |     |     |     | 20  |     |     | Why(agent) |     |          |       |     | Why(agent) |
| 30  |     |     |     |     |     |     | How(agent) |     | (cid:15) | || 40 |     | How(agent) |
Why(agent) Why(schedule) noitanalpxEehtfoytilanidraC Why(schedule)
| 25  |     |     |     |     |     |     |     |     |     | 35  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
How(agent) )(cid:15)(ρssoLycavirP 15 How(schedule) How(schedule)
Why(schedule)
| )s(emiT 20 |     |     |     |     |     |     |     |     |     | 30  |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
How(schedule)
|     |     |     |     | 10  |     |     |     |     |     | 25  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15
| 10  |     |     |     |     |     |     |     |     |     | 20  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5
| 5   |     |     |     |     |     |     |     |     |     | 15  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     |     | 0   |     |     |     |     | 10  |     |     |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
|     |     | p   |     |     |     | p   |     |     |     |     | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (a) |     |     |     | (b) |     |     |     |     | (c) |     |
Figure4:ResultsofExperiment2ontheImpactofPrivacyandAccessRights
Why(agent)
How(agent)
|     |     | 102 |     |     |     |     | 102 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Why(schedule)
How(schedule)
|     |     | 101     |     |     |     |         | 101 |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     |     | )s(emiT |     |     |     | )s(emiT |     |     |     |     |     |     |
|     |     | 100     |     |     |     |         | 100 |     |     |     |     |     |
Why(agent)
How(agent)
|     |     | 10−1 |     |     |     |     | 10−1 |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Why(schedule)
How(schedule)
|     |     |     | 103                           |     | 104    |     |     |                             | 102 |             |     |     |
| --- | --- | --- | ----------------------------- | --- | ------ | --- | --- | --------------------------- | --- | ----------- | --- | --- |
|     |     |     | CardinalityoftheKnowledgeBase |     | | KB | |     |     | CardinalityoftheExplanation |     | || (cid:15) |     |     |
|     |     |     |                               | (a) |        |     |     |                             | (b) |             |     |     |
Figure5:ResultsofExperiment3onSMT-basedEncodingofJob-ShopScheduling
seeking queries than reason-seeking queries. However, unlike the on a Satisfability Modulo Theory (SMT) encoding of the job-shop
previous experiment, there is a significant difference in (cid:15) for the scheduling problem [30]. SMT is a decision problem that extends
| |
different queries in this experiment. As the modification-seeking Boolean logic and allows for richer representations of real-world
queriesrequiredlongerexplanations,theytooklongertosolvethan problemswithlogicalformulaethatarebasedonacombinationof
reason-seekingqueries. backgroundtheoriessuchasintegersandreals[13].
Additionally,theruntimesstayrelativelyconstantforallvaluesof Thejob-shopschedulingprobleminvolvesassigningasetofjobs,
p,reflectingthefactthattheruntimesfortheMCSandMUScom- eachwithitsownprocessingtime,tomachinesinawaythatensures
putationsareindependentoftheweightsoftheclauses.Also,asex- all jobs are completed. We encoded this problem in Python using
pected,theprivacylossdecreasesaspincreasessincefewerclauses theZ3solver[12],andgenerated11instancesbyvaryingthenum-
areprivateaspincreases.Finally,aspincreases, (cid:15) eitherdecreases berofjobs,processingtimes,andmachines.FortheMUSandMCS
| |
orremainsconstant,indicatingthatthesolvercanfindshorter(i.e., solvers,weusedoff-the-shelfimplementationsavailablewithinZ3.
better)explanationswhentheexplanationspaceexpandswithlarger Similartothepreviousexperiment,wegeneratedquerieswithanun-
| valuesofp. |     |     |     |     |     |     | satisfiedconstraintandaninfeasibleschedule. |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
Figures5(a)and5(b)plottheruntimesofQUERIESasafunction
Experiment3:SMTandJob-ShopScheduling:Finally,todemon- of the cardinalities KB and (cid:15), respectively. We observed trends
|     |     |     |     |     |     |     |     |     | |   | | | | |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
stratethatourexplainableschedulingframeworkandalgorithmcan similar to those in Experiment 1, attributable to the same reasons
begeneralizedtootherschedulingproblemsaswellasothertypes describedearlier."
| of logic aside | from | propositional | logic, we | evaluate | our approach |     |     |     |     |     |     |     |
| -------------- | ---- | ------------- | --------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     | be included, | while | the remaining |     | participants | (12%) | suggested | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ------------- | --- | ------------ | ----- | --------- | --- |
combinationofbothpublicandprivateinformation.
Inconclusion,ourstudysupportsthehypothesisthatindividuals
preferexplanationscontainingonlypublicinformation,whichthey
perceiveasnotonlymoresatisfactorybutalsomoreequitable..Based
onthesefindings,ourexplanationgenerationframeworkisdesigned
toalignwithpeople’sexpectationsforaschedulingdecisionexpla-
nationinthisparticularcontext.
|           |               |            |         |               |           |               |            | 7 RelatedWork |     |     |     |     |     |     |     |
| --------- | ------------- | ---------- | ------- | ------------- | --------- | ------------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Figure 6: | Human         | user study | results | from          | 60 users: | (a)           | Percentage |               |     |     |     |     |     |     |     |
| of users  | that selected | generic    | and     | privacy-aware |           | explanations; | and        |               |     |     |     |     |     |     |     |
Thereisasmallbodyofliteratureonexplainablescheduling,with
(b)Percentageofusersthatweresatisfied,indifferent,orunsatisfied
EXPRES[28]beingthemostrelevantrelatedwork.ItusesaMILP
withtheprivacy-awareexplanation.
tofindexplanationsforunsatisfieduserpreferences.Nevertheless,it
|     |     |     |     |     |     |     |     | is limited | to only | identifying | a set | of reasons | for | unsatisfied | user |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | ----- | ---------- | --- | ----------- | ---- |
6.2 HumanUserStudy
|        |         |              |       |              |     |                 |     | preferences,      | thus | lacking | the ability | to address | and      | explain | other   |
| ------ | ------- | ------------ | ----- | ------------ | --- | --------------- | --- | ----------------- | ---- | ------- | ----------- | ---------- | -------- | ------- | ------- |
| We now | present | a user study | aimed | at examining |     | the assumptions |     |                   |      |         |             |            |          |         |         |
|        |         |              |       |              |     |                 |     | types of queries, |      | such as | how (or     | why) a     | schedule | can be  | (or is) |
madeinourframework.Inparticular,wehypothesize: (in)feasible. With regards to privacy, EXPRES preserves privacy
|     |     |     |     |     |     |     |     | by post-processing |     | explanations | to  | remove | identifying | reference | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------ | --- | ------ | ----------- | --------- | --- |
Within agent scheduling problems, individuals prefer expla- agents. In contrast, we give a more thorough treatment on this is-
nations containing only public information (e.g., publicly ac- sueaswefoundthatitiskeytousersinouruserstudy.Onasim-
knowledgedrulesandconstraints)overthoseincludingprivate et al.
|             |        |       |            |       |     |          |      | ilar thread, | Cyras | [11] | proposed | an  | argumentation-based |     | ap- |
| ----------- | ------ | ----- | ---------- | ----- | --- | -------- | ---- | ------------ | ----- | ---- | -------- | --- | ------------------- | --- | --- |
| information | (e.g., | other | employees’ | names | and | personal | con- |              |       |      |          |     |                     |     |     |
proachforexplainingwhyascheduleis(ornot)feasibleandwhya
straints),astheyperceivethemasmoresatisfactory.
preferencewasunsatisfiedintheschedule,aswealsotackleinthis
|     |     |     |     |     |     |     |     | paper. The | key differences |     | between | their approach |     | and ours | is that |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------- | -------------- | --- | -------- | ------- |
To evaluate this hypothesis, we conducted a human user study in- theydonotconsideranyprivacypreservationstrategies,theyarere-
volving 60 English-speaking participants recruited through the on- strictedtomakespanschedulingproblems,andtheydidnotprovide
| line platform | Prolific | [26]. | The study | is  | centered | around | the em- |                  |     |            |          |           |          |         |     |
| ------------- | -------- | ----- | --------- | --- | -------- | ------ | ------- | ---------------- | --- | ---------- | -------- | --------- | -------- | ------- | --- |
|               |          |       |           |     |          |        |         | any experimental |     | evaluation | of their | approach. | Finally, | Agrawal | et  |
ployeeshiftassignmentproblemintroducedearlier,withparticipants
al.[1]andBertoluccietal.[3]alsoconsidertheproblemofexplain-
| engaging | in a thought | experiment |     | by assuming |     | the role | of an em- |     |     |     |     |     |     |     |     |
| -------- | ------------ | ---------- | --- | ----------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingschedulingdecisions,however,theirscopeislimitedtospecific
ployeeinahypotheticalcompany.
domainapplications–schedulingMarsroversandoperatingrooms,
| We informed     |             | the participants    | that          | Alice,   | an automated |                  | schedul-  | respectively. |          |      |                |            |           |           |        |
| --------------- | ----------- | ------------------- | ------------- | -------- | ------------ | ---------------- | --------- | ------------- | -------- | ---- | -------------- | ---------- | --------- | --------- | ------ |
| ing agent,was   | responsible |                     | for creatinga |          | schedule     | under            | theprevi- |               |          |      |                |            |           |           |        |
|                 |             |                     |               |          |              |                  |           | A related     | research | area | is explainable |            | planning, | which     | has a  |
| ously described |             | domain constraints, |               | ensuring | that         | this information |           |               |          |      |                |            |           |           |        |
|                 |             |                     |               |          |              |                  |           | larger body   | of work. | Most | of the         | approaches | in        | this area | aim at |
waspublicandknowntoallusers.Participantswereaskedtochoose
|     |     |     |     |     |     |     |     | explaining | planning-specific |     | queries, | such | as why | a plan | is feasi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | -------- | ---- | ------ | ------ | --------- |
apersonalconstraintfromfouravailableoptions,makingthemaware
|     |     |     |     |     |     |     |     | ble/optimal | and why | a particular |     | action is | (or not) | included | in a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------------ | --- | --------- | -------- | -------- | ---- |
ofonlytheirownpersonalconstraint,whiletheremainingagentcon- plan[7,16,31,32,37,39].CloselyrelatedistheworkbyVasileiou
| straints were | considered | private | information. |     | The | participants | then |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ------- | ------------ | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
etal.[35],whichalsousesminimalcorrectionsets(MCS)andmini-
receivedtheirshiftassignments,andwerenotifiedthattheirpersonal
malunsatisfiablesets(MUS)tofindexplanations.However,thekey
constraintwasnotsatisfiedinAlice’sschedule.
differencesbetweentheirapproachandoursisthattheydonotcon-
| Their primary |     | task was | to select | an explanation |     | out | of two op- |               |              |     |          |        |                 |     |           |
| ------------- | --- | -------- | --------- | -------------- | --- | --- | ---------- | ------------- | ------------ | --- | -------- | ------ | --------------- | --- | --------- |
|               |     |          |           |                |     |     |            | sider privacy | preservation |     | and they | take a | philosophically |     | different |
tions: a generic explanation, which contained another employee’s approachoffindingexplanationsbyreconcilingthedifferencesbe-
nameandprivateconstraintasthereasonfortheirunsatisfiedcon-
tweenthementalmodelsoftheexplainerandexplainee.Finally,for
straint,andaprivacy-awareexplanation,whichincludedonlyapub-
|            |             |              |     |      |          |           |       | a further exposition |     | on the | relationship | between | our | approach | and |
| ---------- | ----------- | ------------ | --- | ---- | -------- | --------- | ----- | -------------------- | --- | ------ | ------------ | ------- | --- | -------- | --- |
| lic domain | constraint. | Participants |     | then | answered | questions | about |                      |     |        |              |         |     |          |     |
previousworkssuchasdiagnosisandMUSgeneration,wereferthe
theirchoiceofexplanationandtheirsatisfactionlevels.
readertotheworkbyVasileiouetal.[35,36].
| Figure | 6 presents | the | main results | of  | the study. | The | majority |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(83.4%)ofparticipantspreferredtheprivacy-awareexplanation(Fig-
ure 6(a)). Among those who chose the privacy-aware explanation, 8 Discussion
54%weresatisfied,whiletheremainingparticipantswereeitherin-
different(22%)orunsatisfied(24%),asshowninFigure6(b).Inthe Privacy:Despiteoptimizingforprivacy,explanationsmaystillcon-
analysisofresponsestothejustificationquestion,i.e.,“whytheyse- tain private constraints with respect to the explainee. As such, pri-
lectedtheparticularexplanation”,weobservedacommontrend:the vacy leakage can occur when these explanations are relayed to the
privacy-aware explanation was considered more “informative” and explainee.Toaddressthisissueandpreservetheagents’privacy,we
“equitable” to all employees. Here, informative meant that it con- canpost-processtheexplanationbyabstractingawaytheremaining
tained well-justified rules (i.e., constraints known to them), while private constraints. This process can take different forms, such as
“equitable”impliedthatitwasnotpersonalinthesensethatitdidnot maskingallidentifyingreferencestotheagents’whoseprivatecon-
discloseotheremployees’information.Finally,whenaskedwhether straintsareincludedintheexplanationorbycompletelyretracting
anexplanationforaschedulingdecisionshouldincludeonlypublic theprivateconstraintsfromtheexplanation.
information,onlyprivateinformation,oracombinationofboth,the As an example, consider that Thanos has no access rights to
vastmajority(88%)respondedthatonlypublicinformationshould any of the agent constraints. Then, the reason-seeking explanation

(cid:15) = x , x x that is generated for him unfor- Acknowledgments
| r {      | 4,1,2 ¬  | 4,1,2 ∨¬ | 1,1,2    | }           |            |     |         |     |     |     |     |     |     |
| -------- | -------- | -------- | -------- | ----------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| tunately | includes | Rose’s   | identity | and private | constraint |     | (= x ). |     |     |     |     |     |     |
4,1,2
ThisresearchispartiallysupportedbytheNationalScienceFounda-
| Post-processing |     | (cid:15) r will | allow | us to retract | x   | 4,1,2 from | (cid:15) r and |     |     |     |     |     |     |
| --------------- | --- | --------------- | ----- | ------------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- |
tionunderawards1812619and2232055.Theviewsandconclusions
| mask the | identity     | of Rose | from            | the remaining |            | clause | x 4,1,2  |                                                         |     |     |     |     |     |
| -------- | ------------ | ------- | --------------- | ------------- | ---------- | ------ | -------- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|          |              |         |                 |               |            |        | ¬ ∨      | containedinthisdocumentarethoseoftheauthorsandshouldnot |     |     |     |     |     |
| x ,      | for example, |         | by transforming |               | the clause | to its | general- |                                                         |     |     |     |     |     |
¬ 1,1,2 be interpreted as representing the official policies, either expressed
| ized form | atmost | 1( x | ,x  | ,x  | ,x  | )   | (do- |     |     |     |     |     |     |
| --------- | ------ | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
{ 1,j,t 2,j,t 3,j,t 4,j,t } ∀rj∈R,st∈S orimplied,ofthesponsoringorganizations,agencies,ortheUnited
| mainconstraintC |     | ).  |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3
Statesgovernment.
| Explanation | Delivery: |     | After the | (potential) | abstraction |     | phase, the |     |     |     |     |     |     |
| ----------- | --------- | --- | --------- | ----------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(post-processed)explanationneedstobecommunicatedtotheagent.
References
Unlesstheexplaineeagentisadomainexpert,theexplanationshould
|                     |     |     |              |                 |     |     |             | [1] Jagriti | Agrawal, | Amruta | Yelamanchili, | and Steve | Chien, ‘Using ex- |
| ------------------- | --- | --- | ------------ | --------------- | --- | --- | ----------- | ----------- | -------- | ------ | ------------- | --------- | ----------------- |
| not be communicated |     |     | in a logical | representation, |     | but | rather in a |             |          |        |               |           |                   |
plainableschedulingfortheMars2020rovermission’,arXivpreprint
human-understandableformatsuchasnaturallanguage.Atrivialdi-
arXiv:2011.08733,(2020).
rectioncouldbetoleveragetheexpressivityandsymbolicnatureof [2] CarlosAnsótegui,MiquelBofill,MiquelPalahí,JosepSuy,andMa-
logic.Thatis,wecandefinenaturallanguagetemplatesandusethem teuVillaret,‘Satisfiabilitymodulotheories:Anefficientapproachfor
theresource-constrainedprojectschedulingproblem’,inProceedings
tomapthegeneratedexplanations.Inparticular,noticethateachcon-
|                      |     |     |          |            |          |             |     | of the | Symposium | on Abstraction, |     | Reformulation | and Approximation |
| -------------------- | --- | --- | -------- | ---------- | -------- | ----------- | --- | ------ | --------- | --------------- | --- | ------------- | ----------------- |
| straint “symbolizes” |     | a   | specific | constraint | type and | is grounded | on  |        |           |                 |     |               |                   |
(SARA),pp.2–9,(2011).
(propositional) variables, with each variable denoting a scheduling [3] Riccardo Bertolucci, Carmine Dodaro, Giuseppe Galatà, Marco
element such as an agent, a resource, or a time step. For instance, Maratea,IvanPorro,andFrancescoRicca,‘ExplainingASP-basedop-
(cid:15) = x , x x saysthatRoseisassignedthemorn- eratingroomschedules’,inProceedingsoftheWorkshoponExplain-
| r 4,1,2             |     | 4,1,2 | 1,1,2                                  |     |     |     |     |                                                |     |     |     |     |     |
| ------------------- | --- | ----- | -------------------------------------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| {                   | ¬   | ∨¬    | }                                      |     |     |     |     | ableLogic-BasedKnowledgeRepresentation,(2021). |     |     |     |     |     |
| ingshiftonTuesday(x |     |       | 4,1,2 ),andthateitherRoseorThanoscanbe |     |     |     |     |                                                |     |     |     |     |     |
[4] ArminBiere,MarijnHeule,HansvanMaaren,andTobyWalsh,Hand-
assignedamorningshiftonTuesday( x 4,1,2 x 1,1,2 ).Assuch, bookofSatisfiability,volume336,IOSpress,2021.
|     |     |     |     | {¬  | ∨¬  | }   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alogic-basedexplanationcanbetransformedintoanaturallanguage [5] MiquelBofill,MarcGarcia,JosepSuy,andMateuVillaret,‘MaxSAT-
explanation by identifying and mapping the constraints to their re- basedschedulingofB2Bmeetings’,inProceedingsoftheInternational
spectivepre-defined,naturallanguagetemplates.Anotherpossibility ConferenceonIntegrationofAIandORTechniquesinConstraintPro-
gramming(CPAIOR),pp.65–73,(2015).
istoleverageLargeLanguageModels(LLMs)[6]totranslatelogical [6] RishiBommasani,DrewAHudson,EhsanAdeli,RussAltman,Simran
explanations into natural language. However, the accuracy of such Arora,SydneyvonArx,MichaelSBernstein,JeannetteBohg,Antoine
translationswillneedtobevalidatedthroughadditionalresearchas Bosselut, Emma Brunskill, et al., ‘On the opportunities and risks of
LLMs have been shown to have hallucination issues [40]. Another foundationmodels’,arXivpreprintarXiv:2108.07258,(2021).
|     |     |     |     |     |     |     |     | [7] Tathagata | Chakraborti, | Sarath | Sreedharan, | Yu Zhang, | and Subbarao |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ------ | ----------- | --------- | ------------ |
approachisthroughvisualizationsystems[22,33],thoughthesesys-
|     |     |     |     |     |     |     |     | Kambhampati, |     | ‘Plan explanations |     | as model reconciliation: | Moving |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------ | --- | ------------------------ | ------ |
temswilllikelyneedtobecraftedwithsignificantdomainexpertise. beyond explanation as soliloquy’, in Proceedings of the Interna-
tionalJointConferenceonArtificialIntelligence(IJCAI),pp.156–163,
| Ethical | Considerations: |     | It is paramount |     | to assess | the | ethical im- |     |     |     |     |     |     |
| ------- | --------------- | --- | --------------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
(2017).
[8] WayneChi,SteveChien,andJagritiAgrawal,‘Schedulingwithcom-
| plications | of our | work. | In our | context, | two ethical | considerations |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | ------ | -------- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
plexconsumptiveresourcesforaplanetaryrover’,inProceedingsof
emerge–theexplanationunavoidablyinvolvesprivateinformation,
theInternationalConferenceonAutomatedPlanningandScheduling
| and the | fair resolution |     | of conflicting | agent | constraints. |     | The former |     |     |     |     |     |     |
| ------- | --------------- | --- | -------------- | ----- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
(ICAPS),pp.348–356,(2020).
| concern | can be | addressed | by the | post-processing |     | mechanisms | de- |             |       |                 |     |                 |                 |
| ------- | ------ | --------- | ------ | --------------- | --- | ---------- | --- | ----------- | ----- | --------------- | --- | --------------- | --------------- |
|         |        |           |        |                 |     |            |     | [9] Stephen | Cook, | ‘The complexity | of  | theorem-proving | procedures’, in |
scribedabove.Forthelatter,whilewedonotaddresstheissuedi- ACM Symposium on Theory of Computing (STOC), pp. 151–158,
(1971).
| rectly in | our work, | we  | imagine | that fairness | could | be achieved | by  |                                                                  |     |     |     |     |     |
| --------- | --------- | --- | ------- | ------------- | ----- | ----------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
|           |           |     |         |               |       |             |     | [10] JamesCrawfordandAndrewBaker,‘Experimentalresultsontheappli- |     |     |     |     |     |
employingmulti-objectiveoptimizationtechniques[15,17,19]that
cationofsatisfiabilityalgorithmstoschedulingproblems’,inProceed-
seekabalanceamongconflictingconstraints.
ingsoftheNationalConferenceonArtificialIntelligence(AAAI),pp.
1092–1097,(1994).
Althoughourcurrentframeworkdoesnotpresentdefinitivesolu- [11] Kristijonas Cyras, Dimitrios Letsios, Ruth Misener, and Francesca
tionstothesecomplexissues,thesepotentialdirectionscouldguide Toni, ‘Argumentation for explainable scheduling’, in Proceedings of
the future trajectory of research in this field. Subsequent iterations theAAAIConferenceonArtificialIntelligence(AAAI),pp.2752–2759,
(2019).
shouldintegratetheseconsiderations,workingtowardsnotjustprac- [12] Leonardo De Moura and Nikolaj Bjørner, ‘Z3: An efficient SMT
ticalbutalsoethicallyrobustAIexplanationsystems. solver’,inProceedingsofInternationalConferenceonToolsandAl-
gorithmsfortheConstructionandAnalysisofSystems(TACAS),pp.
337–340,(2008).
|     |     |     |     |     |     |     |     | [13] LeonardoDeMouraandNikolajBjørner,‘Satisfiabilitymodulothe- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
9 Conclusions ories: introduction and applications’, Communications of the ACM,
54(9),69–77,(2011).
|     |     |     |     |     |     |     |     | [14] EmirDemirovic´,NysretMusliu,andFelixWinter,‘Modelingandsolv- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
Inthispaper,wetackledthechallengeofgeneratingexplanationsfor ingstaffschedulingwithpartialweightedMaxSAT’,AnnalsofOpera-
tionsResearch,275,79–99,(2019).
| agent scheduling |     | problems. | We  | proposed | a logic-based |     | framework |                                                                 |     |     |     |     |     |
| ---------------- | --- | --------- | --- | -------- | ------------- | --- | --------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                  |     |           |     |          |               |     |           | [15] MichaelEmmerichandAndréDeutz,‘Atutorialonmultiobjectiveop- |     |     |     |     |     |
capableofgeneratingprivacy-awareexplanationsforreason-seeking
timization:Fundamentalsandevolutionarymethods’,NaturalComput-
andmodification-seekingqueries.Tothebestofourknowledge,our
ing,17(3),585–609,(2018).
| framework | is the | first to | present | a general | approach | that | tackles a |                                                               |     |     |     |     |     |
| --------- | ------ | -------- | ------- | --------- | -------- | ---- | --------- | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
|           |        |          |         |           |          |      |           | [16] MariaFox,DerekLong,andDanieleMagazzeni,‘Explainableplan- |     |     |     |     |     |
broadspectrumofagentschedulingproblemswhilequantifyingand ning’,arXivpreprintarXiv:1709.10256,(2017).
|     |     |     |     |     |     |     |     | [17] NyomanGunantara,‘Areviewofmulti-objectiveoptimization:Meth- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
optimizingforprivacy.Ourexperimentalresultsdemonstratetheef-
odsanditsapplications’,CogentEngineering,5(1),1502242,(2018).
ficacyofourframework,andouruserstudysupportstheimportance
|             |           |     |                 |     |                |     |            | [18] Stefaan | Haspeslagh, | Tommy | Messelis, | Greet | Vanden Berghe, and |
| ----------- | --------- | --- | --------------- | --- | -------------- | --- | ---------- | ------------ | ----------- | ----- | --------- | ----- | ------------------ |
| of privacy, | fairness, | and | informativeness |     | in explanation |     | generation |              |             |       |           |       |                    |
PatrickDeCausmaecker,‘Anefficienttranslationschemeforrepresent-
forschedulingsystems. ingnurserosteringproblemsassatisfiabilityproblems’,inProceedings

oftheInternationalConferenceonAgentsandArtificialIntelligence [38] Jean-Paul Watson, J. Christopher Beck, Adele Howe, and L. Darrell
(ICAART),pp.303–310,(2013). Whitley,‘Problemdifficultyfortabusearchinjob-shopscheduling’,
[19] Carlos Hernández, William Yeoh, Jorge A. Baier, Han Zhang, Luis ArtificialIntelligence,143(2),189–217,(2003).
Suazo, Sven Koenig, and Oren Salzman, ‘Simple and efficient bi- [39] YuZhang,SarathSreedharan,AnaghaKulkarni,TathagataChakraborti,
objectivesearchalgorithmsviafastdominancechecks’,ArtificialIn- HankzHankuiZhuo,andSubbaraoKambhampati,‘Planexplicability
telligence,314,103807,(2023). andpredictabilityforrobottaskplanning’,inProceedingsoftheInter-
[20] AlexeyIgnatiev,AntonioMorgado,andJoaoMarques-Silva,‘PySAT: nationalConferenceonRoboticsandAutomation(ICRA),pp.1313–
APythontoolkitforprototypingwithSAToracles’,inProceedingsof 1320,(2017).
theInternationalConferenceonTheoryandApplicationsofSatisfiabil- [40] TerryYueZhuo,YujinHuang,ChunyangChen,andZhenchangXing,
ityTesting(SAT),pp.428–437,(2018). ‘Red teaming ChatGPT via jailbreaking: Bias, robustness, reliability
[21] MiyukiKoshimura,HidetomoNabeshima,HiroshiFujita,andRyuzo andtoxicity’,arXivpreprintarXiv:2301.12867,(2023).
Hasegawa, ‘Solving open job-shop scheduling problems by SAT en-
coding’,IEICETransactionsonInformationandSystems,93(8),2316–
2318,(2010).
[22] Ashwin Kumar, Stylianos Loukas Vasileiou, Melanie Bancilhon,
AlvittaOttley,andWilliamYeoh,‘VizXP:Avisualizationframework
forconveyingexplanationstousersinmodelreconciliationproblems’,
inProceedingsoftheInternationalConferenceonAutomatedPlanning
andScheduling(ICAPS),pp.701–709,(2022).
[23] Sudip Kundu and Sriyankar Acharyya, ‘Stochastic local search ap-
proachesinsolvingthenurseschedulingproblem’,inProceedingsof
theInternationalConferneceonComputerInformationSystems-Anal-
ysisandTechnologies(CISIM),pp.202–211.
[24] ChuMinLiandFelipManya,‘MaxSAT,hardandsoftconstraints’,in
HandbookofSatisfiability,903–927,IOSpress,(2021).
[25] João Marques-Silva, Federico Heras, Mikolás Janota, Alessandro
Previti,andAntonBelov,‘Oncomputingminimalcorrectionsubsets’,
inProceedingsoftheInternationalJointConferenceonArtificialIntel-
ligence(IJCAI),pp.615–622,(2013).
[26] StefanPalanand ChristianSchitter,‘Prolific:Asubject poolforon-
line experiments’, Journal of Behavioral and Experimental Finance,
17,22–27,(2018).
[27] JosePintoandIgnacioGrossmann,‘Alogic-basedapproachtoschedul-
ingproblemswithresourceconstraints’,Computers&ChemicalEngi-
neering,21(8),801–818,(1997).
[28] Alberto Pozanco, Francesca Mosca, Parisa Zehtabi, Daniele Maga-
zzeni, and Sarit Kraus, ‘Explaining preference-driven schedules: the
expresframework’,inProceedingsoftheInternationalConferenceon
AutomatedPlanningandScheduling,pp.710–718,(2022).
[29] Alessandro Previti and João Marques-Silva, ‘Partial MUS enumera-
tion’,inProceedingsoftheAAAIConferenceofArtificialIntelligence
(AAAI),pp.818–825,(2013).
[30] Sabino Francesco Roselli, Kristofer Bengtsson, and Knut Åkesson,
‘SMTsolversforjob-shopschedulingproblems:Modelscomparison
andperformanceevaluation’,inInternationalConferenceonAutoma-
tionScienceandEngineering(CASE),pp.547–552,(2018).
[31] TranCaoSon,VanNguyen,StylianosLoukasVasileiou,andWilliam
Yeoh,‘Modelreconciliationinlogicprograms’,inEuropeanConfer-
enceonLogicsinArtificialIntelligence(JELIA),pp.393–406,(2021).
[32] Sarath Sreedharan, Tathagata Chakraborti, and Subbarao Kambham-
pati, ‘The emerging landscape of explainable automated planning &
decisionmaking’,inProceedingsoftheInternationalJointConference
onArtificialIntelligence(IJCAI),pp.4803–4811,(2020).
[33] KarthikValmeekam,SarathSreedharan,SailikSengupta,andSubbarao
Kambhampati,‘RADAR-X:aninteractivemixedinitiativeplanningin-
terfacepairingcontrastiveexplanationsandrevisedplansuggestions’,
inProceedingsoftheInternationalConferenceonAutomatedPlanning
andScheduling(ICAPS),pp.508–517,(2022).
[34] JorneVandenBergh,JeroenBeliën,PhilippeDeBruecker,ErikDe-
meulemeester,andLiesjeDeBoeck,‘Personnelscheduling:Alitera-
turereview’,EuropeanJournalofOperationalResearch,226(3),367–
385,(2013).
[35] StylianosLoukasVasileiou,AlessandroPreviti,andWilliamYeoh,‘On
exploitinghittingsetsformodelreconciliation’,inProceedingsofthe
AAAI Conference on Artificial Intelligence (AAAI), pp. 6514–6521,
(2021).
[36] StylianosLoukasVasileiou,WilliamYeoh,andTranCaoSon,‘Onthe
relationshipbetweenKRapproachesforexplainableplanning’,arXiv
preprintarXiv:2011.09006,(2020).
[37] Stylianos Loukas Vasileiou, William Yeoh, Tran Cao Son, Ashwin
Kumar, Michael Cashmore, and Daniele Magazzeni, ‘A logic-based
explanation generation framework for classical and hybrid planning
problems’,JournalofArtificialIntelligenceResearch,73,1473–1534,
(2022).