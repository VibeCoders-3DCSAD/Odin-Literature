---
conversion_metadata:
  converted_at: "2026-07-21T13:33:43Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Hu X. et al.pdf"
  source_pdf_sha256: "7f64317b7eb44c629665a64a1b6e4aac8a37bd233eebfe555e3ebc4767973a57"
  page_count: 26
  markdown_char_count: 209124
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Two-Stage Predict+Optimize for Mixed Integer Linear
Programs with Unknown Parameters in Constraints

Xinyi Hu1, Jasper C.H. Lee2, Jimmy H.M. Lee1
1Department of Computer Science and Engineering
The Chinese University of Hong Kong, Shatin, N.T., Hong Kong
2Department of Computer Sciences & Institute for Foundations of Data Science
University of Wisconsin–Madison, WI, USA
{xyhu,jlee}@cse.cuhk.edu.hk, jasper.lee@wisc.edu

Abstract

Consider the setting of constrained optimization, with some parameters unknown
at solving time and requiring prediction from relevant features. Predict+Optimize
is a recent framework for end-to-end training supervised learning models for
such predictions, incorporating information about the optimization problem in the
training process in order to yield better predictions in terms of the quality of the
predicted solution under the true parameters. Almost all prior works have focused
on the special case where the unknowns appear only in the optimization objective
and not the constraints. Hu et al. proposed the first adaptation of Predict+Optimize
to handle unknowns appearing in constraints, but the framework has somewhat
ad-hoc elements, and they provided a training algorithm only for covering and
packing linear programs. In this work, we give a new simpler and more powerful
framework called Two-Stage Predict+Optimize, which we believe should be the
canonical framework for the Predict+Optimize setting. We also give a training
algorithm usable for all mixed integer linear programs, vastly generalizing the
applicability of the framework. Experimental results demonstrate the superior
prediction performance of our training framework over all classical and state-of-
the-art methods.

1

Introduction

Optimization problems are prevalent in modern society, and yet the problem parameters are not
always available at the time of solving. For example, consider the real-world application scenario
of stocking a store: as store managers, we need to place monthly orders for products to stock in the
store. We want to stock products that sell fast and yield high profits, as much of them as possible,
subject to the hard constraint of limited storage space. However, orders need to be placed two weeks
in advance of the monthly delivery, and the customer demand next month cannot be known exactly
at the time of order placement. In this paper, we consider the supervised learning setting, where
the unknown parameters can be predicted from relevant features, and there are sufficient historical
(features, parameters) pairs as training data for a prediction model. The goal, then, is to learn a
prediction model from the training data such that, if we plug in the estimated parameters into the
optimization problem and solve for an estimated solution, the estimated solution remains a good
solution even after the true parameters are revealed.

The classic approach to the problem would be to train a simple regression model, based on standard
losses such as (regularized) ℓ2 loss, to predict parameters from the features. It is shown, however, that
having a small prediction error in the parameter space does not necessarily mean that the estimated
solution performs well under the true parameters. The recent framework of Predict+Optimize, by

37th Conference on Neural Information Processing Systems (NeurIPS 2023).

---

<!-- PAGE 2 -->

Elmachtoub and Grigas [7], instead proposes the more effective regret loss for training, which
compares the solution qualities of the true optimal solution and the estimated solution under the
true parameters. Subsequent works [6, 8, 10, 13, 17, 19, 27] have since appeared in the literature,
applying the framework to more and wider classes of optimization problems as well as focusing on
speed-vs-prediction accuracy tradeoffs.

However, all these prior works focus only on the case where the unknown parameters appear in the
optimization objective, and not in the constraints. The technical challenge for the generalization
is immediate: if there were unknown parameters in the constraints, the estimated solution might
not even be feasible under the true parameters revealed afterwards! Thus, in order to tackle the
Predict+Optimize setting with unknowns in constraints, the recent work of Hu et al. [12] presents
the first such adaptation on the framework: they view the estimated solution as representing a
soft commitment. Once the true parameters are revealed, corrective action can be taken to ensure
feasibility, potentially at a penalty corresponding to the real-life cost of (partially) reneging on a soft
commitment. Their framework captures application scenarios whenever such correction is possible,
and requires the practitioner to specify both the correction mechanism and the penalty function. These
data can be determined and derived from the specific application scenario. As an example, in the
product-stocking problem, an additional unknown parameter is the storage space, because it depends
on how the current products in the store sell before the new order arrives. We need to place orders
two weeks ahead based on predicted storage space. The night before the order arrives, we know
the precise available space, meaning that the unknown parameter is revealed. A possible correction
mechanism then is to throw away excess products that the store cannot keep, while incurring the
penalty that is the retail price of the products, as well as disposal fees.

While the Hu et al. [12] framework does capture many application scenarios, there are important
shortcomings. In their framework, they require the practitioner to specify a correction function
that amends an infeasible solution into a feasible solution. However, the derivation of a correction
function can be rather ad-hoc in nature. In particular, given an infeasible estimated solution, there
may be many ways to transform the solution into a feasible one, and yet their framework requires
the practitioner to pick one particular way. This leads to the second downside: it is difficult to give a
general algorithmic framework that applies to a wide variety of optimization problems. Hu et al. had
to restrict their attention only to packing and covering linear programs, for which they could propose
a generic correction function. In this work, we aim to vastly generalize the kinds of optimization
problems that Predict+Optimize can tackle under uncertainty in the constraints. In addition, the
approach of Hu et al. fails to handle the interesting situation in which post-hoc correction is still
desirable when the estimated solution is feasible but not good under the true parameters.

Our contributions are three-fold:

• To mitigate the shortcomings of the prior work, we propose and advocate a new framework, which
we call Two-Stage Predict+Optimize1, that is both conceptually simpler and more expressive in terms
of the class of optimization problems it can tackle. The key idea for the new framework is that the
correction function is unnecessary. All that is required is a penalty function that captures the cost of
modifying one solution to another. A penalty function is sufficient for defining a correction process:
we formulate the correction process itself as a “Stage 2” optimization problem, taking the originally
estimated solution as well as the penalty function into account.

• Under this framework, we further propose a general end-to-end training algorithm that applies not
only to packing and covering linear programs, but also to all mixed integer linear programs (MILPs).
We adapt the approach of Mandi and Guns [18] to give a gradient method for training neural networks
to predict parameters from features.

• We apply the proposed method to three benchmarks to demonstrate the superior empirical perfor-
mance over classical and state-of-the-art training methods.

2 Background

In this section, we give basic definitions for optimization problems and the Predict+Optimize setting
[7], and describe the state-of-the-art framework [12] for Predict+Optimize with unknown parameters

1The literature sometimes uses “two-stage" to mean approaches where the prediction is agnostic to the

optimization problem. Here, “two-stage" refers to the soft commitment and the correction.

2

---

<!-- PAGE 3 -->

in constraints. The theory is stated in terms of minimization but applies of course also to maximization,
upon appropriate negation. Without loss of generality, an optimization problem (OP) P can be defined
as finding:

x∗ = arg min

obj(x)

s.t. C(x)

where x ∈ Rd is a vector of decision variables, obj : Rd → R is a function mapping x to a real
objective value that is to be minimized, and C is a set of constraints that must be satisfied over x. We
call x∗ an optimal solution and obj(x∗) the optimal value. A parameterized optimization problem
(Para-OP) P (θ) is an extension of an OP P :

x

x∗(θ) = arg min

obj(x, θ)

s.t. C(x, θ)

x

where θ ∈ Rt is a vector of parameters. The objective obj(x, θ) and constraints C(x, θ) can both
depend on θ. When the parameters are known, a Para-OP is just an OP.
In the Predict+Optimize setting [7], the true parameters θ ∈ Rt for a Para-OP are not known at
solving time, and estimated parameters ˆθ are used instead. Suppose each parameter is estimated by
m features. The estimation will rely on a machine learning model trained over n observations of a
training data set {(A1, θ1), . . . , (An, θn)} where Ai ∈ Rt×m is a feature matrix for θi, in order to
yield a prediction function f : Rt×m → Rt predicting parameters ˆθ = f (A).
Solving the Para-OP using the estimated parameters, we obtain an estimated solution x∗(ˆθ). When
the unknown parameters appear in constraints, one major challenge is that the feasible region is only
approximated at solving time, and hence the estimated solution may be infeasible under the true
parameters. Fortunately, in certain applications, the estimated solution is not a hard commitment, but
only represents a soft commitment that can be modified once the true parameters are revealed. Hu et
al. [12] propose a Predict+Optimize framework for such applications. The framework is as follows:
i) the unknown parameters are estimated as ˆθ, and an estimated solution x∗(ˆθ) is solved using the
estimated parameters, ii) the true parameters θ are revealed, and if x∗(ˆθ) is infeasible under θ, it is
corr(ˆθ, θ) while potentially incurring some penalty, and finally
amended into a corrected solution x∗
corr(ˆθ, θ) is evaluated according to the sum of both the objective, under the true
iii) the solution x∗
parameters θ, and the incurred penalty from correction.
More formally, a correction function takes an estimated solution x∗(ˆθ) and true parameters θ and
corr(ˆθ, θ) that is feasible under θ. A penalty function P en(x∗(ˆθ) →
returns a corrected solution x∗
corr(ˆθ, θ) and returns a non-
corr(ˆθ, θ)) takes an estimated solution x∗(ˆθ) and the corrected solution x∗
x∗
negative penalty. Both the correction function and the penalty function should be chosen according to
corr(ˆθ, θ) is evaluated using
the precise application scenario at hand. The final corrected solution x∗
corr(ˆθ, θ) and the penalty
the post-hoc regret, which is defined with respect to the corrected solution x∗
corr(ˆθ, θ)). The post-hoc regret is the sum of two terms: (a) the difference
function P en(x∗(ˆθ) → x∗
corr(ˆθ, θ) under the
in objective between the true optimal solution x∗(θ) and the corrected solution x∗
true parameters θ, and (b) the penalty that the correction process incurs. Mathematically, the post-hoc
regret function P Reg(ˆθ, θ) : Rt × Rt → R≥0 (for minimization problems) is:

where obj(x∗

P Reg(ˆθ, θ) = obj(x∗

corr(ˆθ, θ), θ) − obj(x∗(θ), θ) + P en(x∗(ˆθ) → x∗
(1)
corr(ˆθ, θ), θ) is the corrected optimal value and obj(x∗(θ), θ) is the true optimal value.
Given the post-hoc regret as a loss function, the empirical risk minimization principle dictates that we
choose the prediction function to be the function f from the set of models F attaining the smallest
average post-hoc regret over the training data:

corr(ˆθ, θ))

f ∗ = arg min

f ∈F

1
n

n
(cid:88)

i=1

P Reg(f (Ai), θi)

(2)

3 Two-stage Predict+Optimize Framework

While the prior work by Hu et al. [12] is the first Predict+Optimize framework for unknowns in
constraints, and is indeed applicable to a good range of applications, it has several shortcomings.

3

---

<!-- PAGE 4 -->

First, the framework requires mathematically formalizing both a penalty function and a correction
function from the application scenario, and essentially imposes differentiability assumptions on the
correction function for the framework to be usable. The ad-hoc nature of writing down a correction
function limits the practical applicability of the framework. Second, as a result of needing a single
(differentiable) correction function, Hu et al. [12] needed to restrict their attention to only packing
and covering linear programs, in order to derive a general correction function that is applicable to all
the instances. This also significantly limits the immediate applicability of their framework. Third,
their framework only corrects an estimated solution when it is infeasible under the true parameters.
Yet, there are applications where corrections are possible even when the estimated solution were
feasible, but just not very good under the true parameters.

In this paper, we advocate using a simpler yet more powerful framework, which we call Two-Stage
Predict+Optimize, addressing all of the above shortcomings. The simplified perspective will allow us
to discuss more easily how to handle the entire class of mixed integer linear programs (MILPs) instead
of being restricted to just packing and covering linear programs. Since MILPs include all optimization
problems in NP (under a reasonable definition of NP for optimization problems), our framework
is significantly more applicable in practice. We will describe the Two-Stage Predict+Optimize
framework below, and discuss its application to MILPs in the next section.

Our framework is simple: we forgo the idea of a correction function and treat correction itself as
an optimization problem, based on the penalty function, the estimated solution and the revealed
true parameters. Recall the Hu et al. view of Predict+Optimize under uncertainties in constraints:
the estimated solution is a form of soft commitment, which can be modified at a cost once the true
parameters are revealed. The penalty function describes the cost of changing from an estimated
solution to a final solution. The main observation is that, given an estimated solution and the
revealed parameters, we should in fact solve a new optimization problem, formed by applying the true
parameters to the original optimization, and adding the penalty function to the objective. The final
solution from this new optimization thus takes the penalty of correction into account. This approach
yields three immediate advantages. First, the practitioner no longer needs to specify a correction
function, thus reducing the ad-hoc nature of the framework. Second, even feasible solutions are
allowed to be modified after the true parameters are revealed if the penalty of doing so is not infinity.
Third, conditioned on the same penalty function, the solution quality from our two-stage optimization
approach is always at least as good as that from using any correction function. The last advantage is
presented as Proposition A.1.

Now we formally define the Two-Stage Predict+Optimize framework.
I. In Stage 1, the unknown parameters are estimated as ˆθ from features. The practitioner then solves
the Stage 1 optimization, which is the Para-OP using the estimated parameters, to obtain the Stage 1
solution x∗
1. The Stage 1 solution should be interpreted as some form of soft commitment, that we
get to modify in Stage 2 at extra cost/penalty. Assuming the notation of the Para-OP in Section 2, the
Stage 1 OP can be formulated as:

x∗
1 = arg min

x

obj(x, ˆθ)

s.t. C(x, ˆθ)

II. At the beginning of Stage 2, the true parameters θ are revealed. The Stage 2 optimization problem
augments the original Stage 1 problem by adding a penalty term P en(x∗
2, θ) to the objective,
which accounts for the penalty (modelled from the application scenario) for changing from the
softly-committed Stage 1 solution x∗
2. The Stage 2 OP can
then be formulated as:
x∗
2 = arg min

1 to the new Stage 2 and final solution x∗

obj(x, θ) + P en(x∗

1 → x, θ)

s.t. C(x, θ)

1 → x∗

x

Solving the Stage 2 problem yields the final Stage 2 “corrected” solution x∗
2.
III. The Stage 2 solution x∗

2 is evaluated according to the analogous post-hoc regret, as follows:

P Reg(ˆθ, θ) = obj(x∗

2, θ) + P en(x∗

1 → x∗

2, θ) − obj(x∗(θ), θ)

where again, x∗(θ) is an optimal solution of the Para-OP under the true parameters θ. Note that the
post-hoc regret depends on all of a) the predicted parameters, b) the induced Stage 1 solution, c) the
true parameters and d) the final Stage 2 solution.

To see this new framework applies in practice, the following example expands on the product-stocking
problem in the introduction.

4

---

<!-- PAGE 5 -->

Example 1. Consider the product-stocking problem again, where regular orders have to be placed
two weeks ahead of monthly deliveries. Since the available space at the time of delivery is unknown
when we place the regular orders, depending on the sales over the next two weeks, we need to make
a prediction on the available space to make a corresponding order. We learn the predictor using
historical sales records from features such as time-of-year and price. Then, we use the predicted
available space to optimize for the regular order we place. This is the Stage 1 solution.

The night before the order arrives, the unknown constraint parameter, i.e. the precise available space,
is revealed. We can then check if we have over-ordered or under-ordered. In the case of over-ordering,
we would have to call and ask the wholesale company to drop some items from the order. The
company would perhaps allow taking the items off the final bill, but naturally they have a surcharge
for last-minute changes. Similarly, if we under-ordered, we might request the wholesale company to
send us more products, again naturally with a surcharge for last-minute ordering. The updated order
is the Stage 2 decision. The incurred wholesaler surcharges induce the penalty function.

A reader who is familiar with the literature on two-stage optimization problems may note that the
above framework is phrased slightly differently from some other two-stage problem formulations. In
particular, some two-stage frameworks phrase Stage 1 solutions as hard commitments, and include
recourse variables in both stages of optimization to model what changes are made in Stage 2. We
show in Appendix A.1 how our framework can capture this other perspective, and in general discuss
how problem modelling can be done in our new framework.

The reader may also wonder: what about application scenarios where the (Stage 1) estimated solution
is a hard commitment, and there is absolutely no correction/recourse available? In Appendix A.2, we
discuss how our framework is still useful and applicable for learning in these situations.

We also give a more detailed comparison, in Appendix A.3, between our new Two-Stage Pre-
dict+Optimize framework and the prior Hu et al. framework. Technically, if we ignored differen-
tiability issues, the two frameworks are mathematically equivalent in expressiveness. However, we
stress that our new framework is both conceptually simpler and easier to apply to a far wider class
of optimization problems. We show concretely in the next section how to end-to-end train a neural
network for this framework for all MILPs, vastly generalizing the method of Hu et al. which is
restricted to packing and covering (non-integer) linear programs. In addition, Appendix A.3 also
states and proves Proposition A.1, that if we fix an optimization problem, a prediction model and a
penalty function, then the solution quality from our two-stage approach is always at least as good as
using the correction function approach.

4 Two-Stage Predict+Optimize on MILPs

In this section, we describe how to give an end-to-end training method for neural networks to predict
unknown parameters from features, under the Two-Stage Predict+Optimize framework. The following
algorithmic method is applicable whenever both stages of optimization are expressible as MILPs.
Due to the page limit, the discussion in this section is high-level and brief, with all the calculation
details deferred to Appendix B.

The standard way to train a neural network is to use a gradient-based method. In the Two-Stage
Predict+Optimize framework, we use the post-hoc regret P Reg as the loss function. Therefore, for
each edge weight we in the neural network, we need to compute the derivative dP Reg
. Using the law
dwe
of total derivative, we get

dP Reg(ˆθ, θ)
dwe

=

∂P Reg(ˆθ, θ)
∂x∗
2

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)x∗

1

∂x∗
2
∂x∗
1

∂x∗
1
∂ ˆθ

∂ ˆθ
∂we

+

∂P Reg(ˆθ, θ)
∂x∗
1

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)x∗

2

∂x∗
1
∂ ˆθ

∂ ˆθ
∂we

(3)

As such, we wish to calculate each term on the right hand side.
The easiest term to handle is ∂ ˆθ
∂we
can be directly calculated by standard backpropagation [25]. As for the terms ∂P Reg(ˆθ,θ)
∂P Reg(ˆθ,θ)
∂x∗
1

, they are easily calculable whenever both the optimization objective and penalty

, since ˆθ is the neural network output, and so the derivatives

(cid:12)
(cid:12)
(cid:12)x∗

and

∂x∗
2

1

function are smooth, and in fact linear as in the case of MILPs. What remains are the terms ∂x∗
2
∂x∗
1

and

(cid:12)
(cid:12)
(cid:12)x∗

2

5

---

<!-- PAGE 6 -->

. The challenge is that x∗

2 is the solution of a MILP optimization (Stage 2) that uses x∗

∂x∗
1 as its
1
∂ ˆθ
1 depends on ˆθ through a MILP (Stage 1).
parameters, i.e., differentiate through a MILP. Similarly, x∗
Since MILP optima may not change under minor parameter perturbations, the gradients can be either
0 or non-existent, which are uninformative. We thus need to compute some approximation in order to
get useful training signals.

Our approach, inspired by the work of Mandi and Guns [18], is to define a new surrogate loss
function (cid:94)P Reg that is differentiable and produces informative gradients. Prior works related to
learning unknowns in constraints [1, 2, 27] give ways of differentiating through LPs or LPs with
regularizations. These works can be used in place of the proposed approach. However, experiments
in Appendix E demonstrate that the proposed approach performs at least as well in post-hoc regret
performance as the others, while being faster. We show the construction of the proposed approach
below, and note that it does not have a simple closed form. Nonetheless, we can compute its gradients.

The rest of the section assumes that both stages of optimization are expressible as a MILP in the
following standard form:

x∗ = arg min

x

c⊤x s.t. Ax = b, Gx ≥ h, x ≥ 0, xS ∈ Z

(4)

with decision variables x ∈ Rd and problem parameters c ∈ Rd, A ∈ Rp×d, b ∈ Rp, G ∈ Rq×d,
h ∈ Rq. The subset of indices S denotes the set of variables that are under integrality constraints.
Since the unknown parameters may appear in any combination of c, A, b, G and h in the Stage 1
optimization for x∗
1, the surrogate loss function construction needs computable and informative
∂c , ∂x∗
gradients for all of ∂x∗
We follow the interior-point based approach of Mandi and Guns [18], used also by Hu et al. [12].
Consider the following convex relaxation of (4), for a fixed value of µ ≥ 0:

∂G and ∂x∗
∂h .

∂A , ∂x∗

∂b , ∂x∗

x∗ = arg min

c⊤x − µ

x,s

d
(cid:88)

i=1

ln(xi) − µ

q
(cid:88)

i=1

ln(si) s.t. Ax = b, Gx − s = h

(5)

∂c , ∂x

∂b , ∂x

∂A , ∂x

∂G and ∂x

This is a relaxation of (4) by i) dropping all integrality constraints, ii) introducing slack variables
s ≥ 0 to turn Gx ≥ h into Gx − s = h and iii) replacing both the x ≥ 0 and s ≥ 0 constraints
with the logarithm barrier terms in the objective, with multiplier µ ≥ 0. The observation is that the
gradients ∂x
∂h for (5) are all well-defined, computable and informative for a fixed
value of µ ≥ 0: Slater’s condition holds for (5), and so the KKT conditions must be satisfied at the
optimum (x∗, s∗) of (5). We can thus compute all the relevant gradients via differentiating the KKT
conditions, using the implicit function theorem. We give all the calculation details in Appendix B.
Given the above observation, we then aim to construct the surrogate loss function by replacing the x∗
1
and x∗
2, which are supposed to solved using MILP (4), with a) (cid:101)x1 that is solved from program (5)
relaxation of the Stage 1 optimization problem, using the predicted parameters ˆθ and b) (cid:101)x2 that is
solved from the program (5) relaxed version of Stage 2 optimization, using (cid:101)x1 and the true parameters
θ. The only remaining question then, is, which values of µ do we use for the two relaxed problems?

Given a MILP in the form of (4), the interior-point based solver of Mandi and Guns [18] generates
and solves (5) for a sequence of decreasing non-negative µ, with a termination condition that µ cannot
be smaller than some cutoff value. Thus, we simply choose the cutoff value to use as “µ” in (5),
which then completes the definition of the surrogate loss (cid:94)P Reg.
Algorithmically, we train the neural network on the surrogate loss (cid:94)P Reg as follows: given predicted
parameters, we run the Mandi and Guns solver to get the optimal solution (x∗, s∗) for the final value
of µ. We can then compute the gradient of the output solution with respect to any of the problem
parameters using the calculations in Appendix B, combined with backpropagation, to yield d(cid:94)P Reg
dwe
according to Equation (3).

In Appendix C, we give three example application scenarios, along with their penalty functions, that
our training approach can handle. These problems are: a) an alloy production problem, for factory
trying to source ores under uncertainty in chemical compositions in the raw materials, b) a variant of
the classic 0-1 knapsack with unknown weights and rewards, and c) a nurse roster scheduling problem
with unknown patient load. We show explicitly in Appendix C how both stages of optimization

6

---

<!-- PAGE 7 -->

Table 1: Relevant problem sizes of the three benchmarks.

Problem name
Dimension of x
Number of constraints
Number of unknown parameters
Number of features (per parameter)

Brass alloy production
10
12
20
4096

Titanium-alloy production
10
14
40
4096

0-1 knapsack Nurse scheduling problem

10
21
10
4096

315
846
21
8

can be formulated as MILPs for these applications, and apply the Appendix B calculations to yield
gradient computation formulas for the surrogate loss (cid:94)P Reg for these problems.
A limitation of our approach is the requirement that both stages must be expressible as MILPs,
constraining the optimization objectives to be linear in the MILP decision variables. This contrasts
the Hu et al. framework [12] which handles non-linear penalties. We point out that even MILPs can
handle some non-linearity by using extra decision variables: for example, the absolute-value function.
Moreover, the Appendix B gradient calculations can be adapted to handle general differentiable
non-linear objectives. We present only MILPs as a main overarching application for this paper
because of their widespread use in discrete optimization, with readily available solvers.

5 Experimental Evaluation

We evaluate the proposed method2 on three benchmarks described in Section 4 and Appendix C. Table
1 reports the relevant benchmark problem sizes. We compare our method (2S) with the state of the art
Predict+Optimize method, IntOpt-C [12], and 5 classical regression methods [9]: ridge regression
(Ridge), k-nearest neighbors (k-NN), classification and regression tree (CART), random forest (RF),
and neural network (NN). All of these methods use their classic loss function to train the prediction
models. At test time, to ensure the feasibility of the solutions when computing the post-hoc regret,
we perform Stage 2 optimization on the estimated solutions for these classical regression methods
before evaluating the final solution. Additionally, CombOptNet [23] is a different method focusing
on learning unknowns in constraints, but with a different goal and loss function. We experimentally
compare our proposed method with CombOptNet on the 0-1 knapsack benchmark—the only with
available CombOptNet code. We also present a qualitative comparison in Section 6.

In the following experiments, we will need to take care to distinguish two-stage optimization as a
training technique (Section 4) and as an evaluation framework (Section 3). We will denote our training
method as “2S” in the experiments, and when we say “Two-Stage Predict+Optimize” framework,
we always mean it as an evaluation framework. 2S is always evaluated according to the Two-Stage
Predict+Optimize framework. As explained above, we will also evaluate all the classical training
methods using the Two-Stage Predict+Optimize framework. For our comparison with the prior work
of Hu et al. [12], we will also distinguish their training method and evaluation framework. The name
“IntOpt-C” always refers to their training method using their correction function. We will simply
call their evaluation framework the “Hu et al. framework” or with similar phrasing (see Section 2 to
recall details). IntOpt-C will sometimes be evaluated using our new Two-Stage Predict+Optimize
framework, and sometimes the prior framework of Hu et al. [12] using their correction function.

The methods of k-NN, RF, NN, and IntOpt-C as well as 2S have hyperparameters, which we tune via
cross-validation. We include the hyperparameter types and chosen values in Appendix D. In the main
paper we only report the prediction performances. See Appendix H for runtime comparisons.

Alloy Production Problem The alloy production problem is a covering LP, see Appendix C.1 for
the practical motivation and LP model. Since Hu et al. [12] also experimented on this problem, we
use it to compare our 2S method with IntOpt-C [12], using the same dataset and experimental setting.

We conduct experiments on the production of two real alloys: brass and an alloy blend for strength-
ening Titanium. For brass, 2 kinds of metal materials, Cu and Zn, are required [14]. The blend of
the two materials are, proportionally, req = [627.54, 369.72]. For the titanium-strengthening alloy,
4 kinds of metal materials, C, Al, V, and Fe, are required [15]. The blend of the four materials are
proportional to req = [0.8, 60, 40, 2.5]. We use the same real data as that used in IntOpt-C [12] as
numerical values in our experiment instances. In this dataset [23], each unknown metal concentration

2Our implementation is available at https://github.com/Elizabethxyhu/NeurIPS_Two_Stage_Predict-Optimize

7

---

<!-- PAGE 8 -->

Table 2: Comparison of the Two-Stage Predict+Optimize framework and the Hu et al. framework on
the alloy production problem.

PReg

Alloy

Brass

Titanium-alloy

Penalty factor
0.25±0.015
0.5±0.015
1±0.015
2±0.015
4±0.015
8±0.015
0.25±0.015
0.5±0.015
1±0.015
2±0.015
4±0.015
8±0.015

Two-Stage Predict
+Optimize Framework
43.87±2.73
65.71±4.81
88.75±5.91
123.90±6.84
161.86±8.49
194.06±13.09
4.52±0.47
6.03±0.62
8.58±0.74
12.17±1.24
16.10±1.06
19.69±0.91

Hu et al.
Framework
68.16±6.26
82.91±5.45
107.64±6.85
150.47±12.99
178.69±10.09
206.84±12.51
6.45±0.81
7.90±0.56
10.73±0.81
14.17±1.31
17.48±0.99
21.08±1.91

Table 3: Mean post-hoc regrets and standard deviations for the alloy production problem using the
Two-Stage Predict+Optimize framework.

PReg

Alloy

Brass

Titanium-alloy

Penalty factor
0.25±0.015
0.5±0.015
1±0.015
2±0.015
4±0.015
8±0.015
0.25±0.015
0.5±0.015
1±0.015
2±0.015
4±0.015
8±0.015

2S

IntOpt-C

Ridge

k-NN

CART

RF

NN

TOV

43.87±2.73
65.71±4.81
88.75±5.91
123.90±6.84
161.86±8.49
194.06±13.09
4.52±0.47
6.03±0.62
8.58±0.74
12.17±1.24
16.10±1.06
19.69±0.91

45.27±3.35
67.69±4.25
89.83±4.79
125.46±9.26
164.94±10.33
200.42±8.51
4.72±0.58
6.23±0.64
8.71±0.95
12.31±1.31
16.97±1.70
20.80±1.74

60.80±2.55
71.12±3.48
91.82±6.41
133.18±12.98
215.87±26.54
381.30±53.75
6.43±0.39
7.71±0.45
10.26±0.62
15.37±1.03
25.60±1.89
46.04±3.65

63.32±4.39
74.36±5.69
96.52±8.90
140.77±16.02
229.22±30.74
406.19±60.42
6.13±0.34
7.27±0.39
9.55±0.52
14.11±0.84
23.24±1.56
41.49±3.03

77.80±6.37
93.67±7.03
125.50±9.49
189.12±16.10
316.31±30.95
570.75±61.42
7.07±0.45
8.57±0.45
11.57±0.52
17.57±0.80
29.57±1.53
53.57±3.10

60.85±2.35
70.86±3.29
90.97±6.14
131.12±12.48
211.40±25.56
372.01±51.82
5.75±0.48
6.76±0.55
8.76±0.72
12.78±1.11
20.81±1.93
36.88±3.63

64.96±3.58
74.32±2.90
93.12±4.24
130.67±10.52
205.76±24.33
355.96±52.25
6.56±0.59
7.38±0.67
9.03±0.84
12.34±1.21
18.95±2.00
32.16±3.60

312.02±6.94

30.27±0.54

is related to 4096 features. For experiments on both alloys, 350 instances are used for training and
150 instances for testing the model performance. For NN, IntOpt-C, and 2S, we use a 5-layer fully
connected network with 512 neurons per hidden layer.

In the penalty function described in Appendix C.1, we need to choose a penalty factor/multiplier for
each supplier. We conduct experiments on 6 types of penalty factor (σ) settings: 6 vectors where
each entry is i.i.d. uniformly sampled from [0.25 ± 0.015], [0.5 ± 0.015], [1.0 ± 0.015], [2.0 ± 0.015],
[4.0 ± 0.015], and [8.0 ± 0.015] respectively. This random sampling of σ ensures that the penalty
factor for each supplier is different, but remains roughly on the same scale.

The first experiment we run compares 2S+Two-Stage Predict+Optimize framework with IntOpt-C+Hu
et al. framework. Specifically, we compare a) using 2S for training and evaluating using the Two-Stage
Predict+Optimize framework in Section 3, versus b) using IntOpt-C for training and evaluating using
the same correction function from training, according to the Hu et al. framework described in Section 2.
Table 2 compares the mean post-hoc regret and standard deviations for the alloy production problem
for the two different frameworks. The table shows that Two-Stage Predict+Optimize framework
always achieves smaller mean post-hoc regret than the Hu et al. framework. Compared with the
Hu et al. framework, our framework obtains 6.18%-35.63% smaller mean post-hoc regret in brass
production, and 6.59%-29.89% smaller mean post-hoc regret in titanium-alloy production.

We present a further comparison in Appendix F with a variant of the Hu et al. framework—the ℓ2
projection idea in [3], which performs even worse than the Hu et al. framework.

The second experiment compares various training approaches all evaluated under the Two-Stage
Predict+Optimize framework. That is, the models are trained differently, but at test time, we always
use Stage 2 optimization to give a final solution and evaluate post-hoc regret on it. Table 3 reports the
mean post-hoc regrets and standard deviations across 10 runs for each training method on the alloy
production problem. The table shows that our method, 2S, achieves the best performance, compared
with IntOpt-C achieving the second best performance, beating all the classical training approaches.
Compared with IntOpt-C, 2S obtains 1.20%-3.18% smaller mean post-hoc regrets in brass production,
and 1.18%-5.33% smaller mean post-hoc regret in titanium-alloy production. Compared with the
classical approaches, the improvements are much more significant. 2S obtains at least 2.44%-45.48%
smaller mean post-hoc regrets in brass production, and at least 1.39%-38.78% smaller mean post-hoc
regret in titanium-alloy production. The average True Optimal Values (TOV) are reported in the last
column of Table 3 for reference, although the reader should take care to not over-interpret the ratio

8

---

<!-- PAGE 9 -->

Table 4: Mean post-hoc regrets and standard deviations for 0-1 knapsack problem using the Two-Stage
Predict+Optimize framework.

PReg

100

150

200

250

Penalty
factor
0.21
0.25
0.3
0.21
0.25
0.3
0.21
0.25
0.3
0.21
0.25
0.3

2S

CombOptNet

Ridge

k-NN

CART

RF

NN

TOV

1.26±0.01
6.28±0.05
9.22±0.10
0.73±0.01
3.64±0.04
7.27±0.06
0.33±0.01
1.67±0.03
3.33±0.06
0.07±0.00
0.34±0.02
0.69±0.04

9.45±0.19
9.60±0.22
10.45±0.34
8.90±8.97
9.11±9.41
9.34±9.38
15.16±0.21
15.20±0.27
15.25±0.22
20.42±0.25
20.47±0.13
20.54±0.32

9.46±0.19
9.77±0.19
10.16±0.19
9.12±0.22
9.40±0.21
9.76±0.22
6.57±0.21
6.80±0.20
7.09±0.19
2.39±0.22
2.53±0.21
2.71±0.20

9.38±0.21
9.70±0.19
10.10±0.18
8.91±0.20
9.19±0.20
9.53±0.19
6.38±0.29
6.62±0.29
6.91±0.28
2.18±0.20
2.34±0.19
2.54±0.18

8.67±0.13
9.19±0.12
9.85±0.11
8.46±0.18
8.88±0.17
9.41±0.17
6.26±0.21
6.57±0.19
6.95±0.19
2.45±0.20
2.60±0.19
2.79±0.18

9.50±0.26
9.82±0.27
10.22±0.28
9.20±0.27
9.47±0.26
9.81±0.24
6.59±0.23
6.82±0.21
7.10±0.18
2.34±0.32
2.49±0.30
2.67±0.28

9.81±0.20
10.11±0.20
10.49±0.21
9.66±0.47
9.92±0.43
10.23±0.38
7.08±0.95
7.27±0.88
7.52±0.80
2.70±1.34
2.82±1.26
2.97±1.16

29.68±0.14

40.23±0.19

48.13±0.24

53.43±0.26

Table 5: Mean post-hoc regrets and standard deviations for the NSP using the Two-Stage Pre-
dict+Optimize framework.

Penalty factor
0.25±0.015
0.5±0.015
1.0±0.015
2.0±0.015
4.0±0.015
8.0±0.015

2S
3.94±1.91
6.92±2.26
13.12±3.15
25.04±9.29
33.29±9.53
46.72±14.80

Ridge
6.45±4.68
12.68±9.35
25.12±18.71
49.95±37.39
99.61±74.78
198.91±149.54

k-NN
15.20±5.76
30.29±11.53
60.43±23.07
120.62±46.08
241.01±92.14
481.79±184.27

CART
26.20±8.96
52.47±17.96
105.01±36.00
210.02±72.06
420.04±144.18
840.10±288.45

RF
19.47±7.19
38.93±14.42
77.86±28.99
155.64±58.06
311.19±116.23
622.32±232.56

NN
4.27±2.22
8.20±4.40
16.00±8.78
31.51±17.40
62.52±34.64
124.54±69.14

TOV

190.21±26.17

between the post-hoc regret and the true optimal value, since the post-hoc regret also includes the
penalty term which increases with the penalty factors.

0-1 knapsack In the second example, we showcase our framework on a packing integer program-
ming problem, a variant of the 0-1 knapsack problem, with unknown item prices pi and sizes si. See
Appendix C.2 for details of an application in running a “proxy buyer” business. Here, the unknown
parameters appear in both the objective and constraints. The proposed 2S method can handle this
MILP straightforwardly, but the IntOpt-C method cannot be applied. Thus, we only experiment with
the Two-Stage Predict+Optimize framework for evaluation, and compare the proposed 2S method
with classical approaches and CombOptNet. Again, all approaches are evaluated at test time using
the Stage 2 optimization to yield the final solution, on which the post-hoc regret is computed.

The MILP formulation of the two stages and the penalty function are described in Appendix C.2.
We use the dataset of Paulus et al. [23], in which each 0-1 knapsack instance consists of 10 items
and each item has 4096 features related to its price and size. For both NN and our method, we use a
5-layer fully-connected network with 512 neurons per hidden layer. We conduct experiments on 4
different knapsack capacities: 100, 150, 200, and 250. We use 700 instances for training and 300
instances for testing the model performance. Considering the real-life setting, we use 3 scales of the
penalty factor for the penalty function in Appendix C.2: σ = 0.05, 0.25, or 0.5.

Table 4 reports the mean post-hoc regrets and standard deviations across 10 runs for each approach
on this 0-1 knapsack problem. Due to the space limitation and the fact that larger penalty factors
are unrealistic in this problem setting, we present penalty factors ≥ 1 in Appendix G. The average
True Optimal Values (TOV) are reported in the last column, again for reference. As shown in the
table, our proposed 2S method has significantly better results. In addition, we observe that across
all approaches, the post-hoc regrets decrease as the knapsack capacity increases: this is due to the
fact that as the capacity increases, more and more items can be selected, and so minor inaccuracies
in predicted values/weights do not affect the selected set of items as much. On the other hand, the
advantage of our 2S method over other approaches actually becomes more significant as the capacity
increases, demonstrating the superior accuracy of our approach.

Nurse Scheduling Problem Our last experiment is on the nurse scheduling problem (NSP) with
unknown patients needs, with the goal of scheduling a nurse roster satisfying unknown patient load
demands while minimizing mismatched nurse-shift preferences as the objective. See Appendix C.3
for a description of the application scenario, the MILP formulations of the two stages, as well as the
associated penalty function. Given that NSP is not an LP, IntOpt-C again does not apply, and so we

9

---

<!-- PAGE 10 -->

only compare the proposed 2S training method with the classical approaches, using the Two-Stage
Predict+Optimize framework for evaluation. Each NSP instance consists of 15 nurses, 7 days, and 3
shifts per day. The nurse preferences are obtained from the NSPLib dataset [26], which is widely
used for NSP [16, 20]. The number of patients that each nurse can serve in one shift is randomly
generated from [10,20], representing the fact that each nurse has different capabilities. Given that we
are unable to find datasets specifically for the patient load demands and relevant prediction features,
we follow the experimental approach of Demirovic et al. [4, 5, 6] and use real data from a different
problem (the ICON scheduling competition) as the numerical values required for our experiment
instances. In this dataset, the unknown number of patients per shift is predicted by 8 features.

Since there are far fewer features than the previous experiments, for both NN and 2S we use a smaller
network structure: a 4-layer fully-connected network with 16 neurons per hidden layer. We use 210
instances for training and 90 instances for testing. Just like the first experiment, we use 6 scales of
penalty factors (see Appendix C.3 for the penalty function): γ with i.i.d. entries drawn uniformly
from [0.25 ± 0.015], [0.5 ± 0.015], [1.0 ± 0.015], [2.0 ± 0.015], [4.0 ± 0.015], and [8.0 ± 0.015].

Table 5 reports the mean post-hoc regrets and standard deviations across 10 runs for each approach
on the NSP. The table shows that the proposed 2S method again has the best performance among
all the training approaches. Our 2S method obtains at least 7.61%, 15.65%, 17.99%, 20.51%,
46.76%, and 62.49% smaller post-hoc regret than other classical methods when the penalty factor is
[0.25±0.015], [0.5±0.015], [1.0±0.015], [2.0±0.015], [4.0±0.015], and [8.0±0.015] respectively.

Runtime Analysis Appendix H gives the training times for each method. Most classical approaches
are faster than our 2S method, although as shown their post-hoc regrets are much worse. In alloy
production, the only setting where IntOpt-C applies, its running time is shorter but comparable with
2S. In 0-1 knapsack, the only problem with public CombOptNet code, the 2S method is much faster.

6 Literature Review

Section 1 already summarized prior works in Predict+Optimize, most of which focus on learning
unknowns only in the objective. Only the Hu et al. [12] framework considers unknowns in constraints.

Here we summarize other works related to learning unknowns in optimization problem constraints,
particularly those outside of Predict+Optimize. These works can be placed into two categories.

One category also considers learning unknowns in constraints, but with very different goals and mea-
sures of loss. For example, CombOptNet [23] and Nandwani et al. [21] focus on learning parameters
so as to make the predicted optimal solution (first-stage solution in our proposed framework) as close
to the true optimal solution x∗ as possible in the solution space/metric. By contrast, our proposed
framework explicitly formulates the two-stage framework and post-hoc regret in order to directly
capture rewards and costs in application scenarios. Experiments on 0-1 knapsack in Section 5 show
that these other methods yield worse predictive performance when evaluated on the post-hoc regret,
under the proposed two-stage framework.

Another category gives ways to differentiate through LPs or LPs with regularizations, as a technical
component in a gradient-based training algorithm. As mentioned in Section 4, these works can
indeed be used in place of our proposed approach in Section 4/Appendix B. However, we point out
that: (i) these other technical tools are essentially orthogonal to our primary contribution, which
is the two-stage framework (Section 3), and (ii) nonetheless, experiments on the 0-1 knapsack in
Appendix E demonstrate that our gradient calculation approach performs at least as well in post-hoc
regret performance as other works, while being faster.

7 Summary

We proposed Two-Stage Predict+Optimize: a new, conceptually simpler and more powerful framework
for the Predict+Optimize setting where unknown parameters can appear both in the objective and in
constraints. We showed how the simpler perspective offered by the framework allows us to give a
general training framework for all MILPs, contrasting prior work which apply only to covering and
packing LPs. Experimental results demonstrate that our training method offers significantly better
prediction performance over other classical and state-of-the-art approaches.

10

---

<!-- PAGE 11 -->

Acknowledgments

We thank the anonymous referees for their constructive comments. In addition, Xinyi Hu and
Jimmy H.M. Lee acknowledge the financial support of a General Research Fund (RGC Ref. No.
CUHK 14206321) by the University Grants Committee, Hong Kong. Jasper C.H. Lee was supported
in part by the generous funding of a Croucher Fellowship for Postdoctoral Research, NSF award
DMS-2023239, NSF Medium Award CCF-2107079 and NSF AiTF Award CCF-2006206.

References

[1] A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, and J. Z. Kolter. Differentiable convex

optimization layers. Advances in neural information processing systems, 32, 2019.

[2] B. Amos and J. Z. Kolter. Optnet: Differentiable optimization as a layer in neural networks. In

International Conference on Machine Learning, pages 136–145. PMLR, 2017.

[3] B. Chen, P. L. Donti, K. Baker, J. Z. Kolter, and M. Bergés. Enforcing policy feasibility
constraints through differentiable projection for energy optimization. In Proceedings of the
Twelfth ACM International Conference on Future Energy Systems, pages 199–210, 2021.

[4] E. Demirovi´c, P. J. Stuckey, J. Bailey, J. Chan, C. Leckie, K. Ramamohanarao, and T. Guns.
An investigation into Prediction+Optimisation for the knapsack problem. In International
Conference on Integration of Constraint Programming, Artificial Intelligence, and Operations
Research, pages 241–257. Springer, 2019.

[5] E. Demirovi´c, P. J. Stuckey, J. Bailey, J. Chan, C. Leckie, K. Ramamohanarao, and T. Guns.
Predict+Optimise with ranking objectives: Exhaustively learning linear functions. Proceedings
of the Twenty-Eighth International Joint Conference on Artificial Intelligence, pages 1078–1085,
2019.

[6] E. Demirovi´c, P. J. Stuckey, T. Guns, J. Bailey, C. Leckie, K. Ramamohanarao, and J. Chan.
In Proceedings of the Thirty-Fourth AAAI

Dynamic programming for Predict+Optimise.
Conference on Artificial Intelligence, pages 1444–1451, 2020.

[7] A. N. Elmachtoub and P. Grigas. Smart “Predict, then Optimize”. Management Science,

68(1):9–26, 2022.

[8] A. N. Elmachtoub, J. C. N. Liang, and R. McNellis. Decision trees for decision-making under
the predict-then-optimize framework. In Proceedings of the 37th International Conference on
Machine Learning, pages 2858–2867, 2020.

[9] J. Friedman, T. Hastie, and R. Tibshirani. The elements of statistical learning. Springer series

in statistics New York, 2001. Volume 1, Number 10.

[10] A. U. Guler, E. Demirovi´c, J. Chan, J. Bailey, C. Leckie, and P. J. Stuckey. A divide and conquer
algorithm for Predict+Optimize with non-convex problems. In Proceedings of the Thirty-Sixth
AAAI Conference on Artificial Intelligence, 2022.

[11] Gurobi Optimization, LLC. Gurobi Optimizer Reference Manual, 2023.

[12] X. Hu, J. C. H. Lee, and J. H. M. Lee. Predict+Optimize for packing and covering LPs with
In Proceedings of the AAAI Conference on Artificial

unknown parameters in constraints.
Intelligence, 2022.

[13] X. Hu, J. C. H. Lee, J. H. M. Lee, and A. Z. Zhong. Branch & Learn for recursively and iteratively
solvable problems in Predict+Optimize. In Advances in Neural Information Processing Systems,
2022.

[14] K. B. Kabir and I. Mahmud. Study of erosion-corrosion of stainless steel, brass and aluminum
by open circuit potential measurements. Journal of Chemical Engineering, pages 13–17, 2010.

[15] N. Kahraman, B. Gülenç, and F. Findik. Joining of titanium/stainless steel by explosive welding

and effect on interface. Journal of Materials Processing Technology, 169(2):127–133, 2005.

11

---

<!-- PAGE 12 -->

[16] B. Maenhout and M. Vanhoucke. Branching strategies in a Branch-and-Price approach for a
multiple objective nurse scheduling problem. Journal of scheduling, 13(1):77–93, 2010.

[17] J. Mandi, V. Bucarey, M. M. K. Tchomba, and T. Guns. Decision-focused learning: Through the
lens of learning to rank. In International Conference on Machine Learning, pages 14935–14947.
PMLR, 2022.

[18] J. Mandi and T. Guns. Interior point solving for LP-based Prediction+Optimisation. Advances

in Neural Information Processing Systems, 33:7272–7282, 2020.

[19] M. Mulamba, J. Mandi, M. Diligenti, M. Lombardi, V. Bucarey, and T. Guns. Contrastive losses
and solution caching for Predict-and-Optimize. arXiv preprint arXiv:2011.05354, 2020.

[20] R. Muniyan, R. Ramalingam, S. S. Alshamrani, D. Gangodkar, A. Dumka, R. Singh, A. Gehlot,
and M. Rashid. Artificial bee colony algorithm with Nelder–Mead method to solve nurse
scheduling problem. Mathematics, 10(15):2576, 2022.

[21] Y. Nandwani, R. Ranjan, P. Singla, et al. A solver-free framework for scalable learning in neural

ilp architectures. Advances in Neural Information Processing Systems, 35:7972–7986, 2022.

[22] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin,
N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani,
S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala. Pytorch: An imperative style,
high-performance deep learning library. In Advances in Neural Information Processing Systems
32, pages 8024–8035. 2019.

[23] A. Paulus, M. Rolínek, V. Musil, B. Amos, and G. Martius. Comboptnet: Fit the right NP-hard
problem by learning integer programming constraints. In International Conference on Machine
Learning, pages 8443–8453. PMLR, 2021.

[24] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel,
P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher,
M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. Journal of Machine
Learning Research, 12:2825–2830, 2011.

[25] D. E. Rumelhart, G. E. Hinton, and R. J. Williams. Learning representations by back-propagating

errors. nature, 323(6088):533–536, 1986.

[26] M. Vanhoucke and B. Maenhout. Nsplib–a nurse scheduling problem library: A tool to evaluate
(meta-) heuristic procedures. In Operational research for health policy: making better decisions,
proceedings of the 31st annual meeting of the working group on operations research applied to
health services, pages 151–165, 2007.

[27] B. Wilder, B. Dilkina, and M. Tambe. Melding the data-decisions pipeline: Decision-focused
learning for combinatorial optimization. In Proceedings of the Thirty-Third AAAI Conference
on Artificial Intelligence, pages 1658–1665, 2019.

12

---

<!-- PAGE 13 -->

A Detailed discussion on the Two-Stage Predict+Optimize framework

A.1 Problem modelling using the framework

As mentioned in Section 3, the proposed Two-Stage Prediction+Optimize framework is phrased
differently from some other two-stage problem formulations. The proposed framework phrases
Stage 1 solutions as soft commitments, and corrects Stage 1 solutions with penalty in Stage 2. On
the other hand, some two-stage frameworks phrase Stage 1 solutions as hard commitments, and
include explicit recourse variables in both stages of OP to model the correction in Stage 2. Some
optimization problems are more natural to express according to one perspective than the other, while
some problems might be straightforward to express in either. This section aims to show that our
framework, while explicitly stated and motivated according to the first perspective, is in fact general
enough to also easily model the second perspective of hard commitments and recourse actions. In
what follows, we first describe different types of variables and how our framework can capture them.
Then, we give two example problems that respectively use the soft/hard commitment perspectives,
and we detail how the problem can be modelled.

Soft commitment variables: These are variables which represent decisions that correspond to soft
commitments made in Stage 1 in an application, namely decisions that may be modified
once the true parameters are revealed, but at a cost or penalty. The discussion in Section 3 is
tailored for this kind of variables—simply define such a variable in Stage 1 and use a finite
penalty function to model the cost of changing this soft commitment in Stage 2.

Hard commitment variables: These are variables x∗

hard which represent hard commitments made
in Stage 1, meaning that after commitment, they absolutely cannot change in Stage 2. To
model these variables in our framework, simply write a penalty function that is infinite
whenever Stage 1 and Stage 2 solutions for these variables are different. Explicitly, add a
term ∞ · 1[x∗
hard,2]. This way, no Stage 2 solution will change these variables
from what they were committed to in Stage 1.

hard,1 ̸= x∗

Recourse/other variables: These are variables which represent explicit actions/decisions taken only
in Stage 2, once the true parameters are revealed. These variables are necessary, for example,
when Stage 1 actions are all hard commitment variables, to ensure that we have a mechanism
for corrective action if the hard Stage 1 decisions are in any way “incompatible" with the
revealed parameters. These corrective actions also typically come at a cost. Thus, to model
these variables, simply include them in both Stages 1 and 2, and incorporate their cost into
the objective of the optimization problem. There should also be 0 penalty for modifying
these variables between the stages.

To summarize, Stage 1 actions can be classified as either soft or hard commitments, depending
on whether they can be changed in Stage 2 (at a finite penalty). Stage 2 actions are classified as
“recourse" variables, which are simply variables that have no penalty from changing between Stage
1 to Stage 2. The above discussion shows how our framework captures all these possibilities. We
now give two example applications: the first one is more naturally expressed via the soft commitment
perspective, and the second one is more natural to phrase using hard commitments+recourse. We
give also their explicit formulations to demonstrate how the modelling is done in our framework.

We first show an example problem which is naturally modelled using soft commitment variables
and penalty functions. Consider the product-stocking problem in Example 1 again, where regular
orders have to be placed two weeks ahead of monthly deliveries. We aim to maximize the net profit
by selling stocked products, under the constraint that the available storage space is limited. Each
product i has a purchase price pu
i (the price of purchasing the product from the wholesale company)
and a selling price ps
i (the price of selling the product to customers), and needs si space to be stocked.
Let xi denote whether the product i is ordered. In Stage 1, i.e., two weeks before the delivery, the
available storage space Sp at the time of delivery is unknown, and we place the order x based on
estimated space. In Stage 2, i.e., the night before the delivery, the precise available space is revealed,
and we ask the wholesale company to change the order but need to pay a surcharge for last-minute
changes. Assume the surcharge for the last-minute change in the order of product i is ci. In this
example, xi is thus a soft commitment variable, and we model the surcharge ci using the penalty
function of the framework.

13

---

<!-- PAGE 14 -->

The proposed framework can naturally model this problem. The Stage 1 OP can be formulated as:

x∗
1 = arg max

x
(cid:88)

(ps

i − pu

i )xi

(cid:88)

i

s.t.

sixi ≤ ˆSp,

x ∈ {0, 1}

In Stage 2, the order x∗

1 can be changed with surcharges, which can be modelled as a penalty function:

i

P en(x∗

1 → x) =

ci|x∗

1 − xi|

(cid:88)

i

Then the Stage 2 OP can be formulated as:

x∗
2 = arg max

x
(cid:88)

(cid:88)

(ps

i − pu

i )xi −

i

ci|x∗

1 − xi|

(cid:88)

i

s.t.

sixi ≤ Sp,

x ∈ {0, 1}

i

Next, we give an example problem which is more naturally modelled using hard commitment variables
and recourse variables. Consider a production-planning problem: a company owns a set of facilities
and provides services to a set of customers. Each facility i can provide a fixed amount of services mi
and has a fixed operating cost fi in the standard working mode. The company aims to meet customer
demands d at the minimum operating costs. In Stage 1, the company decides which facilities to open
for production based on the estimated demands ˆd. This is a binary decision variable xi for each
facility i. In Stage 2, the orders from customers arrive and the demands d are revealed. If the services
provided by the operating facilities in the standard mode cannot meet demands, the company will
ask some facilities that are already operating (i.e. xi = 1) to work overtime, but naturally need to
pay high overtime fees. Let oi denote the unit overtime fee for producing service in facility i, and σi
denote the amount of service provided by overtime working in facility i.

This example is naturally modelled using hard commitment variables and recourse variables. Which
facilities to operate, x, is a vector of 0/1 hard commitment variables. The amount of service, σ,
provided by the overtime working mode of operating facilities can be modeled by recourse variables,
and the recourse costs are the overtime fees o. Using hard commitment variables and recourse
variables, the Stage 1 OP can be formulated as:

1, σ∗
x∗

1 = arg min

x,σ

(cid:88)

fixi +

(cid:88)

oiσi

i

i

s.t.

(cid:88)

(mi + σi)xi ≥ ˆd,

x ∈ {0, 1},

σ ≥ 0

i

In Stage 2, we include a term ∞ · 1[x∗
1 ̸= x] in the penalty function part of the Stage 2 objective to
make sure that x cannot be changed, while the penalty for changing σ is zero since it is a recourse
variable. The Stage 2 OP is formulated as:

2, σ∗
x∗

2 = arg min

x,σ

(cid:88)

i

fixi +

(cid:88)

i

oiσi + ∞ · 1[x∗

1 ̸= x]

s.t.

(cid:88)

(mi + σi)xi ≥ d,

x ∈ {0, 1},

σ ≥ 0

i

In summary, we discussed how to model in our framework soft and hard commitment actions in Stage
1, as well as recourse/other actions in Stage 2. We gave two concrete examples to demonstrate how
such modelling can be done.

A.2 What if correction/recourse is not possible in the application?

The motivating premise of this paper is that the application scenario at hand allows for some post-
hoc corrective action once the true parameters are revealed. One natural question is: what if such

14

---

<!-- PAGE 15 -->

corrective action (Stage 2 actions) is not actually possible in the application? For example, in our
running example of the product-stocking problem, we considered a wholesale company that allows for
order changes the night before. Other wholesalers may not allow such a correction/modification. Our
framework can essentially still model these scenarios: just set the penalty of modification to infinity
(or at least, very large numbers for practice). Concretely, use the penalty function ∞ · 1[x∗
1] (or
replace ∞ with a very large number). This penalty function encourages the learning algorithm to
learn conservative predictions that maximize the chances of yielding Stage 1 decisions that remain
feasible in Stage 2.

2 ̸= x∗

To show this, we ran another quick experiment, using the 0-1 knapsack problem setting in the paper
(with knapsack capacity = 100). This time, as we varied the magnitude of the penalty function,
we measure at test time the empirical fraction of Stage 1 solutions that remain feasible under the
true parameters. The results in Table 6 demonstrate our claim that as the penalty term increases,
the predictions get more and more likely to remain feasible, making it a reasonable way to train a
predictor even when Stage 2 correction mechanisms do not actually exist in the application.

Table 6: Mean and standard deviation of empirical fraction of Stage 1 solutions that remain feasible
in Stage 2, for the 0-1 knapsack problem when capacity is 100 using the Two-Stage Predict+Optimize
framework.

Penalty Factor
0.05
0.25
0.5
1
2
4

Feasibility%
0.00%±0.00%
0.00%±0.00%
1.73%±0.52%
50.93%±1.92%
51.63%±1.22%
99.07%±0.31%

A.3 Two-Stage Predict+Optimize vs Prior Hu et al. Framework

As mentioned earlier in Section 3, Two-Stage Predict+Optimize is technically mathematically equiva-
lent to the prior framework of Hu et al. [12], in the sense of expressiveness, ignoring differentiability
issues. On the one hand, we can regard the Stage 2 optimization as a form of correction function,
and hence Two-Stage Predict+Optimize can be considered as a special case of the Hu et al. [12]
framework. On the other hand, given a correction function as in the Hu et al. [12] framework,
we can simply modify the penalty function such that we keep the penalty value of the corrected
solution, and make the penalty value infinite for all other potential Stage 2 solutions. This forces
the Stage 2 optimization to always emulate the correction function. In this sense, our Two-Stage
Predict+Optimize framework can also emulate the Hu et al. [12] framework, meaning that the two
frameworks are technically equivalent.

Nevertheless, the Two-Stage Predict+Optimize framework is both conceptually simpler and easier
to apply. In the main paper, we showed how to perform end-to-end neural network training within
this new framework whenever both stages of optimization can be phrased as MILPs, and also give
empirical experimental results. Together, they demonstrate the much more general applicability of
the Two-Stage Predict+Optimize framework.

We end this appendix with the statement and short proof that, conditioned on the same penalty
function and prediction model, Two-Stage Predict+Optimize always outputs at least as good a final
solution as the prior framework using any correction function.
Proposition A.1. Consider an arbitrary minimization Para-OP P , penalty function P en, correction
1(ˆθ) both denote the
function x∗
2(ˆθ, θ) be the output final solution from the
estimated solution from the estimated parameters ˆθ, x∗
corr(ˆθ, θ) be the output corrected solution from the
Two-Stage Predict+Optimize framework, and x∗
prior framework of Hu et al. Then,
2(ˆθ, θ), θ) + P en(x∗

corr, estimated parameters ˆθ and true parameters θ. Let x∗(ˆθ) and x∗

corr(ˆθ, θ), θ) + P en(x∗(ˆθ) → x∗

2(ˆθ, θ)) ≤ obj(x∗

1(ˆθ) → x∗

corr(ˆθ, θ))

obj(x∗

Proof. Observe that both sides of the inequality are the objective of the Stage 2 optimization problem,
evaluated at x∗
2 is the optimal solution to the minimization problem,
the inequality follows directly.

corr respectively. Since x∗

2 and x∗

15

---

<!-- PAGE 16 -->

B Gradient Calculations for Problem (5)

.

Approximating ∂x∗
In the context of the MILP, the unknown parameter ˆθ may either be c, A, b, G,
1
∂ ˆθ
or h. Using the solution x and the barrier weight µ returned from solving Problem (5), we can
compute the relevant derivatives of ∂x∗
∂ˆc . The case of c has already been derived by Mandi and
Guns [18] (see Appendix A.1 and A.2 in their paper). Problem (5) can be rewritten as:

1

x∗ = arg min

c′⊤x′ − µ

x′

s.t. A′x′ = b′

d+q
(cid:88)

i=1

ln(x′
i)

(6)

where

0] ∈ Rd+q
c′ = [c
x′ = [x s] ∈ Rd+q
(cid:21)
(cid:20) A 0
G − I

A′ =

b′ =

(cid:21)

(cid:20) b
h

∈ Rp+q

∈ R(p+q)×(d+q)

Fact B.1. Consider the LP relaxation (6), defining x′ as a function of c′, A′ and b′. Then, according
to Mandi and Guns [18], under this definition of x∗,





−X ′−1T A′⊤ −c′
−b′
κ
τ

A′
−c′⊤

0
b′⊤









∂x′
∂c′
∂y′
∂c′
∂τ
∂c′





 =







τ I
0
x⊤

where X ′ = diag(x′), t = µX ′−1e, T = diag(t), y′ is the lagrangian multiplier of Problem (6), and
κ and τ are additional variables added by Mandi and Guns [18] to represent the duality gap. The
gradient ∂x∗

1

∂ˆc can be obtained by solving this system of equalities.
i=1 ln(xi) − µ (cid:80)q

Define the notation f (x, c, G, h) = c⊤x − µ (cid:80)d
(5) can be expressed as finding:

i=1 ln(G⊤

i x − hi). Then, Problem

x∗ = arg min

f (x, c, G, h) s.t. Ax = b

x

(7)

Using this notation, we write down the following four lemmas on computing ∂x∗
approximately.
Lemma B.2. Consider the LP relaxation (7), defining x∗ as a function of c, A, b, G and h. Then,
under this definition of x∗,

∂A , and ∂x∗

∂G , ∂x∗

∂h , ∂x∗

∂b

∂x∗
∂G

= (H −1A⊤(AH −1A⊤)−1AH −1 − H −1)fGx(x, c, G, h)

where H = fxx(x, c, G, h) denotes the matrix of second derivatives of f with respect to different
coordinates of x, and similarly for other subscripts, and explicitly:

and

fxkxj (x, c, G, h) =

fGℓrxj (x, c, G, h) =

(cid:26) µx−2

j + µ (cid:80)q
µ (cid:80)q

i=1 G2
i=1 GijGik/(G⊤

ij/(G⊤

i x − hi)2,

i x − hi)2,

j = k

j ̸= k

(8)

(cid:26)µGℓjxj/(G⊤
µGℓjxr/(G⊤

ℓ x − hℓ)2 − µ/(G⊤
ℓ x − hℓ)2

ℓ x − hℓ)

r = j
r ̸= j

Note that when there are no equality constraints, i.e., A = 0, we have

∂x∗
∂G

= −H −1fGx(x, c, G, h)

which is the same as the Lemma 3 in [12].

16

---

<!-- PAGE 17 -->

Proof. Using the Lagrangian multiplier y, the Lagrangian relaxation of Problem (7) can be written as
L(x, y; c, G, h) = f (x, c, G, h) + y⊤(b − Ax)
(9)
Since x∗ = arg minx f (x, c, G, h) s.t. Ax = b is an optimum, x∗ must obey the Karush-Kuhn-
Tucker (KKT) conditions, obtained by setting the partial derivative of Equation (9) with respect to
x and y to 0. Let fx(x, c, G, h) denotes the vector of first derivatives of f with respect to different
coordinates of x, fxx(x, c, G, h) denotes the matrix of second derivatives of f with respect to different
coordinates of x, we obtain:

fx(x, c, G, h) − A⊤y = 0
Ax − b = 0

(10)

The implicit differentiation of these KKT conditions with respect to G allows us to get the following
system of equalities:

(cid:20) fGx(x, c, G, h)
0

(cid:21)

+

(cid:20) fxx(x, c, G, h) −A⊤

A

0

(cid:21) (cid:20) ∂x
∂G
∂y
∂G

(cid:21)

= 0

(11)

By solving this system of equalities, we can obtain

∂x∗
∂G

= (H −1A⊤(AH −1A⊤)−1AH −1 − H −1)fGx(x, c, G, h)

Since f (x, c, G, h) = c⊤x − µ (cid:80)d

fxj (x, c, G, h) = cj − µx−1
(cid:26) µx−2

fxkxj (x, c, G, h) =

i x − hi), we have

i=1 ln(xi) − µ (cid:80)q
j − µ (cid:80)q
j + µ (cid:80)q
µ (cid:80)q

i=1 ln(G⊤
i=1 Gij/(G⊤
ij/(G⊤
i=1 G2
i=1 GijGik/(G⊤

i x − hi)
i x − hi)2,

i x − hi)2,

j = k

j ̸= k

(12)

and

fGℓrxj (x, c, G, h) =

(cid:26)µGℓjxj/(G⊤
µGℓjxr/(G⊤

ℓ x − hℓ)2 − µ/(G⊤
ℓ x − hℓ)2

ℓ x − hℓ)

r = j
r ̸= j

Lemma B.3. Consider the LP relaxation (7), defining x∗ as a function of c, A, b, G and h. Then,
under this definition of x∗,

∂x∗
∂h

= (H −1A⊤(AH −1A⊤)−1AH −1 − H −1)fhx(x, c, G, h)

where H = fxx is defined as in Lemma B.2 and

ℓ x − hℓ)2
Note that when there are no equality constraints, i.e., A = 0, we have

fhℓxj (x, c, G, h) = −µGℓj/(G⊤

which is the same as the Lemma 2 in [12].

∂x∗
∂h

= −H −1fhx(x, c, G, h)

Proof. As stated in the proof of Lemma B.2, using the Lagrangian relaxation and the Karush-Kuhn-
Tucker (KKT) conditions, we obtain:

fx(x, c, G, h) − A⊤y = 0
Ax − b = 0

(13)

The implicit differentiation of these KKT conditions with respect to h allows us to get the following
system of equalities:

(cid:20) fhx(x, c, G, h)
0

(cid:21)

+

(cid:20) fxx(x, c, G, h) −A⊤

A

0

(cid:21) (cid:20) ∂x
∂h
∂y
∂h

(cid:21)

= 0

(14)

By solving this system of equalities, we can obtain

∂x∗
∂h

= (H −1A⊤(AH −1A⊤)−1AH −1 − H −1)fhx(x, c, G, h)

17

---

<!-- PAGE 18 -->

where H = fxx is defined as in Lemma B.2. Since f (x, c, G, h) = c⊤x − µ (cid:80)d
µ (cid:80)q

i=1 ln(Gix − hi), we have

i=1 ln(xi) −

fhℓxj (x) = −µGℓj/(G⊤

ℓ x − hℓ)2

Lemma B.4. Consider the LP relaxation (7), defining x∗ as a function of c, A, b, G and h. Then,
under this definition of x∗,

∂x∗
∂Aij

= H −1(−A⊤(AH −1A⊤)−1(I2x + AH −1I1y) + I1y)

where I1 = − ∂A⊤
∂Aij

, I2 = ∂A
∂Aij

, and H = fxx is defined as in Lemma B.2.

Proof. As stated in the proof of Lemma B.2, using the Lagrangian relaxation and the Karush-Kuhn-
Tucker (KKT) conditions, we obtain:

fx(x, c, G, h) − A⊤y = 0
Ax − b = 0

(15)

Since A ∈ Rp×d, fix i ∈ {1, . . . , p}, j ∈ {1, . . . , d}, the implicit differentiation of these KKT
conditions with respect to Aij allows us to get the following system of equalities:

(cid:34)

− ∂A⊤
y
∂Aij
∂A
x
∂Aij

(cid:35)

+

(cid:20) fxx(x, c, G, h) −A⊤

A

0

(cid:21) (cid:34) ∂x
∂Aij
∂y
∂Aij

(cid:35)

= 0

(16)

Let I1 = − ∂A⊤
∂Aij

, I2 = ∂A
∂Aij

. By solving this system of equalities, we can obtain

∂x∗
∂Aij

= H −1(−A⊤(AH −1A⊤)−1(I2x + AH −1I1y) + I1y)

where H = fxx is defined as in Lemma B.2.

Lemma B.5. Consider the LP relaxation (7), defining x∗ as a function of c, A, b, G and h. Then,
under this definition of x∗,

∂x∗
∂b

= H −1A⊤(AH −1A⊤)−1I

where H = fxx is defined as in Lemma B.2.

Proof. As stated in the proof of Lemma B.2, using the Lagrangian relaxation and the Karush-Kuhn-
Tucker (KKT) conditions, we obtain:

fx(x, c, G, h) − A⊤y = 0
Ax − b = 0

(17)

The implicit differentiation of these KKT conditions with respect to b allows us to get the following
system of equalities:

(cid:20) 0
−I

(cid:21)

+

(cid:20) fxx(x, c, G, h) −A⊤

A

0

(cid:21) (cid:20) ∂x
∂b
∂y
∂b

(cid:21)

= 0

(18)

By solving this system of equalities, we can obtain

∂x∗
∂b

= H −1A⊤(AH −1A⊤)−1I

where H = fxx is defined as in Lemma B.2.

18

---

<!-- PAGE 19 -->

C Details for Case Studies

Since the penalty function partly or solely affects the terms ∂P Reg(ˆθ,θ)
, and ∂x∗
2
∂x∗
1
we give three case studies for our framework to show how to design the penalty function and compute
gradients using the corresponding penalty function.

, ∂P Reg(ˆθ,θ)
∂x∗
1

∂x∗
2

1

2

,

(cid:12)
(cid:12)
(cid:12)x∗

(cid:12)
(cid:12)
(cid:12)x∗

C.1 Alloy Production Problem

We first demonstrate, using the example of the alloy production problem, how our framework can
tackle problems solvable by the prior work of Hu et al. [12]. An alloy production factory needs
to produce a certain amount of a particular alloy, requiring a mixture of M kinds of metals. To
that end, it must acquire at least reqm tons of each of the m ∈ [M ] metals. The raw materials are
to be obtained from K suppliers, each supplying a different type of ore. The factory plans to buy
ores from sites and then extract the metals themselves. The ore supplied by site k ∈ [K] contains a
conkm ∈ [0, 1] fraction of material m at a price of costk per ton. The goal of the factory is to meet
its requirements for each metal at the minimum cost. However, the precise metal concentrations
(averaged in a batch) are unknown before the factory actually completes metal extraction. The factory
will estimate metal concentrations based on historical buying records, considering features such as
the ore type, ore origin, site-reported preliminary samples and so on. Then the factory will decide
how much ore to order from each site. This is the Stage 1 solution. The Stage 1 OP is the alloy
production problem using the estimated metal concentrations ˆcon, and can be formulated as follows:

x∗
1 = arg min

x

cost⊤x

s.t. ˆcon⊤x ≥ req, x ≥ 0

After the factory obtains the ores and completes metal extraction, i.e., in Stage 2, the precise metal
concentrations/amounts are known. Since the purchased ores are already processed, the factory
cannot return ores even if it has bought too much. However, if the obtained metals do not satisfy
the requirements, the factory can post-hoc decide to last-minute order more ores at a higher price,
for example, (1 + σk)costk per ton from the site k, where σk ≥ 0 is a non-negative tunable scalar
parameter. In this scenario, the penalty function is:

P en(x∗

1 → x) = (σ ◦ cost)⊤(x − x∗
1)

(19)

where ◦ is the Hadamard/entrywise product.

With respect to the above penalty function, we are now ready to define the Stage 2 OP:

x∗
2 = arg min

x

cost⊤x + (σ ◦ cost)⊤(x − x∗
1)

s.t. con⊤x ≥ req, x ≥ x∗
1

(20)

Note that since the precise metal concentrations con are revealed, the true concentrations are used as
the problem parameters instead of the estimated concentrations. The final amount of ores bought
from each site, including the ores bought in both Stage 1 and Stage 2, is the Stage 2 solution.

The above formulation is based on the “soft commitment" modelling approach discussed in Ap-
pendix A.1.

The post-hoc regret for the alloy production problem can be explicitly written as:

2 − x∗

P Reg(ˆθ, θ) = cost⊤x∗

1) − cost⊤x∗(con)

2 + (σ ◦ cost)⊤(x∗
where x∗(con) is an optimal solution of the alloy production problem under the true concentrations
con. We now show how to compute the relevant gradients as discussed in Section 4 and Appendix B.
Using Equation (21), it is straightforward to compute that the i-th item in vector ∂P Reg(ˆθ,θ)
(cid:12)
(cid:12)
(cid:12)x∗

the i-th item in vector ∂P Reg(ˆθ,θ)
−σicosti.
Now we show how to compute the approximation of the remaining term, ∂x∗
2
∂x∗
1

∂P Reg(ˆθ,θ)
∂x∗
1

∂P Reg(ˆθ,θ)
∂x∗
2

= (1 + σi) costi,

(cid:12)
(cid:12)
(cid:12)x∗
(cid:19)

(cid:12)
(cid:12)
(cid:12)x∗

(cid:12)
(cid:12)
(cid:12)x∗

(21)

and

∂x∗
2

∂x∗
1

=

(cid:18)

(cid:19)

(cid:18)

:

.

i

i

2

1

2

1

19

---

<!-- PAGE 20 -->

. Then the Stage 1 optimal solution x∗

Approximation ∂x∗
. We use the same interior-point LP solver to help compute the relevant
2
∂x∗
1
derivatives. First, the estimated parameters are fed into the LP solver to solve the Stage 1 OP to
obtain the Stage 1 optimal solution x∗
1 and the corresponding µ, which are used to compute the term
∂x∗
1 and the true parameters are fed into the LP solver to solve
1
∂ ˆθ
the Stage 2 OP to obtain the Stage 2 optimal solution x∗
2 and the corresponding µ, which are used to
compute the term ∂x∗
. Consider the Stage 2 OP in program (20). It is clear that the Stage 2 OP is a
2
∂x∗
1
MILP, with x∗
1 in h of the constraints. Applying Lemma B.3, we can compute
an approximate gradient of the ∂x∗
term.
2
∂x∗
1

2 in the objective and x∗

C.2 Variant of 0-1 Knapsack

The second example, which we call the proxy buyer problem, is a variant of the 0-1 knapsack problem.
The unknown parameters appear in both the objective and constraints. This problem, as we shall see,
can be handled by our framework, but not by the prior approach by Hu et al. [12], since the problem
is inherently discrete and cannot be formulated as LPs.

A proxy buyer is a person who purchases goods for others possibly for a profit. Consider a proxy
buyer who is from City A, with a very high cost of living, who regularly travels to City B with a much
lower cost of living. Given her regular travels, her friends in City A have asked her to help purchase
everyday-life products, which are significantly cheaper in City B, yet the time and transportation
cost from City A to City B makes it prohibitive for most people to just go to City B themselves.
The traveller commutes between City A and City B once every three months, and has a known and
limited capacity cap of goods she could carry and bring back. Before each trip, her friends would
make requests for things to buy. For simplicity, one request contains one item. If the buyer brings
back the item as requested, her friends will pay her 20% of the price-tag pi of each item i as a
courtesy-thankyou. We denote this “profit” by fi, i.e., fi = 20%pi.

The buyer is popular, and many friends ask her for favours. One day before the buyer leaves for
City B, the buyer needs to decide which of her friends’ requests to accept, given the limited capacity,
and inform them accordingly. The buyer wants to maximize the total amount of courtesy-thankyou
money she gets, subject to the hard constraint of the limited suitcase capacity cap. However, the
precise price pi of each item i is unknown, due to the uncertainty of the price itself, the volatility of
the exchange rate, and the uncertainty of the discount activities of the items. Thus, the “profit” fi of
buying item i is unknown. In addition, the exact size si of each item i is also estimated. The buyer
will estimate the profit, i.e., the prices, and the sizes based on past experiences, considering features
such as time-of-year, holiday-or-not, brand and so on. The buyer will decide which requests to accept
based on the estimation. This is the Stage 1 solution. The Stage 1 OP is the proxy buyer problem
using the estimated sizes ˆs and estimated profits ˆf :

x∗
1 = arg max

x

ˆf ⊤x,

s.t. ˆs⊤x ≤ cap, x ∈ {0, 1}

After the buyer arrives at City B, the buyer knows the precise price and size of each item. If she
cannot carry all the accepted requests, for example, if the packaging for certain items have changed
since she last bought them, the buyer will necessarily need to drop some of these requests. The buyer
usually feels bad about reneging on a promise to her friends, and treats her friends to a meal as an
apology if the request cannot be fulfilled after she promised. For simplicity, we assume that the price
of the apology-meal is linear in the profit of the dropped request, since more expensive items are
considered “more important” requests. Here, the linearity factor is independent of the request. That
is, if she drops item i, she has to spend σfi amount of money, where σ ≥ 0 is a non-negative tunable
scalar parameter. In this scenario, the penalty function is:

P en(x∗

1 → x) = σf ⊤(x∗

1 − x)

(22)

We are now ready to define the Stage 2 OP with respect to the above penalty function:

x∗
2 = arg max

x

f ⊤x − σf ⊤(x∗

1 − x),

s.t. s⊤x ≤ cap, x ≤ x∗

1, x ∈ {0, 1}

(23)

The requests that were finally filled, namely the items that were actually bought by the buyer and
brought home to City A, forms the Stage 2 solution.

20

---

<!-- PAGE 21 -->

Then the simplified form of the post-hoc regret for the proxy buyer problem can be written as:

P Reg(ˆθ, θ) = f ⊤x∗(f, s) − f ⊤x∗

2 + σf ⊤(x∗

1 − x∗
2)

(24)

where x∗(f, s) is an optimal solution of the proxy buyer problem under the true proxy fees f and
true sizes s.
Using Equation (24), it is straightforward to compute that the i-th item in vector ∂P Reg(ˆθ,θ)
(cid:19)

(cid:12)
(cid:12)
(cid:12)x∗

and

(cid:18)

(cid:19)

(cid:18)

1

the i-th item in vector ∂P Reg(ˆθ,θ)

∂x∗
1

(cid:12)
(cid:12)
(cid:12)x∗

2

:

∂P Reg(ˆθ,θ)
∂x∗
2

(cid:12)
(cid:12)
(cid:12)x∗

1

= (−1 − σ) fi,

i

∂P Reg(ˆθ,θ)
∂x∗
1

∂x∗
2
(cid:12)
(cid:12)
(cid:12)x∗

2

= σfi.

i

1, the Stage 2 optimal solution x∗

Approximation ∂x∗
2
∂x∗
1
solution x∗
compute the term ∂x∗
2
∂x∗
1
MILP, with x∗
an approximate gradient of the ∂x∗
2
∂x∗
1

. Similar to the computation in Section C.1, we obtain the Stage 1 optimal
2, and the corresponding µ from the interior-point LP
. Consider the Stage 2 OP in program (23), it is clear that the Stage 2 OP is a
1 in h of the constraints. Applying Lemma B.3, we can compute
term.

2 in the objective and x∗

C.3 Nurse Scheduling Problem

Our last example is the nurse scheduling problem (NSP), which can be handled by our framework
but not by the prior work of Hu et al. [12] since it is neither a packing LP nor a covering LP.

Consider a large optometry center that needs to assign nurses to shifts per day to meet patients’
needs. Every Monday morning, the center collects the nurses’ preferences for each shift of the
following week. Since nurses may have their own activities and errands during unscheduled shifts,
they want to be informed of their schedules as early as possible. After the preferences are collected,
on Monday night, the center sets a preliminary shift schedule for the upcoming week based on the
estimated number of patients for each shift. Suppose there are n nurses, k days, and s shifts per day,
then the number of the total shifts is t = k × s. We formulate the decision variables as a Boolean
vector x ∈ {0, 1}d, where d = n × k × s. Let P ∈ {1, 2, 3, 4}d represent the value of each nurse’s
preferences for a particular shift (the higher the number the better), and H ∈ Nt represents the
number of patients in each shift, which are unknown and need to be predicted. Each nurse i can
serve mi patients in one shift. The objective is to maximize the nurses’ preferences under a set of
constraints: (1) the schedule must satisfy the patient demand, under each shift (2) each nurse must be
scheduled for exactly one shift each day (3) no nurse may be scheduled to work a night shift followed
immediately by a morning shift. The Stage 1 OP is the NSP using the estimated number of patients
ˆH:

x∗
1 = arg max

P ⊤x

x

n−1
(cid:88)

s.t.

mixit+j ≥ ˆHj ∀j ∈ {0, ..., t − 1}

i=0

s−1
(cid:88)

q=0

xit+sj+q = 1

∀i = {0, . . . , n − 1},
j = {0, . . . , k − 1}

xit+sj+s−1 + xit+sj+s ≤ 1

∀i = {0, . . . , n − 1},
j = {0, . . . , k − 2}

x ∈ {0, 1}

To provide better service to patients, the optometry center has implemented an appointment system
that requires patients to schedule an appointment in advance to receive medical care. Reservations for
the upcoming week, from Monday to Sunday, close every Sunday evening. At this point, the center
knows the precise number of patients for each shift of the next week. The center might adjust the shift
schedule to satisfy the actual patient demand or to improve the overall nurse preferences. However,
due to the late notice for schedule changes, the nurse’s preference may become lower. For example,
if a nurse is rescheduled to a shift for which her original preference is 5, now her preference for this
shift may become 4 due to the late notice. Besides, a nurse may be more unhappy to be changed to

21

---

<!-- PAGE 22 -->

a low-preference shift. In this scenario, since the nurses’ preferences are in {1, 2, 3, 4}, the penalty
function can be formulated as:

P en(x∗

1 → x) =

d−1
(cid:88)

i=0

P en(x∗

1 → x)i

(25)

where the i-th item in the penalty function is:

P en(x∗

1 → x)i =

0

(cid:26)γi(5 − Pi)2(xi − x∗

1i) xi ≥ x∗
1i
xi < x∗
1i

We are now ready to define the Stage 2 OP with respect to the above penalty function:

x∗
2 = arg max

x

P ⊤x −

d−1
(cid:88)

i=0

P en(x∗

1 → x)i

n−1
(cid:88)

s.t.

mixit+j ≥ Hj ∀j ∈ {0, ..., t − 1}

i=0

s−1
(cid:88)

q=0

xit+sj+q = 1

∀i = {0, . . . , n − 1},
j = {0, . . . , k − 1}

xit+sj+s−1 + xit+sj+s ≤ 1

∀i = {0, . . . , n − 1},
j = {0, . . . , k − 2}

x ∈ {0, 1}

Then the simplified form of the post-hoc regret for the NSP can be written as:

P Reg(ˆθ, θ) = P ⊤x∗(H) − P ⊤x∗

2 +

d−1
(cid:88)

i=0

P en(x∗

1 → x∗

2)i

Using Equation (26), it is straightforward to compute that the i-th item in vector ∂P Reg(ˆθ,θ)
the i-th item in vector ∂P Reg(ˆθ,θ)

∂x∗
2

:

∂x∗
1

(cid:12)
(cid:12)
(cid:12)x∗

2

(26)

(cid:12)
(cid:12)
(cid:12)x∗

1

and





∂P Reg(ˆθ, θ)
∂x∗
2





(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)x∗

1

i

=

(cid:26)−Pi + 2γi(5 − Pi) x∗
2i ≥ x∗
1i
2i < x∗
x∗
1i

−Pi





∂P Reg(ˆθ, θ)
∂x∗
1

(cid:12)
(cid:12)
(cid:12)
(cid:12)
(cid:12)x∗

2





i

=

(cid:26)−2γi(5 − Pi) x∗
2i ≥ x∗
1i
2i < x∗
x∗
1i

0

Approximation ∂x∗
2
∂x∗
1
solution x∗
compute the term ∂x∗
2
∂x∗
1

1, the Stage 2 optimal solution x∗

. Similar to the computation in Section C.1, we obtain the Stage 1 optimal
2, and the corresponding µ from the interior-point LP
. Using the penalty function in Equation (25), the Stage 2 OP can be formulated

22

---

<!-- PAGE 23 -->

as a MILP by adding new variables σ and one more constraint:

x∗
2 = arg max

x

P ⊤x −

d−1
(cid:88)

i=0

γi(5 − Pi)2σi

n−1
(cid:88)

s.t.

mixit+j ≥ Hj ∀j ∈ {0, ..., t − 1}

i=0

s−1
(cid:88)

q=0

xit+sj+q = 1

∀i = {0, . . . , n − 1},
j = {0, . . . , k − 1}

xit+sj+s−1 + xit+sj+s ≤ 1

∀i = {0, . . . , n − 1},
j = {0, . . . , k − 2}

1i ∀i = {0, . . . , d − 1}

σi ≥ xi − x∗
x ∈ {0, 1}
σ ∈ {0, 1}

Suppose the Stage 2 OP of the NSP can be written as:

x∗
2 = arg min

x

−P ⊤x + (γ ◦ (5 − P )2)⊤σ

s.t. G1x ≥ H

Ax = b
G2x ≥ −1
σ − x ≥ −x∗
1
x, σ ∈ {0, 1}

Then the standard form of the Stage 2 OP is:

x′
2 = arg min

x′

c⊤x′

s.t. A′x′ = b
Gx ≥ h
x′ ∈ {0, 1}

where

c = (cid:2)−P γ ◦ (5 − P )2(cid:3) ∈ R2d,
(cid:35)

x′ = [x σ] ∈ R2d
(cid:35)

∈ R(t+nk−n+d)×2d,

h =

∈ Rt+nk−n+d

G =

(cid:34) G1
G2
−I

0
0
I

A′ = [ A 0 ] ∈ Rnk×2d

(cid:34) H
−1
−x∗
1

and b ∈ Rnk is an all-ones vector.
It is clear that x∗
2 is in the objective and x∗
compute an approximate gradient of the ∂x∗
2
∂x∗
1

1 is in h of the constraints. Applying Lemma B.3, we can

term.

23

---

<!-- PAGE 24 -->

D Hyperparameters for the Experiments

The methods of k-NN, RF, NN, and IntOpt-C as well as 2S have hyperparameters, which we tune
via cross-validation: for k-NN, we try k ∈ {1, 3, 5}; for RF, we try different numbers of trees in the
forest {10, 50, 100}; for NN, IntOpt-C, and 2S, we treat the learning rate, epochs and weight decay
as hyperparameters.

Tables 7, 8, and 9 show the final hyperparameter choices for the three problems: 1) an alloy production
problem, 2) the classic 0-1 knapsack problem, and 3) a nurse roster scheduling problem.

Table 7: Hyperparameters of the experiments on the alloy production problem.

Model
Proposed
k-NN
RF
NN

Hyperparameters
optimizer: optim.Adam; learning rate: 5 × 10−7; µ = 10−3; epochs=20
k=5
n_estimator=100
optimizer: optim.Adam; learning rate: 10−3; epochs=20

Table 8: Hyperparameters of the experiments on the 0-1 knapsack problem.

Model
Proposed
k-NN
RF
NN

Hyperparameters
optimizer: optim.Adam; learning rate: 10−7; µ = 10−3; epochs=12
k=5
n_estimator=100
optimizer: optim.Adam; learning rate: 10−3; epochs=12

Table 9: Hyperparameters of the experiments on the nurse scheduling problem.

Model
Proposed
k-NN
RF
NN

Hyperparameters
optimizer: optim.Adam; learning rate: 10−1; µ = 10−3; epochs=8
k=5
n_estimator=100
optimizer: optim.Adam; learning rate: 10−2; epochs=8

Ridge, k-NN, CART and RF are implemented using scikit-learn [24]. The neural network is
implemented using PyTorch [22]. To compute the two stages of optimization at test time for our
method, and to compute the optimal solution of an (MI)LP under the true parameters, we use the
MILP solver from Gurobi [11].

E Comparisons of the 2S Method and the Prior Differentiation Methods

In this section, we compare the proposed method with prior works [1, 2, 27] that provide ways of
differentiating through LPs or LPs with regularization. We conduct comparisons with CvxpyLayer
[1] but not OptNet [2] or QPTL [27]. The reason is that the calculation method proposed in QPTL is
LP+quadratic regularization using OptNet, and CvxpyLayer is just a conic extension to OptNet. We
compared CvxpyLayer [1] with a) no regularization, b) quadratic regularization and c) log-barrier
(like our Section 4/Appendix B). The key indicator of its predictive performance is the type of
regularization used, with the log-barrier version performing the best, but still slightly worse than our
method. We applied CvxpyLayer [1] to the 0-1 knapsack benchmark to compare with our 2S method.

Table 10 reports the mean post-hoc regrets and standard deviations across 10 runs and Table 11
reports the average training times. More precisely, we use it with various regularizations (a. LP with
no regularization, b. with quadratic regularization, c. with log-barrier as in our paper) to replace the
Section 4/Appendix B gradient calculations. We find that CvxpyLayer [1] never gives better solution
quality while 2S is 30%–50% faster.

24

---

<!-- PAGE 25 -->

Table 10: Mean post-hoc regrets and standard deviations of the 2S method and CvxpyLayer with
different regularization on the 0-1 knapsack problem.

PReg

cap=100

cap=150

Penalty
factor
0.05
0.25
0.5
0.05
0.25
0.5

2S

CvxpyLayer+log CvxpyLayer+quad_reg CvxpyLayer+no_reg

1.26±0.01
6.28±0.05
9.22±0.10
0.73±0.01
3.64±0.04
7.27±0.06

1.26±0.01
6.28±0.05
9.47±0.31
0.74±0.01
3.64±0.04
7.28±0.08

1.27±0.01
6.34±0.03
9.96±0.54
0.75±0.03
3.70±0.03
7.39±0.06

7.70±0.39
8.87±0.92
10.13±0.46
6.74±0.58
7.18±0.77
8.43±0.58

Table 11: Average runtime (in seconds) of the 2S method and CvxpyLayer with different regularization
on the 0-1 knapsack problem.
2S
204.76
245.61

CvxpyLayer+log CvxpyLayer+quad_reg CvxpyLayer+no_reg

Runtime
cap=100
cap=150

438.24
467.65

571.38
662.30

344.50
366.83

F Frameworks Comparisons on the Alloy Production Problem

In this section, we further compared the proposed framework with the framework using the differ-
entiable projection idea in [3] on the alloy production benchmark. The idea in [3] is to use the l2
projection, and we implemented it using CvxpyLayer. The experiment set-up follows that of Table 2:
both training and testing use l2 projection in the second stage, as opposed to solving the second stage
optimization problem defined in Section 3. Table 12 shows both the post-hoc regret and training time
for l2 projection. We find that not only is l2 projection slow, but it has even worse post-hoc regret
than the Hu et al. correction [12]. We suspect that this is due to the Hu et al. correction function
[12] preserving the direction of the solution vector whereas l2 projection can change the direction,
and that this makes a difference for Alloy Production. In any case, this experiment confirms again
that our Two-Stage framework has better post-hoc regret than a framework based on differentiable
projections, reinforcing the main message of our paper.

Table 12: Comparison of three frameworks on the alloy production problem.

Penalty factor
Two-Stage Predict +
Optimize Framework
Hu et al. Framework
l2_projection

0.25±0.015

0.5±0.015

1±0.015

2±0.015

4±0.015

8±0.015

43.87±2.73

65.71±4.81

88.75±5.91

123.90±6.84

161.86±8.49

194.06±13.09

68.16±6.26
103.28±4.87

82.91±5.45
118.90±6.99

107.64±6.85
150.15±11.45

150.47±12.99
212.62±20.58

178.69±10.09
337.59±23.24

206.84±12.51
562.41±34.29

PReg

Average
runtime

268.22

228.00
442.97

G Experiments on the 0-1 Knapsack Problem with Large Penalty Factors

Table 13 reports the mean post-hoc regrets and standard deviations across 10 runs for each approach
on the 0-1 knapsack problem with large penalty factors (penalty factors ≥ 1). With more data, we
can make further analysis of the performance of the proposed 2S method. Observing Tables 4 and 13,
we can see that the trend, in terms of the difference between 2S and other methods, first decreases,
then increases, as the penalty factor increases. The trend in Tables 4 and 13 is identical to the trend in
Table 3. We can explain this phenomenon as follows.

First, when the penalty factor is small, the rational behavior for the buyer is to just take every order,
and only decide which orders to drop when the true parameters are revealed (at close to no cost). 2S
identifies and exploits this behavior for small penalties, while classic regression methods are agnostic
to this possible tactic. Thus, the advantage of 2S compared to classic regression methods is large in
the small penalty case.

Second, when the penalty factor is large, 2S will analogously learn to be conservative, such that the
first stage solution likely remains feasible under the true parameters, in order to avoid the necessary
(and high) penalty due to having to change to a feasible solution. Again, classic regression methods
will be agnostic to this possible tactic, leading to a large advantage of 2S over the classic methods.

25

---

<!-- PAGE 26 -->

Table 5 only has the increasing trend from the large penalty, since it is neither a covering nor a
packing program, and so there is no analogous tactic/exploitation for the small penalty.

Table 13: Mean post-hoc regrets and standard deviations for 0-1 knapsack problem with large penalty
factors using the Two-Stage Predict+Optimize framework.

PReg

cap=100

cap=150

cap=200

cap=250

Penalty
factor
1
2
4
1
2
4
1
2
4
1
2
4

2S

CombOptNet

Ridge

k-NN

CART

RF

NN

TOV

10.90±0.15
12.31±0.16
14.54±0.15
10.23±0.12
11.18±0.15
13.20±0.16
6.77±0.36
8.19±0.12
9.71±0.35
1.37±0.08
3.34±0.15
4.46±0.09

10.93±0.17
12.45±0.25
15.66±0.47
10.22±0.18
11.74±0.34
14.33±0.46
15.30±0.28
15.39±0.16
15.46±0.22
20.69±0.20
20.78±0.20
20.93±0.20

10.93±0.19
12.48±0.20
15.57±0.25
10.46±0.23
11.88±0.30
14.71±0.49
7.67±0.18
8.84±0.22
11.17±0.40
3.08±0.19
3.80±0.20
5.25±0.35

11.11±0.17
12.49±0.21
15.68±0.39
10.40±0.18
11.63±0.20
14.43±0.33
7.51±0.27
8.69±0.26
11.06±0.32
2.94±0.16
3.73±0.15
5.32±0.27

11.16±0.14
13.77±0.26
19.01±0.56
10.46±0.19
12.56±0.31
16.75±0.63
7.71±0.20
9.24±0.30
12.29±0.59
3.17±0.17
3.94±0.20
5.47±0.35

11.01±0.31
12.60±0.39
15.77±0.62
10.49±0.21
11.83±0.19
14.53±0.29
7.67±0.16
8.80±0.20
11.05±0.46
3.05±0.25
3.79±0.26
5.29±0.48

11.26±0.23
12.78±0.30
15.84±0.50
10.86±0.30
12.12±0.17
14.65±0.41
8.00±0.65
8.97±0.37
10.91±0.53
3.28±0.96
3.89±0.58
5.11±0.39

29.68±0.14

40.23±0.19

48.13±0.24

53.43±0.26

H Runtimes for the Experiments

In this paper, all models are trained with Intel(R) Xeon(R) CPU E5-2630 v2 @ 2.60GHz processors.
Table 14 shows the average runtime across 10 simulations for different optimization problems. Since
the testing time of different approaches is quite similar, here, the runtime refers to only the training
time of the prediction model and does not include the testing time. At training time, only the proposed
2S method and IntOpt-C solve the LP. Training for the usual NN does not involve the LP at all, and
so training is much faster (but gives worse results).

Since IntOpt-C cannot handle the variant of the 0-1 knapsack problem and the NSP, we only report
the runtime of IntOpt-C for the alloy production problem.

Since the provided code of CombOptNet is only available for the 0-1 knapsack problem, we only
report the runtime of CombOptNet for the 0-1 knapsack problem. As Table 14 shows, CombOptNet
is drastically slower than the proposed 2S method.

In the alloy production problem, the runtimes of the proposed 2S method are a little larger than that
of IntOpt-C. The reason is that 2S needs to solve two LPs when training while IntOpt-C only needs
to solve one. But in the alloy production problem, the unknown parameters are on the left hand side
of the inequality constraints and the gradient computation includes matrix computation, which is also
time-consuming. Thus, the runtimes of the 2S method are larger but not twice as large as that of the
IntOpt-C method.

In both the alloy production problem and the variant of the 0-1 knapsack problem, the runtimes of the
2S method are much better than RF.

The runtime of the 2S method is large in the NSP. This is because we use the formulation where each
decision variable corresponds to whether a specific nurse is assigned to a specific day and a specific
shift. Thus, the number of the decision variable of the relaxed LP is large and the LP takes more time
to solve.

Table 14: Average runtime (in seconds) for the alloy production, 0-1 knapsack, and nurse scheduling
problems.

Alloy production

0-1 knapsack

Titanium-alloy Capacity=100 Capacity=150 Capacity=200 Capacity=250
245.61

204.76

193.46

394.53
331.38

202.65
N\A
2394.05

2383.39

Runtime(s)

2S
IntOpt-C
CompOptNet
Ridge
k-NN
CART
RF
NN

Brass
268.22
228.00

20.22
25.14
30.33
959.50
212.22

N\A

2341.40

2940.26

56.89
70.22
94.89
2552.25
321.11

22.33
26.00
34.83
1034.07
135.80

26

Nurse scheduling

537.32

N\A
<1
<1
<1
2.11
11.39

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Two-Stage |     | Predict+Optimize |         |     |            | for Mixed | Integer |             | Linear |
| --------- | --- | ---------------- | ------- | --- | ---------- | --------- | ------- | ----------- | ------ |
| Programs  |     | with             | Unknown |     | Parameters |           | in      | Constraints |        |
XinyiHu1,JasperC.H.Lee2,JimmyH.M.Lee1
1DepartmentofComputerScienceandEngineering
TheChineseUniversityofHongKong,Shatin,N.T.,HongKong
2DepartmentofComputerSciences&InstituteforFoundationsofDataScience
UniversityofWisconsin–Madison,WI,USA
{xyhu,jlee}@cse.cuhk.edu.hk,jasper.lee@wisc.edu
Abstract
Considerthesettingofconstrainedoptimization,withsomeparametersunknown
|     | atsolvingtimeandrequiringpredictionfromrelevantfeatures. |           |     |            |          |            | Predict+Optimize |        |     |
| --- | -------------------------------------------------------- | --------- | --- | ---------- | -------- | ---------- | ---------------- | ------ | --- |
|     | is a recent                                              | framework | for | end-to-end | training | supervised | learning         | models | for |
suchpredictions,incorporatinginformationabouttheoptimizationprobleminthe
trainingprocessinordertoyieldbetterpredictionsintermsofthequalityofthe
|     | predictedsolutionunderthetrueparameters. |     |     |     |     | Almostallpriorworkshavefocused |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
onthespecialcasewheretheunknownsappearonlyintheoptimizationobjective
|     | andnottheconstraints.                   |           | Huetal.proposedthefirstadaptationofPredict+Optimize |          |            |                            |      |              |     |
| --- | --------------------------------------- | --------- | --------------------------------------------------- | -------- | ---------- | -------------------------- | ---- | ------------ | --- |
|     | tohandleunknownsappearinginconstraints, |           |                                                     |          |            | buttheframeworkhassomewhat |      |              |     |
|     | ad-hoc                                  | elements, | and they                                            | provided | a training | algorithm                  | only | for covering | and |
|     | packinglinearprograms.                  |           | Inthiswork,wegiveanewsimplerandmorepowerful         |          |            |                            |      |              |     |
frameworkcalledTwo-StagePredict+Optimize,whichwebelieveshouldbethe
|     | canonical     | framework | for the           | Predict+Optimize |        | setting.  | We also     | give a       | training |
| --- | ------------- | --------- | ----------------- | ---------------- | ------ | --------- | ----------- | ------------ | -------- |
|     | algorithm     | usable    | for all mixed     | integer          | linear | programs, | vastly      | generalizing | the      |
|     | applicability |           | of the framework. | Experimental     |        | results   | demonstrate | the          | superior |
predictionperformanceofourtrainingframeworkoverallclassicalandstate-of-
the-artmethods.
1 Introduction
Optimization problems are prevalent in modern society, and yet the problem parameters are not
alwaysavailableatthetimeofsolving. Forexample,considerthereal-worldapplicationscenario
ofstockingastore:asstoremanagers,weneedtoplacemonthlyordersforproductstostockinthe
store. Wewanttostockproductsthatsellfastandyieldhighprofits,asmuchofthemaspossible,
subjecttothehardconstraintoflimitedstoragespace. However,ordersneedtobeplacedtwoweeks
inadvanceofthemonthlydelivery,andthecustomerdemandnextmonthcannotbeknownexactly
atthetimeoforderplacement. Inthispaper, weconsiderthesupervisedlearningsetting, where
theunknownparameterscanbepredictedfromrelevantfeatures,andtherearesufficienthistorical
(features, parameters) pairs as training data for a prediction model. The goal, then, is to learn a
predictionmodelfromthetrainingdatasuchthat,ifweplugintheestimatedparametersintothe
optimizationproblemandsolveforanestimatedsolution, theestimatedsolutionremainsagood
solutionevenafterthetrueparametersarerevealed.
Theclassicapproachtotheproblemwouldbetotrainasimpleregressionmodel,basedonstandard
lossessuchas(regularized)ℓ loss,topredictparametersfromthefeatures. Itisshown,however,that
2
havingasmallpredictionerrorintheparameterspacedoesnotnecessarilymeanthattheestimated
solutionperformswellunderthetrueparameters. TherecentframeworkofPredict+Optimize,by
37thConferenceonNeuralInformationProcessingSystems(NeurIPS2023).

Elmachtoub and Grigas [7], instead proposes the more effective regret loss for training, which
compares the solution qualities of the true optimal solution and the estimated solution under the
trueparameters. Subsequentworks[6,8,10,13,17,19,27]havesinceappearedintheliterature,
applyingtheframeworktomoreandwiderclassesofoptimizationproblemsaswellasfocusingon
speed-vs-predictionaccuracytradeoffs.
However,allthesepriorworksfocusonlyonthecasewheretheunknownparametersappearinthe
optimizationobjective, andnotintheconstraints. Thetechnicalchallengeforthegeneralization
is immediate: if there were unknown parameters in the constraints, the estimated solution might
not even be feasible under the true parameters revealed afterwards! Thus, in order to tackle the
Predict+Optimizesettingwithunknownsinconstraints,therecentworkofHuetal.[12]presents
the first such adaptation on the framework: they view the estimated solution as representing a
softcommitment. Oncethetrueparametersarerevealed,correctiveactioncanbetakentoensure
feasibility,potentiallyatapenaltycorrespondingtothereal-lifecostof(partially)renegingonasoft
commitment. Theirframeworkcapturesapplicationscenarioswheneversuchcorrectionispossible,
andrequiresthepractitionertospecifyboththecorrectionmechanismandthepenaltyfunction.These
datacanbedeterminedandderivedfromthespecificapplicationscenario. Asanexample,inthe
product-stockingproblem,anadditionalunknownparameteristhestoragespace,becauseitdepends
onhowthecurrentproductsinthestoresellbeforetheneworderarrives. Weneedtoplaceorders
twoweeksaheadbasedonpredictedstoragespace. Thenightbeforetheorderarrives, weknow
thepreciseavailablespace,meaningthattheunknownparameterisrevealed. Apossiblecorrection
mechanismthenistothrowawayexcessproductsthatthestorecannotkeep,whileincurringthe
penaltythatistheretailpriceoftheproducts,aswellasdisposalfees.
WhiletheHuetal.[12]frameworkdoescapturemanyapplicationscenarios,thereareimportant
shortcomings. In their framework, they require the practitioner to specify a correction function
thatamendsaninfeasiblesolutionintoafeasiblesolution. However,thederivationofacorrection
functioncanberatherad-hocinnature. Inparticular,givenaninfeasibleestimatedsolution,there
maybemanywaystotransformthesolutionintoafeasibleone,andyettheirframeworkrequires
thepractitionertopickoneparticularway. Thisleadstotheseconddownside:itisdifficulttogivea
generalalgorithmicframeworkthatappliestoawidevarietyofoptimizationproblems. Huetal.had
torestricttheirattentiononlytopackingandcoveringlinearprograms,forwhichtheycouldpropose
agenericcorrectionfunction. Inthiswork,weaimtovastlygeneralizethekindsofoptimization
problems that Predict+Optimize can tackle under uncertainty in the constraints. In addition, the
approachofHuetal.failstohandletheinterestingsituationinwhichpost-hoccorrectionisstill
desirablewhentheestimatedsolutionisfeasiblebutnotgoodunderthetrueparameters.
Ourcontributionsarethree-fold:
•Tomitigatetheshortcomingsofthepriorwork,weproposeandadvocateanewframework,which
wecallTwo-StagePredict+Optimize1,thatisbothconceptuallysimplerandmoreexpressiveinterms
oftheclassofoptimizationproblemsitcantackle. Thekeyideaforthenewframeworkisthatthe
correctionfunctionisunnecessary. Allthatisrequiredisapenaltyfunctionthatcapturesthecostof
modifyingonesolutiontoanother. Apenaltyfunctionissufficientfordefiningacorrectionprocess:
weformulatethecorrectionprocessitselfasa“Stage2”optimizationproblem,takingtheoriginally
estimatedsolutionaswellasthepenaltyfunctionintoaccount.
•Underthisframework,wefurtherproposeageneralend-to-endtrainingalgorithmthatappliesnot
onlytopackingandcoveringlinearprograms,butalsotoallmixedintegerlinearprograms(MILPs).
WeadapttheapproachofMandiandGuns[18]togiveagradientmethodfortrainingneuralnetworks
topredictparametersfromfeatures.
•Weapplytheproposedmethodtothreebenchmarkstodemonstratethesuperiorempiricalperfor-
manceoverclassicalandstate-of-the-arttrainingmethods.
2 Background
Inthissection,wegivebasicdefinitionsforoptimizationproblemsandthePredict+Optimizesetting
[7],anddescribethestate-of-the-artframework[12]forPredict+Optimizewithunknownparameters
1Theliteraturesometimesuses“two-stage"tomeanapproacheswherethepredictionisagnostictothe
optimizationproblem.Here,“two-stage"referstothesoftcommitmentandthecorrection.
2

inconstraints.Thetheoryisstatedintermsofminimizationbutappliesofcoursealsotomaximization,
uponappropriatenegation.Withoutlossofgenerality,anoptimizationproblem(OP)P canbedefined
asfinding:
x∗ =argminobj(x) s.t. C(x)
x
wherex ∈ Rd isavectorofdecisionvariables, obj : Rd → Risafunctionmappingxtoareal
objectivevaluethatistobeminimized,andC isasetofconstraintsthatmustbesatisfiedoverx. We
callx∗anoptimalsolutionandobj(x∗)theoptimalvalue. Aparameterizedoptimizationproblem
(Para-OP)P(θ)isanextensionofanOPP:
x∗(θ)=argminobj(x,θ) s.t. C(x,θ)
x
whereθ ∈ Rt isavectorofparameters. Theobjectiveobj(x,θ)andconstraintsC(x,θ)canboth
dependonθ. Whentheparametersareknown,aPara-OPisjustanOP.
In the Predict+Optimize setting [7], the true parameters θ ∈ Rt for a Para-OP are not known at
solvingtime,andestimatedparametersθˆareusedinstead. Supposeeachparameterisestimatedby
mfeatures. Theestimationwillrelyonamachinelearningmodeltrainedovernobservationsofa
trainingdataset{(A1,θ1),...,(An,θn)}whereAi ∈Rt×m isafeaturematrixforθi,inorderto
yieldapredictionfunctionf :Rt×m →Rtpredictingparametersθˆ=f(A).
SolvingthePara-OPusingtheestimatedparameters,weobtainanestimatedsolutionx∗(θˆ). When
theunknownparametersappearinconstraints,onemajorchallengeisthatthefeasibleregionisonly
approximatedatsolvingtime, andhencetheestimatedsolutionmaybeinfeasibleunderthetrue
parameters. Fortunately,incertainapplications,theestimatedsolutionisnotahardcommitment,but
onlyrepresentsasoftcommitmentthatcanbemodifiedoncethetrueparametersarerevealed. Huet
al.[12]proposeaPredict+Optimizeframeworkforsuchapplications. Theframeworkisasfollows:
i)theunknownparametersareestimatedasθˆ,andanestimatedsolutionx∗(θˆ)issolvedusingthe
estimatedparameters,ii)thetrueparametersθarerevealed,andifx∗(θˆ)isinfeasibleunderθ,itis
amendedintoacorrectedsolutionx∗ (θˆ,θ)whilepotentiallyincurringsomepenalty,andfinally
corr
iii)thesolutionx∗ (θˆ,θ)isevaluatedaccordingtothesumofboththeobjective,underthetrue
corr
parametersθ,andtheincurredpenaltyfromcorrection.
Moreformally,acorrectionfunctiontakesanestimatedsolutionx∗(θˆ)andtrueparametersθand
returnsacorrectedsolutionx∗ (θˆ,θ)thatisfeasibleunderθ. ApenaltyfunctionPen(x∗(θˆ) →
corr
x∗ (θˆ,θ))takesanestimatedsolutionx∗(θˆ)andthecorrectedsolutionx∗ (θˆ,θ)andreturnsanon-
corr corr
negativepenalty. Boththecorrectionfunctionandthepenaltyfunctionshouldbechosenaccordingto
thepreciseapplicationscenarioathand. Thefinalcorrectedsolutionx∗ (θˆ,θ)isevaluatedusing
corr
thepost-hocregret,whichisdefinedwithrespecttothecorrectedsolutionx∗ (θˆ,θ)andthepenalty
corr
functionPen(x∗(θˆ)→x∗ (θˆ,θ)). Thepost-hocregretisthesumoftwoterms:(a)thedifference
corr
inobjectivebetweenthetrueoptimalsolutionx∗(θ)andthecorrectedsolutionx∗ (θˆ,θ)underthe
corr
trueparametersθ,and(b)thepenaltythatthecorrectionprocessincurs. Mathematically,thepost-hoc
regretfunctionPReg(θˆ,θ): Rt×Rt →R (forminimizationproblems)is:
≥0
PReg(θˆ,θ)= obj(x∗ (θˆ,θ),θ)−obj(x∗(θ),θ) + Pen(x∗(θˆ)→x∗ (θˆ,θ)) (1)
corr corr
whereobj(x∗ (θˆ,θ),θ)isthecorrectedoptimalvalueandobj(x∗(θ),θ)isthetrueoptimalvalue.
corr
Giventhepost-hocregretasalossfunction,theempiricalriskminimizationprincipledictatesthatwe
choosethepredictionfunctiontobethefunctionf fromthesetofmodelsF attainingthesmallest
averagepost-hocregretoverthetrainingdata:
n
1 (cid:88)
f∗ =argmin PReg(f(Ai),θi) (2)
n
f∈F
i=1
3 Two-stagePredict+OptimizeFramework
While the prior work by Hu et al. [12] is the first Predict+Optimize framework for unknowns in
constraints,andisindeedapplicabletoagoodrangeofapplications,ithasseveralshortcomings.
3

First,theframeworkrequiresmathematicallyformalizingbothapenaltyfunctionandacorrection
functionfromtheapplicationscenario,andessentiallyimposesdifferentiabilityassumptionsonthe
correctionfunctionfortheframeworktobeusable. Thead-hocnatureofwritingdownacorrection
functionlimitsthepracticalapplicabilityoftheframework. Second,asaresultofneedingasingle
(differentiable)correctionfunction,Huetal.[12]neededtorestricttheirattentiontoonlypacking
andcoveringlinearprograms,inordertoderiveageneralcorrectionfunctionthatisapplicabletoall
theinstances. Thisalsosignificantlylimitstheimmediateapplicabilityoftheirframework. Third,
theirframeworkonlycorrectsanestimatedsolutionwhenitisinfeasibleunderthetrueparameters.
Yet, thereareapplicationswherecorrectionsarepossibleevenwhentheestimatedsolutionwere
feasible,butjustnotverygoodunderthetrueparameters.
Inthispaper,weadvocateusingasimpleryetmorepowerfulframework,whichwecallTwo-Stage
Predict+Optimize,addressingalloftheaboveshortcomings. Thesimplifiedperspectivewillallowus
todiscussmoreeasilyhowtohandletheentireclassofmixedintegerlinearprograms(MILPs)instead
ofbeingrestrictedtojustpackingandcoveringlinearprograms.SinceMILPsincludealloptimization
problemsinNP(underareasonabledefinitionofNPforoptimizationproblems),ourframework
is significantly more applicable in practice. We will describe the Two-Stage Predict+Optimize
frameworkbelow,anddiscussitsapplicationtoMILPsinthenextsection.
Ourframeworkissimple:weforgotheideaofacorrectionfunctionandtreatcorrectionitselfas
an optimization problem, based on the penalty function, the estimated solution and the revealed
trueparameters. RecalltheHuetal.viewofPredict+Optimizeunderuncertaintiesinconstraints:
theestimatedsolutionisaformofsoftcommitment,whichcanbemodifiedatacostoncethetrue
parameters are revealed. The penalty function describes the cost of changing from an estimated
solution to a final solution. The main observation is that, given an estimated solution and the
revealedparameters,weshouldinfactsolveanewoptimizationproblem,formedbyapplyingthetrue
parameterstotheoriginaloptimization,andaddingthepenaltyfunctiontotheobjective. Thefinal
solutionfromthisnewoptimizationthustakesthepenaltyofcorrectionintoaccount. Thisapproach
yieldsthreeimmediateadvantages. First,thepractitionernolongerneedstospecifyacorrection
function, thus reducing the ad-hoc nature of the framework. Second, even feasible solutions are
allowedtobemodifiedafterthetrueparametersarerevealedifthepenaltyofdoingsoisnotinfinity.
Third,conditionedonthesamepenaltyfunction,thesolutionqualityfromourtwo-stageoptimization
approachisalwaysatleastasgoodasthatfromusinganycorrectionfunction. Thelastadvantageis
presentedasPropositionA.1.
NowweformallydefinetheTwo-StagePredict+Optimizeframework.
I.InStage1,theunknownparametersareestimatedasθˆfromfeatures. Thepractitionerthensolves
theStage1optimization,whichisthePara-OPusingtheestimatedparameters,toobtaintheStage1
solutionx∗. TheStage1solutionshouldbeinterpretedassomeformofsoftcommitment,thatwe
1
gettomodifyinStage2atextracost/penalty. AssumingthenotationofthePara-OPinSection2,the
Stage1OPcanbeformulatedas:
x∗ =argmin obj(x,θˆ) s.t. C(x,θˆ)
1
x
II.AtthebeginningofStage2,thetrueparametersθarerevealed. TheStage2optimizationproblem
augmentstheoriginalStage1problembyaddingapenaltytermPen(x∗ →x∗,θ)totheobjective,
1 2
which accounts for the penalty (modelled from the application scenario) for changing from the
softly-committedStage1solutionx∗tothenewStage2andfinalsolutionx∗. TheStage2OPcan
1 2
thenbeformulatedas:
x∗ =argmin obj(x,θ)+Pen(x∗ →x,θ) s.t. C(x,θ)
2 1
x
SolvingtheStage2problemyieldsthefinalStage2“corrected”solutionx∗.
2
III.TheStage2solutionx∗isevaluatedaccordingtotheanalogouspost-hocregret,asfollows:
2
PReg(θˆ,θ)= obj(x∗,θ)+Pen(x∗ →x∗,θ)−obj(x∗(θ),θ)
2 1 2
whereagain,x∗(θ)isanoptimalsolutionofthePara-OPunderthetrueparametersθ. Notethatthe
post-hocregretdependsonallofa)thepredictedparameters,b)theinducedStage1solution,c)the
trueparametersandd)thefinalStage2solution.
Toseethisnewframeworkappliesinpractice,thefollowingexampleexpandsontheproduct-stocking
problemintheintroduction.
4

Example1. Considertheproduct-stockingproblemagain,whereregularordershavetobeplaced
twoweeksaheadofmonthlydeliveries. Sincetheavailablespaceatthetimeofdeliveryisunknown
whenweplacetheregularorders,dependingonthesalesoverthenexttwoweeks,weneedtomake
apredictionontheavailablespacetomakeacorrespondingorder. Welearnthepredictorusing
historicalsalesrecordsfromfeaturessuchastime-of-yearandprice. Then,weusethepredicted
availablespacetooptimizefortheregularorderweplace. ThisistheStage1solution.
Thenightbeforetheorderarrives,theunknownconstraintparameter,i.e.thepreciseavailablespace,
isrevealed. Wecanthencheckifwehaveover-orderedorunder-ordered. Inthecaseofover-ordering,
we would have to call and ask the wholesale company to drop some items from the order. The
companywouldperhapsallowtakingtheitemsoffthefinalbill,butnaturallytheyhaveasurcharge
forlast-minutechanges. Similarly,ifweunder-ordered,wemightrequestthewholesalecompanyto
sendusmoreproducts,againnaturallywithasurchargeforlast-minuteordering. Theupdatedorder
istheStage2decision. Theincurredwholesalersurchargesinducethepenaltyfunction.
Areaderwhoisfamiliarwiththeliteratureontwo-stageoptimizationproblemsmaynotethatthe
aboveframeworkisphrasedslightlydifferentlyfromsomeothertwo-stageproblemformulations. In
particular,sometwo-stageframeworksphraseStage1solutionsashardcommitments,andinclude
recoursevariablesinbothstagesofoptimizationtomodelwhatchangesaremadeinStage2. We
showinAppendixA.1howourframeworkcancapturethisotherperspective,andingeneraldiscuss
howproblemmodellingcanbedoneinournewframework.
Thereadermayalsowonder:whataboutapplicationscenarioswherethe(Stage1)estimatedsolution
isahardcommitment,andthereisabsolutelynocorrection/recourseavailable? InAppendixA.2,we
discusshowourframeworkisstillusefulandapplicableforlearninginthesesituations.
We also give a more detailed comparison, in Appendix A.3, between our new Two-Stage Pre-
dict+OptimizeframeworkandthepriorHuetal.framework. Technically,ifweignored differen-
tiabilityissues,thetwoframeworksaremathematicallyequivalentinexpressiveness. However,we
stressthatournewframeworkisbothconceptuallysimplerandeasiertoapplytoafarwiderclass
ofoptimizationproblems. Weshowconcretelyinthenextsectionhowtoend-to-endtrainaneural
network for this framework for all MILPs, vastly generalizing the method of Hu et al. which is
restrictedtopackingandcovering(non-integer)linearprograms. Inaddition,AppendixA.3also
statesandprovesPropositionA.1,thatifwefixanoptimizationproblem,apredictionmodelanda
penaltyfunction,thenthesolutionqualityfromourtwo-stageapproachisalwaysatleastasgoodas
usingthecorrectionfunctionapproach.
4 Two-StagePredict+OptimizeonMILPs
Inthissection,wedescribehowtogiveanend-to-endtrainingmethodforneuralnetworkstopredict
unknownparametersfromfeatures,undertheTwo-StagePredict+Optimizeframework.Thefollowing
algorithmicmethodisapplicablewheneverbothstagesofoptimizationareexpressibleasMILPs.
Duetothepagelimit,thediscussioninthissectionishigh-levelandbrief,withallthecalculation
detailsdeferredtoAppendixB.
Thestandardwaytotrainaneuralnetworkistouseagradient-basedmethod. IntheTwo-Stage
Predict+Optimizeframework,weusethepost-hocregretPRegasthelossfunction. Therefore,for
eachedgeweightw intheneuralnetwork,weneedtocomputethederivative dPReg. Usingthelaw
e dwe
oftotalderivative,weget
(cid:12) (cid:12)
dPReg(θˆ,θ) ∂PReg(θˆ,θ)(cid:12) ∂x∗∂x∗ ∂θˆ ∂PReg(θˆ,θ)(cid:12) ∂x∗ ∂θˆ
= (cid:12) 2 1 + (cid:12) 1 (3)
dw
e
∂x∗
2
(cid:12)
(cid:12) x∗
∂x∗
1
∂θˆ ∂w
e
∂x∗
1
(cid:12)
(cid:12) x∗
∂θˆ ∂w
e
1 2
Assuch,wewishtocalculateeachtermontherighthandside.
The easiest term to handle is ∂θˆ , since θˆis the neural network output, and so the derivatives
∂we
(cid:12)
canbedirectlycalculatedbystandardbackpropagation[25]. Asfortheterms
∂PReg(θˆ,θ)(cid:12)
and
∂x∗
2
(cid:12)
x∗
(cid:12) 1
∂PReg(θˆ,θ)(cid:12)
, they are easily calculable whenever both the optimization objective and penalty
∂x∗
1
(cid:12)
x∗
2
functionaresmooth,andinfactlinearasinthecaseofMILPs. Whatremainsaretheterms
∂x∗
2 and
∂x∗
1
5

∂x∗ 1. Thechallengeisthatx∗ isthesolutionofaMILPoptimization(Stage2)thatusesx∗ asits
∂θˆ 2 1
parameters,i.e.,differentiatethroughaMILP.Similarly,x∗dependsonθˆthroughaMILP(Stage1).
1
SinceMILPoptimamaynotchangeunderminorparameterperturbations,thegradientscanbeeither
0ornon-existent,whichareuninformative. Wethusneedtocomputesomeapproximationinorderto
getusefultrainingsignals.
Our approach, inspired by the work of Mandi and Guns [18], is to define a new surrogate loss
(cid:94)
function PReg that is differentiable and produces informative gradients. Prior works related to
learningunknownsinconstraints[1,2,27]givewaysofdifferentiatingthroughLPsorLPswith
regularizations. Theseworkscanbeusedinplaceoftheproposedapproach. However,experiments
inAppendixEdemonstratethattheproposedapproachperformsatleastaswellinpost-hocregret
performanceastheothers,whilebeingfaster. Weshowtheconstructionoftheproposedapproach
below,andnotethatitdoesnothaveasimpleclosedform. Nonetheless,wecancomputeitsgradients.
TherestofthesectionassumesthatbothstagesofoptimizationareexpressibleasaMILPinthe
followingstandardform:
x∗ =argminc⊤x s.t. Ax=b,Gx≥h,x≥0,x ∈Z (4)
S
x
withdecisionvariablesx ∈ Rd andproblemparametersc ∈ Rd,A ∈ Rp×d,b ∈ Rp,G ∈ Rq×d,
h ∈ Rq. ThesubsetofindicesS denotesthesetofvariablesthatareunderintegralityconstraints.
Sincetheunknownparametersmayappearinanycombinationofc,A,b,GandhintheStage1
optimization for x∗, the surrogate loss function construction needs computable and informative
1
gradientsforallof
∂x∗
,
∂x∗
,
∂x∗
,
∂x∗
and
∂x∗
.
∂c ∂A ∂b ∂G ∂h
Wefollowtheinterior-pointbasedapproachofMandiandGuns[18],usedalsobyHuetal.[12].
Considerthefollowingconvexrelaxationof(4),forafixedvalueofµ≥0:
d q
(cid:88) (cid:88)
x∗ =argminc⊤x−µ ln(x )−µ ln(s )s.t. Ax=b,Gx−s=h (5)
i i
x,s
i=1 i=1
Thisisarelaxationof(4)byi)droppingallintegralityconstraints,ii)introducingslackvariables
s ≥ 0toturnGx ≥ hintoGx−s = handiii)replacingboththex ≥ 0ands ≥ 0constraints
withthelogarithmbarriertermsintheobjective,withmultiplierµ≥0. Theobservationisthatthe
gradients ∂x, ∂x, ∂x, ∂x and ∂x for(5)areallwell-defined,computableandinformativeforafixed
∂c ∂A ∂b ∂G ∂h
valueofµ≥0: Slater’sconditionholdsfor(5),andsotheKKTconditionsmustbesatisfiedatthe
optimum(x∗,s∗)of(5). WecanthuscomputealltherelevantgradientsviadifferentiatingtheKKT
conditions,usingtheimplicitfunctiontheorem. WegiveallthecalculationdetailsinAppendixB.
Giventheaboveobservation,wethenaimtoconstructthesurrogatelossfunctionbyreplacingthex∗
1
andx∗,whicharesupposedtosolvedusingMILP(4),witha)x thatissolvedfromprogram(5)
2 (cid:101)1
relaxationoftheStage1optimizationproblem,usingthepredictedparametersθˆandb)x thatis
(cid:101)2
solvedfromtheprogram(5)relaxedversionofStage2optimization,usingx andthetrueparameters
(cid:101)1
θ. Theonlyremainingquestionthen,is,whichvaluesofµdoweuseforthetworelaxedproblems?
GivenaMILPintheformof(4),theinterior-pointbasedsolverofMandiandGuns[18]generates
andsolves(5)forasequenceofdecreasingnon-negativeµ,withaterminationconditionthatµcannot
besmallerthansomecutoffvalue. Thus, wesimplychoosethecutoffvaluetouseas“µ”in(5),
(cid:94)
whichthencompletesthedefinitionofthesurrogatelossPReg.
(cid:94)
Algorithmically,wetraintheneuralnetworkonthesurrogatelossPRegasfollows: givenpredicted
parameters,weruntheMandiandGunssolvertogettheoptimalsolution(x∗,s∗)forthefinalvalue
ofµ. Wecanthencomputethegradientoftheoutputsolutionwithrespecttoanyoftheproblem
parametersusingthecalculationsinAppendixB,combinedwithbackpropagation,toyield
dP(cid:94)Reg
dwe
accordingtoEquation(3).
InAppendixC,wegivethreeexampleapplicationscenarios,alongwiththeirpenaltyfunctions,that
ourtrainingapproachcanhandle. Theseproblemsare:a)analloyproductionproblem,forfactory
tryingtosourceoresunderuncertaintyinchemicalcompositionsintherawmaterials,b)avariantof
theclassic0-1knapsackwithunknownweightsandrewards,andc)anurserosterschedulingproblem
with unknown patient load. We show explicitly in Appendix C how both stages of optimization
6

Table1: Relevantproblemsizesofthethreebenchmarks.
Problemname Brassalloyproduction Titanium-alloyproduction 0-1knapsack Nurseschedulingproblem
Dimensionofx 10 10 10 315
Numberofconstraints 12 14 21 846
Numberofunknownparameters 20 40 10 21
Numberoffeatures(perparameter) 4096 4096 4096 8
canbeformulatedasMILPsfortheseapplications,andapplytheAppendixBcalculationstoyield
(cid:94)
gradientcomputationformulasforthesurrogatelossPRegfortheseproblems.
A limitation of our approach is the requirement that both stages must be expressible as MILPs,
constrainingtheoptimizationobjectivestobelinearintheMILPdecisionvariables. Thiscontrasts
theHuetal.framework[12]whichhandlesnon-linearpenalties. WepointoutthatevenMILPscan
handlesomenon-linearitybyusingextradecisionvariables:forexample,theabsolute-valuefunction.
Moreover, the Appendix B gradient calculations can be adapted to handle general differentiable
non-linear objectives. We present only MILPs as a main overarching application for this paper
becauseoftheirwidespreaduseindiscreteoptimization,withreadilyavailablesolvers.
5 ExperimentalEvaluation
Weevaluatetheproposedmethod2onthreebenchmarksdescribedinSection4andAppendixC.Table
1reportstherelevantbenchmarkproblemsizes. Wecompareourmethod(2S)withthestateoftheart
Predict+Optimizemethod,IntOpt-C[12],and5classicalregressionmethods[9]:ridgeregression
(Ridge),k-nearestneighbors(k-NN),classificationandregressiontree(CART),randomforest(RF),
andneuralnetwork(NN).Allofthesemethodsusetheirclassiclossfunctiontotraintheprediction
models. Attesttime,toensurethefeasibilityofthesolutionswhencomputingthepost-hocregret,
weperformStage2optimizationontheestimatedsolutionsfortheseclassicalregressionmethods
beforeevaluatingthefinalsolution. Additionally,CombOptNet[23]isadifferentmethodfocusing
onlearningunknownsinconstraints,butwithadifferentgoalandlossfunction. Weexperimentally
compareourproposedmethodwithCombOptNetonthe0-1knapsackbenchmark—theonlywith
availableCombOptNetcode. WealsopresentaqualitativecomparisoninSection6.
Inthefollowingexperiments,wewillneedtotakecaretodistinguishtwo-stageoptimizationasa
trainingtechnique(Section4)andasanevaluationframework(Section3).Wewilldenoteourtraining
methodas“2S”intheexperiments,andwhenwesay“Two-StagePredict+Optimize”framework,
wealwaysmeanitasanevaluationframework. 2SisalwaysevaluatedaccordingtotheTwo-Stage
Predict+Optimizeframework. Asexplainedabove,wewillalsoevaluatealltheclassicaltraining
methodsusingtheTwo-StagePredict+Optimizeframework. Forourcomparisonwiththepriorwork
ofHuetal.[12],wewillalsodistinguishtheirtrainingmethodandevaluationframework. Thename
“IntOpt-C”alwaysreferstotheirtrainingmethodusingtheircorrectionfunction. Wewillsimply
calltheirevaluationframeworkthe“Huetal.framework”orwithsimilarphrasing(seeSection2to
recalldetails). IntOpt-CwillsometimesbeevaluatedusingournewTwo-StagePredict+Optimize
framework,andsometimesthepriorframeworkofHuetal.[12]usingtheircorrectionfunction.
Themethodsofk-NN,RF,NN,andIntOpt-Caswellas2Shavehyperparameters,whichwetunevia
cross-validation. WeincludethehyperparametertypesandchosenvaluesinAppendixD.Inthemain
paperweonlyreportthepredictionperformances. SeeAppendixHforruntimecomparisons.
AlloyProductionProblem ThealloyproductionproblemisacoveringLP,seeAppendixC.1for
thepracticalmotivationandLPmodel. SinceHuetal.[12]alsoexperimentedonthisproblem,we
useittocompareour2SmethodwithIntOpt-C[12],usingthesamedatasetandexperimentalsetting.
Weconductexperimentsontheproductionoftworealalloys:brassandanalloyblendforstrength-
eningTitanium. Forbrass,2kindsofmetalmaterials,CuandZn,arerequired[14]. Theblendof
thetwomaterialsare,proportionally,req =[627.54,369.72]. Forthetitanium-strengtheningalloy,
4kindsofmetalmaterials,C,Al,V,andFe,arerequired[15]. Theblendofthefourmaterialsare
proportionaltoreq =[0.8,60,40,2.5]. WeusethesamerealdataasthatusedinIntOpt-C[12]as
numericalvaluesinourexperimentinstances. Inthisdataset[23],eachunknownmetalconcentration
2Ourimplementationisavailableathttps://github.com/Elizabethxyhu/NeurIPS_Two_Stage_Predict-Optimize
7

Table2: ComparisonoftheTwo-StagePredict+OptimizeframeworkandtheHuetal. frameworkon
thealloyproductionproblem.
|     |       | PReg          | Two-StagePredict   | Huetal.     |     |
| --- | ----- | ------------- | ------------------ | ----------- | --- |
|     | Alloy | Penaltyfactor | +OptimizeFramework | Framework   |     |
|     |       | 0.25±0.015    | 43.87±2.73         | 68.16±6.26  |     |
|     |       | 0.5±0.015     | 65.71±4.81         | 82.91±5.45  |     |
|     |       | 1±0.015       | 88.75±5.91         | 107.64±6.85 |     |
Brass
|     |                | 2±0.015    | 123.90±6.84  | 150.47±12.99 |     |
| --- | -------------- | ---------- | ------------ | ------------ | --- |
|     |                | 4±0.015    | 161.86±8.49  | 178.69±10.09 |     |
|     |                | 8±0.015    | 194.06±13.09 | 206.84±12.51 |     |
|     |                | 0.25±0.015 | 4.52±0.47    | 6.45±0.81    |     |
|     |                | 0.5±0.015  | 6.03±0.62    | 7.90±0.56    |     |
|     | Titanium-alloy | 1±0.015    | 8.58±0.74    | 10.73±0.81   |     |
|     |                | 2±0.015    | 12.17±1.24   | 14.17±1.31   |     |
|     |                | 4±0.015    | 16.10±1.06   | 17.48±0.99   |     |
|     |                | 8±0.015    | 19.69±0.91   | 21.08±1.91   |     |
Table3: Meanpost-hocregretsandstandarddeviationsforthealloyproductionproblemusingthe
Two-StagePredict+Optimizeframework.
PReg
|     | 2S  | IntOpt-C | Ridge k-NN | CART RF | NN TOV |
| --- | --- | -------- | ---------- | ------- | ------ |
Alloy Penaltyfactor
| 0.25±0.015 | 43.87±2.73 | 45.27±3.35 60.80±2.55 | 63.32±4.39 | 77.80±6.37 60.85±2.35  | 64.96±3.58 |
| ---------- | ---------- | --------------------- | ---------- | ---------------------- | ---------- |
| 0.5±0.015  | 65.71±4.81 | 67.69±4.25 71.12±3.48 | 74.36±5.69 | 93.67±7.03 70.86±3.29  | 74.32±2.90 |
| 1±0.015    | 88.75±5.91 | 89.83±4.79 91.82±6.41 | 96.52±8.90 | 125.50±9.49 90.97±6.14 | 93.12±4.24 |
Brass 312.02±6.94
| 2±0.015 | 123.90±6.84  | 125.46±9.26 133.18±12.98  | 140.77±16.02 | 189.12±16.10 131.12±12.48 | 130.67±10.52 |
| ------- | ------------ | ------------------------- | ------------ | ------------------------- | ------------ |
| 4±0.015 | 161.86±8.49  | 164.94±10.33 215.87±26.54 | 229.22±30.74 | 316.31±30.95 211.40±25.56 | 205.76±24.33 |
| 8±0.015 | 194.06±13.09 | 200.42±8.51 381.30±53.75  | 406.19±60.42 | 570.75±61.42 372.01±51.82 | 355.96±52.25 |
4.52±0.47
| 0.25±0.015 |           | 4.72±0.58 6.43±0.39  | 6.13±0.34 | 7.07±0.45 5.75±0.48  | 6.56±0.59 |
| ---------- | --------- | -------------------- | --------- | -------------------- | --------- |
| 0.5±0.015  | 6.03±0.62 | 6.23±0.64 7.71±0.45  | 7.27±0.39 | 8.57±0.45 6.76±0.55  | 7.38±0.67 |
| 1±0.015    | 8.58±0.74 | 8.71±0.95 10.26±0.62 | 9.55±0.52 | 11.57±0.52 8.76±0.72 | 9.03±0.84 |
Titanium-alloy 2±0.015 12.17±1.24 12.31±1.31 15.37±1.03 14.11±0.84 17.57±0.80 12.78±1.11 12.34±1.21 30.27±0.54
| 4±0.015 | 16.10±1.06 | 16.97±1.70 25.60±1.89 | 23.24±1.56 | 29.57±1.53 20.81±1.93 | 18.95±2.00 |
| ------- | ---------- | --------------------- | ---------- | --------------------- | ---------- |
| 8±0.015 | 19.69±0.91 | 20.80±1.74 46.04±3.65 | 41.49±3.03 | 53.57±3.10 36.88±3.63 | 32.16±3.60 |
isrelatedto4096features. Forexperimentsonbothalloys,350instancesareusedfortrainingand
150instancesfortestingthemodelperformance. ForNN,IntOpt-C,and2S,weusea5-layerfully
connectednetworkwith512neuronsperhiddenlayer.
InthepenaltyfunctiondescribedinAppendixC.1,weneedtochooseapenaltyfactor/multiplierfor
eachsupplier. Weconductexperimentson6typesofpenaltyfactor(σ)settings: 6vectorswhere
eachentryisi.i.d.uniformlysampledfrom[0.25±0.015],[0.5±0.015],[1.0±0.015],[2.0±0.015],
[4.0±0.015],and[8.0±0.015]respectively. Thisrandomsamplingofσ ensuresthatthepenalty
factorforeachsupplierisdifferent,butremainsroughlyonthesamescale.
Thefirstexperimentweruncompares2S+Two-StagePredict+OptimizeframeworkwithIntOpt-C+Hu
etal.framework.Specifically,wecomparea)using2SfortrainingandevaluatingusingtheTwo-Stage
Predict+OptimizeframeworkinSection3,versusb)usingIntOpt-Cfortrainingandevaluatingusing
thesamecorrectionfunctionfromtraining,accordingtotheHuetal.frameworkdescribedinSection2.
Table2comparesthemeanpost-hocregretandstandarddeviationsforthealloyproductionproblem
for the two different frameworks. The table shows that Two-Stage Predict+Optimize framework
always achieves smaller mean post-hoc regret than the Hu et al. framework. Compared with the
Huetal.framework,ourframeworkobtains6.18%-35.63%smallermeanpost-hocregretinbrass
production,and6.59%-29.89%smallermeanpost-hocregretintitanium-alloyproduction.
WepresentafurthercomparisoninAppendixFwithavariantoftheHuetal.framework—theℓ
2
projectionideain[3],whichperformsevenworsethantheHuetal.framework.
ThesecondexperimentcomparesvarioustrainingapproachesallevaluatedundertheTwo-Stage
Predict+Optimizeframework. Thatis,themodelsaretraineddifferently,butattesttime,wealways
useStage2optimizationtogiveafinalsolutionandevaluatepost-hocregretonit. Table3reportsthe
meanpost-hocregretsandstandarddeviationsacross10runsforeachtrainingmethodonthealloy
productionproblem. Thetableshowsthatourmethod,2S,achievesthebestperformance,compared
withIntOpt-Cachievingthesecondbestperformance,beatingalltheclassicaltrainingapproaches.
ComparedwithIntOpt-C,2Sobtains1.20%-3.18%smallermeanpost-hocregretsinbrassproduction,
and1.18%-5.33%smallermeanpost-hocregretintitanium-alloyproduction. Comparedwiththe
classicalapproaches,theimprovementsaremuchmoresignificant. 2Sobtainsatleast2.44%-45.48%
smallermeanpost-hocregretsinbrassproduction,andatleast1.39%-38.78%smallermeanpost-hoc
regretintitanium-alloyproduction. TheaverageTrueOptimalValues(TOV)arereportedinthelast
columnofTable3forreference,althoughthereadershouldtakecaretonotover-interprettheratio
8

Table4:Meanpost-hocregretsandstandarddeviationsfor0-1knapsackproblemusingtheTwo-Stage
Predict+Optimizeframework.
Penalty
| PReg | 2S  | CombOptNet | Ridge | k-NN | CART |     | RF NN | TOV |
| ---- | --- | ---------- | ----- | ---- | ---- | --- | ----- | --- |
factor
| 0.21 | 1.26±0.01 | 9.45±0.19 | 9.46±0.19 | 9.38±0.21 | 8.67±0.13 | 9.50±0.26 | 9.81±0.20 |     |
| ---- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --- |
100 0.25 6.28±0.05 9.60±0.22 9.77±0.19 9.70±0.19 9.19±0.12 9.82±0.27 10.11±0.20 29.68±0.14
| 0.3  | 9.22±0.10 | 10.45±0.34 | 10.16±0.19 | 10.10±0.18 | 9.85±0.11 | 10.22±0.28 | 10.49±0.21 |     |
| ---- | --------- | ---------- | ---------- | ---------- | --------- | ---------- | ---------- | --- |
| 0.21 | 0.73±0.01 | 8.90±8.97  | 9.12±0.22  | 8.91±0.20  | 8.46±0.18 | 9.20±0.27  | 9.66±0.47  |     |
150 0.25 3.64±0.04 9.11±9.41 9.40±0.21 9.19±0.20 8.88±0.17 9.47±0.26 9.92±0.43 40.23±0.19
| 0.3  | 7.27±0.06 | 9.34±9.38  | 9.76±0.22 | 9.53±0.19 | 9.41±0.17 | 9.81±0.24 | 10.23±0.38 |     |
| ---- | --------- | ---------- | --------- | --------- | --------- | --------- | ---------- | --- |
| 0.21 | 0.33±0.01 | 15.16±0.21 | 6.57±0.21 | 6.38±0.29 | 6.26±0.21 | 6.59±0.23 | 7.08±0.95  |     |
200 0.25 1.67±0.03 15.20±0.27 6.80±0.20 6.62±0.29 6.57±0.19 6.82±0.21 7.27±0.88 48.13±0.24
| 0.3  | 3.33±0.06 | 15.25±0.22 | 7.09±0.19 | 6.91±0.28 | 6.95±0.19 | 7.10±0.18 | 7.52±0.80 |     |
| ---- | --------- | ---------- | --------- | --------- | --------- | --------- | --------- | --- |
| 0.21 | 0.07±0.00 | 20.42±0.25 | 2.39±0.22 | 2.18±0.20 | 2.45±0.20 | 2.34±0.32 | 2.70±1.34 |     |
250 0.25 0.34±0.02 20.47±0.13 2.53±0.21 2.34±0.19 2.60±0.19 2.49±0.30 2.82±1.26 53.43±0.26
| 0.3 | 0.69±0.04 | 20.54±0.32 | 2.71±0.20 | 2.54±0.18 | 2.79±0.18 | 2.67±0.28 | 2.97±1.16 |     |
| --- | --------- | ---------- | --------- | --------- | --------- | --------- | --------- | --- |
Table 5: Mean post-hoc regrets and standard deviations for the NSP using the Two-Stage Pre-
dict+Optimizeframework.
| Penaltyfactor | 2S         | Ridge       | k-NN        | CART         |     | RF          | NN         | TOV |
| ------------- | ---------- | ----------- | ----------- | ------------ | --- | ----------- | ---------- | --- |
| 0.25±0.015    | 3.94±1.91  | 6.45±4.68   | 15.20±5.76  | 26.20±8.96   |     | 19.47±7.19  | 4.27±2.22  |     |
| 0.5±0.015     | 6.92±2.26  | 12.68±9.35  | 30.29±11.53 | 52.47±17.96  |     | 38.93±14.42 | 8.20±4.40  |     |
| 1.0±0.015     | 13.12±3.15 | 25.12±18.71 | 60.43±23.07 | 105.01±36.00 |     | 77.86±28.99 | 16.00±8.78 |     |
190.21±26.17
| 2.0±0.015 | 25.04±9.29  | 49.95±37.39   | 120.62±46.08  | 210.02±72.06  |     | 155.64±58.06  | 31.51±17.40  |     |
| --------- | ----------- | ------------- | ------------- | ------------- | --- | ------------- | ------------ | --- |
| 4.0±0.015 | 33.29±9.53  | 99.61±74.78   | 241.01±92.14  | 420.04±144.18 |     | 311.19±116.23 | 62.52±34.64  |     |
| 8.0±0.015 | 46.72±14.80 | 198.91±149.54 | 481.79±184.27 | 840.10±288.45 |     | 622.32±232.56 | 124.54±69.14 |     |
betweenthepost-hocregretandthetrueoptimalvalue,sincethepost-hocregretalsoincludesthe
penaltytermwhichincreaseswiththepenaltyfactors.
0-1knapsack Inthesecondexample,weshowcaseourframeworkonapackingintegerprogram-
mingproblem,avariantofthe0-1knapsackproblem,withunknownitempricesp andsizess . See
|     |     |     |     |     |     |     | i   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
AppendixC.2fordetailsofanapplicationinrunninga“proxybuyer”business. Here,theunknown
parametersappearinboththeobjectiveandconstraints. Theproposed2Smethodcanhandlethis
MILPstraightforwardly,buttheIntOpt-Cmethodcannotbeapplied. Thus,weonlyexperimentwith
theTwo-StagePredict+Optimizeframeworkforevaluation,andcomparetheproposed2Smethod
withclassicalapproachesandCombOptNet. Again,allapproachesareevaluatedattesttimeusing
theStage2optimizationtoyieldthefinalsolution,onwhichthepost-hocregretiscomputed.
TheMILPformulationofthetwostagesandthepenaltyfunctionaredescribedinAppendixC.2.
WeusethedatasetofPaulusetal.[23],inwhicheach0-1knapsackinstanceconsistsof10items
andeachitemhas4096featuresrelatedtoitspriceandsize. ForbothNNandourmethod,weusea
5-layerfully-connectednetworkwith512neuronsperhiddenlayer. Weconductexperimentson4
differentknapsackcapacities:100,150,200,and250. Weuse700instancesfortrainingand300
instancesfortestingthemodelperformance. Consideringthereal-lifesetting,weuse3scalesofthe
| penaltyfactorforthepenaltyfunctioninAppendixC.2:σ |     |     |     |     | =0.05,0.25,or0.5. |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
Table4reportsthemeanpost-hocregretsandstandarddeviationsacross10runsforeachapproach
onthis0-1knapsackproblem. Duetothespacelimitationandthefactthatlargerpenaltyfactors
areunrealisticinthisproblemsetting,wepresentpenaltyfactors≥1inAppendixG.Theaverage
TrueOptimalValues(TOV)arereportedinthelastcolumn,againforreference. Asshowninthe
table,ourproposed2Smethodhassignificantlybetterresults. Inaddition,weobservethatacross
allapproaches,thepost-hocregretsdecreaseastheknapsackcapacityincreases:thisisduetothe
factthatasthecapacityincreases,moreandmoreitemscanbeselected,andsominorinaccuracies
inpredictedvalues/weightsdonotaffecttheselectedsetofitemsasmuch. Ontheotherhand,the
advantageofour2Smethodoverotherapproachesactuallybecomesmoresignificantasthecapacity
increases,demonstratingthesuperioraccuracyofourapproach.
NurseSchedulingProblem Ourlastexperimentisonthenurseschedulingproblem(NSP)with
unknownpatientsneeds,withthegoalofschedulinganurserostersatisfyingunknownpatientload
demandswhileminimizingmismatchednurse-shiftpreferencesastheobjective. SeeAppendixC.3
foradescriptionoftheapplicationscenario,theMILPformulationsofthetwostages,aswellasthe
associatedpenaltyfunction. GiventhatNSPisnotanLP,IntOpt-Cagaindoesnotapply,andsowe
9

only comparetheproposed2Strainingmethodwiththeclassicalapproaches,usingtheTwo-Stage
Predict+Optimizeframeworkforevaluation. EachNSPinstanceconsistsof15nurses,7days,and3
shiftsperday. ThenursepreferencesareobtainedfromtheNSPLibdataset[26],whichiswidely
usedforNSP[16,20]. Thenumberofpatientsthateachnursecanserveinoneshiftisrandomly
generatedfrom[10,20],representingthefactthateachnursehasdifferentcapabilities. Giventhatwe
areunabletofinddatasetsspecificallyforthepatientloaddemandsandrelevantpredictionfeatures,
wefollowtheexperimentalapproachofDemirovicetal.[4,5,6]anduserealdatafromadifferent
problem(theICONschedulingcompetition)asthenumericalvaluesrequiredforourexperiment
instances. Inthisdataset,theunknownnumberofpatientspershiftispredictedby8features.
Sincetherearefarfewerfeaturesthanthepreviousexperiments,forbothNNand2Sweuseasmaller
networkstructure:a4-layerfully-connectednetworkwith16neuronsperhiddenlayer. Weuse210
instancesfortrainingand90instancesfortesting. Justlikethefirstexperiment,weuse6scalesof
penaltyfactors(seeAppendixC.3forthepenaltyfunction):γ withi.i.d.entriesdrawnuniformly
from[0.25±0.015],[0.5±0.015],[1.0±0.015],[2.0±0.015],[4.0±0.015],and[8.0±0.015].
Table5reportsthemeanpost-hocregretsandstandarddeviationsacross10runsforeachapproach
ontheNSP.Thetableshowsthattheproposed2Smethodagainhasthebestperformanceamong
all the training approaches. Our 2S method obtains at least 7.61%, 15.65%, 17.99%, 20.51%,
46.76%,and62.49%smallerpost-hocregretthanotherclassicalmethodswhenthepenaltyfactoris
[0.25±0.015],[0.5±0.015],[1.0±0.015],[2.0±0.015],[4.0±0.015],and[8.0±0.015]respectively.
RuntimeAnalysis AppendixHgivesthetrainingtimesforeachmethod.Mostclassicalapproaches
arefasterthanour2Smethod,althoughasshowntheirpost-hocregretsaremuchworse. Inalloy
production,theonlysettingwhereIntOpt-Capplies,itsrunningtimeisshorterbutcomparablewith
2S.In0-1knapsack,theonlyproblemwithpublicCombOptNetcode,the2Smethodismuchfaster.
6 LiteratureReview
Section1alreadysummarizedpriorworksinPredict+Optimize,mostofwhichfocusonlearning
unknownsonlyintheobjective. OnlytheHuetal.[12]frameworkconsidersunknownsinconstraints.
Herewesummarizeotherworksrelatedtolearningunknownsinoptimizationproblemconstraints,
particularlythoseoutsideofPredict+Optimize. Theseworkscanbeplacedintotwocategories.
Onecategoryalsoconsiderslearningunknownsinconstraints,butwithverydifferentgoalsandmea-
suresofloss. Forexample,CombOptNet[23]andNandwanietal.[21]focusonlearningparameters
soastomakethepredictedoptimalsolution(first-stagesolutioninourproposedframework)asclose
tothetrueoptimalsolutionx∗ aspossibleinthesolutionspace/metric. Bycontrast,ourproposed
frameworkexplicitlyformulatesthetwo-stageframeworkandpost-hocregretinordertodirectly
capturerewardsandcostsinapplicationscenarios. Experimentson0-1knapsackinSection5show
thattheseothermethodsyieldworsepredictiveperformancewhenevaluatedonthepost-hocregret,
undertheproposedtwo-stageframework.
AnothercategorygiveswaystodifferentiatethroughLPsorLPswithregularizations,asatechnical
component in a gradient-based training algorithm. As mentioned in Section 4, these works can
indeedbeusedinplaceofourproposedapproachinSection4/AppendixB.However,wepointout
that: (i) these other technical tools are essentially orthogonal to our primary contribution, which
isthetwo-stageframework(Section3),and(ii)nonetheless,experimentsonthe0-1knapsackin
AppendixEdemonstratethatourgradientcalculationapproachperformsatleastaswellinpost-hoc
regretperformanceasotherworks,whilebeingfaster.
7 Summary
WeproposedTwo-StagePredict+Optimize:anew,conceptuallysimplerandmorepowerfulframework
forthePredict+Optimizesettingwhereunknownparameterscanappearbothintheobjectiveandin
constraints. Weshowedhowthesimplerperspectiveofferedbytheframeworkallowsustogivea
generaltrainingframeworkforallMILPs,contrastingpriorworkwhichapplyonlytocoveringand
packingLPs. Experimentalresultsdemonstratethatourtrainingmethodofferssignificantlybetter
predictionperformanceoverotherclassicalandstate-of-the-artapproaches.
10

Acknowledgments
We thank the anonymous referees for their constructive comments. In addition, Xinyi Hu and
JimmyH.M.LeeacknowledgethefinancialsupportofaGeneralResearchFund(RGCRef. No.
CUHK14206321)bytheUniversityGrantsCommittee,HongKong. JasperC.H.Leewassupported
inpartbythegenerousfundingofaCroucherFellowshipforPostdoctoralResearch,NSFaward
DMS-2023239,NSFMediumAwardCCF-2107079andNSFAiTFAwardCCF-2006206.
References
[1] A.Agrawal,B.Amos,S.Barratt,S.Boyd,S.Diamond,andJ.Z.Kolter. Differentiableconvex
optimizationlayers. Advancesinneuralinformationprocessingsystems,32,2019.
[2] B.AmosandJ.Z.Kolter. Optnet: Differentiableoptimizationasalayerinneuralnetworks. In
InternationalConferenceonMachineLearning,pages136–145.PMLR,2017.
[3] B. Chen, P. L. Donti, K. Baker, J. Z. Kolter, and M. Bergés. Enforcing policy feasibility
constraintsthroughdifferentiableprojectionforenergyoptimization. InProceedingsofthe
TwelfthACMInternationalConferenceonFutureEnergySystems,pages199–210,2021.
[4] E.Demirovic´,P.J.Stuckey,J.Bailey,J.Chan,C.Leckie,K.Ramamohanarao,andT.Guns.
An investigation into Prediction+Optimisation for the knapsack problem. In International
ConferenceonIntegrationofConstraintProgramming,ArtificialIntelligence,andOperations
Research,pages241–257.Springer,2019.
[5] E.Demirovic´,P.J.Stuckey,J.Bailey,J.Chan,C.Leckie,K.Ramamohanarao,andT.Guns.
Predict+Optimisewithrankingobjectives: Exhaustivelylearninglinearfunctions. Proceedings
oftheTwenty-EighthInternationalJointConferenceonArtificialIntelligence,pages1078–1085,
2019.
[6] E.Demirovic´,P.J.Stuckey,T.Guns,J.Bailey,C.Leckie,K.Ramamohanarao,andJ.Chan.
Dynamic programming for Predict+Optimise. In Proceedings of the Thirty-Fourth AAAI
ConferenceonArtificialIntelligence,pages1444–1451,2020.
[7] A. N. Elmachtoub and P. Grigas. Smart “Predict, then Optimize”. Management Science,
68(1):9–26,2022.
[8] A.N.Elmachtoub,J.C.N.Liang,andR.McNellis. Decisiontreesfordecision-makingunder
thepredict-then-optimizeframework. InProceedingsofthe37thInternationalConferenceon
MachineLearning,pages2858–2867,2020.
[9] J.Friedman,T.Hastie,andR.Tibshirani. Theelementsofstatisticallearning. Springerseries
instatisticsNewYork,2001. Volume1,Number10.
[10] A.U.Guler,E.Demirovic´,J.Chan,J.Bailey,C.Leckie,andP.J.Stuckey. Adivideandconquer
algorithmforPredict+Optimizewithnon-convexproblems. InProceedingsoftheThirty-Sixth
AAAIConferenceonArtificialIntelligence,2022.
[11] GurobiOptimization,LLC. GurobiOptimizerReferenceManual,2023.
[12] X.Hu,J.C.H.Lee,andJ.H.M.Lee. Predict+OptimizeforpackingandcoveringLPswith
unknown parameters in constraints. In Proceedings of the AAAI Conference on Artificial
Intelligence,2022.
[13] X.Hu,J.C.H.Lee,J.H.M.Lee,andA.Z.Zhong.Branch&Learnforrecursivelyanditeratively
solvableproblemsinPredict+Optimize. InAdvancesinNeuralInformationProcessingSystems,
2022.
[14] K.B.KabirandI.Mahmud. Studyoferosion-corrosionofstainlesssteel,brassandaluminum
byopencircuitpotentialmeasurements. JournalofChemicalEngineering,pages13–17,2010.
[15] N.Kahraman,B.Gülenç,andF.Findik. Joiningoftitanium/stainlesssteelbyexplosivewelding
andeffectoninterface. JournalofMaterialsProcessingTechnology,169(2):127–133,2005.
11

[16] B.MaenhoutandM.Vanhoucke. BranchingstrategiesinaBranch-and-Priceapproachfora
multipleobjectivenurseschedulingproblem. Journalofscheduling,13(1):77–93,2010.
[17] J.Mandi,V.Bucarey,M.M.K.Tchomba,andT.Guns. Decision-focusedlearning:Throughthe
lensoflearningtorank. InInternationalConferenceonMachineLearning,pages14935–14947.
PMLR,2022.
[18] J.MandiandT.Guns. InteriorpointsolvingforLP-basedPrediction+Optimisation. Advances
inNeuralInformationProcessingSystems,33:7272–7282,2020.
[19] M.Mulamba,J.Mandi,M.Diligenti,M.Lombardi,V.Bucarey,andT.Guns. Contrastivelosses
andsolutioncachingforPredict-and-Optimize. arXivpreprintarXiv:2011.05354,2020.
[20] R.Muniyan,R.Ramalingam,S.S.Alshamrani,D.Gangodkar,A.Dumka,R.Singh,A.Gehlot,
and M. Rashid. Artificial bee colony algorithm with Nelder–Mead method to solve nurse
schedulingproblem. Mathematics,10(15):2576,2022.
[21] Y.Nandwani,R.Ranjan,P.Singla,etal. Asolver-freeframeworkforscalablelearninginneural
ilparchitectures. AdvancesinNeuralInformationProcessingSystems,35:7972–7986,2022.
[22] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin,
N.Gimelshein,L.Antiga,A.Desmaison,A.Kopf,E.Yang,Z.DeVito,M.Raison,A.Tejani,
S.Chilamkurthy,B.Steiner,L.Fang,J.Bai,andS.Chintala. Pytorch: Animperativestyle,
high-performancedeeplearninglibrary. InAdvancesinNeuralInformationProcessingSystems
32,pages8024–8035.2019.
[23] A.Paulus,M.Rolínek,V.Musil,B.Amos,andG.Martius. Comboptnet: FittherightNP-hard
problembylearningintegerprogrammingconstraints. InInternationalConferenceonMachine
Learning,pages8443–8453.PMLR,2021.
[24] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel,
P.Prettenhofer,R.Weiss,V.Dubourg,J.Vanderplas,A.Passos,D.Cournapeau,M.Brucher,
M.Perrot,andE.Duchesnay. Scikit-learn: MachinelearninginPython. JournalofMachine
LearningResearch,12:2825–2830,2011.
[25] D.E.Rumelhart,G.E.Hinton,andR.J.Williams.Learningrepresentationsbyback-propagating
errors. nature,323(6088):533–536,1986.
[26] M.VanhouckeandB.Maenhout. Nsplib–anurseschedulingproblemlibrary: Atooltoevaluate
(meta-)heuristicprocedures. InOperationalresearchforhealthpolicy:makingbetterdecisions,
proceedingsofthe31stannualmeetingoftheworkinggrouponoperationsresearchappliedto
healthservices,pages151–165,2007.
[27] B.Wilder,B.Dilkina,andM.Tambe. Meldingthedata-decisionspipeline: Decision-focused
learningforcombinatorialoptimization. InProceedingsoftheThirty-ThirdAAAIConference
onArtificialIntelligence,pages1658–1665,2019.
12

A DetaileddiscussionontheTwo-StagePredict+Optimizeframework
A.1 Problemmodellingusingtheframework
As mentioned in Section 3, the proposed Two-Stage Prediction+Optimize framework is phrased
differently from some other two-stage problem formulations. The proposed framework phrases
Stage1solutionsassoftcommitments,andcorrectsStage1solutionswithpenaltyinStage2. On
the other hand, some two-stage frameworks phrase Stage 1 solutions as hard commitments, and
includeexplicitrecoursevariablesinbothstagesofOPtomodelthecorrectioninStage2. Some
optimizationproblemsaremorenaturaltoexpressaccordingtooneperspectivethantheother,while
someproblemsmightbestraightforwardtoexpressineither. Thissectionaimstoshowthatour
framework,whileexplicitlystatedandmotivatedaccordingtothefirstperspective,isinfactgeneral
enoughtoalsoeasilymodelthesecondperspectiveofhardcommitmentsandrecourseactions. In
whatfollows,wefirstdescribedifferenttypesofvariablesandhowourframeworkcancapturethem.
Then,wegivetwoexampleproblemsthatrespectivelyusethesoft/hardcommitmentperspectives,
andwedetailhowtheproblemcanbemodelled.
Softcommitmentvariables: Thesearevariableswhichrepresentdecisionsthatcorrespondtosoft
commitmentsmadeinStage1inanapplication,namelydecisionsthatmaybemodified
oncethetrueparametersarerevealed,butatacostorpenalty. ThediscussioninSection3is
tailoredforthiskindofvariables—simplydefinesuchavariableinStage1anduseafinite
penaltyfunctiontomodelthecostofchangingthissoftcommitmentinStage2.
Hardcommitmentvariables: Thesearevariablesx∗ whichrepresenthardcommitmentsmade
hard
inStage1,meaningthataftercommitment,theyabsolutelycannotchangeinStage2. To
model these variables in our framework, simply write a penalty function that is infinite
wheneverStage1andStage2solutionsforthesevariablesaredifferent. Explicitly,adda
term∞·1[x∗ ̸= x∗ ]. Thisway,noStage2solutionwillchangethesevariables
hard,1 hard,2
fromwhattheywerecommittedtoinStage1.
Recourse/othervariables: Thesearevariableswhichrepresentexplicitactions/decisionstakenonly
inStage2,oncethetrueparametersarerevealed. Thesevariablesarenecessary,forexample,
whenStage1actionsareallhardcommitmentvariables,toensurethatwehaveamechanism
forcorrectiveactionifthehardStage1decisionsareinanyway“incompatible"withthe
revealedparameters. Thesecorrectiveactionsalsotypicallycomeatacost. Thus,tomodel
thesevariables,simplyincludetheminbothStages1and2,andincorporatetheircostinto
theobjectiveoftheoptimizationproblem. Thereshouldalsobe0penaltyformodifying
thesevariablesbetweenthestages.
To summarize, Stage 1 actions can be classified as either soft or hard commitments, depending
onwhethertheycanbechangedinStage2(atafinitepenalty). Stage2actionsareclassifiedas
“recourse"variables,whicharesimplyvariablesthathavenopenaltyfromchangingbetweenStage
1toStage2. Theabovediscussionshowshowourframeworkcapturesallthesepossibilities. We
nowgivetwoexampleapplications:thefirstoneismorenaturallyexpressedviathesoftcommitment
perspective,andthesecondoneismorenaturaltophraseusinghardcommitments+recourse. We
givealsotheirexplicitformulationstodemonstratehowthemodellingisdoneinourframework.
Wefirstshowanexampleproblemwhichisnaturallymodelledusingsoftcommitmentvariables
andpenaltyfunctions. Considertheproduct-stockingprobleminExample1again,whereregular
ordershavetobeplacedtwoweeksaheadofmonthlydeliveries. Weaimtomaximizethenetprofit
bysellingstockedproducts,undertheconstraintthattheavailablestoragespaceislimited. Each
productihasapurchasepricepu(thepriceofpurchasingtheproductfromthewholesalecompany)
i
andasellingpriceps(thepriceofsellingtheproducttocustomers),andneedss spacetobestocked.
i i
Letx denotewhethertheproductiisordered. InStage1,i.e.,twoweeksbeforethedelivery,the
i
availablestoragespaceSpatthetimeofdeliveryisunknown,andweplacetheorderxbasedon
estimatedspace. InStage2,i.e.,thenightbeforethedelivery,thepreciseavailablespaceisrevealed,
andweaskthewholesalecompanytochangetheorderbutneedtopayasurchargeforlast-minute
changes. Assumethesurchargeforthelast-minutechangeintheorderofproductiisc . Inthis
i
example,x isthusasoftcommitmentvariable,andwemodelthesurchargec usingthepenalty
i i
functionoftheframework.
13

Theproposedframeworkcannaturallymodelthisproblem. TheStage1OPcanbeformulatedas:
(cid:88)
x∗ =argmax (ps−pu)x
1 i i i
x
i
s.t. (cid:88) s x ≤Sˆp, x∈{0,1}
i i
i
InStage2,theorderx∗canbechangedwithsurcharges,whichcanbemodelledasapenaltyfunction:
1
(cid:88)
Pen(x∗ →x)= c |x∗−x |
1 i 1 i
i
ThentheStage2OPcanbeformulatedas:
(cid:88) (cid:88)
x∗ =argmax (ps−pu)x − c |x∗−x |
2 i i i i 1 i
x
i i
(cid:88)
s.t. s x ≤Sp, x∈{0,1}
i i
i
Next,wegiveanexampleproblemwhichismorenaturallymodelledusinghardcommitmentvariables
andrecoursevariables. Consideraproduction-planningproblem:acompanyownsasetoffacilities
andprovidesservicestoasetofcustomers. Eachfacilityicanprovideafixedamountofservicesm
i
andhasafixedoperatingcostf inthestandardworkingmode. Thecompanyaimstomeetcustomer
i
demandsdattheminimumoperatingcosts. InStage1,thecompanydecideswhichfacilitiestoopen
for production based on the estimated demands dˆ. This is a binary decision variable x for each
i
facilityi. InStage2,theordersfromcustomersarriveandthedemandsdarerevealed. Iftheservices
providedbytheoperatingfacilitiesinthestandardmodecannotmeetdemands,thecompanywill
asksomefacilitiesthatarealreadyoperating(i.e.x = 1)toworkovertime,butnaturallyneedto
i
payhighovertimefees. Leto denotetheunitovertimefeeforproducingserviceinfacilityi,andσ
i i
denotetheamountofserviceprovidedbyovertimeworkinginfacilityi.
Thisexampleisnaturallymodelledusinghardcommitmentvariablesandrecoursevariables. Which
facilities to operate, x, is a vector of 0/1 hard commitment variables. The amount of service, σ,
providedbytheovertimeworkingmodeofoperatingfacilitiescanbemodeledbyrecoursevariables,
and the recourse costs are the overtime fees o. Using hard commitment variables and recourse
variables,theStage1OPcanbeformulatedas:
(cid:88) (cid:88)
x∗,σ∗ =argmin f x + o σ
1 1 i i i i
x,σ
i i
s.t. (cid:88) (m +σ )x ≥dˆ, x∈{0,1}, σ ≥0
i i i
i
InStage2,weincludeaterm∞·1[x∗ ̸=x]inthepenaltyfunctionpartoftheStage2objectiveto
1
makesurethatxcannotbechanged,whilethepenaltyforchangingσiszerosinceitisarecourse
variable. TheStage2OPisformulatedas:
(cid:88) (cid:88)
x∗,σ∗ =argmin f x + o σ +∞·1[x∗ ̸=x]
2 2 i i i i 1
x,σ
i i
(cid:88)
s.t. (m +σ )x ≥d, x∈{0,1}, σ ≥0
i i i
i
Insummary,wediscussedhowtomodelinourframeworksoftandhardcommitmentactionsinStage
1,aswellasrecourse/otheractionsinStage2. Wegavetwoconcreteexamplestodemonstratehow
suchmodellingcanbedone.
A.2 Whatifcorrection/recourseisnotpossibleintheapplication?
Themotivatingpremiseofthispaperisthattheapplicationscenarioathandallowsforsomepost-
hoccorrectiveactiononcethetrueparametersarerevealed. Onenaturalquestionis:whatifsuch
14

correctiveaction(Stage2actions)isnotactuallypossibleintheapplication? Forexample,inour
runningexampleoftheproduct-stockingproblem,weconsideredawholesalecompanythatallowsfor
orderchangesthenightbefore. Otherwholesalersmaynotallowsuchacorrection/modification. Our
frameworkcanessentiallystillmodelthesescenarios:justsetthepenaltyofmodificationtoinfinity
|                                          | Concretely,usethepenaltyfunction∞·1[x∗ |     | ̸=x∗](or |
| ---------------------------------------- | -------------------------------------- | --- | -------- |
| (oratleast,verylargenumbersforpractice). |                                        |     | 2 1      |
replace∞withaverylargenumber). Thispenaltyfunctionencouragesthelearningalgorithmto
learnconservativepredictionsthatmaximizethechancesofyieldingStage1decisionsthatremain
feasibleinStage2.
Toshowthis,werananotherquickexperiment,usingthe0-1knapsackproblemsettinginthepaper
(with knapsack capacity = 100). This time, as we varied the magnitude of the penalty function,
wemeasureattesttimetheempiricalfractionofStage1solutionsthatremainfeasibleunderthe
trueparameters. TheresultsinTable6demonstrateourclaimthatasthepenaltytermincreases,
thepredictionsgetmoreandmorelikelytoremainfeasible,makingitareasonablewaytotraina
predictorevenwhenStage2correctionmechanismsdonotactuallyexistintheapplication.
Table6: MeanandstandarddeviationofempiricalfractionofStage1solutionsthatremainfeasible
inStage2,forthe0-1knapsackproblemwhencapacityis100usingtheTwo-StagePredict+Optimize
framework.
|     | PenaltyFactor | Feasibility% |     |
| --- | ------------- | ------------ | --- |
|     | 0.05          | 0.00%±0.00%  |     |
|     | 0.25          | 0.00%±0.00%  |     |
|     | 0.5           | 1.73%±0.52%  |     |
|     | 1             | 50.93%±1.92% |     |
|     | 2             | 51.63%±1.22% |     |
|     | 4             | 99.07%±0.31% |     |
A.3 Two-StagePredict+OptimizevsPriorHuetal.Framework
AsmentionedearlierinSection3,Two-StagePredict+Optimizeistechnicallymathematicallyequiva-
lenttothepriorframeworkofHuetal.[12],inthesenseofexpressiveness,ignoringdifferentiability
issues. Ontheonehand,wecanregardtheStage2optimizationasaformofcorrectionfunction,
andhenceTwo-StagePredict+OptimizecanbeconsideredasaspecialcaseoftheHuetal.[12]
framework. On the other hand, given a correction function as in the Hu et al. [12] framework,
we can simply modify the penalty function such that we keep the penalty value of the corrected
solution,andmakethepenaltyvalueinfiniteforallotherpotentialStage2solutions. Thisforces
theStage2optimizationtoalwaysemulatethecorrectionfunction. Inthissense,ourTwo-Stage
Predict+OptimizeframeworkcanalsoemulatetheHuetal.[12]framework,meaningthatthetwo
frameworksaretechnicallyequivalent.
Nevertheless,theTwo-StagePredict+Optimizeframeworkisbothconceptuallysimplerandeasier
toapply. Inthemainpaper,weshowedhowtoperformend-to-endneuralnetworktrainingwithin
thisnewframeworkwheneverbothstagesofoptimizationcanbephrasedasMILPs,andalsogive
empiricalexperimentalresults. Together,theydemonstratethemuchmoregeneralapplicabilityof
theTwo-StagePredict+Optimizeframework.
We end this appendix with the statement and short proof that, conditioned on the same penalty
functionandpredictionmodel,Two-StagePredict+Optimizealwaysoutputsatleastasgoodafinal
solutionasthepriorframeworkusinganycorrectionfunction.
PropositionA.1. ConsideranarbitraryminimizationPara-OPP,penaltyfunctionPen,correction
functionx∗ ,estimatedparametersθˆandtrueparametersθ. Letx∗(θˆ)andx∗(θˆ)bothdenotethe
corr
1
estimatedsolutionfromtheestimatedparametersθˆ,x∗(θˆ,θ)betheoutputfinalsolutionfromthe
2
Two-StagePredict+Optimizeframework,andx∗ (θˆ,θ)betheoutputcorrectedsolutionfromthe
corr
| priorframeworkofHuetal. | Then, |     |     |
| ----------------------- | ----- | --- | --- |
obj(x∗(θˆ,θ),θ)+Pen(x∗(θˆ)→x∗(θˆ,θ))≤obj(x∗ (θˆ,θ),θ)+Pen(x∗(θˆ)→x∗ (θˆ,θ))
| 2   | 1 2 | corr | corr |
| --- | --- | ---- | ---- |
Proof. ObservethatbothsidesoftheinequalityaretheobjectiveoftheStage2optimizationproblem,
evaluatedatx∗andx∗ respectively. Sincex∗istheoptimalsolutiontotheminimizationproblem,
| 2 corr | 2   |     |     |
| ------ | --- | --- | --- |
theinequalityfollowsdirectly.
15

B GradientCalculationsforProblem(5)
|               | ∂x∗ | InthecontextoftheMILP,theunknownparameterθˆmayeitherbec,A,b,G, |     |     |     |     |     |     |     |
| ------------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Approximating | 1.  |                                                                |     |     |     |     |     |     |     |
∂θˆ
or h. Using the solution x and the barrier weight µ returned from solving Problem (5), we can
∂x∗
compute the relevant derivatives of 1. The case of c has already been derived by Mandi and
∂cˆ
Guns[18](seeAppendixA.1andA.2intheirpaper). Problem(5)canberewrittenas:
d+q
(cid:88)
|     |     |     | x∗ =argminc′⊤x′−µ |     |     | ln(x′) |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | ------ | --- | --- | --- |
i
|     |     |     |     | x′  |     |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1
|     |     |     | s.t. | A′x′ =b′ |     |     |     |     |     |
| --- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- |
where
|     |     |     | c′ =[c   | 0]∈Rd+q  |               |     |     |     |     |
| --- | --- | --- | -------- | -------- | ------------- | --- | --- | --- | --- |
|     |     |     | x′ =[x   | s]∈Rd+q  |               |     |     |     |     |
|     |     |     | (cid:20) | (cid:21) |               |     |     |     |     |
|     |     |     |          | A 0      |               |     |     |     |     |
|     |     |     | A′ =     |          | ∈R(p+q)×(d+q) |     |     |     |     |
|     |     |     |          | G −I     |               |     |     |     |     |
(cid:20) (cid:21)
b ∈Rp+q
b′ =
h
FactB.1. ConsidertheLPrelaxation(6),definingx′asafunctionofc′,A′andb′. Then,according
toMandiandGuns[18],underthisdefinitionofx∗,
|     |     |       |     |   | ∂x′ |    |    |    |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | −X′−1T | A′⊤ | −c′ |     |     | τI  |     |     |
∂c′
|     |     |    | A′  | 0 −b′  | ∂y′ | = | 0   |    |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
′
|     |     | −c′⊤ | b′⊤ | κ   | ∂ ∂ | c τ | x⊤  |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     |      |     | τ   | ∂c′ |     |     |     |     |
whereX′ =diag(x′),t=µX′−1e,T =diag(t),y′isthelagrangianmultiplierofProblem(6),and
κandτ areadditionalvariablesaddedbyMandiandGuns[18]torepresentthedualitygap. The
∂x∗
| gradient | 1 canbeobtainedbysolvingthissystemofequalities. |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
∂cˆ
| Definethenotationf(x,c,G,h)=c⊤x−µ |     |     |     | (cid:80)d |            | (cid:80)q | ln(G⊤x−h |                   |     |
| --------------------------------- | --- | --- | --- | --------- | ---------- | --------- | -------- | ----------------- | --- |
|                                   |     |     |     |           | ln(x i )−µ |           |          | i ). Then,Problem |     |
|                                   |     |     |     | i=1       |            |           | i=1      | i                 |     |
(5)canbeexpressedasfinding:
|     |     | x∗  | =argminf(x,c,G,h) |     |     | s.t. Ax=b |     |     | (7) |
| --- | --- | --- | ----------------- | --- | --- | --------- | --- | --- | --- |
x
|     |     |     |     |     |     |     |     | ∂x∗,∂x∗,∂x∗ | ∂x∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
Usingthisnotation,wewritedownthefollowingfourlemmasoncomputing ,and
|     |     |     |     |     |     |     |     | ∂G ∂h ∂A | ∂b  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
approximately.
LemmaB.2. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
|     |     | =(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f |     |     |     |     | (x,c,G,h) |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --------- | --- | --- |
|     | ∂G  |                             |     |     |     |     | Gx        |     |     |
whereH = f xx (x,c,G,h)denotesthematrixofsecondderivativesoff withrespecttodifferent
coordinatesofx,andsimilarlyforothersubscripts,andexplicitly:
|     |      |            | (cid:26) µx−2+µ | (cid:80)q   | G2     | /(G⊤x−h |       | )2,     |     |
| --- | ---- | ---------- | --------------- | ----------- | ------ | ------- | ----- | ------- | --- |
|     |      |            |                 |             |        |         |       | i j =k  |     |
|     | f    | (x,c,G,h)= |                 | j (cid:80)q | i= 1 i | j i     |       |         | (8) |
|     | xkxj |            |                 | µ G         | G /    | ( G⊤x   | −h )2 | , j ̸=k |     |
|     |      |            |                 | i=1 ij      | ik     | i       | i     |         |     |
and
(cid:26)
|     |     |            | µG  | x /(G⊤x−h | )2−µ/(G⊤x−h |     |     | ) r =j |     |
| --- | --- | ---------- | --- | --------- | ----------- | --- | --- | ------ | --- |
|     | f   | (x,c,G,h)= |     | ℓj j ℓ    | ℓ           |     | ℓ   | ℓ      |     |
Gℓrxj
|     |     |     | µG  | x /(G⊤x−h | )2  |     |     | r ̸=j |     |
| --- | --- | --- | --- | --------- | --- | --- | --- | ----- | --- |
|     |     |     |     | ℓj r ℓ    | ℓ   |     |     |       |     |
Notethatwhentherearenoequalityconstraints,i.e.,A=0,wehave
∂x∗
|     |     |     |     | =−H−1f | (x,c,G,h) |     |     |     |     |
| --- | --- | --- | --- | ------ | --------- | --- | --- | --- | --- |
|     |     |     | ∂G  | Gx     |           |     |     |     |     |
whichisthesameastheLemma3in[12].
16

Proof. UsingtheLagrangianmultipliery,theLagrangianrelaxationofProblem(7)canbewrittenas
|     |     | L(x,y;c,G,h)=f(x,c,G,h)+y⊤(b−Ax) |     |     |     |     |     |     |     | (9) |
| --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| x∗  |     |                                  |     |     |     |     |     | x∗  |     |     |
Since = argmin f(x,c,G,h) s.t. Ax = b is an optimum, must obey the Karush-Kuhn-
x
Tucker(KKT)conditions,obtainedbysettingthepartialderivativeofEquation(9)withrespectto
xandyto0. Letf (x,c,G,h)denotesthevectoroffirstderivativesoff withrespecttodifferent
x
coordinatesofx,f (x,c,G,h)denotesthematrixofsecondderivativesoff withrespecttodifferent
xx
coordinatesofx,weobtain:
(x,c,G,h)−A⊤y
|     |     |     |     | f x |     |     | =0  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(10)
Ax−b=0
TheimplicitdifferentiationoftheseKKTconditionswithrespecttoGallowsustogetthefollowing
systemofequalities:
|     | (cid:20) |           |     | (cid:21) (cid:20) |           |     |     | (cid:21)(cid:20) | (cid:21) |      |
| --- | -------- | --------- | --- | ----------------- | --------- | --- | --- | ---------------- | -------- | ---- |
|     | f        | (x,c,G,h) |     | f                 | (x,c,G,h) |     | −A⊤ |                  | ∂x       |      |
|     | Gx       |           |     | +                 | xx        |     |     |                  | ∂G =0    | (11) |
|     |          | 0         |     |                   |           |     |     |                  | ∂y       |      |
|     |          |           |     |                   | A         |     | 0   |                  |          |      |
∂G
Bysolvingthissystemofequalities,wecanobtain
∂x∗
=(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f
Gx (x,c,G,h)
∂G
| Sincef(x,c,G,h)=c⊤x−µ |     |     | (cid:80)d | ln(x )−µ | (cid:80)q | ln(G⊤x−h |     | ),wehave |     |     |
| --------------------- | --- | --- | --------- | -------- | --------- | -------- | --- | -------- | --- | --- |
|                       |     |     | i=1       | i        |           | i=1      | i   | i        |     |     |
(cid:80)q
|     | f (x,c,G,h)=c |     | −µx−1−µ  |             |          | G         | /(G⊤x−h |     | )      |      |
| --- | ------------- | --- | -------- | ----------- | -------- | --------- | ------- | --- | ------ | ---- |
|     | xj            |     | j        | j           |          | i =1 i j  | i       | i   |        |      |
|     |               |     | (cid:26) | −2+µ        | (cid:80) | q 2       | ⊤x−h    |     | )2,    |      |
|     |               |     |          | µx          |          | G         | /(G     |     | i j =k | (12) |
|     | f (x,c,G,h)=  |     |          | j (cid:80)q |          | i=1 ij    | i       |     |        |      |
|     | xkxj          |     |          | µ           | G        | G /(G⊤x−h |         | )2, | j ̸=k  |      |
|     |               |     |          |             | i=1      | ij ik     | i       | i   |        |      |
and
|     |     |     | (cid:26) | µG x | /(G⊤x−h | )2−µ/(G⊤x−h |     |     | ) r =j |     |
| --- | --- | --- | -------- | ---- | ------- | ----------- | --- | --- | ------ | --- |
|     |     |     |          | ℓj j | ℓ       | ℓ           |     | ℓ   | ℓ      |     |
f Gℓrxj (x,c,G,h)=
|     |     |     |     | µG x | /(G⊤x−h | )2  |     |     | r ̸=j |     |
| --- | --- | --- | --- | ---- | ------- | --- | --- | --- | ----- | --- |
|     |     |     |     | ℓj r | ℓ       | ℓ   |     |     |       |     |
LemmaB.3. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
|           |                          | =(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f |     |     |     |     |     | (x,c,G,h) |     |     |
| --------- | ------------------------ | --------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- |
|           | ∂h                       |                             |     |     |     |     |     | hx        |     |     |
| whereH =f | isdefinedasinLemmaB.2and |                             |     |     |     |     |     |           |     |     |
xx
|     |     | f   | (x,c,G,h)=−µG |     |     | /(G⊤x−h |     | )2  |     |     |
| --- | --- | --- | ------------- | --- | --- | ------- | --- | --- | --- | --- |
|     |     |     | hℓxj          |     |     | ℓj      | ℓ   | ℓ   |     |     |
Notethatwhentherearenoequalityconstraints,i.e.,A=0,wehave
∂x∗
|     |     |     |     | =−H−1f |     | (x,c,G,h) |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --------- | --- | --- | --- | --- |
hx
∂h
whichisthesameastheLemma2in[12].
Proof. AsstatedintheproofofLemmaB.2,usingtheLagrangianrelaxationandtheKarush-Kuhn-
Tucker(KKT)conditions,weobtain:
|     |     |     |     | f (x,c,G,h)−A⊤y |     |     | =0  |     |     |      |
| --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     | x               |     |     |     |     |     | (13) |
Ax−b=0
TheimplicitdifferentiationoftheseKKTconditionswithrespecttohallowsustogetthefollowing
systemofequalities:
|     | (cid:20) |           |     | (cid:21) (cid:20) |           |     | −A⊤ | (cid:21)(cid:20) | ∂x (cid:21) |      |
| --- | -------- | --------- | --- | ----------------- | --------- | --- | --- | ---------------- | ----------- | ---- |
|     | f hx     | (x,c,G,h) |     | f                 | (x,c,G,h) |     |     |                  |             |      |
|     |          |           |     | +                 | xx        |     |     |                  | ∂h =0       | (14) |
|     |          | 0         |     |                   | A         |     | 0   |                  | ∂y          |      |
∂h
Bysolvingthissystemofequalities,wecanobtain
∂x∗
|     |     | =(H−1A⊤(AH−1A⊤)−1AH−1−H−1)f |     |     |     |     |     | (x,c,G,h) |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     | ∂h  |                             |     |     |     |     |     | hx        |     |     |
17

(cid:80)d
where H = f is defined as in Lemma B.2. Since f(x,c,G,h) = c⊤x − µ ln(x ) −
|     |                | xx           |     |      |         |     |         |     |     | i=1 | i   |
| --- | -------------- | ------------ | --- | ---- | ------- | --- | ------- | --- | --- | --- | --- |
| µ   | (cid:80)q ln(G | x−h ),wehave |     |      |         |     |         |     |     |     |     |
|     | i=1 i          | i            |     |      |         |     |         |     |     |     |     |
|     |                |              |     | f    | (x)=−µG |     | /(G⊤x−h | )2  |     |     |     |
|     |                |              |     | hℓxj |         | ℓj  | ℓ       | ℓ   |     |     |     |
LemmaB.4. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
|     |     |     | =H−1(−A⊤(AH−1A⊤)−1(I |     |     |     | x+AH−1I |     | y)+I y) |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     | ∂A  |                      |     |     |     | 2       |     | 1 1     |     |     |
ij
| whereI | =−∂A⊤,I |      | = ∂A | ,andH | =f  | isdefinedasinLemmaB.2. |     |     |     |     |     |
| ------ | ------- | ---- | ---- | ----- | --- | ---------------------- | --- | --- | --- | --- | --- |
|        | 1       |      | 2    |       | xx  |                        |     |     |     |     |     |
|        |         | ∂Aij | ∂Aij |       |     |                        |     |     |     |     |     |
Proof. AsstatedintheproofofLemmaB.2,usingtheLagrangianrelaxationandtheKarush-Kuhn-
Tucker(KKT)conditions,weobtain:
|     |     |     |     |     | f (x,c,G,h)−A⊤y |     |     | =0  |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
x
(15)
Ax−b=0
|                          | A ∈ Rp×d, |          | i ∈   | {1,...,p},j                                     | ∈ {1,...,d}, |     |     |                  |                 |          |      |
| ------------------------ | --------- | -------- | ----- | ----------------------------------------------- | ------------ | --- | --- | ---------------- | --------------- | -------- | ---- |
| Since                    |           | fix      |       |                                                 |              |     | the | implicit         | differentiation | of these | KKT  |
| conditionswithrespecttoA |           |          |       | ij allowsustogetthefollowingsystemofequalities: |              |     |     |                  |                 |          |      |
|                          |           | (cid:34) | −∂A⊤y | (cid:35)                                        | (cid:20)     |     |     | (cid:21)(cid:34) | ∂x (cid:35)     |          |      |
|                          |           |          |       |                                                 | f (x,c,G,h)  |     | −A⊤ |                  |                 |          |      |
|                          |           |          | ∂Aij  | +                                               | xx           |     |     |                  | ∂Aij =0         |          | (16) |
|                          |           |          | ∂A    |                                                 |              | A   | 0   |                  | ∂y              |          |      |
x
|      |         |     | ∂Aij |                                               |     |     |     |     | ∂Aij |     |     |
| ---- | ------- | --- | ---- | --------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- |
|      | =−∂A⊤,I |     | ∂A   |                                               |     |     |     |     |      |     |     |
| LetI | 1       | 2 = |      | . Bysolvingthissystemofequalities,wecanobtain |     |     |     |     |      |     |     |
|      | ∂Aij    |     | ∂Aij |                                               |     |     |     |     |      |     |     |
∂x∗
|     |     |     | =H−1(−A⊤(AH−1A⊤)−1(I |     |     |     | x+AH−1I |     | y)+I y) |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     | ∂A  |                      |     |     |     | 2       |     | 1 1     |     |     |
ij
| whereH | =f  | isdefinedasinLemmaB.2. |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
xx
LemmaB.5. ConsidertheLPrelaxation(7),definingx∗ asafunctionofc,A,b,Gandh. Then,
underthisdefinitionofx∗,
∂x∗
=H−1A⊤(AH−1A⊤)−1I
∂b
| whereH | =f xx | isdefinedasinLemmaB.2. |     |     |     |     |     |     |     |     |     |
| ------ | ----- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proof. AsstatedintheproofofLemmaB.2,usingtheLagrangianrelaxationandtheKarush-Kuhn-
Tucker(KKT)conditions,weobtain:
|     |     |     |     |     | f (x,c,G,h)−A⊤y |     |     | =0  |     |     |      |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | x               |     |     |     |     |     | (17) |
Ax−b=0
TheimplicitdifferentiationoftheseKKTconditionswithrespecttoballowsustogetthefollowing
systemofequalities:
|     |     |     | (cid:20) | (cid:21) | (cid:20)    |     |     | (cid:21)(cid:20) | (cid:21) |     |      |
| --- | --- | --- | -------- | -------- | ----------- | --- | --- | ---------------- | -------- | --- | ---- |
|     |     |     | 0        |          | f (x,c,G,h) |     | −A⊤ |                  | ∂x       |     |      |
|     |     |     |          | +        | xx          |     |     |                  | ∂b =0    |     | (18) |
|     |     |     | −I       |          | A           |     | 0   |                  | ∂y       |     |      |
∂b
Bysolvingthissystemofequalities,wecanobtain
∂x∗
=H−1A⊤(AH−1A⊤)−1I
∂b
| whereH | =f  | isdefinedasinLemmaB.2. |     |     |     |     |     |     |     |     |     |
| ------ | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
xx
18

C DetailsforCaseStudies
|     |     |     |     |     |     |     |                     |     | (cid:12)            | (cid:12) |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------------- | -------- | --- |
|     |     |     |     |     |     |     | ∂PReg(θˆ,θ)(cid:12) |     | ∂PReg(θˆ,θ)(cid:12) |          | ∂x∗ |
Sincethepenaltyfunctionpartlyorsolelyaffectstheterms , ,and 2,
|     |     |     |     |     |     |     | ∂x∗ |     | (cid:12) | ∂x∗ (cid:12) | ∂x∗ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- |
|     |     |     |     |     |     |     |     | 2   | x∗       | 1 x∗         | 1   |
wegivethreecasestudiesforourframeworktoshowhowtodesignthepenaltyfunctionandcompute 1 2
gradientsusingthecorrespondingpenaltyfunction.
C.1 AlloyProductionProblem
Wefirstdemonstrate,usingtheexampleofthealloyproductionproblem,howourframeworkcan
tackle problems solvable by the prior work of Hu et al. [12]. An alloy production factory needs
to produce a certain amount of a particular alloy, requiring a mixture of M kinds of metals. To
| thatend,itmustacquireatleastreq |     |     |     | tonsofeachofthem |     |     | ∈   | [M]metals. |                    |     |     |
| ------------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | ---------- | ------------------ | --- | --- |
|                                 |     |     |     | m                |     |     |     |            | Therawmaterialsare |     |     |
tobeobtainedfromK suppliers,eachsupplyingadifferenttypeofore. Thefactoryplanstobuy
oresfromsitesandthenextractthemetalsthemselves. Theoresuppliedbysitek ∈[K]containsa
con ∈[0,1]fractionofmaterialmatapriceofcost perton. Thegoalofthefactoryistomeet
| km  |     |     |     |     |     | k   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itsrequirementsforeachmetalattheminimumcost. However, theprecisemetalconcentrations
(averagedinabatch)areunknownbeforethefactoryactuallycompletesmetalextraction. Thefactory
willestimatemetalconcentrationsbasedonhistoricalbuyingrecords,consideringfeaturessuchas
theoretype,oreorigin,site-reportedpreliminarysamplesandsoon. Thenthefactorywilldecide
howmuchoretoorderfromeachsite. ThisistheStage1solution. TheStage1OPisthealloy
productionproblemusingtheestimatedmetalconcentrationscoˆn,andcanbeformulatedasfollows:
|     |     | x∗  | =argmincost⊤x |     |     | s.t. coˆn⊤x≥req, |     | x≥0 |     |     |     |
| --- | --- | --- | ------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
1
x
Afterthefactoryobtainstheoresandcompletesmetalextraction,i.e.,inStage2,theprecisemetal
concentrations/amounts are known. Since the purchased ores are already processed, the factory
cannotreturnoresevenifithasboughttoomuch. However,iftheobtainedmetalsdonotsatisfy
therequirements,thefactorycanpost-hocdecidetolast-minuteordermoreoresatahigherprice,
forexample,(1+σ )cost pertonfromthesitek,whereσ ≥0isanon-negativetunablescalar
|            |                                      | k   | k      |                     |     |     | k   |     |     |     |      |
| ---------- | ------------------------------------ | --- | ------ | ------------------- | --- | --- | --- | --- | --- | --- | ---- |
| parameter. | Inthisscenario,thepenaltyfunctionis: |     |        |                     |     |     |     |     |     |     |      |
|            |                                      |     | Pen(x∗ | →x)=(σ◦cost)⊤(x−x∗) |     |     |     |     |     |     |      |
|            |                                      |     |        | 1                   |     |     |     | 1   |     |     | (19) |
where◦istheHadamard/entrywiseproduct.
Withrespecttotheabovepenaltyfunction,wearenowreadytodefinetheStage2OP:
|     | x∗ =argmincost⊤x+(σ◦cost)⊤(x−x∗) |     |     |     |     |     |      | con⊤x≥req, |     | x≥x∗ |      |
| --- | -------------------------------- | --- | --- | --- | --- | --- | ---- | ---------- | --- | ---- | ---- |
|     |                                  |     |     |     |     |     | s.t. |            |     |      | (20) |
|     | 2                                |     |     |     |     | 1   |      |            |     | 1    |      |
x
Notethatsincetheprecisemetalconcentrationsconarerevealed,thetrueconcentrationsareusedas
theproblemparametersinsteadoftheestimatedconcentrations. Thefinalamountoforesbought
fromeachsite,includingtheoresboughtinbothStage1andStage2,istheStage2solution.
The above formulation is based on the “soft commitment" modelling approach discussed in Ap-
pendixA.1.
Thepost-hocregretforthealloyproductionproblemcanbeexplicitlywrittenas:
|     | PReg(θˆ,θ)=cost⊤x∗+(σ◦cost)⊤(x∗−x∗)−cost⊤x∗(con) |     |     |     |     |     |     |     |     |     | (21) |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |                                                  |     |     | 2   |     |     | 2 1 |     |     |     |      |
wherex∗(con)isanoptimalsolutionofthealloyproductionproblemunderthetrueconcentrations
con. WenowshowhowtocomputetherelevantgradientsasdiscussedinSection4andAppendixB.
|     |     |     |     |     |     |     |     |     |     | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | -------- |
UsingEquation(21),itisstraightforwardtocomputethatthei-thiteminvector and
|     |     |     |     |     |     |     |     |     |     | ∂x∗ | (cid:12) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
2 x∗
|                     |     |                     |     | (cid:18) |                     | (cid:19) |        |       | (cid:18) |                     | (cid:19)1 |
| ------------------- | --- | ------------------- | --- | -------- | ------------------- | -------- | ------ | ----- | -------- | ------------------- | --------- |
|                     |     | ∂PReg(θˆ,θ)(cid:12) |     | (cid:12) | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |        |       |          | ∂PReg(θˆ,θ)(cid:12) | (cid:12)  |
| thei-thiteminvector |     |                     |     | :        |                     |          | = (1+σ | )cost | ,        |                     | =         |
|                     |     |                     | ∂x∗ | (cid:12) | ∂x∗                 | (cid:12) |        | i     | i        | ∂x∗                 | (cid:12)  |
|                     |     |                     | 1   | x∗       | 2                   | x∗       |        |       |          | 1                   | x∗        |
|                     |     |                     |     | 2        |                     | 1        | i      |       |          |                     | 2 i       |
−σ i cost i .
∂x∗
| Nowweshowhowtocomputetheapproximationoftheremainingterm, |     |     |     |     |     |     |     |     | 2.  |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂x∗
1
19

Approximation
∂x∗
2. We use the same interior-point LP solver to help compute the relevant
∂x∗
1
derivatives. First, theestimatedparametersarefedintotheLPsolvertosolvetheStage1OPto
obtaintheStage1optimalsolutionx∗andthecorrespondingµ,whichareusedtocomputetheterm
1
∂x∗ 1. ThentheStage1optimalsolutionx∗andthetrueparametersarefedintotheLPsolvertosolve
∂θˆ 1
theStage2OPtoobtaintheStage2optimalsolutionx∗andthecorrespondingµ,whichareusedto
2
computetheterm
∂x∗
2. ConsidertheStage2OPinprogram(20). ItisclearthattheStage2OPisa
∂x∗
MILP,withx∗inthe 1 objectiveandx∗inhoftheconstraints. ApplyingLemmaB.3,wecancompute
2 1
anapproximategradientofthe
∂x∗
2 term.
∂x∗
1
C.2 Variantof0-1Knapsack
Thesecondexample,whichwecalltheproxybuyerproblem,isavariantofthe0-1knapsackproblem.
Theunknownparametersappearinboththeobjectiveandconstraints. Thisproblem,asweshallsee,
canbehandledbyourframework,butnotbythepriorapproachbyHuetal.[12],sincetheproblem
isinherentlydiscreteandcannotbeformulatedasLPs.
Aproxybuyerisapersonwhopurchasesgoodsforotherspossiblyforaprofit. Consideraproxy
buyerwhoisfromCityA,withaveryhighcostofliving,whoregularlytravelstoCityBwithamuch
lowercostofliving. Givenherregulartravels,herfriendsinCityAhaveaskedhertohelppurchase
everyday-lifeproducts,whicharesignificantlycheaperinCityB,yetthetimeandtransportation
cost from City A to City B makes it prohibitive for most people to just go to City B themselves.
ThetravellercommutesbetweenCityAandCityBonceeverythreemonths,andhasaknownand
limitedcapacitycapofgoodsshecouldcarryandbringback. Beforeeachtrip,herfriendswould
makerequestsforthingstobuy. Forsimplicity,onerequestcontainsoneitem. Ifthebuyerbrings
back the item as requested, her friends will pay her 20% of the price-tag p of each item i as a
i
courtesy-thankyou. Wedenotethis“profit”byf ,i.e.,f =20%p .
i i i
Thebuyerispopular, andmanyfriendsaskherforfavours. Onedaybeforethebuyerleavesfor
CityB,thebuyerneedstodecidewhichofherfriends’requeststoaccept,giventhelimitedcapacity,
andinformthemaccordingly. Thebuyerwantstomaximizethetotalamountofcourtesy-thankyou
moneyshegets,subjecttothehardconstraintofthelimitedsuitcasecapacitycap. However,the
precisepricep ofeachitemiisunknown,duetotheuncertaintyofthepriceitself,thevolatilityof
i
theexchangerate,andtheuncertaintyofthediscountactivitiesoftheitems. Thus,the“profit”f of
i
buyingitemiisunknown. Inaddition,theexactsizes ofeachitemiisalsoestimated. Thebuyer
i
willestimatetheprofit,i.e.,theprices,andthesizesbasedonpastexperiences,consideringfeatures
suchastime-of-year,holiday-or-not,brandandsoon. Thebuyerwilldecidewhichrequeststoaccept
basedontheestimation. ThisistheStage1solution. TheStage1OPistheproxybuyerproblem
usingtheestimatedsizessˆandestimatedprofitsfˆ:
x∗ =argmaxfˆ⊤x, s.t. sˆ⊤x≤cap, x∈{0,1}
1
x
AfterthebuyerarrivesatCityB,thebuyerknowstheprecisepriceandsizeofeachitem. Ifshe
cannotcarryalltheacceptedrequests,forexample,ifthepackagingforcertainitemshavechanged
sinceshelastboughtthem,thebuyerwillnecessarilyneedtodropsomeoftheserequests. Thebuyer
usuallyfeelsbadaboutrenegingonapromisetoherfriends,andtreatsherfriendstoamealasan
apologyiftherequestcannotbefulfilledaftershepromised. Forsimplicity,weassumethattheprice
oftheapology-mealislinearintheprofitofthedroppedrequest,sincemoreexpensiveitemsare
considered“moreimportant”requests. Here,thelinearityfactorisindependentoftherequest. That
is,ifshedropsitemi,shehastospendσf amountofmoney,whereσ ≥0isanon-negativetunable
i
scalarparameter. Inthisscenario,thepenaltyfunctionis:
Pen(x∗ →x)=σf⊤(x∗−x) (22)
1 1
WearenowreadytodefinetheStage2OPwithrespecttotheabovepenaltyfunction:
x∗ =argmaxf⊤x−σf⊤(x∗−x), s.t. s⊤x≤cap, x≤x∗, x∈{0,1} (23)
2 1 1
x
Therequeststhatwerefinallyfilled,namelytheitemsthatwereactuallyboughtbythebuyerand
broughthometoCityA,formstheStage2solution.
20

Thenthesimplifiedformofthepost-hocregretfortheproxybuyerproblemcanbewrittenas:
PReg(θˆ,θ)=f⊤x∗(f,s)−f⊤x∗+σf⊤(x∗−x∗)
(24)
|     |     |     |     |     |     | 2   | 1 2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wherex∗(f,s)isanoptimalsolutionoftheproxybuyerproblemunderthetrueproxyfeesf
and
truesizess.
(cid:12)
UsingEquation(24),itisstraightforwardtocomputethatthei-thiteminvector ∂PReg(θˆ,θ)(cid:12) and
|                     |                     |     |          |                     |          |          |                     |     | ∂x∗ (cid:12) |
| ------------------- | ------------------- | --- | -------- | ------------------- | -------- | -------- | ------------------- | --- | ------------ |
|                     |                     |     |          |                     |          |          |                     |     | 2 x∗         |
|                     |                     |     | (cid:18) |                     |          | (cid:19) | (cid:18)            |     | (cid:19) 1   |
|                     | ∂PReg(θˆ,θ)(cid:12) |     | (cid:12) | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |          | ∂PReg(θˆ,θ)(cid:12) |     | (cid:12)     |
| thei-thiteminvector |                     |     | :        |                     |          | =(−1−σ)f | ,                   |     | =σf .        |
|                     |                     | ∂x∗ | (cid:12) | ∂x∗                 | (cid:12) |          | i                   | ∂x∗ | (cid:12) i   |
|                     |                     | 1   | x∗       |                     | 2 x∗     |          |                     | 1   | x∗           |
|                     |                     |     | 2        |                     |          | 1 i      |                     |     | 2 i          |
∂x∗
Approximation 2. SimilartothecomputationinSectionC.1,weobtaintheStage1optimal
∂x∗
1
solutionx∗, theSta ge2optimalsolutionx∗, andthecorrespondingµfromtheinterior-pointLP
1 2
∂x∗
computetheterm 2. ConsidertheStage2OPinprogram(23),itisclearthattheStage2OPisa
∂x∗
MILP,withx∗inthe 1 objectiveandx∗inhoftheconstraints. ApplyingLemmaB.3,wecancompute
| 2   |     |     | 1   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∂x∗
| anapproximategradientofthe |     |     | 2 term. |     |     |     |     |     |     |
| -------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
∂x∗
1
C.3 NurseSchedulingProblem
Ourlastexampleisthenurseschedulingproblem(NSP),whichcanbehandledbyourframework
butnotbythepriorworkofHuetal.[12]sinceitisneitherapackingLPnoracoveringLP.
Consider a large optometry center that needs to assign nurses to shifts per day to meet patients’
needs. Every Monday morning, the center collects the nurses’ preferences for each shift of the
followingweek. Sincenursesmayhavetheirownactivitiesanderrandsduringunscheduledshifts,
theywanttobeinformedoftheirschedulesasearlyaspossible. Afterthepreferencesarecollected,
onMondaynight,thecentersetsapreliminaryshiftschedulefortheupcomingweekbasedonthe
estimatednumberofpatientsforeachshift. Supposetherearennurses,kdays,andsshiftsperday,
thenthenumberofthetotalshiftsist=k×s. WeformulatethedecisionvariablesasaBoolean
vectorx∈{0,1}d,whered=n×k×s. ∈{1,2,3,4}drepresentthevalueofeachnurse’s
LetP
Nt
preferences for a particular shift (the higher the number the better), and H ∈ represents the
numberofpatientsineachshift, whichareunknownandneedtobepredicted. Eachnurseican
servem patientsinoneshift. Theobjectiveistomaximizethenurses’preferencesunderasetof
i
constraints: (1)theschedulemustsatisfythepatientdemand,undereachshift(2)eachnursemustbe
scheduledforexactlyoneshifteachday(3)nonursemaybescheduledtoworkanightshiftfollowed
immediatelybyamorningshift. TheStage1OPistheNSPusingtheestimatednumberofpatients
Hˆ:
x∗ =argmaxP⊤x
1
x
n−1 (cid:88)
≥Hˆ
|     | s.t. |     | m i x it+j |     | j ∀j | ∈{0,...,t−1} |     |     |     |
| --- | ---- | --- | ---------- | --- | ---- | ------------ | --- | --- | --- |
i=0
s−1
|     |     | (cid:88) |           |     | ∀i={0,...,n−1}, |                |     |     |     |
| --- | --- | -------- | --------- | --- | --------------- | -------------- | --- | --- | --- |
|     |     |          | x it+sj+q | =1  |                 |                |     |     |     |
|     |     |          |           |     |                 | j ={0,...,k−1} |     |     |     |
q=0
∀i={0,...,n−1},
|     |     | x         |     | +x      |     | ≤1             |     |     |     |
| --- | --- | --------- | --- | ------- | --- | -------------- | --- | --- | --- |
|     |     | it+sj+s−1 |     | it+sj+s |     | j ={0,...,k−2} |     |     |     |
x∈{0,1}
Toprovidebetterservicetopatients,theoptometrycenterhasimplementedanappointmentsystem
thatrequirespatientstoscheduleanappointmentinadvancetoreceivemedicalcare. Reservationsfor
theupcomingweek,fromMondaytoSunday,closeeverySundayevening. Atthispoint,thecenter
knowstheprecisenumberofpatientsforeachshiftofthenextweek. Thecentermightadjusttheshift
scheduletosatisfytheactualpatientdemandortoimprovetheoverallnursepreferences. However,
duetothelatenoticeforschedulechanges,thenurse’spreferencemaybecomelower. Forexample,
ifanurseisrescheduledtoashiftforwhichheroriginalpreferenceis5,nowherpreferenceforthis
shiftmaybecome4duetothelatenotice. Besides,anursemaybemoreunhappytobechangedto
21

alow-preferenceshift. Inthisscenario,sincethenurses’preferencesarein{1,2,3,4},thepenalty
functioncanbeformulatedas:
d−1
(cid:88)
|     |     | Pen(x∗ →x)= |     | Pen(x∗ | →x) |     | (25) |
| --- | --- | ----------- | --- | ------ | --- | --- | ---- |
|     |     | 1           |     | 1      | i   |     |      |
i=0
wherethei-thiteminthepenaltyfunctionis:
(cid:26)
|     |        |       | γ (5−P | )2(x −x∗ | ) x | ≥x∗  |     |
| --- | ------ | ----- | ------ | -------- | --- | ---- | --- |
|     | Pen(x∗ | →x) = | i      | i i      | 1i  | i 1i |     |
|     | 1      | i     |        |          |     | <x∗  |     |
|     |        |       | 0      |          | x   | i    |     |
1i
WearenowreadytodefinetheStage2OPwithrespecttotheabovepenaltyfunction:
(cid:88) d−1
| x∗ =argmaxP⊤x− |     |     | Pen(x∗ |       |     |     |     |
| -------------- | --- | --- | ------ | ----- | --- | --- | --- |
|                |     |     |        | →x) i |     |     |     |
| 2              |     |     |        | 1     |     |     |     |
|                | x   |     | i=0    |       |     |     |     |
n−1
(cid:88)
|     |      | m x    | ≥H  | ∀j ∈{0,...,t−1} |     |     |     |
| --- | ---- | ------ | --- | --------------- | --- | --- | --- |
|     | s.t. | i it+j | j   |                 |     |     |     |
i=0
s−1
|     | (cid:88) |         |     | ∀i={0,...,n−1}, |     |     |     |
| --- | -------- | ------- | --- | --------------- | --- | --- | --- |
|     |          | x       | =1  |                 |     |     |     |
|     |          | it+sj+q |     | j ={0,...,k−1}  |     |     |     |
q=0
∀i={0,...,n−1},
|     | x it+sj+s−1 |     | +x it+sj+s | ≤1  |     |     |     |
| --- | ----------- | --- | ---------- | --- | --- | --- | --- |
j ={0,...,k−2}
x∈{0,1}
Thenthesimplifiedformofthepost-hocregretfortheNSPcanbewrittenas:
d−1
| PReg(θˆ,θ)=P⊤x∗(H)−P⊤x∗+ |     |     |     | (cid:88) | Pen(x∗ | →x∗) |      |
| ------------------------ | --- | --- | --- | -------- | ------ | ---- | ---- |
|                          |     |     |     |          |        | i    | (26) |
|                          |     |     |     | 2        |        | 1 2  |      |
i=0
(cid:12)
∂PReg(θˆ,θ)(cid:12)
UsingEquation(26),itisstraightforwardtocomputethatthei-thiteminvector and
∂x∗ (cid:12)
2 x∗
|     | ∂PReg(θˆ,θ)(cid:12) | (cid:12) |     |     |     |     | 1   |
| --- | ------------------- | -------- | --- | --- | --- | --- | --- |
thei-thiteminvector :
|     | ∂x∗ | (cid:12) |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- |
|     | 1   | x∗       |     |     |     |     |     |
2
|    |     |    |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
(cid:12)
|     | ∂PReg(θˆ,θ)(cid:12) |             | (cid:26) −P | +2γ (5−P | )   | x∗ ≥x∗   |     |
| --- | ------------------- | ----------- | ----------- | -------- | --- | -------- | --- |
|     |                     | (cid:12)    |             | i i      | i   | 2 i 1 i  |     |
|    |                     | (cid:12)   | =           |          |     |          |     |
|     | ∂x∗                 |             | −P          |          |     | x ∗ <x ∗ |     |
|     | 2                   | (cid:12) x∗ |             | i        |     | 2i 1i    |     |
1 i
|     |                    | (cid:12)   |    |            |     |       |     |
| --- | ------------------- | ---------- | --- | ---------- | --- | ----- | --- |
|     | ∂PReg(θˆ,θ)(cid:12) |            |     | (cid:26)   | x∗  | ≥x∗   |     |
|     |                     |            |     | −2γ i (5−P | i ) |       |     |
|     |                    | (cid:12)   |  = |            | 2   | i 1 i |     |
|     | ∂x∗                 | (cid:12)   |     | 0          | x ∗ | <x ∗  |     |
|     |                     | 1 (cid:12) |     |            | 2i  | 1i    |     |
x∗
2 i
∂x∗
Approximation 2. SimilartothecomputationinSectionC.1,weobtaintheStage1optimal
∂x∗
solutionx∗, 1 ge2optimalsolutionx∗, andthecorrespondingµfromtheinterior-pointLP
| 1 theSta |     |     | 2   |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- |
∂x∗
computetheterm 2. UsingthepenaltyfunctioninEquation(25),theStage2OPcanbeformulated
∂x∗
1
22

asaMILPbyaddingnewvariablesσandonemoreconstraint:
d−1
(cid:88)
| x∗ =argmaxP⊤x− |     | γ (5−P | )2σ |     |
| -------------- | --- | ------ | --- | --- |
| 2              |     | i      | i i |     |
|                | x   | i=0    |     |     |
n−1
(cid:88)
|     | s.t. m x | ≥H ∀j  | ∈{0,...,t−1} |     |
| --- | -------- | ------ | ------------ | --- |
|     | i        | it+j j |              |     |
i=0
s−1
|     | (cid:88) | ∀i={0,...,n−1}, |                |     |
| --- | -------- | --------------- | -------------- | --- |
|     | x        | =1              |                |     |
|     | it+sj+q  |                 | j ={0,...,k−1} |     |
q=0
∀i={0,...,n−1},
|     | x it+sj+s−1 | +x it+sj+s | ≤1  |     |
| --- | ----------- | ---------- | --- | --- |
j ={0,...,k−2}
−x∗
|     | σ i ≥x i | ∀i={0,...,d−1} |     |     |
| --- | -------- | -------------- | --- | --- |
1i
x∈{0,1}
σ ∈{0,1}
SupposetheStage2OPoftheNSPcanbewrittenas:
x∗ =argmin−P⊤x+(γ◦(5−P)2)⊤σ
2
x
|     | s.t. | G 1 x≥H |     |     |
| --- | ---- | ------- | --- | --- |
Ax=b
G x≥−1
2
σ−x≥−x∗
1
x,σ ∈{0,1}
ThenthestandardformoftheStage2OPis:
x′ =argminc⊤x′
2
x′
A′x′
|     |     | s.t. | =b  |     |
| --- | --- | ---- | --- | --- |
Gx≥h
|     |     | x′  | ∈{0,1} |     |
| --- | --- | --- | ------ | --- |
where
| (cid:2)    | γ◦(5−P)2(cid:3) | ∈R2d, | σ]∈R2d     |          |
| ---------- | --------------- | ----- | ---------- | -------- |
| c = −P     |                 |       | x′ =[x     |          |
| (cid:34) G | 0 (cid:35)      |       | (cid:34) H | (cid:35) |
1
| G = G | 0 ∈R(t+nk−n+d)×2d, |     | h = −1 | ∈Rt+nk−n+d |
| ----- | ------------------ | --- | ------ | ---------- |
2
| −I  | I   |     | −x∗ |     |
| --- | --- | --- | --- | --- |
1
]∈Rnk×2d
| A′ =[ A | 0   |     |     |     |
| ------- | --- | --- | --- | --- |
andb∈Rnk isanall-onesvector.
Itisclearthatx∗isintheobjectiveandx∗isinhoftheconstraints. ApplyingLemmaB.3,wecan
| 2   |     | 1   |     |     |
| --- | --- | --- | --- | --- |
∂x∗
computeanapproximategradientofthe 2 term.
∂x∗
1
23

D HyperparametersfortheExperiments
Themethodsofk-NN,RF,NN,andIntOpt-Caswellas2Shavehyperparameters,whichwetune
viacross-validation: fork-NN,wetryk ∈{1,3,5};forRF,wetrydifferentnumbersoftreesinthe
forest{10,50,100};forNN,IntOpt-C,and2S,wetreatthelearningrate,epochsandweightdecay
ashyperparameters.
Tables7,8,and9showthefinalhyperparameterchoicesforthethreeproblems:1)analloyproduction
problem,2)theclassic0-1knapsackproblem,and3)anurserosterschedulingproblem.
Table7: Hyperparametersoftheexperimentsonthealloyproductionproblem.
Model Hyperparameters
Proposed optimizer:optim.Adam;learningrate:5×10−7;µ=10−3;epochs=20
k-NN k=5
RF n_estimator=100
NN optimizer:optim.Adam;learningrate:10−3;epochs=20
Table8: Hyperparametersoftheexperimentsonthe0-1knapsackproblem.
Model Hyperparameters
Proposed optimizer:optim.Adam;learningrate:10−7;µ=10−3;epochs=12
k-NN k=5
RF n_estimator=100
NN optimizer:optim.Adam;learningrate:10−3;epochs=12
Table9: Hyperparametersoftheexperimentsonthenurseschedulingproblem.
Model Hyperparameters
Proposed optimizer:optim.Adam;learningrate:10−1;µ=10−3;epochs=8
k-NN k=5
RF n_estimator=100
NN optimizer:optim.Adam;learningrate:10−2;epochs=8
Ridge, k-NN, CART and RF are implemented using scikit-learn [24]. The neural network is
implementedusingPyTorch[22]. Tocomputethetwostagesofoptimizationattesttimeforour
method,andtocomputetheoptimalsolutionofan(MI)LPunderthetrueparameters,weusethe
MILPsolverfromGurobi[11].
E Comparisonsofthe2SMethodandthePriorDifferentiationMethods
Inthissection,wecomparetheproposedmethodwithpriorworks[1,2,27]thatprovidewaysof
differentiatingthroughLPsorLPswithregularization. WeconductcomparisonswithCvxpyLayer
[1]butnotOptNet[2]orQPTL[27]. ThereasonisthatthecalculationmethodproposedinQPTLis
LP+quadraticregularizationusingOptNet,andCvxpyLayerisjustaconicextensiontoOptNet. We
comparedCvxpyLayer[1]witha)noregularization,b)quadraticregularizationandc)log-barrier
(like our Section 4/Appendix B). The key indicator of its predictive performance is the type of
regularizationused,withthelog-barrierversionperformingthebest,butstillslightlyworsethanour
method. WeappliedCvxpyLayer[1]tothe0-1knapsackbenchmarktocomparewithour2Smethod.
Table 10 reports the mean post-hoc regrets and standard deviations across 10 runs and Table 11
reportstheaveragetrainingtimes. Moreprecisely,weuseitwithvariousregularizations(a. LPwith
noregularization,b. withquadraticregularization,c. withlog-barrierasinourpaper)toreplacethe
Section4/AppendixBgradientcalculations. WefindthatCvxpyLayer[1]nevergivesbettersolution
qualitywhile2Sis30%–50%faster.
24

Table10: Meanpost-hocregretsandstandarddeviationsofthe2SmethodandCvxpyLayerwith
differentregularizationonthe0-1knapsackproblem.
Penalty
| PReg    | factor |           | 2S  | CvxpyLayer+log | CvxpyLayer+quad_reg |     | CvxpyLayer+no_reg |     |
| ------- | ------ | --------- | --- | -------------- | ------------------- | --- | ----------------- | --- |
|         | 0.05   | 1.26±0.01 |     | 1.26±0.01      | 1.27±0.01           |     | 7.70±0.39         |     |
| cap=100 | 0.25   | 6.28±0.05 |     | 6.28±0.05      | 6.34±0.03           |     | 8.87±0.92         |     |
|         | 0.5    | 9.22±0.10 |     | 9.47±0.31      | 9.96±0.54           |     | 10.13±0.46        |     |
|         | 0.05   | 0.73±0.01 |     | 0.74±0.01      | 0.75±0.03           |     | 6.74±0.58         |     |
| cap=150 | 0.25   | 3.64±0.04 |     | 3.64±0.04      | 3.70±0.03           |     | 7.18±0.77         |     |
|         | 0.5    | 7.27±0.06 |     | 7.28±0.08      | 7.39±0.06           |     | 8.43±0.58         |     |
Table11:Averageruntime(inseconds)ofthe2SmethodandCvxpyLayerwithdifferentregularization
onthe0-1knapsackproblem.
| Runtime |     | 2S     | CvxpyLayer+log | CvxpyLayer+quad_reg |        | CvxpyLayer+no_reg |        |     |
| ------- | --- | ------ | -------------- | ------------------- | ------ | ----------------- | ------ | --- |
| cap=100 |     | 204.76 | 438.24         |                     | 571.38 |                   | 344.50 |     |
| cap=150 |     | 245.61 | 467.65         |                     | 662.30 |                   | 366.83 |     |
F FrameworksComparisonsontheAlloyProductionProblem
Inthissection,wefurthercomparedtheproposedframeworkwiththeframeworkusingthediffer-
entiableprojectionideain[3]onthealloyproductionbenchmark. Theideain[3]istousethel
2
projection,andweimplementeditusingCvxpyLayer. Theexperimentset-upfollowsthatofTable2:
bothtrainingandtestingusel projectioninthesecondstage,asopposedtosolvingthesecondstage
2
optimizationproblemdefinedinSection3. Table12showsboththepost-hocregretandtrainingtime
forl 2 projection. Wefindthatnotonlyisl 2 projectionslow,butithasevenworsepost-hocregret
thantheHuetal. correction[12]. WesuspectthatthisisduetotheHuetal. correctionfunction
[12]preservingthedirectionofthesolutionvectorwhereasl projectioncanchangethedirection,
2
andthatthismakesadifferenceforAlloyProduction. Inanycase,thisexperimentconfirmsagain
thatourTwo-Stageframeworkhasbetterpost-hocregretthanaframeworkbasedondifferentiable
projections,reinforcingthemainmessageofourpaper.
Table12: Comparisonofthreeframeworksonthealloyproductionproblem.
|     |     |     |     |     | PReg |     |     | Average |
| --- | --- | --- | --- | --- | ---- | --- | --- | ------- |
Penaltyfactor 0.25±0.015 0.5±0.015 1±0.015 2±0.015 4±0.015 8±0.015 runtime
Two-StagePredict+
|     | 43.87±2.73 | 65.71±4.81 |     | 88.75±5.91 | 123.90±6.84 | 161.86±8.49 | 194.06±13.09 | 268.22 |
| --- | ---------- | ---------- | --- | ---------- | ----------- | ----------- | ------------ | ------ |
OptimizeFramework
Huetal.Framework 68.16±6.26 82.91±5.45 107.64±6.85 150.47±12.99 178.69±10.09 206.84±12.51 228.00
l2_projection 103.28±4.87 118.90±6.99 150.15±11.45 212.62±20.58 337.59±23.24 562.41±34.29 442.97
G Experimentsonthe0-1KnapsackProblemwithLargePenaltyFactors
Table13reportsthemeanpost-hocregretsandstandarddeviationsacross10runsforeachapproach
onthe0-1knapsackproblemwithlargepenaltyfactors(penaltyfactors≥1). Withmoredata,we
canmakefurtheranalysisoftheperformanceoftheproposed2Smethod. ObservingTables4and13,
wecanseethatthetrend,intermsofthedifferencebetween2Sandothermethods,firstdecreases,
thenincreases,asthepenaltyfactorincreases. ThetrendinTables4and13isidenticaltothetrendin
Table3. Wecanexplainthisphenomenonasfollows.
First,whenthepenaltyfactorissmall,therationalbehaviorforthebuyeristojusttakeeveryorder,
andonlydecidewhichorderstodropwhenthetrueparametersarerevealed(atclosetonocost). 2S
identifiesandexploitsthisbehaviorforsmallpenalties,whileclassicregressionmethodsareagnostic
tothispossibletactic. Thus,theadvantageof2Scomparedtoclassicregressionmethodsislargein
thesmallpenaltycase.
Second,whenthepenaltyfactorislarge,2Swillanalogouslylearntobeconservative,suchthatthe
firststagesolutionlikelyremainsfeasibleunderthetrueparameters,inordertoavoidthenecessary
(andhigh)penaltyduetohavingtochangetoafeasiblesolution. Again,classicregressionmethods
willbeagnostictothispossibletactic,leadingtoalargeadvantageof2Sovertheclassicmethods.
25

Table 5 only has the increasing trend from the large penalty, since it is neither a covering nor a
packingprogram,andsothereisnoanalogoustactic/exploitationforthesmallpenalty.
Table13: Meanpost-hocregretsandstandarddeviationsfor0-1knapsackproblemwithlargepenalty
factorsusingtheTwo-StagePredict+Optimizeframework.
Penalty
PReg 2S CombOptNet Ridge k-NN CART RF NN TOV
factor
1 10.90±0.15 10.93±0.17 10.93±0.19 11.11±0.17 11.16±0.14 11.01±0.31 11.26±0.23
cap=100 2 12.31±0.16 12.45±0.25 12.48±0.20 12.49±0.21 13.77±0.26 12.60±0.39 12.78±0.30 29.68±0.14
4 14.54±0.15 15.66±0.47 15.57±0.25 15.68±0.39 19.01±0.56 15.77±0.62 15.84±0.50
1 10.23±0.12 10.22±0.18 10.46±0.23 10.40±0.18 10.46±0.19 10.49±0.21 10.86±0.30
cap=150 2 11.18±0.15 11.74±0.34 11.88±0.30 11.63±0.20 12.56±0.31 11.83±0.19 12.12±0.17 40.23±0.19
4 13.20±0.16 14.33±0.46 14.71±0.49 14.43±0.33 16.75±0.63 14.53±0.29 14.65±0.41
1 6.77±0.36 15.30±0.28 7.67±0.18 7.51±0.27 7.71±0.20 7.67±0.16 8.00±0.65
cap=200 2 8.19±0.12 15.39±0.16 8.84±0.22 8.69±0.26 9.24±0.30 8.80±0.20 8.97±0.37 48.13±0.24
4 9.71±0.35 15.46±0.22 11.17±0.40 11.06±0.32 12.29±0.59 11.05±0.46 10.91±0.53
1 1.37±0.08 20.69±0.20 3.08±0.19 2.94±0.16 3.17±0.17 3.05±0.25 3.28±0.96
cap=250 2 3.34±0.15 20.78±0.20 3.80±0.20 3.73±0.15 3.94±0.20 3.79±0.26 3.89±0.58 53.43±0.26
4 4.46±0.09 20.93±0.20 5.25±0.35 5.32±0.27 5.47±0.35 5.29±0.48 5.11±0.39
H RuntimesfortheExperiments
Inthispaper,allmodelsaretrainedwithIntel(R)Xeon(R)CPUE5-2630v2@2.60GHzprocessors.
Table14showstheaverageruntimeacross10simulationsfordifferentoptimizationproblems. Since
thetestingtimeofdifferentapproachesisquitesimilar,here,theruntimereferstoonlythetraining
timeofthepredictionmodelanddoesnotincludethetestingtime.Attrainingtime,onlytheproposed
2SmethodandIntOpt-CsolvetheLP.TrainingfortheusualNNdoesnotinvolvetheLPatall,and
sotrainingismuchfaster(butgivesworseresults).
SinceIntOpt-Ccannothandlethevariantofthe0-1knapsackproblemandtheNSP,weonlyreport
theruntimeofIntOpt-Cforthealloyproductionproblem.
SincetheprovidedcodeofCombOptNetisonlyavailableforthe0-1knapsackproblem,weonly
reporttheruntimeofCombOptNetforthe0-1knapsackproblem. AsTable14shows,CombOptNet
isdrasticallyslowerthantheproposed2Smethod.
Inthealloyproductionproblem,theruntimesoftheproposed2Smethodarealittlelargerthanthat
ofIntOpt-C.Thereasonisthat2SneedstosolvetwoLPswhentrainingwhileIntOpt-Conlyneeds
tosolveone. Butinthealloyproductionproblem,theunknownparametersareonthelefthandside
oftheinequalityconstraintsandthegradientcomputationincludesmatrixcomputation,whichisalso
time-consuming. Thus,theruntimesofthe2Smethodarelargerbutnottwiceaslargeasthatofthe
IntOpt-Cmethod.
Inboththealloyproductionproblemandthevariantofthe0-1knapsackproblem,theruntimesofthe
2SmethodaremuchbetterthanRF.
Theruntimeofthe2SmethodislargeintheNSP.Thisisbecauseweusetheformulationwhereeach
decisionvariablecorrespondstowhetheraspecificnurseisassignedtoaspecificdayandaspecific
shift. Thus,thenumberofthedecisionvariableoftherelaxedLPislargeandtheLPtakesmoretime
tosolve.
Table14: Averageruntime(inseconds)forthealloyproduction,0-1knapsack,andnursescheduling
problems.
Alloyproduction 0-1knapsack
Runtime(s) Nursescheduling
Brass Titanium-alloy Capacity=100 Capacity=150 Capacity=200 Capacity=250
2S 268.22 394.53 204.76 245.61 202.65 193.46 537.32
IntOpt-C 228.00 331.38 N\A
CompOptNet N\A 2341.40 2940.26 2394.05 2383.39 N\A
Ridge 20.22 56.89 22.33 <1
k-NN 25.14 70.22 26.00 <1
CART 30.33 94.89 34.83 <1
RF 959.50 2552.25 1034.07 2.11
NN 212.22 321.11 135.80 11.39
26