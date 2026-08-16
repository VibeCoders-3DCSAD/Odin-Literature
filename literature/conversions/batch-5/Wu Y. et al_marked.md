---
conversion_metadata:
  converted_at: "2026-07-21T09:25:40Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Wu Y. et al.pdf"
  source_pdf_sha256: "eccefe4568af843491a673ae278b6938be9a60f3233ef9309003de21ffb37521"
  page_count: 14
  markdown_char_count: 86297
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

6
2
0
2

n
a
J

0
2

]
T
S
.
n
i
f
-
q
[

1
v
3
7
0
0
0
.
2
0
6
2
:
v
i
X
r
a

Test-Time Adaptation for Non-stationary Time Series:
From Synthetic Regime Shifts to Financial Markets

Yurui Wu, Qingying Deng, Wonou Chung, Mairui Li
Department of Statistics & Operations Research, UNC Chapel Hill
Chapel Hill, NC, 27599
{yuruiwu,doradeng,wchung,mairuili}@email.unc.edu

Abstract

Time series encountered in practice are rarely stationary. When the data distribution
changes, a forecasting model trained on past observations can lose accuracy. We
study a small-footprint test-time adaptation (TTA) framework for causal time-
series forecasting and direction classification. The backbone is frozen, and only
normalization affine parameters are updated using recent unlabeled windows. For
classification we minimize entropy and enforce temporal consistency; for regression
we minimize prediction variance across weak time-preserving augmentations and
optionally distill from an EMA teacher. A quadratic drift penalty and an uncertainty-
triggered fallback keep updates stable. We evaluate this framework in two stages:
synthetic regime shifts on ETT benchmarks, and daily equity and FX series (SPY,
QQQ, EUR/USD) across pandemic, high-inflation, and recovery regimes. On
synthetic gradual drift, normalization-based TTA improves forecasting error, while
in financial markets a simple batch-normalization statistics update is a robust
default and more aggressive norm-only adaptation can even hurt. Our results
provide practical guidance for deploying TTA on non-stationary time series. The
source code of this study is available at this Google Drive.

1

Introduction

Real-world time series, such as financial prices or electricity loads, evolve over time. Structural
breaks, policy changes, and macroeconomic shocks can shift both the level and the volatility of the
process. During the COVID-19 crisis and the subsequent high-inflation period, market dynamics
changed rapidly, and models trained on pre-crisis data became miscalibrated. Once the deployment
distribution departs from the training distribution, minimizing training loss is no longer sufficient to
guarantee test performance.

Test-time adaptation (TTA) addresses this issue by updating part of the model using unlabeled test
inputs. For time series, a practical TTA scheme must be causal (no future data), parameter efficient,
and robust to noisy updates. In this work we freeze the backbone and adapt only a small parameter set
at deployment. When day t arrives, we collect the most recent windows, apply weak time-preserving
augmentations, and take a few gradient steps on unsupervised objectives. For classification we
combine entropy minimization with temporal consistency; for regression we minimize augmentation
variance and optionally distill from an exponential-moving-average teacher. We control the size of
daily parameter changes and fall back to a lightweight batch-normalization statistics update when an
uncertainty proxy is high.

Our goal is not to propose a new heavy architecture, but to understand when small-footprint TTA
helps or hurts on non-stationary sequences. We make three contributions. First, we unify several TTA
choices—no adaptation, batch-normalization statistics refresh, and norm-only adaptation—under
one causal framework. Second, we evaluate this framework in two stages: synthetic shifts on ETT

Preprint. Under review.

---

<!-- PAGE 2 -->

benchmarks, and real markets (SPY, QQQ, EUR/USD) split into pandemic, high-inflation, and
recovery regimes. Third, we connect the results with econometric tools (Diebold–Mariano tests
and Newey–West adjustments) and summarize practical recommendations for deploying TTA in
streaming forecasting systems.

2 Literature Review

2.1 Test-time adaptation under distribution shift

TTA minimizes an unsupervised objective at inference using the current test inputs, while most
parameters are frozen. A central result is that tuning only normalization affine parameters (γ, β) by
entropy minimization can yield large gains under covariate shift [1]. This works because normalization
re-centers and re-scales hidden activations to match the present input distribution, and the affine
degrees of freedom are enough to correct many first/second-moment changes. In streaming scenarios,
adaptation can accumulate error if the procedure is aggressive or if pseudo-targets are unstable. Prior
work proposes stabilizers such as exponential-moving-average teachers and conservative update
schedules [2, 3]. We follow this line by using an EMA teacher for self-distillation in regression and
by adding a quadratic drift penalty that discourages large inter-day parameter motion.

Refreshing batch-normalization statistics at test time (recomputing means and variances without
gradients) already improves robustness to small-batch and covariate shifts [4, 5]. This motivates
our fallback: when an uncertainty proxy is high, we refresh statistics and skip gradient updates.
Recent analyses add explanatory depth; for example, Kim and Lee et al. [21] show that TTA can
increase linearity in intermediate layers, which yields more stable extrapolation on shifted inputs. For
forecasting, test-time learning can be formulated with variance and consistency objectives that do not
require labels [22]. Adaptation in non-stationary environments can also be framed as representation
alignment that maintains proximity between current and reference features [20]. Our consistency and
variance objectives, together with EMA-teacher and drift control, are concrete realizations of these
ideas for time series.

2.2 Normalization and architectures for non-stationary sequences

Non-stationarity often manifests as level/scale drift and time-varying seasonality, so normalization
layers are a primary tool. Reversible instance normalization (RevIN) standardizes each sequence
and then reverses the transform before output; it reduces train–test mismatch while preserving the
forecasting target [6]. Adaptive normalization learns gates that respond to distributional changes [7].
Frequency-aware normalization emphasizes multi-scale periodic structure and modulates features
accordingly [8]. These methods act within the backbone. Our TTA instead acts on top of such
defenses, allowing small affine corrections that follow the deployment stream, so the two approaches
are complementary. On the architecture side, the Non-Stationary Transformer incorporates evolving
statistics directly into attention and residual paths [9]. For our hosts we adopt light yet competitive
models—multi-scale residual Temporal Convolutional Networks (TCN) [10] and compact Transform-
ers—as well as PatchTST and TimesNet as references [11, 12]. We select small widths (64–128) and
few layers (2–4) to ensure that test-time updates touch only thousands of parameters, keeping latency
negligible while preserving accuracy.

2.3 Regime-wise evaluation and econometric significance

Statistical performance should be interpreted by regime. Markov-switching models explain how
coefficients and volatility change across states [14], and survey evidence supports regime-dependent
predictability in financial markets [15]. We therefore report rolling curves and regime-wise summaries.
To compare forecast accuracy we use the Diebold–Mariano test with HAC variance estimation [16, 17].
When we evaluate many variants, standard multiple-comparison corrections may be anti-conservative;
Reality Check and SPA address data-snooping by bootstrapping the maximum performance statistic
across models [18, 19]. Our significance reporting is aligned with these tools.

2

---

<!-- PAGE 3 -->

3 Problem Setup

Let {xt}T
RL×d and study two tasks.

t=1, xt ∈ Rd be a multivariate series. We form an input window Xt = [xt−L+1, . . . , xt] ∈

1. Classification: predict the direction for day t+1; let yt+1 ∈ {0, 1} denote down or up, and
let ˆp(Xt) ∈ [0, 1]2 be the predicted probability. We track accuracy, F1, AUC, direction
accuracy, and expected calibration error (ECE), and draw reliability diagrams.

2. Regression: predict next-day log-return rt+1 = log pt+1 − log pt or H-day cumulative

log-return rt+1:t+H = (cid:80)H

h=1 rt+h; we report MAE, RMSE, and R2.

The deployment stream {Pt} is non-stationary relative to training Ptrain, with shifts including location-
scale drift, noise inflation, and structural changes. Synthetic generators in Appendix B implement
these. For daily equity and FX series we use a unified split: train 2000–2016, validation 2017–2019,
test 2020–2025. All scalers are fit on training only, and we avoid exogenous variables to prevent
leakage. ETT benchmarks follow their standard splits.

4 Method

We train a backbone fθ on the training split with supervised losses. At test time we adapt a small
parameter set on unlabeled windows from the current stream; the backbone is frozen.

4.1 Backbones and updateable units

We consider a multi-scale residual TCN and a compact Transformer (2–4 layers, width 64–128).
GRU/LSTM serve as references. At test time, we compare the following options:

• no_tta: no test-time adaptation, frozen model.
• bn_stats: refresh batch-normalization (BN) means and variances using the current batch, no

gradients.

• norm_only: update only normalization affine parameters (γ, β).

4.2 Unsupervised objectives

Let B be the batch of recent unlabeled windows. For classification we use entropy and consistency:

Lent(θ) =

Lcons(θ) =

1
|B|

1
|B|

(cid:88)

(cid:16)

(cid:88)

−

ˆpc(X) log ˆpc(X)

(cid:17)

,

c

(cid:13)ˆp(X) − ˆp(T (X))(cid:13)
(cid:13)
2
2,
(cid:13)

X∈B
(cid:88)

X∈B

(1)

(2)

where T is a weak time-preserving transform (Section 4.4). For regression we use variance minimiza-
tion and EMA-teacher self-distillation:

Lvar(θ) =

Lsd(θ, ˜θ) =

1
|B|

1
|B|

(cid:88)

X∈B
(cid:88)

X∈B

Var(cid:0){ˆy(Tk(X))}K

k=1

(cid:1),

(cid:13)
(cid:13)ˆy(X) − ˜y(X)(cid:13)
2
2,
(cid:13)

˜θ ← ρ˜θ + (1 − ρ)θ.

Drift control: we penalize inter-day change in the small parameter set,
(cid:13)θ(t) − θ(t−1)(cid:13)
2
2.
(cid:13)

Ldrift(θ(t), θ(t−1)) = γ (cid:13)

Total objective: for classification,

L(θ) = α Lent + β Lcons + Ldrift,

and for regression,

(3)

(4)

(5)

(6)

L(θ) = α Lvar + β Lsd + Ldrift.
(7)
Appendix A provides derivations and gradients for norm-only parameters, including proximal inter-
pretations of the drift penalty and the variance-reduction role of the EMA teacher.

3

---

<!-- PAGE 4 -->

4.3 Uncertainty-triggered fallback

(cid:80)

For classification, we use mean entropy
For regression, we use mean augmentation variance ut =
X Var({ˆy(Tk(X))}k). We set τ as the 80th percentile of ut on validation; 70% and 90%

We compute an uncertainty proxy on B.
ut = 1
|B|
(cid:80)
1
|B|
are ablated. If ut > τ , we refresh BN statistics and skip gradient updates.

X H(ˆp(X)).

4.4 Causality-preserving augmentations

We use weak transforms that keep time order and avoid leakage: amplitude scaling (1±5%), Gaussian
jitter with standard deviation 0.01 times the training standard deviation, time jitter by ±1 step within
the window, and time cutout masking up to 5 steps.

4.5 Daily test-time adaptation algorithm

Default hyperparameters are W =64, S=5, learning rate 10−4, and α = β = 1, γ = 10−3.

Algorithm 1: Causal Test-Time Adaptation for Day t
Input: Frozen backbone fθ; updatable parameter set ϕ ⊂ θ (norm-only BN affine parameters);
Window length L; context size W ; steps S; learning rate η; uncertainty threshold τ ;
Loss type: classification ((6)) or regression ((7)); transforms {Tk}.
Output: Prediction ˆyt+1 (or ˆpt+1) for the next day.

1 Build unlabeled batch B ← {Xt−W +1, . . . , Xt}.
2 Compute uncertainty ut (entropy or augmentation variance).
3 if ut > τ then
4

Refresh BN running statistics on B; return ˆyt+1 ← fθ(Xt).

5 for s = 1 to S do
6

if classification then

7

8

9

10

11

12

Sample a weak transform T ; compute Lent and Lcons.
L ← αLent + βLcons + γ∥ϕ − ϕprev∥2
2.

else

regression

Sample K transforms {Tk}; compute Lvar and optionally Lsd.
L ← αLvar + βLsd + γ∥ϕ − ϕprev∥2
2.
Update only ϕ ← ϕ − η∇ϕL (SGD/Adam).

13
14 return ˆyt+1 ← fθ(Xt) with updated ϕ.

4.6 Ablations and sensitivity

Only thousands of parameters are updated, so extra latency per test day is small on a single T4
GPU. For the hyperparameters, we sweep W ∈ {32, 64, 96}, S ∈ {1, 3, 5}, and learning rate
in {5 × 10−5, 10−4, 2 × 10−4}. We compare entropy-only vs. consistency-only vs. combined
for classification, and variance-only vs. variance plus EMA teacher for regression. We examine
augmentation sets: scaling only; scaling plus jitter; scaling plus jitter and cutout.

5 Data and Shift Construction

Stage I: ETT with synthetic shifts. We use ETTh1/ETTh2 (hourly) and ETTm1/ETTm2 (15-min).
These series include power transformer loads and temperatures with clear seasonality. We generate
three synthetic shifts: (i) gradual mean/variance drift, (ii) local noise inflation, and (iii) structural
switches in periodic components. Formal definitions and grids are in Appendix B.

4

---

<!-- PAGE 5 -->

Figure 1: Regime diagnostics for SPY volatility and returns.

Stage II: equity and FX markets. We use daily SPY and QQQ index ETFs, plus EUR/USD
exchange rates. Features are built from OHLCV only and standardized using training statistics:

rt = log(Ct) − log(Ct−1),

MOM(N )

t = log(Ct) − log(Ct−N ),

REV(N )

t = −

N
(cid:88)

i=1

rt−i,

ATRt = EMA(cid:0) max{Ht − Lt, |Ht − Ct−1|, |Lt − Ct−1|}(cid:1),

σ2
P,t =

1
4 ln 2

(log(Ht/Lt))2,

σ2
GK,t = 1

2 (log(Ht/Lt))2 − (2 ln 2 − 1)(log(Ct/Ot))2.

We split testing into three regimes: (1) pandemic (2020), (2) high-inflation (2021–2023), (3) recovery
(2024–2025). Figure 1 shows basic regime diagnostics for SPY.

6 Experimental Protocol

We evaluate our test-time adaptation framework on three financial direction classification tasks (SPY,
QQQ, and EUR/USD) and one long-horizon time-series forecasting task (ETTh1). All datasets are
preprocessed into fixed-length sliding windows with input length L = 96, and ETTh1 is evaluated
with forecast horizon H = 96. Data are split chronologically into training, validation, and test sets to
ensure strict out-of-sample evaluation. All models use a Temporal Convolutional Network (TCN)
with three residual blocks, hidden dimension 64, and kernel size 3, followed by a linear head for
either classification or regression.
Models are trained using AdamW with learning rate 10−4, batch size 512, and early stopping based
on validation AUC (classification) or validation MSE (regression). At deployment, three main
modes are compared: no adaptation (no_tta), batch-normalization statistics refresh (bn_stats), and
norm-only parameter adaptation (norm_only). Test-time adaptation is triggered using an uncertainty
threshold τ estimated as the 0.8 quantile of validation uncertainty, computed via prediction entropy
for classification and variance of stochastic augmentations for regression. When triggered, norm-only
parameters are updated using a small number of unsupervised gradient steps with entropy/consistency
loss for classification or variance/distillation loss for regression. Evaluation is performed strictly on
the test set using accuracy, F1, AUC, and ECE for classification; MAE, RMSE, and R2 for regression;
along with rolling performance, reliability diagrams, Diebold–Mariano statistical tests, and a simple
directional trading backtest with Newey–West adjusted statistics.

5

---

<!-- PAGE 6 -->

Table 1: Representative ETTh1 results under synthetic regime shifts. Each entry corresponds to one
representative configuration in the specified regime.

Method

Shift

MAE RMSE

no_tta
norm_only
bn_stats

Gradual
Noise
Structural

0.22
0.29
1.26

0.28
0.35
1.62

R2

-0.31
-0.02
-20.80

Figure 2: Rolling forecast metrics on ETTh1 under gradual drift.

7 Results

7.1 Stage I: synthetic shifts on ETT

We first study how different TTA choices behave under controlled shifts on ETTh1. Table 1 reports
mean absolute error (MAE), root mean squared error (RMSE), and R2 for one representative configu-
ration in each synthetic regime: gradual drift, local noise inflation, and structural switches. Negative
R2 values indicate that the model performs worse than a simple training-baseline benchmark under
the corresponding shift.

Norm-only adaptation is most effective under gradual mean/variance drift, where updating normaliza-
tion affine parameters can track slow changes in scale and level. Under local noise inflation, variance
minimization across weak augmentations stabilizes regression outputs and reduces the impact of
noise bursts. Structural switches are the hardest case: even with bn_stats, errors remain large and R2
is strongly negative.

Figure 2 shows rolling forecast metrics on ETTh1 under gradual drift. Compared with the frozen
baseline, norm-only TTA reduces errors in the later part of the horizon, where the synthetic drift
accumulates. This supports the view that normalization-based updates are well suited to smooth
low-order moment shifts.

7.2 Stage II: equity and FX markets

We next evaluate direction classification on SPY, QQQ, and EUR/USD with the same TTA recipe.
Table 2 reports cross-market direction accuracy for all three methods. The baseline accuracy is close
to 0.5 on all series, reflecting the difficulty of daily direction prediction.

These numbers come from a run focused on directional accuracy; absolute values differ from other
experiments, but patterns are consistent. There is no single winner: different markets and regimes
prefer different TTA variants. On SPY, norm_only achieves the best directional accuracy, slightly
ahead of no_tta and bn_stats. On QQQ, bn_stats provides the largest gain, while norm_only can hurt
performance. On EUR/USD, both TTA methods are roughly on par with or slightly better than the
frozen baseline.

Figure 3 plots rolling direction accuracy and RMSE for SPY, QQQ, and EUR/USD with regime
shading. For SPY, improvements from TTA are concentrated in the pandemic and early recovery
periods, when distributional change is strong. For QQQ, batch-normalization statistics updates

6

---

<!-- PAGE 7 -->

Table 2: Directional accuracy on test sets (2020–2025) for equity and FX markets.

Method

SPY

QQQ EURUSD Avg. rank

no_tta
bn_stats
norm_only

0.504
0.498
0.512

0.503
0.525
0.463

0.516
0.520
0.516

2.33
1.66
2.00

Figure 3: Rolling metrics for SPY, QQQ, and EUR/USD with regime shading.

(bn_stats) are particularly effective, while norm_only can overfit local noise and degrade accuracy.
For EUR/USD, bn_stats yields the most stable gains, and norm_only behaves similarly to the frozen
baseline.

7.3 Statistical tests and backtests

To assess whether observed differences are statistically meaningful, we run Diebold–Mariano tests on
daily forecast losses. Table 3 reports DM statistics and p-values for pairwise comparisons between
bn_stats, norm_only, and no_tta. Negative DM values indicate that the first method outperforms the
second under our loss convention. On SPY and QQQ, bn_stats is significantly better than no_tta at
the 5% level, while norm_only is significantly worse than no_tta. On EUR/USD, bn_stats is also
significantly better than no_tta, and norm_only is indistinguishable from the baseline.

7

---

<!-- PAGE 8 -->

Table 3: Diebold–Mariano tests comparing forecast losses.

Comparison

Dataset

DM Stat

p-value

Notes

SPY
bn_stats vs no_tta
SPY
norm_only vs no_tta
QQQ
bn_stats vs no_tta
QQQ
norm_only vs no_tta
bn_stats vs no_tta
EURUSD
norm_only vs no_tta EURUSD

-2.781
6.810
-2.290
8.936
4.350
-0.112

0.0054
0.0000
0.0220
0.0000
0.0000
0.9109

bn_stats significantly better
no_tta significantly better
bn_stats significantly better
no_tta significantly better
bn_stats significantly better
no significant difference

Table 4: SPY backtest performance with Newey–West adjustment.

Strategy

Ann. return Ann. volatility

Sharpe (NW t)

No-TTA
BN-Stats
Norm-Only

3.321
7.933
2.029

4.621
9.582
3.460

1.746
1.930
1.544

Finally, we connect predictive accuracy with simple economic metrics. Tables 4 and 5 report
annualized return, annualized volatility, and Sharpe ratio for a basic directional strategy on SPY
and QQQ, together with Newey–West adjusted t-statistics. On both assets, bn_stats achieves the
highest Sharpe ratio, while norm_only underperforms the frozen baseline. These backtests are
purely illustrative, but they show that the statistical gains from bn_stats translate into more attractive
risk-adjusted returns, whereas naive norm-only updates can be harmful.

8 Discussion and Conclusion

Normalization-based TTA is most effective when shifts mainly change low-order moments. In the
synthetic ETTh1 experiments with gradual drift, updating normalization affine parameters tracks
the changing scale and reduces forecast error. Local noise inflation is partly handled by variance-
based objectives, but structural switches in periodic components still lead to large errors even after
adaptation. This suggests that norm-only updates are well suited to smooth covariate drift, but they
do not fully solve sharp or regime-changing dynamics.

In contrast, the equity and FX series (SPY, QQQ, EUR/USD) are noisy, heavy-tailed, and affected by
jumps and microstructure noise. Here a simple refresh of batch-normalization statistics is a safe and
effective default: bn_stats achieves higher direction accuracy and Sharpe ratios on SPY and QQQ,
and the Diebold–Mariano tests show statistically significant improvements over the frozen baseline.
Aggressive norm-only adaptation, even with drift control, can overfit short windows, perform worse
than no_tta, and reduce economic performance in the backtests.

Our results also highlight the importance of uncertainty control. The fallback rule, which skips
gradient-based adaptation on days with high entropy or large augmentation variance, mitigates many
failure cases of norm-only updates and limits the frequency of harmful steps. At the same time,
the choice of hyperparameters (W, S, η, τ ) and the stability of the backbone remain important, and
different assets may favor different adaptation regimes. Synthetic shift generators are necessarily
stylized and cannot cover all real dynamics, so more realistic benchmarks and stress tests are a natural
direction for future work.

Overall, this study provides an empirical picture of when small-footprint TTA helps and when it hurts
on non-stationary time series. For practitioners, our main recommendation is to start from bn_stats as
a default, add norm-only updates only when validation and uncertainty diagnostics support them, and
always evaluate with regime-wise metrics and robust statistical tests. We hope these findings will
help both practitioners and researchers design safer and more effective test-time adaptation pipelines
for real-world time series.

8

---

<!-- PAGE 9 -->

Table 5: QQQ backtest performance with Newey–West adjustment.

Strategy

Ann. return Ann. volatility

Sharpe (NW t)

No-TTA
BN-Stats
Norm-Only

10.884
20.293
3.136

7.689
11.974
5.204

3.205
4.080
1.349

References

[1] D. Wang, E. Shelhamer, S. Liu, B. Olshausen, and T. Darrell. Tent: Fully test-time adaptation by entropy

minimization. In ICLR, 2021.

[2] J. Wang, Y. Liu, W. Zhang, et al. Continual test-time domain adaptation. In CVPR, 2022.

[3] L. Yuan, S. Wang, et al. Robust test-time adaptation in dynamic scenarios. In CVPR, 2023.

[4] Z. Yang, Z. Li, et al. Test-time batch normalization. arXiv:2205.10210, 2022.

[5] S. Schneider, A. Minderer, et al. Improving robustness against common corruptions by covariate-shift

adaptation at test time. In NeurIPS, 2020.

[6] T. Kim, H. Oh, et al. Reversible instance normalization for accurate time-series forecasting against

distribution shift. In ICLR, 2022.

[7] W. Liu, S. Zhang, et al. Adaptive normalization for non-stationary time series forecasting. In NeurIPS,

2023.

[8] J. Ye, Z. Zhang, et al. Frequency-adaptive normalization for non-stationary time series. In NeurIPS, 2024.

[9] M. Liu, X. Zhang, et al. Non-stationary transformers: Exploring the stationarity in time series forecasting.

In NeurIPS, 2022.

[10] S. Bai, J. Z. Kolter, and V. Koltun. An empirical evaluation of generic convolutional and recurrent networks

for sequence modeling. arXiv:1803.01271, 2018.

[11] Y. Nie, N. Liu, et al. A time series is worth 64 words: Long-term forecasting with transformers. In ICLR,

2023.

[12] H. Wu, J. Xu, et al. TimesNet: Temporal 2D-variation modeling for general time series analysis. In ICLR,

2023.

[13] H. Zhou, S. Zhang, et al. Informer: Beyond efficient transformer for long sequence time-series forecasting.

In AAAI, 2021.

[14] J. D. Hamilton. A new approach to the economic analysis of nonstationary time series and the business

cycle. Econometrica, 1989.

[15] A. Ang and A. Timmermann. Regime changes and financial markets. Annual Review of Financial

Economics, 2011.

[16] F. X. Diebold and R. S. Mariano. Comparing predictive accuracy. Journal of Business and Economic

Statistics, 1995.

[17] W. K. Newey and K. D. West. A simple, positive semi-definite, heteroskedasticity and autocorrelation

consistent covariance matrix. Econometrica, 1987.

[18] H. White. A reality check for data snooping. Econometrica, 2000.

[19] P. R. Hansen. A test for superior predictive ability. Journal of Business and Economic Statistics, 2005.

[20] W. Zhang, X. Li, et al. Test-time adaptation in non-stationary environments via adaptive representation

alignment. In NeurIPS, 2024.

[21] D. Kim, Y. Lee, et al. Test-time adaptation induces stronger accuracy and linearity. In NeurIPS, 2024.

[22] V. Christou, et al. Test time learning for time series forecasting. arXiv:2409.14012, 2024.

9

---

<!-- PAGE 10 -->

A Notation and Derivations

We expand the objectives used in Section 4, give gradients for norm-only batch-normalization (BN)
affine parameters, and explain why each term helps under typical regime shifts. Symbols follow the
main text.

A.1 Norm-only updates as moment matching

Consider a BN-normalized hidden channel

h = BN(u) =

u − µ
σ

,

y = γh + β,

where (µ, σ) are the BN statistics from the current stream and (γ, β) are the trainable affine parameters.
Under a covariate shift with new moments (µ′, σ′), the pre-affine hidden becomes

Choosing

h′ =

u − µ′

σ′ =

σ
σ′ h +

µ − µ′
σ′

.

γ′ = γ ·

σ
σ′ ,

β′ = β + γ ·

µ − µ′
σ′

exactly restores y for all u if the shift is purely first/second moments. Thus small changes of (γ, β)
can cancel location/scale drift at the feature level.

For a scalar loss L, the gradients satisfy

∂L
∂γc

(cid:88)

=

i

∂L
∂yi,c

hi,c,

∂L
∂βc

(cid:88)

=

i

∂L
∂yi,c

,

where c indexes channels and i indexes batch elements. Adapting (γ, β) therefore re-centers and
re-scales along directions where the loss is sensitive. This explains why norm-only is effective
when regime shifts dominantly alter low-order moments, which is exactly the case in our synthetic
gradual-drift experiments.

A.2 Entropy minimization and decision margin

For a two-class softmax ˆp(X) = (p, 1 − p), the entropy is

The derivative and second derivative with respect to p are

H(ˆp) = −p log p − (1 − p) log(1 − p).

dH
dp

= log

1 − p
p

,

d2H
dp2 =

1
p

+

1
1 − p

> 0,

so H is strictly convex in p with minima at p ∈ {0, 1}. A first-order Taylor expansion around the
pre-update p0 shows that a small gradient step with learning rate η reduces H by approximately
η(cid:0) dH
, pushing posteriors away from indecision. Under the usual cluster or low-density separation
assumptions, this coincides with increasing the margin around decision boundaries, which is beneficial
when P (X) drifts but class-conditional structure persists.

(cid:1)2

dp

A.3 Consistency as Jacobian control along causal directions

Let Tϵ be a weak time-preserving transform with T0 equal to the identity. By Taylor expansion,

ˆp(Tϵ(X)) ≈ ˆp(X) + J ˆp(X) ∆X + O(ϵ2),

dϵ Tϵ(X)(cid:12)

where ∆X = d

∥ˆp(X) − ˆp(Tϵ(X))∥2

(cid:12)ϵ=0 and J ˆp is the Jacobian of ˆp with respect to X. Then
(cid:1)∆X .
2 ≈ ∥J ˆp(X) ∆X ∥2
Minimizing the consistency loss therefore penalizes the directional Jacobian norm along small,
causality-preserving deformations (re-timing ±1, mild amplitude changes). This makes predictions
insensitive to benign local perturbations that often accompany measurement noise or microstructure
changes under new regimes.

2 = ∆⊤
X

(cid:0)J ⊤

ˆp J ˆp

10

---

<!-- PAGE 11 -->

A.4 Augmentation-variance minimization and local risk control

For regression with K transforms, define ˆyk = ˆy(Tk(X)) and ¯y = 1
K

(cid:80)K

k=1 ˆyk. The sample variance

Var({ˆyk}) =

1
K − 1

K
(cid:88)

k=1

(ˆyk − ¯y)2

upper-bounds the expected squared deviation under a local neighborhood N (X) of perturbations
when the transform set covers principal directions. Hence minimizing EX [Var] reduces the local
Lipschitz constant of the predictor around each X, which is desirable when the test distribution
features transient noise inflation.

The gradient of the variance term with respect to each ˆym is

∂
∂ ˆym

Var({ˆyk}) =

2
K

(ˆym − ¯y),

so the loss pulls disagreeing outputs toward their mean and shrinks dispersion.

A.5 EMA-teacher self-distillation as temporal ensembling

Let ˜θ be an exponential moving average of the adapted parameters:

˜θ ← ρ˜θ + (1 − ρ)θ,

with ρ ∈ (0, 1). Under a locally quadratic loss with unbiased gradient noise, Polyak averaging implies
that ˜θ has lower variance than the instantaneous θ. Distillation

Lsd =

1
|B|

(cid:88)

X∈B

∥ˆyθ(X) − ˆy˜θ(X)∥2

2

regularizes the student toward a low-pass filtered target, damping oscillations produced by small
batches and a changing B. A simple scalar model with i.i.d. zero-mean gradient noise shows that
the teacher’s variance is scaled by 1−ρ
1+ρ relative to the student’s, so larger ρ yields a steadier target.
This improves stability without requiring labels and complements the variance term by anchoring to a
temporally smoothed predictor.

A.6 Drift penalty as proximal update

Let ϕ denote all adapted BN affine parameters. On day t we solve

min
ϕ

Lunsup(ϕ) + γ∥ϕ − ϕ(t−1)∥2
2,

where Lunsup is the entropy/consistency loss (classification) or variance/distillation loss (regression).
A single gradient step with step size η gives

ϕ(t) = ϕ(t−1) − η

(cid:16)

(cid:17)
∇Lunsup(ϕ(t−1)) + 2γ(ϕ(t−1) − ϕ(t−2))

,

which is equivalent to SGD with a quadratic proximal term that shrinks motion toward the previous
day. In a locally quadratic loss, the exact minimizer is a ridge-regularized solution whose displacement
satisfies

∥ϕ(t) − ϕ(t−1)∥ ≤

∥∇Lunsup(ϕ(t−1))∥
2γ

,

explaining the observed resistance to overreaction when regimes flip quickly.

A.7 BN-statistics refresh as shift correction without gradients

For batch normalization with running statistics (ˆµ, ˆσ) from training, the standard BN transform for a
channel is

h =

u − ˆµ
ˆσ

.

11

---

<!-- PAGE 12 -->

Refreshing statistics on the current unlabeled batch replaces (ˆµ, ˆσ) by (µB, σB), so the transform
becomes

hB =

u − µB
σB

.

When the shift is primarily first/second-order, this “zero-gradient” move cancels most of the covariate
shift at the hidden-layer level. In contrast to norm-only, which updates (γ, β) by gradient descent,
bn_stats changes the normalizing statistics directly and is much harder to overfit in short, noisy
windows. This difference matches our empirical findings: bn_stats is a safe default on financial series,
while norm-only can both help (smooth synthetic drift) and hurt (noisy real markets).

A.8 Uncertainty proxy and a do-no-harm rule

Let ∆R be the change in expected loss after adaptation. When the proxy ut (entropy or augmentation
variance) is large, empirical evidence indicates higher probability that ∆R > 0 due to unstable
pseudo-objectives. Using a quantile threshold τ estimated on validation approximates the decision
rule

P(∆R > 0 | ut) > π
for a chosen tolerance π, and the fallback policy “bn_stats instead of gradient updates” controls the
frequency of harmful steps without needing labels at test time.

A.9 Gradients for norm-only BN parameters

For a BN layer with affine parameters (γc, βc) on channel c and output yi,c for sample i, the backprop
through affine parameters is

∂L
∂γc

(cid:88)

=

gi,c hi,c,

i

∂L
∂βc

(cid:88)

=

gi,c,

i

where gi,c = ∂L/∂yi,c and hi,c is the normalized activation. The drift penalty adds

2γ(cid:0)γc − γprev

c

(cid:1),

2γ(cid:0)βc − βprev

c

(cid:1)

to each gradient term, shrinking daily motion in affine parameters. This is exactly what we implement
in Algorithm 1.

A.10 Entropy/consistency and calibration

Minimizing entropy alone can over-sharpen; pairing it with consistency prevents pathological con-
fidence by forcing agreement across benign transforms. Empirically this improves calibration: the
expected calibration error (ECE) after TTA often decreases relative to the pre-adaptation model on
the same stream, especially on SPY and QQQ where bn_stats plus conservative norm-only updates
reduce both loss and ECE.

A.11 Multi-step horizons

For H-step regression ˆy = (cid:80)H

h=1 ˆrt+h, the variance term still decomposes across transforms:

(cid:32)

(cid:88)

Var

h

(cid:33)

ˆrh,k

=

(cid:88)

h

Var(ˆrh,k) + 2

(cid:88)

Cov(ˆrh,k, ˆrh′,k),

h<h′

so minimizing augmentation variance indirectly controls covariance between stepwise predictions,
reducing compounding error typical under noisy regimes and long horizons (as in our ETTh1 H = 96
setting).

B Synthetic Shift Generators

We briefly detail the synthetic shift generators used in Stage I. In all cases, shifts are applied to
the original ETT series channel-wise, and the same random seed is used across methods for fair
comparison.

12

---

<!-- PAGE 13 -->

Gradual mean/variance drift. Let a clean series be st ∈ Rd. We add a drifted version

xt = at ⊙ st + bt,

at = 1 + κ

t
T

,

bt = µ0 + ν

t
T

,

where T is the length of the test segment, ⊙ denotes element-wise multiplication, and κ, ν are small
drift coefficients. We grid κ, ν so that the final change in mean and standard deviation is within
0.2–0.4 training standard deviations per thousand steps. This produces smooth location-scale drift
without changing higher-order structure.

Local noise inflation. Let

xt = st + ηt,

ηt ∼ N (0, σ2Id)

be the base noisy series, where σ2 is calibrated from the training set. We then select random
non-overlapping segments of length ℓ ∈ [96, 192] and set

ηt ∼ N (0, (kσ)2Id),

k ∈ {1.5, 2.0}

within those segments. This creates bursts of noise inflation while keeping the overall level of the
process similar.

Structural switches in periodic components. Write a seasonal component as

ct =

M
(cid:88)

m=1

Am cos(2πmt/P + ϕm) ,

where P is the base period and (Am, ϕm) are amplitudes and phases. At predefined change points
{tj}J
j=1, we draw new (Am, ϕm) while keeping the unconditional mean unchanged, and set

xt = ct + ϵt,

ϵt ∼ N (0, σ2Id).

We use J ∈ {2, 3} and moderate changes in (Am, ϕm) so that seasonality patterns switch visibly but
remain realistic. This is the hardest regime in our experiments: even with bn_stats, errors remain
large and R2 is strongly negative.

C Statistical Tests

We summarize the statistical tests used for forecast and backtest comparisons.

Diebold–Mariano (DM) test. Let e(A)
and e(B)
t
t. For a per-day loss ℓ(·) (cross-entropy for classification; MAE or MSE for regression), define

be forecast errors from methods A and B on day

t

dt = ℓ(e(A)

t

) − ℓ(e(B)

t

),

¯d =

1
T

T
(cid:88)

t=1

dt.

Under the null of equal predictive accuracy, E[dt] = 0. The DM statistic is

DM =

(cid:113)

¯d
(cid:100)Var( ¯d)

,

where (cid:100)Var( ¯d) is a heteroskedasticity and autocorrelation consistent (HAC) estimator of the long-run
variance of {dt} using Newey–West weights:

(cid:100)Var( ¯d) =

(cid:32)

γ0 + 2

1
T

q
(cid:88)

h=1

(cid:33)

whγh

,

wh = 1 −

h
q + 1

,

with γh the lag-h sample autocovariance of {dt} and q = ⌊4(T /100)2/9⌋ [16, 17]. Under mild
conditions, DM is asymptotically standard normal, so we report two-sided p-values. In our tables,
negative DM values mean that the first method has lower average loss than the second.

13

---

<!-- PAGE 14 -->

Newey–West (NW) for return summaries. Given daily strategy returns zt, the sample mean

has variance

ˆµ =

1
T

T
(cid:88)

t=1

zt

(cid:100)Var(ˆµ) =

(cid:32)

γ0 + 2

1
T

q
(cid:88)

h=1

(cid:33)

whγh

,

with the same Newey–West weights wh and lag q as above, and γh the lag-h autocovariance of {zt}.
The NW t-statistic for testing E[zt] = 0 is

tNW =

(cid:113)

ˆµ

,

(cid:100)Var(ˆµ)

which we report together with annualized return, annualized volatility, and Sharpe ratio for each
strategy in Tables 4 and 5.

14

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Test-Time |           | Adaptation |        | for | Non-stationary |     |              |     | Time Series: |
| --------- | --------- | ---------- | ------ | --- | -------------- | --- | ------------ | --- | ------------ |
| From      | Synthetic |            | Regime |     | Shifts         |     | to Financial |     | Markets      |
YuruiWu,QingyingDeng,WonouChung,MairuiLi
DepartmentofStatistics&OperationsResearch,UNCChapelHill
ChapelHill,NC,27599
6202 naJ 02  ]TS.nif-q[  1v37000.2062:viXra {yuruiwu,doradeng,wchung,mairuili}@email.unc.edu
Abstract
Timeseriesencounteredinpracticearerarelystationary.Whenthedatadistribution
|     | changes,aforecastingmodeltrainedonpastobservationscanloseaccuracy.  |                   |           |     |            |                             |           |     | We           |
| --- | ------------------------------------------------------------------- | ----------------- | --------- | --- | ---------- | --------------------------- | --------- | --- | ------------ |
|     | study                                                               | a small-footprint | test-time |     | adaptation | (TTA)                       | framework | for | causal time- |
|     | seriesforecastinganddirectionclassification.                        |                   |           |     |            | Thebackboneisfrozen,andonly |           |     |              |
|     | normalizationaffineparametersareupdatedusingrecentunlabeledwindows. |                   |           |     |            |                             |           |     | For          |
classificationweminimizeentropyandenforcetemporalconsistency;forregression
weminimizepredictionvarianceacrossweaktime-preservingaugmentationsand
optionallydistillfromanEMAteacher.Aquadraticdriftpenaltyandanuncertainty-
|     | triggeredfallbackkeepupdatesstable. |     |     |     | Weevaluatethisframeworkintwostages: |     |     |     |     |
| --- | ----------------------------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
syntheticregimeshiftsonETTbenchmarks,anddailyequityandFXseries(SPY,
|     | QQQ, | EUR/USD) | across | pandemic, | high-inflation, |     | and recovery |     | regimes. On |
| --- | ---- | -------- | ------ | --------- | --------------- | --- | ------------ | --- | ----------- |
syntheticgradualdrift,normalization-basedTTAimprovesforecastingerror,while
|     | in financial                                                       | markets  | a simple   | batch-normalization |     |            | statistics | update | is a robust |
| --- | ------------------------------------------------------------------ | -------- | ---------- | ------------------- | --- | ---------- | ---------- | ------ | ----------- |
|     | default                                                            | and more | aggressive | norm-only           |     | adaptation | can even   | hurt.  | Our results |
|     | providepracticalguidancefordeployingTTAonnon-stationarytimeseries. |          |            |                     |     |            |            |        | The         |
sourcecodeofthisstudyisavailableatthisGoogleDrive.
1 Introduction
Real-world time series, such as financial prices or electricity loads, evolve over time. Structural
breaks,policychanges,andmacroeconomicshockscanshiftboththelevelandthevolatilityofthe
process. DuringtheCOVID-19crisisandthesubsequenthigh-inflationperiod,marketdynamics
changedrapidly,andmodelstrainedonpre-crisisdatabecamemiscalibrated. Oncethedeployment
distributiondepartsfromthetrainingdistribution,minimizingtraininglossisnolongersufficientto
guaranteetestperformance.
Test-timeadaptation(TTA)addressesthisissuebyupdatingpartofthemodelusingunlabeledtest
inputs. Fortimeseries,apracticalTTAschememustbecausal(nofuturedata),parameterefficient,
androbusttonoisyupdates. Inthisworkwefreezethebackboneandadaptonlyasmallparameterset
atdeployment. Whendaytarrives,wecollectthemostrecentwindows,applyweaktime-preserving
augmentations, and take a few gradient steps on unsupervised objectives. For classification we
combineentropyminimizationwithtemporalconsistency;forregressionweminimizeaugmentation
varianceandoptionallydistillfromanexponential-moving-averageteacher. Wecontrolthesizeof
dailyparameterchangesandfallbacktoalightweightbatch-normalizationstatisticsupdatewhenan
uncertaintyproxyishigh.
Ourgoalisnottoproposeanewheavyarchitecture,buttounderstandwhensmall-footprintTTA
helpsorhurtsonnon-stationarysequences. Wemakethreecontributions. First,weunifyseveralTTA
choices—noadaptation,batch-normalizationstatisticsrefresh,andnorm-onlyadaptation—under
onecausalframework. Second,weevaluatethisframeworkintwostages: syntheticshiftsonETT
Preprint.Underreview.

benchmarks, and real markets (SPY, QQQ, EUR/USD) split into pandemic, high-inflation, and
recovery regimes. Third, we connect the results with econometric tools (Diebold–Mariano tests
and Newey–West adjustments) and summarize practical recommendations for deploying TTA in
streamingforecastingsystems.
2 LiteratureReview
2.1 Test-timeadaptationunderdistributionshift
TTA minimizes an unsupervised objective at inference using the current test inputs, while most
parametersarefrozen. Acentralresultisthattuningonlynormalizationaffineparameters(γ,β)by
entropyminimizationcanyieldlargegainsundercovariateshift[1].Thisworksbecausenormalization
re-centers and re-scales hidden activations to match the present input distribution, and the affine
degreesoffreedomareenoughtocorrectmanyfirst/second-momentchanges. Instreamingscenarios,
adaptationcanaccumulateerroriftheprocedureisaggressiveorifpseudo-targetsareunstable. Prior
work proposes stabilizers such as exponential-moving-average teachers and conservative update
schedules[2,3]. WefollowthislinebyusinganEMAteacherforself-distillationinregressionand
byaddingaquadraticdriftpenaltythatdiscourageslargeinter-dayparametermotion.
Refreshing batch-normalization statistics at test time (recomputing means and variances without
gradients)alreadyimprovesrobustnesstosmall-batchandcovariateshifts[4,5]. Thismotivates
our fallback: when an uncertainty proxy is high, we refresh statistics and skip gradient updates.
Recentanalysesaddexplanatorydepth;forexample,KimandLeeetal.[21]showthatTTAcan
increaselinearityinintermediatelayers,whichyieldsmorestableextrapolationonshiftedinputs. For
forecasting,test-timelearningcanbeformulatedwithvarianceandconsistencyobjectivesthatdonot
requirelabels[22]. Adaptationinnon-stationaryenvironmentscanalsobeframedasrepresentation
alignmentthatmaintainsproximitybetweencurrentandreferencefeatures[20]. Ourconsistencyand
varianceobjectives,togetherwithEMA-teacheranddriftcontrol,areconcreterealizationsofthese
ideasfortimeseries.
2.2 Normalizationandarchitecturesfornon-stationarysequences
Non-stationarityoftenmanifestsaslevel/scaledriftandtime-varyingseasonality,sonormalization
layersareaprimarytool. Reversibleinstancenormalization(RevIN)standardizeseachsequence
andthenreversesthetransformbeforeoutput;itreducestrain–testmismatchwhilepreservingthe
forecastingtarget[6]. Adaptivenormalizationlearnsgatesthatrespondtodistributionalchanges[7].
Frequency-awarenormalizationemphasizesmulti-scaleperiodicstructureandmodulatesfeatures
accordingly [8]. These methods act within the backbone. Our TTA instead acts on top of such
defenses,allowingsmallaffinecorrectionsthatfollowthedeploymentstream,sothetwoapproaches
arecomplementary. Onthearchitectureside,theNon-StationaryTransformerincorporatesevolving
statisticsdirectlyintoattentionandresidualpaths[9]. Forourhostsweadoptlightyetcompetitive
models—multi-scaleresidualTemporalConvolutionalNetworks(TCN)[10]andcompactTransform-
ers—aswellasPatchTSTandTimesNetasreferences[11,12]. Weselectsmallwidths(64–128)and
fewlayers(2–4)toensurethattest-timeupdatestouchonlythousandsofparameters,keepinglatency
negligiblewhilepreservingaccuracy.
2.3 Regime-wiseevaluationandeconometricsignificance
Statistical performance should be interpreted by regime. Markov-switching models explain how
coefficientsandvolatilitychangeacrossstates[14],andsurveyevidencesupportsregime-dependent
predictabilityinfinancialmarkets[15].Wethereforereportrollingcurvesandregime-wisesummaries.
TocompareforecastaccuracyweusetheDiebold–MarianotestwithHACvarianceestimation[16,17].
Whenweevaluatemanyvariants,standardmultiple-comparisoncorrectionsmaybeanti-conservative;
RealityCheckandSPAaddressdata-snoopingbybootstrappingthemaximumperformancestatistic
acrossmodels[18,19]. Oursignificancereportingisalignedwiththesetools.
2

3 ProblemSetup
Let{x }T ,x ∈Rdbeamultivariateseries. WeformaninputwindowX =[x ,...,x ]∈
| t t=1 | t   |     |     |     |     |     |     |     | t t−L+1 | t   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
RL×dandstudytwotasks.
1. Classification: predictthedirectionfordayt+1;lety t+1 ∈{0,1}denotedownorup,and
[0,1]2
let pˆ(X t ) ∈ be the predicted probability. We track accuracy, F1, AUC, direction
accuracy,andexpectedcalibrationerror(ECE),anddrawreliabilitydiagrams.
2. Regression: predict next-day log-return r t+1 = logp t+1 −logp t or H-day cumulative
| log-returnr |     |         | = (cid:80)H | r       | ;wereportMAE,RMSE,andR2. |     |     |     |     |     |
| ----------- | --- | ------- | ----------- | ------- | ------------------------ | --- | --- | --- | --- | --- |
|             |     | t+1:t+H |             | h=1 t+h |                          |     |     |     |     |     |
Thedeploymentstream{P }isnon-stationaryrelativetotrainingP ,withshiftsincludinglocation-
|     |     | t   |     |     |     |     |     | train |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
scaledrift,noiseinflation,andstructuralchanges. SyntheticgeneratorsinAppendixBimplement
these. FordailyequityandFXseriesweuseaunifiedsplit: train2000–2016,validation2017–2019,
test2020–2025. Allscalersarefitontrainingonly,andweavoidexogenousvariablestoprevent
leakage. ETTbenchmarksfollowtheirstandardsplits.
4 Method
Wetrainabackbonef onthetrainingsplitwithsupervisedlosses. Attesttimeweadaptasmall
θ
parametersetonunlabeledwindowsfromthecurrentstream;thebackboneisfrozen.
4.1 Backbonesandupdateableunits
We consider a multi-scale residual TCN and a compact Transformer (2–4 layers, width 64–128).
| GRU/LSTMserveasreferences. |                                    |     |     | Attesttime,wecomparethefollowingoptions: |     |     |     |     |     |     |
| -------------------------- | ---------------------------------- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| • no_tta:                  | notest-timeadaptation,frozenmodel. |     |     |                                          |     |     |     |     |     |     |
• bn_stats: refreshbatch-normalization(BN)meansandvariancesusingthecurrentbatch,no
gradients.
| • norm_only: |     | updateonlynormalizationaffineparameters(γ,β). |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
4.2 Unsupervisedobjectives
LetBbethebatchofrecentunlabeledwindows. Forclassificationweuseentropyandconsistency:
|     |     |     |      | 1   | (cid:88) (cid:16) | (cid:88) |          |     | (cid:17) |     |
| --- | --- | --- | ---- | --- | ----------------- | -------- | -------- | --- | -------- | --- |
|     |     | L   | (θ)= |     | −                 | pˆ       | (X)logpˆ | (X) | ,        | (1) |
|     |     |     | ent  |     |                   |          | c        | c   |          |     |
|B|
|     |     |     |      |     | X∈B                            | c   |     |           |     |     |
| --- | --- | --- | ---- | --- | ------------------------------ | --- | --- | --------- | --- | --- |
|     |     |     |      | 1   | (cid:88) (cid:13)              |     |     | (cid:13)2 |     |     |
|     |     | L   | (θ)= |     | (cid:13)pˆ(X)−pˆ(T(X))(cid:13) |     |     | ,         |     | (2) |
cons
|     |     |     |     | |B| |     |     |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X∈B
whereT isaweaktime-preservingtransform(Section4.4). Forregressionweusevarianceminimiza-
tionandEMA-teacherself-distillation:
1
|     |     |      |     | (cid:88) | (cid:0) | (X))}K | (cid:1) |     |     |     |
| --- | --- | ---- | --- | -------- | ------- | ------ | ------- | --- | --- | --- |
|     | L   | (θ)= |     | Var      | {yˆ(T   |        | ,       |     |     | (3) |
|     | var |      | |B| |          | k       |        | k=1     |     |     |     |
X∈B
|     |     | (θ,θ˜)= | 1    | (cid:88) (cid:13)   |     | (cid:13) 2 | θ˜←ρθ˜+(1−ρ)θ. |     |     |     |
| --- | --- | ------- | ---- | ------------------- | --- | ---------- | -------------- | --- | --- | --- |
|     | L   |         |      | (cid:13)yˆ(X)−y˜(X) |     | (cid:13)   | ,              |     |     | (4) |
|     | sd  |         | |B | |                     |     | 2          |                |     |     |     |
X∈B
Driftcontrol: wepenalizeinter-daychangeinthesmallparameterset,
|     |     |     |       |                 |     | (cid:13) (cid:13)θ(t)−θ(t−1)(cid:13) |     | 2          |     |     |
| --- | --- | --- | ----- | --------------- | --- | ------------------------------------ | --- | ---------- | --- | --- |
|     |     |     | L     | (θ(t),θ(t−1))=γ |     |                                      |     | .          |     | (5) |
|     |     |     | drift |                 |     |                                      |     | (cid:13) 2 |     |     |
Totalobjective: forclassification,
|     |     |     | L(θ)=αL |     | +βL |      | +L    | ,   |     | (6) |
| --- | --- | --- | ------- | --- | --- | ---- | ----- | --- | --- | --- |
|     |     |     |         |     | ent | cons | drift |     |     |     |
andforregression,
|     |     |     | L(θ)=αL |     | var +βL | sd  | +L drift | .   |     | (7) |
| --- | --- | --- | ------- | --- | ------- | --- | -------- | --- | --- | --- |
AppendixAprovidesderivationsandgradientsfornorm-onlyparameters,includingproximalinter-
pretationsofthedriftpenaltyandthevariance-reductionroleoftheEMAteacher.
3

4.3 Uncertainty-triggeredfallback
We compute an uncertainty proxy on B. For classification, we use mean entropy
1 (cid:80)
u t = H(pˆ(X)). For regression, we use mean augmentation variance u t =
|     |     | |B| | X   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
1 (cid:80)
Var({yˆ(T k (X))} k ). We set τ as the 80th percentile of u t on validation; 70% and 90%
|B| X
|     | areablated. | Ifu | >τ,werefreshBNstatisticsandskipgradientupdates. |     |     |     |     |
| --- | ----------- | --- | ----------------------------------------------- | --- | --- | --- | --- |
t
4.4 Causality-preservingaugmentations
Weuseweaktransformsthatkeeptimeorderandavoidleakage:amplitudescaling(1±5%),Gaussian
jitterwithstandarddeviation0.01timesthetrainingstandarddeviation,timejitterby±1stepwithin
thewindow,andtimecutoutmaskingupto5steps.
4.5 Dailytest-timeadaptationalgorithm
DefaulthyperparametersareW=64,S=5,learningrate10−4,andα=β =10−3.
=1,γ
Algorithm1:CausalTest-TimeAdaptationforDayt
Input: Frozenbackbonef θ ;updatableparametersetϕ⊂θ(norm-onlyBNaffineparameters);
WindowlengthL;contextsizeW;stepsS;learningrateη;uncertaintythresholdτ;
|     | Losstype: | classification((6))orregression((7));transforms{T |     |     |     |     | }.  |
| --- | --------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
k
|     | Output:              | Predictionyˆ |     | (orpˆ                            | )forthenextday. |     |     |
| --- | -------------------- | ------------ | --- | -------------------------------- | --------------- | --- | --- |
|     |                      |              | t+1 | t+1                              |                 |     |     |
|     | BuildunlabeledbatchB |              |     | ←{X                              | ,...,X          | }.  |     |
| 1   |                      |              |     | t−W+1                            |                 | t   |     |
| 2   | Computeuncertaintyu  |              | t   | (entropyoraugmentationvariance). |                 |     |     |
| 3   | ifu >τ               | then         |     |                                  |                 |     |     |
t
| 4   | RefreshBNrunningstatisticsonB;returnyˆ |     |     |     |     | ←f (X | ).  |
| --- | -------------------------------------- | --- | --- | --- | --- | ----- | --- |
|     |                                        |     |     |     |     | t+1 θ | t   |
| 5   | fors=1toS                              |     | do  |     |     |       |     |
ifclassificationthen
6
|     | SampleaweaktransformT;computeL |     |     |              |     | andL     | .   |
| --- | ------------------------------ | --- | --- | ------------ | --- | -------- | --- |
| 7   |                                |     |     |              |     | ent cons |     |
| 8   | L←αL                           |     | +βL | +γ∥ϕ−ϕprev∥2 |     | .        |     |
|     |                                |     | ent | cons         |     | 2        |     |
else
9
regression
10
| 11  | SampleK          | transforms{T |                   | k };computeL |     | var andoptionallyL | sd . |
| --- | ---------------- | ------------ | ----------------- | ------------ | --- | ------------------ | ---- |
|     | L←αL             |              | +βL               | +γ∥ϕ−ϕprev∥2 |     | .                  |      |
| 12  |                  | var          | sd                |              | 2   |                    |      |
|     | Updateonlyϕ←ϕ−η∇ |              |                   | L(SGD/Adam). |     |                    |      |
| 13  |                  |              |                   | ϕ            |     |                    |      |
|     | returnyˆ         | ←f           | (X )withupdatedϕ. |              |     |                    |      |
| 14  |                  | t+1          | θ t               |              |     |                    |      |
4.6 Ablationsandsensitivity
Only thousands of parameters are updated, so extra latency per test day is small on a single T4
GPU. For the hyperparameters, we sweep W ∈ {32,64,96}, S ∈ {1,3,5}, and learning rate
in {5 × 10−5,10−4,2 × 10−4}. We compare entropy-only vs. consistency-only vs. combined
for classification, and variance-only vs. variance plus EMA teacher for regression. We examine
|     | augmentationsets: |     | scalingonly;scalingplusjitter;scalingplusjitterandcutout. |     |     |     |     |
| --- | ----------------- | --- | --------------------------------------------------------- | --- | --- | --- | --- |
5 DataandShiftConstruction
StageI:ETTwithsyntheticshifts. WeuseETTh1/ETTh2(hourly)andETTm1/ETTm2(15-min).
Theseseriesincludepowertransformerloadsandtemperatureswithclearseasonality. Wegenerate
threesyntheticshifts: (i)gradualmean/variancedrift,(ii)localnoiseinflation,and(iii)structural
|     | switchesinperiodiccomponents. |     |     |     | FormaldefinitionsandgridsareinAppendixB. |     |     |
| --- | ----------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- |
4

|     |     | Figure1: | RegimediagnosticsforSPYvolatilityandreturns. |     |     |     |
| --- | --- | -------- | -------------------------------------------- | --- | --- | --- |
Stage II: equity and FX markets. We use daily SPY and QQQ index ETFs, plus EUR/USD
exchangerates. FeaturesarebuiltfromOHLCVonlyandstandardizedusingtrainingstatistics:
|        | r =log(C | )−log(C | ),  |     |     |     |
| ------ | -------- | ------- | --- | --- | --- | --- |
|        | t        | t       | t−1 |     |     |     |
| MOM(N) | =log(C   | )−log(C | ),  |     |     |     |
|        | t        | t       | t−N |     |     |     |
N
(cid:88)
| REV(N) | =−  | r , |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
|        | t   | t−i |     |     |     |     |
i=1
|     |        | (cid:0) |                 |               | (cid:1)  |     |
| --- | ------ | ------- | --------------- | ------------- | -------- | --- |
| ATR | t =EMA | max{H   | t −L t ,|H t −C | t−1 |,|L t −C | t−1 |} , |     |
1
|     | σ2       |        | ))2, σ2 | 1(log(H | ))2−(2ln2−1)(log(C | ))2.   |
| --- | -------- | ------ | ------- | ------- | ------------------ | ------ |
|     | =        | (log(H | t /L t  | =       | t /L t             | t /O t |
|     | P,t 4ln2 |        | GK,t    | 2       |                    |        |
Wesplittestingintothreeregimes: (1)pandemic(2020),(2)high-inflation(2021–2023),(3)recovery
| (2024–2025). | Figure1showsbasicregimediagnosticsforSPY. |     |     |     |     |     |
| ------------ | ----------------------------------------- | --- | --- | --- | --- | --- |
6 ExperimentalProtocol
Weevaluateourtest-timeadaptationframeworkonthreefinancialdirectionclassificationtasks(SPY,
QQQ,andEUR/USD)andonelong-horizontime-seriesforecastingtask(ETTh1). Alldatasetsare
preprocessedintofixed-lengthslidingwindowswithinputlengthL=96,andETTh1isevaluated
withforecasthorizonH =96. Dataaresplitchronologicallyintotraining,validation,andtestsetsto
ensurestrictout-of-sampleevaluation. AllmodelsuseaTemporalConvolutionalNetwork(TCN)
withthreeresidualblocks,hiddendimension64,andkernelsize3,followedbyalinearheadfor
eitherclassificationorregression.
ModelsaretrainedusingAdamWwithlearningrate10−4,batchsize512,andearlystoppingbased
on validation AUC (classification) or validation MSE (regression). At deployment, three main
modesarecompared: noadaptation(no_tta),batch-normalizationstatisticsrefresh(bn_stats),and
norm-onlyparameteradaptation(norm_only). Test-timeadaptationistriggeredusinganuncertainty
thresholdτ estimatedasthe0.8quantileofvalidationuncertainty,computedviapredictionentropy
forclassificationandvarianceofstochasticaugmentationsforregression. Whentriggered,norm-only
parametersareupdatedusingasmallnumberofunsupervisedgradientstepswithentropy/consistency
lossforclassificationorvariance/distillationlossforregression. Evaluationisperformedstrictlyon
thetestsetusingaccuracy,F1,AUC,andECEforclassification;MAE,RMSE,andR2forregression;
alongwithrollingperformance,reliabilitydiagrams,Diebold–Marianostatisticaltests,andasimple
directionaltradingbacktestwithNewey–Westadjustedstatistics.
5

Table1: RepresentativeETTh1resultsundersyntheticregimeshifts. Eachentrycorrespondstoone
representativeconfigurationinthespecifiedregime.
Method Shift MAE RMSE R2
no_tta Gradual 0.22 0.28 -0.31
norm_only Noise 0.29 0.35 -0.02
bn_stats Structural 1.26 1.62 -20.80
Figure2: RollingforecastmetricsonETTh1undergradualdrift.
7 Results
7.1 StageI:syntheticshiftsonETT
WefirststudyhowdifferentTTAchoicesbehaveundercontrolledshiftsonETTh1. Table1reports
meanabsoluteerror(MAE),rootmeansquarederror(RMSE),andR2foronerepresentativeconfigu-
rationineachsyntheticregime: gradualdrift,localnoiseinflation,andstructuralswitches. Negative
R2 valuesindicatethatthemodelperformsworsethanasimpletraining-baselinebenchmarkunder
thecorrespondingshift.
Norm-onlyadaptationismosteffectiveundergradualmean/variancedrift,whereupdatingnormaliza-
tionaffineparameterscantrackslowchangesinscaleandlevel. Underlocalnoiseinflation,variance
minimizationacrossweakaugmentationsstabilizesregressionoutputsandreducestheimpactof
noisebursts. Structuralswitchesarethehardestcase: evenwithbn_stats,errorsremainlargeandR2
isstronglynegative.
Figure2showsrollingforecastmetricsonETTh1undergradualdrift. Comparedwiththefrozen
baseline,norm-onlyTTAreduceserrorsinthelaterpartofthehorizon,wherethesyntheticdrift
accumulates. Thissupportstheviewthatnormalization-basedupdatesarewellsuitedtosmooth
low-ordermomentshifts.
7.2 StageII:equityandFXmarkets
WenextevaluatedirectionclassificationonSPY,QQQ,andEUR/USDwiththesameTTArecipe.
Table2reportscross-marketdirectionaccuracyforallthreemethods. Thebaselineaccuracyisclose
to0.5onallseries,reflectingthedifficultyofdailydirectionprediction.
Thesenumberscomefromarunfocusedondirectionalaccuracy;absolutevaluesdifferfromother
experiments,butpatternsareconsistent. Thereisnosinglewinner: differentmarketsandregimes
preferdifferentTTAvariants. OnSPY,norm_onlyachievesthebestdirectionalaccuracy,slightly
aheadofno_ttaandbn_stats. OnQQQ,bn_statsprovidesthelargestgain,whilenorm_onlycanhurt
performance. OnEUR/USD,bothTTAmethodsareroughlyonparwithorslightlybetterthanthe
frozenbaseline.
Figure 3 plots rolling direction accuracy and RMSE for SPY, QQQ, and EUR/USD with regime
shading. ForSPY,improvementsfromTTAareconcentratedinthepandemicandearlyrecovery
periods, when distributional change is strong. For QQQ, batch-normalization statistics updates
6

Table2: Directionalaccuracyontestsets(2020–2025)forequityandFXmarkets.
| Method    | SPY QQQ     | EURUSD | Avg.rank |
| --------- | ----------- | ------ | -------- |
| no_tta    | 0.504 0.503 | 0.516  | 2.33     |
| bn_stats  | 0.498 0.525 | 0.520  | 1.66     |
| norm_only | 0.512 0.463 | 0.516  | 2.00     |
Figure3: RollingmetricsforSPY,QQQ,andEUR/USDwithregimeshading.
(bn_stats)areparticularlyeffective,whilenorm_onlycanoverfitlocalnoiseanddegradeaccuracy.
ForEUR/USD,bn_statsyieldsthemoststablegains,andnorm_onlybehavessimilarlytothefrozen
baseline.
7.3 Statisticaltestsandbacktests
Toassesswhetherobserveddifferencesarestatisticallymeaningful,werunDiebold–Marianotestson
dailyforecastlosses. Table3reportsDMstatisticsandp-valuesforpairwisecomparisonsbetween
bn_stats,norm_only,andno_tta. NegativeDMvaluesindicatethatthefirstmethodoutperformsthe
secondunderourlossconvention. OnSPYandQQQ,bn_statsissignificantlybetterthanno_ttaat
the5%level,whilenorm_onlyissignificantlyworsethanno_tta. OnEUR/USD,bn_statsisalso
significantlybetterthanno_tta,andnorm_onlyisindistinguishablefromthebaseline.
7

|            | Table3: | Diebold–Marianotestscomparingforecastlosses. |        |         |     |       |
| ---------- | ------- | -------------------------------------------- | ------ | ------- | --- | ----- |
| Comparison |         | Dataset                                      | DMStat | p-value |     | Notes |
bn_statsvsno_tta SPY -2.781 0.0054 bn_statssignificantlybetter
| norm_onlyvsno_tta |     | SPY | 6.810 | 0.0000 | no_ttasignificantlybetter |     |
| ----------------- | --- | --- | ----- | ------ | ------------------------- | --- |
bn_statsvsno_tta QQQ -2.290 0.0220 bn_statssignificantlybetter
| norm_onlyvsno_tta |     | QQQ | 8.936 | 0.0000 | no_ttasignificantlybetter |     |
| ----------------- | --- | --- | ----- | ------ | ------------------------- | --- |
bn_statsvsno_tta EURUSD 4.350 0.0000 bn_statssignificantlybetter
| norm_onlyvsno_tta |                                                         | EURUSD     | -0.112 | 0.9109         | nosignificantdifference |     |
| ----------------- | ------------------------------------------------------- | ---------- | ------ | -------------- | ----------------------- | --- |
|                   | Table4: SPYbacktestperformancewithNewey–Westadjustment. |            |        |                |                         |     |
|                   | Strategy                                                | Ann.return |        | Ann.volatility | Sharpe(NWt)             |     |
|                   | No-TTA                                                  | 3.321      |        | 4.621          | 1.746                   |     |
|                   | BN-Stats                                                | 7.933      |        | 9.582          | 1.930                   |     |
|                   | Norm-Only                                               | 2.029      |        | 3.460          | 1.544                   |     |
Finally, we connect predictive accuracy with simple economic metrics. Tables 4 and 5 report
annualized return, annualized volatility, and Sharpe ratio for a basic directional strategy on SPY
andQQQ,togetherwithNewey–Westadjustedt-statistics. Onbothassets, bn_statsachievesthe
highest Sharpe ratio, while norm_only underperforms the frozen baseline. These backtests are
purelyillustrative,buttheyshowthatthestatisticalgainsfrombn_statstranslateintomoreattractive
risk-adjustedreturns,whereasnaivenorm-onlyupdatescanbeharmful.
8 DiscussionandConclusion
Normalization-basedTTAismosteffectivewhenshiftsmainlychangelow-ordermoments. Inthe
syntheticETTh1experimentswithgradualdrift,updatingnormalizationaffineparameterstracks
thechangingscaleandreducesforecasterror. Localnoiseinflationispartlyhandledbyvariance-
basedobjectives,butstructuralswitchesinperiodiccomponentsstillleadtolargeerrorsevenafter
adaptation. Thissuggeststhatnorm-onlyupdatesarewellsuitedtosmoothcovariatedrift,butthey
donotfullysolvesharporregime-changingdynamics.
Incontrast,theequityandFXseries(SPY,QQQ,EUR/USD)arenoisy,heavy-tailed,andaffectedby
jumpsandmicrostructurenoise. Hereasimplerefreshofbatch-normalizationstatisticsisasafeand
effectivedefault: bn_statsachieveshigherdirectionaccuracyandSharperatiosonSPYandQQQ,
andtheDiebold–Marianotestsshowstatisticallysignificantimprovementsoverthefrozenbaseline.
Aggressivenorm-onlyadaptation,evenwithdriftcontrol,canoverfitshortwindows,performworse
thanno_tta,andreduceeconomicperformanceinthebacktests.
Our results also highlight the importance of uncertainty control. The fallback rule, which skips
gradient-basedadaptationondayswithhighentropyorlargeaugmentationvariance,mitigatesmany
failure cases of norm-only updates and limits the frequency of harmful steps. At the same time,
thechoiceofhyperparameters(W,S,η,τ)andthestabilityofthebackboneremainimportant,and
differentassetsmayfavordifferentadaptationregimes. Syntheticshiftgeneratorsarenecessarily
stylizedandcannotcoverallrealdynamics,somorerealisticbenchmarksandstresstestsareanatural
directionforfuturework.
Overall,thisstudyprovidesanempiricalpictureofwhensmall-footprintTTAhelpsandwhenithurts
onnon-stationarytimeseries. Forpractitioners,ourmainrecommendationistostartfrombn_statsas
adefault,addnorm-onlyupdatesonlywhenvalidationanduncertaintydiagnosticssupportthem,and
alwaysevaluatewithregime-wisemetricsandrobuststatisticaltests. Wehopethesefindingswill
helpbothpractitionersandresearchersdesignsaferandmoreeffectivetest-timeadaptationpipelines
forreal-worldtimeseries.
8

|     | Table5: QQQbacktestperformancewithNewey–Westadjustment. |            |                |             |
| --- | ------------------------------------------------------- | ---------- | -------------- | ----------- |
|     | Strategy                                                | Ann.return | Ann.volatility | Sharpe(NWt) |
|     | No-TTA                                                  | 10.884     | 7.689          | 3.205       |
|     | BN-Stats                                                | 20.293     | 11.974         | 4.080       |
|     | Norm-Only                                               | 3.136      | 5.204          | 1.349       |
References
[1] D.Wang,E.Shelhamer,S.Liu,B.Olshausen,andT.Darrell. Tent:Fullytest-timeadaptationbyentropy
| minimization.                  | InICLR,2021. |                                     |     |              |
| ------------------------------ | ------------ | ----------------------------------- | --- | ------------ |
| [2] J.Wang,Y.Liu,W.Zhang,etal. |              | Continualtest-timedomainadaptation. |     | InCVPR,2022. |
[3] L.Yuan,S.Wang,etal. Robusttest-timeadaptationindynamicscenarios. InCVPR,2023.
| [4] Z.Yang,Z.Li,etal. | Test-timebatchnormalization. |     | arXiv:2205.10210,2022. |     |
| --------------------- | ---------------------------- | --- | ---------------------- | --- |
[5] S.Schneider,A.Minderer,etal. Improvingrobustnessagainstcommoncorruptionsbycovariate-shift
| adaptationattesttime. | InNeurIPS,2020. |     |     |     |
| --------------------- | --------------- | --- | --- | --- |
[6] T. Kim, H. Oh, et al. Reversible instance normalization for accurate time-series forecasting against
| distributionshift. | InICLR,2022. |     |     |     |
| ------------------ | ------------ | --- | --- | --- |
[7] W.Liu,S.Zhang,etal. Adaptivenormalizationfornon-stationarytimeseriesforecasting. InNeurIPS,
2023.
[8] J.Ye,Z.Zhang,etal. Frequency-adaptivenormalizationfornon-stationarytimeseries. InNeurIPS,2024.
[9] M.Liu,X.Zhang,etal. Non-stationarytransformers:Exploringthestationarityintimeseriesforecasting.
InNeurIPS,2022.
[10] S.Bai,J.Z.Kolter,andV.Koltun.Anempiricalevaluationofgenericconvolutionalandrecurrentnetworks
| forsequencemodeling. | arXiv:1803.01271,2018. |     |     |     |
| -------------------- | ---------------------- | --- | --- | --- |
[11] Y.Nie,N.Liu,etal. Atimeseriesisworth64words:Long-termforecastingwithtransformers. InICLR,
2023.
[12] H.Wu,J.Xu,etal. TimesNet:Temporal2D-variationmodelingforgeneraltimeseriesanalysis. InICLR,
2023.
[13] H.Zhou,S.Zhang,etal. Informer:Beyondefficienttransformerforlongsequencetime-seriesforecasting.
InAAAI,2021.
[14] J.D.Hamilton. Anewapproachtotheeconomicanalysisofnonstationarytimeseriesandthebusiness
| cycle. | Econometrica,1989. |     |     |     |
| ------ | ------------------ | --- | --- | --- |
[15] A. Ang and A. Timmermann. Regime changes and financial markets. Annual Review of Financial
Economics,2011.
[16] F.X.DieboldandR.S.Mariano. Comparingpredictiveaccuracy. JournalofBusinessandEconomic
Statistics,1995.
[17] W.K.NeweyandK.D.West. Asimple,positivesemi-definite,heteroskedasticityandautocorrelation
| consistentcovariancematrix. |                               | Econometrica,1987. |                    |     |
| --------------------------- | ----------------------------- | ------------------ | ------------------ | --- |
| [18] H.White.               | Arealitycheckfordatasnooping. |                    | Econometrica,2000. |     |
[19] P.R.Hansen. Atestforsuperiorpredictiveability. JournalofBusinessandEconomicStatistics,2005.
[20] W.Zhang,X.Li,etal. Test-timeadaptationinnon-stationaryenvironmentsviaadaptiverepresentation
| alignment. | InNeurIPS,2024. |     |     |     |
| ---------- | --------------- | --- | --- | --- |
[21] D.Kim,Y.Lee,etal. Test-timeadaptationinducesstrongeraccuracyandlinearity. InNeurIPS,2024.
[22] V.Christou,etal. Testtimelearningfortimeseriesforecasting. arXiv:2409.14012,2024.
9

A NotationandDerivations
WeexpandtheobjectivesusedinSection4,givegradientsfornorm-onlybatch-normalization(BN)
affineparameters,andexplainwhyeachtermhelpsundertypicalregimeshifts. Symbolsfollowthe
maintext.
A.1 Norm-onlyupdatesasmomentmatching
ConsideraBN-normalizedhiddenchannel
u−µ
|     |     |     | h=BN(u)= |     | , y =γh+β, |     |     |
| --- | --- | --- | -------- | --- | ---------- | --- | --- |
σ
where(µ,σ)aretheBNstatisticsfromthecurrentstreamand(γ,β)arethetrainableaffineparameters.
Underacovariateshiftwithnewmoments(µ′,σ′),thepre-affinehiddenbecomes
|     |     |     |     | u−µ′ | µ−µ′ |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- |
σ
|     |     |     | h′ = | =   | h+  | .   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     |      | σ′  | σ′  | σ′  |     |
Choosing
|     |     |     |        | σ    |       | µ−µ′ |     |
| --- | --- | --- | ------ | ---- | ----- | ---- | --- |
|     |     |     | γ′ =γ· | , β′ | =β+γ· |      |     |
|     |     |     | σ′     |      |       | σ′   |     |
exactlyrestoresyforalluiftheshiftispurelyfirst/secondmoments. Thussmallchangesof(γ,β)
cancancellocation/scaledriftatthefeaturelevel.
ForascalarlossL,thegradientssatisfy
|     |     | ∂L  |          | ∂L  | ∂L  | ∂L       |     |
| --- | --- | --- | -------- | --- | --- | -------- | --- |
|     |     |     | (cid:88) |     |     | (cid:88) |     |
|     |     |     | =        | h , | =   |          | ,   |
|     |     | ∂γ  | ∂y       | i,c | ∂β  | ∂y       |     |
|     |     |     | c        | i,c | c   |          | i,c |
|     |     |     | i        |     |     | i        |     |
wherecindexeschannelsandiindexesbatchelements. Adapting(γ,β)thereforere-centersand
re-scales along directions where the loss is sensitive. This explains why norm-only is effective
whenregimeshiftsdominantlyalterlow-ordermoments,whichisexactlythecaseinoursynthetic
gradual-driftexperiments.
A.2 Entropyminimizationanddecisionmargin
Foratwo-classsoftmaxpˆ(X)=(p,1−p),theentropyis
H(pˆ)=−plogp−(1−p)log(1−p).
Thederivativeandsecondderivativewithrespecttopare
|     |     | dH  | 1−p  | d2H | 1   | 1   |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     | =log | ,   | =   | +   | >0, |
|     |     | dp  | p    | dp2 | p   | 1−p |     |
soH isstrictlyconvexinpwithminimaatp ∈ {0,1}. Afirst-orderTaylorexpansionaroundthe
pre-update p shows that a small gradient step with learning rate η reduces H by approximately
0
(cid:0)dH(cid:1)2
η ,pushingposteriorsawayfromindecision. Undertheusualclusterorlow-densityseparation
dp
assumptions,thiscoincideswithincreasingthemarginarounddecisionboundaries,whichisbeneficial
whenP(X)driftsbutclass-conditionalstructurepersists.
A.3 ConsistencyasJacobiancontrolalongcausaldirections
LetT beaweaktime-preservingtransformwithT equaltotheidentity. ByTaylorexpansion,
| ϵ   |     |     |                   |     | 0    |         |     |
| --- | --- | --- | ----------------- | --- | ---- | ------- | --- |
|     |     |     | pˆ(T (X))≈pˆ(X)+J |     | (X)∆ | +O(ϵ2), |     |
|     |     |     | ϵ                 |     | pˆ X |         |     |
(cid:12)
| where∆ | = d T (X)   | (cid:12) andJ | istheJacobianofpˆwithrespecttoX. |             |     |            | Then        |
| ------ | ----------- | ------------- | -------------------------------- | ----------- | --- | ---------- | ----------- |
| X      | d ϵ ϵ       | ϵ=0           | pˆ                               |             |     |            |             |
|        |             |               | (X))∥2                           |             | ∥2  | =∆⊤(cid:0) | J⊤J (cid:1) |
|        | ∥pˆ(X)−pˆ(T |               | ϵ                                | ≈∥J pˆ (X)∆ | X   |            | pˆ ∆ X .    |
|        |             |               |                                  | 2           | 2   | X          | pˆ          |
Minimizing the consistency loss therefore penalizes the directional Jacobian norm along small,
causality-preservingdeformations(re-timing±1,mildamplitudechanges). Thismakespredictions
insensitivetobenignlocalperturbationsthatoftenaccompanymeasurementnoiseormicrostructure
changesundernewregimes.
10

A.4 Augmentation-varianceminimizationandlocalriskcontrol
(cid:80)K
ForregressionwithKtransforms,defineyˆ =yˆ(T (X))andy¯= 1 yˆ . Thesamplevariance
|     |     | k   | k   |     | K k=1 | k   |
| --- | --- | --- | --- | --- | ----- | --- |
K
1 (cid:88)
|     | Var({yˆ | })= |     | (yˆ −y¯)2 |     |     |
| --- | ------- | --- | --- | --------- | --- | --- |
|     |         | k   | K−1 | k         |     |     |
k=1
upper-boundstheexpectedsquareddeviationunderalocalneighborhoodN(X)ofperturbations
HenceminimizingE
whenthetransformsetcoversprincipaldirections. [Var]reducesthelocal
X
Lipschitz constant of the predictor around each X, which is desirable when the test distribution
featurestransientnoiseinflation.
| Thegradientofthevariancetermwithrespecttoeachyˆ |     |         | m       | is    |     |     |
| ----------------------------------------------- | --- | ------- | ------- | ----- | --- | --- |
|                                                 |     | ∂       | 2       |       |     |     |
|                                                 |     | Var({yˆ | })= (yˆ | −y¯), |     |     |
|                                                 |     |         | k       | m     |     |     |
|                                                 |     | ∂yˆ m   | K       |       |     |     |
sothelosspullsdisagreeingoutputstowardtheirmeanandshrinksdispersion.
A.5 EMA-teacherself-distillationastemporalensembling
Letθ˜beanexponentialmovingaverageoftheadaptedparameters:
θ˜←ρθ˜+(1−ρ)θ,
withρ∈(0,1).Underalocallyquadraticlosswithunbiasedgradientnoise,Polyakaveragingimplies
thatθ˜haslowervariancethantheinstantaneousθ.
Distillation
1 (cid:88)
|     | L   | =   | ∥yˆ (X)−yˆ | (X)∥2 |     |     |
| --- | --- | --- | ---------- | ----- | --- | --- |
|     |     | sd  | θ          | θ˜    | 2   |     |
|B|
X∈B
regularizesthestudenttowardalow-passfilteredtarget, dampingoscillationsproducedbysmall
batchesandachangingB. Asimplescalarmodelwithi.i.d.zero-meangradientnoiseshowsthat
theteacher’svarianceisscaledby 1−ρ relativetothestudent’s,solargerρyieldsasteadiertarget.
1+ρ
Thisimprovesstabilitywithoutrequiringlabelsandcomplementsthevariancetermbyanchoringtoa
temporallysmoothedpredictor.
A.6 Driftpenaltyasproximalupdate
LetϕdenotealladaptedBNaffineparameters. Ondaytwesolve
|     | min | L     | (ϕ)+γ∥ϕ−ϕ(t−1)∥2, |     |     |     |
| --- | --- | ----- | ----------------- | --- | --- | --- |
|     |     | unsup |                   |     | 2   |     |
ϕ
whereL unsup istheentropy/consistencyloss(classification)orvariance/distillationloss(regression).
Asinglegradientstepwithstepsizeηgives
|                |     | (cid:16) |                            |     |     | (cid:17) |
| -------------- | --- | -------- | -------------------------- | --- | --- | -------- |
| ϕ(t) =ϕ(t−1)−η |     | ∇L       | (ϕ(t−1))+2γ(ϕ(t−1)−ϕ(t−2)) |     |     | ,        |
unsup
whichisequivalenttoSGDwithaquadraticproximaltermthatshrinksmotiontowardtheprevious
day.Inalocallyquadraticloss,theexactminimizerisaridge-regularizedsolutionwhosedisplacement
satisfies
(ϕ(t−1))∥
∥∇L unsup
|     | ∥ϕ(t)−ϕ(t−1)∥ |     | ≤   |     | ,   |     |
| --- | ------------- | --- | --- | --- | --- | --- |
2γ
explainingtheobservedresistancetooverreactionwhenregimesflipquickly.
A.7 BN-statisticsrefreshasshiftcorrectionwithoutgradients
Forbatchnormalizationwithrunningstatistics(µˆ,σˆ)fromtraining,thestandardBNtransformfora
channelis
u−µˆ
|     |     |     | h= . |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- |
σˆ
11

Refreshingstatisticsonthecurrentunlabeledbatchreplaces(µˆ,σˆ)by(µ ,σ ),sothetransform
B B
becomes
u−µ
B.
|     |     |     |     | h   | B = |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
σ
B
Whentheshiftisprimarilyfirst/second-order,this“zero-gradient”movecancelsmostofthecovariate
shiftatthehidden-layerlevel. Incontrasttonorm-only,whichupdates(γ,β)bygradientdescent,
bn_stats changes the normalizing statistics directly and is much harder to overfit in short, noisy
windows. Thisdifferencematchesourempiricalfindings:bn_statsisasafedefaultonfinancialseries,
whilenorm-onlycanbothhelp(smoothsyntheticdrift)andhurt(noisyrealmarkets).
A.8 Uncertaintyproxyandado-no-harmrule
Let∆Rbethechangeinexpectedlossafteradaptation. Whentheproxyu (entropyoraugmentation
t
variance) is large, empirical evidence indicates higher probability that ∆R > 0 due to unstable
pseudo-objectives. Usingaquantilethresholdτ estimatedonvalidationapproximatesthedecision
rule
|     |     |     |     | P(∆R>0|u |     | )>π |     |
| --- | --- | --- | --- | -------- | --- | --- | --- |
t
forachosentoleranceπ,andthefallbackpolicy“bn_statsinsteadofgradientupdates”controlsthe
frequencyofharmfulstepswithoutneedinglabelsattesttime.
A.9 Gradientsfornorm-onlyBNparameters
ForaBNlayerwithaffineparameters(γ ,β )onchannelcandoutputy forsamplei,thebackprop
|     |     |     |     | c c |     |     | i,c |
| --- | --- | --- | --- | --- | --- | --- | --- |
throughaffineparametersis
|               |     |      | ∂L                         |               |         | ∂L                    |          |
| ------------- | --- | ---- | -------------------------- | ------------- | ------- | --------------------- | -------- |
|               |     |      |                            | (cid:88)      |         |                       | (cid:88) |
|               |     |      | =                          | g i,c         | h i,c , | =                     | g i,c ,  |
|               |     |      | ∂γ                         |               |         | ∂β                    |          |
|               |     |      | c                          |               |         | c                     |          |
|               |     |      |                            | i             |         |                       | i        |
| whereg =∂L/∂y |     | andh | isthenormalizedactivation. |               |         | Thedriftpenaltyadds   |          |
| i,c           | i,c |      | i,c                        |               |         |                       |          |
|               |     |      | (cid:0)                    | −γprev(cid:1) |         | (cid:0) −βprev(cid:1) |          |
|               |     |      | 2γ γ                       |               | ,       | 2γ β                  |          |
|               |     |      |                            | c c           |         | c                     | c        |
toeachgradientterm,shrinkingdailymotioninaffineparameters. Thisisexactlywhatweimplement
inAlgorithm1.
A.10 Entropy/consistencyandcalibration
Minimizingentropyalonecanover-sharpen;pairingitwithconsistencypreventspathologicalcon-
fidencebyforcingagreementacrossbenigntransforms. Empiricallythisimprovescalibration: the
expectedcalibrationerror(ECE)afterTTAoftendecreasesrelativetothepre-adaptationmodelon
thesamestream,especiallyonSPYandQQQwherebn_statsplusconservativenorm-onlyupdates
reducebothlossandECE.
A.11 Multi-stephorizons
ForH-stepregressionyˆ= (cid:80)H rˆ ,thevariancetermstilldecomposesacrosstransforms:
|     |     |          | h=1 t+h  |          |        |          |               |
| --- | --- | -------- | -------- | -------- | ------ | -------- | ------------- |
|     |     | (cid:32) | (cid:33) |          |        |          |               |
|     |     | (cid:88) |          | (cid:88) |        | (cid:88) |               |
|     | Var |          | rˆ       | =        | Var(rˆ | )+2      | Cov(rˆ ,rˆ ), |
|     |     |          | h,k      |          | h,k    |          | h,k h′,k      |
|     |     | h        |          | h        |        | h<h′     |               |
sominimizingaugmentationvarianceindirectlycontrolscovariancebetweenstepwisepredictions,
reducingcompoundingerrortypicalundernoisyregimesandlonghorizons(asinourETTh1H =96
setting).
B SyntheticShiftGenerators
We briefly detail the synthetic shift generators used in Stage I. In all cases, shifts are applied to
the original ETT series channel-wise, and the same random seed is used across methods for fair
comparison.
12

Gradualmean/variancedrift. Letacleanseriesbes ∈Rd. Weaddadriftedversion
t
t t
x =a ⊙s +b , a =1+κ , b =µ +ν ,
t t t t t T t 0 T
whereT isthelengthofthetestsegment,⊙denoteselement-wisemultiplication,andκ,ν aresmall
drift coefficients. We grid κ,ν so that the final change in mean and standard deviation is within
0.2–0.4trainingstandarddeviationsperthousandsteps. Thisproducessmoothlocation-scaledrift
withoutchanginghigher-orderstructure.
Localnoiseinflation. Let
x =s +η , η ∼N(0,σ2I )
t t t t d
be the base noisy series, where σ2 is calibrated from the training set. We then select random
non-overlappingsegmentsoflengthℓ∈[96,192]andset
η ∼N(0,(kσ)2I ), k ∈{1.5,2.0}
t d
withinthosesegments. Thiscreatesburstsofnoiseinflationwhilekeepingtheoveralllevelofthe
processsimilar.
Structuralswitchesinperiodiccomponents. Writeaseasonalcomponentas
M
(cid:88)
c = A cos(2πmt/P +ϕ ),
t m m
m=1
whereP isthebaseperiodand(A ,ϕ )areamplitudesandphases. Atpredefinedchangepoints
m m
{t }J ,wedrawnew(A ,ϕ )whilekeepingtheunconditionalmeanunchanged,andset
j j=1 m m
x =c +ϵ , ϵ ∼N(0,σ2I ).
t t t t d
WeuseJ ∈{2,3}andmoderatechangesin(A ,ϕ )sothatseasonalitypatternsswitchvisiblybut
m m
remainrealistic. Thisisthehardestregimeinourexperiments: evenwithbn_stats,errorsremain
largeandR2isstronglynegative.
C StatisticalTests
Wesummarizethestatisticaltestsusedforforecastandbacktestcomparisons.
Diebold–Mariano(DM)test. Lete(A)ande(B)beforecasterrorsfrommethodsAandBonday
t t
t. Foraper-daylossℓ(·)(cross-entropyforclassification;MAEorMSEforregression),define
T
d =ℓ(e(A))−ℓ(e(B)), d¯= 1 (cid:88) d .
t t t T t
t=1
Underthenullofequalpredictiveaccuracy,E[d ]=0. TheDMstatisticis
t
d¯
DM= ,
(cid:113)
V(cid:100)ar(d¯)
whereV(cid:100)ar(d¯)isaheteroskedasticityandautocorrelationconsistent(HAC)estimatorofthelong-run
varianceof{d }usingNewey–Westweights:
t
(cid:32) q (cid:33)
V(cid:100)ar(d¯)=
T
1 γ
0
+2 (cid:88) w
h
γ
h
, w
h
=1−
q+
h
1
,
h=1
with γ the lag-h sample autocovariance of {d } and q = ⌊4(T/100)2/9⌋ [16, 17]. Under mild
h t
conditions,DMisasymptoticallystandardnormal,sowereporttwo-sidedp-values. Inourtables,
negativeDMvaluesmeanthatthefirstmethodhasloweraveragelossthanthesecond.
13

Newey–West(NW)forreturnsummaries. Givendailystrategyreturnsz ,thesamplemean
t
T
1 (cid:88)
µˆ = z
T t
t=1
hasvariance
(cid:32) q (cid:33)
1 (cid:88)
V(cid:100)ar(µˆ)=
T
γ
0
+2 w
h
γ
h
,
h=1
withthesameNewey–Westweightsw andlagqasabove,andγ thelag-hautocovarianceof{z }.
h h t
TheNWt-statisticfortestingE[z ]=0is
t
µˆ
t = ,
NW (cid:113)
V(cid:100)ar(µˆ)
whichwereporttogetherwithannualizedreturn, annualizedvolatility, andSharperatioforeach
strategyinTables4and5.
14