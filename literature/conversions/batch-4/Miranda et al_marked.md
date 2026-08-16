---
conversion_metadata:
  converted_at: "2026-07-21T07:33:53Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Miranda et al.pdf"
  source_pdf_sha256: "950f84f96cba1a132f0633cbaa3a3097c08be70d7345f9aa11ee6dbafcd72363"
  page_count: 28
  markdown_char_count: 277187
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Polyglot Teachers: Evaluating Language Models for Multilingual
Synthetic Data Generation

Lester James V. Miranda

Ivan Vuli´c Anna Korhonen

Language Technology Lab, University of Cambridge
ljvm2@cam.ac.uk

Collection ljvmiranda921/polyglot-teachers

Code ljvmiranda921/polyglot-teachers

6
2
0
2

r
p
A
3
1

]
L
C
.
s
c
[

1
v
0
9
2
1
1
.
4
0
6
2
:
v
i
X
r
a

Abstract

Synthesizing supervised finetuning (SFT) data
from language models (LMs) to teach smaller
models multilingual tasks has become increas-
ingly common. However, teacher model se-
lection is often ad hoc, typically defaulting
to the largest available option, even though
such models may have significant capability
gaps in non-English languages. This practice
can result in poor-quality synthetic data and
suboptimal student downstream performance.
In this work, we systematically characterize
what makes an effective multilingual teacher.
We measure intrinsic measures of data qual-
ity with extrinsic student model performance
in a metric we call POLYGLOT SCORE; eval-
uating 10 LMs across 6 typologically diverse
languages, generating over 1.4M SFT examples
and training 240 student models. Among the
models tested, Gemma 3 27B and Aya Expanse
32B emerge as consistently effective teachers
across different student base model families.
Further analyses reveal that model scale alone
does not significantly predict teacher effective-
ness; instead, data qualities such as prompt
diversity, length, and response fluency capture
over 93.3% of variance in intrinsic data quality
and predict student performance. Finally, we
provide practical recommendations, including
matching the model families of teacher-student
pairs and translating from or responding to ex-
isting prompts, which can yield improvements
for less-resourced languages. We hope that our
work advances data-centric research in multi-
lingual synthetic data and LM development.

1

Introduction

Supervised finetuning (SFT, Ouyang et al., 2022)
has emerged as a standard approach for adapting
language models (LMs) to specific target languages
(Zhang et al., 2025b; Aryabumi et al., 2024, inter
alia). Central to the success of SFT is the avail-
ability of high-quality training data, consisting of

1

pairs of user prompts and a corresponding response,
which is often scarce for less-resourced languages
(Kunchukuttan et al., 2025). Generating prompt-
response pairs for these languages demands sub-
stantial human effort (Singh et al., 2024; Kapania
et al., 2025), creating a bottleneck for language-
specific model development.

To alleviate the challenge of human effort and
data scarcity, synthetic data generation using LMs
has gained traction as a promising solution for
multilingual LM development (Cahyawijaya et al.,
2024; Ng et al., 2025; Martins et al., 2025; Ham-
moud et al., 2026, inter alia). This approach in-
volves leveraging a typically larger teacher model
to generate training examples, which are then used
to finetune a smaller student model to replicate the
knowledge of the teacher (Kim and Rush, 2016).
However, existing works often select teacher mod-
els arbitrarily, defaulting to the largest state-of-the-
art models that excel on benchmarks (Xu et al.,
2025b; Li et al., 2025; Zhang et al., 2025a). This
practice is problematic because these models, de-
spite strong performance, may have significant ca-
pability gaps in non-English languages, leading
to poor-quality synthetic data that propagates the
teacher’s weaknesses rather than its strengths. And
so we ask: “what makes an effective multilingual
teacher for synthetic data generation, and how can
we systematically measure it?”

In this work, we conduct a comprehensive anal-
ysis of 10 LMs across 6 typologically diverse lan-
guages on three common synthetic data generation
methods: responding to a user query or instruc-
tion, translating prompts from English to a target
language, and generating prompt-response pairs
given in-context examples (§2.2). To systemati-
cally assess teacher model effectiveness, we eval-
uate LMs using both intrinsic measures of data
quality (§2.2, i.e., the diversity of prompts and re-
sponses, the perplexity of the base model on the
response, and response quality based on a multi-

---

<!-- PAGE 2 -->

Figure 1: Overview of our method for evaluating language models as multilingual teachers (POLYGLOT
SCORE). We evaluate teacher models on their synthetic data generation capabilities across three methods: Generate
a prompt-response pair given few-shot examples, Translate prompts from English and generate a response, and
Respond to a prompt in the target language. The POLYGLOT SCORE incorporates both intrinsic data quality metrics
and extrinsic student model performance to assess the effectiveness of a teacher model for a target language.

lingual reward model) and an extrinsic measure
of student model performance on multilingual
tasks (§2.3, cultural understanding, mathematical
reasoning, general chat). We aggregate these mea-
surements into a single metric called POLYGLOT
SCORE (PG-SCORE), in order to provide a holistic
assessment of a teacher model’s data generation
capabilities. Our contributions are as follows:
• We close the evaluation gap by evaluating 10
teacher models, generating over 1.4M SFT ex-
amples and finetuning 240 student models from
OLMo 3 7B. We find that Gemma 3 27B con-
sistently ranks within the top three highest PG-
SCORE and that the Gemma 3 model family out-
performs other families such as Llama 3.1 and
IBM Granite (§3.1). Our PG-SCORE rankings
are consistent across other base model families
(Llama 3.1 8B, Qwen 3 8B, Gemma 3 4B, §3.2).
• We provide analyses and insights on the char-
acteristics of a good multilingual teacher model.
Our analyses reveal that model scale and bench-
mark performance, which are common assump-
tions of a “strong” model, do not significantly
predict teacher effectiveness (§4.1). Instead, we
find that qualities of the generated data, namely
prompt diversity and length coupled with flu-
ent and diverse responses, capture over 93.3%
of the variance in intrinsic data quality metrics,
and their principal components predict student
performance with R2=0.664 (§4.2).

• Based on these findings, we recommend a
recipe (§5) for generating multilingual syn-
thetic data. For example, we find that matching

the model families of the teacher and student is
a reliable heuristic for choosing a teacher model
(§3.2), and generating responses to existing
prompts or translating from English can yield
substantial improvements on less-resourced lan-
guages compared to a random mix of data gen-
eration methods, though gains vary by teacher
model (§3.3).1
We hope that this work paves the way for devel-
oping inclusive and equitable language technolo-
gies through quality and cost-effective data. We
release our code, data, and models to drive research
in multilingual synthetic data generation.

2 Evaluating Language Models as

Multilingual Teachers

The POLYGLOT SCORE (Figure 1) of a teacher
model T for a target language ℓ is based on the (1)
intrinsic quality of the synthetic data generated by
the teacher (§2.2) and the (2) extrinsic performance
of a student model S finetuned on this data (§2.3).

2.1 Creating the seed dataset

In order to bootstrap the synthetic data gener-
ation process, we create a seed dataset
Dseed,ℓ
for each target language ℓ. We create
Dseed,ℓ
by aggregating publicly available multilingual
instruction-tuning datasets, including the Aya Col-
lection (Aryabumi et al., 2024), WildChat 4.8-M
(Zhao et al., 2024), EuroBlocks-SFT (Martins et al.,

1As a supplementary, we show that our recipe improves
performance on a held-out language (Tagalog) on a language-
specific benchmark (Appendix I).

2

---

<!-- PAGE 3 -->

2025), and Magpie-Align (Xu et al., 2025a). In or-
der to simulate scenarios where English prompts
are translated into a target language, we also in-
clude examples from Tülu 3 SFT (Lambert et al.,
2025), Helpsteer3 (chosen responses, Wang et al.,
2025), and GSM8K (train split, Cobbe et al., 2021).
Detailed seed dataset statistics in Appendix B.

2.2 Multilingual Data Quality & Diversity

{

Synthetic data generation Given a teacher
model T , target language ℓ, and a seed dataset for
language ℓ,
Dseed,ℓ, we distill a synthetic dataset
N
i=1 consisting of N prompt-
(xi, yi)
T,ℓ =
D
}
response pairs (xi, yi). We consider three synthetic
data generation methods found in literature:
• Generate: we sample k prompt-response pairs
Dseed,ℓ as few-shot examples and use T
from
to generate a new pair (xi, yi) conditioned on
these examples.

• Translate:

we forward-translate English
Dseed,ℓ to the target language ℓ
prompts from
to obtain xi, and use T to generate the corre-
sponding response yi.

• Respond: we take a prompt xi from
use T to generate the response yi.
We provide a brief review of multilingual syn-
thetic data generation methods in §6 and a supple-
mentary survey in Appendix A.

Dseed,ℓ and

D

Data quality and diversity metrics Synthetic
data is valuable when it is both high-quality and di-
verse (Raventos et al., 2023; Chen et al., 2024; Zhu
et al., 2025).2 To estimate the value of
T,ℓ, we
compute a set of lexical and model-based metrics:
• Diversity of prompts and responses (dx, dy):
a corpus-level statistic that computes the co-
sine distance of the prompt and response em-
beddings. In practice, we use Llama-Embed-
Nemotron-8B (Babakhin et al., 2025), the top-
performing model on the MMTEB leaderboard
(Enevoldsen et al., 2025), to embed the texts.
• Perplexity (PPL): the perplexity of a base model
on the response yi conditioned on the prompt
xi, measuring the fluency and naturalness of the
generated text. Lower perplexity indicates more
coherent and linguistically natural responses.
• Reward score of a multilingual reward model
(R): the verbalized score (1-5) of a multilin-
gual reward model based on rubrics relating to
fluency, naturalness, and instruction-following.
In practice, we prompt M-Prometheus 14B

(Pombal et al., 2025) as an LM judge to score
the quality of the prompt-response pair (Fig-
ure 13). We choose M-Prometheus because of
its high performance on human-aligned evalu-
ation benchmarks, suggesting that the reward
model aligns well with native speakers.
We combine these intrinsic metrics by scaling
each metric using z-score normalization and aver-
aging them as shown in Equation 1.
1
M

IntrinsicT,ℓ =

z-score(m(

T,ℓ))

(cid:88)

D

(1)

|

m∈M

|
dx, dy,

where M =

log(1 + PPL), R

{
2.3 Student Model Performance

−

}

S

D

We perform supervised finetuning of a base model
Sϕ on the synthetic dataset
T,ℓ to obtain a student
model ST,ℓ. Then, we evaluate
T,ℓ on a suite of
multilingual tasks to assess how well the student
has learned from the teacher. These tasks include:
• Cultural and factual understanding (CULTURE):
we evaluate on Global-MMLU Lite (Singh et al.,
2025), containing culturally diverse and relevant
questions that were localized by native speakers
from English (Hendrycks et al., 2021).

• General chat (CHAT): we evaluate on M-
RewardBench (Gureja et al., 2025) which mea-
sures the alignment of models with human pref-
erences in conversational settings.

• Mathematical reasoning (MATH): we evaluate
on M-GSM (Shi et al., 2023), a multilingual ver-
sion of the GSM8K dataset (Cobbe et al., 2021)
that tests the model’s ability to solve mathemat-
ical word problems.
Inspired by Kim et al. (2025), we compute the
Performance Gap Recovered (PGR) that measures
the improvement of ST,ℓ over a base model Sϕ on
a benchmark b relative to a reference model SREF
(Equation 2).

ExtrinsicT,ℓ =

1
B

|

(cid:88)

b∈B

|

scoreb(ST,ℓ)
scoreb(SREF)

scoreb(Sϕ)
scoreb(Sϕ)

−
−

where B =

{

CULTURE, CHAT, MATH

}

(2)

2.4 Computing POLYGLOT SCORE

To provide straightforward comparisons between
teacher models, PG-SCORE reports a single score
that combines both extrinsic and intrinsic metrics
as shown in Equation 3.

2We use “data quality” to refer to both aspects hereafter.

PG-SCORET,ℓ = z-score(Intr.T,ℓ + Extr.T,ℓ) (3)

3

---

<!-- PAGE 4 -->

Teacher Model

Average Arabic (ar) Czech (cs) German (de) Spanish (es)

Indonesian (id)

Japanese (ja)

Gemma 3 27B Inst.
Aya Expanse 32B
Gemma 3 12B Inst.
Command A
Gemma 3 4B Inst.
GPT 4o mini
IBM Granite 4.0
IBM Granite Micro
Llama 3.1 70B Inst.
Llama 3.1 8B Inst.

0.726
0.706
0.595
0.546
0.469
0.461
0.312
0.304
0.140
-0.356

0.145
-0.058
-0.464
-1.360
-0.488
-1.117
-0.072
-0.282
-0.964
-1.693

0.360
0.222
0.327
0.114
0.330
0.015
-0.031
0.290
0.109
-0.974

1.655
1.468
1.756
1.673
1.644
1.766
1.000
1.102
1.195
0.891

1.358
1.129
1.228
1.102
0.929
0.908
0.734
0.783
0.688
0.182

0.214
1.153
0.151
1.063
-0.105
1.003
-0.079
-0.329
0.182
0.322

0.626
0.320
0.573
0.683
0.504
0.189
0.321
0.264
-0.373
-0.863

Table 1: Top models with the highest PG-SCORE (average across six languages). We evaluate teacher models
with varying size and model family on 6 typologically-diverse languages. For each language, we highlight the best
model in bold and the second-best model with an underline. Detailed results with standard errors are in Table 13.

We combine both intrinsic and extrinsic met-
rics because they capture complementary aspects
of teacher quality. Extrinsic metrics alone may
overlook the quality of synthetic data that propa-
gates through the ecosystem, while intrinsic met-
rics alone do not guarantee that the student model
achieves strong downstream performance. The re-
sulting PG-SCORE is z-score normalized, where 0
indicates average teacher effectiveness, and higher
scores indicate better synthetic data quality and
student performance for that language. We adopt
equal weighting as a baseline; we show that
teacher rankings are robust to alternative weighting
schemes in Appendix G.4.

3 Experiments: Evaluating LMs and

PG-SCORE Generalization

In this section, we measure the POLYGLOT SCORE
of state-of-the-art LMs (§3.1). Then, we test
whether our findings are consistent across other
base models (§3.2). Finally, we determine if a cer-
tain data generation method is more effective in
multilingual settings (§3.3). We conduct additional
experiments and ablations in Appendix G.

3.1 Which State-of-the-Art LMs Are Good

Multilingual Teachers?

Setup In order to evaluate the effectiveness of
different LMs as multilingual teachers, we select
10 state-of-the-art models that vary in scale, ar-
chitecture, and training data, then evaluate them
on 6 typologically diverse languages by generat-
ing 10.5k prompt-response pairs for each teacher-
language pair where each data generation (§2.2)
method is equally represented. We repeat the data
generation process three times with different ran-
dom seeds to account for variability in LM outputs.

Then, we finetune a pretrained OLMo 3 7B model
(OLMo Team et al., 2025) on each
T,ℓ to obtain
ST,ℓ. Appendix E.1 describes SFT information.

D

Teacher Models We include Llama 3.1 (8B, 70B,
Grattafiori et al., 2024), Gemma 3 (4B, 12B, 27B,
Gemma Team et al., 2025), Command A (Cohere
Team et al., 2025), Aya Expanse 32B (Dang et al.,
2024), and IBM Granite (4.0, Micro, Granite Team,
IBM, 2025).
In addition, we also include GPT
4o mini (OpenAI et al., 2024) as a representative
closed-source model. See Table 7 in Appendix D
for detailed model information.

Target Languages We select 6 typologically di-
verse languages: Arabic (ar), Czech (cs), German
(de), Spanish (es), Indonesian (id), and Japanese
(ja). These languages are chosen due to their varia-
tion in resource availability, script, and family. This
language choice is also supported by prior work on
informed sampling (Ploeger et al., 2026) that con-
siders typological variety of the chosen languages.
See Table 8 in Appendix D for language statistics.

Results Table 1 shows the PG-SCORE of each
teacher model across all target languages. The
results suggest the following:
• Gemma 3 27B and Aya Expanse 32B are
the most effective teachers.
Gemma 3
27B achieves the highest average PG-SCORE
(0.726), followed closely by Aya Expanse 32B
(0.706), both outperforming larger models like
Llama 3.1 70B Inst. (0.140), suggesting that
model scale alone does not determine teacher ef-
fectiveness. We also observe that the Gemma 3
family dominates the top ranks, while the Llama
3.1 family underperforms on most languages.
• Smaller LMs can be effective multilingual
teachers. Gemma 3 12B (0.595) and 4B (0.469)

4

---

<!-- PAGE 5 -->

Base Model (Sϕ)

Teacher Model

OLMo 3 7B Gemma 3 4B Qwen 3 8B Llama 3 8B

GPT 4o mini
Llama 3.1 70B Inst.
Llama 3.1 8B Inst.
Command A
Aya Expanse 32B
Gemma 3 27B Inst.
Gemma 3 12B Inst.
Gemma 3 4B Inst.
IBM Granite 4.0
IBM Granite Micro

0.551
0.138
−0.160
0.459
0.854
0.672
0.481
0.350
0.283
0.164

1.022
0.338
−0.133
0.725
0.762
0.810
0.666
0.712
0.278
0.455

1.005
1.039
0.365
0.974
1.183
1.301
1.393
0.545
0.831
1.079

0.621
0.497
0.048
0.737
0.793
0.800
0.804
1.062
−0.001
0.396

Figure 2: PG-SCORE across different base models (average across Arabic, German, and Indonesian). Left:
Average PG-SCORE of each teacher model on students finetuned on three different base models. We highlight the
top , second , and third best teacher models for each setting. Right: Heatmap showing Spearman rank correlation
ρ of teacher model rankings across base models. We show percentage increases in PG-SCORE on Table 14.

Arabic (ar)

German (de)

Indonesian (id)

Teacher Model

Generate Translate Respond Generate Translate Respond Generate Translate Respond

0.802
0.276
0.032
Gemma 3 27B Inst.
0.148 −1.349
−0.276
Aya Expanse 32B
Llama 3.1 70B Inst. −0.867 −1.025 −0.215

2.140
1.473
1.391

2.086
1.255
0.459

1.189
1.212
1.451
0.039
1.187 −0.146

1.196
0.733
0.089

0.046
1.606
0.155

Table 2: PG-SCORE across three data generation methods: Generate, Translate, and Respond (§2.2). For
each data generation method, we generate 10k samples per teacher-language pair and finetune a student model on
OLMo 3 7B. We show percentage increases in PG-SCORE compared to a baseline (equal representation of the three
data generation methods) on Table 15.

rank among the top-5 teachers, while the Llama
3.1 70B Inst. (0.140) ranks ninth, suggesting
that smaller LMs can match or exceed larger
LMs in data generation capabilities.

• Teacher performance varies significantly by
language. German and Spanish consistently
show the highest scores across all models, while
Arabic proves challenging with most teach-
ers yielding negative scores, suggesting that
language-specific factors influence teacher ef-
fectiveness. We hypothesize that a language’s
resource status or presence in pretraining data
may contribute to this variability (§G.5).

3.2 Generalization of PG-SCORE Across

Different Base Models

Setup Instead of using OLMo 3 7B as the base
model (Sϕ) for student finetuning, we use (1)
Llama 3.1 8B, (2) Gemma 3 4B PT, and (3) Qwen
3 8B Base (Yang et al., 2025). We recompute Sϕ-
dependent metrics such as perplexity and PGR. To
reduce computational costs, we focus on three lan-
guages: German (high PG-SCORE), Indonesian
(mid-range), and Arabic (low PG-SCORE).

Results Figure 2 shows the average PG-SCORE
of each teacher model across different base mod-
els while Table 14 shows the percentage increase
of family-matched teacher-student pairs compared
to the OLMo 3 7B (mismatch) baseline. We ob-
serve that the best teacher models remain consis-
tent across different student base models, with
Gemma 3 27B and Aya Expanse 32B consistently
ranking among the top three teachers. Further-
more, the Gemma 3 family continues to outper-
form other model families. In addition, we find
that the model rankings vary slightly depending
on the base model used, as Spearman rank corre-
lation ranges from ρ=0.57 (moderate) to ρ=0.87
(strong). We hypothesize that this variation may be
due to differences in architecture and pretraining
data between base models. Despite this variation,
we observe that teacher-student model family
alignment is a reliable heuristic for achieving
good PG-SCORE. For example, Gemma 3 teach-
ers consistently perform well with Gemma 3 stu-
dent bases, with family-matched pairs achieving
at least +20.5% higher PG-SCORE compared to
the worst pair (see Table 14). This finding is in-

5

---

<!-- PAGE 6 -->

teresting but reasonable given that models from
the same family likely share similar tokenization
schemes, leading to easier transfer from teacher to
student. In addition, family-matching is not a hard
constraint unlike in other distillation settings (on-
policy, Agarwal et al., 2024; Boizard et al., 2025),
but it remains a reliable heuristic for teacher selec-
tion when the optimal teacher is unknown. For our
core experiment, we use OLMo 3 7B as the base
model for finetuning to control the effect of model
family alignment when evaluating teacher quality.

3.3 Effect of Synthetic Data Generation

Method on PG-SCORE

Setup In order to determine if a data generation
method is more effective than others, we gener-
ate 10k prompt-response pairs for each method in
§2.2 and compare the PG-SCORE of each mix. We
recompute intrinsic data quality metrics and fine-
tune OLMo 3 7B to obtain a student model and
evaluate the teacher’s PG-SCORE. We also com-
pare each mix against a baseline consisting of 10k
instances with roughly equal number of samples
(
3.3k) from each method. To reduce computa-
≈
tional costs, we conduct this experiment on three
representative teachers (Gemma 3 27B, Aya Ex-
panse 32B, and Llama 3.1 70B) spanning high to
low PG-SCORE, and three languages (German, In-
donesian, Arabic) covering diverse resource levels.

Results Table 2 shows the PG-SCORE of each
data generation (see Table 15 for baseline compar-
isons). We observe that for a high-resource lan-
guage like German, the Generate method yields
the highest PG-SCORE, while for less-resourced
languages like Arabic and Indonesian, the Re-
spond or Translate methods are more effective.
We hypothesize that this occurs because the Gener-
ate method depends on few-shot examples from the
seed dataset, which are typically of higher quality
in high-resource languages. Overall, our findings
suggest that selecting a data generation method can

Predictor

β

SE

p

log (Param. Size)
Avg. Multilingual Perf.

0.053
1.387

0.080
2.204

0.507
0.529

Table 3: Results from a mixed-effects regression
model on PG-SCORE on an LM’s (a) size and (b)
avg. multilingual benchmark performance. The lack
of significant correlation suggests that both predictors
are not solely sufficient to ensure teacher effectiveness.

6

PC

Variance Expl. Cumulative

PC 1
PC 2
PC 3
PC 4
PC 5
PC 6

42.2%
22.1%
16.5%
12.6%
3.5%
3.2%

42.2%
64.3%
80.8%
93.3%
96.8%
100.0%

Table 4: Variance explained by principal components
from intrinsic data quality metrics. There are four
principal components that explain over 93.3% (cumula-
tive) of the variance.

have an impact on teacher effectiveness. In our
core experiment, we sample an equal mix of all
three methods (3.5k each) to control their effect
when evaluating teacher model quality.

4 Analysis: What Makes a Good Polyglot

Teacher?

We investigate the factors that contribute to effec-
tive multilingual teachers. We start by analyzing
common assumptions about teacher model perfor-
mance, such as size and benchmark scores (§4.1),
then determine which intrinsic factors drive stu-
dent performance (§4.2). Lastly, we examine lan-
guage properties that might influence a teacher’s
PG-SCORE (§G.5).

4.1 Do stronger models make better teachers?

Setup In order to determine if there is a rela-
tionship between a model’s size or benchmark per-
formance (i.e., common assumptions to assess a
model’s “strength”) to its effectiveness as a mul-
tilingual teacher, we fit a mixed-effects model re-
gressing PG-SCORE on (a) parameter size (N=27,
9 models, excluding GPT-4o-mini with unknown
size
3 trials), and (b) average multilingual bench-
mark performance on Global-MMLU Lite, M-
GSM, and M-RewardBench (N=180, 10 models

×

6 languages

3 trials).

×

×
Results Table 3 shows the regression results. We
observe that neither parameter size nor average
multilingual benchmark performance signifi-
cantly predict PG-SCORE (p>0.05). Specifically,
a 1-unit increase in log(Param. Size) corresponds
to a non-significant 0.053 increase in PG-SCORE.
Although this finding confirms the results of Xu
et al. (2025b) and Kim et al. (2025) for English-
based tasks, we show that “stronger” models do not

---

<!-- PAGE 7 -->

Figure 3: Loading strength of intrinsic metrics on the
principal components (PCs). PC1 suggests that good
teachers produce diverse and high-quality responses,
while PC2 focuses on prompt diversity and length. PC3
and PC4, together, indicates the importance of prompts
on student performance.

Figure 4: Fit of a linear regression model on the
PCs of the intrinsic metrics to predict student per-
formance.
Intrinsic metrics, via their PCs, can pre-
dict extrinsic student performance (R2 = 0.664 and
RMSE = 0.440) on multilingual benchmarks (§2.3).

necessarily make better multilingual teachers.

4.2 Which intrinsic metrics determine

extrinsic student model performance?

Setup In order to identify latent factors from the
intrinsic metrics that explain student performance,
we perform principal component analysis (PCA)
on the intrinsic metrics described in §2.2. Then, we
fit a regression model to predict extrinsic student
performance based on the principal components
(PCs) obtained from PCA: we split 180 data points
(10 models
3 trials) into 80%
train and 20% test, then train a linear regression
model with the PCs as the features and the student
performance as the target.

6 languages

×

×

Results Table 4 shows how much of the variance
is explained by each principal component while
Figure 3 shows the loading strength of each in-
trinsic metric on the principal components. We
observe that the first four PCs explain over 93.3%
of the variance in the intrinsic data quality metrics.
Specifically, PC 1 (42.2%) captures characteris-
tics such as lower response perplexity and high
distinctiveness, PC2 (22.1%) captures variance
in characteristics such as higher prompt diver-
sity and length, whereas PC3 (16.5%) and PC4
(12.6%) capture variance that reinforce trends on
prompt length and diversity. In addition, Figure 4

7

shows the fit of a linear model on the test set when
the PCs learn to predict student performance. We
observe that interactions within the intrinsic met-
rics can predict extrinsic student performance de-
cently, with R2 = 0.664 and RMSE = 0.440.
This finding suggests that even with a simple linear
model, our chosen intrinsic metrics are predic-
tive of student performance. In practice, these in-
sights can help practitioners select teacher models
based on intrinsic metrics alone, which are cheaper
to compute than extrinsic student evaluations.

5 Discussion: Towards a Recipe for

Multilingual Synthetic Data Generation

Our results provide actionable insights for select-
ing and effectively using teacher models in mul-
tilingual synthetic data generation. First, we find
that model scale does not significantly predict
teacher effectiveness: Llama 3.1 70B Instruct, de-
spite being the largest model evaluated, ranks at
the bottom half in PG-SCORE across all student
base models we tested (§3.1, §3.2). Our analyses
suggest that what matters instead is the quality of
generated data: prompt diversity, response fluency,
and length collectively capture over 93% of the
variance in intrinsic data quality and predict stu-
dent performance with R2=0.664 (§4.2), offering
practitioners a cheaper alternative to full student
training runs for screening teacher candidates.

---

<!-- PAGE 8 -->

Second, when the optimal teacher is unknown,
matching model families offers a reliable heuris-
tic for teacher selection. Gemma teachers paired
with Gemma students, and Llama teachers with
Llama students, outperform a mismatched baseline
by at least 20% (Figure 2). We hypothesize this
finding reflects shared tokenization and similar pre-
training distributions, though disentangling these
factors remains future work.

Finally, we find that there are language-
dependent considerations for data generation.
For high-resource languages like German, where
seed data quality is high, the Generate method
performs best. For less-resourced languages like
Arabic and Indonesian, methods that leverage ex-
isting prompts (Respond) or transfer from English
(Translate) can yield substantial gains over a uni-
form mix of methods, though the magnitude varies
by teacher (Table 2). For truly low-resource lan-
guages, we recommend combining synthetic data
generation with targeted data collection.

As a supplementary, we demonstrate the applica-
bility of our findings by building a multilingual syn-
thetic data recipe for a held-out language, Tagalog,
in Appendix I. We show that models trained using
our recipe (based on analyses from PG-SCORE)
have better performance on an unseen Filipino-
centric benchmark, and that each component of
our recommendation (e.g., choose top teacher from
Table 1, match model families, etc.) resulted in ob-
servable performance gains. This suggests that our
evaluation protocol is robust that the insights trans-
fer to an unseen language, even when measured
with a different set of downstream metrics.

6 Related Work

Synthetic Data Generation for Multilingual SFT
In order to offset the high costs of recruiting lan-
guage experts for data collection, prior works re-
lied on generating synthetic datasets. This ef-
fort resulted in large multilingual datasets such as
Bactrian-X (Translate, Li et al., 2023), MultiAl-
paca (Generate, Wei et al., 2023), and xP3 (Re-
spond, Muennighoff et al., 2023) that were created
through various data generation methods. These
works have different data generation recipes, and
so we provide a brief survey of these works and
their recipes in Appendix A, then classify them
across the three strategies / archetypes (Generate,
Translate, Response; 2.2). Building on these prior
efforts, we examine the three core strategies for

multilingual synthetic data generation, distill them
into three strategies, and test each in isolation.
This setup enabled us to provide practitioners with
empirically-grounded recipe on selecting teacher
LMs that we hope to be applicable across any gen-
eration method.

⊕

Evaluating and Improving the Synthetic Data
Pipeline While prior works have evaluated as-
pects of the synthetic data pipeline, they typically
do so in isolation (i.e., intrinsic
extrinsic) or fo-
cus exclusively on English (Zhang et al., 2025a).
For instance, Kim et al. (2025) evaluated teacher
models solely as a function of extrinsic student
performance on English tasks (e.g., reasoning and
coding), while Cai et al. (2025)’s OpenDataArena
focuses on intrinsic data quality (model-based and
heuristic) to score models. Signals of multilingual
data quality are often a function of corpus-level
diversity (Artetxe and Schwenk, 2019; Enevoldsen
et al., 2025; Sam et al., 2025) and generation qual-
ity (Pombal et al., 2025; Anugraha et al., 2026) On
the other hand, multilingual LMs are typically eval-
uated on general-knowledge and culture-specific
benchmarks (Qin et al., 2025; Gemma Team et al.,
2025; Salamanca et al., 2026, inter alia). These
practices informed our choice of intrinsic and ex-
trinsic metrics throughout this work. More im-
portantly, PG-SCORE provides a holistic analysis
that combines both intrinsic data quality and extrin-
sic student downstream performance to evaluate
teacher models across various generation methods.

7 Conclusion

We conduct a comprehensive evaluation of state-of-
the-art LMs as multilingual teachers for synthetic
data generation by assessing both intrinsic data
quality and extrinsic student model performance.
We find several properties that contribute to teacher
effectiveness outside of model size or benchmark
performance, such as prompt-response diversity,
fluency, and language representation. Finally, we
outline practical recommendations for creating a
multilingual synthetic data generation recipe. We
hope our findings guide future work on develop-
ing inclusive language technologies through high-
quality synthetic data.

Limitations

Our work comes with some limitations and open
questions left for future work. For example, our
language set encompasses six languages. Although

8

---

<!-- PAGE 9 -->

we chose these languages carefully based on (1)
whether they can be evaluated on publicly-available
LM benchmarks and (2) prior theoretical work on
principled test language selection (Ploeger et al.,
2026), validating our findings across a broader lan-
guage sample remains important future work. In
addition, our Translate data generation method as-
sumes access to English prompts that can be mean-
ingfully translated to target languages. This ap-
proach inherits limitations from LM-based tech-
niques such as localizing culture-specific refer-
ences, introducing translationese artifacts.

Ethics Statement

Synthetic data generation risks amplifying biases
present in teacher models. If a teacher model under-
performs on certain languages or exhibits cultural
biases, these weaknesses propagate to student mod-
els trained on its outputs. Our finding that teacher
effectiveness correlates with CommonCrawl repre-
sentation (ρ = 0.886, based on six languages) sug-
gests that already underrepresented languages may
be further disadvantaged in synthetic data pipelines,
potentially widening the performance gap between
high- and low-resource languages.

Acknowledgments

LJVM and AK acknowledge the support of the
UKRI Frontier Grant EP/Y031350/1 (EQUATE).
This work was performed using joint resources pro-
vided by the Cambridge Service for Data Driven
Discovery (CSD3) EP/T022159/1, Isambard AI Na-
tional AI Research Resource (AIRR) ST/AIRR/I-A-
I/1023, and the Microsoft Research Grant. LJVM
would also like to thank Songbo Hu, Chen Cecilia
Liu, Millicent Ochieng, and Felermino Ali for help-
ful and productive discussions on the project.

References

Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr
Stanczyk, Sabela Ramos Garea, Matthieu Geist, and
Olivier Bachem. 2024. On-Policy Distillation of
Language Models: Learning from Self-Generated
Mistakes. In The Twelfth International Conference
on Learning Representations.

Sanchit Ahuja, Kumar Tanmay, Hardik Hansrajbhai
Chauhan, Barun Patra, Kriti Aggarwal, Luciano Del
Corro, Arindam Mitra, Tejas Indulal Dhamecha,
Ahmed Hassan Awadallah, Monojit Choudhury,
Vishrav Chaudhary, and Sunayana Sitaram. 2025.
sPhinX: Sample Efficient Multilingual Instruction
Fine-Tuning Through N-shot Guided Prompting. In

Proceedings of the Fourth Workshop on Generation,
Evaluation and Metrics (GEM²), pages 927–946, Vi-
enna, Austria and virtual meeting. Association for
Computational Linguistics.

Anthropic. 2024. The Claude 3 Model Family: Opus,

Sonnet, Haiku. Technical report, Anthropic.

David Anugraha, Shou-Yi Hung, Zilu Tang, En-
Shiun Annie Lee, Derry Tanti Wijaya, and Genta In-
dra Winata. 2026. mR3: Multilingual Rubric-
Agnostic Reward Reasoning Models. In The Four-
teenth International Conference on Learning Repre-
sentations.

Mikel Artetxe and Holger Schwenk. 2019. Margin-
based Parallel Corpus Mining with Multilingual Sen-
tence Embeddings. In Proceedings of the 57th An-
nual Meeting of the Association for Computational
Linguistics, pages 3197–3203, Florence, Italy. Asso-
ciation for Computational Linguistics.

Viraat Aryabumi,

John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Jon Ander Campos,
Yi Chern Tan, Kelly Marchisio, Max Bartolo, Se-
bastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick
Frosst, Aidan Gomez, Phil Blunsom, Marzieh Fadaee,
and 2 others. 2024. Aya 23: Open Weight Re-
leases to Further Multilingual Progress. Preprint,
arXiv:2405.15032.

Yauhen Babakhin, Radek Osmulski, Ronay Ak, Gabriel
Moreira, Mengyao Xu, Benedikt Schifferer, Bo Liu,
and Even Oldridge. 2025. Llama-Embed-Nemotron-
8B: A Universal Text Embedding Model for Mul-
Preprint,
tilingual and Cross-Lingual Tasks.
arXiv:2511.07025.

Nicolas Boizard, Kevin El Haddad, Celine Hudelot, and
Pierre Colombo. 2025. Towards Cross-Tokenizer
Distillation: the Universal Logit Distillation Loss for
LLMs. Transactions on Machine Learning Research.

Samuel Cahyawijaya, Holy Lovenia, Fajri Koto, Rifki
Putri, Wawan Cenggoro, Jhonson Lee, Salsabil Ak-
bar, Emmanuel Dave, Nuurshadieq Nuurshadieq,
Muhammad Mahendra, Rr Putri, Bryan Wilie, Genta
Winata, Alham Aji, Ayu Purwarianti, and Pascale
Fung. 2024. Cendol: Open instruction-tuned genera-
tive large language models for Indonesian languages.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1:
Long Papers), pages 14899–14914, Bangkok, Thai-
land. Association for Computational Linguistics.

Mengzhang Cai, Xin Gao, Yu Li, Honglin Lin,
Zheng Liu, Zhuoshi Pan, Qizhi Pei, Xiaoran Shang,
Mengyuan Sun, Zinan Tang, Xiaoyang Wang, Zhan-
ping Zhong, Yun Zhu, Dahua Lin, Conghui He,
and Lijun Wu. 2025. OpenDataArena: A Fair and
Open Arena for Benchmarking Post-Training Dataset
Value. Preprint, arXiv:2512.14051.

Hao Chen, Abdul Waheed, Xiang Li, Yidong Wang,
Jindong Wang, Bhiksha Raj, and Marah I. Abdin.

9

---

<!-- PAGE 10 -->

2024. On the Diversity of Synthetic Data and its Im-
pact on Training Large Language Models. Preprint,
arXiv:2410.15226.

Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training Verifiers to Solve Math Word Prob-
lems. Preprint, arXiv:2110.14168.

Cohere Team, Aakanksha, Arash Ahmadian, Marwan
Ahmed, Jay Alammar, Milad Alizadeh, Yazeed Al-
numay, Sophia Althammer, Arkady Arkhangorodsky,
Viraat Aryabumi, Dennis Aumiller, Raphaël Avalos,
Zahara Aviv, Sammie Bae, Saurabh Baji, Alexan-
dre Barbet, Max Bartolo, Björn Bebensee, Neeral
Beladia, and 210 others. 2025. Command A: An
Enterprise-Ready Large Language Model. Preprint,
arXiv:2504.00698.

John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, Sandra Kublik, Meor Amer, Viraat
Aryabumi, Jon Ander Campos, Yi-Chern Tan, Tom
Kocmi, Florian Strub, Nathan Grinsztajn, Yannis Flet-
Berliac, and 26 others. 2024. Aya Expanse: Combin-
ing Research Breakthroughs for a New Multilingual
Frontier. Preprint, arXiv:2412.04261.

Kenneth Enevoldsen, Isaac Chung, Imene Kerboua,
Márton Kardos, Ashwin Mathur, David Stap,
Jay Gala, Wissam Siblini, Dominik Krzemi´nski,
Genta Indra Winata, Saba Sturua, Saiteja Utpala,
Mathieu Ciancone, Marion Schaeffer, Diganta Misra,
Shreeya Dhakal, Jonathan Rystrøm, Roman Solo-
matin, Ömer Veysel Ça˘gatan, and 63 others. 2025.
MMTEB: Massive Multilingual Text Embedding
Benchmark. In The Thirteenth International Con-
ference on Learning Representations.

Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya
Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin,
Tatiana Matejovicova, Alexandre Ramé, Morgane
Rivière, Louis Rouillard, Thomas Mesnard, Geoffrey
Cideron, Jean bastien Grill, Sabela Ramos, Edouard
Yvinec, Michelle Casbon, Etienne Pot, Ivo Penchev,
and 197 others. 2025. Gemma 3 Technical Report.
Preprint, arXiv:2503.19786.

Granite Team, IBM. 2025. Granite 4.0 Language Mod-
https://huggingface.co/collections/

els.
ibm-granite/granite-40-language-models.
Accessed: 2025-12-08.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The Llama 3 Herd
of Models. Preprint, arXiv:2407.21783.

Srishti Gureja, Lester

James Validad Miranda,
Shayekh Bin Islam, Rishabh Maheshwary, Drishti
Sharma, Gusti Triandi Winata, Nathan Lambert, Se-
bastian Ruder, Sara Hooker, and Marzieh Fadaee.
2025. M-RewardBench: Evaluating Reward Models
in Multilingual Settings. In Proceedings of the 63rd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 43–58,
Vienna, Austria. Association for Computational Lin-
guistics.

Nathan Habib, Clémentine Fourrier, Hynek Kydlíˇcek,
Thomas Wolf, and Lewis Tunstall. 2023. LightEval:
A lightweight framework for LLM evaluation.

Hasan Abed Al Kader Hammoud, Mohamad Bilal Zbib,
and Bernard Ghanem. 2026. Hala Technical Report
Building Arabic-Centric Instruction & Translation
Models at Scale. In Proceedings of the 2nd Workshop
on NLP for Languages Using Arabic Script, pages
236–244, Rabat, Morocco. Association for Computa-
tional Linguistics.

Daniel Han, Michael Han, and Unsloth Team. 2023.

Unsloth.

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring Massive Multitask Language Un-
derstanding. In International Conference on Learn-
ing Representations.

Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020. The State and
Fate of Linguistic Diversity and Inclusion in the NLP
World. In Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics, pages
6282–6293, Online. Association for Computational
Linguistics.

Armand Joulin, Edouard Grave, Piotr Bojanowski,
Matthijs Douze, Hérve Jégou, and Tomas Mikolov.
2016. FastText.zip: Compressing text classification
models. Preprint, arXiv:1612.03651.

Armand Joulin, Edouard Grave, Piotr Bojanowski, and
Tomas Mikolov. 2017. Bag of Tricks for Efficient
Text Classification. In Proceedings of the 15th Con-
ference of the European Chapter of the Association
for Computational Linguistics: Volume 2, Short Pa-
pers, pages 427–431, Valencia, Spain. Association
for Computational Linguistics.

Shivani Kapania, Stephanie Ballard, Alex Kessler, and
Jennifer Wortman Vaughan. 2025. Examining the
Expanding Role of Synthetic Data Throughout the
AI Development Pipeline. In Proceedings of the 2025
ACM Conference on Fairness, Accountability, and
Transparency, FAccT ’25, pages 45–60, New York,
NY, USA. Association for Computing Machinery.

Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B.
Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models. Preprint,
arXiv:2001.08361.

10

---

<!-- PAGE 11 -->

Seungone Kim, Juyoung Suk, Xiang Yue, Vijay
Viswanathan, Seongyun Lee, Yizhong Wang, Kiril
Gashteovski, Carolin Lawrence, Sean Welleck, and
Graham Neubig. 2025. Evaluating language models
as synthetic data generators. In Proceedings of the
63rd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
6385–6403, Vienna, Austria. Association for Compu-
tational Linguistics.

Yoon Kim and Alexander M. Rush. 2016. Sequence-
level knowledge distillation. In Proceedings of the
2016 Conference on Empirical Methods in Natu-
ral Language Processing, pages 1317–1327, Austin,
Texas. Association for Computational Linguistics.

Anoop Kunchukuttan, Raj Dabre, Rudra Murthy, Mo-
hammed Safi Ur Rahman Khan, and Thanmay
Jayakumar. 2025. Data and Model Centric Ap-
proaches for Expansion of Large Language Models
to New languages. In Proceedings of the 2025 Con-
ference on Empirical Methods in Natural Language
Processing: Tutorial Abstracts, pages 12–13, Suzhou,
China. Association for Computational Linguistics.

Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Ef-
ficient Memory Management for Large Language
Model Serving with PagedAttention. In Proceedings
of the ACM SIGOPS 29th Symposium on Operating
Systems Principles.

Nathan Lambert, Jacob Morrison, Valentina Pyatkin,
Shengyi Huang, Hamish Ivison, Faeze Brahman,
Lester James Validad Miranda, Alisa Liu, Nouha
Dziri, Xinxi Lyu, Yuling Gu, Saumya Malik, Victoria
Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le
Bras, Oyvind Tafjord, Christopher Wilhelm, Luca
Soldaini, and 4 others. 2025. Tulu 3: Pushing Fron-
tiers in Open Language Model Post-Training.
In
Second Conference on Language Modeling.

Haonan Li, Fajri Koto, Minghao Wu, Alham Fikri Aji,
and Timothy Baldwin. 2023. Bactrian-X: Multilin-
gual replicable instruction-following models with
low-rank adaptation. Preprint, arXiv:2305.15011.

Yuetai Li, Xiang Yue, Zhangchen Xu, Fengqing Jiang,
Luyao Niu, Bill Yuchen Lin, Bhaskar Ramasubrama-
nian, and Radha Poovendran. 2025. Small Models
Struggle to Learn from Strong Reasoners. In Find-
ings of the Association for Computational Linguistics:
ACL 2025, pages 25366–25394, Vienna, Austria. As-
sociation for Computational Linguistics.

Ryan Marten, Trung Vu, Charlie Cheng-Jie Ji, Kartik
Sharma, Shreyas Pimpalgaonkar, Alex Dimakis, and
Maheswaran Sathiamoorthy. 2025. Curator: A Tool
for Synthetic Data Creation. https://github.com/
bespokelabsai/curator.

Pedro Henrique Martins, João Alves, Patrick Fernan-
des, Nuno M. Guerreiro, Ricardo Rei, Amin Fara-
jian, Mateusz Klimaszewski, Duarte M. Alves, José

Pombal, Nicolas Boizard, Manuel Faysse, Pierre
Colombo, François Yvon, Barry Haddow, José G. C.
de Souza, Alexandra Birch, and André F. T. Martins.
2025. EuroLLM-9B: Technical Report. Preprint,
arXiv:2506.04079.

Pedro Henrique Martins, Patrick Fernandes, João Alves,
Nuno M. Guerreiro, Ricardo Rei, Duarte M. Alves,
José Pombal, Amin Farajian, Manuel Faysse, Ma-
teusz Klimaszewski, Pierre Colombo, Barry Haddow,
José G. C. de Souza, Alexandra Birch, and André F. T.
Martins. 2024. EuroLLM: Multilingual Language
Models for Europe. Preprint, arXiv:2409.16235.

Lester James Validad Miranda, Elyanah Aco, Conner G.
Manuel, Jan Christian Blaise Cruz, and Joseph Mar-
vin Imperial. 2025. FilBench: Can LLMs Under-
In Proceedings of
stand and Generate Filipino?
the 2025 Conference on Empirical Methods in Natu-
ral Language Processing, pages 2496–2529, Suzhou,
China. Association for Computational Linguistics.

Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng Xin Yong, Hai-
ley Schoelkopf, Xiangru Tang, Dragomir Radev,
Alham Fikri Aji, Khalid Almubarak, Samuel Al-
banie, Zaid Alyafeai, Albert Webson, Edward Raff,
and Colin Raffel. 2023. Crosslingual Generaliza-
tion through Multitask Finetuning. In Proceedings
of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 15991–16111, Toronto, Canada. Association
for Computational Linguistics.

Raymond Ng, Thanh Ngan Nguyen, Huang Yuli,
Tai Ngee Chia, Leong Wai Yi, Wei Qi Leong, Xianbin
Yong, Jian Gang Ngui, Yosephine Susanto, Nicholas
Cheng, Hamsawardhini Rengarajan, Peerat Limkon-
chotiwat, Adithya Venkatadri Hulagadri, Kok Wai
Teng, Yeo Yeow Tong, Bryan Siow, Wei Yi Teo,
Tan Choon Meng, Brandon Ong, and 11 others. 2025.
SEA-LION: Southeast Asian Languages in One Net-
work. In Proceedings of the 14th International Joint
Conference on Natural Language Processing and
the 4th Conference of the Asia-Pacific Chapter of
the Association for Computational Linguistics, pages
512–526, Mumbai, India. The Asian Federation of
Natural Language Processing and The Association
for Computational Linguistics.

NLLB Team, Marta R. Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Hef-
fernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Barrault,
Gabriel Mejia Gonzalez, Prangthip Hansanti, and
20 others. 2022. No language left behind: Scal-
ing human-centered machine translation. Preprint,
arXiv:2207.04672.

OLMo Team, Allyson Ettinger, Amanda Bertsch, Bailey
Kuehl, David Graham, David Heineman, Dirk Groen-
eveld, Faeze Brahman, Finbarr Timbers, Hamish
Ivison, Jacob Morrison, Jake Poznanski, Kyle Lo,

11

---

<!-- PAGE 12 -->

Luca Soldaini, Matt Jordan, Mayee Chen, Michael
Noukhovitch, Nathan Lambert, Pete Walsh, and 49
others. 2025. OLMo 3. Technical report, Allen Insti-
tute for AI. Technical Report.

OpenAI, Aaron Hurst, Adam Lerer, Adam P. Goucher,
Adam Perelman, Aditya Ramesh, Aidan Clark,
AJ Ostrow, Akila Welihinda, Alan Hayes, Alec
Radford, Aleksander M ˛adry, Alex Baker-Whitcomb,
Alex Beutel, Alex Borzunov, Alex Carney, Alex
Chow, Alex Kirillov, Alex Nichol, and 400 oth-
Preprint,
ers. 2024.
GPT-4o System Card.
arXiv:2410.21276.

Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Gray, John
Schulman, Jacob Hilton, Fraser Kelton, Luke Miller,
Maddie Simens, Amanda Askell, Peter Welinder,
Paul Christiano, Jan Leike, and Ryan Lowe. 2022.
Training language models to follow instructions with
human feedback. In Advances in Neural Information
Processing Systems.

Parinthapat Pengpun, Can Udomcharoenchaikit, Weer-
ayut Buaphet, and Peerat Limkonchotiwat. 2024.
Seed-free synthetic data generation framework for
instruction-tuning LLMs: A case study in Thai. In
Proceedings of the 62nd Annual Meeting of the Asso-
ciation for Computational Linguistics (Volume 4: Stu-
dent Research Workshop), pages 445–464, Bangkok,
Thailand. Association for Computational Linguistics.

Esther Ploeger, Wessel Poelman, Andreas Holck Høeg-
Petersen, Anders Schlichtkrull, Miryam de Lhoneux,
and Johannes Bjerva. 2026. A principled framework
for evaluating on typologically diverse languages.
Computational Linguistics, pages 1–33.

José Pombal, Dongkeun Yoon, Patrick Fernandes, Ian
Wu, Seungone Kim, Ricardo Rei, Graham Neubig,
and Andre Martins. 2025. M-Prometheus: A Suite
of Open Multilingual LLM Judges. In Second Con-
ference on Language Modeling.

Libo Qin, Qiguang Chen, Yuhang Zhou, Zhi Chen,
Yinghui Li, Lizi Liao, Min Li, Wanxiang Che, and
Philip S. Yu. 2025. A survey of multilingual large
language models. Patterns, 6(1):101118.

Neel Prabhanjan Rachamalla, Aravind Konakalla, Gau-
tam Rajeev, Ashish Kulkarni, Chandra Khatri, and
Shubham Agarwal. 2025. Pragyaan: Designing
and Curating High-Quality Cultural Post-Training
Datasets for Indian Languages. In Proceedings of the
5th Workshop on Multilingual Representation Learn-
ing (MRL 2025), pages 285–321, Suzhuo, China. As-
sociation for Computational Linguistics.

Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J. Liu. 2020. Exploring the limits
of transfer learning with a unified text-to-text trans-
former. J. Mach. Learn. Res., 21(1).

Allan Raventos, Mansheej Paul, Feng Chen, and Surya
Ganguli. 2023. Pretraining task diversity and the
emergence of non-Bayesian in-context learning for
regression. In Thirty-seventh Conference on Neural
Information Processing Systems.

Alejandro R. Salamanca, Diana Abagyan, Daniel
D’souza, Ammar Khairi, David Mora, Saurabh Dash,
Viraat Aryabumi, Sara Rajaee, Mehrnaz Mofakhami,
Ananya Sahu, Thomas Euyang, Brittawnya Prince,
Madeline Smith, Hangyu Lin, Acyr Locatelli, Sara
Hooker, Tom Kocmi, Aidan Gomez, Ivan Zhang, and
7 others. 2026. Tiny Aya: Bridging Scale and Multi-
lingual Depth. Preprint, arXiv:2603.11510.

Dylan Sam, Ayan Chakrabarti, Afshin Rostamizadeh,
Srikumar Ramalingam, Gui Citovsky, and Sanjiv Ku-
mar. 2025. Analyzing Similarity Metrics for Data
Selection for Language Model Pretraining. In The
Thirty-ninth Annual Conference on Neural Informa-
tion Processing Systems.

Muhammad Ali Shafique, Kanwal Mehreen, Muham-
mad Arham, Maaz Amjad, Sabur Butt, and Hamza
Farooq. 2025. Alif: Advancing Urdu Large Lan-
guage Models via Multilingual Synthetic Data Dis-
In Proceedings of the 5th Workshop on
tillation.
Multilingual Representation Learning (MRL 2025),
pages 271–284, Suzhuo, China. Association for Com-
putational Linguistics.

Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das,
and Jason Wei. 2023. Language models are multi-
lingual chain-of-thought reasoners. In The Eleventh
International Conference on Learning Representa-
tions.

Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David Ifeoluwa Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Sebastian Ruder, Wei-Yin
Ko, Antoine Bosselut, Alice Oh, Andre Martins,
Leshem Choshen, Daphne Ippolito, and 4 others.
2025. Global MMLU: Understanding and Address-
ing Cultural and Linguistic Biases in Multilingual
Evaluation. In Proceedings of the 63rd Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 18761–18799, Vi-
enna, Austria. Association for Computational Lin-
guistics.

Shivalika Singh, Freddie Vargus, Daniel D’souza,
Börje F. Karlsson, Abinaya Mahendiran, Wei-Yin
Ko, Herumb Shandilya, Jay Patel, Deividas Mataci-
unas, Laura O’Mahony, Mike Zhang, Ramith Het-
tiarachchi, Joseph Wilson, Marina Machado, Luisa
Moura, Dominik Krzemi´nski, Hakimeh Fadaei, Irem
Ergun, Ifeoma Okoh, and 14 others. 2024. Aya
Dataset: An Open-Access Collection for Multilin-
gual Instruction Tuning. In Proceedings of the 62nd
Annual Meeting of the Association for Computational

12

---

<!-- PAGE 13 -->

Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang,
Xiaofei Sun, Shuhe Wang, Jiwei Li, Runyi Hu, Tian-
wei Zhang, Fei Wu, and Guoyin Wang. 2025b. In-
struction Tuning for Large Language Models: A Sur-
vey. Preprint, arXiv:2308.10792.

Wenting Zhao, Xiang Ren, Jack Hessel, Claire Cardie,
Yejin Choi, and Yuntian Deng. 2024. WildChat:
1M ChatGPT Interaction Logs in the Wild. In The
Twelfth International Conference on Learning Repre-
sentations.

Alan Zhu, Parth Asawa, Jared Quincy Davis, Lingjiao
Chen, Boris Hanin, Ion Stoica, Joseph E. Gonzalez,
and Matei Zaharia. 2025. BARE: Leveraging Base
Language Models for Few-Shot Synthetic Data Gen-
eration. Preprint, arXiv:2502.01697.

Linguistics (Volume 1: Long Papers), pages 11521–
11567, Bangkok, Thailand. Association for Compu-
tational Linguistics.

Bibek Upadhayay and Vahid Behzadan. 2024. TaCo:
Enhancing Cross-Lingual Transfer for Low-Resource
Languages in LLMs through Translation-Assisted
Chain-of-Thought Processes. In 5th Workshop on
practical ML for limited/low resource settings.

Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa
Liu, Noah A. Smith, Daniel Khashabi, and Hannaneh
Hajishirzi. 2023. Self-instruct: Aligning language
models with self-generated instructions. In Proceed-
ings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 13484–13508, Toronto, Canada. Association
for Computational Linguistics.

Zhilin Wang, Jiaqi Zeng, Olivier Delalleau, Daniel
Egert, Ellie Evans, Hoo-Chang Shin, Felipe Soares,
Yi Dong, and Oleksii Kuchaiev. 2025. Help-
Steer3: Human-Annotated Feedback and Edit Data
to Empower Inference-Time Scaling in Open-Ended
General-Domain Tasks. Preprint, arXiv:2503.04378.

Xiangpeng Wei, Haoran Wei, Huan Lin, Tianhao Li,
Pei Zhang, Xingzhang Ren, Mei Li, Yu Wan, Zhi-
wei Cao, Binbin Xie, Tianxiang Hu, Shangjie Li,
Binyuan Hui, Bowen Yu, Dayiheng Liu, Baosong
Yang, Fei Huang, and Jun Xie. 2023. PolyLM:
An Open Source Polyglot Large Language Model.
Preprint, arXiv:2307.06018.

Zhangchen Xu, Fengqing Jiang, Luyao Niu, Yun-
tian Deng, Radha Poovendran, Yejin Choi, and
Bill Yuchen Lin. 2025a. Magpie: Alignment data
synthesis from scratch by prompting aligned LLMs
with nothing. In The Thirteenth International Con-
ference on Learning Representations.

Zhangchen Xu, Fengqing Jiang, Luyao Niu, Bill Yuchen
Lin, and Radha Poovendran. 2025b. Stronger mod-
els are not always stronger teachers for instruction
tuning. In Proceedings of the 2025 Conference of the
Nations of the Americas Chapter of the Association
for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), pages 4392–
4405, Albuquerque, New Mexico. Association for
Computational Linguistics.

An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025. Qwen3 Technical Report. Preprint,
arXiv:2505.09388.

Hengyuan Zhang, Shiping Yang, Xiao Liang, Chen-
ming Shang, Yuxuan Jiang, Chaofan Tao, Jing
Xiong, Hayden Kwok-Hay So, Ruobing Xie, An-
gel X. Chang, and Ngai Wong. 2025a. Find Your
Optimal Teacher: Personalized Data Synthesis via
Router-Guided Multi-Teacher Distillation. Preprint,
arXiv:2510.10925.

13

---

<!-- PAGE 14 -->

16

16

16

16

16
16
16

16

17
17
18
18
19
21

21

21
22
23
23

25

Appendix

A Multilingual Synthetic Data Generation

B Seed Dataset Statistics

C The POLYGLOT Collection

D Teacher Model and Target Language Details

E Experimental Details

E.1 Supervised Finetuning .
.
E.2 Model Evaluation .

.

.

.
.

.
.

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

F Full Results for Intr. and Extr. Metrics

G Additional Experiments and Ablations

G.1 Effect of Data Scale on Student Model Performance . . . . . . . . . . . . . . . . . . . .
G.2 Generalization Across Model Size . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
G.3 Effect of Translation Method (Prompting an LM vs. Translation Model) . . . . . . . . .
G.4 Weighing of Intrinsic and Extrinsic Metrics in PG-SCORE . . . . . . . . . . . . . . . .
G.5 Effect of language resource levels on PG-SCORE . . . . . . . . . . . . . . . . . . . . .

H Disclosure on the Use of LLMs

I Multilingual Synthetic Data Recipe: Case Study on Tagalog

I.1
I.2 Results: Leaderboard Scores and Ablations
I.3 Analysis: Ablation Experiments

Setup: Recipe Design and Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

J

Inference Details

14

---

<!-- PAGE 15 -->

Dataset

Language(s)

Generation Method / Description

Bactrian-X (Li et al., 2023)

MultiAlpaca (Wei et al., 2023)

52 languages - Arabic, Indonesian, Chi-
nese, Malaysian, Tamil, Tagalog, etc.

18 languages - English, Chinese, Rus-
sian, Spanish, German, French, etc.

xP3-MT (Muennighoff et al., 2023)

46 languages - Arabic, English, Span-
ish, Hindi, Chinese, Indonesian, etc.

Cendol (Cahyawijaya et al., 2024)

Seed Free Thai (Pengpun et al., 2024)

18 Indonesian languages - Sundanese,
Javanese, Acehnese, Banjarese, Bugi-
nese, Gorontalo, etc.
Thai

Aya Dataset and Collection (Singh et al.,
2024)

114 languages - Arabic, French, Hindi,
Indonesian, Japanese, Spanish, Swahili,
Turkish, Yoruba, Filipino, etc.

sPhinX (Ahuja et al., 2025)

EuroBlocks (Martins et al., 2025, 2024)

51 languages - Afrikaan, Arabic, Ben-
gali, Bulgarian, Burmese, Chinese,
Croatian, Czech, etc.
31 languages - English, Chinese, Span-
ish,
Italian, French, German, Por-
tuguese, Dutch, Polish, etc.

SEA-LION Dataset (Ng et al., 2025)

11 languages - English, Chinese, In-
donesian, Vietnamese, Malay, Thai,
Burmese, Lao, Filipino, Khmer, and
Tamil

Urdu-Instruct Dataset (Shafique et al.,
2025)

Urdu

Pragyaan (Rachamalla et al., 2025)

10 Indian languages - Gujarati, Kan-
nada, Marathi, Bengali, Odia, Tamil,
Malayalam, Telugu, Punjabi, Hindi,
and Sanskrit

Translate - used Google Translate API
to translate English instructions from
Alpaca (52K) and Dolly (15K).
Generate, Translate - used a multilin-
gual self-instruct (Wang et al., 2023)
method from English prompt-response
pairs to perform translation.
Translate, Respond - used Google
Translate API
to translate English
prompt-response pairs from differ-
in addition to creating
ent sources,
template-based prompts where an LM
responds to it.
Translate, Respond - curated various
prompts from past Indonesian NLP
tasks, including translations of Dolly.
Generate - generated synthetic instruc-
tion data without seed examples by us-
ing Wikipedia contexts. Identifies flu-
ency, diversity, and cultural context as
key properties.
Translate, Respond - involves a collec-
tion of translated prompts from English,
and templated prompts. A sizeable por-
tion of the collection includes native-
speaker annotations.
Translate - selectively translates essen-
tial portions of multilingual inputs in or-
der to semantically preserve meaning.
Generate, Translate - prompted Llama
3 or an earlier EuroLLM checkpoint
with a document, target language, and
category, then asking it to generate an
instruction. Also involved translating
prompt-response pairs.
Generate, Translate - for the majority
of the datasets, samples were first gener-
ated into English using Qwen 32B, and
then translated into the target language
using Gemma 2 27B.
Generate - uses a modified Self-Instruct
from a pool of culturally relevant
prompts.
Generate, Translate - perform transla-
tion using an LM for a subset of data.
Used Self-Instruct from a pool of native
prompts for another subset of data.

Table 5: Short survey of related work on synthetic data generation for multilingual LMs. For each work, we
provide a brief description of their data generation method. We find that most methods fall into one of the three
categories described in §2.2, i.e., Generate, Translate, or Respond, which we tested in our experiments.

15

---

<!-- PAGE 16 -->

A Multilingual Synthetic Data

Generation

We present an overview of prior works in Table 5
that used synthetic data to train multilingual LMs.
In general, we find that most data generation meth-
ods fall into one of the three categories described in
§2.2, i.e., Generate, Translate, or Respond, which
we tested in our experiments. Our survey suggests
that our choice of data generation methods are
grounded in prior work and covers the majority
of approaches used in synthetic data generation.

B Seed Dataset Statistics

Table 6 shows the statistics of the seed dataset used
for synthetic data generation.

C The POLYGLOT Collection

In order to facilitate future research on multilingual
synthetic data generation, we introduce the POLY-
GLOT collection, a collection of synthetic datasets
and student models generated by the best teacher
model across all target languages. The POLYGLOT
collection includes:
• POLYGLOT-INSTRUCTIONS-SYNTH: Synthetic
datasets for each target language generated by
each teacher model using all three data genera-
tion methods (§2.2).

• POLYGLOT-GEMMA-SFT: A set of 8B student
models finetuned on each synthetic dataset from
the OLMo 3 7B base model using the Gemma
3 27B (highest-scoring model) teacher.
We publicly release the POLYGLOT Collection

in HuggingFace.3

D Teacher Model and Target Language

Details

In this section, we provide additional details about
the teacher models and target languages used in
our experiments. Table 7 summarizes the key char-
acteristics of each teacher model. On the other
hand, Table 8 provides information about the target
languages, including language family, number of
speakers, and resource availability.

E Experimental Details

E.1 Supervised Finetuning

Table 9 summarizes the hyperparameters used for
finetuning student models. We train models using

3

: ljvmiranda921/polyglot-teachers

the Unsloth framework (Han et al., 2023) using a
cluster of Grace Hopper GH200 Superchips. Full
finetuning (7B) takes around 1.5 hours (wall clock)
for 2 epochs and 2 nodes.

Hyperparameter

Value Hyperparameter

Value

Learning rate
Epochs
Max seq. length
Optimizer

5e-5 Batch size

2 Grad. Acum. Steps

16,384 Weight decay

AdamW Scheduler

32
4
0.001
Linear

Table 9: Hyperparameters for finetuning a 7B student
model from OLMo 3 7B.

E.2 Model Evaluation

We used the Lighteval framework (v0.13.1dev0,
Habib et al., 2023) for evaluation. Table 10 summa-
rizes the benchmarks used for evaluating student
models. We decided to use Global-MMLU Lite in-
stead of Global-MMLU becaue the former contains
actual native speaker annotations that localized the
benchmark into different cultural contexts.

Benchmark

Formulation Metric

N-shots

Global-MMLU Lite MCF
MCF
M-RewardBench
Generative
M-GSM

Accuracy
Weighted Acc.
Exact-Match

0
0
5

Table 10: Evaluation settings for each benchmark (MCF:
Multiple-Choice Formulation).

For Global-MMLU Lite and M-RewardBench,
we use the Multiple-Choice Formulation (MCF)
with character normalization. In addition, we also
follow the corpus-level metric in M-RewardBench
which uses a weighted accuracy for each data sub-
set and category (Gureja et al., 2025). For M-GSM,
we show 5 few-shot examples from the training set
in order for the model to properly generate the an-
swer. We run all evaluation experiments for three
trials with different random seeds and report the
average and standard deviation.

F Full Results for Intr. and Extr. Metrics

Table 11 shows all the data quality metrics for each
teacher model across all languages. Table 12 shows
the full results of student models finetuned on syn-
thetic datasets generated by each teacher model
across all target languages.

Percentage Increase Tables We provide addi-
tional tables from the main experiments in §3 and
§4. Table 14 shows the percentage increase in

16

---

<!-- PAGE 17 -->

Language

Source

English (en) Arabic (ar) Czech (cs) German (de) Spanish (es) Indonesian (id) Japanese (ja)

Aya Dataset
Tülu 3 SFT
WildChat 4.8M
CIDAR
Cendol v2
OpenAssistant 2
EuroBlocks SFT
GSM8k (train)
Helpsteer3 (chosen)
Magpie Pro Filtered

Total per language

-
10,000
10,000
-
-
-
-
7,473
-
10,000

30,743

-
-
4,660
6,000
-
23
-
-
-
-

5,000
-
1,266
-
-
4
3,813
-
-
-

10,683

10,083

241
-
5,908
-
-
2,328
12,551
-
462
-

21,490

3,854
-
5,900
-
-
8,785
15,641
-
778
-

34,958

2,786
-
7,983
-
3,000
3
-
-
156
-

6,259
-
602
-
-
306
2,893
-
534
-

13,928

10,594

Table 6: Seed dataset statistics. In order to bootstrap our synthetic data generation methods, we use a seed dataset
composed of various multilingual instruction-following datasets. We include English samples in order to simulate
data generation pipelines where English is translated into a target language. We collect a total of 132,929 seed
examples across 7 languages (including English).

Model Name

Provider

Size (B)

# Langs License

OpenAI
GPT-4o mini (OpenAI et al., 2024)
Meta
Llama 3.1 70B Instruct (Grattafiori et al., 2024)
Meta
Llama 3.1 8B Instruct (Grattafiori et al., 2024)
Cohere
Command A (Cohere Team et al., 2025)
Aya Expanse 32B (Dang et al., 2024)
Cohere
Gemma 3 27B Instruct (Gemma Team et al., 2025) Google
Gemma 3 12B Instruct (Gemma Team et al., 2025) Google
Google
Gemma 3 4B Instruct (Gemma Team et al., 2025)
IBM
IBM Granite 4.0 (Granite Team, IBM, 2025)
IBM
IBM Granite Micro (Granite Team, IBM, 2025)

–
70
8
104
32
27
12
4
3
0.4

50+
Proprietary
8
Llama 3.1
Llama 3.1
8
23 CC-BY-NC-4.0
23 CC-BY-NC-4.0

100+ Gemma
100+ Gemma
100+ Gemma

116 Apache 2.0
116 Apache 2.0

Table 7: Teacher model details. We evaluate 10 teacher models across different providers, sizes, multilingual
capabilities, and licensing terms. Size is reported in billions of parameters (B) where available. # Langs indicates
the number of languages the model was trained on or evaluated for.

PG-SCORE when using family-matched teacher-
student pairs compared to the OLMo 3 7B baseline
(see §3.2). Table 15 shows the percentage increase
in PG-SCORE when using the best data generation
method for each teacher-language pair compared
to an equal mix baseline (see §3.3).

G Additional Experiments and Ablations

In this section, we ablate several aspects of our eval-
uation protocol that may affect a teacher model’s
PG-SCORE.

G.1 Effect of Data Scale on Student Model

Performance

One component of PG-SCORE is the extrinsic stu-
dent performance metric (§2.3) as measured by
PGR. Scaling laws suggest that this performance
improves with more data (Kaplan et al., 2020).
Then, it is possible to inflate PG-SCORE by simply
using more synthetic data. In order to control for
this variable, we conduct an experiment to deter-

mine how much synthetic data is needed to reliably
compute PG-SCORE.

Setup We finetune an OLMo 3 7B base
model on n SFT instances where n
∈
1k, 5k, 10k, 25k, 50k
. To reduce computational
{
}
costs, we perform this experiment only on a single
teacher model (Gemma 3 27B Instruct) on three
target languages that represent diverse scripts and
resource availability: Arabic, German, and Indone-
sian. Similar to the main experiments, we represent
each data generation method equally when creating
the SFT datasets. Then, we recompute the intrinsic
metrics and finetune student models and measure
their performance across three benchmarks (§2.3).

Results Figure 5 shows the average student
model performance as a function of the number
of SFT instances. We observe that student per-
formance improves with more synthetic data, but
gains diminish beyond 10k examples. This finding
suggests that using 10k synthetic examples per

17

---

<!-- PAGE 18 -->

Language

Family

Script

Resource Availability % in CC

Arabic

Arabic
Czech
German
Spanish
Indonesian Austronesian
Japanese

Afro-Asiatic
Indo-European Latin
Indo-European Latin
Indo-European Latin
Latin
Japanese

Japonic

5 (High)
4 (Medium-High)
5 (High)
5 (High)
3 (Medium)
5 (High)

0.65%
0.99%
6.01%
4.37%
0.95%
5.20%

Table 8: Target language details. We evaluate teacher models across six typologically diverse languages spanning
different language families and scripts. Resource availability is based on the classification from Joshi et al. (2020),
ranging from 0 (lowest) to 5 (highest). CommonCrawl percentages (Raffel et al., 2020) indicate the proportion of
web text available for each language.

Instruct, Aya Expanse 32B, Llama 30B Instruct)
and all 6 target languages.

−

Results Table 16 shows the PG-SCORE scores
for three teacher models when using OLMo 3 32B
as the student model. We find that Gemma 3 27B
Instruct remains the highest-scoring teacher in
this comparison, achieving the highest average
PG-SCORE of 0.805 across all languages. This
result is consistent with our findings using the 8B
student model (§3), demonstrating that the supe-
rior data quality generated by Gemma 3 27B gen-
eralizes across model scales. Aya Expanse 32B
achieves a positive average PG-SCORE of 0.227,
while Llama 3.1 70B Instruct shows a negative
average of

0.267.

Furthermore, the language-dependent effects
observed in the 8B experiments remain consis-
tent at 32B scale. German continues to show the
highest PG-SCORE values across all three teach-
ers (2.389 for Gemma, 1.979 for Aya, 0.838 for
Llama), suggesting that certain languages bene-
fit more from synthetic data regardless of student
model size. Similarly, Spanish exhibits strong per-
formance across all teachers, with PG-SCORE val-
ues ranging from 1.353 to 1.855. In contrast, Ara-
bic shows the most variable results, with Gemma
0.239) while
achieving slightly negative scores (
Aya and Llama show substantially lower perfor-
mance (
1.688, respectively). Overall,
these findings demonstrate that PG-SCORE and
teacher model rankings generalize to the 32B pa-
rameter range.

0.872 and

−

−

−

G.3 Effect of Translation Method (Prompting

an LM vs. Translation Model)

An alternative to using an LM for translating texts
from English to a target language is via a translation

18

Figure 5: Effect of synthetic data scale on student
model performance. Student performance improves
with more synthetic data, but gains diminish beyond 10k
examples.

language is sufficient to reliably compute PG-
SCORE without inflating the metric by increas-
ing the number of samples. In our experiments,
we use 10k synthetic examples per language when
computing PG-SCORE. Specifically, we show that
10k synthetic examples from a strong teacher are
sufficient to finetune a student model to achieve rea-
sonable performance across multiple benchmarks.

G.2 Generalization Across Model Size

Setup In order to test whether PG-SCORE gen-
eralizes beyond 8B parameter size models, we use
an OLMo 32B base model (Sϕ) and recompute the
intrinsic and extrinsic metrics to obtain the PG-
SCORE. To save computational costs, we train stu-
dent models across three teachers (Gemma 3 27B

---

<!-- PAGE 19 -->

Arabic (ar)

Czech (cs)

German (de)

Model

dx

dy

GPT 4o mini
Llama 3.1 70B Inst.
Llama 3.1 8B Inst.
Command A
Aya Expanse 32B
Gemma 3 27B Inst.
Gemma 3 12B Inst.
Gemma 3 4B Inst.
IBM Granite 4.0
IBM Granite Micro

0.704
0.701
0.708
0.690
0.693
0.717
0.721
0.728
0.704
0.741

0.869
0.875
0.779
0.846
0.888
0.890
0.864
0.869
0.829
0.863

PPL

8.40
7.00
6.2e4
5.41
4.34
4.40
4.43
5.52
1.9e4
12.45

R

dx

dy

3.516
2.719
1.731
3.996
3.964
3.932
3.774
3.470
2.463
3.033

0.643
0.654
0.673
0.647
0.650
0.675
0.676
0.682
0.665
0.713

0.862
0.889
0.799
0.865
0.884
0.885
0.882
0.883
0.862
0.874

PPL

3.18
3.18
2.7e4
3.24
3.15
3.77
3.88
3.87
5.29
4.61

R

dx

dy

3.716
3.327
1.908
4.184
4.133
4.342
4.266
4.127
3.158
3.568

0.732
0.707
0.738
0.730
0.700
0.731
0.751
0.744
0.717
0.726

0.889
0.892
0.873
0.889
0.902
0.898
0.899
0.898
0.885
0.892

PPL

3.65
3.22
3.6e3
3.59
3.44
3.96
4.06
3.96
24.61
4.59

Spanish (es)

Indonesian (id)

Japanese (ja)

Model

dx

dy

GPT 4o mini
Llama 3.1 70B Inst.
Llama 3.1 8B Inst.
Command A
Aya Expanse 32B
Gemma 3 27B Inst.
Gemma 3 12B Inst.
Gemma 3 4B Inst.
IBM Granite 4.0
IBM Granite Micro

0.729
0.728
0.744
0.733
0.724
0.768
0.763
0.754
0.743
0.729

0.887
0.892
0.898
0.884
0.893
0.903
0.895
0.887
0.882
0.887

PPL

3.78
3.15
503.0
3.77
3.67
4.30
4.14
4.52
5.22
4.58

R

dx

dy

3.883
3.434
2.860
4.336
4.181
4.266
4.193
4.021
3.309
3.779

0.728
0.727
0.738
0.747
0.726
0.740
0.762
0.760
0.729
0.760

0.854
0.874
0.863
0.857
0.879
0.854
0.851
0.851
0.833
0.860

PPL

5.50
4.85
1.1e3
4.94
4.43
5.49
5.84
6.46
16.80
11.92

R

dx

dy

3.656
3.293
2.599
3.899
4.017
4.057
3.958
3.657
2.437
3.113

0.736
0.756
0.759
0.739
0.743
0.765
0.756
0.794
0.761
0.764

0.880
0.799
0.796
0.881
0.883
0.875
0.885
0.875
0.849
0.877

PPL

5.81
4.52
5.4e4
4.92
5.96
5.90
5.78
6.45
9.79
7.22

R

3.810
3.396
2.513
4.235
4.140
4.260
4.203
4.103
3.365
3.704

R

3.639
2.459
1.806
4.174
3.821
3.956
4.017
3.656
2.889
3.295

Table 11: Full intrinsic evaluation results across all languages. Data quality metrics include the diversity of
prompts and responses (dP and dR), average perplexity of the student model on the response (PPL), and average
reward score based on a multilingual LLM judge (R).

model such as NLLB (NLLB Team et al., 2022). In
this section, we examine the effect of the translation
method on the PG-SCORE of teacher models.

Setup First, we filter and sample 10k En-
glish prompt-response pairs from the Tülu 3
SFT dataset.4 Then, using the NLLB model
(nllb-200-distilled-600M), we perform two
(1) NLLB-Translate-then-
translation methods:
Respond: translate the prompts to each target lan-
guage and prompt Gemma 3 27B Instruct to gener-
ate a response, and (2) NLLB-Translate-Both: trans-
late both the prompts and responses from English to
the target language. We choose the 600M version
due to its computational efficiency and popularity
among practitioners, as measured by HuggingFace
downloads and community likes.

We compare these methods against our original
Translate method, i.e., prompting Gemma 3 27B In-
struct to directly translate the prompt and generate
the response in the target language (LM-Translate).
Then, we compute the intrinsic data quality metrics
and finetune OLMo 3 7B student models on each

4Tülu 3 also contains non-English data. We perform
English-language filtering using fastText (Joulin et al., 2016,
2017) and the staticvectors library.

19

synthetic dataset to compute PG-SCORE.

Results Figure 6 shows the PG-SCORE and aver-
age benchmark performance of the student model
for each translation method across Arabic, Ger-
man, and Indonesian. We find that LM-Translate
outperforms both NLLB-based approaches, achiev-
ing an average PG-SCORE of 1.36 compared to
0.85 for NLLB-Translate-Both and 0.80 for NLLB-
Translate-then-Respond. This pattern holds across
all three languages, with the largest gap observed
for German (2.09 vs 1.26/1.68).

Our findings suggest that prompt naturalness,
rather than response quality, is a bottleneck in
translation-based pipelines: having an LM gen-
erate responses to NLLB-translated prompts pro-
vides no improvement over pure NLLB translation
(0.80 vs 0.85), indicating that translated prompts
fail to elicit the same quality of responses as LM-
translated prompts.

G.4 Weighing of Intrinsic and Extrinsic

Metrics in PG-SCORE

Our PG-SCORE formulation uses an assumption-
free and equal weighing scheme between the intrin-
) metrics. In this section,
sic (

) and extrinsic (

I

E

---

<!-- PAGE 20 -->

Model

Arabic (ar) Czech (cs) German (de)

Spanish (es)

Indonesian (id)

Japanese (ja)

GPT 4o mini
Llama 3.1 70B Inst.
Llama 3.1 8B Inst.
Command A
Aya Expanse 32B
Gemma 3 27B Inst.
Gemma 3 12B Inst.
Gemma 3 4B Inst.
IBM Granite 4.0
IBM Granite Micro

-2.086
-1.528
-0.841
-2.476
-0.293
-0.074
-1.015
-1.033
1.565
-0.421

0.538
0.538
0.525
0.505
0.538
0.552
0.538
0.538
0.538
0.538

3.098
2.265
2.623
2.759
2.491
2.635
2.700
2.568
2.061
1.842

1.395
1.075
0.595
1.613
1.701
1.724
1.592
1.209
1.235
1.203

2.025
0.329
1.425
1.863
1.943
0.198
-0.017
-0.388
0.614
-0.659

0.099
0.013
0.236
0.841
0.221
0.677
0.524
0.349
0.802
0.210

Table 12: Average performance gain recovered (PGR) of a student model across various multilingual bench-
marks. Our multilingual evaluation suite includes Global-MMLU Lite (Singh et al., 2025), M-RewardBench
(Gureja et al., 2025), and M-GSM (Shi et al., 2023). The PGR computation is based on Kim et al. (2025) and
detailed in §2.3 (Equation 2) where SREF = OLMo 3 7B Instruct SFT and Sϕ = OLMo 3 1025 7B.

Model

Arabic (ar)

Czech (cs)

German (de)

Spanish (es)

Indonesian (id)

Japanese (ja)

Gemma 3 27B Inst.
Aya Expanse 32B
Gemma 3 12B Inst.
Command A
Gemma 3 4B Inst.
GPT 4o mini
IBM Granite 4.0
IBM Granite Micro
Llama 3.1 70B Inst.
Llama 3.1 8B Inst.

0.145 (0.0121)
-0.058 (0.0116)
-0.464 (0.0119)
-1.360 (0.0112)
-0.488 (0.0119)
-1.117 (0.0117)
-0.072 (0.0123)
-0.282 (0.0121)
-0.964 (0.0117)
-1.693 (0.0120)

0.360 (0.0004)
0.222 (0.0004)
0.327 (0.0004)
0.114 (0.0004)
0.330 (0.0004)
0.015 (0.0004)
-0.031 (0.0004)
0.290 (0.0004)
0.109 (0.0004)
-0.974 (0.0004)

1.655 (0.0141)
1.468 (0.0134)
1.756 (0.0137)
1.673 (0.0139)
1.644 (0.0137)
1.766 (0.0136)
1.000 (0.0135)
1.102 (0.0139)
1.195 (0.0146)
0.891 (0.0148)

1.358 (0.0141)
1.129 (0.0123)
1.228 (0.0140)
1.102 (0.0145)
0.929 (0.0140)
0.908 (0.0149)
0.734 (0.0151)
0.783 (0.0133)
0.688 (0.0146)
0.182 (0.0164)

0.214 (0.0167)
1.153 (0.0124)
0.151 (0.0126)
1.063 (0.0125)
-0.105 (0.0126)
1.003 (0.0125)
-0.079 (0.0125)
-0.329 (0.0126)
0.182 (0.0126)
0.322 (0.0124)

0.626 (0.0124)
0.320 (0.0111)
0.573 (0.0142)
0.683 (0.0122)
0.504 (0.0113)
0.189 (0.0117)
0.321 (0.0108)
0.264 (0.0121)
-0.373 (0.0116)
-0.863 (0.0129)

Table 13: Detailed results from Table 1 with standard errors. We compute PG-SCORE thrice with different
synthetically-generated data (each trial uses a different data mix based on a random seed). We report the mean and
standard error for each teacher model across all target languages. For each language, we highlight the best model in
bold and the second-best model with an underline.

Base Model (Sϕ)

Teacher Model

Gemma 3 4B Llama 3.1 8B

Llama 3.1 70B Inst.
Llama 3.1 8B Inst.
Gemma 3 27B Inst.
Gemma 3 12B Inst.
Gemma 3 4B Inst.

+362.3%
+183.1%
+20.5%
+38.5%
+103.4%

+260.1%
+130.0%
+26.5%
+67.2%
+203.4%

Table 14: Percentage increase in PG-SCORE for
family-matched teacher-student pairs. Percentage
increase when using family-matched teachers compared
to OLMo 3 7B baseline (average across Arabic, German,
and Indonesian).

we test whether these two metrics capture (1) com-
plementary aspects of teacher effectiveness and (2)
how model rankings differ if one metric is weighted
more than the other.

Setup In order to test whether each metric cap-
tures complementary aspects of teacher effective-
ness, we compute the Spearman rank correlation (ρ)

between the intrinsic and extrinsic metrics across
all teacher-language pairs (N=60, 10 models
6
languages). In addition, in order to test the effect
of weighing one metric against the other, we for-
mulate a generalized version of PG-SCORE:

×

PG-SCORET,ℓ = α

+ (1

I

where 0

α)

E
1

−
α

≤

≤

(4)

{

0.00, 0.25, 0.50, 0.75, 1.00

Note that the experiments in §3 and §4 assume
α = 0.5. We compute the PG-SCORE across
α =
and then test
the resulting model ranks’ ρ across all pairs of α.
We perform this experiment on all teacher-language
pairs where students are finetuned from the OLMo
6 languages).
3 7B base model (N=30, 10 models

}

×

Results
Intrinsic and extrinsic metrics show a
moderate positive correlation (Spearman ρ = 0.41,
p < 0.01), suggesting that data quality metrics
are predictive of student performance while cap-
turing complementary information. This finding
motivates our combined PG-SCORE computation.

20

---

<!-- PAGE 21 -->

Teacher Model (ST,ℓ)

Language

Best Method Gemma 3 27B Aya Expanse 32B Llama 3.1 70B

Respond
Arabic (ar)
German (de)
Generate
Indonesian (id) Translate

+453.1%
+29.3%
+458.9%

+355.2%
+0.3%
+39.3%

+77.7%
+16.4%
−14.8%

Table 15: Percentage increase in PG-SCORE for best data generation method. Percentage increase when using
the best-performing data generation method compared to an equal mix baseline of all three methods (Generate,
Translate, Respond). For less-resourced languages (Arabic and Indonesian), using Translate or Respond methods
yields substantial improvements for most teachers, though gains are teacher-dependent.

Teacher Model

Average Arabic (ar) Czech (cs) German (de) Spanish (es)

Indonesian (id)

Japanese (ja)

Gemma 3 27B Inst.
Aya Expanse 32B
Llama 3.1 70B Inst.

0.805
0.227
-0.267

-0.239
-0.872
-1.688

0.222
-0.038
-0.807

2.389
1.979
0.838

1.855
1.353
1.407

0.239
-0.249
-1.441

0.366
-0.809
0.089

Table 16: PG-SCORE of three teacher models (Sϕ = OLMo 3 32B) We show that our findings generalize up to
the 32B parameter range on the three teacher models we tested: (1) Gemma 3 27B maintains its position as the
most effective teacher, and the (2) language-dependent effects are still apparent with German having the highest
PG-SCOREs across most teachers.

In addition, teacher rankings are stable for nearby
weighting schemes (ρ
0.90 for adjacent α val-
≥
ues) as shown in Figure 7. Our finding suggests
that model rankings are robust to small changes
in the weighing of intrinsic and extrinsic met-
rics. Our equal weighting (α = 0.5) balances both
perspectives, correlating strongly with extrinsic-
focused (ρ = 0.89) and reasonably with intrinsic-
focused (ρ = 0.74) rankings.

G.5 Effect of language resource levels on

PG-SCORE

Setup For each language, we consider the follow-
ing properties drawn from prior work: Common-
Crawl (CC) percentage as a proxy for presence in
pretraining data (% in CC, Raffel et al., 2020), and
linguistic resource availability (score from 1–5, 5
as high-resource, obtained from the LDC Catalog
and the ELRA Map, Joshi et al., 2020). We com-
pute the Spearman rank correlation (ρ) between
each property and PG-SCORE across all teacher-
6 languages).
language pairs (N=60, 10 models

×

Results Figure 8 shows the relationship between
a language’s percentage in CommonCrawl and PG-
SCORE. We observe a suggestive positive trend
between CommonCrawl representation and PG-
SCORE (ρ =0.886, p <0.05). This finding sug-
gests that languages with greater presence in pre-
training data enable teacher models to generate
higher-quality synthetic data that leads to better
student performance. This finding is unsurprising,

but it provides empirical evidence of a structural
gap that inhibits quality synthetic data generation
for long-tail languages. In contrast, we do not find
a significant correlation between resource avail-
ability and PG-SCORE (ρ =0.372, p =0.468). Our
findings suggest that teacher model generation qual-
ity depends more heavily on pretraining exposure
than linguistic resources. Additionally, the data
sources from Joshi et al. (2020) do not reflect the
current landscape: recent LMs are trained on either
publicly-available datasets from HuggingFace or
in-house datasets. While our work includes 6 di-
verse languages, the sample size remains limited;
we encourage future work to expand the number of
languages to validate these findings.

H Disclosure on the Use of LLMs

We used Claude (Anthropic, 2024) to assist with
editing, title ideation, and proofreading portions of
this work. All scientific claims and interpretations
are solely our own. We reviewed and revised all
LLM-assisted text.

I Multilingual Synthetic Data Recipe:

Case Study on Tagalog

As an application of our findings and discussion in
§5, we present a case study on developing a multi-
lingual synthetic data recipe on a held-out language:
Tagalog. It is a mid-resource language (Category 3
in Joshi et al. (2020)’s taxonomy) and the standard-
ized form of Filipino, the national language of the

21

---

<!-- PAGE 22 -->

Model Name

Temperature Top-p Top-k Max Seq Len

Generation Parameters

GPT-4o mini
Llama 3.1 70B Instruct
Llama 3.1 8B Instruct
Command A
Aya Expanse 32B
Gemma 3 27B Instruct
Gemma 3 12B Instruct
Gemma 3 4B Instruct
IBM Granite 4.0
IBM Granite Micro
Default

0.8
0.6
0.6
0.3
0.3
1.0
1.0
1.0
0.0
0.0
0.8

0.9
0.9
0.9
–
–
0.95
0.95
0.95
–
–
0.9

–
–
–
–
–
64
64
64
–
–
–

16,384
131,072
131,072
128,000
128,000
8,192
8,192
8,192
4,096
4,096
–

Table 17: Inference settings for each teacher model. Generation parameters are based on model provider
recommendations from HuggingFace and/or official documentation. The Default row indicates parameters used
when model-specific recommendations are unavailable. The “–” symbol indicates the parameter was not specified
in the official recommendations.

Philippines.

I.1 Setup: Recipe Design and Evaluation

Data We collect Filipino seed data from various
publicly-available SFT datasets such as WildChat
4.8M and the Aya Collection. In addition, we also
include English data from the Tülu 3 SFT dataset
for the Translate method. Table 18 shows the statis-
tics of the seed dataset used for Tagalog synthetic
data generation. Then, we implement the following
data interventions based on our findings:
• Teacher Model: we use Gemma 3 27B In-
struct as the teacher model, as it was the best-
performing model across most target languages
we evaluated (§3).

• Data Generation Method: we use the Trans-
late and Respond methods, as they were the
best-performing methods for mid-resource lan-
guages like Indonesian (§3.3). In addition, we
add a small sample of prompt-response pairs
synthesized via the Generate method.

• Synthetic Data Scale: we generate 10k syn-
thetic examples using the selected teacher and
data generation method, as we found that this
scale is sufficient to achieve strong student per-
formance (Appendix G.1). However, we also
test on finetuning a model with 25k synthetic
examples to see if more data improves perfor-
mance.

• Student Base Model: we finetune using the
Gemma 3 4B model, as we find that family-

Source

Num. Instances

TaCo Alpaca
Aya Collection
WildChat 4.8M
WildChat 1M

10,000
1,241
997
250

Table 18: Tagalog seed dataset statistics. In order to
bootstrap the synthetic data generation recipe for Taga-
log, we curate a seed dataset containing a mix of Tagalog
and English prompts from various sources. Majority of
the seed dataset is from the TaCo paper (Upadhayay and
Behzadan, 2024).

matched teacher-student pairs yield higher PG-
SCORE (§3.2).
For the purposes of this report, we will designate
the model finetuned on Gemma 3 4B using our
synthetic recipe as 10K-Polyglot-TL, where “10K”
indicates the number of SFT instances used during
finetuning.

Evaluation We evaluate on FILBENCH (Miranda
et al., 2025), a benchmark for LMs that includes
Filipino-centric multiple-choice and generative
tasks. It measures an LM’s performance across
four categories such as classical NLP, cultural
knowledge, reading comprehension, and genera-
tion, alongside an aggregated FILBENCH score.

We also compare against two data mix baselines:
1. 10K-Public: we sample 10k Tagalog prompt-
response pairs from the seed dataset. This base-
line aims to simulate a non-synthetic data ap-

22

---

<!-- PAGE 23 -->

Figure 7: Effect of weighing intrinsic and extrinsic
metrics in PG-SCORE. Model rankings remain rela-
tively stable across neighboring weightings of intrinsic
and extrinsic metrics.

not always produce better training data (§3).

In addition, comparing 10K-Polyglot-TL to
other models in the FILBENCH leaderboard5 shows
that the former is competitive against Qwen 3 4B
and Llama 3.1 8B Instruct. We highlight that our
4B models are competitive against other mod-
els with larger parameter sizes, suggesting that
a multilingual synthetic data recipe based on our
PG-SCORE findings is data-efficient. We also find
that increasing the number of SFT instances (10k
to 25k) led to a performance increase of 0.21pp.
While we previously found that 10K instances
showed diminishing returns (see Appendix G.1),
the continued gains from scaling to 25K instances
on FILBENCH suggest that saturation points may
depend on task diversity. FILBENCH covers a
broader range of NLP tasks (e.g., named-entity
recognition) compared to our experimental bench-
marks in §3 and Appendix G, indicating that prac-
titioners working with diverse task distributions
may benefit from exploring larger synthetic
datasets beyond the 10K threshold.

I.3 Analysis: Ablation Experiments

In order to measure the contribution of our find-
ings and recommendations in §5, we perform the
following ablation experiments as shown in Fig-
ure 9. Note that the interventions described below

5Official FILBENCH leaderboard:
spaces/filbench/filbench-leaderboard

https://hf.co/

Figure 6: Effect of translation method on PG-
SCORE. We compare three methods: LM translates
prompt EN-to-XX and responds (LM-Translate), NLLB
translates prompt EN-to-XX and LM responds (NLLB-
Translate-then-Respond), and NLLB translates both
prompt and response (NLLB-Translate-Both).

proach to training multilingual LMs.

2. 10K-GPT-4oM: we synthesize 10k instances
using an off-the-shelf teacher model (GPT-4o-
mini). This baseline simulates a typical data
generation approach of choosing a teacher in
an ad hoc manner due to its perceived strength
(size or benchmark performance) or ease of use.
For all methods, we finetune a Gemma 3 4B base
model using the same training settings indicated in
Appendix E.1.

I.2 Results: Leaderboard Scores and

Ablations

Table 19 shows the FILBENCH score of our op-
timal synthetic recipe compared to other models
in the same parameter range. We find that 10K-
Polyglot-TL is competitive against 10K-GPT-4oM
(+1.85pp), and has better performance compared to
10K-Public (+2.28pp). These results suggest that
(1) synthetic data generation is a viable approach
for building less-resource language models, and
(2) our finding that selecting strong teacher models
based on PG-score is effective, as larger models do

23

---

<!-- PAGE 24 -->

Model

FILBENCH Score

GPT-4o (2024-08-06)
Gemma 3 27B Inst.
Gemma 3 12B Inst.
25K-Polyglot-TL 4B
10K-Polyglot-TL 4B
Qwen 3 4B
10K-GPT-4oM
Llama 3.1 8B Inst.
Ministral 8B Inst.
10K-Public
Pangea 7B
SeaLLMs 3 1.5B

74.27
55.17
54.04
49.73
49.52
48.42
47.67
47.38
47.33
47.24
43.98
43.20

Figure 8: Relationship between a language’s percent-
age in CommonCrawl and PG-SCORE. We observe a
suggestive positive trend (ρ = 0.886, p<0.05) between
CommonCrawl representation and PG-SCORE across
the six languages tested.

Table 19: Model performance on a held-out language
(Tagalog) as evaluated on FILBENCH (Miranda et al.,
2025). We compare our optimal synthetic recipe

against baseline approaches and other models in the
same parameter range.

are additive.

Curation of publicly-available data vs. Syn-
thetic data generation We compare student mod-
els trained on (1) publicly-available Tagalog SFT
data and (2) synthetic SFT instances generated
by a GPT-4o teacher (note that these are also the
same baselines in Appendix I.2). We find that
the performance of these two baselines are similar
(∆ = 0.5pp), suggesting that there is no signifi-
cant advantage to using a synthetic data pipeline
if the teacher model is not optimal. We also hy-
pothesize that some publicly-accessible datasets
in Tagalog were semi-synthetic (e.g., TaCO uses
a synthetic pipeline akin to the Translate method,
but using chain-of-thought to improve the quality
of translations), making it difficult to perform a fair
comparison.

Using a teacher with a higher PG-SCORE We
then swap the GPT-4o-mini teacher with Aya Ex-
panse 32B, a teacher with a higher PG-SCORE
based on our main findings (0.461 vs. 0.706, c.f.
§3, Table 1). We observe a slight performance
improvement in this intervention, suggesting that
the PG-SCORE metric is generalizable across an
unseen language.

Matching teacher and student model families
One of our key findings and recommendation is to
match the model families of the teacher and the
student (§3.2). We use a Gemma 3 Instruct 27B
teacher model to match the family of the Gemma 3

4B base model. This intervention yields a substan-
tial performance improvement, demonstrating that
family alignment is a reliable heuristic for teacher
selection. The improvement from family matching
is consistent with our findings that family-matched
pairs achieve at least +20.5% higher PG-SCORE
compared to mismatched pairs, likely due to shared
tokenization schemes and architectural similari-
ties that facilitate better knowledge transfer from
teacher to student.

Increase data scale We increase the number
of synthetic instances from 10k to 25k to assess
whether additional data continues to improve per-
formance. We observe a modest gain of 0.21pp,
which is smaller than the improvements from
teacher model selection and model family match-
ing. This finding aligns with our earlier observa-
tion that gains diminish beyond 10k examples (Ap-
pendix G.1), though the continued improvement on
FILBENCH’s diverse task distribution suggests that
saturation points may be task-dependent.

Increase model scale Finally, we explore
whether scaling the student model from 4B to 12B
(and 27B) parameters provides additional perfor-
mance gains. We find that the larger student model
achieves higher performance, demonstrating that
our synthetic data recipe benefits from increased
model capacity. This result is consistent with our
generalization experiments (Appendix G.2), where
we showed that PG-SCORE generalizes across dif-

24

---

<!-- PAGE 25 -->

Figure 9: Student model performance on a held-out language (Tagalog) across several synthetic data interven-
tions. Given a held-out language (Tagalog) and an evaluation benchmark (FILBENCH), we apply data interventions
based on our recommendations on creating a multilingual synthetic data recipe (§5).

ferent model sizes while maintaining the relative
ranking of teacher models. However, we note that
the performance of our best models are still be-
hind Gemma 3 27B Instruct and Gemma 3 12B
Instruct (Table 19). Given that observation, we still
argue that our synthetic pipeline, which uses 25K
instances trained only via SFT, can be considered
data and resource-efficient compared to the post-
training interventions done in Gemma 3, which in-
volved instruction-tuning and reinforcement learn-
ing objectives (Gemma Team et al., 2025).

J

Inference Details

Prompt templates Figure 10 to Figure 12 show
the prompt templates used for each data generation
method. In addition, Figure 13 shows the prompt
template used for the LLM-as-a-judge method to
evaluate text quality.

Inference settings We use vLLM (Kwon et al.,
2023) and Curator (Marten et al., 2025) for infer-
ence. For each teacher model, we check whether
the model provider recommended best settings for
usage. If not, then we set a default configuration
(temperature=0.8, top_p=0.9). Table 17 summa-
rizes the inference settings we used for each teacher
model.

25

---

<!-- PAGE 26 -->

Generate: sample k prompt-response pairs from Dseed,ℓ and use it as in-context examples

As a multilingual data generator, your task is to generate a new example (‘prompt‘ and ‘response‘) for a
dataset demonstrating how AI agents can fulfill general instructions for {lang_name}.

To do this, you will want to generate two pieces of information:
1) A "prompt" specifying a task to be completed or a question to be answered (what, where, when, how, who,
why). The task should be very challenging yet solvable.
2) A "response" representing a valid completion of that task in natural language. If the "response" does not
satisfy the "prompt", then you have failed at your job. Do not provide unnecessary details, beyond what is
explicitly needed to satisfy the instruction you generated.

Hard constraint: The generated task MUST belong to exactly one of the following categories (pick
one at random and do NOT mention the category).
1. Logical reasoning / error analysis
2. Math or quantitative reasoning with explanation
3. Classification or labeling
4. Dialogue or role-play
5. Translation or paraphrasing with constraints
6. Procedural instructions (step-by-step)
7. Grammar correction or linguistic analysis
8. Short-form creative output (≤50 words)
9. Knowledge recall with verification or correction
10. Cultural or pragmatic judgment

Add diversity to your generations by varying the types of tasks you create, the styles and tones of the
responses, and the complexity of the language used. This will help ensure a rich and varied dataset. For example,
you might create tasks that involve answering knowledge-based questions, answering math questions, providing
explanations, generating creative content, or performing translations.

Please provide a JSON dictionary response that
‘response‘. Use the ‘prompt‘ and ‘response‘ keys in the dictionary.
Do not generate any other text in your response (for example, do not start your message with any greetings, and
never ask for clarification or apologize for struggling with the task).
Try you best to ensure that the input and response you generate are distinct from the provided examples while
maintaining a diverse, detailed, precise, comprehensive, and high-quality response.
It is important to generate responses that are contextually relevant and culturally appropriate for {lang_name}.

includes the new ‘prompt‘ and its corresponding

Here are some examples to guide your generation. The best way to use these examples is to identify
the patterns and structures they follow, rather than copying them directly:

{% for example in examples[:k] %}
Prompt: {{example[“prompt”]}}
Response: {{example[“response”]}}
{% endfor %}

New Example:

Figure 10: Prompt template for the Generate data generation method.

26

---

<!-- PAGE 27 -->

Translate: forward-translate English prompts from
response yi

Dseed,ℓ and use teacher T to generate the

As a multilingual data generator, your task is to translate the given prompt from English into
{lang_name} and generate the appropriate response in the same language.
Important: you must return both the translated prompt (into {lang_name}) and the response.
Ensure that both the translated prompt and the response are coherent, culturally appropriate,
and demonstrate a deep understanding of the language nuances.

Do not generate any other text
in your response (for example, do not start your
message with any greetings, and never ask for clarification or apologize for struggling with
the task).
Do not return the original English prompt. Remember, you must translate the prompt first
and return it.
Here is the prompt you need to translate and respond to:

{prompt}

Figure 11: Prompt template for the Translate data generation method.

Respond: take prompts from

Dseed,ℓ and use teacher T to generate the response yi

As a multilingual data generator, you will be presented a user request or instruction in
the {lang_name} language. Your task is to generate an appropriate response for the given
request. Ensure that your response is coherent, culturally appropriate, and demonstrates a
deep understanding of the language nuances Do not generate any other text in your response
(for example, do not start your message with any greetings, and never ask for clarification or
apologize for struggling with the task). Here is the prompt you need to respond to:

{prompt}

Figure 12: Prompt template for the Respond data generation method.

27

---

<!-- PAGE 28 -->

LLM-as-a-judge: evaluating text quality using the multilingual rubric language model

Task Description:
An instruction (might include an Input inside it) in {language}, a response to evaluate, and
a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of the response strictly based on the given
score rubric, not evaluating in general.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should
refer to the score rubric.
3. The output should contain the score and feedback only.
4. Please do not generate any other opening, closing, and explanations.

The instruction to evaluate:
{{instruction}}

Response to evaluate:
{{response}}

Score Rubrics:
[Is the model proficient in language {lang_name}, including its cultural nuance and gram-
matical usage, and responds in a helpful and harmless manner according to the instruction?]
Score 1: The response contains severe grammatical errors, lacks cultural appropriateness, or
is unhelpful/harmful. The language proficiency is very poor.
Score 2: The response has noticeable grammatical errors and limited cultural awareness.
It partially addresses the instruction but with significant gaps in language proficiency or
helpfulness.
Score 3: The response demonstrates adequate language proficiency with some minor
grammatical errors. It shows reasonable cultural awareness and addresses the instruction in a
helpful manner, though improvements are possible.
Score 4: The response exhibits strong language proficiency with minimal grammatical errors
and good cultural nuance. It addresses the instruction in a helpful and harmless way with
only minor room for improvement.
Score 5: The response demonstrates excellent language proficiency with proper grammar,
appropriate cultural nuance, and idiomatic usage. It fully addresses the instruction in a
helpful and harmless manner.

Feedback:

Figure 13: We evaluate text quality of synthesized texts using a multilingual rubric model called M-Prometheus
(Pombal et al., 2025). We choose M-Prometheus due to its strong performance on multilingual and human-aligned
benchmarks.

28

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Polyglot Teachers: Evaluating Language Models for Multilingual
|     |                      |     | Synthetic |     | Data Generation |              |     |     |     |     |
| --- | -------------------- | --- | --------- | --- | --------------- | ------------ | --- | --- | --- | --- |
|     | LesterJamesV.Miranda |     |           |     | IvanVulic´      | AnnaKorhonen |     |     |     |     |
LanguageTechnologyLab,UniversityofCambridge
ljvm2@cam.ac.uk
Collection ljvmiranda921/polyglot-teachers Code ljvmiranda921/polyglot-teachers
Abstract
pairsofuserpromptsandacorrespondingresponse,
whichisoftenscarceforless-resourcedlanguages
6202 rpA 31  ]LC.sc[  1v09211.4062:viXra Synthesizingsupervisedfinetuning(SFT)data
|     |     |     |     |     | (Kunchukuttan | et  | al., 2025). | Generating |     | prompt- |
| --- | --- | --- | --- | --- | ------------- | --- | ----------- | ---------- | --- | ------- |
fromlanguagemodels(LMs)toteachsmaller
|     |     |     |     |     | response | pairs for | these languages |     | demands | sub- |
| --- | --- | --- | --- | --- | -------- | --------- | --------------- | --- | ------- | ---- |
modelsmultilingualtaskshasbecomeincreas-
stantialhumaneffort(Singhetal.,2024;Kapania
| ingly common. | However,         | teacher   | model      | se- |                |          |              |     |     |           |
| ------------- | ---------------- | --------- | ---------- | --- | -------------- | -------- | ------------ | --- | --- | --------- |
|               |                  |           |            |     | et al., 2025), | creating | a bottleneck |     | for | language- |
| lection       | is often ad hoc, | typically | defaulting |     |                |          |              |     |     |           |
to the largest available option, even though specificmodeldevelopment.
such models may have significant capability To alleviate the challenge of human effort and
gapsinnon-Englishlanguages. Thispractice datascarcity,syntheticdatagenerationusingLMs
| can result | in poor-quality | synthetic | data | and |            |          |      |           |     |              |
| ---------- | --------------- | --------- | ---- | --- | ---------- | -------- | ---- | --------- | --- | ------------ |
|            |                 |           |      |     | has gained | traction | as a | promising |     | solution for |
suboptimalstudentdownstreamperformance.
multilingualLMdevelopment(Cahyawijayaetal.,
| In this work, | we systematically |              | characterize |          |          |               |              |     |               |            |
| ------------- | ----------------- | ------------ | ------------ | -------- | -------- | ------------- | ------------ | --- | ------------- | ---------- |
|               |                   |              |              |          | 2024; Ng | et al., 2025; | Martins      |     | et al.,       | 2025; Ham- |
| what makes    | an effective      | multilingual |              | teacher. |          |               |              |     |               |            |
|               |                   |              |              |          | moud et  | al., 2026,    | inter alia). |     | This approach | in-        |
| We measure    | intrinsic         | measures     | of data      | qual-    |          |               |              |     |               |            |
itywithextrinsicstudentmodelperformance volvesleveragingatypicallylargerteachermodel
in a metric we call POLYGLOT SCORE; eval- togeneratetrainingexamples,whicharethenused
uating10LMsacross6typologicallydiverse tofinetuneasmallerstudentmodeltoreplicatethe
languages,generatingover1.4MSFTexamples knowledge of the teacher (Kim and Rush, 2016).
| andtraining240studentmodels. |     |     | Amongthe |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
However,existingworksoftenselectteachermod-
modelstested,Gemma327BandAyaExpanse
elsarbitrarily,defaultingtothelargeststate-of-the-
32Bemergeasconsistentlyeffectiveteachers
|                  |         |      |       |           | art models                            | that excel | on  | benchmarks |     | (Xu et al., |
| ---------------- | ------- | ---- | ----- | --------- | ------------------------------------- | ---------- | --- | ---------- | --- | ----------- |
| across different | student | base | model | families. |                                       |            |     |            |     |             |
|                  |         |      |       |           | 2025b;Lietal.,2025;Zhangetal.,2025a). |            |     |            |     | This        |
Furtheranalysesrevealthatmodelscalealone
doesnotsignificantlypredictteachereffective- practiceisproblematicbecausethesemodels,de-
ness; instead, data qualities such as prompt spitestrongperformance,mayhavesignificantca-
diversity,length,andresponsefluencycapture pability gaps in non-English languages, leading
over93.3%ofvarianceinintrinsicdataquality
topoor-qualitysyntheticdatathatpropagatesthe
| andpredictstudentperformance. |     |     | Finally,we |     |                                            |     |     |     |     |     |
| ----------------------------- | --- | --- | ---------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
|                               |     |     |            |     | teacher’sweaknessesratherthanitsstrengths. |     |     |     |     | And |
providepracticalrecommendations,including
|     |     |     |     |     | soweask: | “whatmakesaneffectivemultilingual |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --------------------------------- | --- | --- | --- | --- |
matchingthemodelfamiliesofteacher-student
teacherforsyntheticdatageneration,andhowcan
pairsandtranslatingfromorrespondingtoex-
wesystematicallymeasureit?”
istingprompts,whichcanyieldimprovements
forless-resourcedlanguages. Wehopethatour Inthiswork,weconductacomprehensiveanal-
workadvancesdata-centricresearchinmulti- ysisof10LMsacross6typologicallydiverselan-
lingualsyntheticdataandLMdevelopment.
guagesonthreecommonsyntheticdatageneration
|     |     |     |     |     | methods: | responding | to  | a user | query | or instruc- |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | ------ | ----- | ----------- |
tion,translatingpromptsfromEnglishtoatarget
1 Introduction
|     |     |     |     |     | language, | and generating |     | prompt-response |     | pairs |
| --- | --- | --- | --- | --- | --------- | -------------- | --- | --------------- | --- | ----- |
Supervisedfinetuning(SFT,Ouyangetal.,2022) given in-context examples (§2.2). To systemati-
has emerged as a standard approach for adapting callyassessteachermodeleffectiveness,weeval-
languagemodels(LMs)tospecifictargetlanguages uateLMsusingbothintrinsicmeasuresofdata
quality(§2.2,i.e.,thediversityofpromptsandre-
(Zhangetal.,2025b;Aryabumietal.,2024,inter
alia). Central to the success of SFT is the avail- sponses, the perplexity of the base model on the
abilityofhigh-qualitytrainingdata,consistingof response, and response quality based on a multi-
1

|     |     | = Multilingual
 | + Student Model
 |     | Multilingual Data Quality |     |     |
| --- | --- | ---------------- | ----------------- | --- | ------------------------- | --- | --- |
Polyglot Score
|     |     | Data Quality | Performance |     |     |     |     |
| --- | --- | ------------ | ----------- | --- | --- | --- | --- |
Diversity of prompts and responses
Seed
Perplexity of the base model
Multilingual LLM-as-a-judge score
SFT
Student Model Performance
Synthetic

|           | Data Generation |                 |     |           | Cultural and Factual Knowledge |              |     |
| --------- | --------------- | --------------- | --- | --------- | ------------------------------ | ------------ | --- |
| Teacher
 |                 | Synthetic
     |     | Student
 |                                |              |     |
|           | Generate        | Respond Dataset |     | Model     |                                |              |     |
| Model     |                 |                 |     |           |                                | General Chat |     |
Translate
Mathematical Reasoning
Base Model
Figure 1: Overview of our method for evaluating language models as multilingual teachers (POLYGLOT
SCORE). Weevaluateteachermodelsontheirsyntheticdatagenerationcapabilitiesacrossthreemethods: Generate
aprompt-responsepairgivenfew-shotexamples,TranslatepromptsfromEnglishandgeneratearesponse,and
Respondtoapromptinthetargetlanguage. ThePOLYGLOTSCOREincorporatesbothintrinsicdataqualitymetrics
andextrinsicstudentmodelperformancetoassesstheeffectivenessofateachermodelforatargetlanguage.
extrinsicmeasure
lingualreward model)andan themodelfamiliesoftheteacherandstudentis
of student model performance on multilingual areliableheuristicforchoosingateachermodel
tasks(§2.3,culturalunderstanding,mathematical (§3.2), and generating responses to existing
reasoning,generalchat). Weaggregatethesemea- prompts or translating from English can yield
surements into a single metric called POLYGLOT substantialimprovementsonless-resourcedlan-
SCORE(PG-SCORE),inordertoprovideaholistic guagescomparedtoarandommixofdatagen-
assessment of a teacher model’s data generation erationmethods,thoughgainsvarybyteacher
model(§3.3).1
| capabilities. | Ourcontributionsareasfollows: |     |     |     |     |     |     |
| ------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
• Weclosetheevaluationgapbyevaluating10 Wehopethatthisworkpavesthewayfordevel-
|     |     |     | oping | inclusive | and equitable | language | technolo- |
| --- | --- | --- | ----- | --------- | ------------- | -------- | --------- |
teachermodels,generatingover1.4MSFTex-
amplesandfinetuning240studentmodelsfrom gies through quality and cost-effective data. We
OLMo37B.WefindthatGemma327Bcon- releaseourcode,data,andmodelstodriveresearch
inmultilingualsyntheticdatageneration.
| sistentlyrankswithinthetopthreehighest |     |     | PG- |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
SCOREandthattheGemma3modelfamilyout-
|     |     |     | 2   | EvaluatingLanguageModelsas |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | --- |
performsotherfamiliessuchasLlama3.1and
MultilingualTeachers
| IBMGranite(§3.1). |     | OurPG-SCORErankings |     |     |     |     |     |
| ----------------- | --- | ------------------- | --- | --- | --- | --- | --- |
areconsistentacrossotherbasemodelfamilies The POLYGLOT SCORE (Figure 1) of a teacher
(Llama3.18B,Qwen38B,Gemma34B,§3.2).
|     |     |     | modelT | foratargetlanguageℓisbasedonthe(1) |     |     |     |
| --- | --- | --- | ------ | ---------------------------------- | --- | --- | --- |
• Weprovideanalysesandinsightsonthechar-
intrinsicqualityofthesyntheticdatageneratedby
acteristicsofagoodmultilingualteachermodel. theteacher(§2.2)andthe(2)extrinsicperformance
Ouranalysesrevealthatmodelscaleandbench-
|     |     |     | ofastudentmodelS |     | finetunedonthisdata(§2.3). |     |     |
| --- | --- | --- | ---------------- | --- | -------------------------- | --- | --- |
markperformance,whicharecommonassump-
|     |     |     | 2.1 | Creatingtheseeddataset |     |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- |
tionsofa“strong”model,donotsignificantly
predictteachereffectiveness(§4.1). Instead,we In order to bootstrap the synthetic data gener-
findthatqualitiesofthegenerateddata,namely
|     |     |     | ation | process, | we create | a seed dataset | seed,ℓ |
| --- | --- | --- | ----- | -------- | --------- | -------------- | ------ |
D
prompt diversity and length coupled with flu- for each target language ℓ. We create
seed,ℓ
D
entanddiverseresponses,captureover93.3% by aggregating publicly available multilingual
ofthevarianceinintrinsicdataqualitymetrics,
instruction-tuningdatasets,includingtheAyaCol-
andtheirprincipalcomponentspredictstudent
|     |     |     | lection | (Aryabumi | et al., | 2024), WildChat | 4.8-M |
| --- | --- | --- | ------- | --------- | ------- | --------------- | ----- |
performancewithR2=0.664(§4.2).
(Zhaoetal.,2024),EuroBlocks-SFT(Martinsetal.,
|         |                    | recommend | a   |     |     |     |     |
| ------- | ------------------ | --------- | --- | --- | --- | --- | --- |
| • Based | on these findings, | we        |     |     |     |     |     |
1Asasupplementary,weshowthatourrecipeimproves
| recipe | (§5) for generating | multilingual | syn- |     |     |     |     |
| ------ | ------------------- | ------------ | ---- | --- | --- | --- | --- |
performanceonaheld-outlanguage(Tagalog)onalanguage-
theticdata. Forexample,wefindthatmatching specificbenchmark(AppendixI).
2

2025),andMagpie-Align(Xuetal.,2025a). Inor- (Pombaletal.,2025)asanLMjudgetoscore
der to simulate scenarios where English prompts the quality of the prompt-response pair (Fig-
are translated into a target language, we also in- ure13). WechooseM-Prometheusbecauseof
cludeexamplesfromTülu3SFT(Lambertetal., itshighperformanceonhuman-alignedevalu-
2025),Helpsteer3(chosenresponses,Wangetal., ation benchmarks, suggesting that the reward
2025),andGSM8K(trainsplit,Cobbeetal.,2021). modelalignswellwithnativespeakers.
DetailedseeddatasetstatisticsinAppendixB. We combine these intrinsic metrics by scaling
eachmetricusingz-scorenormalizationandaver-
2.2 MultilingualDataQuality&Diversity
agingthemasshowninEquation1.
| Synthetic |     | data generation |     | Given | a   | teacher |     |     |     | 1   |     |     |     |
| --------- | --- | --------------- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|                                           |     |     |     |     |     |     | Intrinsic |     | =   |     | z-score(m( |     | ))  |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---------- | --- | --- |
| modelT,targetlanguageℓ,andaseeddatasetfor |     |     |     |     |     |     |           | T,ℓ |     | M   |            | D   | T,ℓ |
(1)
| language | ℓ,  | , we | distill | a synthetic |     | dataset |     |     | |   | | m∈M |     |     |     |
| -------- | --- | ---- | ------- | ----------- | --- | ------- | --- | --- | --- | ----- | --- | --- | --- |
seed,ℓ
D
= (x ,y ) N consisting of N prompt- whereM = d x ,d y , log(1+PPL),R
| T,ℓ             |     | i i i=1   |                          |     |     |     |     |                         | {   |     | −   |     | }   |
| --------------- | --- | --------- | ------------------------ | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
| D               | {   | }         |                          |     |     |     |     |                         |     |     |     |     |     |
| responsepairs(x |     | i ,y i ). | Weconsiderthreesynthetic |     |     |     |     |                         |     |     |     |     |     |
|                 |     |           |                          |     |     |     | 2.3 | StudentModelPerformance |     |     |     |     |     |
datagenerationmethodsfoundinliterature:
Weperformsupervisedfinetuningofabasemodel
| • Generate: |          | wesamplek   | prompt-responsepairs |          |             |       |                         |     |         |             |                  |      |             |
| ----------- | -------- | ----------- | -------------------- | -------- | ----------- | ----- | ----------------------- | --- | ------- | ----------- | ---------------- | ---- | ----------- |
|             |          |             |                      |          |             |       | S onthesyntheticdataset |     |         |             | toobtainastudent |      |             |
| from        |          | as few-shot |                      | examples | and         | use T | ϕ                       |     |         |             | T,ℓ              |      |             |
|             |          | seed,ℓ      |                      |          |             |       |                         |     |         |             | D                |      |             |
|             | D        |             |                      |          |             |       | model                   | S   | . Then, | we evaluate |                  | on   | a suite of  |
| to          | generate | a new       | pair (x              | i ,y i ) | conditioned | on    |                         | T,ℓ |         |             | S                | T,ℓ  |             |
|             |          |             |                      |          |             |       | multilingual            |     | tasks   | to assess   | how              | well | the student |
theseexamples.
|              |     |     |                   |     |     |         | haslearnedfromtheteacher. |     |     |     | Thesetasksinclude: |     |     |
| ------------ | --- | --- | ----------------- | --- | --- | ------- | ------------------------- | --- | --- | --- | ------------------ | --- | --- |
| • Translate: |     | we  | forward-translate |     |     | English |                           |     |     |     |                    |     |     |
• Culturalandfactualunderstanding(CULTURE):
| prompts |     | from | to  | the target | language | ℓ   |     |     |     |     |     |     |     |
| ------- | --- | ---- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
D seed,ℓ
weevaluateonGlobal-MMLULite(Singhetal.,
| to  | obtain | x i , and | use T | to generate | the | corre- |     |     |     |     |     |     |     |
| --- | ------ | --------- | ----- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
spondingresponsey . 2025),containingculturallydiverseandrelevant
i
questionsthatwerelocalizedbynativespeakers
| • Respond: |                        | wetakeapromptx |        | from            |     | and    |                                   |     |      |         |     |          |       |
| ---------- | ---------------------- | -------------- | ------ | --------------- | --- | ------ | --------------------------------- | --- | ---- | ------- | --- | -------- | ----- |
|            |                        |                |        | i               |     | seed,ℓ |                                   |     |      |         |     |          |       |
|            |                        |                |        |                 | D   |        | fromEnglish(Hendrycksetal.,2021). |     |      |         |     |          |       |
| useT       | togeneratetheresponsey |                |        |                 | i . |        |                                   |     |      |         |     |          |       |
|            |                        |                |        |                 |     |        | • General                         |     | chat | (CHAT): | we  | evaluate | on M- |
| We         | provide                | a brief        | review | of multilingual |     | syn-   |                                   |     |      |         |     |          |       |
RewardBench(Gurejaetal.,2025)whichmea-
theticdatagenerationmethodsin§6andasupple-
suresthealignmentofmodelswithhumanpref-
mentarysurveyinAppendixA.
erencesinconversationalsettings.
| Data | quality | and diversity |     | metrics | Synthetic |     |                                |     |     |     |     |            |     |
| ---- | ------- | ------------- | --- | ------- | --------- | --- | ------------------------------ | --- | --- | --- | --- | ---------- | --- |
|      |         |               |     |         |           |     | • Mathematicalreasoning(MATH): |     |     |     |     | weevaluate |     |
dataisvaluablewhenitisbothhigh-qualityanddi- onM-GSM(Shietal.,2023),amultilingualver-
verse(Raventosetal.,2023;Chenetal.,2024;Zhu sionoftheGSM8Kdataset(Cobbeetal.,2021)
| et al., | 2025).2 | To estimate |     | the value | of  | , we |                                            |     |     |     |     |     |     |
| ------- | ------- | ----------- | --- | --------- | --- | ---- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|         |         |             |     |           |     | T,ℓ  | thatteststhemodel’sabilitytosolvemathemat- |     |     |     |     |     |     |
D
| computeasetoflexicalandmodel-basedmetrics: |     |     |     |     |     |     | icalwordproblems. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
• Diversity of prompts and responses (d ,d ): InspiredbyKimetal.(2025), wecomputethe
x y
a corpus-level statistic that computes the co- PerformanceGapRecovered(PGR)thatmeasures
| sine | distance | of the | prompt | and | response | em- |                   |     |     |     |                 |     |      |
| ---- | -------- | ------ | ------ | --- | -------- | --- | ----------------- | --- | --- | --- | --------------- | --- | ---- |
|      |          |        |        |     |          |     | theimprovementofS |     |     | T,ℓ | overabasemodelS |     | ϕ on |
beddings. In practice, we use Llama-Embed- abenchmarkbrelativetoareferencemodelS
REF
| Nemotron-8B(Babakhinetal.,2025),thetop- |     |     |     |     |     |     | (Equation2). |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
performingmodelontheMMTEBleaderboard
|                                             |     |     |     |     |     |     |           |     | 1   | (cid:88) | score (S | )   | score (S ) |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | -------- | -------- | --- | ---------- |
| (Enevoldsenetal.,2025),toembedthetexts.     |     |     |     |     |     |     |           |     |     |          | b        | T,ℓ | b ϕ        |
|                                             |     |     |     |     |     |     | Extrinsic | T,ℓ | =   |          |          | −   |            |
|                                             |     |     |     |     |     |     |           |     | B   | score    | (S       | )   | score (S ) |
| • Perplexity(PPL):theperplexityofabasemodel |     |     |     |     |     |     |           |     |     |          | b REF    |     | b ϕ        |
|                                             |     |     |     |     |     |     |           |     | |   | | b∈B    |          | −   |            |
on the response y i conditioned on the prompt whereB = CULTURE,CHAT,MATH
| x              | ,measuringthefluencyandnaturalnessofthe |                              |     |     |     |     |     |     | {   |     |     |     | }   |
| -------------- | --------------------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                | i                                       |                              |     |     |     |     |     |     |     |     |     |     | (2) |
| generatedtext. |                                         | Lowerperplexityindicatesmore |     |     |     |     |     |     |     |     |     |     |     |
coherentandlinguisticallynaturalresponses.
|          |     |            |              |     |        |       | 2.4 | Computing |     | POLYGLOT | SCORE |     |     |
| -------- | --- | ---------- | ------------ | --- | ------ | ----- | --- | --------- | --- | -------- | ----- | --- | --- |
| • Reward |     | score of a | multilingual |     | reward | model |     |           |     |          |       |     |     |
(R): the verbalized score (1-5) of a multilin- Toprovidestraightforwardcomparisonsbetween
gualrewardmodelbasedonrubricsrelatingto teachermodels, PG-SCORE reportsasinglescore
thatcombinesbothextrinsicandintrinsicmetrics
fluency,naturalness,andinstruction-following.
| In  | practice, | we prompt |     | M-Prometheus |     | 14B | asshowninEquation3. |     |     |     |     |     |     |
| --- | --------- | --------- | --- | ------------ | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
2Weuse“dataquality”torefertobothaspectshereafter. PG-SCORET,ℓ = z-score(Intr. +Extr. ) (3)
|     |     |     |     |     |     |     |     |     |     |     | T,ℓ |     | T,ℓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3

TeacherModel Average Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
| Gemma327BInst.   |     | 0.726 |     | 0.145  | 0.360  |     | 1.655 | 1.358 | 0.214  |     | 0.626  |     |
| ---------------- | --- | ----- | --- | ------ | ------ | --- | ----- | ----- | ------ | --- | ------ | --- |
| AyaExpanse32B    |     | 0.706 |     | -0.058 | 0.222  |     | 1.468 | 1.129 | 1.153  |     | 0.320  |     |
| Gemma312BInst.   |     | 0.595 |     | -0.464 | 0.327  |     | 1.756 | 1.228 | 0.151  |     | 0.573  |     |
| CommandA         |     | 0.546 |     | -1.360 | 0.114  |     | 1.673 | 1.102 | 1.063  |     | 0.683  |     |
| Gemma34BInst.    |     | 0.469 |     | -0.488 | 0.330  |     | 1.644 | 0.929 | -0.105 |     | 0.504  |     |
| GPT4omini        |     | 0.461 |     | -1.117 | 0.015  |     | 1.766 | 0.908 | 1.003  |     | 0.189  |     |
| IBMGranite4.0    |     | 0.312 |     | -0.072 | -0.031 |     | 1.000 | 0.734 | -0.079 |     | 0.321  |     |
| IBMGraniteMicro  |     | 0.304 |     | -0.282 | 0.290  |     | 1.102 | 0.783 | -0.329 |     | 0.264  |     |
| Llama3.170BInst. |     | 0.140 |     | -0.964 | 0.109  |     | 1.195 | 0.688 | 0.182  |     | -0.373 |     |
Llama3.18BInst. -0.356 -1.693 -0.974 0.891 0.182 0.322 -0.863
TopmodelswiththehighestPG-SCORE(averageacrosssixlanguages).
| Table1: |     |     |     |     |     |     |     |     | Weevaluateteachermodels |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
withvaryingsizeandmodelfamilyon6typologically-diverselanguages. Foreachlanguage,wehighlightthebest
modelinboldandthesecond-bestmodelwithanunderline. DetailedresultswithstandarderrorsareinTable13.
We combine both intrinsic and extrinsic met- Then,wefinetuneapretrainedOLMo37Bmodel
ricsbecausetheycapturecomplementaryaspects (OLMoTeametal.,2025)oneach T,ℓ toobtain
D
of teacher quality. Extrinsic metrics alone may S . AppendixE.1describesSFTinformation.
T,ℓ
| overlook | the quality | of  | synthetic | data | that | propa- |     |     |     |     |     |     |
| -------- | ----------- | --- | --------- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- |
TeacherModels
WeincludeLlama3.1(8B,70B,
| gates through | the | ecosystem, |     | while | intrinsic | met- |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ----- | --------- | ---- | --- | --- | --- | --- | --- | --- |
Grattafiorietal.,2024),Gemma3(4B,12B,27B,
ricsalonedonotguaranteethatthestudentmodel
GemmaTeametal.,2025),CommandA(Cohere
| achievesstrongdownstreamperformance. |     |     |     |     |     | There- |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Teametal.,2025),AyaExpanse32B(Dangetal.,
sultingPG-SCOREisz-scorenormalized,where0
2024),andIBMGranite(4.0,Micro,GraniteTeam,
indicatesaverageteachereffectiveness,andhigher
|                 |     |        |           |      |         |     | IBM, 2025). | In addition, |     | we also | include | GPT |
| --------------- | --- | ------ | --------- | ---- | ------- | --- | ----------- | ------------ | --- | ------- | ------- | --- |
| scores indicate |     | better | synthetic | data | quality | and |             |              |     |         |         |     |
4omini(OpenAIetal.,2024)asarepresentative
| studentperformanceforthatlanguage. |     |     |             |     | Weadopt |      |                     |     |                      |     |     |     |
| ---------------------------------- | --- | --- | ----------- | --- | ------- | ---- | ------------------- | --- | -------------------- | --- | --- | --- |
|                                    |     |     |             |     |         |      | closed-sourcemodel. |     | SeeTable7inAppendixD |     |     |     |
| equal weighting                    |     | as  | a baseline; | we  | show    | that |                     |     |                      |     |     |     |
fordetailedmodelinformation.
teacherrankingsarerobusttoalternativeweighting
schemesinAppendixG.4. TargetLanguages Weselect6typologicallydi-
|                |     |                  |     |     |     |     | verselanguages: | Arabic(ar),Czech(cs),German |     |       |     |          |
| -------------- | --- | ---------------- | --- | --- | --- | --- | --------------- | --------------------------- | --- | ----- | --- | -------- |
| 3 Experiments: |     | EvaluatingLMsand |     |     |     |     |                 |                             |     |       |     |          |
|                |     |                  |     |     |     |     | (de), Spanish   | (es), Indonesian            |     | (id), | and | Japanese |
PG-SCORE Generalization (ja). Theselanguagesarechosenduetotheirvaria-
|                            |     |     |     |          |     |       | tioninresourceavailability,script,andfamily. |     |     |     |     | This |
| -------------------------- | --- | --- | --- | -------- | --- | ----- | -------------------------------------------- | --- | --- | --- | --- | ---- |
| Inthissection,wemeasurethe |     |     |     | POLYGLOT |     | SCORE |                                              |     |     |     |     |      |
languagechoiceisalsosupportedbypriorworkon
| of state-of-the-art |     | LMs | (§3.1). | Then, |     | we test |     |     |     |     |     |     |
| ------------------- | --- | --- | ------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
informedsampling(Ploegeretal.,2026)thatcon-
| whether | our findings |     | are consistent |     | across | other |     |     |     |     |     |     |
| ------- | ------------ | --- | -------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
siderstypologicalvarietyofthechosenlanguages.
| basemodels(§3.2). |     | Finally,wedetermineifacer- |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SeeTable8inAppendixDforlanguagestatistics.
| tain data | generation | method |     | is more | effective | in  |     |     |     |     |     |     |
| --------- | ---------- | ------ | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
multilingualsettings(§3.3). Weconductadditional Results Table 1 shows the PG-SCORE of each
experimentsandablationsinAppendixG. teacher model across all target languages. The
resultssuggestthefollowing:
3.1 WhichState-of-the-ArtLMsAreGood
|     |     |     |     |     |     |     | • Gemma | 3 27B and | Aya | Expanse |     | 32B are |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------- | --- | ------- |
MultilingualTeachers?
|     |     |     |     |     |     |     | the | most effective | teachers. |     | Gemma | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | ----- | --- |
Setup
In order to evaluate the effectiveness of 27B achieves the highest average PG-SCORE
differentLMsasmultilingualteachers, weselect (0.726),followedcloselybyAyaExpanse32B
10 state-of-the-art models that vary in scale, ar- (0.706),bothoutperforminglargermodelslike
chitecture, and training data, then evaluate them Llama 3.1 70B Inst. (0.140), suggesting that
on 6 typologically diverse languages by generat- modelscalealonedoesnotdetermineteacheref-
ing10.5kprompt-responsepairsforeachteacher- fectiveness. WealsoobservethattheGemma3
language pair where each data generation (§2.2) familydominatesthetopranks,whiletheLlama
methodisequallyrepresented. Werepeatthedata 3.1familyunderperformsonmostlanguages.
generationprocessthreetimeswithdifferentran- • Smaller LMs can be effective multilingual
domseedstoaccountforvariabilityinLMoutputs. teachers. Gemma312B(0.595)and4B(0.469)
4

|     |     |     |     |     |     |     |     |     |     | B   | 4 B | B   | B    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     |     |     | 3 7 | 3   | 8   | 8    |
|     |     |     |     |     |     |     |     |     |     | Mo  | ma  | 3   | ma 3 |
m wen
|                  |     |         |          | BaseModel(S | ϕ)      |          |       |          |      | O L Ge | Q    | Lla  |     |
| ---------------- | --- | ------- | -------- | ----------- | ------- | -------- | ----- | -------- | ---- | ------ | ---- | ---- | --- |
| TeacherModel     |     | OLMo37B | Gemma34B |             | Qwen38B | Llama38B |       |          |      |        |      |      |     |
|                  |     |         |          |             |         |          |       | Llama38B | 0.63 | 0.68*  | 0.57 | 1.00 |     |
| GPT4omini        |     | 0.551   |          | 1.022       | 1.005   |          | 0.621 |          |      |        |      |      |     |
| Llama3.170BInst. |     | 0.138   |          | 0.338       | 1.039   |          | 0.497 |          |      |        |      |      |     |
Llama3.18BInst. −0.160 −0.133 0.365 0.048 Qwen38B 0.60 0.65 1.00
| CommandA       |     | 0.459 |     | 0.725 | 0.974 |     | 0.737 |          |        |      |     |     |     |
| -------------- | --- | ----- | --- | ----- | ----- | --- | ----- | -------- | ------ | ---- | --- | --- | --- |
| AyaExpanse32B  |     | 0.854 |     | 0.762 | 1.183 |     | 0.793 |          |        |      |     |     |     |
| Gemma327BInst. |     | 0.672 |     | 0.810 | 1.301 |     | 0.800 | Gemma34B | 0.87** | 1.00 |     |     |     |
**:p<0.01
| Gemma312BInst.  |     | 0.481 |     | 0.666 | 1.393 |        | 0.804 |         |      |     | *:p<0.05 |     |     |
| --------------- | --- | ----- | --- | ----- | ----- | ------ | ----- | ------- | ---- | --- | -------- | --- | --- |
| Gemma34BInst.   |     | 0.350 |     | 0.712 | 0.545 |        | 1.062 |         |      |     |          |     |     |
|                 |     |       |     |       |       |        |       | OLMo37B | 1.00 |     |          |     |     |
| IBMGranite4.0   |     | 0.283 |     | 0.278 | 0.831 | −0.001 |       |         |      |     |          |     |     |
| IBMGraniteMicro |     | 0.164 |     | 0.455 | 1.079 |        | 0.396 |         |      |     |          |     |     |
PG-SCOREacrossdifferentbasemodels(averageacrossArabic,German,andIndonesian). Left:
Figure2:
AveragePG-SCOREofeachteachermodelonstudentsfinetunedonthreedifferentbasemodels. Wehighlightthe
top, second,and third bestteachermodelsforeachsetting. Right: HeatmapshowingSpearmanrankcorrelation
ρofteachermodelrankingsacrossbasemodels. WeshowpercentageincreasesinPG-SCOREonTable14.
|     |     |     | Arabic(ar) |     |     | German(de) |     |     |     | Indonesian(id) |     |     |     |
| --- | --- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | -------------- | --- | --- | --- |
TeacherModel Generate Translate Respond Generate Translate Respond Generate Translate Respond
Gemma327BInst. 0.032 0.276 0.802 2.140 2.086 1.212 1.189 1.196 0.046
|               |     | −0.276 |     | 0.148 | −1.349 | 1.473 |       |     |       |       |       |     | 1.606 |
| ------------- | --- | ------ | --- | ----- | ------ | ----- | ----- | --- | ----- | ----- | ----- | --- | ----- |
| AyaExpanse32B |     |        |     |       |        |       | 1.255 |     | 1.451 | 0.039 | 0.733 |     |       |
Llama3.170BInst. −0.867 −1.025 −0.215 1.391 0.459 1.187 −0.146 0.089 0.155
Table2: PG-SCOREacrossthreedatagenerationmethods: Generate,Translate,andRespond(§2.2). For
eachdatagenerationmethod,wegenerate10ksamplesperteacher-languagepairandfinetuneastudentmodelon
OLMo37B.WeshowpercentageincreasesinPG-SCOREcomparedtoabaseline(equalrepresentationofthethree
datagenerationmethods)onTable15.
rankamongthetop-5teachers,whiletheLlama Results Figure2showstheaveragePG-SCORE
3.1 70B Inst. (0.140) ranks ninth, suggesting of each teacher model across different base mod-
that smaller LMs can match or exceed larger elswhileTable14showsthepercentageincrease
LMsindatagenerationcapabilities. offamily-matchedteacher-studentpairscompared
Teacherperformancevariessignificantlyby
| •   |     |     |     |     |     | to  | the OLMo | 3   | 7B (mismatch) |     | baseline. |     | We ob- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --- | --------- | --- | ------ |
language. German and Spanish consistently servethatthebestteachermodelsremainconsis-
showthehighestscoresacrossallmodels,while tentacrossdifferentstudentbasemodels,with
Arabic proves challenging with most teach- Gemma327BandAyaExpanse32Bconsistently
ers yielding negative scores, suggesting that ranking among the top three teachers. Further-
language-specific factors influence teacher ef- more, the Gemma 3 family continues to outper-
fectiveness. Wehypothesizethatalanguage’s form other model families. In addition, we find
resourcestatusorpresenceinpretrainingdata that the model rankings vary slightly depending
maycontributetothisvariability(§G.5). on the base model used, as Spearman rank corre-
|                      |     |     |                |     |     | lation    | ranges                              | from | ρ=0.57 | (moderate) |     | to  | ρ=0.87 |
| -------------------- | --- | --- | -------------- | --- | --- | --------- | ----------------------------------- | ---- | ------ | ---------- | --- | --- | ------ |
| 3.2 Generalizationof |     |     | PG-SCOREAcross |     |     |           |                                     |      |        |            |     |     |        |
|                      |     |     |                |     |     | (strong). | Wehypothesizethatthisvariationmaybe |      |        |            |     |     |        |
DifferentBaseModels due to differences in architecture and pretraining
|     |     |     |     |     |     | databetweenbasemodels. |     |     |     | Despitethisvariation, |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --------------------- | --- | --- | --- |
Setup InsteadofusingOLMo37Basthebase
|          |         |         |             |     |     | we        | observe | that | teacher-student |           | model |           | family |
| -------- | ------- | ------- | ----------- | --- | --- | --------- | ------- | ---- | --------------- | --------- | ----- | --------- | ------ |
| model (S | ϕ ) for | student | finetuning, | we  | use | (1)       |         |      |                 |           |       |           |        |
|          |         |         |             |     |     | alignment |         | is a | reliable        | heuristic | for   | achieving |        |
Llama3.18B,(2)Gemma34BPT,and(3)Qwen
|                          |     |     |     |              |     | goodPG-SCORE. |     |     | Forexample,Gemma3teach- |     |     |     |     |
| ------------------------ | --- | --- | --- | ------------ | --- | ------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
| 38BBase(Yangetal.,2025). |     |     |     | WerecomputeS |     | -             |     |     |                         |     |     |     |     |
ϕ
|     |     |     |     |     |     | ers | consistently |     | perform | well | with Gemma |     | 3 stu- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ---- | ---------- | --- | ------ |
dependentmetricssuchasperplexityandPGR.To
|     |     |     |     |     |     | dent | bases, | with | family-matched |     | pairs | achieving |     |
| --- | --- | --- | --- | --- | --- | ---- | ------ | ---- | -------------- | --- | ----- | --------- | --- |
reducecomputationalcosts,wefocusonthreelan-
|                           |        |       |            |            |     | at least | +20.5% |           | higher | PG-SCORE |      | compared | to     |
| ------------------------- | ------ | ----- | ---------- | ---------- | --- | -------- | ------ | --------- | ------ | -------- | ---- | -------- | ------ |
| guages:                   | German | (high | PG-SCORE), | Indonesian |     |          |        |           |        |          |      |          |        |
|                           |        |       |            |            |     | the      | worst  | pair (see | Table  | 14).     | This | finding  | is in- |
| (mid-range),andArabic(low |        |       | PG-SCORE). |            |     |          |        |           |        |          |      |          |        |
5

teresting but reasonable given that models from PC VarianceExpl. Cumulative
| the same | family | likely | share | similar | tokenization |     |     |     |     |       |     |       |     |
| -------- | ------ | ------ | ----- | ------- | ------------ | --- | --- | --- | --- | ----- | --- | ----- | --- |
|          |        |        |       |         |              |     |     | PC1 |     | 42.2% |     | 42.2% |     |
schemes,leadingtoeasiertransferfromteacherto
|     |     |     |     |     |     |     |     | PC2 |     | 22.1% |     | 64.3% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
student. Inaddition,family-matchingisnotahard
|     |     |     |     |     |     |     |     | PC3 |     | 16.5% |     | 80.8% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
constraintunlikeinotherdistillationsettings(on-
|     |     |     |     |     |     |     |     | PC4 |     | 12.6% |     | 93.3% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
policy,Agarwaletal.,2024;Boizardetal.,2025),
|     |     |     |     |     |     |     |     | PC5 |     |     | 3.5% | 96.8% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- |
butitremainsareliableheuristicforteacherselec-
|                                     |     |     |          |      |        |        |     | PC6 |     |     | 3.2% | 100.0% |     |
| ----------------------------------- | --- | --- | -------- | ---- | ------ | ------ | --- | --- | --- | --- | ---- | ------ | --- |
| tionwhentheoptimalteacherisunknown. |     |     |          |      |        | Forour |     |     |     |     |      |        |     |
| core experiment,                    |     | we  | use OLMo | 3 7B | as the | base   |     |     |     |     |      |        |     |
Table4:Varianceexplainedbyprincipalcomponents
modelforfinetuningtocontroltheeffectofmodel
|     |     |     |     |     |     |     | from | intrinsic | data | quality | metrics. | There | are four |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---- | ------- | -------- | ----- | -------- |
familyalignmentwhenevaluatingteacherquality.
principalcomponentsthatexplainover93.3%(cumula-
tive)ofthevariance.
3.3 EffectofSyntheticDataGeneration
| Methodon |     | PG-SCORE |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Setup Inordertodetermineifadatageneration have an impact on teacher effectiveness. In our
method is more effective than others, we gener- core experiment, we sample an equal mix of all
|     |     |     |     |     |     |     | three | methods | (3.5k | each) | to control |     | their effect |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ----- | ----- | ---------- | --- | ------------ |
ate10kprompt-responsepairsforeachmethodin
whenevaluatingteachermodelquality.
| §2.2andcomparethePG-SCOREofeachmix. |     |     |     |     |     | We  |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recomputeintrinsicdataqualitymetricsandfine-
|           |     |         |        |           |       |     | 4   | Analysis: | WhatMakesaGoodPolyglot |     |     |     |     |
| --------- | --- | ------- | ------ | --------- | ----- | --- | --- | --------- | ---------------------- | --- | --- | --- | --- |
| tune OLMo |     | 3 7B to | obtain | a student | model | and |     |           |                        |     |     |     |     |
Teacher?
| evaluate | the | teacher’s | PG-SCORE. |     | We also | com- |     |     |     |     |     |     |     |
| -------- | --- | --------- | --------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
pareeachmixagainstabaselineconsistingof10k
Weinvestigatethefactorsthatcontributetoeffec-
| instances | with | roughly      | equal | number    | of       | samples |                                           |              |     |           |          |     |           |
| --------- | ---- | ------------ | ----- | --------- | -------- | ------- | ----------------------------------------- | ------------ | --- | --------- | -------- | --- | --------- |
|           |      |              |       |           |          |         | tive                                      | multilingual |     | teachers. | We start | by  | analyzing |
| ( 3.3k)   | from | each method. |       | To reduce | computa- |         |                                           |              |     |           |          |     |           |
| ≈         |      |              |       |           |          |         | commonassumptionsaboutteachermodelperfor- |              |     |           |          |     |           |
tionalcosts,weconductthisexperimentonthree
mance,suchassizeandbenchmarkscores(§4.1),
| representative |     | teachers | (Gemma | 3   | 27B, | Aya Ex- |      |           |     |       |           |         |            |
| -------------- | --- | -------- | ------ | --- | ---- | ------- | ---- | --------- | --- | ----- | --------- | ------- | ---------- |
|                |     |          |        |     |      |         | then | determine |     | which | intrinsic | factors | drive stu- |
panse32B,andLlama3.170B)spanninghighto
|     |     |     |     |     |     |     | dentperformance(§4.2). |     |     |     | Lastly,weexaminelan- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | -------------------- | --- | --- |
low PG-SCORE,andthreelanguages(German,In-
|     |     |     |     |     |     |     | guage | properties |     | that might | influence |     | a teacher’s |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ---------- | --------- | --- | ----------- |
donesian,Arabic)coveringdiverseresourcelevels.
PG-SCORE(§G.5).
Results
|     | Table | 2 shows | the | PG-SCORE |     | of each |     |                                     |     |     |     |     |     |
| --- | ----- | ------- | --- | -------- | --- | ------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
|     |       |         |     |          |     |         | 4.1 | Dostrongermodelsmakebetterteachers? |     |     |     |     |     |
datageneration(seeTable15forbaselinecompar-
isons). We observe that for a high-resource lan- Setup In order to determine if there is a rela-
guagelikeGerman,theGeneratemethodyields tionshipbetweenamodel’ssizeorbenchmarkper-
thehighestPG-SCORE,whileforless-resourced formance (i.e., common assumptions to assess a
languages like Arabic and Indonesian, the Re- model’s “strength”) to its effectiveness as a mul-
spondorTranslatemethodsaremoreeffective. tilingualteacher,wefitamixed-effectsmodelre-
WehypothesizethatthisoccursbecausetheGener- gressingPG-SCOREon(a)parametersize(N=27,
atemethoddependsonfew-shotexamplesfromthe 9models,excludingGPT-4o-miniwithunknown
seeddataset,whicharetypicallyofhigherquality size 3trials),and(b)averagemultilingualbench-
×
|                           |     |     |     |                     |     |     | mark | performance |     | on  | Global-MMLU |     | Lite, M- |
| ------------------------- | --- | --- | --- | ------------------- | --- | --- | ---- | ----------- | --- | --- | ----------- | --- | -------- |
| inhigh-resourcelanguages. |     |     |     | Overall,ourfindings |     |     |      |             |     |     |             |     |          |
suggestthatselectingadatagenerationmethodcan GSM, and M-RewardBench (N=180, 10 models
|           |     |     |     |     |     |     |         | 6languages |                                  | 3trials). |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------------------------------- | --------- | --- | --- | --- |
|           |     |     |     |     |     |     | ×       |            | ×                                |           |     |     |     |
| Predictor |     |     |     | β   | SE  | p   | Results |            | Table3showstheregressionresults. |           |     |     | We  |
observethatneitherparametersizenoraverage
| log(Param. |                   | Size) | 0.053           |     | 0.080      | 0.507 |                                |     |           |     |                  |     |               |
| ---------- | ----------------- | ----- | --------------- | --- | ---------- | ----- | ------------------------------ | --- | --------- | --- | ---------------- | --- | ------------- |
|            |                   |       |                 |     |            |       | multilingual                   |     | benchmark |     | performance      |     | signifi-      |
| Avg.       | MultilingualPerf. |       | 1.387           |     | 2.204      | 0.529 |                                |     |           |     |                  |     |               |
|            |                   |       |                 |     |            |       | cantlypredictPG-SCORE(p>0.05). |     |           |     |                  |     | Specifically, |
|            |                   |       |                 |     |            |       | a1-unitincreaseinlog(Param.    |     |           |     | Size)corresponds |     |               |
| Table      | 3: Results        | from  | a mixed-effects |     | regression |       |                                |     |           |     |                  |     |               |
model on PG-SCORE on an LM’s (a) size and (b) toanon-significant0.053increasein PG-SCORE.
avg. multilingualbenchmarkperformance.
|     |     |     |     |     |     | Thelack | Although |     | this finding |     | confirms | the results | of Xu |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ------------ | --- | -------- | ----------- | ----- |
ofsignificantcorrelationsuggeststhatbothpredictors et al. (2025b) and Kim et al. (2025) for English-
arenotsolelysufficienttoensureteachereffectiveness.
basedtasks,weshowthat“stronger”modelsdonot
6

|     | Distinct |       |       |             |       |        |     | 0.50 |     |     |     |     |     |
| --- | -------- | ----- | ----- | ----------- | ----- | ------ | --- | ---- | --- | --- | --- | --- | --- |
|     | Prompts  | 0.073 | 0.654 | 0.008 0.744 | 0.012 | -0.117 |     |      |     |     |     |     |     |
erocSkramhcneBdetciderP
Distinct
|     |     | 0.579 | -0.098 | -0.017 0.111 | -0.660 | 0.456 |     | 0.45 |     |     |     |     |     |
| --- | --- | ----- | ------ | ------------ | ------ | ----- | --- | ---- | --- | --- | --- | --- | --- |
Responses
|     | Perplexity | -0.578 | -0.037 | 0.017 0.211 | 0.075 | 0.784 |     |     |     |     |     |     |     |
| --- | ---------- | ------ | ------ | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
0.40
RubricScore
|     |     | 0.514 | -0.237 | 0.354 0.182 | 0.678 | 0.247 |     |     |     |     |     |     |     |
| --- | --- | ----- | ------ | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
(M-Prometheus)
Avg.Prompt
0.35
|     | Length | -0.079 | 0.388 | 0.838 -0.332 | -0.171 | 0.048 |     |     |     |     |     |     |     |
| --- | ------ | ------ | ----- | ------------ | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
R2=0.664
Avg.Response
|     |        | -0.234 | -0.596 | 0.415 0.497 | -0.265 | -0.318 |     |      |     |     |     | RMSE=0.440 |     |
| --- | ------ | ------ | ------ | ----------- | ------ | ------ | --- | ---- | --- | --- | --- | ---------- | --- |
|     | Length |        |        |             |        |        |     | 0.30 |     |     |     |            |     |
|     |        |        |        |             |        |        |     |      | 0.3 |     | 0.4 |            | 0.5 |
|     |        | PC1    | PC2    | PC3 PC4     | PC5    | PC6    |     |      |     |     |     |            |     |
ActualBenchmarkScore
|     |     |     |     |     |     |     |     |     |     | Arabic | German  | Indonesian |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------- | --- |
|     |     |     | 0.5 | 0.0 | 0.5 |     |     |     |     |        |         |            |     |
|     |     |     | −   |     |     |     |     |     |     | Czech  | Spanish | Japanese   |     |
LoadingStrength
|     |     |     |     |     |     |     | Figure | 4:  | Fit | of a linear | regression | model | on the |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ----------- | ---------- | ----- | ------ |
Figure3:Loadingstrengthofintrinsicmetricsonthe
principalcomponents(PCs). PC1suggeststhatgood PCsoftheintrinsicmetricstopredictstudentper-
teachers produce diverse and high-quality responses, formance. Intrinsic metrics, via their PCs, can pre-
|                                            |     |     |     |     |     |     | dict | extrinsic | student | performance |     | (R2 = | 0.664 and |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- | --------- | ------- | ----------- | --- | ----- | --------- |
| whilePC2focusesonpromptdiversityandlength. |     |     |     |     |     | PC3 |      |           |         |             |     |       |           |
andPC4,together,indicatestheimportanceofprompts RMSE=0.440)onmultilingualbenchmarks(§2.3).
onstudentperformance.
showsthefitofalinearmodelonthetestsetwhen
necessarilymakebettermultilingualteachers. thePCslearntopredictstudentperformance. We
|     |     |     |     |     |     |     | observe |     | that interactions |     | within | the intrinsic | met- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------------- | --- | ------ | ------------- | ---- |
4.2 Whichintrinsicmetricsdetermine
ricscanpredictextrinsicstudentperformancede-
|     | extrinsicstudentmodelperformance? |     |     |     |     |     |         |     |      | R2  |           |      |          |
| --- | --------------------------------- | --- | --- | --- | --- | --- | ------- | --- | ---- | --- | --------- | ---- | -------- |
|     |                                   |     |     |     |     |     | cently, |     | with | =   | 0.664 and | RMSE | = 0.440. |
Setup Inordertoidentifylatentfactorsfromthe Thisfindingsuggeststhatevenwithasimplelinear
|     |     |     |     |     |     |     | model, |     | our chosen | intrinsic |     | metrics | are predic- |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | --------- | --- | ------- | ----------- |
intrinsicmetricsthatexplainstudentperformance,
we perform principal component analysis (PCA) tiveofstudentperformance. Inpractice,thesein-
ontheintrinsicmetricsdescribedin§2.2. Then,we sightscanhelppractitionersselectteachermodels
basedonintrinsicmetricsalone,whicharecheaper
fitaregressionmodeltopredictextrinsicstudent
performance based on the principal components tocomputethanextrinsicstudentevaluations.
(PCs)obtainedfromPCA:wesplit180datapoints
|     |        |     |           |           |      |     | 5   | Discussion: |     | TowardsaRecipefor |     |     |     |
| --- | ------ | --- | --------- | --------- | ---- | --- | --- | ----------- | --- | ----------------- | --- | --- | --- |
| (10 | models | 6   | languages | 3 trials) | into | 80% |     |             |     |                   |     |     |     |
|     |        | ×   |           | ×         |      |     |     |             |     |                   |     |     |     |
MultilingualSyntheticDataGeneration
| train | and 20% | test, | then | train a linear | regression |     |     |     |     |     |     |     |     |
| ----- | ------- | ----- | ---- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
modelwiththePCsasthefeaturesandthestudent
Ourresultsprovideactionableinsightsforselect-
performanceasthetarget.
|     |     |     |     |     |     |     | ing | and | effectively | using | teacher | models | in mul- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | ------ | ------- |
Results Table4showshowmuchofthevariance tilingualsyntheticdatageneration. First, we find
is explained by each principal component while that model scale does not significantly predict
Figure 3 shows the loading strength of each in- teachereffectiveness: Llama3.170BInstruct,de-
trinsic metric on the principal components. We spite being the largest model evaluated, ranks at
observethatthefirstfourPCsexplainover93.3% the bottom half in PG-SCORE across all student
ofthevarianceintheintrinsicdataqualitymetrics. basemodelswetested(§3.1,§3.2). Ouranalyses
Specifically, PC 1 (42.2%) captures characteris- suggestthatwhatmattersinsteadisthequalityof
ticssuchaslowerresponseperplexityandhigh generateddata: promptdiversity,responsefluency,
distinctiveness, PC2 (22.1%) captures variance and length collectively capture over 93% of the
in characteristics such as higher prompt diver- variance in intrinsic data quality and predict stu-
| sity | and length, |     |         |             |     |         | dentperformancewithR2=0.664(§4.2),offering |     |     |     |     |     |     |
| ---- | ----------- | --- | ------- | ----------- | --- | ------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|      |             |     | whereas | PC3 (16.5%) |     | and PC4 |                                            |     |     |     |     |     |     |
(12.6%)capturevariancethatreinforcetrendson practitioners a cheaper alternative to full student
promptlengthanddiversity. Inaddition,Figure4 trainingrunsforscreeningteachercandidates.
7

Second, whentheoptimalteacherisunknown, multilingualsyntheticdatageneration,distillthem
matchingmodelfamiliesoffersareliableheuris-
|     |     |     |     |     |     |     | into three | strategies, |     | and | test each | in  | isolation. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | --------- | --- | ---------- |
ticforteacherselection. Gemmateacherspaired Thissetupenabledustoprovidepractitionerswith
with Gemma students, and Llama teachers with empirically-grounded recipe on selecting teacher
Llamastudents,outperformamismatchedbaseline LMsthatwehopetobeapplicableacrossanygen-
| by at least | 20% | (Figure | 2). | We hypothesize |     | this | erationmethod. |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | -------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
findingreflectssharedtokenizationandsimilarpre-
|     |     |     |     |     |     |     | Evaluating | and | Improving |     | the | Synthetic | Data |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- | --------- | ---- |
trainingdistributions,thoughdisentanglingthese
|     |     |     |     |     |     |     | Pipeline | While | prior | works | have | evaluated | as- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----- | ----- | ---- | --------- | --- |
factorsremainsfuturework.
pectsofthesyntheticdatapipeline,theytypically
| Finally,                             | we             | find | that           | there are    | language-   |       |                                |        |               |            |           |                 |         |
| ------------------------------------ | -------------- | ---- | -------------- | ------------ | ----------- | ----- | ------------------------------ | ------ | ------------- | ---------- | --------- | --------------- | ------- |
|                                      |                |      |                |              |             |       | dosoinisolation(i.e.,intrinsic |        |               |            |           | extrinsic)orfo- |         |
| dependent                            | considerations |      |                | for data     | generation. |       |                                |        |               |            | ⊕         |                 |         |
|                                      |                |      |                |              |             |       | cus exclusively                |        | on English    |            | (Zhang    | et al.,         | 2025a). |
| Forhigh-resourcelanguageslikeGerman, |                |      |                |              |             | where |                                |        |               |            |           |                 |         |
|                                      |                |      |                |              |             |       | For instance,                  |        | Kim et        | al. (2025) | evaluated |                 | teacher |
| seed data                            | quality        | is   | high,          | the Generate | method      |       |                                |        |               |            |           |                 |         |
|                                      |                |      |                |              |             |       | models                         | solely | as a function |            | of        | extrinsic       | student |
| performs                             | best.          | For  | less-resourced | languages    |             | like  |                                |        |               |            |           |                 |         |
performanceonEnglishtasks(e.g.,reasoningand
ArabicandIndonesian,methodsthatleverageex-
coding),whileCaietal.(2025)’sOpenDataArena
istingprompts(Respond)ortransferfromEnglish
focusesonintrinsicdataquality(model-basedand
(Translate)canyieldsubstantialgainsoverauni-
|     |     |     |     |     |     |     | heuristic)toscoremodels. |     |     |     | Signalsofmultilingual |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --------------------- | --- | --- |
formmixofmethods,thoughthemagnitudevaries
|            |        |     |     |                    |     |      | data quality | are | often | a function |     | of corpus-level |     |
| ---------- | ------ | --- | --- | ------------------ | --- | ---- | ------------ | --- | ----- | ---------- | --- | --------------- | --- |
| by teacher | (Table | 2). | For | truly low-resource |     | lan- |              |     |       |            |     |                 |     |
diversity(ArtetxeandSchwenk,2019;Enevoldsen
guages,werecommendcombiningsyntheticdata
etal.,2025;Sametal.,2025)andgenerationqual-
generationwithtargeteddatacollection.
ity(Pombaletal.,2025;Anugrahaetal.,2026)On
Asasupplementary,wedemonstratetheapplica-
theotherhand,multilingualLMsaretypicallyeval-
bilityofourfindingsbybuildingamultilingualsyn-
|     |     |     |     |     |     |     | uated on | general-knowledge |     |     | and | culture-specific |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | --- | --- | ---------------- | --- |
theticdatarecipeforaheld-outlanguage,Tagalog,
benchmarks(Qinetal.,2025;GemmaTeametal.,
| inAppendixI. |        | Weshowthatmodelstrainedusing |          |      |           |     |                 |     |     |            |       |        |       |
| ------------ | ------ | ---------------------------- | -------- | ---- | --------- | --- | --------------- | --- | --- | ---------- | ----- | ------ | ----- |
|              |        |                              |          |      |           |     | 2025; Salamanca |     | et  | al., 2026, | inter | alia). | These |
| our recipe   | (based | on                           | analyses | from | PG-SCORE) |     |                 |     |     |            |       |        |       |
practicesinformedourchoiceofintrinsicandex-
| have better | performance |     |          | on an unseen   | Filipino- |     |            |          |            |                           |            |     |          |
| ----------- | ----------- | --- | -------- | -------------- | --------- | --- | ---------- | -------- | ---------- | ------------------------- | ---------- | --- | -------- |
|             |             |     |          |                |           |     | trinsic    | metrics  | throughout |                           | this work. |     | More im- |
| centric     | benchmark,  |     | and that | each component |           | of  |            |          |            |                           |            |     |          |
|             |             |     |          |                |           |     | portantly, | PG-SCORE |            | providesaholisticanalysis |            |     |          |
ourrecommendation(e.g.,choosetopteacherfrom
thatcombinesbothintrinsicdataqualityandextrin-
| Table1,matchmodelfamilies,etc.) |     |     |     | resultedinob- |     |     |             |            |     |             |     |     |          |
| ------------------------------- | --- | --- | --- | ------------- | --- | --- | ----------- | ---------- | --- | ----------- | --- | --- | -------- |
|                                 |     |     |     |               |     |     | sic student | downstream |     | performance |     | to  | evaluate |
servableperformancegains. Thissuggeststhatour teachermodelsacrossvariousgenerationmethods.
evaluationprotocolisrobustthattheinsightstrans-
| fer to an | unseen | language, |     | even when | measured |     | 7 Conclusion |     |     |     |     |     |     |
| --------- | ------ | --------- | --- | --------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
withadifferentsetofdownstreammetrics.
Weconductacomprehensiveevaluationofstate-of-
the-artLMsasmultilingualteachersforsynthetic
6 RelatedWork
|     |     |     |     |     |     |     | data generation |               | by assessing |         | both  | intrinsic    | data |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ------------ | ------- | ----- | ------------ | ---- |
|     |     |     |     |     |     |     | quality         | and extrinsic |              | student | model | performance. |      |
SyntheticDataGenerationforMultilingualSFT
Wefindseveralpropertiesthatcontributetoteacher
| In order | to offset | the | high | costs of recruiting |     | lan- |     |     |     |     |     |     |     |
| -------- | --------- | --- | ---- | ------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
guage experts for data collection, prior works re- effectivenessoutsideofmodelsizeorbenchmark
lied on generating synthetic datasets. This ef- performance, such as prompt-response diversity,
|     |     |     |     |     |     |     | fluency,andlanguagerepresentation. |     |     |     |     | Finally,we |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ---------- | --- |
fortresultedinlargemultilingualdatasetssuchas
|            |             |     |     |                |          |     | outline | practical | recommendations |     |     | for | creating a |
| ---------- | ----------- | --- | --- | -------------- | -------- | --- | ------- | --------- | --------------- | --- | --- | --- | ---------- |
| Bactrian-X | (Translate, |     | Li  | et al., 2023), | MultiAl- |     |         |           |                 |     |     |     |            |
paca (Generate, Wei et al., 2023), and xP3 (Re- multilingualsyntheticdatagenerationrecipe. We
|     |     |     |     |     |     |     | hope our | findings | guide | future | work | on  | develop- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | ------ | ---- | --- | -------- |
spond,Muennighoffetal.,2023)thatwerecreated
inginclusivelanguagetechnologiesthroughhigh-
| through | various | data | generation | methods. |     | These |     |     |     |     |     |     |     |
| ------- | ------- | ---- | ---------- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
workshavedifferentdatagenerationrecipes,and qualitysyntheticdata.
| so we provide |     | a brief | survey | of these | works | and |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Limitations
| their recipes |     | in Appendix |     | A, then classify |     | them |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
acrossthethreestrategies/archetypes(Generate, Our work comes with some limitations and open
Translate,Response;2.2). Buildingontheseprior questions left for future work. For example, our
efforts, we examine the three core strategies for languagesetencompassessixlanguages. Although
8

we chose these languages carefully based on (1) ProceedingsoftheFourthWorkshoponGeneration,
EvaluationandMetrics(GEM²),pages927–946,Vi-
whethertheycanbeevaluatedonpublicly-available
|     |     |     |     |     |     | enna, Austria | and | virtual | meeting. | Association | for |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ----------- | --- |
LMbenchmarksand(2)priortheoreticalworkon
ComputationalLinguistics.
| principled | test | language | selection | (Ploeger | et al., |                 |                        |     |     |     |       |
| ---------- | ---- | -------- | --------- | -------- | ------- | --------------- | ---------------------- | --- | --- | --- | ----- |
|            |      |          |           |          |         | Anthropic.2024. | TheClaude3ModelFamily: |     |     |     | Opus, |
2026),validatingourfindingsacrossabroaderlan-
guage sample remains important future work. In Sonnet,Haiku. Technicalreport,Anthropic.
addition,ourTranslatedatagenerationmethodas-
|     |     |     |     |     |     | David Anugraha, | Shou-Yi |     | Hung, | Zilu | Tang, En- |
| --- | --- | --- | --- | --- | --- | --------------- | ------- | --- | ----- | ---- | --------- |
sumesaccesstoEnglishpromptsthatcanbemean- ShiunAnnieLee,DerryTantiWijaya,andGentaIn-
ingfully translated to target languages. This ap- dra Winata. 2026. mR3: Multilingual Rubric-
|        |          |             |      |          |       | AgnosticRewardReasoningModels. |     |     |     | InTheFour- |     |
| ------ | -------- | ----------- | ---- | -------- | ----- | ------------------------------ | --- | --- | --- | ---------- | --- |
| proach | inherits | limitations | from | LM-based | tech- |                                |     |     |     |            |     |
teenthInternationalConferenceonLearningRepre-
| niques | such as | localizing | culture-specific |     | refer- | sentations. |     |     |     |     |     |
| ------ | ------- | ---------- | ---------------- | --- | ------ | ----------- | --- | --- | --- | --- | --- |
ences,introducingtranslationeseartifacts.
|     |     |     |     |     |     | Mikel Artetxe | and Holger | Schwenk. |     | 2019. | Margin- |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | -------- | --- | ----- | ------- |
EthicsStatement basedParallelCorpusMiningwithMultilingualSen-
|     |     |     |     |     |     | tenceEmbeddings. |     | InProceedingsofthe57thAn- |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------- | --- | --- | --- |
nualMeetingoftheAssociationforComputational
Syntheticdatagenerationrisksamplifyingbiases
Linguistics,pages3197–3203,Florence,Italy.Asso-
| presentinteachermodels. |     |     | Ifateachermodelunder- |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ciationforComputationalLinguistics.
performsoncertainlanguagesorexhibitscultural
|     |     |     |     |     |     | Viraat Aryabumi, |     | John Dang, | Dwarak |     | Talupuru, |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ------ | --- | --------- |
biases,theseweaknessespropagatetostudentmod-
|                         |     |     |                       |     |     | Saurabh    | Dash, David | Cairuz, | Hangyu | Lin,  | Bharat  |
| ----------------------- | --- | --- | --------------------- | --- | --- | ---------- | ----------- | ------- | ------ | ----- | ------- |
| elstrainedonitsoutputs. |     |     | Ourfindingthatteacher |     |     |            |             |         |        |       |         |
|                         |     |     |                       |     |     | Venkitesh, | Madeline    | Smith,  | Jon    | Ander | Campos, |
effectivenesscorrelateswithCommonCrawlrepre-
|     |     |     |     |     |     | Yi Chern | Tan, Kelly | Marchisio, |     | Max Bartolo, | Se- |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ---------- | --- | ------------ | --- |
sentation(ρ = 0.886,basedonsixlanguages)sug- bastianRuder,AcyrLocatelli,JuliaKreutzer,Nick
Frosst,AidanGomez,PhilBlunsom,MarziehFadaee,
geststhatalreadyunderrepresentedlanguagesmay
|     |     |     |     |     |     | and 2 others. | 2024. | Aya | 23: | Open | Weight Re- |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | --- | ---- | ---------- |
befurtherdisadvantagedinsyntheticdatapipelines,
|     |     |     |     |     |     | leases to | Further | Multilingual | Progress. |     | Preprint, |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ------------ | --------- | --- | --------- |
potentiallywideningtheperformancegapbetween
arXiv:2405.15032.
high-andlow-resourcelanguages.
YauhenBabakhin,RadekOsmulski,RonayAk,Gabriel
| Acknowledgments |     |                    |     |             |        | Moreira,MengyaoXu,BenediktSchifferer,BoLiu, |                   |                |                       |       |           |
| --------------- | --- | ------------------ | --- | ----------- | ------ | ------------------------------------------- | ----------------- | -------------- | --------------------- | ----- | --------- |
|                 |     |                    |     |             |        | andEvenOldridge.2025.                       |                   |                | Llama-Embed-Nemotron- |       |           |
|                 |     |                    |     |             |        | 8B: A Universal                             |                   | Text Embedding |                       | Model | for Mul-  |
| LJVM and        | AK  | acknowledge        |     | the support | of the |                                             |                   |                |                       |       |           |
|                 |     |                    |     |             |        | tilingual                                   | and Cross-Lingual |                | Tasks.                |       | Preprint, |
| UKRI Frontier   |     | Grant EP/Y031350/1 |     | (EQUATE).   |        |                                             |                   |                |                       |       |           |
arXiv:2511.07025.
Thisworkwasperformedusingjointresourcespro-
vided by the Cambridge Service for Data Driven NicolasBoizard,KevinElHaddad,CelineHudelot,and
Discovery(CSD3)EP/T022159/1,IsambardAINa- Pierre Colombo. 2025. Towards Cross-Tokenizer
|     |     |     |     |     |     | Distillation: | theUniversalLogitDistillationLossfor |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------ | --- | --- | --- | --- |
tionalAIResearchResource(AIRR)ST/AIRR/I-A-
|                                      |     |     |     |     |      | LLMs. TransactionsonMachineLearningResearch. |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ---- | -------------------------------------------- | --- | --- | --- | --- | --- |
| I/1023,andtheMicrosoftResearchGrant. |     |     |     |     | LJVM |                                              |     |     |     |     |     |
SamuelCahyawijaya,HolyLovenia,FajriKoto,Rifki
wouldalsoliketothankSongboHu,ChenCecilia
Putri,WawanCenggoro,JhonsonLee,SalsabilAk-
Liu,MillicentOchieng,andFelerminoAliforhelp-
|     |     |     |     |     |     | bar, Emmanuel | Dave, | Nuurshadieq |     | Nuurshadieq, |     |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ----------- | --- | ------------ | --- |
fulandproductivediscussionsontheproject.
MuhammadMahendra,RrPutri,BryanWilie,Genta
|            |     |     |     |     |     | Winata,                                        | Alham Aji, | Ayu                          | Purwarianti, | and     | Pascale |
| ---------- | --- | --- | --- | --- | --- | ---------------------------------------------- | ---------- | ---------------------------- | ------------ | ------- | ------- |
|            |     |     |     |     |     | Fung.2024.                                     | Cendol:    | Openinstruction-tunedgenera- |              |         |         |
| References |     |     |     |     |     | tivelargelanguagemodelsforIndonesianlanguages. |            |                              |              |         |         |
|            |     |     |     |     |     | In Proceedings                                 | of         | the 62nd                     | Annual       | Meeting | of the  |
RishabhAgarwal,NinoVieillard,YongchaoZhou,Piotr
AssociationforComputationalLinguistics(Volume1:
Stanczyk,SabelaRamosGarea,MatthieuGeist,and
LongPapers),pages14899–14914,Bangkok,Thai-
| Olivier | Bachem. | 2024. | On-Policy | Distillation | of  |     |     |     |     |     |     |
| ------- | ------- | ----- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
land.AssociationforComputationalLinguistics.
| Language | Models: | Learning | from | Self-Generated |     |     |     |     |     |     |     |
| -------- | ------- | -------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Mistakes. InTheTwelfthInternationalConference Mengzhang Cai, Xin Gao, Yu Li, Honglin Lin,
onLearningRepresentations. ZhengLiu,ZhuoshiPan,QizhiPei,XiaoranShang,
MengyuanSun,ZinanTang,XiaoyangWang,Zhan-
Sanchit Ahuja, Kumar Tanmay, Hardik Hansrajbhai ping Zhong, Yun Zhu, Dahua Lin, Conghui He,
Chauhan,BarunPatra,KritiAggarwal,LucianoDel
|        |         |        |       |         |           | andLijunWu.2025. |     | OpenDataArena: |     |     | AFairand |
| ------ | ------- | ------ | ----- | ------- | --------- | ---------------- | --- | -------------- | --- | --- | -------- |
| Corro, | Arindam | Mitra, | Tejas | Indulal | Dhamecha, |                  |     |                |     |     |          |
OpenArenaforBenchmarkingPost-TrainingDataset
Ahmed Hassan Awadallah, Monojit Choudhury, Value. Preprint,arXiv:2512.14051.
| Vishrav | Chaudhary, | and | Sunayana | Sitaram. | 2025. |     |     |     |     |     |     |
| ------- | ---------- | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
sPhinX: Sample Efficient Multilingual Instruction Hao Chen, Abdul Waheed, Xiang Li, Yidong Wang,
Fine-TuningThroughN-shotGuidedPrompting. In Jindong Wang, Bhiksha Raj, and Marah I. Abdin.
9

2024. OntheDiversityofSyntheticDataanditsIm- Srishti Gureja, Lester James Validad Miranda,
pactonTrainingLargeLanguageModels. Preprint, Shayekh Bin Islam, Rishabh Maheshwary, Drishti
arXiv:2410.15226. Sharma,GustiTriandiWinata,NathanLambert,Se-
|     |     |     |     |     |     | bastian | Ruder, | Sara | Hooker, | and | Marzieh | Fadaee. |
| --- | --- | --- | --- | --- | --- | ------- | ------ | ---- | ------- | --- | ------- | ------- |
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, 2025. M-RewardBench: EvaluatingRewardModels
MarkChen,HeewooJun,LukaszKaiser,Matthias inMultilingualSettings. InProceedingsofthe63rd
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro AnnualMeetingoftheAssociationforComputational
Nakano, Christopher Hesse, and John Schulman. Linguistics(Volume1: LongPapers),pages43–58,
2021. TrainingVerifierstoSolveMathWordProb- Vienna,Austria.AssociationforComputationalLin-
| lems. | Preprint,arXiv:2110.14168. |     |     |     |     | guistics. |     |     |     |     |     |     |
| ----- | -------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
CohereTeam,Aakanksha,ArashAhmadian,Marwan NathanHabib,ClémentineFourrier,HynekKydlícˇek,
Ahmed,JayAlammar,MiladAlizadeh,YazeedAl- ThomasWolf,andLewisTunstall.2023. LightEval:
numay,SophiaAlthammer,ArkadyArkhangorodsky, AlightweightframeworkforLLMevaluation.
ViraatAryabumi,DennisAumiller,RaphaëlAvalos,
HasanAbedAlKaderHammoud,MohamadBilalZbib,
| Zahara                              | Aviv, | Sammie      | Bae, Saurabh |           | Baji, Alexan- |                                     |                |                               |             |                     |               |       |
| ----------------------------------- | ----- | ----------- | ------------ | --------- | ------------- | ----------------------------------- | -------------- | ----------------------------- | ----------- | ------------------- | ------------- | ----- |
|                                     |       |             |              |           |               | andBernardGhanem.2026.              |                |                               |             | HalaTechnicalReport |               |       |
| dre Barbet,                         | Max   | Bartolo,    | Björn        | Bebensee, | Neeral        |                                     |                |                               |             |                     |               |       |
|                                     |       |             |              |           |               | Building                            | Arabic-Centric |                               | Instruction |                     | & Translation |       |
| Beladia,                            | and   | 210 others. | 2025.        | Command   | A: An         |                                     |                |                               |             |                     |               |       |
|                                     |       |             |              |           |               | ModelsatScale.                      |                | InProceedingsofthe2ndWorkshop |             |                     |               |       |
| Enterprise-ReadyLargeLanguageModel. |       |             |              |           | Preprint,     |                                     |                |                               |             |                     |               |       |
|                                     |       |             |              |           |               | onNLPforLanguagesUsingArabicScript, |                |                               |             |                     |               | pages |
arXiv:2504.00698.
236–244,Rabat,Morocco.AssociationforComputa-
tionalLinguistics.
| John Dang, | Shivalika | Singh, | Daniel | D’souza, | Arash |     |     |     |     |     |     |     |
| ---------- | --------- | ------ | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Ahmadian,AlejandroSalamanca,MadelineSmith,
|     |     |     |     |     |     | Daniel Han, | Michael | Han, | and | Unsloth | Team. | 2023. |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ---- | --- | ------- | ----- | ----- |
AidanPeppin,SungjinHong,ManojGovindassamy,
Unsloth.
| TerrenceZhao, |     | SandraKublik, |     | MeorAmer, | Viraat |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Aryabumi,JonAnderCampos,Yi-ChernTan,Tom DanHendrycks,CollinBurns,StevenBasart,AndyZou,
Kocmi,FlorianStrub,NathanGrinsztajn,YannisFlet- MantasMazeika,DawnSong,andJacobSteinhardt.
Berliac,and26others.2024. AyaExpanse: Combin- 2021. MeasuringMassiveMultitaskLanguageUn-
ingResearchBreakthroughsforaNewMultilingual
|           |                            |     |     |     |     | derstanding.        |     | InInternationalConferenceonLearn- |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | ------------------- | --- | --------------------------------- | --- | --- | --- | --- |
| Frontier. | Preprint,arXiv:2412.04261. |     |     |     |     | ingRepresentations. |     |                                   |     |     |     |     |
Kenneth Enevoldsen, Isaac Chung, Imene Kerboua, PratikJoshi, SebastinSanty, AmarBudhiraja, Kalika
Márton Kardos, Ashwin Mathur, David Stap, Bali,andMonojitChoudhury.2020. TheStateand
Jay Gala, Wissam Siblini, Dominik Krzemin´ski, FateofLinguisticDiversityandInclusionintheNLP
|       |       |              |         |         |         | World. | InProceedingsofthe58thAnnualMeetingof |     |     |     |     |     |
| ----- | ----- | ------------ | ------- | ------- | ------- | ------ | ------------------------------------- | --- | --- | --- | --- | --- |
| Genta | Indra | Winata, Saba | Sturua, | Saiteja | Utpala, |        |                                       |     |     |     |     |     |
theAssociationforComputationalLinguistics,pages
MathieuCiancone,MarionSchaeffer,DigantaMisra,
Shreeya Dhakal, Jonathan Rystrøm, Roman Solo- 6282–6293,Online.AssociationforComputational
| matin, | Ömer    | Veysel Çag˘atan, |     | and 63 | others. 2025. | Linguistics. |     |     |     |     |     |     |
| ------ | ------- | ---------------- | --- | ------ | ------------- | ------------ | --- | --- | --- | --- | --- | --- |
| MMTEB: | Massive | Multilingual     |     | Text   | Embedding     |              |     |     |     |     |     |     |
Benchmark. In The Thirteenth International Con- Armand Joulin, Edouard Grave, Piotr Bojanowski,
MatthijsDouze,HérveJégou,andTomasMikolov.
ferenceonLearningRepresentations.
|     |     |     |     |     |     | 2016.   | FastText.zip:              | Compressingtextclassification |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------------------------- | ----------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | models. | Preprint,arXiv:1612.03651. |                               |     |     |     |     |
GemmaTeam,AishwaryaKamath,JohanFerret,Shreya
Pathak,NinoVieillard,RamonaMerhej,SarahPerrin,
ArmandJoulin,EdouardGrave,PiotrBojanowski,and
| Tatiana | Matejovicova, |     | Alexandre | Ramé, | Morgane |       |          |       |     |           |     |           |
| ------- | ------------- | --- | --------- | ----- | ------- | ----- | -------- | ----- | --- | --------- | --- | --------- |
|         |               |     |           |       |         | Tomas | Mikolov. | 2017. | Bag | of Tricks | for | Efficient |
Rivière,LouisRouillard,ThomasMesnard,Geoffrey
|     |     |     |     |     |     | TextClassification. |     | InProceedingsofthe15thCon- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------------------- | --- | --- | --- | --- |
Cideron,JeanbastienGrill,SabelaRamos,Edouard
ferenceoftheEuropeanChapteroftheAssociation
Yvinec,MichelleCasbon,EtiennePot,IvoPenchev,
|                    |     |     |                        |     |     | forComputationalLinguistics: |     |     |           | Volume2,ShortPa-  |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | ---------------------------- | --- | --- | --------- | ----------------- | --- | --- |
| and197others.2025. |     |     | Gemma3TechnicalReport. |     |     |                              |     |     |           |                   |     |     |
|                    |     |     |                        |     |     | pers, pages427–431,          |     |     | Valencia, | Spain.Association |     |     |
Preprint,arXiv:2503.19786.
forComputationalLinguistics.
GraniteTeam,IBM.2025. Granite4.0LanguageMod- ShivaniKapania,StephanieBallard,AlexKessler,and
els. https://huggingface.co/collections/ Jennifer Wortman Vaughan. 2025. Examining the
ibm-granite/granite-40-language-models.
ExpandingRoleofSyntheticDataThroughoutthe
| Accessed: | 2025-12-08. |     |     |     |     |                        |            |     |                        |                 |     |     |
| --------- | ----------- | --- | --- | --- | --- | ---------------------- | ---------- | --- | ---------------------- | --------------- | --- | --- |
|           |             |     |     |     |     | AIDevelopmentPipeline. |            |     | InProceedingsofthe2025 |                 |     |     |
|           |             |     |     |     |     | ACM                    | Conference | on  | Fairness,              | Accountability, |     | and |
AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri, Transparency,FAccT’25,pages45–60,NewYork,
Abhinav Pandey, Abhishek Kadian, Ahmad Al- NY,USA.AssociationforComputingMachinery.
| Dahle, | Aiesha | Letman, | Akhil | Mathur, | Alan Schel- |     |     |     |     |     |     |     |
| ------ | ------ | ------- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ten,AlexVaughan,AmyYang,AngelaFan,Anirudh JaredKaplan,SamMcCandlish,TomHenighan,TomB.
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi- Brown,BenjaminChess,RewonChild,ScottGray,
tra, Archie Sravankumar, Artem Korenev, Arthur AlecRadford,JeffreyWu,andDarioAmodei.2020.
Hinsvark,and542others.2024. TheLlama3Herd Scalinglawsforneurallanguagemodels. Preprint,
| ofModels. | Preprint,arXiv:2407.21783. |     |     |     |     | arXiv:2001.08361. |     |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
10

Seungone Kim, Juyoung Suk, Xiang Yue, Vijay Pombal, Nicolas Boizard, Manuel Faysse, Pierre
Viswanathan,SeongyunLee,YizhongWang,Kiril Colombo,FrançoisYvon,BarryHaddow,JoséG.C.
Gashteovski,CarolinLawrence,SeanWelleck,and deSouza,AlexandraBirch,andAndréF.T.Martins.
Preprint,
GrahamNeubig.2025. Evaluatinglanguagemodels 2025. EuroLLM-9B: Technical Report.
| assyntheticdatagenerators. |     | InProceedingsofthe | arXiv:2506.04079. |     |     |     |
| -------------------------- | --- | ------------------ | ----------------- | --- | --- | --- |
63rdAnnualMeetingoftheAssociationforCompu-
tationalLinguistics(Volume1: LongPapers),pages PedroHenriqueMartins,PatrickFernandes,JoãoAlves,
6385–6403,Vienna,Austria.AssociationforCompu- NunoM.Guerreiro,RicardoRei,DuarteM.Alves,
tationalLinguistics. José Pombal, Amin Farajian, Manuel Faysse, Ma-
teuszKlimaszewski,PierreColombo,BarryHaddow,
Yoon Kim and Alexander M. Rush. 2016. Sequence- JoséG.C.deSouza,AlexandraBirch,andAndréF.T.
levelknowledgedistillation. InProceedingsofthe Martins. 2024. EuroLLM: Multilingual Language
2016 Conference on Empirical Methods in Natu- ModelsforEurope. Preprint,arXiv:2409.16235.
ralLanguageProcessing,pages1317–1327,Austin,
Texas.AssociationforComputationalLinguistics. LesterJamesValidadMiranda,ElyanahAco,ConnerG.
Manuel,JanChristianBlaiseCruz,andJosephMar-
AnoopKunchukuttan,RajDabre,RudraMurthy,Mo- vin Imperial. 2025. FilBench: Can LLMs Under-
|     |     |     |     |     |     | Proceedings of |
| --- | --- | --- | --- | --- | --- | -------------- |
hammed Safi Ur Rahman Khan, and Thanmay stand and Generate Filipino? In
Jayakumar. 2025. Data and Model Centric Ap- the2025ConferenceonEmpiricalMethodsinNatu-
proachesforExpansionofLargeLanguageModels ralLanguageProcessing,pages2496–2529,Suzhou,
toNewlanguages. InProceedingsofthe2025Con- China.AssociationforComputationalLinguistics.
ferenceonEmpiricalMethodsinNaturalLanguage
NiklasMuennighoff,ThomasWang,LintangSutawika,
Processing:TutorialAbstracts,pages12–13,Suzhou,
|     |     |     | Adam Roberts, | Stella | Biderman, | Teven Le Scao, |
| --- | --- | --- | ------------- | ------ | --------- | -------------- |
China.AssociationforComputationalLinguistics.
|     |     |     | MSaifulBari, | ShengShen, | ZhengXinYong, | Hai- |
| --- | --- | --- | ------------ | ---------- | ------------- | ---- |
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying ley Schoelkopf, Xiangru Tang, Dragomir Radev,
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Alham Fikri Aji, Khalid Almubarak, Samuel Al-
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Ef- banie,ZaidAlyafeai,AlbertWebson,EdwardRaff,
|                                 |            |                    | and Colin                       | Raffel. 2023. | Crosslingual | Generaliza-   |
| ------------------------------- | ---------- | ------------------ | ------------------------------- | ------------- | ------------ | ------------- |
| ficient Memory                  | Management | for Large Language |                                 |               |              |               |
|                                 |            |                    | tionthroughMultitaskFinetuning. |               |              | InProceedings |
| ModelServingwithPagedAttention. |            | InProceedings      |                                 |               |              |               |
oftheACMSIGOPS29thSymposiumonOperating of the 61st Annual Meeting of the Association for
SystemsPrinciples. ComputationalLinguistics(Volume1: LongPapers),
pages15991–16111,Toronto,Canada.Association
Nathan Lambert, Jacob Morrison, Valentina Pyatkin, forComputationalLinguistics.
| Shengyi Huang, | Hamish           | Ivison, Faeze Brahman, |             |            |         |             |
| -------------- | ---------------- | ---------------------- | ----------- | ---------- | ------- | ----------- |
|                |                  |                        | Raymond Ng, | Thanh Ngan | Nguyen, | Huang Yuli, |
| Lester James   | Validad Miranda, | Alisa Liu,             | Nouha       |            |         |             |
TaiNgeeChia,LeongWaiYi,WeiQiLeong,Xianbin
Dziri,XinxiLyu,YulingGu,SaumyaMalik,Victoria
Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Yong,JianGangNgui,YosephineSusanto,Nicholas
Bras, Oyvind Tafjord, Christopher Wilhelm, Luca Cheng,HamsawardhiniRengarajan,PeeratLimkon-
Soldaini,and4others.2025. Tulu3: PushingFron- chotiwat, Adithya Venkatadri Hulagadri, Kok Wai
|               |          |                      | Teng, Yeo | Yeow Tong, | Bryan Siow, | Wei Yi Teo, |
| ------------- | -------- | -------------------- | --------- | ---------- | ----------- | ----------- |
| tiers in Open | Language | Model Post-Training. | In        |            |             |             |
TanChoonMeng,BrandonOng,and11others.2025.
SecondConferenceonLanguageModeling.
SEA-LION:SoutheastAsianLanguagesinOneNet-
HaonanLi,FajriKoto,MinghaoWu,AlhamFikriAji, work. InProceedingsofthe14thInternationalJoint
andTimothyBaldwin.2023. Bactrian-X:Multilin- Conference on Natural Language Processing and
gual replicable instruction-following models with the 4th Conference of the Asia-Pacific Chapter of
low-rankadaptation. Preprint,arXiv:2305.15011. theAssociationforComputationalLinguistics,pages
512–526,Mumbai,India.TheAsianFederationof
YuetaiLi,XiangYue,ZhangchenXu,FengqingJiang, NaturalLanguageProcessingandTheAssociation
LuyaoNiu,BillYuchenLin,BhaskarRamasubrama- forComputationalLinguistics.
| nian,andRadhaPoovendran.2025. |     | SmallModels |     |     |     |     |
| ----------------------------- | --- | ----------- | --- | --- | --- | --- |
StruggletoLearnfromStrongReasoners. InFind- NLLBTeam,MartaR.Costa-jussà,JamesCross,Onur
ingsoftheAssociationforComputationalLinguistics: Çelebi,MahaElbayad,KennethHeafield,KevinHef-
|     |     |     | fernan, Elahe | Kalbassi, | Janice Lam, | Daniel Licht, |
| --- | --- | --- | ------------- | --------- | ----------- | ------------- |
ACL2025,pages25366–25394,Vienna,Austria.As-
sociationforComputationalLinguistics. JeanMaillard,AnnaSun,SkylerWang,Guillaume
Wenzek,AlYoungblood,BapiAkula,LoicBarrault,
RyanMarten,TrungVu,CharlieCheng-JieJi,Kartik Gabriel Mejia Gonzalez, Prangthip Hansanti, and
Sharma,ShreyasPimpalgaonkar,AlexDimakis,and 20 others. 2022. No language left behind: Scal-
MaheswaranSathiamoorthy.2025. Curator: ATool inghuman-centeredmachinetranslation. Preprint,
| forSyntheticDataCreation. |     | https://github.com/ |     |     |     |     |
| ------------------------- | --- | ------------------- | --- | --- | --- | --- |
arXiv:2207.04672.
bespokelabsai/curator.
OLMoTeam,AllysonEttinger,AmandaBertsch,Bailey
Pedro Henrique Martins, João Alves, Patrick Fernan- Kuehl,DavidGraham,DavidHeineman,DirkGroen-
des, Nuno M. Guerreiro, Ricardo Rei, Amin Fara- eveld, Faeze Brahman, Finbarr Timbers, Hamish
jian,MateuszKlimaszewski,DuarteM.Alves,José Ivison, Jacob Morrison, Jake Poznanski, Kyle Lo,
11

LucaSoldaini,MattJordan,MayeeChen,Michael AllanRaventos,MansheejPaul,FengChen,andSurya
Noukhovitch,NathanLambert,PeteWalsh,and49 Ganguli. 2023. Pretraining task diversity and the
others.2025. OLMo3. Technicalreport,AllenInsti- emergenceofnon-Bayesianin-contextlearningfor
tuteforAI. TechnicalReport. regression. InThirty-seventhConferenceonNeural
InformationProcessingSystems.
OpenAI,AaronHurst,AdamLerer,AdamP.Goucher,
Adam Perelman, Aditya Ramesh, Aidan Clark, Alejandro R. Salamanca, Diana Abagyan, Daniel
AJ Ostrow, Akila Welihinda, Alan Hayes, Alec D’souza,AmmarKhairi,DavidMora,SaurabhDash,
Radford,AleksanderMa˛dry,AlexBaker-Whitcomb, ViraatAryabumi,SaraRajaee,MehrnazMofakhami,
Alex Beutel, Alex Borzunov, Alex Carney, Alex AnanyaSahu, ThomasEuyang, BrittawnyaPrince,
Chow, Alex Kirillov, Alex Nichol, and 400 oth- MadelineSmith,HangyuLin,AcyrLocatelli,Sara
ers. 2024. GPT-4o System Card. Preprint, Hooker,TomKocmi,AidanGomez,IvanZhang,and
arXiv:2410.21276. 7others.2026. TinyAya: BridgingScaleandMulti-
lingualDepth. Preprint,arXiv:2603.11510.
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,
CarrollWainwright,PamelaMishkin,ChongZhang, DylanSam,AyanChakrabarti,AfshinRostamizadeh,
SandhiniAgarwal,KatarinaSlama,AlexGray,John SrikumarRamalingam,GuiCitovsky,andSanjivKu-
Schulman,JacobHilton,FraserKelton,LukeMiller, mar. 2025. Analyzing Similarity Metrics for Data
Maddie Simens, Amanda Askell, Peter Welinder, SelectionforLanguageModelPretraining. InThe
Paul Christiano, Jan Leike, and Ryan Lowe. 2022. Thirty-ninthAnnualConferenceonNeuralInforma-
Traininglanguagemodelstofollowinstructionswith tionProcessingSystems.
humanfeedback. InAdvancesinNeuralInformation
ProcessingSystems. MuhammadAliShafique,KanwalMehreen,Muham-
madArham,MaazAmjad,SaburButt,andHamza
ParinthapatPengpun,CanUdomcharoenchaikit,Weer- Farooq. 2025. Alif: Advancing Urdu Large Lan-
ayut Buaphet, and Peerat Limkonchotiwat. 2024. guageModelsviaMultilingualSyntheticDataDis-
Seed-free synthetic data generation framework for tillation. In Proceedings of the 5th Workshop on
instruction-tuningLLMs: AcasestudyinThai. In MultilingualRepresentationLearning(MRL2025),
Proceedingsofthe62ndAnnualMeetingoftheAsso- pages271–284,Suzhuo,China.AssociationforCom-
ciationforComputationalLinguistics(Volume4:Stu- putationalLinguistics.
dentResearchWorkshop),pages445–464,Bangkok,
Thailand.AssociationforComputationalLinguistics. FredaShi,MiracSuzgun,MarkusFreitag,XuezhiWang,
SurajSrivats,SoroushVosoughi,HyungWonChung,
EstherPloeger,WesselPoelman,AndreasHolckHøeg- YiTay,SebastianRuder,DennyZhou,DipanjanDas,
Petersen,AndersSchlichtkrull,MiryamdeLhoneux, and Jason Wei. 2023. Language models are multi-
andJohannesBjerva.2026. Aprincipledframework lingualchain-of-thoughtreasoners. InTheEleventh
for evaluating on typologically diverse languages. International Conference on Learning Representa-
ComputationalLinguistics,pages1–33. tions.
JoséPombal,DongkeunYoon,PatrickFernandes,Ian ShivalikaSingh,AngelikaRomanou,ClémentineFour-
Wu,SeungoneKim,RicardoRei,GrahamNeubig, rier,DavidIfeoluwaAdelani,JianGangNgui,Daniel
andAndreMartins.2025. M-Prometheus: ASuite Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
ofOpenMultilingualLLMJudges. InSecondCon- sio, Wei Qi Leong, Yosephine Susanto, Raymond
ferenceonLanguageModeling. Ng, Shayne Longpre, Sebastian Ruder, Wei-Yin
Ko, Antoine Bosselut, Alice Oh, Andre Martins,
Libo Qin, Qiguang Chen, Yuhang Zhou, Zhi Chen, Leshem Choshen, Daphne Ippolito, and 4 others.
YinghuiLi,LiziLiao,MinLi,WanxiangChe,and 2025. GlobalMMLU:UnderstandingandAddress-
PhilipS.Yu.2025. Asurveyofmultilinguallarge ing Cultural and Linguistic Biases in Multilingual
languagemodels. Patterns,6(1):101118. Evaluation. InProceedingsofthe63rdAnnualMeet-
ingoftheAssociationforComputationalLinguistics
NeelPrabhanjanRachamalla,AravindKonakalla,Gau- (Volume1: LongPapers), pages18761–18799, Vi-
tamRajeev, AshishKulkarni, ChandraKhatri, and enna, Austria. Association for Computational Lin-
Shubham Agarwal. 2025. Pragyaan: Designing guistics.
and Curating High-Quality Cultural Post-Training
DatasetsforIndianLanguages. InProceedingsofthe Shivalika Singh, Freddie Vargus, Daniel D’souza,
5thWorkshoponMultilingualRepresentationLearn- Börje F. Karlsson, Abinaya Mahendiran, Wei-Yin
ing(MRL2025),pages285–321,Suzhuo,China.As- Ko,HerumbShandilya,JayPatel,DeividasMataci-
sociationforComputationalLinguistics. unas, Laura O’Mahony, Mike Zhang, Ramith Het-
tiarachchi,JosephWilson,MarinaMachado,Luisa
ColinRaffel,NoamShazeer,AdamRoberts,Katherine Moura,DominikKrzemin´ski,HakimehFadaei,Irem
Lee,SharanNarang,MichaelMatena,YanqiZhou, Ergun, Ifeoma Okoh, and 14 others. 2024. Aya
WeiLi,andPeterJ.Liu.2020. Exploringthelimits Dataset: An Open-Access Collection for Multilin-
oftransferlearningwithaunifiedtext-to-texttrans- gualInstructionTuning. InProceedingsofthe62nd
former. J.Mach.Learn.Res.,21(1). AnnualMeetingoftheAssociationforComputational
12

Linguistics(Volume1: LongPapers),pages11521– ShengyuZhang,LinfengDong,XiaoyaLi,SenZhang,
11567,Bangkok,Thailand.AssociationforCompu- XiaofeiSun,ShuheWang,JiweiLi,RunyiHu,Tian-
tationalLinguistics. weiZhang, FeiWu, andGuoyinWang.2025b. In-
structionTuningforLargeLanguageModels: ASur-
Bibek Upadhayay and Vahid Behzadan. 2024. TaCo: vey. Preprint,arXiv:2308.10792.
EnhancingCross-LingualTransferforLow-Resource
Languages in LLMs through Translation-Assisted WentingZhao,XiangRen,JackHessel,ClaireCardie,
Chain-of-Thought Processes. In 5th Workshop on Yejin Choi, and Yuntian Deng. 2024. WildChat:
practicalMLforlimited/lowresourcesettings. 1MChatGPTInteractionLogsintheWild. InThe
TwelfthInternationalConferenceonLearningRepre-
YizhongWang,YeganehKordi,SwaroopMishra,Alisa
sentations.
Liu,NoahA.Smith,DanielKhashabi,andHannaneh
Hajishirzi. 2023. Self-instruct: Aligning language AlanZhu,ParthAsawa,JaredQuincyDavis,Lingjiao
modelswithself-generatedinstructions. InProceed- Chen,BorisHanin,IonStoica,JosephE.Gonzalez,
ingsofthe61stAnnualMeetingoftheAssociationfor andMateiZaharia.2025. BARE:LeveragingBase
ComputationalLinguistics(Volume1: LongPapers), LanguageModelsforFew-ShotSyntheticDataGen-
pages13484–13508,Toronto,Canada.Association eration. Preprint,arXiv:2502.01697.
forComputationalLinguistics.
Zhilin Wang, Jiaqi Zeng, Olivier Delalleau, Daniel
Egert,EllieEvans,Hoo-ChangShin,FelipeSoares,
Yi Dong, and Oleksii Kuchaiev. 2025. Help-
Steer3: Human-AnnotatedFeedbackandEditData
toEmpowerInference-TimeScalinginOpen-Ended
General-DomainTasks. Preprint,arXiv:2503.04378.
Xiangpeng Wei, Haoran Wei, Huan Lin, Tianhao Li,
Pei Zhang, Xingzhang Ren, Mei Li, Yu Wan, Zhi-
wei Cao, Binbin Xie, Tianxiang Hu, Shangjie Li,
Binyuan Hui, Bowen Yu, Dayiheng Liu, Baosong
Yang, Fei Huang, and Jun Xie. 2023. PolyLM:
An Open Source Polyglot Large Language Model.
Preprint,arXiv:2307.06018.
Zhangchen Xu, Fengqing Jiang, Luyao Niu, Yun-
tian Deng, Radha Poovendran, Yejin Choi, and
Bill Yuchen Lin. 2025a. Magpie: Alignment data
synthesisfromscratchbypromptingalignedLLMs
withnothing. InTheThirteenthInternationalCon-
ferenceonLearningRepresentations.
ZhangchenXu,FengqingJiang,LuyaoNiu,BillYuchen
Lin,andRadhaPoovendran.2025b. Strongermod-
elsarenotalwaysstrongerteachersforinstruction
tuning. InProceedingsofthe2025Conferenceofthe
NationsoftheAmericasChapteroftheAssociation
for Computational Linguistics: Human Language
Technologies(Volume1: LongPapers),pages4392–
4405, Albuquerque, New Mexico. Association for
ComputationalLinguistics.
AnYang,AnfengLi,BaosongYang,BeichenZhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025. Qwen3 Technical Report. Preprint,
arXiv:2505.09388.
Hengyuan Zhang, Shiping Yang, Xiao Liang, Chen-
ming Shang, Yuxuan Jiang, Chaofan Tao, Jing
Xiong, Hayden Kwok-Hay So, Ruobing Xie, An-
gel X. Chang, and Ngai Wong. 2025a. Find Your
Optimal Teacher: Personalized Data Synthesis via
Router-GuidedMulti-TeacherDistillation. Preprint,
arXiv:2510.10925.
13

Appendix
| A MultilingualSyntheticDataGeneration  |            |     | 16  |
| -------------------------------------- | ---------- | --- | --- |
| B SeedDatasetStatistics                |            |     | 16  |
| C The POLYGLOT                         | Collection |     | 16  |
| D TeacherModelandTargetLanguageDetails |            |     | 16  |
| E ExperimentalDetails                  |            |     | 16  |
E.1 SupervisedFinetuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
E.2 ModelEvaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
| F FullResultsforIntr.               | andExtr. Metrics |     | 16  |
| ----------------------------------- | ---------------- | --- | --- |
| G AdditionalExperimentsandAblations |                  |     | 17  |
G.1 EffectofDataScaleonStudentModelPerformance . . . . . . . . . . . . . . . . . . . . 17
G.2 GeneralizationAcrossModelSize . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
G.3 EffectofTranslationMethod(PromptinganLMvs. TranslationModel) . . . . . . . . . 18
G.4 WeighingofIntrinsicandExtrinsicMetricsin PG-SCORE . . . . . . . . . . . . . . . . 19
G.5 Effectoflanguageresourcelevelson PG-SCORE . . . . . . . . . . . . . . . . . . . . . 21
| H DisclosureontheUseofLLMs         |     |                    | 21  |
| ---------------------------------- | --- | ------------------ | --- |
| I MultilingualSyntheticDataRecipe: |     | CaseStudyonTagalog | 21  |
I.1 Setup: RecipeDesignandEvaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
I.2 Results: LeaderboardScoresandAblations . . . . . . . . . . . . . . . . . . . . . . . . 23
I.3 Analysis: AblationExperiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
| J InferenceDetails |     |     | 25  |
| ------------------ | --- | --- | --- |
14

| Dataset | Language(s) |     |     |     | GenerationMethod/Description |     |     |     |
| ------- | ----------- | --- | --- | --- | ---------------------------- | --- | --- | --- |
Bactrian-X(Lietal.,2023) 52languages-Arabic,Indonesian,Chi- Translate-usedGoogleTranslateAPI
|     | nese,Malaysian,Tamil,Tagalog,etc. |     |     |     | to translate |     | English instructions | from |
| --- | --------------------------------- | --- | --- | --- | ------------ | --- | -------------------- | ---- |
Alpaca(52K)andDolly(15K).
MultiAlpaca(Weietal.,2023) 18languages-English,Chinese,Rus- Generate,Translate-usedamultilin-
|     | sian,Spanish,German,French,etc. |     |     |     | gual | self-instruct | (Wang | et al., 2023) |
| --- | ------------------------------- | --- | --- | --- | ---- | ------------- | ----- | ------------- |
methodfromEnglishprompt-response
pairstoperformtranslation.
xP3-MT(Muennighoffetal.,2023) 46languages-Arabic,English,Span- Translate, Respond - used Google
|     | ish,Hindi,Chinese,Indonesian,etc. |     |     |     | Translate       |          | API to translate | English      |
| --- | --------------------------------- | --- | --- | --- | --------------- | -------- | ---------------- | ------------ |
|     |                                   |     |     |     | prompt-response |          | pairs            | from differ- |
|     |                                   |     |     |     | ent             | sources, | in addition      | to creating  |
template-basedpromptswhereanLM
respondstoit.
Cendol(Cahyawijayaetal.,2024) 18Indonesianlanguages-Sundanese, Translate, Respond - curated various
|     | Javanese,           | Acehnese, | Banjarese, | Bugi- | prompts                             | from | past Indonesian | NLP |
| --- | ------------------- | --------- | ---------- | ----- | ----------------------------------- | ---- | --------------- | --- |
|     | nese,Gorontalo,etc. |           |            |       | tasks,includingtranslationsofDolly. |      |                 |     |
SeedFreeThai(Pengpunetal.,2024) Thai Generate-generatedsyntheticinstruc-
tiondatawithoutseedexamplesbyus-
|     |     |     |     |     | ingWikipediacontexts. |     |     | Identifiesflu- |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | -------------- |
ency,diversity,andculturalcontextas
keyproperties.
AyaDatasetandCollection(Singhetal., 114languages-Arabic,French,Hindi, Translate,Respond-involvesacollec-
2024) Indonesian,Japanese,Spanish,Swahili, tionoftranslatedpromptsfromEnglish,
|     | Turkish,Yoruba,Filipino,etc. |     |     |     | andtemplatedprompts.Asizeablepor- |        |            |                  |
| --- | ---------------------------- | --- | --- | --- | --------------------------------- | ------ | ---------- | ---------------- |
|     |                              |     |     |     | tion                              | of the | collection | includes native- |
speakerannotations.
sPhinX(Ahujaetal.,2025) 51languages-Afrikaan,Arabic,Ben- Translate-selectivelytranslatesessen-
|     | gali, Bulgarian,    |     | Burmese, | Chinese, | tialportionsofmultilingualinputsinor- |     |     |     |
| --- | ------------------- | --- | -------- | -------- | ------------------------------------- | --- | --- | --- |
|     | Croatian,Czech,etc. |     |          |          | dertosemanticallypreservemeaning.     |     |     |     |
EuroBlocks(Martinsetal.,2025,2024) 31languages-English,Chinese,Span- Generate,Translate-promptedLlama
|     | ish, Italian,             | French, | German, | Por- | 3 or                             | an earlier | EuroLLM | checkpoint |
| --- | ------------------------- | ------- | ------- | ---- | -------------------------------- | ---------- | ------- | ---------- |
|     | tuguese,Dutch,Polish,etc. |         |         |      | withadocument,targetlanguage,and |            |         |            |
category,thenaskingittogeneratean
|     |     |     |     |     | instruction. |     | Alsoinvolvedtranslating |     |
| --- | --- | --- | --- | --- | ------------ | --- | ----------------------- | --- |
prompt-responsepairs.
SEA-LIONDataset(Ngetal.,2025) 11 languages - English, Chinese, In- Generate,Translate-forthemajority
|     | donesian, | Vietnamese, | Malay,           | Thai, | ofthedatasets,sampleswerefirstgener- |     |     |     |
| --- | --------- | ----------- | ---------------- | ----- | ------------------------------------ | --- | --- | --- |
|     | Burmese,  | Lao,        | Filipino, Khmer, | and   | atedintoEnglishusingQwen32B,and      |     |     |     |
|     | Tamil     |             |                  |       | thentranslatedintothetargetlanguage  |     |     |     |
usingGemma227B.
Urdu-InstructDataset(Shafiqueetal., Urdu Generate-usesamodifiedSelf-Instruct
| 2025) |     |     |     |     | from | a pool | of culturally | relevant |
| ----- | --- | --- | --- | --- | ---- | ------ | ------------- | -------- |
prompts.
Pragyaan(Rachamallaetal.,2025) 10 Indian languages - Gujarati, Kan- Generate,Translate-performtransla-
|     | nada, Marathi, |         | Bengali, Odia, | Tamil, | tionusinganLMforasubsetofdata.     |     |     |     |
| --- | -------------- | ------- | -------------- | ------ | ---------------------------------- | --- | --- | --- |
|     | Malayalam,     | Telugu, | Punjabi,       | Hindi, | UsedSelf-Instructfromapoolofnative |     |     |     |
|     | andSanskrit    |         |                |        | promptsforanothersubsetofdata.     |     |     |     |
Table5: ShortsurveyofrelatedworkonsyntheticdatagenerationformultilingualLMs. Foreachwork,we
provideabriefdescriptionoftheirdatagenerationmethod. Wefindthatmostmethodsfallintooneofthethree
categoriesdescribedin§2.2,i.e.,Generate,Translate,orRespond,whichwetestedinourexperiments.
15

A MultilingualSyntheticData
theUnslothframework(Hanetal.,2023)usinga
Generation
|     |     |     |     | clusterofGraceHopperGH200Superchips. |     |     | Full |
| --- | --- | --- | --- | ------------------------------------ | --- | --- | ---- |
finetuning(7B)takesaround1.5hours(wallclock)
WepresentanoverviewofpriorworksinTable5
for2epochsand2nodes.
thatusedsyntheticdatatotrainmultilingualLMs.
Ingeneral,wefindthatmostdatagenerationmeth-
|     |     |     |     | Hyperparameter | Value | Hyperparameter | Value |
| --- | --- | --- | --- | -------------- | ----- | -------------- | ----- |
odsfallintooneofthethreecategoriesdescribedin
|     |     |     |     | Learningrate | 5e-5 | Batchsize | 32  |
| --- | --- | --- | --- | ------------ | ---- | --------- | --- |
§2.2,i.e.,Generate,Translate,orRespond,which
|                           |     |                   |     | Epochs        | 2      | Grad.Acum.Steps | 4     |
| ------------------------- | --- | ----------------- | --- | ------------- | ------ | --------------- | ----- |
| wetestedinourexperiments. |     | Oursurveysuggests |     |               |        |                 |       |
|                           |     |                   |     | Maxseq.length | 16,384 | Weightdecay     | 0.001 |
thatourchoiceofdatagenerationmethodsare Optimizer AdamW Scheduler Linear
groundedinpriorworkandcoversthemajority
Table9: Hyperparametersforfinetuninga7Bstudent
ofapproachesusedinsyntheticdatageneration.
modelfromOLMo37B.
B SeedDatasetStatistics
E.2 ModelEvaluation
Table6showsthestatisticsoftheseeddatasetused
WeusedtheLightevalframework(v0.13.1dev0,
forsyntheticdatageneration.
|     |     |     |     | Habibetal.,2023)forevaluation. |     | Table10summa- |     |
| --- | --- | --- | --- | ------------------------------ | --- | ------------- | --- |
C The POLYGLOT Collection rizes the benchmarks used for evaluating student
models. WedecidedtouseGlobal-MMLULitein-
Inordertofacilitatefutureresearchonmultilingual
steadofGlobal-MMLUbecauetheformercontains
syntheticdatageneration,weintroducethePOLY-
actualnativespeakerannotationsthatlocalizedthe
GLOTcollection,acollectionofsyntheticdatasets
benchmarkintodifferentculturalcontexts.
andstudentmodelsgeneratedbythebestteacher
| modelacrossalltargetlanguages. |     | ThePOLYGLOT |     |           |             |        |         |
| ------------------------------ | --- | ----------- | --- | --------- | ----------- | ------ | ------- |
|                                |     |             |     | Benchmark | Formulation | Metric | N-shots |
collectionincludes:
|     |     |     |     | Global-MMLULite | MCF | Accuracy | 0   |
| --- | --- | --- | --- | --------------- | --- | -------- | --- |
• POLYGLOT-INSTRUCTIONS-SYNTH: Synthetic M-RewardBench MCF WeightedAcc. 0
|     |     |     |     | M-GSM | Generative | Exact-Match | 5   |
| --- | --- | --- | --- | ----- | ---------- | ----------- | --- |
datasetsforeachtargetlanguagegeneratedby
eachteachermodelusingallthreedatagenera-
Table10:Evaluationsettingsforeachbenchmark(MCF:
tionmethods(§2.2).
Multiple-ChoiceFormulation).
• POLYGLOT-GEMMA-SFT:Asetof8Bstudent
modelsfinetunedoneachsyntheticdatasetfrom
ForGlobal-MMLULiteandM-RewardBench,
theOLMo37BbasemodelusingtheGemma
|     |     |     |     | we use | the Multiple-Choice | Formulation | (MCF) |
| --- | --- | --- | --- | ------ | ------------------- | ----------- | ----- |
327B(highest-scoringmodel)teacher.
|                      |     |          |            | withcharacternormalization. |     | Inaddition,wealso |     |
| -------------------- | --- | -------- | ---------- | --------------------------- | --- | ----------------- | --- |
| Wepubliclyreleasethe |     | POLYGLOT | Collection |                             |     |                   |     |
followthecorpus-levelmetricinM-RewardBench
inHuggingFace.3
whichusesaweightedaccuracyforeachdatasub-
|     |     |     |     | setandcategory(Gurejaetal.,2025). |     | ForM-GSM, |     |
| --- | --- | --- | --- | --------------------------------- | --- | --------- | --- |
D TeacherModelandTargetLanguage
weshow5few-shotexamplesfromthetrainingset
Details
inorderforthemodeltoproperlygeneratethean-
Inthissection,weprovideadditionaldetailsabout swer. Werunallevaluationexperimentsforthree
the teacher models and target languages used in trials with different random seeds and report the
ourexperiments. Table7summarizesthekeychar- averageandstandarddeviation.
| acteristics | of each teacher | model. | On the other |     |     |     |     |
| ----------- | --------------- | ------ | ------------ | --- | --- | --- | --- |
hand,Table8providesinformationaboutthetarget F FullResultsforIntr. andExtr. Metrics
languages,includinglanguagefamily,numberof
Table11showsallthedataqualitymetricsforeach
speakers,andresourceavailability.
|     |     |     |     | teachermodelacrossalllanguages. |     | Table12shows |     |
| --- | --- | --- | --- | ------------------------------- | --- | ------------ | --- |
E ExperimentalDetails thefullresultsofstudentmodelsfinetunedonsyn-
|                          |     |     |     | thetic datasets           | generated | by each teacher | model |
| ------------------------ | --- | --- | --- | ------------------------- | --------- | --------------- | ----- |
| E.1 SupervisedFinetuning |     |     |     | acrossalltargetlanguages. |           |                 |       |
Table9summarizesthehyperparametersusedfor
|                          |     |                    |     | Percentage | Increase Tables |            |       |
| ------------------------ | --- | ------------------ | --- | ---------- | --------------- | ---------- | ----- |
|                          |     |                    |     |            |                 | We provide | addi- |
| finetuningstudentmodels. |     | Wetrainmodelsusing |     |            |                 |            |       |
tionaltablesfromthemainexperimentsin§3and
3 :ljvmiranda921/polyglot-teachers §4. Table 14 shows the percentage increase in
16

Language
Source English(en)Arabic(ar)Czech(cs)German(de)Spanish(es)Indonesian(id)Japanese(ja)
| AyaDataset         |     | -      | -     | 5,000 |     | 241    | 3,854  |     | 2,786 | 6,259 |
| ------------------ | --- | ------ | ----- | ----- | --- | ------ | ------ | --- | ----- | ----- |
| Tülu3SFT           |     | 10,000 | -     |       | -   | -      |        | -   | -     | -     |
| WildChat4.8M       |     | 10,000 | 4,660 | 1,266 |     | 5,908  | 5,900  |     | 7,983 | 602   |
| CIDAR              |     | -      | 6,000 |       | -   | -      |        | -   | -     | -     |
| Cendolv2           |     | -      | -     |       | -   | -      |        | -   | 3,000 | -     |
| OpenAssistant2     |     | -      | 23    |       | 4   | 2,328  | 8,785  |     | 3     | 306   |
| EuroBlocksSFT      |     | -      | -     | 3,813 |     | 12,551 | 15,641 |     | -     | 2,893 |
| GSM8k(train)       |     | 7,473  | -     |       | -   | -      |        | -   | -     | -     |
| Helpsteer3(chosen) |     | -      | -     |       | -   | 462    |        | 778 | 156   | 534   |
| MagpieProFiltered  |     | 10,000 | -     |       | -   | -      |        | -   | -     | -     |
Totalperlanguage
|     |     | 30,743 | 10,683 | 10,083 |     | 21,490 | 34,958 |     | 13,928 | 10,594 |
| --- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ | ------ |
Table6: Seeddatasetstatistics. Inordertobootstrapoursyntheticdatagenerationmethods,weuseaseeddataset
composedofvariousmultilingualinstruction-followingdatasets. WeincludeEnglishsamplesinordertosimulate
datagenerationpipelineswhereEnglishistranslatedintoatargetlanguage. Wecollectatotalof132,929seed
examplesacross7languages(includingEnglish).
|     | ModelName                    |     |     |     | Provider | Size(B) |     | #Langs | License     |     |
| --- | ---------------------------- | --- | --- | --- | -------- | ------- | --- | ------ | ----------- | --- |
|     | GPT-4omini(OpenAIetal.,2024) |     |     |     | OpenAI   | –       |     | 50+    | Proprietary |     |
Llama3.170BInstruct(Grattafiorietal.,2024) Meta 70 8 Llama3.1
|     | Llama3.18BInstruct(Grattafiorietal.,2024) |     |     |     | Meta   | 8   |     | 8    | Llama3.1     |     |
| --- | ----------------------------------------- | --- | --- | --- | ------ | --- | --- | ---- | ------------ | --- |
|     | CommandA(CohereTeametal.,2025)            |     |     |     | Cohere | 104 |     | 23   | CC-BY-NC-4.0 |     |
|     | AyaExpanse32B(Dangetal.,2024)             |     |     |     | Cohere | 32  |     | 23   | CC-BY-NC-4.0 |     |
|     | Gemma327BInstruct(GemmaTeametal.,2025)    |     |     |     | Google | 27  |     | 100+ | Gemma        |     |
|     | Gemma312BInstruct(GemmaTeametal.,2025)    |     |     |     | Google | 12  |     | 100+ | Gemma        |     |
|     | Gemma34BInstruct(GemmaTeametal.,2025)     |     |     |     | Google | 4   |     | 100+ | Gemma        |     |
|     | IBMGranite4.0(GraniteTeam,IBM,2025)       |     |     |     | IBM    | 3   |     | 116  | Apache2.0    |     |
|     | IBMGraniteMicro(GraniteTeam,IBM,2025)     |     |     |     | IBM    | 0.4 |     | 116  | Apache2.0    |     |
Table7: Teachermodeldetails. Weevaluate10teachermodelsacrossdifferentproviders, sizes,multilingual
capabilities,andlicensingterms. Sizeisreportedinbillionsofparameters(B)whereavailable. #Langsindicates
thenumberoflanguagesthemodelwastrainedonorevaluatedfor.
PG-SCORE when using family-matched teacher- minehowmuchsyntheticdataisneededtoreliably
| studentpairscomparedtotheOLMo37Bbaseline |                                   |     |     |     | compute | PG-SCORE. |     |     |     |     |
| ---------------------------------------- | --------------------------------- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- |
| (see§3.2).                               | Table15showsthepercentageincrease |     |     |     |         |           |     |     |     |     |
in PG-SCOREwhenusingthebestdatageneration Setup We finetune an OLMo 3 7B base
methodforeachteacher-languagepaircompared model on n SFT instances where n
∈
toanequalmixbaseline(see§3.3). 1k,5k,10k,25k,50k . Toreducecomputational
|     |     |     |     |     | {   |     |     | }   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
costs,weperformthisexperimentonlyonasingle
G AdditionalExperimentsandAblations teacher model (Gemma 3 27B Instruct) on three
targetlanguagesthatrepresentdiversescriptsand
Inthissection,weablateseveralaspectsofoureval-
|     |     |     |     |     | resourceavailability: |     |     | Arabic,German,andIndone- |     |     |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | ------------------------ | --- | --- |
uationprotocolthatmayaffectateachermodel’s
|     |     |     |     |     | sian. | Similartothemainexperiments,werepresent |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --------------------------------------- | --- | --- | --- | --- |
PG-SCORE.
eachdatagenerationmethodequallywhencreating
|     |     |     |     |     | theSFTdatasets. |     |     | Then,werecomputetheintrinsic |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | ---------------------------- | --- | --- |
G.1 EffectofDataScaleonStudentModel
metricsandfinetunestudentmodelsandmeasure
Performance
theirperformanceacrossthreebenchmarks(§2.3).
OnecomponentofPG-SCOREistheextrinsicstu-
dent performance metric (§2.3) as measured by Results Figure 5 shows the average student
PGR.Scalinglawssuggestthatthisperformance model performance as a function of the number
improves with more data (Kaplan et al., 2020). of SFT instances. We observe that student per-
Then,itispossibletoinflatePG-SCOREbysimply formanceimproveswithmoresyntheticdata,but
usingmoresyntheticdata. Inordertocontrolfor gainsdiminishbeyond10kexamples. Thisfinding
this variable, we conduct an experiment to deter- suggests that using 10k synthetic examples per
17

Language Family Script ResourceAvailability %inCC
Arabic Afro-Asiatic Arabic 5(High) 0.65%
Czech Indo-European Latin 4(Medium-High) 0.99%
German Indo-European Latin 5(High) 6.01%
Spanish Indo-European Latin 5(High) 4.37%
Indonesian Austronesian Latin 3(Medium) 0.95%
Japanese Japonic Japanese 5(High) 5.20%
Table8: Targetlanguagedetails. Weevaluateteachermodelsacrosssixtypologicallydiverselanguagesspanning
differentlanguagefamiliesandscripts. ResourceavailabilityisbasedontheclassificationfromJoshietal.(2020),
rangingfrom0(lowest)to5(highest). CommonCrawlpercentages(Raffeletal.,2020)indicatetheproportionof
webtextavailableforeachlanguage.
0.65
0.60
0.55
0.50
0.45
103 104
Num. samples,log
ecnamrofrePlaugnilitluM
.gvA
Instruct, Aya Expanse 32B, Llama 30B Instruct)
andall6targetlanguages.
Results Table 16 shows the PG-SCORE scores
forthreeteachermodelswhenusingOLMo332B
asthestudentmodel. WefindthatGemma327B
Instructremainsthehighest-scoringteacherin
this comparison, achieving the highest average
PG-SCORE of 0.805 across all languages. This
resultisconsistentwithourfindingsusingthe8B
student model (§3), demonstrating that the supe-
riordataqualitygeneratedbyGemma327Bgen-
eralizes across model scales. Aya Expanse 32B
achieves a positive average PG-SCORE of 0.227,
while Llama 3.1 70B Instruct shows a negative
Arabic German Indonesian averageof 0.267.
−
Furthermore, the language-dependent effects
Figure 5: Effect of synthetic data scale on student observedinthe8Bexperimentsremainconsis-
model performance. Student performance improves tentat32Bscale. Germancontinuestoshowthe
withmoresyntheticdata,butgainsdiminishbeyond10k
highest PG-SCORE values across all three teach-
examples.
ers (2.389 for Gemma, 1.979 for Aya, 0.838 for
Llama), suggesting that certain languages bene-
language is sufficient to reliably compute PG- fitmorefromsyntheticdataregardlessofstudent
SCORE withoutinflatingthemetricbyincreas- modelsize. Similarly,Spanishexhibitsstrongper-
ing the number of samples. In our experiments, formanceacrossallteachers,with PG-SCOREval-
weuse10ksyntheticexamplesperlanguagewhen uesrangingfrom1.353to1.855. Incontrast,Ara-
computing PG-SCORE. Specifically,weshowthat bicshowsthemostvariableresults,withGemma
10ksyntheticexamplesfromastrongteacherare achievingslightlynegativescores( 0.239)while
−
sufficienttofinetuneastudentmodeltoachieverea- Aya and Llama show substantially lower perfor-
sonableperformanceacrossmultiplebenchmarks. mance( 0.872and 1.688,respectively). Overall,
− −
these findings demonstrate that PG-SCORE and
G.2 GeneralizationAcrossModelSize teacher model rankings generalize to the 32B pa-
rameterrange.
Setup Inordertotestwhether PG-SCORE gen-
eralizesbeyond8Bparametersizemodels,weuse
G.3 EffectofTranslationMethod(Prompting
anOLMo32Bbasemodel(S )andrecomputethe
ϕ
anLMvs. TranslationModel)
intrinsic and extrinsic metrics to obtain the PG-
SCORE. Tosavecomputationalcosts,wetrainstu- AnalternativetousinganLMfortranslatingtexts
dentmodelsacrossthreeteachers(Gemma327B fromEnglishtoatargetlanguageisviaatranslation
18

|       |     |     |     | Arabic(ar) |     |     | Czech(cs) |     |     | German(de) |       |
| ----- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- | ---------- | ----- |
| Model |     |     | d   | d          | PPL | R   | d d       | PPL | R d | d          | PPL R |
|       |     |     | x   | y          |     |     | x y       |     | x   |            | y     |
GPT4omini 0.704 0.869 8.40 3.516 0.643 0.862 3.18 3.716 0.732 0.889 3.65 3.810
Llama3.170BInst. 0.701 0.875 7.00 2.719 0.654 0.889 3.18 3.327 0.707 0.892 3.22 3.396
Llama3.18BInst. 0.708 0.779 6.2e4 1.731 0.673 0.799 2.7e4 1.908 0.738 0.873 3.6e3 2.513
CommandA 0.690 0.846 5.41 3.996 0.647 0.865 3.24 4.184 0.730 0.889 3.59 4.235
AyaExpanse32B 0.693 0.888 4.34 3.964 0.650 0.884 3.15 4.133 0.700 0.902 3.44 4.140
Gemma327BInst. 0.717 0.890 4.40 3.932 0.675 0.885 3.77 4.342 0.731 0.898 3.96 4.260
Gemma312BInst. 0.721 0.864 4.43 3.774 0.676 0.882 3.88 4.266 0.751 0.899 4.06 4.203
Gemma34BInst. 0.728 0.869 5.52 3.470 0.682 0.883 3.87 4.127 0.744 0.898 3.96 4.103
IBMGranite4.0 0.704 0.829 1.9e4 2.463 0.665 0.862 5.29 3.158 0.717 0.885 24.61 3.365
IBMGraniteMicro 0.741 0.863 12.45 3.033 0.713 0.874 4.61 3.568 0.726 0.892 4.59 3.704
|       |     |     |     | Spanish(es) |     |     | Indonesian(id) |     |     | Japanese(ja) |           |
| ----- | --- | --- | --- | ----------- | --- | --- | -------------- | --- | --- | ------------ | --------- |
| Model |     |     | d x | d y         | PPL | R   | d x d y        | PPL | R d | x            | d y PPL R |
GPT4omini 0.729 0.887 3.78 3.883 0.728 0.854 5.50 3.656 0.736 0.880 5.81 3.639
Llama3.170BInst. 0.728 0.892 3.15 3.434 0.727 0.874 4.85 3.293 0.756 0.799 4.52 2.459
Llama3.18BInst. 0.744 0.898 503.0 2.860 0.738 0.863 1.1e3 2.599 0.759 0.796 5.4e4 1.806
CommandA 0.733 0.884 3.77 4.336 0.747 0.857 4.94 3.899 0.739 0.881 4.92 4.174
AyaExpanse32B 0.724 0.893 3.67 4.181 0.726 0.879 4.43 4.017 0.743 0.883 5.96 3.821
Gemma327BInst. 0.768 0.903 4.30 4.266 0.740 0.854 5.49 4.057 0.765 0.875 5.90 3.956
Gemma312BInst. 0.763 0.895 4.14 4.193 0.762 0.851 5.84 3.958 0.756 0.885 5.78 4.017
Gemma34BInst. 0.754 0.887 4.52 4.021 0.760 0.851 6.46 3.657 0.794 0.875 6.45 3.656
IBMGranite4.0 0.743 0.882 5.22 3.309 0.729 0.833 16.80 2.437 0.761 0.849 9.79 2.889
IBMGraniteMicro 0.729 0.887 4.58 3.779 0.760 0.860 11.92 3.113 0.764 0.877 7.22 3.295
Table11: Fullintrinsicevaluationresultsacrossalllanguages. Dataqualitymetricsincludethediversityof
promptsandresponses(d P andd R ),averageperplexityofthestudentmodelontheresponse(PPL),andaverage
rewardscorebasedonamultilingualLLMjudge(R).
modelsuchasNLLB(NLLBTeametal.,2022). In syntheticdatasettocompute PG-SCORE.
thissection,weexaminetheeffectofthetranslation
methodonthe PG-SCOREofteachermodels. Results Figure6showsthePG-SCOREandaver-
agebenchmarkperformanceofthestudentmodel
| Setup |        |     |        |     |            |     | for each | translation | method | across | Arabic, Ger- |
| ----- | ------ | --- | ------ | --- | ---------- | --- | -------- | ----------- | ------ | ------ | ------------ |
|       | First, | we  | filter | and | sample 10k | En- |          |             |        |        |              |
glish prompt-response pairs from the Tülu 3 man, andIndonesian. WefindthatLM-Translate
SFT dataset.4 Then, using the NLLB model outperformsbothNLLB-basedapproaches,achiev-
(nllb-200-distilled-600M), ing an average PG-SCORE of 1.36 compared to
|     |     |     |     |     | we perform | two |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
translation methods: (1) NLLB-Translate-then- 0.85forNLLB-Translate-Bothand0.80forNLLB-
Respond: translatethepromptstoeachtargetlan- Translate-then-Respond. Thispatternholdsacross
allthreelanguages,withthelargestgapobserved
guageandpromptGemma327BInstructtogener-
atearesponse,and(2)NLLB-Translate-Both: trans- forGerman(2.09vs1.26/1.68).
lateboththepromptsandresponsesfromEnglishto Ourfindingssuggestthatpromptnaturalness,
thetargetlanguage. Wechoosethe600Mversion ratherthanresponsequality,isabottleneckin
|     |     |     |     |     |     |     | translation-basedpipelines: |     |     | havinganLMgen- |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | -------------- | --- |
duetoitscomputationalefficiencyandpopularity
amongpractitioners,asmeasuredbyHuggingFace erate responses to NLLB-translated prompts pro-
downloadsandcommunitylikes. videsnoimprovementoverpureNLLBtranslation
Wecomparethesemethodsagainstouroriginal (0.80 vs 0.85), indicating that translated prompts
failtoelicitthesamequalityofresponsesasLM-
Translatemethod,i.e.,promptingGemma327BIn-
| structtodirectlytranslatethepromptandgenerate |     |     |     |     |     |     | translatedprompts. |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
theresponseinthetargetlanguage(LM-Translate).
|     |     |     |     |     |     |     | G.4 | WeighingofIntrinsicandExtrinsic |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- |
Then,wecomputetheintrinsicdataqualitymetrics
|     |     |     |     |     |     |     |     | Metricsin | PG-SCORE |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --- |
andfinetuneOLMo37Bstudentmodelsoneach
|       |     |               |     |             |          |         | Our PG-SCORE |     | formulationusesanassumption- |     |     |
| ----- | --- | ------------- | --- | ----------- | -------- | ------- | ------------ | --- | ---------------------------- | --- | --- |
| 4Tülu | 3   | also contains |     | non-English | data. We | perform |              |     |                              |     |     |
freeandequalweighingschemebetweentheintrin-
English-languagefilteringusingfastText(Joulinetal.,2016,
2017)andthestaticvectorslibrary. sic ( ) and extrinsic ( ) metrics. In this section,
|     |     |     |     |     |     |     | I   |     | E   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
19

Model Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
GPT4omini -2.086 0.538 3.098 1.395 2.025 0.099
Llama3.170BInst. -1.528 0.538 2.265 1.075 0.329 0.013
Llama3.18BInst. -0.841 0.525 2.623 0.595 1.425 0.236
CommandA -2.476 0.505 2.759 1.613 1.863 0.841
AyaExpanse32B -0.293 0.538 2.491 1.701 1.943 0.221
Gemma327BInst. -0.074 0.552 2.635 1.724 0.198 0.677
Gemma312BInst. -1.015 0.538 2.700 1.592 -0.017 0.524
Gemma34BInst. -1.033 0.538 2.568 1.209 -0.388 0.349
IBMGranite4.0 1.565 0.538 2.061 1.235 0.614 0.802
IBMGraniteMicro -0.421 0.538 1.842 1.203 -0.659 0.210
Table12: Averageperformancegainrecovered(PGR)ofastudentmodelacrossvariousmultilingualbench-
marks. Our multilingual evaluation suite includes Global-MMLU Lite (Singh et al., 2025), M-RewardBench
(Gurejaetal.,2025), andM-GSM(Shietal.,2023). ThePGRcomputationisbasedonKimetal.(2025)and
detailedin§2.3(Equation2)whereS =OLMo37BInstructSFTandS =OLMo310257B.
REF ϕ
Model Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
Gemma327BInst. 0.145(0.0121) 0.360(0.0004) 1.655(0.0141) 1.358(0.0141) 0.214(0.0167) 0.626(0.0124)
AyaExpanse32B -0.058(0.0116) 0.222(0.0004) 1.468(0.0134) 1.129(0.0123) 1.153(0.0124) 0.320(0.0111)
Gemma312BInst. -0.464(0.0119) 0.327(0.0004) 1.756(0.0137) 1.228(0.0140) 0.151(0.0126) 0.573(0.0142)
CommandA -1.360(0.0112) 0.114(0.0004) 1.673(0.0139) 1.102(0.0145) 1.063(0.0125) 0.683(0.0122)
Gemma34BInst. -0.488(0.0119) 0.330(0.0004) 1.644(0.0137) 0.929(0.0140) -0.105(0.0126) 0.504(0.0113)
GPT4omini -1.117(0.0117) 0.015(0.0004) 1.766(0.0136) 0.908(0.0149) 1.003(0.0125) 0.189(0.0117)
IBMGranite4.0 -0.072(0.0123) -0.031(0.0004) 1.000(0.0135) 0.734(0.0151) -0.079(0.0125) 0.321(0.0108)
IBMGraniteMicro -0.282(0.0121) 0.290(0.0004) 1.102(0.0139) 0.783(0.0133) -0.329(0.0126) 0.264(0.0121)
Llama3.170BInst. -0.964(0.0117) 0.109(0.0004) 1.195(0.0146) 0.688(0.0146) 0.182(0.0126) -0.373(0.0116)
Llama3.18BInst. -1.693(0.0120) -0.974(0.0004) 0.891(0.0148) 0.182(0.0164) 0.322(0.0124) -0.863(0.0129)
Table13: DetailedresultsfromTable1withstandarderrors. Wecompute PG-SCORE thricewithdifferent
synthetically-generateddata(eachtrialusesadifferentdatamixbasedonarandomseed). Wereportthemeanand
standarderrorforeachteachermodelacrossalltargetlanguages. Foreachlanguage,wehighlightthebestmodelin
boldandthesecond-bestmodelwithanunderline.
BaseModel(S ) betweentheintrinsicandextrinsicmetricsacross
ϕ
allteacher-languagepairs(N=60,10models 6
TeacherModel Gemma34BLlama3.18B ×
languages). Inaddition,inordertotesttheeffect
Llama3.170BInst. +362.3% +260.1% of weighing one metric against the other, we for-
Llama3.18BInst. +183.1% +130.0% mulateageneralizedversionof PG-SCORE:
Gemma327BInst. +20.5% +26.5%
Gemma312BInst. +38.5% +67.2% PG-SCORET,ℓ = α +(1 α)
I − E (4)
Gemma34BInst. +103.4% +203.4% where0 α 1
≤ ≤
Table 14: Percentage increase in PG-SCORE for Notethattheexperimentsin§3and§4assume
family-matched teacher-student pairs. Percentage α = 0.5. We compute the PG-SCORE across
increasewhenusingfamily-matchedteacherscompared α = 0.00,0.25,0.50,0.75,1.00 and then test
toOLMo37Bbaseline(averageacrossArabic,German, { }
theresultingmodelranks’ρacrossallpairsofα.
andIndonesian).
Weperformthisexperimentonallteacher-language
pairswherestudentsarefinetunedfromtheOLMo
wetestwhetherthesetwometricscapture(1)com- 37Bbasemodel(N=30,10models 6languages).
×
plementaryaspectsofteachereffectivenessand(2)
Results Intrinsic and extrinsic metrics show a
howmodelrankingsdifferifonemetricisweighted
moderatepositivecorrelation(Spearmanρ=0.41,
morethantheother.
p < 0.01), suggesting that data quality metrics
Setup In order to test whether each metric cap- arepredictiveofstudentperformancewhilecap-
turescomplementaryaspectsofteachereffective- turingcomplementaryinformation. Thisfinding
ness,wecomputetheSpearmanrankcorrelation(ρ) motivatesourcombined PG-SCORE computation.
20

|     |                |            |           |         | TeacherModel(S |         | T,ℓ)        |        |     |     |     |
| --- | -------------- | ---------- | --------- | ------- | -------------- | ------- | ----------- | ------ | --- | --- | --- |
|     | Language       | BestMethod | Gemma327B |         | AyaExpanse32B  |         | Llama3.170B |        |     |     |     |
|     | Arabic(ar)     | Respond    |           | +453.1% |                | +355.2% |             | +77.7% |     |     |     |
|     | German(de)     | Generate   |           | +29.3%  |                | +0.3%   |             | +16.4% |     |     |     |
|     | Indonesian(id) | Translate  |           | +458.9% |                | +39.3%  |             | −14.8% |     |     |     |
Table15: PercentageincreaseinPG-SCOREforbestdatagenerationmethod. Percentageincreasewhenusing
thebest-performingdatagenerationmethodcomparedtoanequalmixbaselineofallthreemethods(Generate,
Translate,Respond). Forless-resourcedlanguages(ArabicandIndonesian),usingTranslateorRespondmethods
yieldssubstantialimprovementsformostteachers,thoughgainsareteacher-dependent.
TeacherModel Average Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
| Gemma327BInst. | 0.805 | -0.239 | 0.222  |     | 2.389 | 1.855 |     | 0.239  |     | 0.366  |     |
| -------------- | ----- | ------ | ------ | --- | ----- | ----- | --- | ------ | --- | ------ | --- |
| AyaExpanse32B  | 0.227 | -0.872 | -0.038 |     | 1.979 | 1.353 |     | -0.249 |     | -0.809 |     |
Llama3.170BInst. -0.267 -1.688 -0.807 0.838 1.407 -1.441 0.089
Table16: PG-SCOREofthreeteachermodels(S ϕ =OLMo332B)Weshowthatourfindingsgeneralizeupto
the32Bparameterrangeonthethreeteachermodelswetested: (1)Gemma327Bmaintainsitspositionasthe
mosteffectiveteacher,andthe(2)language-dependenteffectsarestillapparentwithGermanhavingthehighest
PG-SCOREsacrossmostteachers.
Inaddition,teacherrankingsarestablefornearby but it provides empirical evidence of a structural
weighting schemes (ρ 0.90 for adjacent α val- gapthatinhibitsqualitysyntheticdatageneration
≥
ues) as shown in Figure 7. Our finding suggests forlong-taillanguages. Incontrast,wedonotfind
thatmodelrankingsarerobusttosmallchanges a significant correlation between resource avail-
in the weighing of intrinsic and extrinsic met- abilityandPG-SCORE(ρ =0.372,p =0.468).
Our
rics. Ourequalweighting(α = 0.5)balancesboth findingssuggestthatteachermodelgenerationqual-
perspectives, correlating strongly with extrinsic- itydependsmoreheavilyonpretrainingexposure
focused(ρ = 0.89)andreasonablywithintrinsic- than linguistic resources. Additionally, the data
focused(ρ = 0.74)rankings. sourcesfromJoshietal.(2020)donotreflectthe
|     |     |     |     |     | currentlandscape: |     | recentLMsaretrainedoneither |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --------------------------- | --- | --- | --- | --- |
G.5 Effectoflanguageresourcelevelson
|          |     |     |     |     | publicly-available |           | datasets | from | HuggingFace |          | or    |
| -------- | --- | --- | --- | --- | ------------------ | --------- | -------- | ---- | ----------- | -------- | ----- |
| PG-SCORE |     |     |     |     | in-house           | datasets. | While    | our  | work        | includes | 6 di- |
verselanguages,thesamplesizeremainslimited;
Setup Foreachlanguage,weconsiderthefollow-
weencouragefutureworktoexpandthenumberof
| ing properties | drawn from | prior | work: Common- |     |     |     |     |     |     |     |     |
| -------------- | ---------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Crawl(CC)percentageasaproxyforpresencein languagestovalidatethesefindings.
pretrainingdata(%inCC,Raffeletal.,2020),and
|     |     |     |     |     | H DisclosureontheUseofLLMs |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
linguisticresourceavailability(scorefrom1–5,5
ashigh-resource,obtainedfromtheLDCCatalog We used Claude (Anthropic, 2024) to assist with
| andtheELRAMap,Joshietal.,2020). |     |     | Wecom- |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
editing,titleideation,andproofreadingportionsof
| pute the Spearman | rank | correlation | (ρ) between |     |           |                                       |     |     |     |     |     |
| ----------------- | ---- | ----------- | ----------- | --- | --------- | ------------------------------------- | --- | --- | --- | --- | --- |
|                   |      |             |             |     | thiswork. | Allscientificclaimsandinterpretations |     |     |     |     |     |
each property and PG-SCORE across all teacher- are solely our own. We reviewed and revised all
| languagepairs(N=60,10models |     |     | 6languages). |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
LLM-assistedtext.
×
| Results Figure8showstherelationshipbetween |     |     |     |     |                                    |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|                                            |     |     |     |     | I MultilingualSyntheticDataRecipe: |     |     |     |     |     |     |
alanguage’spercentageinCommonCrawlandPG-
CaseStudyonTagalog
SCORE. Weobserveasuggestivepositivetrend
betweenCommonCrawlrepresentationandPG- Asanapplicationofourfindingsanddiscussionin
SCORE (ρ =0.886, p <0.05). This finding sug- §5,wepresentacasestudyondevelopingamulti-
geststhatlanguageswithgreaterpresenceinpre- lingualsyntheticdatarecipeonaheld-outlanguage:
training data enable teacher models to generate Tagalog. Itisamid-resourcelanguage(Category3
higher-quality synthetic data that leads to better inJoshietal.(2020)’staxonomy)andthestandard-
studentperformance. Thisfindingisunsurprising, izedformofFilipino,thenationallanguageofthe
21

GenerationParameters
|     | ModelName           |     |     |     | Temperature |     | Top-p | Top-k | MaxSeqLen |       |     |
| --- | ------------------- | --- | --- | --- | ----------- | --- | ----- | ----- | --------- | ----- | --- |
|     | GPT-4omini          |     |     |     |             | 0.8 | 0.9   | –     | 16,384    |       |     |
|     | Llama3.170BInstruct |     |     |     |             | 0.6 | 0.9   | –     | 131,072   |       |     |
|     | Llama3.18BInstruct  |     |     |     |             | 0.6 | 0.9   | –     | 131,072   |       |     |
|     | CommandA            |     |     |     |             | 0.3 | –     | –     | 128,000   |       |     |
|     | AyaExpanse32B       |     |     |     |             | 0.3 | –     | –     | 128,000   |       |     |
|     | Gemma327BInstruct   |     |     |     |             | 1.0 | 0.95  | 64    |           | 8,192 |     |
|     | Gemma312BInstruct   |     |     |     |             | 1.0 | 0.95  | 64    |           | 8,192 |     |
|     | Gemma34BInstruct    |     |     |     |             | 1.0 | 0.95  | 64    |           | 8,192 |     |
|     | IBMGranite4.0       |     |     |     |             | 0.0 | –     | –     |           | 4,096 |     |
|     | IBMGraniteMicro     |     |     |     |             | 0.0 | –     | –     |           | 4,096 |     |
|     | Default             |     |     |     |             | 0.8 | 0.9   | –     |           | –     |     |
Table 17: Inference settings for each teacher model. Generation parameters are based on model provider
recommendationsfromHuggingFaceand/orofficialdocumentation. TheDefaultrowindicatesparametersused
whenmodel-specificrecommendationsareunavailable. The“–”symbolindicatestheparameterwasnotspecified
intheofficialrecommendations.
| Philippines. |                           |     |     |     |     |     | Source        |     | Num. | Instances |     |
| ------------ | ------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ---- | --------- | --- |
|              |                           |     |     |     |     |     | TaCoAlpaca    |     |      | 10,000    |     |
| I.1 Setup:   | RecipeDesignandEvaluation |     |     |     |     |     |               |     |      |           |     |
|              |                           |     |     |     |     |     | AyaCollection |     |      | 1,241     |     |
|              |                           |     |     |     |     |     | WildChat4.8M  |     |      |           | 997 |
Data WecollectFilipinoseeddatafromvarious
|     |     |     |     |     |     |     | WildChat1M |     |     |     | 250 |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
publicly-availableSFTdatasetssuchasWildChat
4.8MandtheAyaCollection. Inaddition,wealso Tagalogseeddatasetstatistics.
|     |     |     |     |     |     |     | Table18: |     |     |     | Inorderto |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --------- |
includeEnglishdatafromtheTülu3SFTdataset
bootstrapthesyntheticdatagenerationrecipeforTaga-
fortheTranslatemethod. Table18showsthestatis- log,wecurateaseeddatasetcontainingamixofTagalog
ticsoftheseeddatasetusedforTagalogsynthetic andEnglishpromptsfromvarioussources. Majorityof
datageneration. Then,weimplementthefollowing theseeddatasetisfromtheTaCopaper(Upadhayayand
| datainterventionsbasedonourfindings:     |             |          |           |                |           |     | Behzadan,2024).                            |     |          |      |           |
| ---------------------------------------- | ----------- | -------- | --------- | -------------- | --------- | --- | ------------------------------------------ | --- | -------- | ---- | --------- |
| Teacher                                  | Model:      |          |           |                |           |     |                                            |     |          |      |           |
| •                                        |             | we       | use Gemma | 3              | 27B       | In- |                                            |     |          |      |           |
| struct as                                | the teacher |          | model,    | as it was      | the best- |     |                                            |     |          |      |           |
|                                          |             |          |           |                |           |     | matchedteacher-studentpairsyieldhigher     |     |          |      | PG-       |
| performingmodelacrossmosttargetlanguages |             |          |           |                |           |     | SCORE(§3.2).                               |     |          |      |           |
| weevaluated(§3).                         |             |          |           |                |           |     | Forthepurposesofthisreport,wewilldesignate |     |          |      |           |
| • DataGenerationMethod:                  |             |          |           | weusetheTrans- |           |     |                                            |     |          |      |           |
|                                          |             |          |           |                |           |     | the model finetuned                        |     | on Gemma | 3 4B | using our |
| late and                                 | Respond     | methods, |           | as they        | were      | the |                                            |     |          |      |           |
syntheticrecipeas10K-Polyglot-TL,where“10K”
best-performingmethodsformid-resourcelan- indicatesthenumberofSFTinstancesusedduring
| guageslikeIndonesian(§3.3). |     |     |     | Inaddition,we |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
finetuning.
| add a small | sample |     | of prompt-response |     | pairs |     |     |     |     |     |     |
| ----------- | ------ | --- | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
synthesizedviatheGeneratemethod. Evaluation WeevaluateonFILBENCH(Miranda
Synthetic Data Scale: et al., 2025), a benchmark for LMs that includes
| •   |     |     | we  | generate | 10k syn- |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
theticexamplesusingtheselectedteacherand Filipino-centric multiple-choice and generative
data generation method, as we found that this tasks. It measures an LM’s performance across
scaleissufficienttoachievestrongstudentper- four categories such as classical NLP, cultural
formance (Appendix G.1). However, we also knowledge, reading comprehension, and genera-
test on finetuning a model with 25k synthetic tion,alongsideanaggregated FILBENCHscore.
examples to see if more data improves perfor- Wealsocompareagainsttwodatamixbaselines:
10K-Public:
| mance. |     |     |     |     |     |     | 1.  | we  | sample 10k | Tagalog | prompt- |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- |
• Student Base Model: we finetune using the responsepairsfromtheseeddataset. Thisbase-
Gemma 3 4B model, as we find that family- line aims to simulate a non-synthetic data ap-
22

1.50
1.25
1.00
0.75
0.50
0.25
0.00
NLLB NLLBTranslate LMTranslate
TranslateBoth thenRespond
erocS-GPegarevA
1.36
0.85
0.80
2.0
1.5
1.0
0.5
0.0
NLLB NLLBTranslate LMTranslate
TranslateBoth thenRespond
erocS-GP
Arabic
Indonesian 0.0 0.25 0.5 0.75 1.0
German
Figure 6: Effect of translation method on PG-
SCORE. We compare three methods: LM translates
promptEN-to-XXandresponds(LM-Translate),NLLB
translatespromptEN-to-XXandLMresponds(NLLB-
Translate-then-Respond), and NLLB translates both
promptandresponse(NLLB-Translate-Both).
proachtotrainingmultilingualLMs.
2. 10K-GPT-4oM: we synthesize 10k instances
usinganoff-the-shelfteachermodel(GPT-4o-
mini). This baseline simulates a typical data
generation approach of choosing a teacher in
anadhocmannerduetoitsperceivedstrength
(sizeorbenchmarkperformance)oreaseofuse.
Forallmethods,wefinetuneaGemma34Bbase
modelusingthesametrainingsettingsindicatedin
AppendixE.1.
I.2 Results: LeaderboardScoresand
Ablations
Table 19 shows the FILBENCH score of our op-
timal synthetic recipe compared to other models
in the same parameter range. We find that 10K-
Polyglot-TLiscompetitiveagainst10K-GPT-4oM
(+1.85pp),andhasbetterperformancecomparedto
10K-Public(+2.28pp). Theseresultssuggestthat
(1)syntheticdatagenerationisaviableapproach
for building less-resource language models, and
(2)ourfindingthatselectingstrongteachermodels
basedonPG-scoreiseffective,aslargermodelsdo
0.0
52.0
5.0
57.0
0.1
*:p<0.05 **:p<0.01
1.00
0.97** 1.00
0.89** 0.96** 1.00
0.71** 0.82** 0.94** 1.00
0.41** 0.55** 0.74** 0.91** 1.00
0.6 0.8 1.0
Spearman rank ρ
Figure7: Effectofweighingintrinsicandextrinsic
metricsin PG-SCORE. Modelrankingsremainrela-
tivelystableacrossneighboringweightingsofintrinsic
andextrinsicmetrics.
notalwaysproducebettertrainingdata(§3).
In addition, comparing 10K-Polyglot-TL to
othermodelsintheFILBENCHleaderboard5shows
thattheformeriscompetitiveagainstQwen34B
andLlama3.18BInstruct. Wehighlightthatour
4B models are competitive against other mod-
elswithlargerparametersizes,suggestingthat
a multilingual synthetic data recipe based on our
PG-SCOREfindingsisdata-efficient. Wealsofind
thatincreasingthenumberofSFTinstances(10k
to 25k) led to a performance increase of 0.21pp.
While we previously found that 10K instances
showed diminishing returns (see Appendix G.1),
thecontinuedgainsfromscalingto25Kinstances
on FILBENCH suggestthatsaturationpointsmay
depend on task diversity. FILBENCH covers a
broader range of NLP tasks (e.g., named-entity
recognition)comparedtoourexperimentalbench-
marksin§3andAppendixG,indicatingthatprac-
titionersworkingwithdiversetaskdistributions
may benefit from exploring larger synthetic
datasetsbeyondthe10Kthreshold.
I.3 Analysis: AblationExperiments
In order to measure the contribution of our find-
ingsandrecommendationsin§5,weperformthe
following ablation experiments as shown in Fig-
ure9. Notethattheinterventionsdescribedbelow
5Official FILBENCH leaderboard: https://hf.co/
spaces/filbench/filbench-leaderboard
23

|     |     |                |     |     |     | Model |     |     |     | FILBENCHScore |     |     |
| --- | --- | -------------- | --- | --- | --- | ----- | --- | --- | --- | ------------- | --- | --- |
|     | ρ   | =0.886, p<0.05 |     |     |     |       |     |     |     |               |     |     |
4
|          |     |     |     |     |     | GPT-4o(2024-08-06) |     |     |     |     |     | 74.27 |
| -------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | ----- |
|          |     |     |     |     |     | Gemma327BInst.     |     |     |     |     |     | 55.17 |
| erocS-GP |     |     |     |     |     | Gemma312BInst.     |     |     |     |     |     | 54.04 |
2
|     |     |      |      |     |     | 25K-Polyglot-TL4B |     |     |     |     |     | 49.73 |
| --- | --- | ---- | ---- | --- | --- | ----------------- | --- | --- | --- | --- | --- | ----- |
|     |     |      |      |     |     | 10K-Polyglot-TL4B |     |     |     |     |     | 49.52 |
|     |     |      |      |     |     | Qwen34B           |     |     |     |     |     | 48.42 |
|     | 0   |      |      |     |     | 10K-GPT-4oM       |     |     |     |     |     | 47.67 |
|     |     |      |      |     |     | Llama3.18BInst.   |     |     |     |     |     | 47.38 |
|     |     |      |      |     |     | Ministral8BInst.  |     |     |     |     |     | 47.33 |
|     | <1% | 1–2% | 2–5% |     | >5% | 10K-Public        |     |     |     |     |     | 47.24 |
|     |     |      |      |     |     | Pangea7B          |     |     |     |     |     | 43.98 |
PercentageofaLanguage
|     |     | inCommonCrawl |     |     |     | SeaLLMs31.5B |     |     |     |     |     | 43.20 |
| --- | --- | ------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ----- |
Relationshipbetweenalanguage’spercent-
Figure8:
Table19: Modelperformanceonaheld-outlanguage
| ageinCommonCrawlandPG-SCORE. |     |     |     |     | Weobservea |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
(Tagalog)asevaluatedonFILBENCH(Mirandaetal.,
suggestivepositivetrend(ρ=0.886,p<0.05)between
|     |     |     |     |     |     | 2025). | We  | compare | ouroptimalsyntheticrecipe |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------- | ------------------------- | --- | --- | --- |
CommonCrawlrepresentationandPG-SCOREacross
thesixlanguagestested. against baselineapproaches and other models in the
sameparameterrange.
areadditive.
|          |     |                       |     |      |          | 4Bbasemodel. |     | Thisinterventionyieldsasubstan- |     |     |     |     |
| -------- | --- | --------------------- | --- | ---- | -------- | ------------ | --- | ------------------------------- | --- | --- | --- | --- |
| Curation |     | of publicly-available |     | data | vs. Syn- |              |     |                                 |     |     |     |     |
tialperformanceimprovement,demonstratingthat
| theticdatageneration |     |     | Wecomparestudentmod- |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
familyalignmentisareliableheuristicforteacher
elstrainedon(1)publicly-availableTagalogSFT selection. Theimprovementfromfamilymatching
data and (2) synthetic SFT instances generated isconsistentwithourfindingsthatfamily-matched
| by a | GPT-4o    | teacher (note | that | these | are also the |               |     |          |        |        |          |     |
| ---- | --------- | ------------- | ---- | ----- | ------------ | ------------- | --- | -------- | ------ | ------ | -------- | --- |
|      |           |               |      |       |              | pairs achieve |     | at least | +20.5% | higher | PG-SCORE |     |
| same | baselines | in Appendix   |      | I.2). | We find that |               |     |          |        |        |          |     |
comparedtomismatchedpairs,likelyduetoshared
theperformanceofthesetwobaselinesaresimilar tokenization schemes and architectural similari-
(∆ = 0.5pp),
suggesting that there is no signifi- tiesthatfacilitatebetterknowledgetransferfrom
| cant | advantage | to using | a synthetic |     | data pipeline |     |     |     |     |     |     |     |
| ---- | --------- | -------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
teachertostudent.
| if the    | teacher | model is                 | not optimal. |     | We also hy- |          |      |       |     |          |     |        |
| --------- | ------- | ------------------------ | ------------ | --- | ----------- | -------- | ---- | ----- | --- | -------- | --- | ------ |
|           |         |                          |              |     |             | Increase | data | scale | We  | increase | the | number |
| pothesize | that    | some publicly-accessible |              |     | datasets    |          |      |       |     |          |     |        |
in Tagalog were semi-synthetic (e.g., TaCO uses of synthetic instances from 10k to 25k to assess
whetheradditionaldatacontinuestoimproveper-
asyntheticpipelineakintotheTranslatemethod,
|     |     |     |     |     |     | formance. | We  | observe | a   | modest | gain | of 0.21pp, |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | ------ | ---- | ---------- |
butusingchain-of-thoughttoimprovethequality
|     |     |     |     |     |     | which | is smaller | than | the | improvements |     | from |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | ---- | --- | ------------ | --- | ---- |
oftranslations),makingitdifficulttoperformafair
| comparison. |     |     |     |     |     | teachermodelselectionandmodelfamilymatch- |         |        |      |     |         |          |
| ----------- | --- | --- | --- | --- | --- | ----------------------------------------- | ------- | ------ | ---- | --- | ------- | -------- |
|             |     |     |     |     |     | ing. This                                 | finding | aligns | with | our | earlier | observa- |
Usingateacherwithahigher PG-SCORE We tionthatgainsdiminishbeyond10kexamples(Ap-
thenswaptheGPT-4o-miniteacherwithAyaEx-
pendixG.1),thoughthecontinuedimprovementon
panse 32B, a teacher with a higher PG-SCORE FILBENCH’sdiversetaskdistributionsuggeststhat
based on our main findings (0.461 vs. 0.706, c.f. saturationpointsmaybetask-dependent.
| §3, Table |     | 1). We observe | a   | slight | performance |          |       |       |     |          |     |         |
| --------- | --- | -------------- | --- | ------ | ----------- | -------- | ----- | ----- | --- | -------- | --- | ------- |
|           |     |                |     |        |             | Increase | model | scale |     | Finally, | we  | explore |
improvementinthisintervention,suggestingthat
whetherscalingthestudentmodelfrom4Bto12B
| the PG-SCORE |     | metric | is generalizable |     | across an |           |            |     |          |            |     |         |
| ------------ | --- | ------ | ---------------- | --- | --------- | --------- | ---------- | --- | -------- | ---------- | --- | ------- |
|              |     |        |                  |     |           | (and 27B) | parameters |     | provides | additional |     | perfor- |
unseenlanguage.
|     |     |     |     |     |     | mancegains. | Wefindthatthelargerstudentmodel |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------------------------- | --- | --- | --- | --- | --- |
Matching teacher and student model families achieves higher performance, demonstrating that
Oneofourkeyfindingsandrecommendationisto our synthetic data recipe benefits from increased
match the model families of the teacher and the modelcapacity. Thisresultisconsistentwithour
student (§3.2). We use a Gemma 3 Instruct 27B generalizationexperiments(AppendixG.2),where
teachermodeltomatchthefamilyoftheGemma3 weshowedthat PG-SCORE generalizesacrossdif-
24

|     |     | EROCS |           |            |                |            | + S c ale            | s i ze + S c a les i z e |
| --- | --- | ----- | --------- | ---------- | -------------- | ---------- | -------------------- | ------------------------ |
|     |     |       | + U se    | sy nthetic | + B e tt e r + | M a t ch + | S c a le d a ta      |                          |
|     |     | 75    |           |            | fa             | m il y (1  | 0 k → 2 5 k ) (4 B → | 1 2 B ) (1 2 B → 2 7 B ) |
|     |     |       | pi pe lin | e          | te ac h e r    |            |                      |                          |
51.4 53.0
|     |     | 50  | 47.2 | 47.7 | 48.2 | 49.5 | 49.7 |     |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | --- |
HCNEBLIF
25
0
|     |     |     | None | GPT-4o | AyaExp  | ——–Gemma327B——– |       |     |
| --- | --- | --- | ---- | ------ | ------- | --------------- | ----- | --- |
|     |     |     |      |        |         | |               |       | |   |
|     |     |     |      |        | Teacher |                 | Model |     |
Studentmodelperformanceonaheld-outlanguage(Tagalog)acrossseveralsyntheticdatainterven-
Figure9:
tions. Givenaheld-outlanguage(Tagalog)andanevaluationbenchmark(FILBENCH),weapplydatainterventions
basedonourrecommendationsoncreatingamultilingualsyntheticdatarecipe(§5).
| ferent model            | sizes | while                        | maintaining        | the   | relative  |     |     |     |
| ----------------------- | ----- | ---------------------------- | ------------------ | ----- | --------- | --- | --- | --- |
| rankingofteachermodels. |       |                              | However,wenotethat |       |           |     |     |     |
| the performance         |       | of our                       | best models        | are   | still be- |     |     |     |
| hind Gemma              | 3 27B | Instruct                     | and                | Gemma | 3 12B     |     |     |     |
| Instruct(Table19).      |       | Giventhatobservation,westill |                    |       |           |     |     |     |
arguethatoursyntheticpipeline,whichuses25K
instancestrainedonlyviaSFT,canbeconsidered
| data and | resource-efficient |     | compared | to  | the post- |     |     |     |
| -------- | ------------------ | --- | -------- | --- | --------- | --- | --- | --- |
traininginterventionsdoneinGemma3,whichin-
volvedinstruction-tuningandreinforcementlearn-
ingobjectives(GemmaTeametal.,2025).
J InferenceDetails
| Prompttemplates |     | Figure10toFigure12show |     |     |     |     |     |     |
| --------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
theprompttemplatesusedforeachdatageneration
| method. Inaddition,Figure13showstheprompt |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
templateusedfortheLLM-as-a-judgemethodto
evaluatetextquality.
| Inferencesettings |     | WeusevLLM(Kwonetal., |     |     |     |     |     |     |
| ----------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
2023)andCurator(Martenetal.,2025)forinfer-
| ence. Foreachteachermodel, |     |     | wecheckwhether |     |     |     |     |     |
| -------------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
themodelproviderrecommendedbestsettingsfor
| usage. If         | not, then | we set      | a default | configuration |        |     |     |     |
| ----------------- | --------- | ----------- | --------- | ------------- | ------ | --- | --- | --- |
| (temperature=0.8, |           | top_p=0.9). | Table     | 17            | summa- |     |     |     |
rizestheinferencesettingsweusedforeachteacher
model.
25

Generate:samplekprompt-responsepairsfromD seed,ℓanduseitasin-contextexamples
Asamultilingualdatagenerator,yourtaskistogenerateanewexample(‘prompt‘and‘response‘)fora
datasetdemonstratinghowAIagentscanfulfillgeneralinstructionsfor{lang_name}.
Todothis,youwillwanttogeneratetwopiecesofinformation:
1)A"prompt"specifyingatasktobecompletedoraquestiontobeanswered(what,where,when,how,who,
why).Thetaskshouldbeverychallengingyetsolvable.
2)A"response"representingavalidcompletionofthattaskinnaturallanguage. Ifthe"response"doesnot
satisfythe"prompt", thenyouhavefailedatyourjob. Donotprovideunnecessarydetails, beyondwhatis
explicitlyneededtosatisfytheinstructionyougenerated.
Hard constraint: The generated task MUST belong to exactly one of the following categories (pick
oneatrandomanddoNOTmentionthecategory).
1.Logicalreasoning/erroranalysis
2.Mathorquantitativereasoningwithexplanation
3.Classificationorlabeling
4.Dialogueorrole-play
5.Translationorparaphrasingwithconstraints
6.Proceduralinstructions(step-by-step)
7.Grammarcorrectionorlinguisticanalysis
8.Short-formcreativeoutput(≤50words)
9.Knowledgerecallwithverificationorcorrection
10.Culturalorpragmaticjudgment
Add diversity to your generations by varying the types of tasks you create, the styles and tones of the
responses,andthecomplexityofthelanguageused.Thiswillhelpensurearichandvarieddataset.Forexample,
youmightcreatetasksthatinvolveansweringknowledge-basedquestions,answeringmathquestions,providing
explanations,generatingcreativecontent,orperformingtranslations.
Please provide a JSON dictionary response that includes the new ‘prompt‘ and its corresponding
‘response‘.Usethe‘prompt‘and‘response‘keysinthedictionary.
Donotgenerateanyothertextinyourresponse(forexample,donotstartyourmessagewithanygreetings,and
neveraskforclarificationorapologizeforstrugglingwiththetask).
Tryyoubesttoensurethattheinputandresponseyougeneratearedistinctfromtheprovidedexampleswhile
maintainingadiverse,detailed,precise,comprehensive,andhigh-qualityresponse.
Itisimportanttogenerateresponsesthatarecontextuallyrelevantandculturallyappropriatefor{lang_name}.
Here are some examples to guide your generation. The best way to use these examples is to identify
thepatternsandstructurestheyfollow,ratherthancopyingthemdirectly:
{% for example in examples[:k] %}
Prompt: {{example[“prompt”]}}
Response: {{example[“response”]}}
{% endfor %}
NewExample:
Figure10: PrompttemplatefortheGeneratedatagenerationmethod.
26

Translate: forward-translateEnglishpromptsfrom anduseteacherT togeneratethe
seed,ℓ
D
responsey
i
Asamultilingualdatagenerator,yourtaskistotranslatethegivenpromptfromEnglishinto
{lang_name}andgeneratetheappropriateresponseinthesamelanguage.
Important: youmustreturnboththetranslatedprompt(into{lang_name})andtheresponse.
Ensurethatboththetranslatedpromptandtheresponsearecoherent,culturallyappropriate,
anddemonstrateadeepunderstandingofthelanguagenuances.
Do not generate any other text in your response (for example, do not start your
messagewithanygreetings,andneveraskforclarificationorapologizeforstrugglingwith
thetask).
DonotreturntheoriginalEnglishprompt. Remember,youmusttranslatethepromptfirst
andreturnit.
Hereisthepromptyouneedtotranslateandrespondto:
{prompt}
Figure11: PrompttemplatefortheTranslatedatagenerationmethod.
Respond: takepromptsfrom anduseteacherT togeneratetheresponsey
seed,ℓ i
D
As a multilingual data generator, you will be presented a user request or instruction in
the{lang_name}language. Yourtaskistogenerateanappropriateresponseforthegiven
request. Ensurethatyourresponseiscoherent,culturallyappropriate,anddemonstratesa
deepunderstandingofthelanguagenuancesDonotgenerateanyothertextinyourresponse
(forexample,donotstartyourmessagewithanygreetings,andneveraskforclarificationor
apologizeforstrugglingwiththetask). Hereisthepromptyouneedtorespondto:
{prompt}
Figure12: PrompttemplatefortheResponddatagenerationmethod.
27

LLM-as-a-judge: evaluatingtextqualityusingthemultilingualrubriclanguagemodel
TaskDescription:
Aninstruction(mightincludeanInputinsideit)in{language},aresponsetoevaluate,and
ascorerubricrepresentingaevaluationcriteriaaregiven.
1. Writeadetailedfeedbackthatassessthequalityoftheresponsestrictlybasedonthegiven
scorerubric,notevaluatingingeneral.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should
refertothescorerubric.
3. Theoutputshouldcontainthescoreandfeedbackonly.
4. Pleasedonotgenerateanyotheropening,closing,andexplanations.
Theinstructiontoevaluate:
{{instruction}}
Responsetoevaluate:
{{response}}
ScoreRubrics:
[Isthemodelproficientinlanguage{lang_name},includingitsculturalnuanceandgram-
maticalusage,andrespondsinahelpfulandharmlessmanneraccordingtotheinstruction?]
Score1: Theresponsecontainsseveregrammaticalerrors,lacksculturalappropriateness,or
isunhelpful/harmful. Thelanguageproficiencyisverypoor.
Score 2: The response has noticeable grammatical errors and limited cultural awareness.
It partially addresses the instruction but with significant gaps in language proficiency or
helpfulness.
Score 3: The response demonstrates adequate language proficiency with some minor
grammaticalerrors. Itshowsreasonableculturalawarenessandaddressestheinstructionina
helpfulmanner,thoughimprovementsarepossible.
Score4: Theresponseexhibitsstronglanguageproficiencywithminimalgrammaticalerrors
andgoodculturalnuance. Itaddressestheinstructioninahelpfulandharmlesswaywith
onlyminorroomforimprovement.
Score5: Theresponsedemonstratesexcellentlanguageproficiencywithpropergrammar,
appropriate cultural nuance, and idiomatic usage. It fully addresses the instruction in a
helpfulandharmlessmanner.
Feedback:
Figure13: WeevaluatetextqualityofsynthesizedtextsusingamultilingualrubricmodelcalledM-Prometheus
(Pombaletal.,2025). WechooseM-Prometheusduetoitsstrongperformanceonmultilingualandhuman-aligned
benchmarks.
28