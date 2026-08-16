---
conversion_metadata:
  converted_at: "2026-07-22T12:42:19Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cau & Spano.pdf"
  source_pdf_sha256: "50c6966d0c93b1131dfd61c91a7732dfc3bd7f8a34d9e914f9c4efe64c0afa10"
  page_count: 43
  markdown_char_count: 277758
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

User Modeling and User-Adapted Interaction (2026) 36:3
https://doi.org/10.1007/s11257-025-09438-0

Exploring the impact of explainable AI and cognitive
capabilities on users’ decisions

Federico Maria Cau1 · Lucio Davide Spano1

Received: 16 December 2024 / Accepted in revised form: 12 November 2025 / Published online: 6 December 2025
© The Author(s) 2025

Abstract
Artiﬁcial Intelligence (AI) systems are increasingly used for decision-making across
domains, raising debates over the information and explanations they should provide.
Most research on Explainable AI (XAI) has focused on feature-based explanations,
with less attention on alternative styles. Personality traits like the Need for Cognition
(NFC) can also lead to different decision-making outcomes among low and high NFC
individuals. We investigated how presenting AI information (prediction, conﬁdence,
and accuracy) and different explanation styles (example-based, feature-based, rule-
based, and counterfactual) affect accuracy, reliance on AI, and cognitive load in a loan
application scenario. We also examined low and high NFC individuals’ differences in
prioritizing XAI interface elements (loan attributes, AI information, and explanations),
accuracy, and cognitive load. Our ﬁndings show that high AI conﬁdence signiﬁcantly
increases reliance on AI while reducing cognitive load. Feature-based explanations did
not enhance accuracy compared to other conditions. Although counterfactual explana-
tions were less understandable, they enhanced overall accuracy, increasing reliance on
AI and reducing cognitive load when AI predictions were correct. Both low and high
NFC individuals prioritized explanations after loan attributes, leaving AI information
as the least important. However, we found no signiﬁcant differences between low and
high NFC groups in accuracy or cognitive load, raising questions about the role of this
speciﬁc personality trait in AI-assisted decision-making. These ﬁndings underscore
the importance of user-centric personalization in XAI interfaces, where explanation
styles are tailored to users’ personality traits, cognitive characteristics, and task con-
text, with support adapted to each individual to optimize human–AI collaboration.

Keywords Loan approval prediction · AI-assisted decisions · Explainable AI ·
Reliance · Accuracy · Need for cognition
Federico Maria and Lucio Davide Spano are equally contributed to this work.
B Federico Maria Cau

federicom.cau@unica.it

Lucio Davide Spano
davide.spano@unica.it

1 Department of Mathematics and Computer Science, University of Cagliari, Via Ospedale 72, 09124

Cagliari, Sardegna, Italy

123

---

<!-- PAGE 2 -->

3

Page 2 of 43

1 Introduction

F. M. Cau, L. D. Spano

Artiﬁcial Intelligence (AI) systems are becoming increasingly prevalent to assist
human decision-makers across various domains, ranging from low-stakes activities
like automating routine processes (Herzog and Wörndl 2019; Zehrung et al. 2021;
Musto et al. 2021; Liao et al. 2022; Viswanathan et al. 2022; Grace et al. 2022) to
high-stakes scenarios like healthcare diagnostics (Cai et al. 2019b; Lee et al. 2020,
2021; Beede et al. 2020; Fogliato et al. 2022a; Panigutti et al. 2022). AI-assisted
decision approaches pose numerous challenges within the HCI community, princi-
pally focusing on the problems of increasing users’ decision-making accuracy1 and
appropriate reliance on AI systems recommendations, i.e., accepting correct AI sug-
gestions and rejecting wrong ones (Zhang et al. 2020; Rechkemmer and Yin 2022;
Bove et al. 2022; Scharowski et al. 2023; Kahr et al. 2023; Vasconcelos et al. 2023;
Chen et al. 2023). In particular, previous research on human–AI teams mainly focused
on investigating the following elements: task characteristics (e.g., complexity, stakes,
and uncertainty) (Buçinca et al. 2020; Cau et al. 2023b; Salimzadeh et al. 2023,
2024), users’ traits (e.g., Need for Cognition, task familiarity, and AI literacy) (Gajos
and Chauncey 2017; Buçinca et al. 2021; Gajos and Mamykina 2022; Ford and Keane
2023; Celar and Byrne 2023; He et al. 2023a; Foroudi et al. 2025; Yurrita et al. 2025),
different types of information about AI assistance (e.g., prediction, conﬁdence, and
accuracy) (Yin et al. 2019; Lai and Tan 2019; Zhang et al. 2020; Rechkemmer and
Yin 2022; Kahr et al. 2023; He et al. 2023a; Cau and Spano 2025), and explanation
techniques to interpret AI decisions (e.g., example-based, feature-based, and coun-
terfactuals) (Lai and Tan 2019; Buçinca et al. 2020; Wang and Yin 2022; Bove et al.
2022; Chen et al. 2023; Teso et al. 2023). Despite these efforts, current research on
AI-assisted decision-making exhibits diverging results on how and when AI assistance
is delivered and which explanation styles could better help users assess the provided
information.

For example, presenting speciﬁc AI information (i.e., prediction, conﬁdence, and
accuracy) strongly inﬂuences users’ decision-making processes. While displaying
predicted labels increases users’ accuracy in the task compared to showing no AI
assistance (Lai and Tan 2019; Buçinca et al. 2020), a high AI conﬁdence (indicating
the correctness likelihood in its prediction), appears to encourage participants to rely
on AI decisions more than a low one (Zhang et al. 2020; Rechkemmer and Yin 2022;
Cau et al. 2023a, b). Similarly, users tend to agree with predictions of AI with a high
stated accuracy2 more often than those of models with a low stated accuracy (Yin et al.
2019; Rechkemmer and Yin 2022; Kahr et al. 2023; He et al. 2023a; Kahr et al. 2024).
Furthermore, studies on human–AI decision-making rarely evaluate users’ cognitive
load during task performance and thus overlook the extent of cognitive resources being
utilized (Steyvers and Kumar 2024). The combined presentation of these AI informa-
tion pieces and their inﬂuence on users’ decision outcomes and perceptions is still
understudied.

1 Throughout the paper, we will use the term users’ “accuracy” to identify their “decision-making accuracy”.
2 AI stated accuracy refers to the accuracy reported for the model when evaluated on unseen data, usually
the test or held-out set.

123

---

<!-- PAGE 3 -->

Exploring the impact of explainable AI and cognitive…

Page 3 of 43

3

Another crucial aspect of the decision-making process involves eXplainable AI
(XAI) techniques, whose potential to enhance user accuracy and appropriate reliance
on AI is currently under debate. In our work, we focus on objective tasks (e.g., whether a
person will repay a loan), where a ground truth exists and the goal is to evaluate, under-
stand, and/or improve human performance and experience for a decision-making task
(Lai et al. 2023a). In these types of tasks, most empirical studies on AI decision support
have focused on feature-based explanations (Lai et al. 2023a), and evidence remains
inconclusive regarding their effectiveness in improving user accuracy or reducing
overreliance (Zhang et al. 2020; Wang and Yin 2021; Ma et al. 2023; Cau et al. 2023b;
Chen et al. 2023). Additionally, while prior works have compared the effects of feature-
based and example-based explanations on users (Lai and Tan 2019; Cai et al. 2019a;
Bove et al. 2022; Ford and Keane 2023; Chen et al. 2023; Lai et al. 2023b), the bene-
ﬁts and limitations of other explanation styles, such as rule-based and counterfactual
explanations, remain largely underexplored (Wang and Yin 2022; Bodria et al. 2023;
Teso et al. 2023; Cau et al. 2023b, a).

Furthermore, prior work has highlighted that individual differences can also inﬂu-
ence people’s decision-making. Recent studies in music recommendation (Millecamp
et al. 2019, 2020), AI-assisted nutrition decisions (Buçinca et al. 2021; Gajos and
Mamykina 2022), and intelligent tutoring systems (Conati et al. 2021; Bahel et al.
2024) have explored the inﬂuence of user-centric attributes like Need for Cognition
(NFC) (Cacioppo et al 1984) in user-AI teams. NFC is a personality trait that reﬂects
an individual’s tendency to engage in and enjoy effortful cognitive activities (Carenini
2001; Cazan and Indreica 2014; Gajos and Chauncey 2017). This research highlights
signiﬁcant differences in how low and high NFC individuals interact with AI, espe-
cially considering decision-making behavior, users’ accuracy, reliance on AI, and
cognitive load. While these studies provide some insights on speciﬁc domains, it is
unclear how people with different NFC levels prioritize certain information in the XAI
interface and how detailed AI information and multiple explanation styles affect their
decisions.

Considering this, this paper investigates how including different AI information
and explanations (i.e., prediction, conﬁdence, accuracy, and explanation styles such as
example-based, feature-based, rule-based, and counterfactual) impact users’ decision-
making process in a set of loan approval tasks considering their accuracy, reliance on
AI, and cognitive load. Speciﬁcally, given the recent interest in studying the Need
for Cognition (NFC) personality trait in human–AI teams, we aim to examine how
different types of AI information and explanation styles affect low and high NFC users
in terms of (i) how they prioritize the information in the XAI interface when making
a decision, (ii) the accuracy of the ﬁnal decision, and (iii) the required cognitive load.
Our research questions to address these gaps are the following:

RQ1 How do AI information and explanations impact users’ accuracy, reliance on AI,

and cognitive load?

RQ2 Is there any difference in how people with low and high levels of Need for Cognition

prioritize the information supplied in the XAI interface?

RQ3 Do people with low and high levels of Need for Cognition have different accuracy

and cognitive load when engaging with explanations?

123

---

<!-- PAGE 4 -->

3

Page 4 of 43

F. M. Cau, L. D. Spano

To answer these questions, we conducted an online user study (N = 288) where
participants interacted with an AI-assisted loan approval interface, deciding whether to
accept or reject eight loan requests based on varying AI assistance (i.e., no AI, AI with
no explanation, AI with example-based, feature-based, rule-based, and counterfactual
explanations). We analyzed their accuracy, reliance on AI, cognitive load, and the
importance of the XAI interface elements (i.e., loan attributes, AI information, and
explanation) that led them to the ﬁnal decision, further differentiating the results by
low and high levels of Need for Cognition.

In summary, the contributions of this paper are:

1. We found that a high AI conﬁdence signiﬁcantly increases users’ reliance on AI
decisions while reducing cognitive load. These ﬁndings highlight the importance of
calibrating AI conﬁdence estimates to reﬂect the likelihood of system correctness.
Additionally, integrating users’ conﬁdence calibration before AI interactions could
enable new personalized AI-assisted strategies tailored to individual conﬁdence
levels.

2. Contrary to expectations, feature-based explanations did not improve users’ accu-
racy compared to other AI-assisted conditions. However, despite being perceived
as less understandable by users, counterfactual explanations enhanced reliance on
AI and reduced cognitive load, particularly when the AI predictions were correct,
potentially improving overall accuracy. These ﬁndings suggest combining mul-
tiple explanation styles to complement each other’s strengths and mitigate their
shortcomings, ultimately leading to the development of hybrid XAI visualizations.
3. We show that different levels (low and high) of the Need for Cognition (NFC)
might not capture differences in people’s accuracy, cognitive load, and XAI inter-
face element prioritization. While prior studies in less complex domains have often
demonstrated differences in NFC levels, our results suggest that such distinctions
may diminish as task complexity increases. These ﬁndings suggest that NFC dif-
ferences may not consistently generalize across diverse domains and tasks. Future
studies should explore a broader range of personality traits and consider moving
beyond personality-based factors to focus on other user-centric characteristics.

Our paper is organized as follows. We ﬁrst review prior work on the inﬂuence of AI
information, explainable AI (XAI) effectiveness, and the role of Need for Cognition
(NFC) in AI-assisted decision-making (Sect. 2). We then outline our hypotheses, fur-
ther detailing the task design, including data, model, instances, and the AI assistance
with explanations in Sect. 3. We describe our study design, focusing on variables, sam-
ple size, statistical analysis, and the participants’ procedure in Sect. 4. We present the
results in Sect. 5, beginning with descriptive statistics and hypothesis tests. This is fol-
lowed by post hoc and exploratory analyses, covering task-speciﬁc metrics, interface
understandability, and qualitative feedback. Next, we discuss the broader implications
of our ﬁndings, highlighting study limitations and proposing directions for future
research in Sect. 6. We conclude with key contributions and insights for improving
XAI systems in Sect. 7. The study pipeline of data processing, model training, expla-
nation generation, and statistical analysis is openly available at https://osf.io/j64x8/?
view_only=7f546294a08843acbf204521ba7dee7e.

123

---

<!-- PAGE 5 -->

Exploring the impact of explainable AI and cognitive…

Page 5 of 43

3

2 Related work

In this section, we provide an overview of previous work on the effectiveness of AI
information and current explainable AI methodologies in relation to users, considering
the most common metrics for evaluating XAI systems and highlighting understudied
topics. Then, we summarize previous studies on disaggregating low and high Need
for Cognition participants in AI-assisted decision-making, focusing on the gaps in the
current literature.

2.1 Influence of AI information on decision support

Previous studies have shown that providing speciﬁc information about the AI assis-
tant during decision-making (i.e., prediction, conﬁdence score, and test set accuracy)
strongly inﬂuences users’ behaviors and task outcomes. For example, Lai and Tan
(2019) illustrated that showing AI predicted labels signiﬁcantly improves human per-
formance in a deception detection task. They found that, when predicted labels were
presented, providing feature-based explanations for the AI’s predictions resulted in
human decision accuracy comparable to that obtained when participants were explic-
itly informed of the AI’s strong performance. Similarly, Buçinca et al. (2020) found
that participants who received AI predictions (with or without explanations) provided
more accurate answers than those who did not receive any AI assistance in a nutrition-
related decision-making task.

Another valuable piece of information provided by the AI is the conﬁdence score,
which refers to provided estimates about the correctness of its outcomes in various
formats, such as numerical conﬁdence scores or ranges (Cao et al. 2024a; Bhattacharya
et al. 2024a; Cau and Spano 2025), or textual/graphical representations (Padilla et al.
2021; Prabhudesai et al. 2023; Zhao et al. 2024; Marusich et al. 2024). In this paper,
we speciﬁcally focus on a binary classiﬁcation task, where we present AI outputs’
probabilities as numerical conﬁdence estimates in percentage. For example, Zhang
et al. (2020) explored the effects of AI conﬁdence on accuracy and agreement with AI
in an income prediction task, ﬁnding that people were more likely to follow the AI’s
predictions when the AI had higher conﬁdence. Nevertheless, they found no evidence
that AI conﬁdence scores improve the accuracy of AI-assisted predictions. Another
study from Rechkemmer and Yin (2022) studied the effects of AI conﬁdence, AI stated
accuracy, and their interaction on users’ propensity to rely on the AI’s advice in a speed
dating event task. The results showed that the effect of AI conﬁdence on following its
predictions depends on people’s belief in the presented AI’s stated accuracy: the higher
the AI conﬁdence, the more accurate people perceive the model to be. The authors
argue that a possible reason for these results may lie in the users’ perception of the AI
information, considering AI accuracy as a fact and AI conﬁdence as an estimate (i.e.,
less trustworthy than AI performance). Additionally, Cau et al. (2023a, b) found that
low and high levels of AI conﬁdence in predictions signiﬁcantly affect users’ accuracy
and agreement on AI, also inﬂuencing the effectiveness of different explanation styles
considering different domains and stakes scenarios.

123

---

<!-- PAGE 6 -->

3

Page 6 of 43

F. M. Cau, L. D. Spano

As per AI accuracy effects on users, we speciﬁcally focus on AI test set accuracy
(e.g., accuracy in the held-out data, also called “stated accuracy”). As such, Yin et al.
(2019) explored how AI stated accuracy affected people’s agreement with the AI
in a speed dating task. The results show that high stated AI accuracy on held-out
data increases people’s reliance on AI. Furthermore, reliance is affected by both AI’s
stated accuracy and its observed accuracy (i.e., actual AI accuracy on the observed
instances) during the task, and the effect of stated accuracy can change depending
on the observed accuracy. Rechkemmer and Yin (2022) also found that AI’s stated
accuracy signiﬁcantly increases people’s agreement with the AI and switch fraction
(i.e., users’ change opinion after seeing the AI prediction) in a second date prediction
task. People rely on the AI model predictions more when its stated accuracy is higher.
Additionally, the impact of the AI’s conﬁdence on people’s belief in its predictions
changes based on the AI’s reported accuracy levels. Similarly, prior works by Kahr
et al. (2023, 2024) also found that people’s reliance on AI is higher when presented
with high-accuracy AI, where users are asked to estimate jail time for 20 legal cases. In
contrast, He et al. (2023a) found no signiﬁcant effects of AI stated accuracy impacting
users’ reliance on the AI (expressed as agreement on AI and switch fraction) in a loan
prediction task.

On top of this, how AI assistance is presented also strongly shapes human–AI
decision-making. Although multiple interaction patterns exist (Gomez et al. 2025),
we focus on the two most common Human-Centered AI paradigms: one stage and two
stage. The one-stage AI paradigm delivers AI assistance immediately to the human
decision-maker (Buçinca et al. 2021; Rastogi et al. 2022; Cau et al. 2023a, b; Lu et al.
2024; Swaroop et al. 2025). While this paradigm can speed decisions and reduce cog-
nitive load, it can also create an anchoring effect in which the AI’s output becomes a
salient reference point that shapes the users’ judgment (Nourani et al. 2021; Fogliato
et al. 2022b; Ma et al. 2023; Boonprakong et al. 2025). Instead, in the two-stage AI
paradigm, the user ﬁrst gives an initial answer and then receives the AI’s advice to
revise that judgment. HCI research introduced this paradigm as a cognitive forcing
function (i.e., a cognitive intervention to enhance users’ engagement with AI assis-
tance) to promote more deliberate, critical thinking, and offer potential improvements
in accuracy and appropriate reliance on AI (Buçinca et al. 2021; He et al. 2023a, b; Sal-
imzadeh et al. 2024; Agudo et al. 2024; Morrison et al. 2024; Cao et al. 2024b; Küper
et al. 2025). However, several studies warn that performance gains may instead reﬂect
greater alignment with AI outputs, including alignment with incorrect advice, rather
than genuine improvements in user critical thinking (Lu et al. 2024; Ma et al. 2024;
Cao et al. 2024b). In our study, we speciﬁcally focus on the one-stage AI paradigm, as
our goal is to assess the effectiveness of explanations without using cognitive forcing
approaches. We also test whether this introduces differences in the interpretation of
people with different propensities for enjoying effortful thinking (see Sect. 2.3 for the
Need for Cognition trait).

To summarize, prior research consistently highlights that AI conﬁdence and accu-
racy combinations affect users’ reliance on AI during decision-making. We believe
that when users are exposed to relatively high stated accuracy, the AI conﬁdence acts
as the tiebreaker in following the AI prediction: higher conﬁdence increases the like-
lihood of users following the AI’s suggestion. Thus, this study explores the impact of

123

---

<!-- PAGE 7 -->

Exploring the impact of explainable AI and cognitive…

Page 7 of 43

3

AI information on user reliance on AI (i.e., agreement with AI decisions), particularly
focusing on different levels of AI conﬁdence. Furthermore, since users’ cognitive load
based on AI assistance is still underexplored in studies of AI-assisted decision-making
(Steyvers and Kumar 2024), we argue that low AI conﬁdence may elicit a higher cog-
nitive load in users than high conﬁdence, forcing them to reason independently rather
than blindly following the AI’s prediction.

2.2 Explainable AI effectiveness in AI-assisted decisions

With the rise of complex black-box AI models, eXplainable AI techniques have
emerged to help users understand how the AI reached a speciﬁc decision in low-
and high-stakes situations, including high-uncertainty and safety-critical contexts
(Bertrand et al. 2022; Lai et al. 2023a; Rong et al. 2024; Subramanian et al. 2024). Pre-
vious studies have shown that explanations may lead to increased user accuracy (Lai
and Tan 2019; Buçinca et al. 2020; Bansal et al. 2021; Herm 2023) and appropriate
reliance on AI (Wang and Yin 2022; Scharowski et al. 2023; Chen et al. 2023) when
compared to AI prediction alone or not showing any assistance. Nevertheless, several
studies on AI-assisted decisions explored explanation style differences in increasing
users’ accuracy and appropriate reliance, reporting contrasting results. Most of these
studies focused on example-based and feature-based explanations (Binns et al. 2018;
Lai and Tan 2019; Cai et al. 2019a; Zhang et al. 2020; Bove et al. 2022; Ford and Keane
2023; Chen et al. 2023; Lai et al. 2023b), with a limited number of studies also assess-
ing the effects of rule-based and counterfactual explanations (Gajos and Mamykina
2022; Wang and Yin 2022; Teso et al. 2023; Celar and Byrne 2023; Xuan et al. 2025).
For example, Wang and Yin (2022) studied the effects of different explanations (i.e.,
feature importance, feature contribution, nearest neighbors, and counterfactuals) in a
recidivism prediction task and found that when users have some domain expertise in
the decision-making task, feature contribution can satisfy more desiderata of the AI
model and explanations (i.e., understanding, uncertainty awareness, and trust calibra-
tion) regardless of the complexity of the AI model. Another study (Chen et al. 2023)
found that, for an income prediction task, example-based explanations improved par-
ticipants’ task accuracy when compared with no AI assistance, but only when the AI’s
predictions were correct. Instead, when the AI provided wrong predictions, the authors
found a trend of feature-based explanations increasing overreliance. Furthermore, Cau
et al. (2023b) investigated the effects on AI conﬁdence and logic-style explanations in
a stock trading market task, discovering that when AI conﬁdence is high, users tend to
over-rely on an erroneous AI more with inductive (example-based) explanations than
abductive (feature-based) and deductive (rule-based) explanations.

Given that most of the existing XAI literature has focused on feature-based expla-
nations (Lai et al. 2023a), and there is insufﬁcient evidence regarding their impact on
users’ accuracy, particularly with tabular data (Zhang et al. 2020; Wang and Yin 2021;
Chen et al. 2023; Ma et al. 2023; Cau et al. 2023b; Cau and Spano 2025), we aim to
investigate whether feature-based explanations improve users’ accuracy compared to

123

---

<!-- PAGE 8 -->

3

Page 8 of 43

F. M. Cau, L. D. Spano

other types of AI assistance (i.e., no AI; AI without explanations; AI + example-based
explanations; AI + rule-based explanations; and AI + counterfactual explanations).3

2.3 Need for cognition in human–AI decisions

In this work, we focus speciﬁcally on the Need for Cognition (NFC) trait (Cacioppo
et al 1984), given previous studies suggest that individual differences in NFC can affect
people’s interactions with AI assistance and explanations (Millecamp et al. 2019;
Buçinca et al. 2021; Gajos and Mamykina 2022; Bahel et al. 2024). NFC is a measure
that reﬂects the tendency for an individual to undertake effortful cognitive activities
(Gajos and Chauncey 2017; Buçinca et al. 2021) and beneﬁt more from complex user
interface features (Carenini 2001; Cazan and Indreica 2014; Gajos and Chauncey 2017;
Ghai et al. 2021; Gajos and Mamykina 2022). Previous work has shown that people
with higher NFC are more likely to be curious and in a focused, attentive state while
using a computer (Li and Browne 2006) and have higher performance at complex skill
acquisition in the context of computer task performance (Day et al. 2007).

Considering explanations in music recommendations (i.e., assisted creation of a
playlist), Millecamp et al. (2019) found that explanations raised the conﬁdence of
users with a low NFC when making their playlist. In contrast, users with a high NFC
experienced a decrease in their conﬁdence due to explanations. On the contrary, a
follow-up study from Millecamp et al. (2020) did not ﬁnd an effect of NFC on the
perception of explanations. The authors stated that a potential reason for this result
might lie in the explanations’ presentation and the proactive activation of explanations,
which brings out the differences between low and high NFC users. While in the
previous study (Millecamp et al. 2019) explanations had to be explicitly activated by
the users, in Millecamp et al. (2020) explanations were always visible.

Concerning NFC effects in the nutrition domain, Buçinca et al. (2021) studied
the impact of cognitive forcing functions (i.e., interventions that disrupt heuristic
reasoning and cause the person to engage in analytical thinking)4 and simple XAI
approaches among low and high NFC participants in an AI-assisted nutrition study
(e.g., making a plate low-carb by changing the ingredients accompanied by AI and
explanations) with a simulated AI. Despite high NFC participants trusting and pre-
ferring cognitive forcing functions less than simple explainable AI approaches, they
generally performed better in the task than low NFC participants. Furthermore, low
NFC participants generally found the task signiﬁcantly more mentally demanding
and the system considerably more complex than high NFC participants. This might
conﬁrm the ﬁndings from Millecamp et al. (2019, 2020) that only cognitive forcing
functions produce intervention-generated inequalities between people based on their
NFC level.

3 Please refer to Sect. 3.2.4 and Fig. 1 for a detailed discussion of the explanations used in our study.
4 As we mentioned earlier, in Millecamp et al. (2019), explanations had to be explicitly activated by the
users. This is an example of cognitive forcing known as on-demand (Martijn et al. 2022; He et al. 2024,
2025; Buçinca et al. 2024; Cau and Spano 2025), where AI assistance or explanations are not immediately
available and must be enabled by a user action.

123

---

<!-- PAGE 9 -->

Exploring the impact of explainable AI and cognitive…

Page 9 of 43

3

Another study on AI-assisted nutrition by Gajos and Mamykina (2022) found that
explanation-only design (without AI recommendation and before the user decision)
beneﬁts people with a high NFC more in task learning than those with low NFC. This
ﬁnding contrasts with previous studies, suggesting that differences in participants with
diverse levels of NFC may emerge without using interventions like cognitive forcing
functions. In the context of AI-assisted maze solving, a recent study from Vasconcelos
et al. (2023) investigated whether overreliance was affected by the interaction between
participants’ NFC scores and the AI with and without explanations when the task was
hard to solve (both the AI and explanations were simulated). However, they did not ﬁnd
any evidence for this interaction, probably because the hard task given to participants
was too difﬁcult to reveal differences across NFC scores. The authors hypothesized
that even those with a high propensity for effortful thinking are likely to over-rely on
AI advice. A more recent work by Cau and Spano (2025) examined how different
levels of NFC (low or high) could inﬂuence accuracy and overreliance on AI when
presented with on-demand multifaceted explanations in an AI-assisted job application
context, and found no differences across NFC levels.

Based on this body of research, our work aims to deepen the alleged requirement
for cognitive forcing functions to highlight the differences between low and high NFC
participants. Speciﬁcally, apart from Gajos and Mamykina (2022) results, the use of
interventions to provide explanations to users on-demand or employing two-stage
detection paradigms (Green and Chen 2019a, b; He et al. 2023a; Cau and Spano 2025;
Buçinca et al. 2025) where users make the initial decision alone and then make a sec-
ond ﬁnal choice to decide whether to incorporate AI advice seems to be the only ways
to elicit differences in low and high NFC participants. Additionally, previous studies
investigating participants’ NFC used simulated AIs, always correct AI’s recommen-
dations, and one/two types of simulated explanations. Therefore, we examine whether
a difference exists between low and high NFC participants’ decision-making given
different AI information and explanations (i.e., prediction, conﬁdence, accuracy, and
explanation styles such as example-based, feature-based, rule-based, and counterfac-
tual) in a complex (Salimzadeh et al. 2023) and high-stakes Footnote 7 loan application
scenario, considering users’ accuracy, cognitive load, and how they prioritize the XAI
interface information.

3 Hypotheses and task design

In this section, we start describing how we translated our research questions into
hypotheses, studying how AI information and explanations affect decision-making
(RQ1), how individuals with varying levels of Need for Cognition prioritize interface
elements (RQ2), and whether these individuals differ in accuracy and cognitive load
(RQ3). We then detail the task design scenario employed to test these hypotheses.

123

---

<!-- PAGE 10 -->

3

Page 10 of 43

3.1 Hypotheses

F. M. Cau, L. D. Spano

Hypotheses Related to RQ1. As discussed in Sect. 2.1, previous research indicates
that low and high levels of AI conﬁdence and accuracy affect user reliance on AI
in decision-making. Given we showed users a ﬁxed AI accuracy that is relatively
high (i.e., 83% on the test set, see Sect. 3.2.2), we believe that high AI conﬁdence
will lead users to rely more on AI predictions. Conversely, low AI conﬁdence may
encourage users to think independently, increasing their cognitive load compared to
high AI conﬁdence. In Sect. 2.2, we also mentioned that previous work does not
highlight any strong advantages of rule-based and counterfactual explanations over
feature-based ones. Additionally, the efﬁcacy of example-based explanations primarily
depends on the similar instances retrieved. Given that we are considering tabular data,5
presenting similar instances would signiﬁcantly increase task complexity and thus
users’ cognitive load (Salimzadeh et al. 2023; Cau et al. 2023b), which may lead
them to rely on the most frequent AI prediction across the similar instances (such
as accepting if the majority of similar instances are accepted) rather than carefully
analyzing each instance individually. Instead, feature-based explanations (in our case,
feature contribution) provide users with an immediate overview of important attributes
relevant to the AI’s decision and seem at a glance to satisfy more desiderata for
AI models and explanations (i.e., understanding, uncertainty awareness, and trust
calibration) when users are somewhat knowledgeable about the target domain (Wang
and Yin 2022). Although satisfying more desiderata does not imply an increased
accuracy in the task, we hypothesize that feature-based explanations might lead users
to achieve higher accuracy than the other AI assistance conditions. Summarizing, we
formulate the following hypotheses:

(cid:129) H1a: Users exposed to a high AI conﬁdence will rely more on the AI prediction

than users exposed to a low AI conﬁdence.

(cid:129) H1b: Users exposed to a high AI conﬁdence will report a lower cognitive load

than users exposed to a low AI conﬁdence.

(cid:129) H1c: Users exposed to feature-based explanations will achieve higher accuracy

than in other AI assistance conditions.

Hypotheses Related to RQ2. As noted in Sect. 2.3, high NFC individuals engage more
with effortful activities and complex interfaces than low NFC individuals. We therefore
aim to explore which type of information (i.e., applicant details, AI information, or
explanations) participants prioritize when ranking interface elements to make a ﬁnal
decision at different levels of NFC. We hypothesize that, given the complexity of the
loan prediction task and the effort needed to inspect explanations, low NFC individuals
will assign higher priority to AI information (rank 2) than to explanations (rank 3)
when making their ﬁnal decision. In contrast, high NFC individuals will assign higher
priority to explanations (rank 2) over AI information (rank 3), reﬂecting their tendency
to engage with more complex interface features and attribute greater importance to
explanations. Hence, we formalized the following hypotheses:

5 Loan approval decisions are recorded and communicated using tables that summarize applicant attributes
(e.g., income, credit score, and employment; see Sect. 3.2.1).

123

---

<!-- PAGE 11 -->

Exploring the impact of explainable AI and cognitive…

Page 11 of 43

3

(cid:129) H2a: Users with a low NFC will mainly prioritize the applicant’s details to make
their ﬁnal decision (rank 1), then the AI information (rank 2), and lastly the expla-
nation (rank 3).

(cid:129) H2b: Users with a high NFC will mainly prioritize the applicant’s details to make
their ﬁnal decision (rank 1), then the explanation (rank 2), and lastly the AI infor-
mation (rank 3).

Hypotheses Related to RQ3. We hypothesize that high NFC participants will leverage
explanations to get more insights about the information provided by the AI, potentially
achieving higher accuracy than the low NFC ones. Additionally, given their inclina-
tion to enjoy complex cognitive activities, high NFC participants will report a lower
cognitive load in completing the loan approval tasks:
(cid:129) H3a: When provided with explanations, users with a high NFC will achieve a

higher accuracy than users with a low NFC.

(cid:129) H3b: When provided with explanations, users with a high NFC will report a lower

cognitive load than users with a low NFC.

3.2 Task design

This subsection deﬁnes how we implemented the loan application task, describing the
data we used, the model, instance selection, and model explanation generation.

3.2.1 Data

We built the loan approval task on the publicly available Loan Prediction Problem
Dataset,6 consisting of 614 loan requests where the goal is to decide whether to accept
or reject a loan application based on twelve features. We opted for this dataset since it
reﬂects a realistic and fairly complex human–AI collaboration scenario (Salimzadeh
et al. 2023; He et al. 2023a). Also, the loan prediction scenario has been used in other
human–AI team studies (Binns et al. 2018; Green and Chen 2019b; Gomez et al. 2020;
Chromik et al. 2021; van Berkel et al. 2021; He et al. 2023a; Esfahani et al. 2024a;
He et al. 2025), reinforcing its validity and suitability for collaboratively analyzing
interactions between humans and AI systems. We decided to convert the nature of this
task from low-stakes to high-stakes7 by rewarding participants with a monetary bonus
in case of correct decisions (Salimzadeh et al. 2023) (see Sect. 4.3). Before training the
model, we discarded the Loan-ID column given its low informativeness for both the
user and the AI in the decision-making process, resulting in eleven features (excluding
the outcome of the loan request, see Fig. 1A).

3.2.2 Model

We used a Random Forest Classiﬁer (RFC) to solve the loan approval task, following
the approach in Chromik et al. (2021). The RFC was trained with 100 estimators (trees)

6 https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset.
7 We designed the task as high-stakes to increase participants’ engagement and simulate realism, as ﬁnancial
decision-making in the real world often involves consequences (Salimzadeh et al. 2023).

123

---

<!-- PAGE 12 -->

3

Page 12 of 43

F. M. Cau, L. D. Spano

using an 80:20 stratiﬁed split for training and test sets, achieving a test set accuracy
of about 83%, consistent with their results. We then proceeded to the RFC calibration
phase (Silva Filho et al. 2023), although the methods we tested did not signiﬁcantly
improve the calibration metrics (see Sect. A.1). We computed the model conﬁdence
estimates on the test set, as described in Sect. 3.2.3. From now on, we will refer to the
RFC model as the AI.

3.2.3 Instances

Before selecting the instances for the user study, we computed the AI conﬁdence
estimates on the test set using Shannon’s entropy method to extract the epistemic
uncertainty (Shaker and Hüllermeier 2020) and convert it into a conﬁdence score
ranging from 0 to 100. We computed the quartiles on the test set conﬁdence scores,
assigning an instance to a low conﬁdence if its value was below 44.3 (Q2) and a high
conﬁdence if its value was above 61.6 (Q3). Then, we selected the ﬁnal instances to
include in the user study by randomly picking 16 (Candrian and Scherer 2022; He
et al. 2023b; Tsirtsis et al. 2024; Strickland et al. 2024) and balancing them across
AI correctness, conﬁdence, predicted class, and true class (see Table 1). Next, we
randomly split these instances into two groups of eight, balancing the values of the
aforementioned attributes (i.e., our controlled variables). We keep the ﬁrst group for
practice and the latter for the main session. The ﬁnal low conﬁdence values were
between 9% and 43%, while high conﬁdence values were between 68% and 85%.
Given the test accuracy of the AI is about 83%, participants’ “observed” accuracy8
will be only 62.5% (i.e., the AI provides correct recommendations in 5 out of 8
instances). We deliberately presented more instances where the AI made incorrect
predictions to investigate whether and how participants would tend to rely excessively
on the AI system. To account for ordering effects (Nourani et al. 2021), we prepared
400 random permutations for the practice and main session instances, ensuring each
participant sees differently ordered loan requests.

3.2.4 AI assistance and explanations

In this work, we assessed the effects of six AI assistance conditions (see Fig. 1), using
no AI assistance as a baseline. One condition included AI information without expla-
nations, incorporating prediction, conﬁdence in the prediction, and AI accuracy on the
test set. The remaining four conditions added explanations to this AI information, as
detailed below.

Example-based. Example-based explanations do not usually provide direct insights
into the internal model functioning in predicting a speciﬁc output. Instead, they are
usually employed to show representative prototypes of the AI’s predicted class or
select similar examples (Binns et al. 2018; Cai et al. 2019a; Dodge et al. 2019; Lai
and Tan 2019; Buçinca et al. 2020; Hase and Bansal 2020; Wang and Yin 2021;
Kim et al. 2022) that resemble the examined instance. An exception of this concerns

8 Observed accuracy (62.5%) refers to the actual accuracy the AI is set to provide throughout the study for
both practice and main sessions, which we do not communicate to participants.

123

---

<!-- PAGE 13 -->

Exploring the impact of explainable AI and cognitive…

Page 13 of 43

3

Table 1 Instance settings for practice and main sessions of the loan prediction tasks, for which the order
has been uniquely randomized for each participant

ID

AI correctness

AI conﬁdence

AI prediction

True prediction

1

2

3

4

5

6

7

8

Correct

Correct

Wrong

Correct

Correct

Correct

Wrong

Wrong

High

Low

High

Low

High

Low

High

Low

Reject

Reject

Reject

Accept

Accept

Accept

Accept

Accept

Reject

Reject

Accept

Accept

Accept

Accept

Reject

Reject

approximating a black-box model to a surrogate transparent model (i.e., Twin Systems
Kenny and Keane 2019, 2021; Ford and Keane 2023), where the weights of a black-
box model are transferred into a transparent surrogate such as a k-NN. This way, the
surrogate model mimics the original black-box model behavior and provides nearest
neighbor instances that align with the original model decisions. In our study, we built
example-based explanations taking inspiration from Chen et al. (2023). We selected
the three nearest neighbor instances from the training set with the closest standardized
Euclidean distance to the current loan request test instance, showing the AI prediction
of the neighbor instances. To reduce the cognitive load on users, we highlight the
neighbor feature values that differ from the given loan request test instance, so that
users can focus on the differences between instances (see Fig. 1C, Example-based).

Feature-based. Feature contribution enables users to identify the key attributes
that signiﬁcantly inﬂuence the AI’s output, facilitating informed decision-making and
understanding of the AI’s behavior (e.g., LIME Ribeiro et al. 2016 and SHAP Lund-
berg and Lee 2017). Given its solid theoretical background, and the faithfulness and
robustness in the generated explanations (Bodria et al. 2023; Feldkamp and Strass-
burger 2023), we rendered feature-based explanations using the SHapley Additive
exPlanations (SHAP) model-agnostic method (Lundberg and Lee 2017), explaining
the AI’s prediction by showing the Shapley contribution of each feature in favor
(positive sign) or against (negative sign) the AI’s prediction, and presented with an
interactive vertical bar chart (see Fig. 1D, Feature-based). We used purple to represent
contributions of a rejected loan request and green for an accepted loan request. The
length of each bar indicates the magnitude of that attribute’s contribution relative to
the AI prediction on the current loan request.

Rule-based. Rule-based explanations provide a series of “if-then” statements high-
lighting a model’s decision-making process that humans can easily understand (Adadi
and Berrada 2018; Wang et al. 2019; Ribeiro et al. 2018; Bodria et al. 2023). We gener-
ated rule-based explanations via the model-agnostic method called Anchors (Ribeiro
et al. 2018), which deﬁnes a rule (set of predicates) so that an instance is assigned
to a speciﬁc class only if all its predicates (i.e., features tested with threshold values)
satisfy that rule with a high probability. Anchors also return the precision and the

123

---

<!-- PAGE 14 -->

3

Page 14 of 43

F. M. Cau, L. D. Spano

Fig. 1 AI assistance conditions for the loan approval tasks. Participants can display additional information
about the attributes by hovering over the info buttons. A (No AI) Participants will see the task’s goal and
the current applicant’s details. B (AI) Participants will also be assisted by an AI in the decision-making task
(i.e., with prediction, conﬁdence, and accuracy). C (Example-based) Participants will see condition “B - AI”
and the three nearest neighbors of the current applicant. D (Feature-based) Participants will see condition
“B - AI” and the Shapley feature contribution for each applicant’s attribute. E (Rule-based) Participants will
see condition “B - AI” and the rule generated by Anchor. F (Counterfactual) Participants will see condition
“B - AI” and three counterfactual instances generated by DiCE

coverage of the extracted rule. The precision indicates how well an anchor predicts
the model’s output. A high precision value suggests that the anchor is a good pre-
dictor of the output variable, while a low precision value highlights that the anchor
is a poor predictor. Instead, coverage measures how many examples in the dataset
are covered by the anchor. A high coverage value indicates that the anchor is a good
representative of the dataset, while a low coverage value means the anchor is a poor
representative. When generating the rules, we set the precision threshold constraint
to 95% (i.e., ﬁnding the anchor that maximizes the coverage given the threshold). We
show participants the extracted rule in a tabular form, where each row represents a
predicate which a feature is tested against a threshold value. Additionally, we added

123

---

<!-- PAGE 15 -->

Exploring the impact of explainable AI and cognitive…

Page 15 of 43

3

two columns showing the precision and coverage of the generated rule (see Fig. 1E,
Rule-based).9

Counterfactual. Counterfactual explanations provide contrastive “what-if” state-
ments that help users understand what changes could be made to achieve a desired
output (Wachter et al. 2017; Adadi and Berrada 2018; Mothilal et al. 2020a). We built
counterfactual explanations using the Diverse Counterfactual Explanations (DiCE)
framework (Mothilal et al. 2020b) for its effectiveness in providing diverse and action-
able counterfactual explanations (Mothilal et al. 2021; Moreira et al. 2022). Given a
test instance, DiCE generates counterfactual explanations that emphasize diversity and
deliver a more comprehensive understanding of the model’s behavior, providing mul-
tiple counterfactuals that are diverse in terms of the changes made to the input features.
Following the line of example-based explanations, we show users three counterfactual
explanations generated from a given loan request test instance. Similarly, we highlight
the counterfactual feature values that differ from the given loan request test instance to
reduce users’ cognitive load and let them focus on the differences between instances
(see Fig. 1F, Counterfactual).

4 Study design

Our study followed a mixed-factorial design, where we asked participants to decide
whether to accept or reject a series of loan requests (see Table 1). We initially measured
participants’ NFC and divided them into low and high groups based on the distribution
median. Next, we assigned each participant to one of the AI assistance conditions as
a between-subjects factor (i.e., no AI; AI without explanations; AI + example-based
explanations; AI + rule-based explanations; and AI + counterfactual explanations).
Also, we studied the effects of the following within-subjects covariates: AI conﬁdence
(low and high), and AI correctness (correct and wrong). First, participants completed
a practice session of eight loan requests to familiarize themselves with the task and
the assigned AI assistance condition. Next, they completed the main session of the
study with another eight loan requests.

This section outlines the variables, planned sample size, statistical analysis, and the

procedure for the user study we conducted to test our hypotheses.

4.1 Variables

For the hypothesis test, we considered the following measurements collected in the
main session of the user study. We collected the following independent variables:

(cid:129) AI assistance (between-subjects, categorical). We created six scenarios that varied
in terms of assistance provided by the AI and explanations to the participants
during their decision-making process.

9 Participants could view detailed information about the operator, precision, and coverage attributes at any
time during the study by hovering the info button next to each attribute. These concepts were also explained
in detail before the practice session.

123

---

<!-- PAGE 16 -->

3

Page 16 of 43

F. M. Cau, L. D. Spano

– No AI. We showed participants the loan request attributes and asked whether

it should be accepted or rejected.

– AI. We showed participants the information in the No AI condition and the
following AI information: (i) prediction for the current loan request, (ii) pre-
diction conﬁdence, and iii) accuracy on the test set.

– Example-based. We showed participants the information in the AI condition

and three nearest neighbor instances of the current loan request.

– Feature-based. We showed participants the information in the AI condition

and the SHAP feature contribution for each loan request attribute.

– Rule-based. We showed participants the information in the AI condition and

the Anchor rule for the current loan request.

– Counterfactual. We showed participants the information in the AI condition
and three DiCE-generated counterfactual instances based on the current loan
request.

(cid:129) Need for cognition (between-subjects, categorical). NFC is a stable personality
trait that reﬂects how much a person enjoys engaging in cognitively demanding
activities (Cacioppo et al 1984). We measured participants’ NFC using the six-item
Need for Cognition Scale (NCS-6) deﬁned in de Holanda Coelho et al. (2020) (see
Sect. A for details). We split participants into low and high NFC by computing the
median of the NFC score distribution, the same criteria used in previous work on
AI-assisted decisions (Buçinca et al. 2021, 2024, 2025; Conati et al. 2021; Bahel
et al. 2024; Cau and Spano 2025).

We measured their effects on four dependent variables:

(cid:129) Accuracy (categorical). We measured participants’ accuracy as whether each
accept/reject decision for a loan matched the instance’s ground truth (i.e., wrong
or correct).

(cid:129) Reliance (categorical). We measured participants’ reliance on AI by assessing
whether a participant agreed or disagreed with the AI prediction (i.e., agree or
disagree).

(cid:129) Interface components importance (ranking). We measured the importance of inter-
face elements for participants in determining their ﬁnal choice, including the loan
request, the AI information, and the explanation, measured as a ranking. Partici-
pants responded to the statement: “Please rank the following information in terms
of how important it was for you in making your ﬁnal decision: (a) loan attributes,
(b) AI information, (c) explanation.”

(cid:129) Cognitive load (numerical). We assessed how difﬁcult participants found the tasks
using the Single Ease Question (SEQ) (Sauro and Dumas 2009) 7-point rating
scale, ranging from “1 - Very easy” to “7 - Very difﬁcult.”

We also collected the following covariates (see Table 1):

(cid:129) AI conﬁdence (within-subjects, categorical). Participants saw loan requests with

either low or high AI conﬁdence.

(cid:129) AI correctness (within-subjects, categorical). Participants saw loan requests with

correct or wrong AI predictions.

123

---

<!-- PAGE 17 -->

Exploring the impact of explainable AI and cognitive…

Page 17 of 43

3

Finally, we collected other descriptive and exploratory measurements to provide
context for our study and enable further exploratory analyses to motivate our hypothe-
ses:

(cid:129) Demographics (categorical). We gathered participants’ information on their sex

and age from the Proliﬁc platform.

(cid:129) Familiarity with the task (categorical). We asked participants about their familiarity
with loan request approval with the following statements using a 5-point Likert
scale ranging from “1 - No experience” to “5 - Highly experienced”:

– “Do you have any experience with loan request approval?”
– “Do you have any experience with AI-assisted loan request approval?”
(cid:129) AI information importance (ranking). We asked participants to rank the importance
of the AI prediction, conﬁdence, and accuracy in the conditions that include the
AI information by asking: “Please rank the following AI information in terms of
how important it was for you in making your ﬁnal decision: (a) AI prediction, (b)
AI conﬁdence, (c) AI accuracy.”

(cid:129) XAI interface understanding (numerical). At the end of the survey, we asked par-
ticipants to state their easiness of understanding the loan application attributes,
AI information, and explanations using a 5-point Likert scale ranging from ”1 -
Strongly disagree” to ”5 - Strongly agree” in three items (i) “The loan application
attributes were easy to understand,” (ii) ‘The AI information provided was easy to
understand,” and (iii) “The AI explanation provided was easy to understand.”
(cid:129) Textual feedback (open text). At the end of the survey, we collected participants’
feedback about the explanations (when presented) by asking: “What were the pros
and cons of the AI explanations you encountered?”

4.2 Planned sample size and statistical analysis

Before recruiting participants, we estimated the required sample size for our study
using G*Power software (Faul et al. 2009), resulting in 286 participants. This rec-
ommended sample size is motivated by the maximum number of participants needed
among the hypotheses, which we describe in detail as follows. Since we are assessing
ﬁve hypotheses with mixed models (continuous/categorical dependent variables) and
two based on ranking information (using the Friedman test), we decided to apply two
different thresholds, using α = 0.05
= .025
5
for ranking tests. Thus, we considered as signiﬁcant the p-values below these reduced
thresholds in the analysis. Additionally, we assigned a randomly generated seed to
each user as a (i) random intercept to account for the variability of the dependent
variables across different clusters in the mixed-effects logistic regression and as a (ii)
within-cluster correlation effect on the dependent variable in the Generalized Estima-
tion Equation (GEE) models. All the models converged successfully.

= .01 for mixed models and α = 0.05
2

To answer H1a and H1c with categorical dependent variables, we used two mixed-
effects logistic regression models with Reliance and Accuracy as the dependent
variables, assessing the main effects of AI assistance as the independent variable,
and AI conﬁdence and AI correctness as covariates. We computed the required sample

123

---

<!-- PAGE 18 -->

3

Page 18 of 43

F. M. Cau, L. D. Spano

size using G*Power for a mixed-effects logistic regression model (a priori χ 2 test)
with medium effect size (Cohen’s d = 0.25), a desired power of 0.8, Df = 5, and two
covariates (AI conﬁdence and AI correctness), resulting in 286 participants.10 Instead,
to answer H1b which involves a numeric dependent variable, we used a Generalized
Estimation Equation (GEE) model with Cognitive load as the dependent variable to
assess the main effects of the AI conﬁdence covariate while also studying potential
impacts of the AI assistance as an independent variable and AI correctness as a covari-
ate. We computed the required sample size using the G*Power for a mixed-design
ANCOVA, medium effect size (Cohen’s f = 0.25), a desired power of 0.8, Df = 1, and
two covariates (AI conﬁdence and AI correctness), resulting in 191 participants.

To answer H2, we conducted a Friedman test (Friedman 1937, 1940) with Interface
component importance ranked measurements as the dependent variable to assess the
main and interaction effects of Need for Cognition (low and high) as the independent
variable. We computed the required sample size using G*Power for a within-subjects
Friedman Test with medium effect size (Cohen’s f = 0.16), a desired power of 0.8, one
group, and three measurements (i.e., loan application attributes, AI information, and
explanation), resulting in 100 participants. To establish the ranking order among XAI
interface elements, we conducted a Nemenyi post hoc analysis when we discovered
signiﬁcant factors in the Friedman test.

To answer hypothesis H3a with a categorical dependent variable, we used a mixed-
effects logistic regression model with Accuracy as the dependent variable to study the
main effects of Need for Cognition as the independent variable. We also investigated
the impact of AI assistance as an independent variable and AI conﬁdence and AI
correctness as covariates. We computed the required sample size using the G*Power
for a mixed-effects logistic regression model (a priori χ 2 test) with medium effect size
(Cohen’s d = 0.25), a desired power of 0.8, Df = 1, and two covariates (AI conﬁdence
and AI correctness), resulting in 187 participants. Instead, to answer H3b, which
involves a numeric dependent variable, we used a Generalized Estimation Equation
(GEE) model with Cognitive load as the dependent variable to assess the main effects
of Need for Cognition. Further, we also investigated the impact of AI assistance as an
independent variable, and AI conﬁdence and AI correctness as covariates. We computed
the required sample size using the G*Power for a mixed-design ANCOVA, medium
effect size (Cohen’s f = 0.25), a desired power of 0.8, Df = 1, and two covariates (AI
conﬁdence and AI correctness), resulting in 191 participants.

4.3 Procedure

To verify our hypotheses, we conducted an online user study using the Proliﬁc plat-
form,11 where we recruited participants aged 18 or older with high English proﬁciency
and approval rates between 95 and 100. Participants were then redirected to the
LimeSurvey tool12 where they completed the study in three steps. Participants received

10 While H1a and H1b require around 191 participants (Df = 1) for low and high AI conﬁdence levels, H1c
increases the number of participants given that we tested all six AI assistance conditions (Df = 5).
11 https://www.proliﬁc.com/.
12 https://www.limesurvey.org/.

123

---

<!-- PAGE 19 -->

Exploring the impact of explainable AI and cognitive…

Page 19 of 43

3

Fig. 2 Illustration of the procedure participants engaged in during our study

£2.7 as a reward for the study, with an average completion time of 18 min (i.e., £9/h,
which is considered a fair payment for Proliﬁc). Proliﬁc automatically timed out par-
ticipants after 60 min. We rewarded participants with an extra £0.12 for each correctly
classiﬁed loan request of the main session. We only included participants in the analy-
sis if they passed all ﬁve attention checks. The study has been approved by the Ethics
Committee of the University of Cagliari.13

Participants went through the following steps, illustrated in Fig. 2. First, they read
a document containing a brief study description, ﬁlled out an informed consent form,
and completed an attention check14 Next, they stated their familiarity with the task
and completed another attention check. Then, we asked participants to ﬁll out the
six-item Need for Cognition Scale (de Holanda Coelho et al. 2020) and to complete
another attention check. We introduced participants to the task and assigned them to
one of the six AI assistance conditions (i.e., no AI; AI without explanations; AI +
example-based explanations; AI + rule-based explanations; and AI + counterfactual
explanations) while balancing the participation among conditions. Before starting the
practice session, we provided participants with details about the assigned AI assistance
condition, where they completed another attention check. Then, participants completed
eight loan request tasks as a practice session, where they needed to decide whether to
accept or reject the applications. After each decision, participants received feedback
on their answers, where we revealed the corresponding true class. When participants
ﬁnished the practice session, we showed them a page as a reminder for the main task
session, resulting in a compensation bonus in case of correctly classifying a loan.
Before starting the main session, participants completed the last attention check.

Participants completed eight loan request tasks, with the same AI assistance condi-
tion assigned in Step 2 but without receiving feedback on the true class. For each task,
we measured participants’ cognitive load. We also asked them to rank the importance
of the interface components (see Sect. 4.1) except in the “No AI” and “AI” conditions.
Finally, we asked participants to state their ease of understanding of the XAI interface
elements (i.e., loan application attributes, AI information, and explanation) and to
provide textual feedback about the pros and cons of the explanations they encountered
(see Sect. 4).

13 Received on July 25, 2024, Prot. 0205640.
14 We use Instructional Manipulation Checks (IMCs), where the answer to each attention check is explicitly
reported in the question text and follows the good practices of Proliﬁc. https://researcher-help.proliﬁc.com/
en/article/fb63bb.

123

---

<!-- PAGE 20 -->

3

Page 20 of 43

5 Results

5.1 Descriptive statistics

F. M. Cau, L. D. Spano

The ﬁnal sample of 288 participants comprised 144 males and 144 females, aged
between 18 and 74 (M = 32.42, SD = 10.95). Participants reported low familiarity
with the loan application task (M = 1.83, SD = 0.99, 5-point Likert scale, 1: no
experience, 5: highly experienced) and AI-assisted loan request approval (M = 1.32,
SD = 0.71, 5-point Likert scale, 1: no experience, 5: highly experienced). Overall,
participants reported a good easiness in understanding the loan application attributes
(M = 3.72, SD = 0.93, 5-point Likert scale, 1: strongly disagree, 5: strongly agree),
AI information (M = 3.74, SD = 0.95, 5-point Likert scale, 1: strongly disagree,
5: strongly agree), and explanations (M = 3.67, SD = 1.00, 5-point Likert scale, 1:
strongly disagree, 5: strongly agree). The NFC subdivision into low (143) and high
(145) individuals was achieved with a computed median Mdn = 3.50 (M = 3.48 and
SD = 0.76). Figure 8 in Appendix shows the continuous values of the NFC distribution.
Given the distributions for low and high NFC were non-normal (Shapiro–Wilk: low,
W = 0.915, p < .0001; high W = 0.888, p < .0001) and that homogeneity of
variances was unequal (Levene’s test: F = 23.2, p < .0001), we used a Wilcoxon
rank-sum test, which conﬁrmed a signiﬁcant difference between low and high NFC
groups (W = 0, p < .0001). The between-subject design and NFC variables were
overall homogeneous in terms of demographics and familiarity.15 We further discuss
differences in the participants’ understanding of the interface components (i.e., loan,
AI information, and explanations) in Sect. 5.3.1.

5.2 Hypothesis tests

5.2.1 H1: Effects of AI and explanations on users’ reliance on AI, cognitive load, and

accuracy

The resulting charts for H1 are depicted in Fig. 3. For H1a, we used a mixed-effects
logistic regression model to examine the differences in users’ reliance on AI, consider-
ing low and high AI conﬁdence. The results of the analysis showed a signiﬁcant effect
(Log-Odds = 1.22, Std. error = 0.12, z-value = 10.40, p < .01) of high AI conﬁdence
in increasing users’ reliance on AI than low AI conﬁdence. Hence we reject the null
hypothesis for H1a, as users rely more on the AI when exposed to high AI conﬁ-
dence than low conﬁdence. In H1b, we studied the differences in users’ cognitive load
between low and high AI conﬁdence using a Generalized Estimation Equation (GEE)

15 A Kruskal–Wallis test was conducted to compare familiarity scores across design and NFC groups. The
results indicated no signiﬁcant differences in familiarity considering the design variable (familiarity: χ 2 =
5.74, p = .33; familiarity AI: χ 2 = 9.2, p = .1). We observed similar results across NFC groups, except for
task familiarity (χ 2 = 4.79, p = .03), which was higher for high NFC individuals (M = 1.97, SD = 1.06),
compared to low NFC individuals (M = 1.69, SD = 0.89). For familiarity with AI (χ 2 = 1.5, p = .22),
the difference was not signiﬁcant (high NFC: M = 1.36, SD = 0.75; low NFC: M = 1.28, SD = 0.68). We
thus repeated the analysis for hypotheses H3a and H3b, adding familiarity as a covariate for potential main
effects and interactions for NFC and familiarity with the task. However, no signiﬁcant results were found.

123

---

<!-- PAGE 21 -->

Exploring the impact of explainable AI and cognitive…

Page 21 of 43

3

Fig. 3 Effects of low and high AI conﬁdence considering reliance on AI (H1a), cognitive load (H1b) (ticks
above bars indicate lower and higher conﬁdence intervals based on standard errors), and users’ accuracy
(H1c) divided by AI assistance conditions. The asterisks highlight p-value signiﬁcance strength (*** p <
.001)

model. The results of the analysis showed a signiﬁcant effect (Log-Odds = −0.41,
Std. error = 0.06, Wald = 54.57, p < .01) of high AI conﬁdence in decreasing users’
cognitive load compared to low AI conﬁdence. Hence, we reject the null hypothesis
for H1b, concluding that users report lower cognitive load when exposed to high AI
conﬁdence compared to low conﬁdence. For H1c, we investigated the users’ accuracy
differences among AI assistance conditions using a mixed-effects logistic regression
model. The results of the analysis showed no signiﬁcant effects (Log-Odds = 0.34, Std.
error = 0.16, z-value = 2.11, p = .0349) of feature-based explanations over the other
interface conditions on users’ accuracy; hence, we fail to reject the null hypothesis for
H1c16.

5.2.2 H2: Effects of low and high NFC participants on XAI interface information

importance

To test H2 (see Fig. 4), we included only participants exposed to explanations, resulting
in 192 users. For H2a, we hypothesized that low NFC participants would give priority
to the AI information (rank 2) immediately after the loan attributes (rank 1), keeping
the explanation (rank 3) as a last resort. The Friedman test for H2a shows a signiﬁcant
difference (χ 2 = 159, df = 2, p < .025) between the three XAI interface elements
when investigating low NFC participants. The pairwise ranking comparisons using the
Nemenyi ( p < .025) show that users prioritize the loan attributes (rank 1), followed
by the explanation (rank 2) and the AI information (rank 3) when making their ﬁnal
decision. In this light, we fail to reject the null hypothesis for H2a. For H2b, the
Friedman test shows a signiﬁcant difference (χ 2 = 324, df = 2, p < .025) between the
three XAI interface elements when investigating high NFC participants. The Nemenyi
pairwise ranking comparisons ( p < .025) align with our hypothesis, showing that
users prioritize the loan attributes (rank 1), followed by the explanation (rank 2) and

16 Although the result did not meet the α = .01 threshold, counterfactual explanations were the only other
explanation type, besides feature-based explanations, to show an effect on improving users’ accuracy (Log-
Odds = 0.39, Std. Error = 0.16, z = 2.43, p = .0149). Post hoc pairwise comparisons using Tukey HSD did
not show signiﬁcant differences across AI assistance conditions.

123

---

<!-- PAGE 22 -->

3

Page 22 of 43

F. M. Cau, L. D. Spano

Fig. 4 XAI interface components rank frequencies for low (H2a) and high (H2b) NFC individuals. The
asterisks highlight p-value signiﬁcant strength (*** p < .001)

the AI information (rank 3) when making their ﬁnal decision. Hence, we reject the
null hypothesis for H2b.

5.2.3 H3: Effects of low and high NFC participants on accuracy and cognitive load

For H3a (see Fig. 5), we investigated whether high NFC individuals may achieve
increased accuracy when exposed to explanations compared to low NFC individuals.
The results of the mixed-effects logistic regression analysis showed no signiﬁcant
effects (Log-Odds = 0.03, Std. error = 0.10, z-value = 0.28, p = .78) among low
and high NFC participants. Hence, we fail to reject the null hypothesis for H3a. In
H3b, we studied the differences in users’ cognitive load between low and high NFC
participants when exposed to explanations using a Generalized Estimation Equation
(GEE) model. The results of the analysis showed no signiﬁcant effects (Log-Odds =
−0.08, Std. error = 0.12, Wald = 0.51, p = .47) for high NFC participants compared
to low NFC participants. Hence, we fail to reject the null hypothesis for H3b.17

5.3 Post hoc and exploratory analyses

The hypotheses results (see Table 2) revealed that high AI conﬁdence increases reliance
on AI and reduces cognitive load. Additionally, there were no signiﬁcant differences in
users’ accuracy among the different AI assistance conditions. Considering the interface
component preferences, low and high NFC participants ranked loan attributes ﬁrst,
explanation second, and AI information third. Finally, no accuracy or cognitive load
differences between low and high NFC individuals were found.

To further clarify the role of AI and explanations in shaping user behavior, we con-
ducted additional analyses considering the interaction effects between covariates (AI
conﬁdence and correctness) and explanations, further clarifying the role of AI infor-
mation in users’ prioritization of XAI interface elements’ ranking. We ﬁrst examined

17 For completeness, we also repeated the same tests to examine the impact of NFC with the original
continuous values, ﬁnding no signiﬁcant results for H3a and H3b.

123

---

<!-- PAGE 23 -->

Exploring the impact of explainable AI and cognitive…

Page 23 of 43

3

Fig. 5 Users’ accuracy (H3a) and cognitive load (H3b) disaggregated by low and high NFC (ticks above
bars indicate the Standard Error)

Table 2 Summary results of our hypotheses

Hypotheses

H1a: Users exposed to a high AI conﬁdence will rely more on the

AI prediction than users exposed to a low AI conﬁdence

H1b: Users exposed to a high AI conﬁdence will report a lower

cognitive load than users exposed to a low AI conﬁdence

H1c: Users exposed to feature-based explanations will achieve

higher accuracy than other AI assistance conditions

H2a: Users with a low NFC will mainly prioritize the applicant’s

details to make their ﬁnal decision (rank 1), then the AI
information (rank 2), and lastly the explanation (rank 3)

H2b: Users with a high NFC will mainly prioritize the applicant’s
details to make their ﬁnal decision (rank 1), then the explanation
(rank 2), and lastly the AI information (rank 3)

H3a: When explanations are shown, users with a high NFC will

achieve a higher accuracy than users with a low NFC

H3b: When explanations are shown, users with a high NFC will

report a lower cognitive load than users with a low NFC

Supported

✓

✓

✗

✗

✓

✗

✗

how AI conﬁdence inﬂuences users’ interpretation of explanations by considering
metrics such as accuracy, reliance on AI, and cognitive load. We then reassessed these
metrics by considering AI correctness to investigate potential overreliance behavior in
AI when users interact with explanations. Additionally, given the signiﬁcant impact of
high AI conﬁdence on increasing users’ reliance on AI, we evaluated how it impacted
users’ prioritization of the XAI interface elements (i.e., loan attributes, AI informa-
tion, and explanation) and whether it affected users’ ranking of AI information (i.e.,
prediction, conﬁdence, and accuracy). Lastly, we focused on how low and high NFC
users ranked the AI information (i.e., prediction, conﬁdence, and accuracy), where we
considered only the AI assistance condition incorporating explanations.

123

---

<!-- PAGE 24 -->

3

Page 24 of 43

F. M. Cau, L. D. Spano

The results from the ﬁrst analysis show no signiﬁcant interactions between AI
conﬁdence and explanations of users’ reliance on AI, cognitive load, and accuracy
(see Fig. 9 in Appendix).18 Instead, we found multiple signiﬁcant results when con-
sidering the AI correctness and explanation interactions (see Fig. 6-A). For reliance
on AI, counterfactual explanation interaction with AI correct predictions leads to an
increase in reliance (Log-Odds = 0.98, Std. error = 0.35, z-value = 2.79, p = .0051).
The cognitive load results for counterfactual explanations and interaction with AI
correctness (Log-Odds = −0.48, Std. error = 0.14, Wald = 10.91, p = .0009) show a
decrease in users’ cognitive load. These ﬁndings suggest that presenting counterfactual
explanations reduces the cognitive load when AI predictions are correct. Additionally,
such explanations encourage users to follow correct predictions, potentially mitigating
overreliance on AI.

Interestingly, users’ accuracy ﬁndings highlight a trend for AI correct predictions
interacting with counterfactual explanations (Log-Odds = − 0.84, Std. error = 0.34,
z value = − 2.47, p < .0133) in decreasing accuracy. Additionally, counterfactual
explanations (Log-Odds = 0.87, Std. error = 0.27, z-value = 3.17, p = .0015) lead to an
increase in accuracy. These results might indicate a nuanced trade-off: counterfactual
explanations improve decision-making overall but can sometimes confuse users when
AI predictions are already correct.

The results of splitting XAI interface information by AI conﬁdence (see Fig. 10
in Appendix and Fig. 6B) show a signiﬁcant difference between the three interface
components for low conﬁdence (χ 2 = 301, df = 2, p < .025). The Nemenyi pairwise
comparisons show a signiﬁcant difference ( p < .025) between loan attributes (rank
1) with AI information and explanation. Instead, there are no differences between AI
information and explanation. We also have a signiﬁcant difference among the three
interface components for high AI conﬁdence (χ 2 = 196, df = 2, p < .025). The
Nemenyi pairwise comparison results ( p < .025) show that participants prioritize
the loan attributes (rank 1), followed by the AI information (rank 2), and then the
explanation (rank 3). Finally, we found no ranking differences among AI prediction,
conﬁdence, and accuracy when considering low AI conﬁdence. Instead, the results
for high AI conﬁdence highlight a difference among the AI information elements (χ 2
= 17.3, df = 2, p < .025). The Nemenyi pairwise comparisons ( p < .025) reveal
a signiﬁcant difference between AI prediction and both AI conﬁdence and accuracy,
while no signiﬁcant difference is observed between AI conﬁdence and accuracy.

In the second analysis, we repeated the Friedman test focusing on the AI prediction,
conﬁdence, and accuracy ranking, considering low and high NFC participants. The
results for low NFC participants show a signiﬁcant difference between AI informa-
tion provided (χ 2 = 13.2, df = 2, p < .025). The Nemenyi pairwise comparisons
( p < .025) reveal a signiﬁcant difference between AI prediction and AI accuracy.
However, no differences emerge when considering AI conﬁdence in comparison to AI
prediction and accuracy. Instead, the Friedman test for high NFC participants high-
lights no signiﬁcant differences among AI prediction, conﬁdence, and accuracy. This
may hint that low NFC users seem to focus more on the AI prediction, which is rein-

18 Although it falls outside the scope of our hypotheses, it is important to notice that high AI conﬁdence
signiﬁcantly increases users’ accuracy ( p < .01).

123

---

<!-- PAGE 25 -->

Exploring the impact of explainable AI and cognitive…

Page 25 of 43

3

Fig. 6 Post hoc analyses results for A AI correctness interaction with AI assistance, and B ranking for low
and high AI conﬁdence with AI information importance of interface elements. The connections between
rows present p values and the direction of the effect (e.g., a downward arrow for a decrease in the connected
dependent variable; for rankings, we display the exact position of each interface element based on pairwise
comparisons)

forced by AI conﬁdence, while high NFC people seem to look at the AI information
as a whole.

5.3.1 Participants’ interface understandability and qualitative feedback

This section summarizes users’ understanding of the interface components and textual
feedback on explanation types we collected from the user study, highlighting subjective
perspectives and perceived pros and cons from users about explanations.

The chart depicting users’ overall understanding of loan attributes, AI information,
and explanations is shown in Fig. 7. We notice that, in general, counterfactual expla-
nations decrease overall understanding of interface components. We then conducted
a statistical analysis to understand if these differences are merely visual trends or if
there is indeed a signiﬁcant difference. Given the non-normal nature of the interface
components’ distributions, we opted for a nonparametric Kruskal–Wallis test, using
the above variables as dependent variables and the design as the independent variable.
Although there were no differences for loan understanding among conditions, we
found signiﬁcant differences for AI (χ 2 = 9.76, df = 4, p = .045) and explanation (χ 2
= 9.92, df = 3, p = .019) understanding. We performed a pairwise comparison using
a Dunn test with Bonferroni for p-value adjustment. We found a difference between
AI (without explanations) and counterfactual conditions (z = − 2.88, p = .0389) for

123

---

<!-- PAGE 26 -->

3

Page 26 of 43

F. M. Cau, L. D. Spano

Fig. 7 Users’ understanding of loan attributes, AI information, and explanations by AI assistance conditions

the AI information understanding and another difference between feature-based and
counterfactual conditions (z = − 3.018, p = .0152) in the explanation understanding.
Considering users’ feedback on explanations, 11 participants reported that example-
based ones were easy, understandable, and a fast way to compare applications. As such,
P16 said: “[explanation] was helpful once understood all the attribute details”. On
the contrary, 11 participants said that explanations lacked details and that it was hard
to trust them fully. P73 stated: “[explanation] made it easy for making a decision but
not sure about their reliability”.

Feature-based explanations were perceived by 8 participants as helpful and pro-
viding clarity for the decision-making. P75 stated: “explain well the rationale behind
accepting or rejecting the loan”. However, 10 participants reported needing more
insight into why speciﬁc weights were assigned to attributes. As such, P79 said: “The
explanation needed more insights about how the weights were generated”.

Twelve participants perceived rule-based explanations as useful and easy to under-
stand, providing good guidance in decision-making. For example, P22 said: “The
explanation helped me decide whether my evaluation of the loan application is more
or less correct or not”. Despite this, 12 participants stated these explanations lacked
understandability, highlighting the absence of “reasoning” for the rules. As such, P84
reported: “Some rules had more information than others which made the choices
slightly harder”.

6 participants perceived counterfactual explanations as helpful and easy to read. For
example, P85 reported: “The explanation includes many changes in the attribute but
helps to understand (going through scenarios) which attributes are more important
and inﬂuential than others.”. On the contrary, 6 participants stated they were unclear
or untrustworthy. For example, P5 said: “Explanation is very helpful but hard to trust
due to not knowing the mechanisms behind the AI”.

6 Discussion

The paper explored how AI assistance and various explanation types inﬂuence users’
accuracy, reliance on AI, and cognitive load. Additionally, we examined the role of
XAI interface elements for individuals with low and high NFC, analyzing differences

123

---

<!-- PAGE 27 -->

Exploring the impact of explainable AI and cognitive…

Page 27 of 43

3

in accuracy and cognitive load across these groups. Based on our results, we present
a comprehensive discussion of our key ﬁndings, offering insights into design impli-
cations and examining user behaviors in the context of a loan application scenario.

6.1 The role of AI in shaping user decision-making

Our ﬁndings reveal that high AI conﬁdence increases users’ reliance on AI prediction.
This is supported by post hoc analysis, where users prioritize loan attributes ﬁrst (rank
1), then AI information (rank 2), and explanations last (rank 3). When AI conﬁdence
is low, users still prioritize loan attributes (rank 1) but assign equal priority to AI
information and explanations (both rank 2). Interestingly, prior research (Cau et al.
2023b) in high-uncertainty domains like stock trading found that users prioritize data
or AI information interchangeably (rank 1) with high AI conﬁdence, but rank AI
(2nd) immediately after data (1st) when AI conﬁdence is low. This suggests that as
uncertainty in decision-making increases, individuals are more likely to seek additional
guidance from AI. In this context, the conﬁdence level of the AI is essential to the
decision-making process. Our results also indicate that high AI conﬁdence reduces
cognitive load, with only a few studies supporting this direction (Souchet et al. 2024;
Steyvers and Kumar 2024). Altogether, our ﬁndings reinforce prior work where users
tend to rely more on high AI conﬁdence across various domains and tasks (Zhang
et al. 2020; Rechkemmer and Yin 2022; Cau et al. 2023a, b; Ma et al. 2024; Kahr et al.
2023; Ma et al. 2024; Cau and Spano 2025).

While we balanced participants’ exposure to low and high AI conﬁdence, they
encountered more instances with low conﬁdence and correct predictions than with
other combinations of conﬁdence and correctness. This distribution was intentionally
designed to reﬂect a potential real-world scenario and to study participants’ reliance
behavior on AI, where the stated AI accuracy (83%) might not align with the observed
accuracy (63%) on unseen instances. As summarized in Table 4, users’ performance
in the loan prediction tasks highlights a clear split between low and high AI conﬁ-
dence instances, particularly considering under-reliance on correct suggestions with
low conﬁdence and (over)reliance on wrong suggestions with high conﬁdence. These
results highlight the participants’ uncertainty in their decision-making and their lack
of self-conﬁdence. Since we can estimate AI conﬁdence but cannot directly control
the correctness of predictions for unseen instances, it is essential to explore alterna-
tive strategies to optimize the use of AI conﬁdence estimates. Consequently, while
presenting AI conﬁdence to users is essential for enhancing transparency (Bertrand
et al. 2022; Ma et al. 2023, 2024; Fok and Weld 2024; Li et al. 2025), its signiﬁcant
impact on reinforcing AI predictions underscores the need for targeted interface design
interventions.

AI conﬁdence calibration approaches (Silva Filho et al. 2023; Ma et al. 2024; Li
et al. 2025) provide estimates that accurately reﬂect the likelihood of correctness in
AI predictions. Therefore, it is important to cultivate user awareness regarding their
own decision conﬁdence and to determine strategically when to present AI sugges-
tions based on both user and AI conﬁdence levels. One possible solution is to calibrate
users’ conﬁdence without initial AI assistance, allowing them to receive feedback

123

---

<!-- PAGE 28 -->

3

Page 28 of 43

F. M. Cau, L. D. Spano

on the trade-offs between their conﬁdence and accuracy. Once users have developed
their conﬁdence, AI assistance can be introduced using design patterns that accom-
modate both one-stage and two-stage decision-making processes. For instance, prior
research (Ma et al. 2023, 2024; Li et al. 2025) suggests dynamically adjusting the
timing of AI assistance by comparing the conﬁdence levels of the user and the AI. AI
advice may be omitted or provided on-demand (Buçinca et al. 2020; Ma et al. 2023;
He et al. 2024, 2025; Cau and Spano 2025) when user conﬁdence is high, thereby
preserving user autonomy. Conversely, when AI conﬁdence is higher, suggestions
can be presented before users make their decisions. These approaches might balance
optimizing AI support while maintaining users’ autonomy.

6.2 The impact of explanation types on user behavior

In line with previous studies on the effects of explanations on users (Zhang et al. 2020;
Chen et al. 2023; Celar and Byrne 2023; Cau and Spano 2025), our results showed that
the feature-based explanation might not improve accuracy compared to the other AI
assistance conditions. The counterfactual was the only type of explanation closest to
our threshold in increasing the accuracy of users, although we did not ﬁnd differences
among the other AI conditions. The post hoc analysis highlights multiple beneﬁts for
counterfactual explanations: increasing users’ reliance on AI while diminishing cogni-
tive load when correct AI predictions are shown, and potentially increasing accuracy.
Nevertheless, a trend suggests they might occasionally lower accuracy in speciﬁc con-
texts (correct AI predictions) and be perceived as less understandable, as highlighted
by our qualitative analysis. Interestingly, despite having nearly identical visualizations
to counterfactuals, example-based explanations had no measurable impact on these
evaluation metrics.

Recent work from Chae et al. (2025) supports these ﬁndings, indicating that counter-
factual explanations improve task performance, though users report lower satisfaction
and understandability. This suggests that counterfactual explanations may trade off
user understandability for performance gains. Also, our results are consistent with
Xuan et al. (2025), stating that counterfactual explanations are perceived as less under-
standable than other types, such as feature importance, often seen as easier to grasp.
However, explanations perceived as “easy to understand” were found to be both more
intelligible and more misleading. This aligns with the ﬁndings of Chromik et al. (2021),
suggesting that users might overestimate their understanding of local feature explana-
tions due to the illusion of explanatory depth. Furthermore, previous work (Buçinca
et al. 2020; Wang and Yin 2022) also demonstrates that subjective measures, such as
user preferences, do not necessarily align or predict objective outcomes. Overall, our
ﬁndings emphasize the importance of shifting from traditional feature-based explana-
tions, which are commonly used in AI systems. Instead, we should adopt approaches
that resemble human-like reasoning, such as counterfactuals. Hence, it is essential to
integrate various types of explanations to offer complementary insights. This combina-
tion can address each explanation’s shortcomings and limitations, ultimately leading
to the development of hybrid visualizations for explainable AI (XAI). Recent studies
have proposed integrating actionable data-centric explanations (Anik and Bunt 2021;

123

---

<!-- PAGE 29 -->

Exploring the impact of explainable AI and cognitive…

Page 29 of 43

3

Liao and Varshney 2021; Yurrita et al. 2023; Esfahani et al. 2024b; Bhattacharya et al.
2025) alongside model-centric ones, offering potential beneﬁts for both AI experts
and lay users by connecting them to the training data and inﬂuencing their percep-
tions of trust and fairness in AI systems. For instance, research in the health domain
has demonstrated that expert users gain signiﬁcant advantages from hybrid explana-
tions combining data-centric and global model-centric elements (Bhattacharya et al.
2023, 2024a, b; Szymanski et al. 2024), though these approaches remain underex-
plored for lay users (Cau and Spano 2025). Future work should focus on developing
tailored explanation interfaces that adapt to users’ expertise levels and contextual
needs, ensuring both accessibility for lay users and depth for experts. On top of this,
tailoring XAI interfaces for users may involve assessing user-centric perspectives and
characteristics, which we discuss in the next subsection.

6.3 Individual differences: NFC and personalization in AI interaction

Our ﬁndings differ from previous work (Millecamp et al. 2019; Buçinca et al. 2021;
Conati et al. 2021; Bahel et al. 2024), which reported differences between low and high
NFC individuals in terms of accuracy and cognitive load. Interestingly, we found that
both low and high NFC participants prioritized explanations (ranked 2nd) immediately
after loan application attributes (ranked 1st), leaving AI information (ranked 3rd) as
the least inﬂuential in decision-making. Moreover, low NFC individuals prioritized AI
prediction over accuracy, while those with a high NFC seem to consider AI information
as a whole. We can identify two main reasons we might not have observed signiﬁcant
NFC-related differences compared to prior studies.

First, the task’s nature and complexity may have minimized the differences between
NFC groups. Notably, prior studies focused on low-stakes tasks, such as explaining
music recommendations (Millecamp et al. 2019), nutrition choices in image-based
domains (Buçinca et al. 2021), and tutoring systems for university students with
some domain knowledge (Bahel et al. 2024). In contrast, our study involved a high-
stakes loan approval task using tabular data with eleven features, where participants
were unfamiliar with the domain. Additionally, our explanations added substantial
information for users to process, classifying the task as high-complexity according to
Salimzadeh et al. (2023). This suggests that as task complexity increases, NFC may
lose its predictive ability to differentiate individual behaviors.

Second, while the NFC personality trait has been shown to distinguish between low
and high NFC individuals, it may not reliably explain differences in AI-driven decision
outcomes, regardless of cognitive forcing. Recent AI-assisted user studies in domains
like art period detection (Küper and Krämer 2025), job applications (Cau and Spano
2025), and exercise recommendation (Buçinca et al. 2024, 2025), indicate that NFC
may not always predict differences in users’ accuracy, learning, reliance on AI, or men-
tal demand, regardless of explanation type or cognitive interventions. These ﬁndings
highlight the need for alternative traits that might capture richer insights about intrinsic
motivation to learn and think, such as Epistemic Curiosity (Litman 2008) or the ﬁve-
dimensional curiosity scale (Kashdan et al. 2018). Moreover, a notable methodological
concern is dividing participants into low- and high-trait groups after data collection

123

---

<!-- PAGE 30 -->

3

Page 30 of 43

F. M. Cau, L. D. Spano

based on the overall participant distribution median. This approach, commonly used
for NFC and other traits, may lead to imbalances and unequal group sizes, compli-
cating statistical analyses and consequent reproducibility of results. Future research
should explore alternative user-centric metrics beyond personality traits that enable
real-time categorization during studies, ensuring more balanced groups and dynamic
personalization.

6.4 Limitations and future work

We acknowledge the following limitations in our work. The ﬁrst consists of using an AI
model with uncalibrated conﬁdence estimates. Although we assessed that calibration
metrics did not improve the AI baseline model (Random Forest), this may have affected
the computation of model conﬁdence estimates and explanations generation, and con-
sequently users’ decision-making during the study. As such, we strongly encourage
future studies to calibrate their AI models when necessary to ensure stability between
AI probability outputs and conﬁdence estimates. A second limitation is that our study
employed a one-stage detection paradigm, where users’ decision-making co-occurs
with AI suggestions and explanations. While this approach mirrors many real-world
applications applied to autonomous driving (Atakishiyev et al. 2024) and cybersecu-
rity (Desolda et al. 2023), it may restrict the ability to disentangle users’ independent
reasoning from their reliance on AI advice. In contrast, two-stage detection paradigms,
where users ﬁrst evaluate a task independently before incorporating AI input, provide
a clearer separation of cognitive engagement and reliance patterns. Future research
should explore balancing these paradigms to achieve an optimal trade-off based on the
target domain’s speciﬁc demands, stakes, and cognitive complexity. The third limita-
tion is that we solely focused on the Need for Cognition personality trait. However,
many other individual differences might drive people’s decision-making and behaviors
when interacting with AI assistance or explanations, such as AI literacy (Schoeffer
et al. 2022), Actively Open-minded Thinking (Baron 1985), or metacognitive percep-
tions (Cushing et al. 2024), which would require further investigation in future work.
The last limitation concerns the generalizability of our ﬁndings beyond the speciﬁc
domain, dataset, classiﬁcation model, AI conﬁdence split into low and high levels,
and explanation methods used. Our study employed a publicly available loan approval
dataset commonly used in HCI research, along with a model achieving comparable
evaluation metrics. Additionally, our participants’ sample demonstrated low familiar-
ity with the loan approval task, and we encourage caution in generalizing these ﬁndings
to expert users. Although we used state-of-the-art methods to generate explanations,
it is possible to produce the same type of explanation (e.g., feature-based, rules, or
counterfactuals) through different approaches, which could lead to different ﬁndings.
While we ensured replicability by detailing the data processing, AI model, explana-
tion generation, and statistical analysis, several variables unique to our setup may have
inﬂuenced decision-making. Further research is needed to evaluate the impact of AI
and explanations across diverse domains with varying stakes and levels of uncertainty.

123

---

<!-- PAGE 31 -->

Exploring the impact of explainable AI and cognitive…

Page 31 of 43

3

7 Conclusion

This article investigated how presenting AI information, including prediction, con-
ﬁdence, accuracy, and explanation styles such as example-based, feature-based,
rule-based, and counterfactual, affects users’ decision-making in loan approval tasks.
Speciﬁcally, we conducted a user study (N = 288) examining how these elements inﬂu-
ence accuracy, reliance on AI, and cognitive load across six AI assistance conditions:
no AI, AI with no explanation, and AI with each of the four explanation styles. Addi-
tionally, given the recent interest in studying the Need for Cognition (NFC) personality
trait in human–AI teams, we explored how NFC levels affect users’ prioritization of
information, accuracy, and cognitive load when interacting with different explanation
styles.

Our results show that high AI conﬁdence signiﬁcantly increases users’ reliance on
AI while reducing cognitive load, emphasizing the importance of accurately calibrating
conﬁdence estimates to reﬂect AI correctness. Counterfactual explanations, despite
being rated as less understandable than feature-based ones, overall increase users’
accuracy, also reducing cognitive load and increasing reliance on AI, particularly
when paired with correct AI predictions. In contrast, feature-based explanations failed
to improve accuracy as anticipated. Moreover, we observed that NFC levels did not
signiﬁcantly differ in how users prioritize information or their reliance, accuracy, and
cognitive load, suggesting that NFC’s inﬂuence may be task- or context-speciﬁc. These
ﬁndings contribute to a deeper understanding of how AI-assisted decision-making can
be optimized by integrating complementary explanation styles and tailoring interfaces
to individual user needs. Future work should explore hybrid explanation systems and
reﬁne user-centric models with AI to create more adaptive, effective, and equitable
human–AI collaboration frameworks.

Appendix A

A.1. Model calibration

Given we will show participants the RFC conﬁdence for each prediction, we decided
to calibrate the RFC probabilities before computing the conﬁdence estimates using
three methods: Isotonic Regression (Zadrozny and Elkan 2001), Platt Scaling (Platt
2000), inductive and cross Venn-Abers (Vovk and Petej 2014; Vovk et al. 2015;
Manokhin 2017). Speciﬁcally, we compared the RFC with ensembles of ten RFC
models for each method to assess a ten-fold cross-validation. Nevertheless, in this
speciﬁc scenario, these methods slightly worsened the metrics we took into consider-
ation (Accuracy, Brier loss Brier 1950, Log loss Domingos 1999, ROC-AUC Fawcett
2004, and Expected Calibration Error Guo et al. 2017), except for the Isotonic Regres-
sion to some extent (see Table 3). We decided to use our original (uncalibrated) RFC
model for the loan prediction task as it resulted in better calibration metrics than the
other methods we used.

123

---

<!-- PAGE 32 -->

3

Page 32 of 43

F. M. Cau, L. D. Spano

Table 3 Summary of the Random Forest calibration results using the following metrics: accuracy, Brier
loss, Log loss, ECE, and ROC-AUC

Method

Accuracy

Brier loss

Log loss

ECE

ROC-AUC

RF raw probabilities

Isotonic Regression

Platt Scaling

Cross Venn-Abers

0.8293

0.8130

0.8130

0.8211

0.1370

0.1403

0.1413

0.1492

0.4424

0.4518

0.4524

0.4727

0.0580

0.0618

0.0768

0.0641

0.8204

0.8215

0.8167

0.8

We omitted the inductive Venn-Abers given the worst results overall compared to the other methods.
The values in bold represent the best results achieved across the model calibration methods (for Accuracy
and ROC-AUC, the higher the better; for Brier loss, Log loss, and ECE, the lower the better).

A.2. Need for cognition scale

We will measure participants’ Need for Cognition (NFC) with the NCS-6 considering
a 5-point scale (1 = extremely uncharacteristic of me; 5 = extremely characteristic
of me). We will sum up all the six-item scores and then compute the median to split
participants into low and high NFC. We used the following six items to compute the
NFC from de Holanda Coelho et al. (2020)19:

1. I would prefer complex to simple problems.
2. I like to have the responsibility of handling a situation that requires a lot of thinking.
3. Thinking is not my idea of fun. (R)
4. I would rather do something that requires little thought than something that is sure

to challenge my thinking abilities. (R)

5. I really enjoy a task that involves coming up with new solutions to problems.
6. I would prefer a task that is intellectual, difﬁcult, and important to one that is

somewhat important.

A.3. Metrics overview by task

We summarized participants’ performance on loan prediction tasks in Table 4, ordered
by decreasing accuracy. Along with reliance on AI and cognitive load, we also reported
participants’ disagreement with correct AI advice, namely their under-reliance. We
reported all the metrics in percent (%), except for cognitive load.

19 note: (R) = reversed items.

123

---

<!-- PAGE 33 -->

Exploring the impact of explainable AI and cognitive…

Page 33 of 43

3

Table 4 Participants’ accuracy, reliance on AI, under-reliance on AI, and cognitive load for our loan
prediction task instance settings

ID

AI correctness

AI conﬁdence

Accuracy

Reliance

Under-reliance

Cognitive load

5

1

6

4

2

8

3

7

Correct

Correct

Correct

Correct

Correct

Wrong

Wrong

Wrong

High

High

Low

Low

Low

Low

High

High

90.4

85.4

71.2

56.2

44.2

27.9

27.1

14.6

90.4

85.4

71.2

56.2

44.2

72.1

72.9

85.4

9.6

14.6

28.7

43.8

55.8

–

–

–

3.1

3.3

3.8

3.7

3.8

3.5

3.4

3.3

Fig. 8 NFC distribution of participants in the user study. The orange vertical line represents the NFC median
(3.5) we used to split participants into low and high NFC groups

Fig. 9 Participants’ reliance on AI, cognitive load, and accuracy divided by AI assistance and AI conﬁdence
conditions

123

---

<!-- PAGE 34 -->

3

Page 34 of 43

F. M. Cau, L. D. Spano

Fig. 10 XAI interface components rank frequencies for low and high AI conﬁdence. The asterisks highlight
p value signiﬁcant strength (*** p < .001)

Acknowledgements This research is funded by the Italian Ministry of University and Research (MUR)
and by the European Union—NextGenerationEU, Mission 4, Component 2, Investment 1.1, under grant
PRIN 2022 PNRR ”DAMOCLES: Detection And Mitigation Of Cyber attacks that exploit human vuLner-
abilitiES” (Grant P2022FXP5B)—CUP: H53D23008140001.

Author contribution FC conceived and designed the user study and performed experiments under the
supervision of LS. All authors jointly wrote and reviewed the manuscript.

Funding Open access funding provided by Università degli Studi di Cagliari within the CRUI-CARE
Agreement.

Data availability The original dataset used in this article is openly available at https://www.kaggle.
com/datasets/altruistdelhite04/loan-prediction-problem-dataset. The study pipeline of data processing,
model training, explanation generation, and statistical analysis is openly available at https://osf.io/j64x8/?
viewonly=7f546294a08843acbf204521ba7dee7e.

Declarations

Conﬂict of interest The authors declare no conﬂict of interest.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included
in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

References

Adadi, A., Berrada, M.: Peeking inside the black-box: a survey on explainable artiﬁcial intelligence (xai).

IEEE Access 6, 52138–52160 (2018). https://doi.org/10.1109/ACCESS.2018.2870052

Agudo, U., Liberal, K.G., Arrese, M., et al.: The impact of ai errors in a human-in-the-loop process. Cogn.

Res. Princ. Implic. 9(1), 1 (2024). https://doi.org/10.1186/s41235-023-00529-3

Anik, A.I., Bunt, A.: Data-centric explanations: explaining training data of machine learning systems to
promote transparency. In: Proceedings of the 2021 CHI Conference on Human Factors in Computing

123

---

<!-- PAGE 35 -->

Exploring the impact of explainable AI and cognitive…

Page 35 of 43

3

Systems. Association for Computing Machinery, New York, NY, USA, CHI ’21 (2021). https://doi.
org/10.1145/3411764.3445736

Atakishiyev, S., Salameh, M., Yao, H., et al.: Explainable artiﬁcial intelligence for autonomous driving:
a comprehensive overview and ﬁeld guide for future research directions. IEEE Access 12, 101603–
101625 (2024). https://doi.org/10.1109/ACCESS.2024.3431437

Bahel, V., Sriram, H., Conati, C.: Initial results on personalizing explanations of ai hints in an its. In:
Proceedings of the 32nd ACM Conference on User Modeling, Adaptation and Personalization. Asso-
ciation for Computing Machinery, New York, NY, USA, UMAP ’24, pp. 244–248 (2024). https://doi.
org/10.1145/3627043.3659566

Bansal, G., Wu, T., Zhou, J. et al.: Does the whole exceed its parts? the effect of ai explanations on
complementary team performance. In: Proceedings of the 2021 CHI Conference on Human Factors in
Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’21 (2021).
https://doi.org/10.1145/3411764.3445717

Baron, J.: Rationality and Intelligence. Cambridge University Press, Cambridge (1985)
Beede, E., Baylor, E., Hersch, F. et al.: A human-centered evaluation of a deep learning system deployed
in clinics for the detection of diabetic retinopathy. In: Proceedings of the 2020 CHI Conference on
Human Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA,
CHI ’20, pp. 1–12 (2020). https://doi.org/10.1145/3313831.3376718

Bertrand, A., Belloum, R., Eagan, J.R., et al.: How cognitive biases affect xai-assisted decision-making: a
systematic review. In: Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society.
Association for Computing Machinery, New York, NY, USA, AIES ’22, pp. 78–91 (2022). https://
doi.org/10.1145/3514094.3534164

Bhattacharya, A., Ooge, J., Stiglic, G., et al.: Directive explanations for monitoring the risk of diabetes onset:
Introducing directive data-centric explanations and combinations to support what-if explorations.
In: Proceedings of the 28th International Conference on Intelligent User Interfaces. Association for
Computing Machinery, New York, NY, USA, IUI ’23, pp. 204–219 (2023). https://doi.org/10.1145/
3581641.3584075

Bhattacharya, A., Stumpf, S., Gosak, L., et al.: Exmos: explanatory model steering through multifaceted
explanations and data conﬁgurations. In: Proceedings of the CHI Conference on Human Factors in
Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’24 (2024a).
https://doi.org/10.1145/3613904.3642106

Bhattacharya, A., Stumpf, S., Verbert, K.: An explanatory model steering system for collaboration between
domain experts and ai. In: Adjunct Proceedings of the 32nd ACM Conference on User Modeling,
Adaptation and Personalization. Association for Computing Machinery, New York, NY, USA, UMAP
Adjunct ’24, pp. 75–79 (2024b). https://doi.org/10.1145/3631700.3664886

Bhattacharya, A., Vanherwegen, T., Verbert, K.: "show me how": beneﬁts and challenges of agent-augmented
counterfactual explanations for non-expert users. In: Proceedings of the 33rd ACM Conference on
User Modeling, Adaptation and Personalization. Association for Computing Machinery, New York,
NY, USA, UMAP ’25, pp. 174–184 (2025). https://doi.org/10.1145/3699682.3728321

Binns, R., Van Kleek, M., Veale, M., et al.: ’It’s reducing a human being to a percentage’: perceptions of
justice in algorithmic decisions. In: Proceedings of the 2018 CHI Conference on Human Factors in
Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’18, pp. 1–14
(2018). https://doi.org/10.1145/3173574.3173951

Bodria, F., Giannotti, F., Guidotti, R., et al.: Benchmarking and survey of explanation methods for black
box models. Data Min. Knowl. Disc. 37(5), 1719–1778 (2023). https://doi.org/10.1007/s10618-023-
00933-9

Boonprakong, N., Tag, B., Goncalves, J., et al.: How do HCI researchers study cognitive biases? A scoping
review. In: Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.
Association for Computing Machinery, New York, NY, USA, CHI ’25 (2025). https://doi.org/10.
1145/3706598.3713450

Bove, C., Aigrain, J., Lesot, M.J., et al.: Contextualization and exploration of local feature importance
explanations to improve understanding and satisfaction of non-expert users. In: 27th International
Conference on Intelligent User Interfaces. Association for Computing Machinery, New York, NY,
USA, IUI ’22, pp. 807–819 (2022). https://doi.org/10.1145/3490099.3511139

Brier, G.W.: Veriﬁcation of forecasts expressed in terms of probability. Mon. Weather Rev. 78, 1–3 (1950)
Buçinca, Z., Lin, P., Gajos, K.Z., et al.: Proxy tasks and subjective measures can be misleading in evaluat-
ing explainable ai systems. In: Proceedings of the 25th International Conference on Intelligent User

123

---

<!-- PAGE 36 -->

3

Page 36 of 43

F. M. Cau, L. D. Spano

Interfaces. Association for Computing Machinery, New York, NY, USA, IUI ’20, pp. 454–464 (2020).
https://doi.org/10.1145/3377325.3377498

Buçinca, Z., Malaya, M.B., Gajos, K.Z.: To trust or to think: cognitive forcing functions can reduce overre-
liance on AI in ai-assisted decision-making. Proc. ACM Hum. Comput. Interact. (2021). https://doi.
org/10.1145/3449287

Buçinca, Z., Swaroop, S., Paluch, A.E., et al.: Towards optimizing human-centric objectives in ai-assisted

decision-making with ofﬂine reinforcement learning (2024). arxiv:2403.05911

Buçinca, Z., Swaroop, S., Paluch. A.E., et al.: Contrastive explanations that anticipate human misconceptions
can improve human decision-making skills. In: Proceedings of the 2025 CHI Conference on Human
Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’25
(2025). https://doi.org/10.1145/3706598.3713229

Cacioppo, J., Petty, R., Kao, C.: The efﬁcient assessment of NFC. J. Pers. Assess. 48, 306–7 (1984). https://

doi.org/10.1207/s15327752jpa4803_13

Cai, C.J., Jongejan, J., Holbrook, J.: The effects of example-based explanations in a machine learning inter-
face. In: Proceedings of the 24th International Conference on Intelligent User Interfaces. Association
for Computing Machinery, New York, NY, USA, IUI ’19, pp. 258–262 (2019a). https://doi.org/10.
1145/3301275.3302289

Cai, C.J., Reif, E., Hegde, N., et al.: Human-centered tools for coping with imperfect algorithms during
medical decision-making. In: Proceedings of the 2019 CHI Conference on Human Factors in Comput-
ing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’19, pp. 1–14 (2019b).
https://doi.org/10.1145/3290605.3300234

Candrian, C., Scherer, A.: Rise of the machines: delegating decisions to autonomous ai. Comput. Hum.

Behav. 134, 107308 (2022). https://doi.org/10.1016/j.chb.2022.107308

Cao, S., Liu, A., Huang, C.M.: Designing for appropriate reliance: the roles of ai uncertainty presentation,
initial user decision, and user demographics in ai-assisted decision-making. Proc ACM Hum. Comput.
Interact. (2024a). https://doi.org/10.1145/3637318

Cao, S., Liu, A., Huang, C.M.: Designing for appropriate reliance: the roles of ai uncertainty presentation,
initial user decision, and user demographics in ai-assisted decision-making. Proc. ACM Hum. Comput.
Interact. (2024b). https://doi.org/10.1145/3637318

Carenini, G.: An analysis of the inﬂuence of need for cognition on dynamic queries usage. In: CHI ’01
Extended Abstracts on Human Factors in Computing Systems. Association for Computing Machinery,
New York, NY, USA, CHI EA ’01, pp. 383–384 (2001). https://doi.org/10.1145/634067.634293
Cau, F.M., Spano, L.D.: The inﬂuence of curiosity traits and on-demand explanations in ai-assisted
decision-making. In: Proceedings of the 30th International Conference on Intelligent User Interfaces.
Association for Computing Machinery, New York, NY, USA, IUI ’25, pp. 1440–1457 (2025). https://
doi.org/10.1145/3708359.3712165

Cau, F.M., Hauptmann, H., Spano, L.D., et al.: Effects of ai and logic-style explanations on users’ decisions
under different levels of uncertainty. ACM Trans. Interact. Intell. Syst. (2023a). https://doi.org/10.
1145/3588320

Cau, F.M., Hauptmann, H., Spano, L.D., et al.: Supporting high-uncertainty decisions through ai and logic-
style explanations. In: Proceedings of the 28th International Conference on Intelligent User Interfaces.
Association for Computing Machinery, New York, NY, USA, IUI ’23, pp. 251–263 (2023b). https://
doi.org/10.1145/3581641.3584080

Cazan, A.M., Indreica, S.E.: Need for cognition and approaches to learning among university students.
Procedia Soc. Behav. Sci. 127, 134–138 (2014). https://doi.org/10.1016/j.sbspro.2014.03.227
Celar, L., Byrne, R.: How people reason with counterfactual and causal explanations for artiﬁcial intelligence
decisions in familiar and unfamiliar domains. Memory Cogn. (2023). https://doi.org/10.3758/s13421-
023-01407-5

Chae, S., Lee, S., Hauptmann, H., et al.: The role of explanation styles and perceived accuracy on decision
making in predictive process monitoring. In: Krogstie, J., Rinderle-Ma, S., Kappel, G., et al. (eds.)
Adv. Inf. Syst. Eng., pp. 39–56. Springer, Cham (2025)

Chen, V., Liao, Q.V., Wortman Vaughan, J., et al.: Understanding the role of human intuition on reliance
in human–AI decision-making with explanations. Proc. ACM Hum. Comput. Interact. (2023). https://
doi.org/10.1145/3610219

Chromik, M., Eiband, M., Buchner, F., et al.: I think i get your point, ai! the illusion of explanatory depth
in explainable ai. In: Proceedings of the 26th International Conference on Intelligent User Interfaces.

123

---

<!-- PAGE 37 -->

Exploring the impact of explainable AI and cognitive…

Page 37 of 43

3

Association for Computing Machinery, New York, NY, USA, IUI ’21, pp. 307–317 (2021) .https://
doi.org/10.1145/3397481.3450644

Conati, C., Barral, O., Putnam, V., et al.: Toward personalized XAI: a case study in intelligent tutoring

systems. Artif. Intell. 298, 103503 (2021). https://doi.org/10.1016/j.artint.2021.103503

Cushing, C.A., Lau, H., Hofmann, S.G., et al.: Metacognition as a window into subjective affective expe-

rience. Psychiatry Clin. Neurosci. 78(8), 430–437 (2024)

Day, E., Boatman, J., Kowollik, V., et al.: Modeling the links between need for cognition and the acquisition
of a complex skill. Person. Indiv. Differ. 42, 201–212 (2007). https://doi.org/10.1016/j.paid.2006.06.
012

de Holanda Coelho, G.L., Hanel, P.H.P., Wolf, L.J.: The very efﬁcient assessment of need for cogni-
tion: developing a six-item version. Assessment 27(8), 1870–1885 (2020). https://doi.org/10.1177/
1073191118793208

Desolda, G., Aneke, J., Ardito, C., et al.: Explanations in warning dialogs to help users defend against
phishing attacks. Int. J. Hum. Comput. Stud. 176, 103056 (2023). https://doi.org/10.1016/j.ijhcs.
2023.103056

Dodge, J., Vera Liao, Q., Zhang, Y., et al.: Explaining models: an empirical study of how explanations impact
fairness judgment. pp 275–285 (publisher Copyright: 2019 Association for Computing Machinery.;
24th ACM International Conference on Intelligent User Interfaces, IUI 2019 ; Conference date: 17-
03-2019 Through 20-03-2019) (2019). https://doi.org/10.1145/3301275.3302310

Domingos, P.: Metacost: a general method for making classiﬁers cost-sensitive. In: Proceedings of the Fifth
ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. Association for
Computing Machinery, New York, NY, USA, KDD ’99, pp. 155–164, (1999). https://doi.org/10.1145/
312129.312220

Esfahani, S., De Toni, G., Lepri, B., et al.: Preference elicitation in interactive and user-centered algorithmic
recourse: an initial exploration. In: Proceedings of the 32nd ACM Conference on User Modeling,
Adaptation and Personalization. Association for Computing Machinery, New York, NY, USA, UMAP
’24, pp. 249–254 (2024a). https://doi.org/10.1145/3627043.3659556

Esfahani, S., De Toni, G., Lepri, B., et al.: Preference elicitation in interactive and user-centered algorithmic
recourse: an initial exploration. In: Proceedings of the 32nd ACM Conference on User Modeling,
Adaptation and Personalization. Association for Computing Machinery, New York, NY, USA, UMAP
’24, pp. 249–254 (2024b). https://doi.org/10.1145/3627043.3659556

Faul, F., Erdfelder, E., Buchner, A., et al.: Statistical power analyses using g* power 3.1: tests for correlation

and regression analyses. Behav. Res. Methods 41(4), 1149–1160 (2009)

Fawcett, T.: Roc graphs: notes and practical considerations for researchers. Mach. Learn. 31, 1–38 (2004)
Feldkamp, N., Strassburger, S.: From explainable ai to explainable simulation: using machine learning
and xai to understand system robustness. In: Proceedings of the 2023 ACM SIGSIM Conference on
Principles of Advanced Discrete Simulation. Association for Computing Machinery, New York, NY,
USA, SIGSIM-PADS ’23, pp. 96–106 (2023). https://doi.org/10.1145/3573900.3591114

Fogliato, R., Chappidi, S., Lungren, M., et al.: Who goes ﬁrst? Inﬂuences of human–AI workﬂow on decision
making in clinical imaging. In: Proceedings of the 2022 ACM Conference on Fairness, Accountability,
and Transparency. Association for Computing Machinery, New York, NY, USA, FAccT ’22, pp. 1362–
1374 (2022a). https://doi.org/10.1145/3531146.3533193

Fogliato, R., Chappidi, S., Lungren, M., et al.: Who goes ﬁrst? Inﬂuences of human-ai workﬂow on decision
making in clinical imaging. In: Proceedings of the 2022 ACM Conference on Fairness, Accountability,
and Transparency. Association for Computing Machinery, New York, NY, USA, FAccT ’22, pp. 1362–
1374 (2022b). https://doi.org/10.1145/3531146.3533193

Fok, R., Weld, D.S.: In search of veriﬁability: explanations rarely enable complementary performance in
AI-advised decision making. AI Mag. 45(3), 317–332 (2024). https://doi.org/10.1002/aaai.12182.
(https://onlinelibrary.wiley.com/doi/pdf/10.1002/aaai.12182)

Ford, C., Keane, M.T.: Explaining classiﬁcations to non-experts: an xai user study of post-hoc explanations
for a classiﬁer when people lack expertise. In: Pattern Recognition, Computer Vision, and Image
Processing. ICPR 2022 International Workshops and Challenges: Montreal, QC, Canada, August 21–
25, 2022, Proceedings, Part III. Springer-Verlag, Berlin, Heidelberg, pp. 246–260 (2023). https://doi.
org/10.1007/978-3-031-37731-0_15

Foroudi, P., Marvi, R., Zha, D.: Ai sensation and engagement: unpacking the sensory experience in human–
AI interaction. Int. J. Inf. Manage. 84, 102918 (2025). https://doi.org/10.1016/j.ijinfomgt.2025.102918

123

---

<!-- PAGE 38 -->

3

Page 38 of 43

F. M. Cau, L. D. Spano

Friedman, M.: The use of ranks to avoid the assumption of normality implicit in the analysis of variance.
J. Am. Stat. Assoc. 32(200), 675–701 (1937). https://doi.org/10.1080/01621459.1937.10503522.
(https://www.tandfonline.com/doi/pdf/10.1080/01621459.1937.10503522)

Friedman, M.: A comparison of alternative tests of signiﬁcance for the problem of $m$ rankings. Ann.

Math. Stat. 11, 86–92 (1940)

Gajos, K.Z., Chauncey, K.: The inﬂuence of personality traits and cognitive load on the use of adaptive
user interfaces. In: Proceedings of the 22nd International Conference on Intelligent User Interfaces.
Association for Computing Machinery, New York, NY, USA, IUI ’17, pp. 301–306 (2017). https://
doi.org/10.1145/3025171.3025192

Gajos, K.Z., Mamykina, L.: Do people engage cognitively with AI? Impact of AI assistance on incidental
learning. In: Proceedings of the 27th International Conference on Intelligent User Interfaces. Associ-
ation for Computing Machinery, New York, NY, USA, IUI ’22, pp. 794–806 (2022). https://doi.org/
10.1145/3490099.3511138

Ghai, B., Liao, Q.V., Zhang, Y., et al.: Explainable active learning (xal): toward ai explanations as interfaces

for machine teachers. Proc. ACM Hum. Comput. Interact. (2021). https://doi.org/10.1145/3432934

Gomez, O., Holter, S., Yuan, J., et al.: Vice: visual counterfactual explanations for machine learning models.
In: Proceedings of the 25th International Conference on Intelligent User Interfaces. Association for
Computing Machinery, New York, NY, USA, IUI ’20, pp. 531–535 (2020). https://doi.org/10.1145/
3377325.3377536

Gomez, C., Cho, S.M., Ke, S., et al.: Human–AI collaboration is not very collaborative yet: a taxonomy
of interaction patterns in AI-assisted decision making from a systematic review. Front. Comput. Sci.
(2025). https://doi.org/10.3389/fcomp.2024.1521066

Grace, K., Finch, E., Gulbransen-Diaz, N., et al.: Q-chef: the impact of surprise-eliciting systems on food-
related decision-making. In: Proceedings of the 2022 CHI Conference on Human Factors in Computing
Systems. Association for Computing Machinery, New York, NY, USA, CHI ’22 (2022). https://doi.
org/10.1145/3491102.3501862

Green, B., Chen, Y.: Disparate interactions: an algorithm-in-the-loop analysis of fairness in risk assessments.
In: Proceedings of the Conference on Fairness, Accountability, and Transparency. Association for
Computing Machinery, New York, NY, USA, FAT* ’19, pp. 90–99 (2019a). https://doi.org/10.1145/
3287560.3287563

Green, B., Chen, Y.: The principles and limits of algorithm-in-the-loop decision making. Proc. ACM Hum.

Comput. Interact. (2019b). https://doi.org/10.1145/3359152

Guo, C., Pleiss, G., Sun, Y., et al.: On calibration of modern neural networks. In: Precup D, Teh YW (eds),
Proceedings of the 34th International Conference on Machine Learning, Proceedings of Machine
Learning Research, vol 70. PMLR, pp. 1321–1330 (2017). https://proceedings.mlr.press/v70/guo17a.
html

Hase, P., Bansal, M.: Evaluating explainable AI: Which algorithmic explanations help users predict model
behavior? In: Jurafsky, D., Chai, J., Schluter, N., et al. (eds), Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics. Association for Computational Linguistics,
Online, pp. 5540–5552 (2020). https://doi.org/10.18653/v1/2020.acl-main.491. https://aclanthology.
org/2020.acl-main.491

He, G., Buijsman, S., Gadiraju, U.: How stated accuracy of an ai system and analogies to explain accuracy
affect human reliance on the system. Proc. ACM Hum. Comput. Interact. (2023a). https://doi.org/10.
1145/3610067

He, G., Kuiper, L., Gadiraju, U.: Knowing about knowing: an illusion of human competence can hinder
appropriate reliance on AI systems. In: Proceedings of the 2023 CHI Conference on Human Factors in
Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’23 (2023b).
https://doi.org/10.1145/3544548.3581025

He, G., Balayn, A., Buijsman, S., et al.: Opening the analogical portal to explainability: Can analogies
help laypeople in ai-assisted decision making? J. Artif. Int. Res. (2024). https://doi.org/10.1613/jair.
1.15118

He, G., Aishwarya, N., Gadiraju, U.: Is conversational XAI all you need? Human–AI decision making with
a conversational xai assistant. In: Proceedings of the 30th International Conference on Intelligent User
Interfaces. Association for Computing Machinery, New York, NY, USA, IUI ’25, pp. 907–924 (2025).
https://doi.org/10.1145/3708359.3712133

Herm, L.V.: Impact of explainable AI on cognitive load: insights from an empirical study. In: European

Conference on Information Systems, ECIS 2023 Research, p. 269 (2023)

123

---

<!-- PAGE 39 -->

Exploring the impact of explainable AI and cognitive…

Page 39 of 43

3

Herzog, D., Wörndl, W.: A user study on groups interacting with tourist trip recommender systems in
public spaces. In: Proceedings of the 27th ACM Conference on User Modeling, Adaptation and
Personalization. Association for Computing Machinery, New York, NY, USA, UMAP ’19, pp. 130–
138 (2019). https://doi.org/10.1145/3320435.3320449

Kahr, P.K., Rooks, G., Willemsen, M.C., et al.: It seems smart, but it acts stupid: development of trust in ai
advice in a repeated legal decision-making task. In: Proceedings of the 28th International Conference
on Intelligent User Interfaces. Association for Computing Machinery, New York, NY, USA, IUI ’23,
pp. 528–539 (2023). https://doi.org/10.1145/3581641.3584058

Kahr, P.K., Rooks, G., Willemsen, M.C., et al.: Understanding trust and reliance development in ai advice:
assessing model accuracy, model explanations, and experiences from previous interactions. ACM
Trans. Interact. Intell. Syst. (2024). https://doi.org/10.1145/3686164

Kashdan, T.B., Stiksma, M.C., Disabato, D.J., et al.: The ﬁve-dimensional curiosity scale: capturing the
bandwidth of curiosity and identifying four unique subgroups of curious people. J. Res. Pers. 73,
130–149 (2018). https://doi.org/10.1016/j.jrp.2017.11.011. (https://www.sciencedirect.com/science/
article/pii/S0092656617301149)

Kenny, E.M., Keane, M.T.: Twin-systems to explain artiﬁcial neural networks using case-based reasoning:
comparative tests of feature-weighting methods in ANN-CBR twins for XAI. In: Proceedings of the
Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence, IJCAI-19. International Joint
Conferences on Artiﬁcial Intelligence Organization, pp. 2708–2715 (2019). https://doi.org/10.24963/
ijcai.2019/376

Kenny, E.M., Keane, M.T.: Explaining deep learning using examples: optimal feature weighting
methods for twin systems using post-hoc, explanation-by-example in XAI. Knowl. Based Syst.
233, 107530 (2021). https://doi.org/10.1016/j.knosys.2021.107530. (https://www.sciencedirect.com/
science/article/pii/S0950705121007929)

Kim, S., Meister, N., Ramaswamy, V., et al.: Hive: evaluating the human interpretability of visual expla-
nations. In: Avidan, S., Brostow, G., Cissé, M., et al. (eds), Computer Vision—ECCV 2022: 17th
European Conference, Proceedings. Springer Science and Business Media Deutschland GmbH, Ger-
many, Lecture Notes in Computer Science (including subseries Lecture Notes in Artiﬁcial Intelligence
and Lecture Notes in Bioinformatics), pp. 280–298 (publisher Copyright: 2022, The Author(s), under
exclusive license to Springer Nature Switzerland AG.; 17th European Conference on Computer Vision,
ECCV 2022 ; Conference date: 23-10-2022 Through 27-10-2022) (2022). https://doi.org/10.1007/
978-3-031-19775-8_17

Küper, A., Lodde, G.C., Livingstone, E., et al.: Psychological factors inﬂuencing appropriate reliance on
ai-enabled clinical decision support systems: experimental web-based study among dermatologists.
J. Med. Int. Res. 27, e58660 (2025). https://doi.org/10.2196/58660. (https://www.jmir.org/2025/1/
e58660)

Küper, A., Krämer, N.: Psychological traits and appropriate reliance: factors shaping trust in AI. Int. J.
Hum. Comput. Interact. 41(7), 4115–4131 (2025). https://doi.org/10.1080/10447318.2024.2348216
Lai, V., Tan, C.: On human predictions with explanations and predictions of machine learning models: a
case study on deception detection. In: Proceedings of the Conference on Fairness, Accountability,
and Transparency. Association for Computing Machinery, New York, NY, USA, FAT* ’19, pp. 29–38
(2019). https://doi.org/10.1145/3287560.3287590

Lai, V., Chen, C., Smith-Renner, A., et al.: Towards a science of human–AI decision making: An overview
of design space in empirical human-subject studies. In: Proceedings of the 2023 ACM Conference on
Fairness, Accountability, and Transparency. Association for Computing Machinery, New York, NY,
USA, FAccT ’23, pp. 1369–1385 (2023a). https://doi.org/10.1145/3593013.3594087

Lai, V., Zhang, Y., Chen, C., et al.: Selective explanations: leveraging human input to align explainable AI.

Proc. ACM Hum. Comput. Interact. (2023b). https://doi.org/10.1145/3610206

Lee, M.H., Siewiorek, D.P., Smailagic, A., et al.: Co-design and evaluation of an intelligent decision support
system for stroke rehabilitation assessment. Proc. ACM Hum. Comput. Interact. (2020). https://doi.
org/10.1145/3415227

Lee, M.H., Siewiorek, D.P., Smailagic, A., et al.: A human–AI collaborative approach for clinical decision
making on rehabilitation assessment. In: Proceedings of the 2021 CHI Conference on Human Factors
in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’21 (2021).
https://doi.org/10.1145/3411764.3445472

Li, D., Browne, G.: The role of need for cognition and mood in online ﬂow experience. J. Comput. Inf.

Syst. 46(3), 11–17 (2006)

123

---

<!-- PAGE 40 -->

3

Page 40 of 43

F. M. Cau, L. D. Spano

Li, J., Yang, Y., Liao, Q.V., et al.: As conﬁdence aligns: understanding the effect of ai conﬁdence on human
self-conﬁdence in human–AI decision making. In: Proceedings of the 2025 CHI Conference on Human
Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’25
(2025). https://doi.org/10.1145/3706598.3713336

Liao, M., Sundar, S.S., Walther, B.J.: User trust in recommendation systems: a comparison of content-based,
collaborative and demographic ﬁltering. In: Proceedings of the 2022 CHI Conference on Human
Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’22
(2022). https://doi.org/10.1145/3491102.3501936

Liao, Q.V., Varshney, K.R.: Human-centered explainable AI (XAI): from algorithms to user experiences

(2021)

Litman, J.A.: Interest and deprivation factors of epistemic curiosity. Person. Indvid. Differ. 44(7), 1585–1595
(2008). https://doi.org/10.1016/j.paid.2008.01.014. (https://www.sciencedirect.com/science/article/
pii/S0191886908000275)

Lu, J., Yan, Y., Huang, K., et al.: Do we learn from each other: understanding the human–AI co-learning
process embedded in human–AI collaboration. Group Decis. Negot. (2024). https://doi.org/10.1007/
s10726-024-09912-x

Lundberg, S.M., Lee, S.I.: A uniﬁed approach to interpreting model predictions. In: Proceedings of the 31st
International Conference on Neural Information Processing Systems, Curran Associates Inc., Red
Hook, NY, USA, NIPS’17, pp. 4768–4777 (2017)

Ma, S., Lei, Y., Wang, X., et al.: Who should i trust: Ai or myself? Leveraging human and ai correctness
likelihood to promote appropriate trust in AI-assisted decision-making. In: Proceedings of the 2023
CHI Conference on Human Factors in Computing Systems. Association for Computing Machinery,
New York, NY, USA, CHI ’23 (2023). https://doi.org/10.1145/3544548.3581058

Ma, S., Wang, X., Lei, Y., et al.: “are you really sure?” Understanding the effects of human self-conﬁdence
calibration in ai-assisted decision making. In: Proceedings of the 2024 CHI Conference on Human
Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’24
(2024). https://doi.org/10.1145/3613904.3642671

Manokhin, V.: Multi-class probabilistic classiﬁcation using inductive and cross Venn–Abers predictors. In:
Gammerman, A., Vovk, V., Luo, Z., et al. (eds), Proceedings of the Sixth Workshop on Conformal
and Probabilistic Prediction and Applications, Proceedings of Machine Learning Research, vol. 60.
PMLR, pp. 228–240 (2017). https://proceedings.mlr.press/v60/manokhin17a.html

Martijn, M., Conati, C., Verbert, K.: “knowing me, knowing you”: personalized explanations for a music
recommender system. User Model. User Adap. Int. 32(1), 215–252 (2022). https://doi.org/10.1007/
s11257-021-09304-9

Marusich, L.R., Bakdash, J.Z., Zhou, Y., et al.: Using ai uncertainty quantiﬁcation to improve human
decision-making. In: Proceedings of the 41st International Conference on Machine Learning.
JMLR.org, ICML’24 (2024)

Millecamp, M., Htun, N.N., Conati, C., et al.: To explain or not to explain: the effects of personal character-
istics when explaining music recommendations. In: Proceedings of the 24th International Conference
on Intelligent User Interfaces. Association for Computing Machinery, New York, NY, USA, IUI ’19,
pp. 397–407 (2019). https://doi.org/10.1145/3301275.3302313

Millecamp, M., Htun, N.N., Conati, C., et al.: What’s in a user? Towards personalising transparency for
music recommender interfaces. In: Proceedings of the 28th ACM Conference on User Modeling,
Adaptation and Personalization. Association for Computing Machinery, New York, NY, USA, UMAP
’20, pp. 173–182 (2020). https://doi.org/10.1145/3340631.3394844

Moreira, C., Chou, Y.L., Hsieh, C.J., et al.: Benchmarking counterfactual algorithms for XAI: from white

box to black box (2022). https://api.semanticscholar.org/CorpusID:252280631

Morrison, K., Spitzer, P., Turri, V., et al.: The impact of imperfect XAI on human–AI decision-making.

Proc. ACM Hum. Comput. Interact. (2024). https://doi.org/10.1145/3641022

Mothilal, R., Sharma, A., Tan, C.: Explaining Machine Learning Classiﬁers Through Diverse Counterfactual

Explanations, pp. 607–617 (2020a). https://doi.org/10.1145/3351095.3372850

Mothilal, R.K., Sharma, A., Tan, C.: Explaining machine learning classiﬁers through diverse counterfactual
explanations. In: Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency.
Association for Computing Machinery, New York, NY, USA, FAT* ’20, pp. 607–617 (2020b). https://
doi.org/10.1145/3351095.3372850

Mothilal, R.K., Mahajan, D., Tan, C., et al.: Towards unifying feature attribution and counterfactual
explanations: different means to the same end. In: AAAI/ACM Conference on AI, Ethics, and

123

---

<!-- PAGE 41 -->

Exploring the impact of explainable AI and cognitive…

Page 41 of 43

3

Society (AIES) (2021). https://www.microsoft.com/en-us/research/publication/towards-unifying-
feature-attribution-and-counterfactual-explanations-different-means-to-the-same-end/

Musto, C., Starke, A.D., Trattner, C., et al.: Exploring the effects of natural language justiﬁcations in food
recommender systems. In: Proceedings of the 29th ACM Conference on User Modeling, Adaptation
and Personalization. Association for Computing Machinery, New York, NY, USA, UMAP ’21, pp.
147–157 (2021). https://doi.org/10.1145/3450613.3456827

Nourani, M., Roy, C., Block, J.E., et al.: Anchoring bias affects mental model formation and user reliance
in explainable AI systems. In: Proceedings of the 26th International Conference on Intelligent User
Interfaces. Association for Computing Machinery, New York, NY, USA, IUI ’21, pp. 340–350 (2021).
https://doi.org/10.1145/3397481.3450639

Padilla, L.M.K., Powell, M., Kay, M., et al.: Uncertain about uncertainty: how qualitative expres-
sions of forecaster conﬁdence impact decision-making with uncertainty visualizations. Front.
Psychol. (2021). https://doi.org/10.3389/fpsyg.2020.579267. (https://www.frontiersin.org/journals/
psychology/articles/10.3389/fpsyg.2020.579267)

Panigutti, C., Beretta, A., Giannotti, F., et al.: Understanding the impact of explanations on advice-taking: a
user study for ai-based clinical decision support systems. In: Proceedings of the 2022 CHI Conference
on Human Factors in Computing Systems. Association for Computing Machinery, New York, NY,
USA, CHI ’22 (2022). https://doi.org/10.1145/3491102.3502104

Platt, J.: Probabilities for Support Vector Machines (2000)
Prabhudesai, S., Yang, L., Asthana, S., et al.: Understanding uncertainty: how lay decision-makers perceive
and interpret uncertainty in human–AI decision making. In: Proceedings of the 28th International
Conference on Intelligent User Interfaces. Association for Computing Machinery, New York, NY,
USA, IUI ’23, pp. 379–396 (2023). https://doi.org/10.1145/3581641.3584033

Rastogi, C., Zhang, Y., Wei, D., et al.: Deciding fast and slow: the role of cognitive biases in ai-assisted
decision-making. Proc. ACM Hum. Comput. Interact. (2022). https://doi.org/10.1145/3512930
Rechkemmer, A., Yin, M.: When conﬁdence meets accuracy: exploring the effects of multiple performance
indicators on trust in machine learning models. In: Proceedings of the 2022 CHI Conference on Human
Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’22
(2022). https://doi.org/10.1145/3491102.3501967

Ribeiro, M.T., Singh, S., Guestrin, C.: “why should i trust you?”: explaining the predictions of any classiﬁer.
In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining. Association for Computing Machinery, New York, NY, USA, KDD ’16, pp. 1135–1144
(2016). https://doi.org/10.1145/2939672.2939778

Ribeiro, M.T., Singh, S., Guestrin, C.: Anchors: high-precision model-agnostic explanations. In: Pro-
ceedings of the Thirty-Second AAAI Conference on Artiﬁcial Intelligence and Thirtieth Innovative
Applications of Artiﬁcial Intelligence Conference and Eighth AAAI Symposium on Educational
Advances in Artiﬁcial Intelligence. AAAI Press, AAAI’18/IAAI’18/EAAI’18 (2018)

Rong, Y., Leemann, T., Nguyen, T., et al.: Towards human-centered explainable AI: a survey of user studies
for model explanations. IEEE Trans. Pattern Anal. Mach. Intell. 46(04), 2104–2122 (2024). https://
doi.org/10.1109/TPAMI.2023.3331846

Salimzadeh, S., He, G., Gadiraju, U.: A missing piece in the puzzle: considering the role of task complexity
in human–AI decision making. In: Proceedings of the 31st ACM Conference on User Modeling,
Adaptation and Personalization. Association for Computing Machinery, New York, NY, USA, UMAP
’23, pp. 215–227 (2023). https://doi.org/10.1145/3565472.3592959

Salimzadeh, S., He, G., Gadiraju, U.: Dealing with uncertainty: Understanding the impact of prognostic
versus diagnostic tasks on trust and reliance in human–AI decision making. In: Proceedings of the
CHI Conference on Human Factors in Computing Systems. Association for Computing Machinery,
New York, NY, USA, CHI ’24 (2024). https://doi.org/10.1145/3613904.3641905

Sauro, J., Dumas, J.S.: Comparison of three one-question, post-task usability questionnaires. In: Proceedings
of the SIGCHI Conference on Human Factors in Computing Systems. Association for Computing
Machinery, New York, NY, USA, CHI ’09, pp. 1599–1608 (2009). https://doi.org/10.1145/1518701.
1518946

Scharowski, N., Perrig, S.A.C., Svab, M., et al.: Exploring the effects of human-centered AI explanations on
trust and reliance. Front. Comput. Sci. (2023). https://doi.org/10.3389/fcomp.2023.1151150. https://
www.frontiersin.org/articles/10.3389/fcomp.2023.1151150

Schoeffer, J., Kuehl, N., Machowski, Y.: “there is not enough information”: on the effects of explanations
on perceptions of informational fairness and trustworthiness in automated decision-making. In: Pro-

123

---

<!-- PAGE 42 -->

3

Page 42 of 43

F. M. Cau, L. D. Spano

ceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency. Association
for Computing Machinery, New York, NY, USA, FAccT ’22, pp. 1616–1628 (2022). https://doi.org/
10.1145/3531146.3533218

Shaker, M.H., Hüllermeier, E.: Aleatoric and epistemic uncertainty with random forests. In: Berthold, M.R.,
Feelders, A., Krempl, G. (eds.) Advances in Intelligent Data Analysis XVIII, pp. 444–456. Springer,
Cham (2020)

Silva Filho, T., Song, H., Perello-Nieto, M., et al.: Classiﬁer calibration: a survey on how to assess and
improve predicted class probabilities. Mach. Learn. 112(9), 3211–3260 (2023). https://doi.org/10.
1007/s10994-023-06336-7

Souchet, A., Amokrane-Ferka, K., Burkhardt, J.M.: Ai-assistance to decision-makers: evaluating usability,
induced cognitive load, and trust’s impact. In: Proceedings of the European Conference on Cognitive
Ergonomics 2024. Association for Computing Machinery, New York, NY, USA, ECCE ’24 (2024).
https://doi.org/10.1145/3673805.3673845

Steyvers, M., Kumar, A.: Three challenges for AI-assisted decision-making. Perspect. Psychol. Sci. 19(5),

722–734 (2024). https://doi.org/10.1177/17456916231181102

Strickland, L., Farrell, S., Wilson, M.K., et al.: How do humans learn about the reliability of automation?

Cogn. Res. Princ. Implic. 9(1), 8 (2024). https://doi.org/10.1186/s41235-024-00533-1

Subramanian, H.V., Canﬁeld, C., Shank, D.B.: Designing explainable ai

to improve human-
ai
Intell. Med.
149, 102780 (2024). https://doi.org/10.1016/j.artmed.2024.102780. https://www.sciencedirect.com/
science/article/pii/S0933365724000228

stakeholder-driven scoping review. Artif.

team performance: a medical

Swaroop, S., Buçinca, Z., Gajos, K.Z., et al.: Personalising ai assistance based on overreliance rate in AI-
assisted decision making. In: Proceedings of the 30th International Conference on Intelligent User
Interfaces. Association for Computing Machinery, New York, NY, USA, IUI ’25, pp. 1107–1122
(2025). https://doi.org/10.1145/3708359.3712128

Szymanski, M., Abeele V.V., Verbert, K.: Designing and evaluating explanations for a predictive health
dashboard: a user-centred case study. In: Extended Abstracts of the 2024 CHI Conference on Human
Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI EA
’24 (2024). https://doi.org/10.1145/3613905.3637140

Teso, S., Alkan, Ö., Stammer, W., et al.: Leveraging explanations in interactive machine learning: an

overview. Front. Artif. Intell. 6, 1066049 (2023)

Tsirtsis, S., Gomez-Rodriguez, M., Gerstenberg, T.: Towards a computational model of responsibility
judgments in sequential human-ai collaboration. In: Proceedings of the 46th Annual Meeting of the
Cognitive Science Society (CogSci 2024), Rotterdam, Netherlands (2024). https://escholarship.org/
uc/item/5h1742zk

van Berkel, N., Goncalves, J., Russo, D. et al.: Effect of information presentation on fairness perceptions
of machine learning predictors. In: Proceedings of the 2021 CHI Conference on Human Factors in
Computing Systems. Association for Computing Machinery, New York, NY, USA, CHI ’21 (2021).
https://doi.org/10.1145/3411764.3445365

Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., et al.: Explanations can reduce overreliance on ai
systems during decision-making. Proc ACM Hum. Comput. Interact. (2023). https://doi.org/10.1145/
3579605

Viswanathan, S., Omidvar-Tehrani, B., Renders, J.M.: What is your current mindset? In: Proceedings of
the 2022 CHI Conference on Human Factors in Computing Systems. Association for Computing
Machinery, New York, NY, USA, CHI ’22 (2022). https://doi.org/10.1145/3491102.3501912
Vovk, V., Petej, I.: Venn-abers predictors. In: Proceedings of the Thirtieth Conference on Uncertainty in

Artiﬁcial Intelligence. AUAI Press, Arlington, Virginia, USA, UAI’14, pp. 829–838 (2014)

Vovk, V., Petej, I., Fedorova, V.: Large-scale probabilistic predictors with and without guarantees of validity.
In: Proceedings of the 28th International Conference on Neural Information Processing Systems,
Volume 1. MIT Press, Cambridge, MA, USA, NIPS’15, pp. 892–900 (2015)

Wachter, S., Mittelstadt, B.D., Russell, C.: Counterfactual explanations without opening the black box:
automated decisions and the GDPR. Cybersecurity (2017). https://api.semanticscholar.org/CorpusID:
3995299

Wang, D., Yang, Q., Abdul, A., et al.: Designing theory-driven user-centric explainable ai. In: Proceedings
of the 2019 CHI Conference on Human Factors in Computing Systems. Association for Computing
Machinery, New York, NY, USA, CHI ’19, pp. 1–15 (2019). https://doi.org/10.1145/3290605.3300831

123

---

<!-- PAGE 43 -->

Exploring the impact of explainable AI and cognitive…

Page 43 of 43

3

Wang, X., Yin, M.: Are explanations helpful? A comparative study of the effects of explanations in ai-
assisted decision-making. In: 26th International Conference on Intelligent User Interfaces. Association
for Computing Machinery, New York, NY, USA, IUI ’21, pp. 318–328 (2021). https://doi.org/10.1145/
3397481.3450650

Wang, X., Yin, M.: Effects of explanations in AI-assisted decision making: principles and comparisons.

ACM Trans. Interact. Intell. Syst. (2022). https://doi.org/10.1145/3519266

Xuan, Y., Small, E., Sokol, K., et al.: Comprehension is a double-edged sword: over-interpreting unspeci-
ﬁed information in intelligible machine learning explanations. Int. J. Hum Comput Stud. 193, 103376
(2025). https://doi.org/10.1016/j.ijhcs.2024.103376. https://www.sciencedirect.com/science/article/
pii/S1071581924001599

Yin, M., Vaughan, W.J., Wallach, H.: Understanding the effect of accuracy on trust in machine learning
models. In: Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems.
Association for Computing Machinery, New York, NY, USA, CHI ’19, pp. 1–12 (2019) .https://doi.
org/10.1145/3290605.3300509

Yurrita, M., Draws, T., Balayn, A., et al.: Disentangling fairness perceptions in algorithmic decision-making:
the effects of explanations, human oversight, and contestability. In: Proceedings of the 2023 CHI
Conference on Human Factors in Computing Systems. Association for Computing Machinery, New
York, NY, USA, CHI ’23 (2023). https://doi.org/10.1145/3544548.3581161

Yurrita, M., Verma, H., Balayn, A., et al.: Towards effective human intervention in algorithmic decision-
making: Understanding the effect of decision-makers’ conﬁguration on decision-subjects’ fairness
perceptions. In: Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.
Association for Computing Machinery, New York, NY, USA, CHI ’25 (2025). https://doi.org/10.1145/
3706598.3713145

Zadrozny, B., Elkan, C.: Obtaining calibrated probability estimates from decision trees and naive Bayesian

classiﬁers. ICML, p. 1 (2001)

Zehrung, R., Singhal, A., Correll, M., et al.: Vis ex machina: an analysis of trust in human versus algorith-
mically generated visualization recommendations. In: Proceedings of the 2021 CHI Conference on
Human Factors in Computing Systems. Association for Computing Machinery, New York, NY, USA,
CHI ’21 (2021) .https://doi.org/10.1145/3411764.3445195

Zhang, Y., Liao, Q.V., Bellamy, R.K.E.: Effect of conﬁdence and explanation on accuracy and trust
calibration in ai-assisted decision making. In: Proceedings of the 2020 Conference on Fairness,
Accountability, and Transparency. Association for Computing Machinery, New York, NY, USA, FAT*
’20, pp. 295–305. (2020). https://doi.org/10.1145/3351095.3372852

Zhao, J., Wang, Y., Mancenido, M.V., et al.: Evaluating the impact of uncertainty visualization on model
reliance. IEEE Trans. Visual Comput. Gr. 30(7), 4093–4107 (2024). https://doi.org/10.1109/TVCG.
2023.3251950

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional afﬁliations.

Federico Maria Cau obtained his bachelor’s and master’s degrees from the University of Cagliari, where
he also earned a Ph.D. in Mathematics and Computer Science, with a focus on the effects of explanation
and uncertainty on AI-assisted user decisions. He is currently a postdoctoral researcher at the University
of Cagliari. His research interests include AI-assisted decision-making, explainable AI, Human-Centered
AI, and intelligent interfaces.

Lucio Davide Spano is an Associate Professor at the University of Cagliari, Italy, where he has been part
of the Department of Mathematics and Computer Science since 2012. He earned his Ph.D. in Computer
Science from the University of Pisa in 2013. His research focuses on Human-Computer Interaction (HCI),
extended Reality (XR), End-User Development, and explainable AI. He has authored numerous publica-
tions on interaction techniques, intelligent user interfaces, and immersive technologies. Spano has led and
contributed to various European and regional research projects, including those under H2020, FP7, and the
Italian PNRR framework. He is active in the international HCI community, serving on program commit-
tees for conferences such as ACM IUI, INTERACT, NordiCHI, and EICS, and holds leadership roles in
IFIP and SIGCHI-Italy.

123

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

UserModelingandUser-AdaptedInteraction(2026)36:3
https://doi.org/10.1007/s11257-025-09438-0
ExploringtheimpactofexplainableAIandcognitive
capabilitiesonusers’decisions
Federico Maria Cau1·Lucio Davide Spano1
Received:16December2024/Acceptedinrevisedform:12November2025/Publishedonline:6December2025
©TheAuthor(s)2025
Abstract
ArtificialIntelligence(AI)systemsareincreasinglyusedfordecision-makingacross
domains,raisingdebatesovertheinformationandexplanationstheyshouldprovide.
Most research on Explainable AI (XAI) has focused on feature-based explanations,
withlessattentiononalternativestyles.PersonalitytraitsliketheNeedforCognition
(NFC)canalsoleadtodifferentdecision-makingoutcomesamonglowandhighNFC
individuals.WeinvestigatedhowpresentingAIinformation(prediction,confidence,
and accuracy) and different explanation styles (example-based, feature-based, rule-
based,andcounterfactual)affectaccuracy,relianceonAI,andcognitiveloadinaloan
applicationscenario.WealsoexaminedlowandhighNFCindividuals’differencesin
prioritizingXAIinterfaceelements(loanattributes,AIinformation,andexplanations),
accuracy,andcognitiveload.OurfindingsshowthathighAIconfidencesignificantly
increasesrelianceonAIwhilereducingcognitiveload.Feature-basedexplanationsdid
notenhanceaccuracycomparedtootherconditions.Althoughcounterfactualexplana-
tionswerelessunderstandable,theyenhancedoverallaccuracy,increasingrelianceon
AIandreducingcognitiveloadwhenAIpredictionswerecorrect.Bothlowandhigh
NFCindividualsprioritizedexplanationsafterloanattributes,leavingAIinformation
astheleastimportant.However,wefoundnosignificantdifferencesbetweenlowand
highNFCgroupsinaccuracyorcognitiveload,raisingquestionsabouttheroleofthis
specific personality trait in AI-assisted decision-making. These findings underscore
the importance of user-centric personalization in XAI interfaces, where explanation
stylesaretailoredtousers’personalitytraits,cognitivecharacteristics,andtaskcon-
text,withsupportadaptedtoeachindividualtooptimizehuman–AIcollaboration.
Keywords Loanapprovalprediction·AI-assisteddecisions·ExplainableAI·
Reliance·Accuracy·Needforcognition
FedericoMariaandLucioDavideSpanoareequallycontributedtothiswork.
B
FedericoMariaCau
federicom.cau@unica.it
LucioDavideSpano
davide.spano@unica.it
1 DepartmentofMathematicsandComputerScience,UniversityofCagliari,ViaOspedale72,09124
Cagliari,Sardegna,Italy
123

3 Page 2 of 43 F.M.Cau,L.D.Spano
1 Introduction
Artificial Intelligence (AI) systems are becoming increasingly prevalent to assist
human decision-makers across various domains, ranging from low-stakes activities
like automating routine processes (Herzog and Wörndl 2019; Zehrung et al. 2021;
Musto et al. 2021; Liao et al. 2022; Viswanathan et al. 2022; Grace et al. 2022) to
high-stakes scenarios like healthcare diagnostics (Cai et al. 2019b; Lee et al. 2020,
2021; Beede et al. 2020; Fogliato et al. 2022a; Panigutti et al. 2022). AI-assisted
decision approaches pose numerous challenges within the HCI community, princi-
pally focusing on the problems of increasing users’ decision-making accuracy1 and
appropriaterelianceonAIsystemsrecommendations,i.e.,acceptingcorrectAIsug-
gestions and rejecting wrong ones (Zhang et al. 2020; Rechkemmer and Yin 2022;
Boveetal.2022;Scharowskietal.2023;Kahretal.2023;Vasconcelosetal.2023;
Chenetal.2023).Inparticular,previousresearchonhuman–AIteamsmainlyfocused
oninvestigatingthefollowingelements:taskcharacteristics(e.g.,complexity,stakes,
and uncertainty) (Buçinca et al. 2020; Cau et al. 2023b; Salimzadeh et al. 2023,
2024),users’traits(e.g.,NeedforCognition,taskfamiliarity,andAIliteracy)(Gajos
andChauncey2017;Buçincaetal.2021;GajosandMamykina2022;FordandKeane
2023;CelarandByrne2023;Heetal.2023a;Foroudietal.2025;Yurritaetal.2025),
different types of information about AI assistance (e.g., prediction, confidence, and
accuracy) (Yin et al. 2019; Lai and Tan 2019; Zhang et al. 2020; Rechkemmer and
Yin2022;Kahretal.2023;Heetal.2023a;CauandSpano2025),andexplanation
techniques to interpret AI decisions (e.g., example-based, feature-based, and coun-
terfactuals)(LaiandTan2019;Buçincaetal.2020;WangandYin2022;Boveetal.
2022; Chen et al. 2023; Teso et al. 2023). Despite these efforts, current research on
AI-assisteddecision-makingexhibitsdivergingresultsonhowandwhenAIassistance
isdeliveredandwhichexplanationstylescouldbetterhelpusersassesstheprovided
information.
Forexample,presentingspecificAIinformation(i.e.,prediction,confidence,and
accuracy) strongly influences users’ decision-making processes. While displaying
predicted labels increases users’ accuracy in the task compared to showing no AI
assistance(LaiandTan2019;Buçincaetal.2020),ahighAIconfidence(indicating
thecorrectnesslikelihoodinitsprediction),appearstoencourageparticipantstorely
onAIdecisionsmorethanalowone(Zhangetal.2020;RechkemmerandYin2022;
Cauetal.2023a,b).Similarly,userstendtoagreewithpredictionsofAIwithahigh
statedaccuracy2moreoftenthanthoseofmodelswithalowstatedaccuracy(Yinetal.
2019;RechkemmerandYin2022;Kahretal.2023;Heetal.2023a;Kahretal.2024).
Furthermore,studiesonhuman–AIdecision-makingrarelyevaluateusers’cognitive
loadduringtaskperformanceandthusoverlooktheextentofcognitiveresourcesbeing
utilized(SteyversandKumar2024).ThecombinedpresentationoftheseAIinforma-
tion pieces and their influence on users’ decision outcomes and perceptions is still
understudied.
1 Throughoutthepaper,wewillusethetermusers’“accuracy”toidentifytheir“decision-makingaccuracy”.
2 AIstatedaccuracyreferstotheaccuracyreportedforthemodelwhenevaluatedonunseendata,usually
thetestorheld-outset.
123

ExploringtheimpactofexplainableAIandcognitive… Page 3 of 43 3
Another crucial aspect of the decision-making process involves eXplainable AI
(XAI)techniques,whosepotentialtoenhanceuseraccuracyandappropriatereliance
onAIiscurrentlyunderdebate.Inourwork,wefocusonobjectivetasks(e.g.,whethera
personwillrepayaloan),whereagroundtruthexistsandthegoalistoevaluate,under-
stand,and/orimprovehumanperformanceandexperienceforadecision-makingtask
(Laietal.2023a).Inthesetypesoftasks,mostempiricalstudiesonAIdecisionsupport
havefocusedonfeature-basedexplanations(Laietal.2023a),andevidenceremains
inconclusive regarding their effectiveness in improving user accuracy or reducing
overreliance(Zhangetal.2020;WangandYin2021;Maetal.2023;Cauetal.2023b;
Chenetal.2023).Additionally,whilepriorworkshavecomparedtheeffectsoffeature-
basedandexample-basedexplanationsonusers(LaiandTan2019;Caietal.2019a;
Boveetal.2022;FordandKeane2023;Chenetal.2023;Laietal.2023b),thebene-
fitsandlimitationsofotherexplanationstyles,suchasrule-basedandcounterfactual
explanations,remainlargelyunderexplored(WangandYin2022;Bodriaetal.2023;
Tesoetal.2023;Cauetal.2023b,a).
Furthermore,priorworkhashighlightedthatindividualdifferencescanalsoinflu-
encepeople’sdecision-making.Recentstudiesinmusicrecommendation(Millecamp
et al. 2019, 2020), AI-assisted nutrition decisions (Buçinca et al. 2021; Gajos and
Mamykina 2022), and intelligent tutoring systems (Conati et al. 2021; Bahel et al.
2024) have explored theinfluence ofuser-centricattributeslikeNeedforCognition
(NFC)(Cacioppoetal1984)inuser-AIteams.NFCisapersonalitytraitthatreflects
anindividual’stendencytoengageinandenjoyeffortfulcognitiveactivities(Carenini
2001;CazanandIndreica2014;GajosandChauncey2017).Thisresearchhighlights
significantdifferencesinhowlowandhighNFCindividualsinteractwithAI,espe-
cially considering decision-making behavior, users’ accuracy, reliance on AI, and
cognitive load. While these studies provide some insights on specific domains, it is
unclearhowpeoplewithdifferentNFClevelsprioritizecertaininformationintheXAI
interfaceandhowdetailedAIinformationandmultipleexplanationstylesaffecttheir
decisions.
Considering this, this paper investigates how including different AI information
andexplanations(i.e.,prediction,confidence,accuracy,andexplanationstylessuchas
example-based,feature-based,rule-based,andcounterfactual)impactusers’decision-
makingprocessinasetofloanapprovaltasksconsideringtheiraccuracy,relianceon
AI, and cognitive load. Specifically, given the recent interest in studying the Need
for Cognition (NFC) personality trait in human–AI teams, we aim to examine how
differenttypesofAIinformationandexplanationstylesaffectlowandhighNFCusers
intermsof(i)howtheyprioritizetheinformationintheXAIinterfacewhenmaking
adecision,(ii)theaccuracyofthefinaldecision,and(iii)therequiredcognitiveload.
Ourresearchquestionstoaddressthesegapsarethefollowing:
RQ1 HowdoAIinformationandexplanationsimpactusers’accuracy,relianceonAI,
andcognitiveload?
RQ2 IsthereanydifferenceinhowpeoplewithlowandhighlevelsofNeedforCognition
prioritizetheinformationsuppliedintheXAIinterface?
RQ3 DopeoplewithlowandhighlevelsofNeedforCognitionhavedifferentaccuracy
andcognitiveloadwhenengagingwithexplanations?
123

3 Page 4 of 43 F.M.Cau,L.D.Spano
To answer these questions, we conducted an online user study (N = 288) where
participantsinteractedwithanAI-assistedloanapprovalinterface,decidingwhetherto
acceptorrejecteightloanrequestsbasedonvaryingAIassistance(i.e.,noAI,AIwith
noexplanation,AIwithexample-based,feature-based,rule-based,andcounterfactual
explanations). We analyzed their accuracy, reliance on AI, cognitive load, and the
importance of the XAI interface elements (i.e., loan attributes, AI information, and
explanation)thatledthemtothefinaldecision,furtherdifferentiatingtheresultsby
lowandhighlevelsofNeedforCognition.
Insummary,thecontributionsofthispaperare:
1. WefoundthatahighAIconfidencesignificantlyincreasesusers’relianceonAI
decisionswhilereducingcognitiveload.Thesefindingshighlighttheimportanceof
calibratingAIconfidenceestimatestoreflectthelikelihoodofsystemcorrectness.
Additionally,integratingusers’confidencecalibrationbeforeAIinteractionscould
enable new personalized AI-assisted strategies tailored to individual confidence
levels.
2. Contrarytoexpectations,feature-basedexplanationsdidnotimproveusers’accu-
racycomparedtootherAI-assistedconditions.However,despitebeingperceived
aslessunderstandablebyusers,counterfactualexplanationsenhancedrelianceon
AIandreducedcognitiveload,particularlywhentheAIpredictionswerecorrect,
potentially improving overall accuracy. These findings suggest combining mul-
tiple explanation styles to complement each other’s strengths and mitigate their
shortcomings,ultimatelyleadingtothedevelopmentofhybridXAIvisualizations.
3. We show that different levels (low and high) of the Need for Cognition (NFC)
mightnotcapturedifferencesinpeople’saccuracy,cognitiveload,andXAIinter-
faceelementprioritization.Whilepriorstudiesinlesscomplexdomainshaveoften
demonstrateddifferencesinNFClevels,ourresultssuggestthatsuchdistinctions
maydiminishastaskcomplexityincreases.ThesefindingssuggestthatNFCdif-
ferencesmaynotconsistentlygeneralizeacrossdiversedomainsandtasks.Future
studiesshouldexploreabroaderrangeofpersonalitytraitsandconsidermoving
beyondpersonality-basedfactorstofocusonotheruser-centriccharacteristics.
Ourpaperisorganizedasfollows.WefirstreviewpriorworkontheinfluenceofAI
information,explainableAI(XAI)effectiveness,andtheroleofNeedforCognition
(NFC)inAI-assisteddecision-making(Sect.2).Wethenoutlineourhypotheses,fur-
therdetailingthetaskdesign,includingdata,model,instances,andtheAIassistance
withexplanationsinSect.3.Wedescribeourstudydesign,focusingonvariables,sam-
plesize,statisticalanalysis,andtheparticipants’procedureinSect.4.Wepresentthe
resultsinSect.5,beginningwithdescriptivestatisticsandhypothesistests.Thisisfol-
lowedbyposthocandexploratoryanalyses,coveringtask-specificmetrics,interface
understandability,andqualitativefeedback.Next,wediscussthebroaderimplications
of our findings, highlighting study limitations and proposing directions for future
research in Sect. 6. We conclude with key contributions and insights for improving
XAIsystemsinSect.7.Thestudypipelineofdataprocessing,modeltraining,expla-
nationgeneration,andstatisticalanalysisisopenlyavailableathttps://osf.io/j64x8/?
view_only=7f546294a08843acbf204521ba7dee7e.
123

ExploringtheimpactofexplainableAIandcognitive… Page 5 of 43 3
2 Relatedwork
Inthissection,weprovideanoverviewofpreviousworkontheeffectivenessofAI
informationandcurrentexplainableAImethodologiesinrelationtousers,considering
themostcommonmetricsforevaluatingXAIsystemsandhighlightingunderstudied
topics. Then, we summarize previous studies on disaggregating low and high Need
forCognitionparticipantsinAI-assisteddecision-making,focusingonthegapsinthe
currentliterature.
2.1 InfluenceofAIinformationondecisionsupport
Previous studieshave shownthatproviding specificinformationabouttheAIassis-
tantduringdecision-making(i.e.,prediction,confidencescore,andtestsetaccuracy)
strongly influences users’ behaviors and task outcomes. For example, Lai and Tan
(2019)illustratedthatshowingAIpredictedlabelssignificantlyimproveshumanper-
formanceinadeceptiondetectiontask.Theyfoundthat,whenpredictedlabelswere
presented, providing feature-based explanations for the AI’s predictions resulted in
humandecisionaccuracycomparabletothatobtainedwhenparticipantswereexplic-
itlyinformedoftheAI’sstrongperformance.Similarly,Buçincaetal.(2020)found
thatparticipantswhoreceivedAIpredictions(withorwithoutexplanations)provided
moreaccurateanswersthanthosewhodidnotreceiveanyAIassistanceinanutrition-
relateddecision-makingtask.
AnothervaluablepieceofinformationprovidedbytheAIistheconfidencescore,
which refers to provided estimates about the correctness of its outcomes in various
formats,suchasnumericalconfidencescoresorranges(Caoetal.2024a;Bhattacharya
etal.2024a;CauandSpano2025),ortextual/graphicalrepresentations(Padillaetal.
2021;Prabhudesaietal.2023;Zhaoetal.2024;Marusichetal.2024).Inthispaper,
we specifically focus on a binary classification task, where we present AI outputs’
probabilities as numerical confidence estimates in percentage. For example, Zhang
etal.(2020)exploredtheeffectsofAIconfidenceonaccuracyandagreementwithAI
inanincomepredictiontask,findingthatpeopleweremorelikelytofollowtheAI’s
predictionswhentheAIhadhigherconfidence.Nevertheless,theyfoundnoevidence
that AI confidence scores improve the accuracy of AI-assisted predictions. Another
studyfromRechkemmerandYin(2022)studiedtheeffectsofAIconfidence,AIstated
accuracy,andtheirinteractiononusers’propensitytorelyontheAI’sadviceinaspeed
datingeventtask.TheresultsshowedthattheeffectofAIconfidenceonfollowingits
predictionsdependsonpeople’sbeliefinthepresentedAI’sstatedaccuracy:thehigher
the AI confidence, the more accurate people perceive the model to be. The authors
arguethatapossiblereasonfortheseresultsmaylieintheusers’perceptionoftheAI
information,consideringAIaccuracyasafactandAIconfidenceasanestimate(i.e.,
lesstrustworthythanAIperformance).Additionally,Cauetal.(2023a,b)foundthat
lowandhighlevelsofAIconfidenceinpredictionssignificantlyaffectusers’accuracy
andagreementonAI,alsoinfluencingtheeffectivenessofdifferentexplanationstyles
consideringdifferentdomainsandstakesscenarios.
123

3 Page 6 of 43 F.M.Cau,L.D.Spano
AsperAIaccuracyeffectsonusers,wespecificallyfocusonAItestsetaccuracy
(e.g.,accuracyintheheld-outdata,alsocalled“statedaccuracy”).Assuch,Yinetal.
(2019) explored how AI stated accuracy affected people’s agreement with the AI
in a speed dating task. The results show that high stated AI accuracy on held-out
dataincreasespeople’srelianceonAI.Furthermore,relianceisaffectedbybothAI’s
stated accuracy and its observed accuracy (i.e., actual AI accuracy on the observed
instances) during the task, and the effect of stated accuracy can change depending
on the observed accuracy. Rechkemmer and Yin (2022) also found that AI’s stated
accuracy significantlyincreasespeople’s agreement withtheAIandswitchfraction
(i.e.,users’changeopinionafterseeingtheAIprediction)inaseconddateprediction
task.PeoplerelyontheAImodelpredictionsmorewhenitsstatedaccuracyishigher.
Additionally, the impact of the AI’s confidence on people’s belief in its predictions
changes based on the AI’s reported accuracy levels. Similarly, prior works by Kahr
etal.(2023, 2024)alsofoundthatpeople’srelianceonAIishigherwhenpresented
withhigh-accuracyAI,whereusersareaskedtoestimatejailtimefor20legalcases.In
contrast,Heetal.(2023a)foundnosignificanteffectsofAIstatedaccuracyimpacting
users’relianceontheAI(expressedasagreementonAIandswitchfraction)inaloan
predictiontask.
On top of this, how AI assistance is presented also strongly shapes human–AI
decision-making. Although multiple interaction patterns exist (Gomez et al. 2025),
wefocusonthetwomostcommonHuman-CenteredAIparadigms:onestageandtwo
stage. The one-stage AI paradigm delivers AI assistance immediately to the human
decision-maker(Buçincaetal.2021;Rastogietal.2022;Cauetal.2023a,b;Luetal.
2024;Swaroopetal.2025).Whilethisparadigmcanspeeddecisionsandreducecog-
nitiveload,itcanalsocreateananchoringeffectinwhichtheAI’soutputbecomesa
salientreferencepointthatshapestheusers’judgment(Nouranietal.2021;Fogliato
etal.2022b;Maetal.2023;Boonprakongetal.2025).Instead,inthetwo-stageAI
paradigm, the user first gives an initial answer and then receives the AI’s advice to
revise that judgment. HCI research introduced this paradigm as a cognitive forcing
function (i.e., a cognitive intervention to enhance users’ engagement with AI assis-
tance)topromotemoredeliberate,criticalthinking,andofferpotentialimprovements
inaccuracyandappropriaterelianceonAI(Buçincaetal.2021;Heetal.2023a,b;Sal-
imzadehetal.2024;Agudoetal.2024;Morrisonetal.2024;Caoetal.2024b;Küper
etal.2025).However,severalstudieswarnthatperformancegainsmayinsteadreflect
greateralignmentwithAIoutputs,includingalignmentwithincorrectadvice,rather
thangenuineimprovementsinusercriticalthinking(Luetal.2024;Maetal.2024;
Caoetal.2024b).Inourstudy,wespecificallyfocusontheone-stageAIparadigm,as
ourgoalistoassesstheeffectivenessofexplanationswithoutusingcognitiveforcing
approaches. We also test whether this introduces differences in the interpretation of
peoplewithdifferentpropensitiesforenjoyingeffortfulthinking(seeSect.2.3forthe
NeedforCognitiontrait).
Tosummarize,priorresearchconsistentlyhighlightsthatAIconfidenceandaccu-
racy combinations affect users’ reliance on AI during decision-making. We believe
thatwhenusersareexposedtorelativelyhighstatedaccuracy,theAIconfidenceacts
asthetiebreakerinfollowingtheAIprediction:higherconfidenceincreasesthelike-
lihoodofusersfollowingtheAI’ssuggestion.Thus,thisstudyexplorestheimpactof
123

ExploringtheimpactofexplainableAIandcognitive… Page 7 of 43 3
AIinformationonuserrelianceonAI(i.e.,agreementwithAIdecisions),particularly
focusingondifferentlevelsofAIconfidence.Furthermore,sinceusers’cognitiveload
basedonAIassistanceisstillunderexploredinstudiesofAI-assisteddecision-making
(SteyversandKumar2024),wearguethatlowAIconfidencemayelicitahighercog-
nitiveloadinusersthanhighconfidence,forcingthemtoreasonindependentlyrather
thanblindlyfollowingtheAI’sprediction.
2.2 ExplainableAIeffectivenessinAI-assisteddecisions
With the rise of complex black-box AI models, eXplainable AI techniques have
emerged to help users understand how the AI reached a specific decision in low-
and high-stakes situations, including high-uncertainty and safety-critical contexts
(Bertrandetal.2022;Laietal.2023a;Rongetal.2024;Subramanianetal.2024).Pre-
viousstudieshaveshownthatexplanationsmayleadtoincreaseduseraccuracy(Lai
andTan2019;Buçincaetal.2020;Bansaletal.2021;Herm2023)andappropriate
relianceonAI(WangandYin2022;Scharowskietal.2023;Chenetal.2023)when
comparedtoAIpredictionaloneornotshowinganyassistance.Nevertheless,several
studiesonAI-assisteddecisionsexploredexplanationstyledifferencesinincreasing
users’accuracyandappropriatereliance,reportingcontrastingresults.Mostofthese
studiesfocusedonexample-basedandfeature-basedexplanations(Binnsetal.2018;
LaiandTan2019;Caietal.2019a;Zhangetal.2020;Boveetal.2022;FordandKeane
2023;Chenetal.2023;Laietal.2023b),withalimitednumberofstudiesalsoassess-
ing the effects of rule-based and counterfactual explanations (Gajos and Mamykina
2022;WangandYin2022;Tesoetal.2023;CelarandByrne2023;Xuanetal.2025).
Forexample,WangandYin(2022)studiedtheeffectsofdifferentexplanations(i.e.,
featureimportance,featurecontribution,nearestneighbors,andcounterfactuals)ina
recidivismpredictiontaskandfoundthatwhenusershavesomedomainexpertisein
thedecision-makingtask,featurecontributioncansatisfymoredesiderataoftheAI
modelandexplanations(i.e.,understanding,uncertaintyawareness,andtrustcalibra-
tion)regardlessofthecomplexityoftheAImodel.Anotherstudy(Chenetal.2023)
foundthat,foranincomepredictiontask,example-basedexplanationsimprovedpar-
ticipants’taskaccuracywhencomparedwithnoAIassistance,butonlywhentheAI’s
predictionswerecorrect.Instead,whentheAIprovidedwrongpredictions,theauthors
foundatrendoffeature-basedexplanationsincreasingoverreliance.Furthermore,Cau
etal.(2023b)investigatedtheeffectsonAIconfidenceandlogic-styleexplanationsin
astocktradingmarkettask,discoveringthatwhenAIconfidenceishigh,userstendto
over-relyonanerroneousAImorewithinductive(example-based)explanationsthan
abductive(feature-based)anddeductive(rule-based)explanations.
GiventhatmostoftheexistingXAIliteraturehasfocusedonfeature-basedexpla-
nations(Laietal.2023a),andthereisinsufficientevidenceregardingtheirimpacton
users’accuracy,particularlywithtabulardata(Zhangetal.2020;WangandYin2021;
Chenetal.2023;Maetal.2023;Cauetal.2023b;CauandSpano2025),weaimto
investigatewhetherfeature-basedexplanationsimproveusers’accuracycomparedto
123

3 Page 8 of 43 F.M.Cau,L.D.Spano
othertypesofAIassistance(i.e.,noAI;AIwithoutexplanations;AI+example-based
explanations;AI+rule-basedexplanations;andAI+counterfactualexplanations).3
2.3 Needforcognitioninhuman–AIdecisions
Inthiswork,wefocusspecificallyontheNeedforCognition(NFC)trait(Cacioppo
etal1984),givenpreviousstudiessuggestthatindividualdifferencesinNFCcanaffect
people’s interactions with AI assistance and explanations (Millecamp et al. 2019;
Buçincaetal.2021;GajosandMamykina2022;Baheletal.2024).NFCisameasure
thatreflectsthetendencyforanindividualtoundertakeeffortfulcognitiveactivities
(GajosandChauncey2017;Buçincaetal.2021)andbenefitmorefromcomplexuser
interfacefeatures(Carenini2001;CazanandIndreica2014;GajosandChauncey2017;
Ghaietal.2021;GajosandMamykina2022).Previousworkhasshownthatpeople
withhigherNFCaremorelikelytobecuriousandinafocused,attentivestatewhile
usingacomputer(LiandBrowne2006)andhavehigherperformanceatcomplexskill
acquisitioninthecontextofcomputertaskperformance(Dayetal.2007).
Considering explanations in music recommendations (i.e., assisted creation of a
playlist), Millecamp et al. (2019) found that explanations raised the confidence of
userswithalowNFCwhenmakingtheirplaylist.Incontrast,userswithahighNFC
experienced a decrease in their confidence due to explanations. On the contrary, a
follow-up study from Millecamp et al. (2020) did not find an effect of NFC on the
perception of explanations. The authors stated that a potential reason for this result
mightlieintheexplanations’presentationandtheproactiveactivationofexplanations,
which brings out the differences between low and high NFC users. While in the
previousstudy(Millecampetal.2019)explanationshadtobeexplicitlyactivatedby
theusers,inMillecampetal.(2020)explanationswerealwaysvisible.
Concerning NFC effects in the nutrition domain, Buçinca et al. (2021) studied
the impact of cognitive forcing functions (i.e., interventions that disrupt heuristic
reasoning and cause the person to engage in analytical thinking)4 and simple XAI
approaches among low and high NFC participants in an AI-assisted nutrition study
(e.g., making a plate low-carb by changing the ingredients accompanied by AI and
explanations) with a simulated AI. Despite high NFC participants trusting and pre-
ferringcognitiveforcingfunctionslessthansimpleexplainableAIapproaches,they
generally performed better inthetaskthan lowNFCparticipants. Furthermore,low
NFC participants generally found the task significantly more mentally demanding
and the system considerably more complex than high NFC participants. This might
confirmthefindingsfromMillecampetal.(2019, 2020)thatonlycognitiveforcing
functionsproduceintervention-generatedinequalitiesbetweenpeoplebasedontheir
NFClevel.
3 PleaserefertoSect.3.2.4andFig.1foradetaileddiscussionoftheexplanationsusedinourstudy.
4 Aswementionedearlier,inMillecampetal.(2019),explanationshadtobeexplicitlyactivatedbythe
users.Thisisanexampleofcognitiveforcingknownason-demand(Martijnetal.2022;Heetal.2024,
2025;Buçincaetal.2024;CauandSpano2025),whereAIassistanceorexplanationsarenotimmediately
availableandmustbeenabledbyauseraction.
123

ExploringtheimpactofexplainableAIandcognitive… Page 9 of 43 3
AnotherstudyonAI-assistednutritionbyGajosandMamykina(2022)foundthat
explanation-only design (without AI recommendation and before the user decision)
benefitspeoplewithahighNFCmoreintasklearningthanthosewithlowNFC.This
findingcontrastswithpreviousstudies,suggestingthatdifferencesinparticipantswith
diverselevelsofNFCmayemergewithoutusinginterventionslikecognitiveforcing
functions.InthecontextofAI-assistedmazesolving,arecentstudyfromVasconcelos
etal.(2023)investigatedwhetheroverreliancewasaffectedbytheinteractionbetween
participants’NFCscoresandtheAIwithandwithoutexplanationswhenthetaskwas
hardtosolve(boththeAIandexplanationsweresimulated).However,theydidnotfind
anyevidenceforthisinteraction,probablybecausethehardtaskgiventoparticipants
was too difficult to reveal differences across NFC scores. The authors hypothesized
thateventhosewithahighpropensityforeffortfulthinkingarelikelytoover-relyon
AI advice. A more recent work by Cau and Spano (2025) examined how different
levels of NFC (low or high) could influence accuracy and overreliance on AI when
presentedwithon-demandmultifacetedexplanationsinanAI-assistedjobapplication
context,andfoundnodifferencesacrossNFClevels.
Basedonthisbodyofresearch,ourworkaimstodeepentheallegedrequirement
forcognitiveforcingfunctionstohighlightthedifferencesbetweenlowandhighNFC
participants.Specifically,apartfromGajosandMamykina(2022)results,theuseof
interventions to provide explanations to users on-demand or employing two-stage
detectionparadigms(GreenandChen2019a,b;Heetal.2023a;CauandSpano2025;
Buçincaetal.2025)whereusersmaketheinitialdecisionaloneandthenmakeasec-
ondfinalchoicetodecidewhethertoincorporateAIadviceseemstobetheonlyways
toelicitdifferencesinlowandhighNFCparticipants.Additionally,previousstudies
investigatingparticipants’NFCusedsimulatedAIs,alwayscorrectAI’srecommen-
dations,andone/twotypesofsimulatedexplanations.Therefore,weexaminewhether
a difference exists between low and high NFC participants’ decision-making given
differentAIinformationandexplanations(i.e.,prediction,confidence,accuracy,and
explanationstylessuchasexample-based,feature-based,rule-based,andcounterfac-
tual)inacomplex(Salimzadehetal.2023)andhigh-stakesFootnote7loanapplication
scenario,consideringusers’accuracy,cognitiveload,andhowtheyprioritizetheXAI
interfaceinformation.
3 Hypothesesandtaskdesign
In this section, we start describing how we translated our research questions into
hypotheses, studying how AI information and explanations affect decision-making
(RQ1),howindividualswithvaryinglevelsofNeedforCognitionprioritizeinterface
elements(RQ2),andwhethertheseindividualsdifferinaccuracyandcognitiveload
(RQ3).Wethendetailthetaskdesignscenarioemployedtotestthesehypotheses.
123

3 Page 10 of 43 F.M.Cau,L.D.Spano
3.1 Hypotheses
Hypotheses Related to RQ1. As discussed in Sect. 2.1, previous research indicates
that low and high levels of AI confidence and accuracy affect user reliance on AI
in decision-making. Given we showed users a fixed AI accuracy that is relatively
high (i.e., 83% on the test set, see Sect. 3.2.2), we believe that high AI confidence
will lead users to rely more on AI predictions. Conversely, low AI confidence may
encourageuserstothinkindependently,increasingtheircognitiveloadcomparedto
high AI confidence. In Sect. 2.2, we also mentioned that previous work does not
highlight any strong advantages of rule-based and counterfactual explanations over
feature-basedones.Additionally,theefficacyofexample-basedexplanationsprimarily
dependsonthesimilarinstancesretrieved.Giventhatweareconsideringtabulardata,5
presenting similar instances would significantly increase task complexity and thus
users’ cognitive load (Salimzadeh et al. 2023; Cau et al. 2023b), which may lead
them to rely on the most frequent AI prediction across the similar instances (such
as accepting if the majority of similar instances are accepted) rather than carefully
analyzingeachinstanceindividually.Instead,feature-basedexplanations(inourcase,
featurecontribution)provideuserswithanimmediateoverviewofimportantattributes
relevant to the AI’s decision and seem at a glance to satisfy more desiderata for
AI models and explanations (i.e., understanding, uncertainty awareness, and trust
calibration)whenusersaresomewhatknowledgeableaboutthetargetdomain(Wang
and Yin 2022). Although satisfying more desiderata does not imply an increased
accuracyinthetask,wehypothesizethatfeature-basedexplanationsmightleadusers
toachievehigheraccuracythantheotherAIassistanceconditions.Summarizing,we
formulatethefollowinghypotheses:
(cid:129) H1a:UsersexposedtoahighAIconfidencewillrelymoreontheAIprediction
thanusersexposedtoalowAIconfidence.
(cid:129) H1b: Users exposed to a high AI confidence will report a lower cognitive load
thanusersexposedtoalowAIconfidence.
(cid:129) H1c: Users exposed to feature-based explanations will achieve higher accuracy
thaninotherAIassistanceconditions.
HypothesesRelatedtoRQ2.AsnotedinSect.2.3,highNFCindividualsengagemore
witheffortfulactivitiesandcomplexinterfacesthanlowNFCindividuals.Wetherefore
aim to explore which type of information (i.e., applicant details, AI information, or
explanations)participantsprioritizewhenrankinginterfaceelementstomakeafinal
decisionatdifferentlevelsofNFC.Wehypothesizethat,giventhecomplexityofthe
loanpredictiontaskandtheeffortneededtoinspectexplanations,lowNFCindividuals
will assign higher priority to AI information (rank 2) than to explanations (rank 3)
whenmakingtheirfinaldecision.Incontrast,highNFCindividualswillassignhigher
prioritytoexplanations(rank2)overAIinformation(rank3),reflectingtheirtendency
to engage with more complex interface features and attribute greater importance to
explanations.Hence,weformalizedthefollowinghypotheses:
5 Loanapprovaldecisionsarerecordedandcommunicatedusingtablesthatsummarizeapplicantattributes
(e.g.,income,creditscore,andemployment;seeSect.3.2.1).
123

ExploringtheimpactofexplainableAIandcognitive… Page 11 of 43 3
(cid:129) H2a:UserswithalowNFCwillmainlyprioritizetheapplicant’sdetailstomake
theirfinaldecision(rank1),thentheAIinformation(rank2),andlastlytheexpla-
nation(rank3).
(cid:129) H2b:UserswithahighNFCwillmainlyprioritizetheapplicant’sdetailstomake
theirfinaldecision(rank1),thentheexplanation(rank2),andlastlytheAIinfor-
mation(rank3).
HypothesesRelatedtoRQ3.WehypothesizethathighNFCparticipantswillleverage
explanationstogetmoreinsightsabouttheinformationprovidedbytheAI,potentially
achievinghigheraccuracythanthelowNFCones.Additionally,giventheirinclina-
tiontoenjoycomplexcognitiveactivities,highNFCparticipantswillreportalower
cognitiveloadincompletingtheloanapprovaltasks:
(cid:129) H3a: When provided with explanations, users with a high NFC will achieve a
higheraccuracythanuserswithalowNFC.
(cid:129) H3b:Whenprovidedwithexplanations,userswithahighNFCwillreportalower
cognitiveloadthanuserswithalowNFC.
3.2 Taskdesign
Thissubsectiondefineshowweimplementedtheloanapplicationtask,describingthe
dataweused,themodel,instanceselection,andmodelexplanationgeneration.
3.2.1 Data
We built the loan approval task on the publicly available Loan Prediction Problem
Dataset,6consistingof614loanrequestswherethegoalistodecidewhethertoaccept
orrejectaloanapplicationbasedontwelvefeatures.Weoptedforthisdatasetsinceit
reflectsarealisticandfairlycomplexhuman–AIcollaborationscenario(Salimzadeh
etal.2023;Heetal.2023a).Also,theloanpredictionscenariohasbeenusedinother
human–AIteamstudies(Binnsetal.2018;GreenandChen2019b;Gomezetal.2020;
Chromiketal.2021;van Berkeletal.2021;Heetal.2023a; Esfahanietal.2024a;
He et al. 2025), reinforcing its validity and suitability for collaboratively analyzing
interactionsbetweenhumansandAIsystems.Wedecidedtoconvertthenatureofthis
taskfromlow-stakestohigh-stakes7byrewardingparticipantswithamonetarybonus
incaseofcorrectdecisions(Salimzadehetal.2023)(seeSect.4.3).Beforetrainingthe
model,wediscardedtheLoan-IDcolumngivenitslowinformativenessforboththe
userandtheAIinthedecision-makingprocess,resultinginelevenfeatures(excluding
theoutcomeoftheloanrequest,seeFig.1A).
3.2.2 Model
WeusedaRandomForestClassifier(RFC)tosolvetheloanapprovaltask,following
theapproachinChromiketal.(2021).TheRFCwastrainedwith100estimators(trees)
6 https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset.
7 Wedesignedthetaskashigh-stakestoincreaseparticipants’engagementandsimulaterealism,asfinancial
decision-makingintherealworldofteninvolvesconsequences(Salimzadehetal.2023).
123

3 Page 12 of 43 F.M.Cau,L.D.Spano
usingan80:20stratifiedsplitfortrainingandtestsets,achievingatestsetaccuracy
ofabout83%,consistentwiththeirresults.WethenproceededtotheRFCcalibration
phase(SilvaFilhoetal.2023),althoughthemethodswetesteddidnotsignificantly
improvethecalibrationmetrics(seeSect.A.1).Wecomputedthemodelconfidence
estimatesonthetestset,asdescribedinSect.3.2.3.Fromnowon,wewillrefertothe
RFCmodelastheAI.
3.2.3 Instances
Before selecting the instances for the user study, we computed the AI confidence
estimates on the test set using Shannon’s entropy method to extract the epistemic
uncertainty (Shaker and Hüllermeier 2020) and convert it into a confidence score
rangingfrom0to100.Wecomputedthequartilesonthetestsetconfidencescores,
assigninganinstancetoalowconfidenceifitsvaluewasbelow44.3(Q )andahigh
2
confidenceifitsvaluewasabove61.6(Q ).Then,weselectedthefinalinstancesto
3
include in the user study by randomly picking 16 (Candrian and Scherer 2022; He
et al. 2023b; Tsirtsis et al. 2024; Strickland et al. 2024) and balancing them across
AI correctness, confidence, predicted class, and true class (see Table 1). Next, we
randomly split these instances into two groups of eight, balancing the values of the
aforementionedattributes(i.e.,ourcontrolledvariables).Wekeepthefirstgroupfor
practice and the latter for the main session. The final low confidence values were
between 9% and 43%, while high confidence values were between 68% and 85%.
Given the test accuracy of the AI is about 83%, participants’ “observed” accuracy8
will be only 62.5% (i.e., the AI provides correct recommendations in 5 out of 8
instances). We deliberately presented more instances where the AI made incorrect
predictionstoinvestigatewhetherandhowparticipantswouldtendtorelyexcessively
ontheAIsystem.Toaccountfororderingeffects(Nouranietal.2021),weprepared
400randompermutationsforthepracticeandmainsessioninstances,ensuringeach
participantseesdifferentlyorderedloanrequests.
3.2.4 AIassistanceandexplanations
Inthiswork,weassessedtheeffectsofsixAIassistanceconditions(seeFig.1),using
noAIassistanceasabaseline.OneconditionincludedAIinformationwithoutexpla-
nations,incorporatingprediction,confidenceintheprediction,andAIaccuracyonthe
testset.TheremainingfourconditionsaddedexplanationstothisAIinformation,as
detailedbelow.
Example-based.Example-basedexplanationsdonotusuallyprovidedirectinsights
into the internal model functioning in predicting a specific output. Instead, they are
usually employed to show representative prototypes of the AI’s predicted class or
select similar examples (Binns et al. 2018; Cai et al. 2019a; Dodge et al. 2019; Lai
and Tan 2019; Buçinca et al. 2020; Hase and Bansal 2020; Wang and Yin 2021;
Kimetal.2022)thatresembletheexaminedinstance.Anexceptionofthisconcerns
8 Observedaccuracy(62.5%)referstotheactualaccuracytheAIissettoprovidethroughoutthestudyfor
bothpracticeandmainsessions,whichwedonotcommunicatetoparticipants.
123

ExploringtheimpactofexplainableAIandcognitive… Page 13 of 43 3
Table1 Instancesettingsforpracticeandmainsessionsoftheloanpredictiontasks,forwhichtheorder
hasbeenuniquelyrandomizedforeachparticipant
| ID AIcorrectness | AIconfidence | AIprediction | Trueprediction |
| ---------------- | ------------ | ------------ | -------------- |
| 1 Correct        | High         | Reject       | Reject         |
| 2 Correct        | Low          | Reject       | Reject         |
| 3 Wrong          | High         | Reject       | Accept         |
| 4 Correct        | Low          | Accept       | Accept         |
| 5 Correct        | High         | Accept       | Accept         |
| 6 Correct        | Low          | Accept       | Accept         |
| 7 Wrong          | High         | Accept       | Reject         |
| 8 Wrong          | Low          | Accept       | Reject         |
approximatingablack-boxmodeltoasurrogatetransparentmodel(i.e.,TwinSystems
KennyandKeane2019, 2021;FordandKeane2023),wheretheweightsofablack-
boxmodelaretransferredintoatransparentsurrogatesuchasak-NN.Thisway,the
surrogatemodelmimicstheoriginalblack-boxmodelbehaviorandprovidesnearest
neighborinstancesthatalignwiththeoriginalmodeldecisions.Inourstudy,webuilt
example-basedexplanationstakinginspirationfromChenetal.(2023).Weselected
thethreenearestneighborinstancesfromthetrainingsetwiththecloseststandardized
Euclideandistancetothecurrentloanrequesttestinstance,showingtheAIprediction
of the neighbor instances. To reduce the cognitive load on users, we highlight the
neighbor feature values that differ from the given loan request test instance, so that
userscanfocusonthedifferencesbetweeninstances(seeFig.1C,Example-based).
Feature-based. Feature contribution enables users to identify the key attributes
thatsignificantlyinfluencetheAI’soutput,facilitatinginformeddecision-makingand
understandingoftheAI’sbehavior(e.g.,LIMERibeiroetal.2016andSHAPLund-
bergandLee2017).Givenitssolidtheoreticalbackground,andthefaithfulnessand
robustness in the generated explanations (Bodria et al. 2023; Feldkamp and Strass-
burger 2023), we rendered feature-based explanations using the SHapley Additive
exPlanations (SHAP) model-agnostic method (Lundberg and Lee 2017), explaining
the AI’s prediction by showing the Shapley contribution of each feature in favor
(positive sign) or against (negative sign) the AI’s prediction, and presented with an
interactiveverticalbarchart(seeFig.1D,Feature-based).Weusedpurpletorepresent
contributionsofarejectedloanrequestandgreenforanacceptedloanrequest.The
lengthofeachbarindicatesthemagnitudeofthatattribute’scontributionrelativeto
theAIpredictiononthecurrentloanrequest.
Rule-based.Rule-basedexplanationsprovideaseriesof“if-then”statementshigh-
lightingamodel’sdecision-makingprocessthathumanscaneasilyunderstand(Adadi
andBerrada2018;Wangetal.2019;Ribeiroetal.2018;Bodriaetal.2023).Wegener-
atedrule-basedexplanationsviathemodel-agnosticmethodcalledAnchors(Ribeiro
et al. 2018), which defines a rule (set of predicates) so that an instance is assigned
toaspecificclassonlyifallitspredicates(i.e.,featurestestedwiththresholdvalues)
satisfy that rule with a high probability. Anchors also return the precision and the
123

3 Page 14 of 43 F.M.Cau,L.D.Spano
Fig.1 AIassistanceconditionsfortheloanapprovaltasks.Participantscandisplayadditionalinformation
abouttheattributesbyhoveringovertheinfobuttons.A(NoAI)Participantswillseethetask’sgoaland
thecurrentapplicant’sdetails.B(AI)ParticipantswillalsobeassistedbyanAIinthedecision-makingtask
(i.e.,withprediction,confidence,andaccuracy).C(Example-based)Participantswillseecondition“B-AI”
andthethreenearestneighborsofthecurrentapplicant.D(Feature-based)Participantswillseecondition
“B-AI”andtheShapleyfeaturecontributionforeachapplicant’sattribute.E(Rule-based)Participantswill
seecondition“B-AI”andtherulegeneratedbyAnchor.F(Counterfactual)Participantswillseecondition
“B-AI”andthreecounterfactualinstancesgeneratedbyDiCE
coverage of the extracted rule. The precision indicates how well an anchor predicts
the model’s output. A high precision value suggests that the anchor is a good pre-
dictor of the output variable, while a low precision value highlights that the anchor
is a poor predictor. Instead, coverage measures how many examples in the dataset
arecoveredbytheanchor.Ahighcoveragevalueindicatesthattheanchorisagood
representativeofthedataset,whilealowcoveragevaluemeanstheanchorisapoor
representative. When generating the rules, we set the precision threshold constraint
to95%(i.e.,findingtheanchorthatmaximizesthecoveragegiventhethreshold).We
show participants the extracted rule in a tabular form, where each row represents a
predicatewhichafeatureistestedagainstathresholdvalue.Additionally,weadded
123

ExploringtheimpactofexplainableAIandcognitive… Page 15 of 43 3
twocolumnsshowingtheprecisionandcoverageofthegeneratedrule(seeFig.1E,
Rule-based).9
Counterfactual. Counterfactual explanations provide contrastive “what-if” state-
ments that help users understand what changes could be made to achieve a desired
output(Wachteretal.2017;AdadiandBerrada2018;Mothilaletal.2020a).Webuilt
counterfactual explanations using the Diverse Counterfactual Explanations (DiCE)
framework(Mothilaletal.2020b)foritseffectivenessinprovidingdiverseandaction-
ablecounterfactualexplanations(Mothilaletal.2021;Moreiraetal.2022).Givena
testinstance,DiCEgeneratescounterfactualexplanationsthatemphasizediversityand
deliveramorecomprehensiveunderstandingofthemodel’sbehavior,providingmul-
tiplecounterfactualsthatarediverseintermsofthechangesmadetotheinputfeatures.
Followingthelineofexample-basedexplanations,weshowusersthreecounterfactual
explanationsgeneratedfromagivenloanrequesttestinstance.Similarly,wehighlight
thecounterfactualfeaturevaluesthatdifferfromthegivenloanrequesttestinstanceto
reduceusers’cognitiveloadandletthemfocusonthedifferencesbetweeninstances
(seeFig.1F,Counterfactual).
4 Studydesign
Ourstudyfollowedamixed-factorialdesign,whereweaskedparticipantstodecide
whethertoacceptorrejectaseriesofloanrequests(seeTable1).Weinitiallymeasured
participants’NFCanddividedthemintolowandhighgroupsbasedonthedistribution
median.Next,weassignedeachparticipanttooneoftheAIassistanceconditionsas
abetween-subjectsfactor(i.e.,noAI;AIwithoutexplanations;AI+example-based
explanations; AI + rule-based explanations; and AI + counterfactual explanations).
Also,westudiedtheeffectsofthefollowingwithin-subjectscovariates:AIconfidence
(lowandhigh),andAIcorrectness(correctandwrong).First,participantscompleted
a practice session of eight loan requests to familiarize themselves with the task and
the assigned AI assistance condition. Next, they completed the main session of the
studywithanothereightloanrequests.
Thissectionoutlinesthevariables,plannedsamplesize,statisticalanalysis,andthe
procedurefortheuserstudyweconductedtotestourhypotheses.
4.1 Variables
For the hypothesis test, we considered the following measurements collected in the
mainsessionoftheuserstudy.Wecollectedthefollowingindependentvariables:
(cid:129) AIassistance(between-subjects,categorical).Wecreatedsixscenariosthatvaried
in terms of assistance provided by the AI and explanations to the participants
duringtheirdecision-makingprocess.
9 Participantscouldviewdetailedinformationabouttheoperator,precision,andcoverageattributesatany
timeduringthestudybyhoveringtheinfobuttonnexttoeachattribute.Theseconceptswerealsoexplained
indetailbeforethepracticesession.
123

3 Page 16 of 43 F.M.Cau,L.D.Spano
– NoAI.Weshowedparticipantstheloanrequestattributesandaskedwhether
itshouldbeacceptedorrejected.
– AI. We showed participants the information in the No AI condition and the
followingAIinformation:(i)predictionforthecurrentloanrequest,(ii)pre-
dictionconfidence,andiii)accuracyonthetestset.
– Example-based. Weshowedparticipants theinformationintheAI condition
andthreenearestneighborinstancesofthecurrentloanrequest.
– Feature-based. We showed participants the information in the AI condition
andtheSHAPfeaturecontributionforeachloanrequestattribute.
– Rule-based.WeshowedparticipantstheinformationintheAI conditionand
theAnchorruleforthecurrentloanrequest.
– Counterfactual. We showed participants the information in the AI condition
andthreeDiCE-generatedcounterfactualinstancesbasedonthecurrentloan
request.
(cid:129) Need for cognition (between-subjects, categorical). NFC is a stable personality
trait that reflects how much a person enjoys engaging in cognitively demanding
activities(Cacioppoetal1984).Wemeasuredparticipants’NFCusingthesix-item
NeedforCognitionScale(NCS-6)definedindeHolandaCoelhoetal.(2020)(see
Sect.Afordetails).WesplitparticipantsintolowandhighNFCbycomputingthe
medianoftheNFCscoredistribution,thesamecriteriausedinpreviousworkon
AI-assisteddecisions(Buçincaetal.2021, 2024, 2025;Conatietal.2021;Bahel
etal.2024;CauandSpano2025).
Wemeasuredtheireffectsonfourdependentvariables:
(cid:129) Accuracy (categorical). We measured participants’ accuracy as whether each
accept/rejectdecisionforaloanmatchedtheinstance’sgroundtruth(i.e.,wrong
orcorrect).
(cid:129) Reliance (categorical). We measured participants’ reliance on AI by assessing
whether a participant agreed or disagreed with the AI prediction (i.e., agree or
disagree).
(cid:129) Interfacecomponentsimportance(ranking).Wemeasuredtheimportanceofinter-
faceelementsforparticipantsindeterminingtheirfinalchoice,includingtheloan
request,theAIinformation,andtheexplanation,measuredasaranking.Partici-
pantsrespondedtothestatement:“Pleaserankthefollowinginformationinterms
ofhowimportantitwasforyouinmakingyourfinaldecision:(a)loanattributes,
(b)AIinformation,(c)explanation.”
(cid:129) Cognitiveload(numerical).Weassessedhowdifficultparticipantsfoundthetasks
using the Single Ease Question (SEQ) (Sauro and Dumas 2009) 7-point rating
scale,rangingfrom“1-Veryeasy”to“7-Verydifficult.”
Wealsocollectedthefollowingcovariates(seeTable1):
(cid:129) AI confidence (within-subjects, categorical). Participants saw loan requests with
eitherloworhighAIconfidence.
(cid:129) AIcorrectness(within-subjects,categorical).Participantssawloanrequestswith
correctorwrongAIpredictions.
123

ExploringtheimpactofexplainableAIandcognitive… Page 17 of 43 3
Finally, we collected other descriptive and exploratory measurements to provide
contextforourstudyandenablefurtherexploratoryanalysestomotivateourhypothe-
ses:
(cid:129) Demographics (categorical). We gathered participants’ information on their sex
andagefromtheProlificplatform.
(cid:129) Familiaritywiththetask(categorical).Weaskedparticipantsabouttheirfamiliarity
with loan request approval with the following statements using a 5-point Likert
scalerangingfrom“1-Noexperience”to“5-Highlyexperienced”:
– “Doyouhaveanyexperiencewithloanrequestapproval?”
– “DoyouhaveanyexperiencewithAI-assistedloanrequestapproval?”
(cid:129) AIinformationimportance(ranking).Weaskedparticipantstoranktheimportance
oftheAIprediction,confidence,andaccuracyintheconditionsthatincludethe
AIinformationbyasking:“PleaserankthefollowingAIinformationintermsof
howimportantitwasforyouinmakingyourfinaldecision:(a)AIprediction,(b)
AIconfidence,(c)AIaccuracy.”
(cid:129) XAIinterfaceunderstanding(numerical).Attheendofthesurvey,weaskedpar-
ticipants to state their easiness of understanding the loan application attributes,
AI information, and explanations using a 5-point Likert scale ranging from ”1 -
Stronglydisagree”to”5-Stronglyagree”inthreeitems(i)“Theloanapplication
attributeswereeasytounderstand,”(ii)‘TheAIinformationprovidedwaseasyto
understand,”and(iii)“TheAIexplanationprovidedwaseasytounderstand.”
(cid:129) Textualfeedback (opentext).Attheendofthesurvey,wecollectedparticipants’
feedbackabouttheexplanations(whenpresented)byasking:“Whatwerethepros
andconsoftheAIexplanationsyouencountered?”
4.2 Plannedsamplesizeandstatisticalanalysis
Before recruiting participants, we estimated the required sample size for our study
using G*Power software (Faul et al. 2009), resulting in 286 participants. This rec-
ommendedsamplesizeismotivatedbythemaximumnumberofparticipantsneeded
amongthehypotheses,whichwedescribeindetailasfollows.Sinceweareassessing
fivehypotheseswithmixedmodels(continuous/categoricaldependentvariables)and
twobasedonrankinginformation(usingtheFriedmantest),wedecidedtoapplytwo
different thresholds, using α = 0.05 = .01 for mixed models and α = 0.05 = .025
5 2
forrankingtests.Thus,weconsideredassignificantthep-valuesbelowthesereduced
thresholds in the analysis. Additionally, we assigned a randomly generated seed to
each user as a (i) random intercept to account for the variability of the dependent
variablesacrossdifferentclustersinthemixed-effectslogisticregressionandasa(ii)
within-clustercorrelationeffectonthedependentvariableintheGeneralizedEstima-
tionEquation(GEE)models.Allthemodelsconvergedsuccessfully.
ToanswerH1aandH1cwithcategoricaldependentvariables,weusedtwomixed-
effects logistic regression models with Reliance and Accuracy as the dependent
variables, assessing the main effects of AI assistance as the independent variable,
andAIconfidenceandAIcorrectnessascovariates.Wecomputedtherequiredsample
123

3 Page 18 of 43 F.M.Cau,L.D.Spano
size using G*Power for a mixed-effects logistic regression model (a priori χ2 test)
withmediumeffectsize(Cohen’sd =0.25),adesiredpowerof0.8,Df=5,andtwo
covariates(AIconfidenceandAIcorrectness),resultingin286participants.10Instead,
toanswerH1bwhichinvolvesanumericdependentvariable,weusedaGeneralized
EstimationEquation(GEE)modelwithCognitiveload asthedependentvariableto
assess the main effects of the AI confidence covariate while also studying potential
impactsoftheAIassistanceasanindependentvariableandAIcorrectnessasacovari-
ate. We computed the required sample size using the G*Power for a mixed-design
ANCOVA,mediumeffectsize(Cohen’s f =0.25),adesiredpowerof0.8,Df=1,and
twocovariates(AIconfidenceandAIcorrectness),resultingin191participants.
ToanswerH2,weconductedaFriedmantest(Friedman1937, 1940)withInterface
componentimportancerankedmeasurementsasthedependentvariabletoassessthe
mainandinteractioneffectsofNeedforCognition(lowandhigh)astheindependent
variable.WecomputedtherequiredsamplesizeusingG*Powerforawithin-subjects
FriedmanTestwithmediumeffectsize(Cohen’s f =0.16),adesiredpowerof0.8,one
group,andthreemeasurements(i.e.,loanapplicationattributes,AIinformation,and
explanation),resultingin100participants.ToestablishtherankingorderamongXAI
interfaceelements,weconductedaNemenyiposthocanalysiswhenwediscovered
significantfactorsintheFriedmantest.
ToanswerhypothesisH3awithacategoricaldependentvariable,weusedamixed-
effectslogisticregressionmodelwithAccuracyasthedependentvariabletostudythe
maineffectsofNeedforCognitionastheindependentvariable.Wealsoinvestigated
the impact of AI assistance as an independent variable and AI confidence and AI
correctnessascovariates.WecomputedtherequiredsamplesizeusingtheG*Power
foramixed-effectslogisticregressionmodel(aprioriχ2test)withmediumeffectsize
(Cohen’sd =0.25),adesiredpowerof0.8,Df=1,andtwocovariates(AIconfidence
and AI correctness), resulting in 187 participants. Instead, to answer H3b, which
involves a numeric dependent variable, we used a Generalized Estimation Equation
(GEE)modelwithCognitiveloadasthedependentvariabletoassessthemaineffects
ofNeedforCognition.Further,wealsoinvestigatedtheimpactofAIassistanceasan
independentvariable,andAIconfidenceandAIcorrectnessascovariates.Wecomputed
therequiredsamplesizeusingtheG*Power foramixed-designANCOVA,medium
effectsize(Cohen’s f =0.25),adesiredpowerof0.8,Df=1,andtwocovariates(AI
confidenceandAIcorrectness),resultingin191participants.
4.3 Procedure
Toverifyourhypotheses,weconductedanonlineuserstudyusingtheProlificplat-
form,11wherewerecruitedparticipantsaged18orolderwithhighEnglishproficiency
and approval rates between 95 and 100. Participants were then redirected to the
LimeSurveytool12wheretheycompletedthestudyinthreesteps.Participantsreceived
10 WhileH1aandH1brequirearound191participants(Df=1)forlowandhighAIconfidencelevels,H1c
increasesthenumberofparticipantsgiventhatwetestedallsixAIassistanceconditions(Df=5).
11 https://www.prolific.com/.
12 https://www.limesurvey.org/.
123

ExploringtheimpactofexplainableAIandcognitive… Page 19 of 43 3
Fig.2 Illustrationoftheprocedureparticipantsengagedinduringourstudy
£2.7asarewardforthestudy,withanaveragecompletiontimeof18min(i.e.,£9/h,
whichisconsideredafairpaymentforProlific).Prolificautomaticallytimedoutpar-
ticipantsafter60min.Werewardedparticipantswithanextra£0.12foreachcorrectly
classifiedloanrequestofthemainsession.Weonlyincludedparticipantsintheanaly-
sisiftheypassedallfiveattentionchecks.ThestudyhasbeenapprovedbytheEthics
CommitteeoftheUniversityofCagliari.13
Participantswentthroughthefollowingsteps,illustratedinFig.2.First,theyread
adocumentcontainingabriefstudydescription,filledoutaninformedconsentform,
and completed an attention check14 Next, they stated their familiarity with the task
and completed another attention check. Then, we asked participants to fill out the
six-itemNeedforCognitionScale(deHolandaCoelhoetal.2020)andtocomplete
anotherattentioncheck.Weintroducedparticipantstothetaskandassignedthemto
one of the six AI assistance conditions (i.e., no AI; AI without explanations; AI +
example-based explanations;AI+rule-basedexplanations;andAI+counterfactual
explanations)whilebalancingtheparticipationamongconditions.Beforestartingthe
practicesession,weprovidedparticipantswithdetailsabouttheassignedAIassistance
condition,wheretheycompletedanotherattentioncheck.Then,participantscompleted
eightloanrequesttasksasapracticesession,wheretheyneededtodecidewhetherto
acceptorrejecttheapplications.Aftereachdecision,participantsreceivedfeedback
ontheiranswers,wherewerevealedthecorrespondingtrueclass.Whenparticipants
finishedthepracticesession,weshowedthemapageasareminderforthemaintask
session, resulting in a compensation bonus in case of correctly classifying a loan.
Beforestartingthemainsession,participantscompletedthelastattentioncheck.
Participantscompletedeightloanrequesttasks,withthesameAIassistancecondi-
tionassignedinStep2butwithoutreceivingfeedbackonthetrueclass.Foreachtask,
wemeasuredparticipants’cognitiveload.Wealsoaskedthemtoranktheimportance
oftheinterfacecomponents(seeSect.4.1)exceptinthe“NoAI”and“AI”conditions.
Finally,weaskedparticipantstostatetheireaseofunderstandingoftheXAIinterface
elements (i.e., loan application attributes, AI information, and explanation) and to
providetextualfeedbackabouttheprosandconsoftheexplanationstheyencountered
(seeSect.4).
13 ReceivedonJuly25,2024,Prot.0205640.
14 WeuseInstructionalManipulationChecks(IMCs),wheretheanswertoeachattentioncheckisexplicitly
reportedinthequestiontextandfollowsthegoodpracticesofProlific.https://researcher-help.prolific.com/
en/article/fb63bb.
123

3 Page 20 of 43 F.M.Cau,L.D.Spano
5 Results
5.1 Descriptivestatistics
The final sample of 288 participants comprised 144 males and 144 females, aged
between 18 and 74 (M = 32.42, SD = 10.95). Participants reported low familiarity
with the loan application task (M = 1.83, SD = 0.99, 5-point Likert scale, 1: no
experience,5:highlyexperienced)andAI-assistedloanrequestapproval(M =1.32,
SD = 0.71, 5-point Likert scale, 1: no experience, 5: highly experienced). Overall,
participantsreportedagoodeasinessinunderstandingtheloanapplicationattributes
(M =3.72,SD=0.93,5-pointLikertscale,1:stronglydisagree,5:stronglyagree),
AI information (M = 3.74, SD = 0.95, 5-point Likert scale, 1: strongly disagree,
5: strongly agree), and explanations (M = 3.67, SD = 1.00, 5-point Likert scale, 1:
strongly disagree, 5: strongly agree). The NFC subdivision into low (143) and high
(145)individualswasachievedwithacomputedmedian Mdn =3.50(M =3.48and
SD=0.76).Figure8inAppendixshowsthecontinuousvaluesoftheNFCdistribution.
GiventhedistributionsforlowandhighNFCwerenon-normal(Shapiro–Wilk:low,
W = 0.915, p < .0001; high W = 0.888, p < .0001) and that homogeneity of
variances was unequal (Levene’s test: F = 23.2, p < .0001), we used a Wilcoxon
rank-sum test, which confirmed a significant difference between low and high NFC
groups (W = 0, p < .0001). The between-subject design and NFC variables were
overallhomogeneousintermsofdemographicsandfamiliarity.15 Wefurtherdiscuss
differencesintheparticipants’understandingoftheinterfacecomponents(i.e.,loan,
AIinformation,andexplanations)inSect.5.3.1.
5.2 Hypothesistests
5.2.1 H1:EffectsofAIandexplanationsonusers’relianceonAI,cognitiveload,and
accuracy
TheresultingchartsforH1aredepictedinFig.3.ForH1a,weusedamixed-effects
logisticregressionmodeltoexaminethedifferencesinusers’relianceonAI,consider-
inglowandhighAIconfidence.Theresultsoftheanalysisshowedasignificanteffect
(Log-Odds=1.22,Std.error=0.12,z-value=10.40, p<.01)ofhighAIconfidence
inincreasingusers’relianceonAIthanlowAIconfidence.Hencewerejectthenull
hypothesis for H1a, as users rely more on the AI when exposed to high AI confi-
dencethanlowconfidence.InH1b,westudiedthedifferencesinusers’cognitiveload
betweenlowandhighAIconfidenceusingaGeneralizedEstimationEquation(GEE)
15 AKruskal–WallistestwasconductedtocomparefamiliarityscoresacrossdesignandNFCgroups.The
resultsindicatednosignificantdifferencesinfamiliarityconsideringthedesignvariable(familiarity:χ2=
5.74,p=.33;familiarityAI:χ2=9.2,p=.1).WeobservedsimilarresultsacrossNFCgroups,exceptfor
taskfamiliarity(χ2=4.79, p=.03),whichwashigherforhighNFCindividuals(M=1.97,SD=1.06),
comparedtolowNFCindividuals(M =1.69,SD=0.89).ForfamiliaritywithAI(χ2 =1.5, p=.22),
thedifferencewasnotsignificant(highNFC:M=1.36,SD=0.75;lowNFC:M=1.28,SD=0.68).We
thusrepeatedtheanalysisforhypothesesH3aandH3b,addingfamiliarityasacovariateforpotentialmain
effectsandinteractionsforNFCandfamiliaritywiththetask.However,nosignificantresultswerefound.
123

ExploringtheimpactofexplainableAIandcognitive… Page 21 of 43 3
Fig.3 EffectsoflowandhighAIconfidenceconsideringrelianceonAI(H1a),cognitiveload(H1b)(ticks
abovebarsindicatelowerandhigherconfidenceintervalsbasedonstandarderrors),andusers’accuracy
(H1c)dividedbyAIassistanceconditions.Theasteriskshighlightp-valuesignificancestrength(***p<
.001)
model. The results of the analysis showed a significant effect (Log-Odds = −0.41,
Std.error =0.06,Wald =54.57, p<.01)ofhighAIconfidenceindecreasingusers’
cognitiveloadcomparedtolowAIconfidence.Hence,werejectthenullhypothesis
forH1b,concludingthatusersreportlowercognitiveloadwhenexposedtohighAI
confidencecomparedtolowconfidence.ForH1c,weinvestigatedtheusers’accuracy
differencesamongAIassistanceconditionsusingamixed-effectslogisticregression
model.Theresultsoftheanalysisshowednosignificanteffects(Log-Odds=0.34,Std.
error =0.16,z-value=2.11, p=.0349)offeature-basedexplanationsovertheother
interfaceconditionsonusers’accuracy;hence,wefailtorejectthenullhypothesisfor
H1c16.
5.2.2 H2:EffectsoflowandhighNFCparticipantsonXAIinterfaceinformation
importance
TotestH2(seeFig.4),weincludedonlyparticipantsexposedtoexplanations,resulting
in192users.ForH2a,wehypothesizedthatlowNFCparticipantswouldgivepriority
totheAIinformation(rank2)immediatelyaftertheloanattributes(rank1),keeping
theexplanation(rank3)asalastresort.TheFriedmantestforH2ashowsasignificant
difference (χ2 = 159, df = 2, p < .025) between the three XAI interface elements
wheninvestigatinglowNFCparticipants.Thepairwiserankingcomparisonsusingthe
Nemenyi(p < .025)showthatusersprioritizetheloanattributes(rank1),followed
bytheexplanation(rank2)andtheAIinformation(rank3)whenmakingtheirfinal
decision. In this light, we fail to reject the null hypothesis for H2a. For H2b, the
Friedmantestshowsasignificantdifference(χ2=324,df =2,p<.025)betweenthe
threeXAIinterfaceelementswheninvestigatinghighNFCparticipants.TheNemenyi
pairwise ranking comparisons (p < .025) align with our hypothesis, showing that
usersprioritizetheloanattributes(rank1),followedbytheexplanation(rank2)and
16 Althoughtheresultdidnotmeettheα=.01threshold,counterfactualexplanationsweretheonlyother
explanationtype,besidesfeature-basedexplanations,toshowaneffectonimprovingusers’accuracy(Log-
Odds=0.39,Std.Error=0.16,z=2.43,p=.0149).PosthocpairwisecomparisonsusingTukeyHSDdid
notshowsignificantdifferencesacrossAIassistanceconditions.
123

3 Page 22 of 43 F.M.Cau,L.D.Spano
Fig.4 XAIinterfacecomponentsrankfrequenciesforlow(H2a)andhigh(H2b)NFCindividuals.The
asteriskshighlightp-valuesignificantstrength(***p<.001)
the AI information (rank 3) when making their final decision. Hence, we reject the
nullhypothesisforH2b.
5.2.3 H3:EffectsoflowandhighNFCparticipantsonaccuracyandcognitiveload
For H3a (see Fig. 5), we investigated whether high NFC individuals may achieve
increasedaccuracywhenexposedtoexplanationscomparedtolowNFCindividuals.
The results of the mixed-effects logistic regression analysis showed no significant
effects (Log-Odds = 0.03, Std. error = 0.10, z-value = 0.28, p = .78) among low
and high NFC participants. Hence, we fail to reject the null hypothesis for H3a. In
H3b,westudiedthedifferencesinusers’cognitiveloadbetweenlowandhighNFC
participantswhenexposedtoexplanationsusingaGeneralizedEstimationEquation
(GEE)model.Theresultsoftheanalysisshowednosignificanteffects(Log-Odds=
−0.08,Std.error =0.12,Wald =0.51, p=.47)forhighNFCparticipantscompared
tolowNFCparticipants.Hence,wefailtorejectthenullhypothesisforH3b.17
5.3 Posthocandexploratoryanalyses
Thehypothesesresults(seeTable2)revealedthathighAIconfidenceincreasesreliance
onAIandreducescognitiveload.Additionally,therewerenosignificantdifferencesin
users’accuracyamongthedifferentAIassistanceconditions.Consideringtheinterface
component preferences, low and high NFC participants ranked loan attributes first,
explanationsecond,andAIinformationthird.Finally,noaccuracyorcognitiveload
differencesbetweenlowandhighNFCindividualswerefound.
TofurtherclarifytheroleofAIandexplanationsinshapinguserbehavior,wecon-
ductedadditionalanalysesconsideringtheinteractioneffectsbetweencovariates(AI
confidenceandcorrectness)andexplanations,furtherclarifyingtheroleofAIinfor-
mationinusers’prioritizationofXAIinterfaceelements’ranking.Wefirstexamined
17 Forcompleteness,wealsorepeatedthesameteststoexaminetheimpactofNFCwiththeoriginal
continuousvalues,findingnosignificantresultsforH3aandH3b.
123

ExploringtheimpactofexplainableAIandcognitive… Page 23 of 43 3
Fig.5 Users’accuracy(H3a)andcognitiveload(H3b)disaggregatedbylowandhighNFC(ticksabove
barsindicatetheStandardError)
Table2 Summaryresultsofourhypotheses
Hypotheses Supported
H1a:UsersexposedtoahighAIconfidencewillrelymoreonthe ✓
AIpredictionthanusersexposedtoalowAIconfidence
H1b:UsersexposedtoahighAIconfidencewillreportalower ✓
cognitiveloadthanusersexposedtoalowAIconfidence
H1c:Usersexposedtofeature-basedexplanationswillachieve ✗
higheraccuracythanotherAIassistanceconditions
H2a:UserswithalowNFCwillmainlyprioritizetheapplicant’s ✗
detailstomaketheirfinaldecision(rank1),thentheAI
information(rank2),andlastlytheexplanation(rank3)
H2b:UserswithahighNFCwillmainlyprioritizetheapplicant’s ✓
detailstomaketheirfinaldecision(rank1),thentheexplanation
(rank2),andlastlytheAIinformation(rank3)
H3a:Whenexplanationsareshown,userswithahighNFCwill ✗
achieveahigheraccuracythanuserswithalowNFC
H3b:Whenexplanationsareshown,userswithahighNFCwill ✗
reportalowercognitiveloadthanuserswithalowNFC
how AI confidence influences users’ interpretation of explanations by considering
metricssuchasaccuracy,relianceonAI,andcognitiveload.Wethenreassessedthese
metricsbyconsideringAIcorrectnesstoinvestigatepotentialoverreliancebehaviorin
AIwhenusersinteractwithexplanations.Additionally,giventhesignificantimpactof
highAIconfidenceonincreasingusers’relianceonAI,weevaluatedhowitimpacted
users’ prioritization of the XAI interface elements (i.e., loan attributes, AI informa-
tion,andexplanation)andwhetheritaffectedusers’rankingofAIinformation(i.e.,
prediction,confidence,andaccuracy).Lastly,wefocusedonhowlowandhighNFC
usersrankedtheAIinformation(i.e.,prediction,confidence,andaccuracy),wherewe
consideredonlytheAIassistanceconditionincorporatingexplanations.
123

3 Page 24 of 43 F.M.Cau,L.D.Spano
The results from the first analysis show no significant interactions between AI
confidence and explanations of users’ reliance on AI, cognitive load, and accuracy
(seeFig.9inAppendix).18 Instead,wefoundmultiplesignificantresultswhencon-
sideringtheAIcorrectnessandexplanationinteractions(seeFig.6-A).Forreliance
onAI,counterfactualexplanationinteractionwithAIcorrectpredictionsleadstoan
increaseinreliance(Log-Odds=0.98,Std.error =0.35,z-value=2.79, p =.0051).
The cognitive load results for counterfactual explanations and interaction with AI
correctness(Log-Odds=−0.48,Std.error =0.14,Wald =10.91, p=.0009)showa
decreaseinusers’cognitiveload.Thesefindingssuggestthatpresentingcounterfactual
explanationsreducesthecognitiveloadwhenAIpredictionsarecorrect.Additionally,
suchexplanationsencourageuserstofollowcorrectpredictions,potentiallymitigating
overrelianceonAI.
Interestingly,users’accuracyfindingshighlightatrendforAIcorrectpredictions
interacting with counterfactual explanations (Log-Odds = −0.84, Std. error = 0.34,
z value = −2.47, p < .0133) in decreasing accuracy. Additionally, counterfactual
explanations(Log-Odds=0.87,Std.error=0.27,z-value=3.17, p=.0015)leadtoan
increaseinaccuracy.Theseresultsmightindicateanuancedtrade-off:counterfactual
explanationsimprovedecision-makingoverallbutcansometimesconfuseuserswhen
AIpredictionsarealreadycorrect.
The results of splitting XAI interface information by AI confidence (see Fig. 10
in Appendix and Fig. 6B) show a significant difference between the three interface
componentsforlowconfidence(χ2=301,df =2, p <.025).TheNemenyipairwise
comparisonsshowasignificantdifference(p < .025)betweenloanattributes(rank
1)withAIinformationandexplanation.Instead,therearenodifferencesbetweenAI
information and explanation. We also have a significant difference among the three
interface components for high AI confidence (χ2 = 196, df = 2, p < .025). The
Nemenyi pairwise comparison results (p < .025) show that participants prioritize
the loan attributes (rank 1), followed by the AI information (rank 2), and then the
explanation(rank3).Finally,wefoundnorankingdifferencesamongAIprediction,
confidence, and accuracy when considering low AI confidence. Instead, the results
forhighAIconfidencehighlightadifferenceamongtheAIinformationelements(χ2
= 17.3, df = 2, p < .025). The Nemenyi pairwise comparisons (p < .025) reveal
asignificantdifferencebetweenAIpredictionandbothAIconfidenceandaccuracy,
whilenosignificantdifferenceisobservedbetweenAIconfidenceandaccuracy.
Inthesecondanalysis,werepeatedtheFriedmantestfocusingontheAIprediction,
confidence, and accuracy ranking, considering low and high NFC participants. The
results for low NFC participants show a significant difference between AI informa-
tion provided (χ2 = 13.2, df = 2, p < .025). The Nemenyi pairwise comparisons
(p < .025) reveal a significant difference between AI prediction and AI accuracy.
However,nodifferencesemergewhenconsideringAIconfidenceincomparisontoAI
prediction and accuracy. Instead, the Friedman test for high NFC participants high-
lightsnosignificantdifferencesamongAIprediction,confidence,andaccuracy.This
mayhintthatlowNFCusersseemtofocusmoreontheAIprediction,whichisrein-
18 Althoughitfallsoutsidethescopeofourhypotheses,itisimportanttonoticethathighAIconfidence
significantlyincreasesusers’accuracy(p<.01).
123

ExploringtheimpactofexplainableAIandcognitive… Page 25 of 43 3
Fig.6 PosthocanalysesresultsforAAIcorrectnessinteractionwithAIassistance,andBrankingforlow
andhighAIconfidencewithAIinformationimportanceofinterfaceelements.Theconnectionsbetween
rowspresentpvaluesandthedirectionoftheeffect(e.g.,adownwardarrowforadecreaseintheconnected
dependentvariable;forrankings,wedisplaytheexactpositionofeachinterfaceelementbasedonpairwise
comparisons)
forcedbyAIconfidence,whilehighNFCpeopleseemtolookattheAIinformation
asawhole.
5.3.1 Participants’interfaceunderstandabilityandqualitativefeedback
Thissectionsummarizesusers’understandingoftheinterfacecomponentsandtextual
feedbackonexplanationtypeswecollectedfromtheuserstudy,highlightingsubjective
perspectivesandperceivedprosandconsfromusersaboutexplanations.
Thechartdepictingusers’overallunderstandingofloanattributes,AIinformation,
andexplanationsisshowninFig.7.Wenoticethat,ingeneral,counterfactualexpla-
nationsdecreaseoverallunderstandingofinterfacecomponents.Wethenconducted
astatisticalanalysistounderstand ifthesedifferences aremerelyvisualtrendsorif
thereisindeedasignificantdifference.Giventhenon-normalnatureoftheinterface
components’ distributions,weoptedforanonparametricKruskal–Wallistest,using
theabovevariablesasdependentvariablesandthedesignastheindependentvariable.
Although there were no differences for loan understanding among conditions, we
foundsignificantdifferencesforAI(χ2=9.76,df =4, p =.045)andexplanation(χ2
=9.92,df =3, p =.019)understanding.Weperformedapairwisecomparisonusing
aDunntestwithBonferroniforp-valueadjustment.Wefoundadifferencebetween
AI (without explanations) and counterfactual conditions (z = −2.88, p = .0389) for
123

3 Page 26 of 43 F.M.Cau,L.D.Spano
Fig.7 Users’understandingofloanattributes,AIinformation,andexplanationsbyAIassistanceconditions
theAIinformationunderstandingandanotherdifferencebetweenfeature-basedand
counterfactualconditions(z=−3.018,p=.0152)intheexplanationunderstanding.
Consideringusers’feedbackonexplanations,11participantsreportedthatexample-
basedoneswereeasy,understandable,andafastwaytocompareapplications.Assuch,
P16said:“[explanation]washelpfulonceunderstoodalltheattributedetails”.On
thecontrary,11participantssaidthatexplanationslackeddetailsandthatitwashard
totrustthemfully.P73stated:“[explanation]madeiteasyformakingadecisionbut
notsureabouttheirreliability”.
Feature-based explanations were perceived by 8 participants as helpful and pro-
vidingclarityforthedecision-making.P75stated:“explainwelltherationalebehind
accepting or rejecting the loan”. However, 10 participants reported needing more
insightintowhyspecificweightswereassignedtoattributes.Assuch,P79said:“The
explanationneededmoreinsightsabouthowtheweightsweregenerated”.
Twelveparticipantsperceivedrule-basedexplanationsasusefulandeasytounder-
stand, providing good guidance in decision-making. For example, P22 said: “The
explanationhelpedmedecidewhethermyevaluationoftheloanapplicationismore
orlesscorrectornot”.Despitethis,12participantsstatedtheseexplanationslacked
understandability,highlightingtheabsenceof“reasoning”fortherules.Assuch,P84
reported: “Some rules had more information than others which made the choices
slightlyharder”.
6participantsperceivedcounterfactualexplanationsashelpfulandeasytoread.For
example,P85reported:“Theexplanationincludesmanychangesintheattributebut
helps to understand (going through scenarios) which attributes are more important
andinfluentialthanothers.”.Onthecontrary,6participantsstatedtheywereunclear
oruntrustworthy.Forexample,P5said:“Explanationisveryhelpfulbuthardtotrust
duetonotknowingthemechanismsbehindtheAI”.
6 Discussion
ThepaperexploredhowAIassistanceandvariousexplanationtypesinfluenceusers’
accuracy, reliance on AI, and cognitive load. Additionally, we examined the role of
XAIinterfaceelementsforindividualswithlowandhighNFC,analyzingdifferences
123

ExploringtheimpactofexplainableAIandcognitive… Page 27 of 43 3
inaccuracyandcognitiveloadacrossthesegroups.Basedonourresults,wepresent
acomprehensivediscussionofourkeyfindings,offeringinsightsintodesignimpli-
cationsandexamininguserbehaviorsinthecontextofaloanapplicationscenario.
6.1 TheroleofAIinshapinguserdecision-making
OurfindingsrevealthathighAIconfidenceincreasesusers’relianceonAIprediction.
Thisissupportedbyposthocanalysis,whereusersprioritizeloanattributesfirst(rank
1),thenAIinformation(rank2),andexplanationslast(rank3).WhenAIconfidence
is low, users still prioritize loan attributes (rank 1) but assign equal priority to AI
information and explanations (both rank 2). Interestingly, prior research (Cau et al.
2023b)inhigh-uncertaintydomainslikestocktradingfoundthatusersprioritizedata
or AI information interchangeably (rank 1) with high AI confidence, but rank AI
(2nd) immediately after data (1st) when AI confidence is low. This suggests that as
uncertaintyindecision-makingincreases,individualsaremorelikelytoseekadditional
guidance from AI. In this context, the confidence level of the AI is essential to the
decision-making process. Our results also indicate that high AI confidence reduces
cognitiveload,withonlyafewstudiessupportingthisdirection(Souchetetal.2024;
SteyversandKumar2024).Altogether,ourfindingsreinforcepriorworkwhereusers
tend to rely more on high AI confidence across various domains and tasks (Zhang
etal.2020;RechkemmerandYin2022;Cauetal.2023a,b;Maetal.2024;Kahretal.
2023;Maetal.2024;CauandSpano2025).
While we balanced participants’ exposure to low and high AI confidence, they
encountered more instances with low confidence and correct predictions than with
othercombinationsofconfidenceandcorrectness.Thisdistributionwasintentionally
designedtoreflectapotentialreal-worldscenarioandtostudyparticipants’reliance
behavioronAI,wherethestatedAIaccuracy(83%)mightnotalignwiththeobserved
accuracy(63%)onunseeninstances.AssummarizedinTable4,users’performance
in the loan prediction tasks highlights a clear split between low and high AI confi-
denceinstances,particularlyconsideringunder-relianceoncorrectsuggestionswith
lowconfidenceand(over)relianceonwrongsuggestionswithhighconfidence.These
resultshighlighttheparticipants’uncertaintyintheirdecision-makingandtheirlack
of self-confidence. Since we can estimate AI confidence but cannot directly control
thecorrectnessofpredictionsforunseeninstances,itisessentialtoexplorealterna-
tive strategies to optimize the use of AI confidence estimates. Consequently, while
presenting AI confidence to users is essential for enhancing transparency (Bertrand
etal.2022;Maetal.2023, 2024;FokandWeld2024;Lietal.2025),itssignificant
impactonreinforcingAIpredictionsunderscorestheneedfortargetedinterfacedesign
interventions.
AI confidence calibration approaches (Silva Filho et al.2023; Ma et al. 2024; Li
etal.2025) provideestimatesthataccurately reflectthelikelihoodofcorrectnessin
AIpredictions.Therefore,itisimportanttocultivateuserawarenessregardingtheir
own decision confidence and to determine strategically when to present AI sugges-
tionsbasedonbothuserandAIconfidencelevels.Onepossiblesolutionistocalibrate
users’ confidence without initial AI assistance, allowing them to receive feedback
123

3 Page 28 of 43 F.M.Cau,L.D.Spano
onthetrade-offsbetweentheirconfidenceandaccuracy.Onceusershavedeveloped
their confidence, AI assistance can be introduced using design patterns that accom-
modatebothone-stageandtwo-stagedecision-makingprocesses.Forinstance,prior
research (Ma et al. 2023, 2024; Li et al. 2025) suggests dynamically adjusting the
timingofAIassistancebycomparingtheconfidencelevelsoftheuserandtheAI.AI
advicemaybeomittedorprovidedon-demand(Buçincaetal.2020;Maetal.2023;
He et al. 2024, 2025; Cau and Spano 2025) when user confidence is high, thereby
preserving user autonomy. Conversely, when AI confidence is higher, suggestions
canbepresentedbeforeusersmaketheirdecisions.Theseapproachesmightbalance
optimizingAIsupportwhilemaintainingusers’autonomy.
6.2 Theimpactofexplanationtypesonuserbehavior
Inlinewithpreviousstudiesontheeffectsofexplanationsonusers(Zhangetal.2020;
Chenetal.2023;CelarandByrne2023;CauandSpano2025),ourresultsshowedthat
thefeature-basedexplanationmightnotimproveaccuracycomparedtotheotherAI
assistanceconditions.Thecounterfactualwastheonlytypeofexplanationclosestto
ourthresholdinincreasingtheaccuracyofusers,althoughwedidnotfinddifferences
amongtheotherAIconditions.Theposthocanalysishighlightsmultiplebenefitsfor
counterfactualexplanations:increasingusers’relianceonAIwhilediminishingcogni-
tiveloadwhencorrectAIpredictionsareshown,andpotentiallyincreasingaccuracy.
Nevertheless,atrendsuggeststheymightoccasionallyloweraccuracyinspecificcon-
texts(correctAIpredictions)andbeperceivedaslessunderstandable,ashighlighted
byourqualitativeanalysis.Interestingly,despitehavingnearlyidenticalvisualizations
to counterfactuals, example-based explanations had no measurable impact on these
evaluationmetrics.
RecentworkfromChaeetal.(2025)supportsthesefindings,indicatingthatcounter-
factualexplanationsimprovetaskperformance,thoughusersreportlowersatisfaction
and understandability. This suggests that counterfactual explanations may trade off
user understandability for performance gains. Also, our results are consistent with
Xuanetal.(2025),statingthatcounterfactualexplanationsareperceivedaslessunder-
standablethanothertypes,suchasfeatureimportance,oftenseenaseasiertograsp.
However,explanationsperceivedas“easytounderstand”werefoundtobebothmore
intelligibleandmoremisleading.ThisalignswiththefindingsofChromiketal.(2021),
suggestingthatusersmightoverestimatetheirunderstandingoflocalfeatureexplana-
tionsduetotheillusionofexplanatorydepth.Furthermore,previouswork(Buçinca
etal.2020;WangandYin2022)alsodemonstratesthatsubjectivemeasures,suchas
userpreferences,donotnecessarilyalignorpredictobjectiveoutcomes.Overall,our
findingsemphasizetheimportanceofshiftingfromtraditionalfeature-basedexplana-
tions,whicharecommonlyusedinAIsystems.Instead,weshouldadoptapproaches
thatresemblehuman-likereasoning,suchascounterfactuals.Hence,itisessentialto
integratevarioustypesofexplanationstooffercomplementaryinsights.Thiscombina-
tioncanaddresseachexplanation’sshortcomingsandlimitations,ultimatelyleading
tothedevelopmentofhybridvisualizationsforexplainableAI(XAI).Recentstudies
haveproposedintegratingactionabledata-centricexplanations(AnikandBunt2021;
123

ExploringtheimpactofexplainableAIandcognitive… Page 29 of 43 3
LiaoandVarshney2021;Yurritaetal.2023;Esfahanietal.2024b;Bhattacharyaetal.
2025) alongside model-centric ones, offering potential benefits for both AI experts
and lay users by connecting them to the training data and influencing their percep-
tionsoftrustandfairnessinAIsystems.Forinstance,researchinthehealthdomain
hasdemonstratedthatexpertusersgainsignificantadvantagesfromhybridexplana-
tionscombiningdata-centricandglobalmodel-centricelements(Bhattacharyaetal.
2023, 2024a,b; Szymanski et al. 2024), though these approaches remain underex-
ploredforlayusers(CauandSpano2025).Futureworkshouldfocusondeveloping
tailored explanation interfaces that adapt to users’ expertise levels and contextual
needs,ensuringbothaccessibilityforlayusersanddepthforexperts.Ontopofthis,
tailoringXAIinterfacesforusersmayinvolveassessinguser-centricperspectivesand
characteristics,whichwediscussinthenextsubsection.
6.3 Individualdifferences:NFCandpersonalizationinAIinteraction
Ourfindingsdifferfrompreviouswork(Millecampetal.2019;Buçincaetal.2021;
Conatietal.2021;Baheletal.2024),whichreporteddifferencesbetweenlowandhigh
NFCindividualsintermsofaccuracyandcognitiveload.Interestingly,wefoundthat
bothlowandhighNFCparticipantsprioritizedexplanations(ranked2nd)immediately
afterloanapplicationattributes(ranked1st),leavingAIinformation(ranked3rd)as
theleastinfluentialindecision-making.Moreover,lowNFCindividualsprioritizedAI
predictionoveraccuracy,whilethosewithahighNFCseemtoconsiderAIinformation
asawhole.Wecanidentifytwomainreasonswemightnothaveobservedsignificant
NFC-relateddifferencescomparedtopriorstudies.
First,thetask’snatureandcomplexitymayhaveminimizedthedifferencesbetween
NFC groups. Notably, prior studies focused on low-stakes tasks, such as explaining
music recommendations (Millecamp et al. 2019), nutrition choices in image-based
domains (Buçinca et al. 2021), and tutoring systems for university students with
somedomainknowledge(Baheletal.2024).Incontrast,ourstudyinvolvedahigh-
stakesloanapprovaltaskusingtabulardatawithelevenfeatures,whereparticipants
were unfamiliar with the domain. Additionally, our explanations added substantial
informationforuserstoprocess,classifyingthetaskashigh-complexityaccordingto
Salimzadehetal.(2023).Thissuggeststhatastaskcomplexityincreases,NFCmay
loseitspredictiveabilitytodifferentiateindividualbehaviors.
Second,whiletheNFCpersonalitytraithasbeenshowntodistinguishbetweenlow
andhighNFCindividuals,itmaynotreliablyexplaindifferencesinAI-drivendecision
outcomes,regardlessofcognitiveforcing.RecentAI-assisteduserstudiesindomains
likeartperioddetection(KüperandKrämer2025),jobapplications(CauandSpano
2025),andexerciserecommendation(Buçincaetal.2024, 2025),indicatethatNFC
maynotalwayspredictdifferencesinusers’accuracy,learning,relianceonAI,ormen-
taldemand,regardlessofexplanationtypeorcognitiveinterventions.Thesefindings
highlighttheneedforalternativetraitsthatmightcapturericherinsightsaboutintrinsic
motivationtolearnandthink,suchasEpistemicCuriosity(Litman2008)orthefive-
dimensionalcuriosityscale(Kashdanetal.2018).Moreover,anotablemethodological
concern is dividing participants into low- and high-trait groups after data collection
123

3 Page 30 of 43 F.M.Cau,L.D.Spano
basedontheoverallparticipantdistributionmedian.Thisapproach,commonlyused
for NFC and other traits, may lead to imbalances and unequal group sizes, compli-
cating statistical analyses and consequent reproducibility of results. Future research
should explore alternative user-centric metrics beyond personality traits that enable
real-timecategorizationduringstudies,ensuringmorebalancedgroupsanddynamic
personalization.
6.4 Limitationsandfuturework
Weacknowledgethefollowinglimitationsinourwork.ThefirstconsistsofusinganAI
modelwithuncalibratedconfidenceestimates.Althoughweassessedthatcalibration
metricsdidnotimprovetheAIbaselinemodel(RandomForest),thismayhaveaffected
thecomputationofmodelconfidenceestimatesandexplanationsgeneration,andcon-
sequently users’ decision-making during the study. As such, we strongly encourage
futurestudiestocalibratetheirAImodelswhennecessarytoensurestabilitybetween
AIprobabilityoutputsandconfidenceestimates.Asecondlimitationisthatourstudy
employed a one-stage detection paradigm, where users’ decision-making co-occurs
withAIsuggestionsandexplanations.Whilethisapproachmirrorsmanyreal-world
applicationsappliedtoautonomousdriving(Atakishiyevetal.2024)andcybersecu-
rity(Desoldaetal.2023),itmayrestricttheabilitytodisentangleusers’independent
reasoningfromtheirrelianceonAIadvice.Incontrast,two-stagedetectionparadigms,
whereusersfirstevaluateataskindependentlybeforeincorporatingAIinput,provide
a clearer separation of cognitive engagement and reliance patterns. Future research
shouldexplorebalancingtheseparadigmstoachieveanoptimaltrade-offbasedonthe
targetdomain’sspecificdemands,stakes,andcognitivecomplexity.Thethirdlimita-
tionisthatwesolelyfocusedontheNeedforCognitionpersonalitytrait.However,
manyotherindividualdifferencesmightdrivepeople’sdecision-makingandbehaviors
when interacting with AI assistance or explanations, such as AI literacy (Schoeffer
etal.2022),ActivelyOpen-mindedThinking(Baron1985),ormetacognitivepercep-
tions(Cushingetal.2024),whichwouldrequirefurtherinvestigationinfuturework.
The last limitation concerns the generalizability of our findings beyond the specific
domain, dataset, classification model, AI confidence split into low and high levels,
andexplanationmethodsused.Ourstudyemployedapubliclyavailableloanapproval
dataset commonly used in HCI research, along with a model achieving comparable
evaluationmetrics.Additionally,ourparticipants’sampledemonstratedlowfamiliar-
itywiththeloanapprovaltask,andweencouragecautioningeneralizingthesefindings
toexpertusers.Althoughweusedstate-of-the-artmethodstogenerateexplanations,
it is possible to produce the same type of explanation (e.g., feature-based, rules, or
counterfactuals)throughdifferentapproaches,whichcouldleadtodifferentfindings.
Whileweensuredreplicabilitybydetailingthedataprocessing,AImodel,explana-
tiongeneration,andstatisticalanalysis,severalvariablesuniquetooursetupmayhave
influenceddecision-making.FurtherresearchisneededtoevaluatetheimpactofAI
andexplanationsacrossdiversedomainswithvaryingstakesandlevelsofuncertainty.
123

ExploringtheimpactofexplainableAIandcognitive… Page 31 of 43 3
7 Conclusion
This article investigated how presenting AI information, including prediction, con-
fidence, accuracy, and explanation styles such as example-based, feature-based,
rule-based,andcounterfactual,affectsusers’decision-makinginloanapprovaltasks.
Specifically,weconductedauserstudy(N=288)examininghowtheseelementsinflu-
enceaccuracy,relianceonAI,andcognitiveloadacrosssixAIassistanceconditions:
noAI,AIwithnoexplanation,andAIwitheachofthefourexplanationstyles.Addi-
tionally,giventherecentinterestinstudyingtheNeedforCognition(NFC)personality
traitinhuman–AIteams,weexploredhowNFClevelsaffectusers’prioritizationof
information,accuracy,andcognitiveloadwheninteractingwithdifferentexplanation
styles.
OurresultsshowthathighAIconfidencesignificantlyincreasesusers’relianceon
AIwhilereducingcognitiveload,emphasizingtheimportanceofaccuratelycalibrating
confidence estimates to reflect AI correctness. Counterfactual explanations, despite
being rated as less understandable than feature-based ones, overall increase users’
accuracy, also reducing cognitive load and increasing reliance on AI, particularly
whenpairedwithcorrectAIpredictions.Incontrast,feature-basedexplanationsfailed
toimprove accuracy asanticipated.Moreover,weobserved thatNFClevelsdidnot
significantlydifferinhowusersprioritizeinformationortheirreliance,accuracy,and
cognitiveload,suggestingthatNFC’sinfluencemaybetask-orcontext-specific.These
findingscontributetoadeeperunderstandingofhowAI-assisteddecision-makingcan
beoptimizedbyintegratingcomplementaryexplanationstylesandtailoringinterfaces
toindividualuserneeds.Futureworkshouldexplorehybridexplanationsystemsand
refine user-centric models with AI to create more adaptive, effective, and equitable
human–AIcollaborationframeworks.
AppendixA
A.1.Modelcalibration
GivenwewillshowparticipantstheRFCconfidenceforeachprediction,wedecided
to calibrate the RFC probabilities before computing the confidence estimates using
three methods: Isotonic Regression (Zadrozny and Elkan 2001), Platt Scaling (Platt
2000), inductive and cross Venn-Abers (Vovk and Petej 2014; Vovk et al. 2015;
Manokhin 2017). Specifically, we compared the RFC with ensembles of ten RFC
models for each method to assess a ten-fold cross-validation. Nevertheless, in this
specificscenario,thesemethodsslightlyworsenedthemetricswetookintoconsider-
ation(Accuracy,BrierlossBrier1950,LoglossDomingos1999,ROC-AUCFawcett
2004,andExpectedCalibrationErrorGuoetal.2017),exceptfortheIsotonicRegres-
siontosomeextent(seeTable3).Wedecidedtouseouroriginal(uncalibrated)RFC
modelfortheloanpredictiontaskasitresultedinbettercalibrationmetricsthanthe
othermethodsweused.
123

3 Page 32 of 43 F.M.Cau,L.D.Spano
Table3 SummaryoftheRandomForestcalibrationresultsusingthefollowingmetrics:accuracy,Brier
loss,Logloss,ECE,andROC-AUC
Method Accuracy Brierloss Logloss ECE ROC-AUC
RFrawprobabilities 0.8293 0.1370 0.4424 0.0580 0.8204
IsotonicRegression 0.8130 0.1403 0.4518 0.0618 0.8215
PlattScaling 0.8130 0.1413 0.4524 0.0768 0.8167
CrossVenn-Abers 0.8211 0.1492 0.4727 0.0641 0.8
WeomittedtheinductiveVenn-Abersgiventheworstresultsoverallcomparedtotheothermethods.
Thevaluesinboldrepresentthebestresultsachievedacrossthemodelcalibrationmethods(forAccuracy
andROC-AUC,thehigherthebetter;forBrierloss,Logloss,andECE,thelowerthebetter).
A.2.Needforcognitionscale
Wewillmeasureparticipants’NeedforCognition(NFC)withtheNCS-6considering
a 5-point scale (1 = extremely uncharacteristic of me; 5 = extremely characteristic
ofme).Wewillsumupallthesix-itemscoresandthencomputethemediantosplit
participantsintolowandhighNFC.Weusedthefollowingsixitemstocomputethe
NFCfromdeHolandaCoelhoetal.(2020)19:
1. Iwouldprefercomplextosimpleproblems.
2. Iliketohavetheresponsibilityofhandlingasituationthatrequiresalotofthinking.
3. Thinkingisnotmyideaoffun.(R)
4. Iwouldratherdosomethingthatrequireslittlethoughtthansomethingthatissure
tochallengemythinkingabilities.(R)
5. Ireallyenjoyataskthatinvolvescomingupwithnewsolutionstoproblems.
6. I would prefer a task that is intellectual, difficult, and important to one that is
somewhatimportant.
A.3.Metricsoverviewbytask
Wesummarizedparticipants’performanceonloanpredictiontasksinTable4,ordered
bydecreasingaccuracy.AlongwithrelianceonAIandcognitiveload,wealsoreported
participants’ disagreement with correct AI advice, namely their under-reliance. We
reportedallthemetricsinpercent(%),exceptforcognitiveload.
19 note:(R)=reverseditems.
123

ExploringtheimpactofexplainableAIandcognitive… Page 33 of 43 3
Table 4 Participants’ accuracy, reliance on AI, under-reliance on AI, and cognitive load for our loan
predictiontaskinstancesettings
ID AIcorrectness AIconfidence Accuracy Reliance Under-reliance Cognitiveload
| 5 Correct | High | 90.4 90.4 | 9.6  | 3.1 |
| --------- | ---- | --------- | ---- | --- |
| 1 Correct | High | 85.4 85.4 | 14.6 | 3.3 |
| 6 Correct | Low  | 71.2 71.2 | 28.7 | 3.8 |
| 4 Correct | Low  | 56.2 56.2 | 43.8 | 3.7 |
| 2 Correct | Low  | 44.2 44.2 | 55.8 | 3.8 |
| 8 Wrong   | Low  | 27.9 72.1 | –    | 3.5 |
| 3 Wrong   | High | 27.1 72.9 | –    | 3.4 |
| 7 Wrong   | High | 14.6 85.4 | –    | 3.3 |
Fig.8 NFCdistributionofparticipantsintheuserstudy.TheorangeverticallinerepresentstheNFCmedian
(3.5)weusedtosplitparticipantsintolowandhighNFCgroups
Fig.9 Participants’relianceonAI,cognitiveload,andaccuracydividedbyAIassistanceandAIconfidence
conditions
123

3 Page 34 of 43 F.M.Cau,L.D.Spano
Fig.10 XAIinterfacecomponentsrankfrequenciesforlowandhighAIconfidence.Theasteriskshighlight
pvaluesignificantstrength(***p<.001)
Acknowledgements ThisresearchisfundedbytheItalianMinistryofUniversityandResearch(MUR)
andbytheEuropeanUnion—NextGenerationEU,Mission4,Component2,Investment1.1,undergrant
PRIN2022PNRR”DAMOCLES:DetectionAndMitigationOfCyberattacksthatexploithumanvuLner-
abilitiES”(GrantP2022FXP5B)—CUP:H53D23008140001.
Author contribution FC conceived and designed the user study and performed experiments under the
supervisionofLS.Allauthorsjointlywroteandreviewedthemanuscript.
Funding Open access funding provided by Università degli Studi di Cagliari within the CRUI-CARE
Agreement.
Data availability The original dataset used in this article is openly available at https://www.kaggle.
com/datasets/altruistdelhite04/loan-prediction-problem-dataset. The study pipeline of data processing,
modeltraining,explanationgeneration,andstatisticalanalysisisopenlyavailableathttps://osf.io/j64x8/?
viewonly=7f546294a08843acbf204521ba7dee7e.
Declarations
Conflictofinterest Theauthorsdeclarenoconflictofinterest.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincluded
inthearticle’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.If
materialisnotincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermitted
bystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthe
copyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
Adadi,A.,Berrada,M.:Peekinginsidetheblack-box:asurveyonexplainableartificialintelligence(xai).
IEEEAccess6,52138–52160(2018).https://doi.org/10.1109/ACCESS.2018.2870052
Agudo,U.,Liberal,K.G.,Arrese,M.,etal.:Theimpactofaierrorsinahuman-in-the-loopprocess.Cogn.
Res.Princ.Implic.9(1),1(2024).https://doi.org/10.1186/s41235-023-00529-3
Anik,A.I.,Bunt,A.:Data-centricexplanations:explainingtrainingdataofmachinelearningsystemsto
promotetransparency.In:Proceedingsofthe2021CHIConferenceonHumanFactorsinComputing
123

ExploringtheimpactofexplainableAIandcognitive… Page 35 of 43 3
Systems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).https://doi.
org/10.1145/3411764.3445736
Atakishiyev,S.,Salameh,M.,Yao,H.,etal.:Explainableartificialintelligenceforautonomousdriving:
acomprehensiveoverviewandfieldguideforfutureresearchdirections.IEEEAccess12,101603–
101625(2024).https://doi.org/10.1109/ACCESS.2024.3431437
Bahel, V., Sriram, H., Conati, C.: Initial results on personalizing explanations of ai hints in an its. In:
Proceedingsofthe32ndACMConferenceonUserModeling,AdaptationandPersonalization.Asso-
ciationforComputingMachinery,NewYork,NY,USA,UMAP’24,pp.244–248(2024).https://doi.
org/10.1145/3627043.3659566
Bansal, G., Wu, T., Zhou, J. et al.: Does the whole exceed its parts? the effect of ai explanations on
complementaryteamperformance.In:Proceedingsofthe2021CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).
https://doi.org/10.1145/3411764.3445717
Baron,J.:RationalityandIntelligence.CambridgeUniversityPress,Cambridge(1985)
Beede,E.,Baylor,E.,Hersch,F.etal.:Ahuman-centeredevaluationofadeeplearningsystemdeployed
inclinicsforthedetectionofdiabeticretinopathy.In:Proceedingsofthe2020CHIConferenceon
HumanFactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,
CHI’20,pp.1–12(2020).https://doi.org/10.1145/3313831.3376718
Bertrand,A.,Belloum,R.,Eagan,J.R.,etal.:Howcognitivebiasesaffectxai-assisteddecision-making:a
systematicreview.In:Proceedingsofthe2022AAAI/ACMConferenceonAI,Ethics,andSociety.
AssociationforComputingMachinery,NewYork,NY,USA,AIES’22,pp.78–91(2022).https://
doi.org/10.1145/3514094.3534164
Bhattacharya,A.,Ooge,J.,Stiglic,G.,etal.:Directiveexplanationsformonitoringtheriskofdiabetesonset:
Introducing directive data-centric explanations and combinations to support what-if explorations.
In:Proceedingsofthe28thInternationalConferenceonIntelligentUserInterfaces.Associationfor
ComputingMachinery,NewYork,NY,USA,IUI’23,pp.204–219(2023).https://doi.org/10.1145/
3581641.3584075
Bhattacharya,A.,Stumpf,S.,Gosak,L.,etal.:Exmos:explanatorymodelsteeringthroughmultifaceted
explanationsanddataconfigurations.In:ProceedingsoftheCHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’24(2024a).
https://doi.org/10.1145/3613904.3642106
Bhattacharya,A.,Stumpf,S.,Verbert,K.:Anexplanatorymodelsteeringsystemforcollaborationbetween
domainexpertsandai.In:AdjunctProceedingsofthe32ndACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
Adjunct’24,pp.75–79(2024b).https://doi.org/10.1145/3631700.3664886
Bhattacharya,A.,Vanherwegen,T.,Verbert,K.:"showmehow":benefitsandchallengesofagent-augmented
counterfactualexplanationsfornon-expertusers.In:Proceedingsofthe33rdACMConferenceon
UserModeling,AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,
NY,USA,UMAP’25,pp.174–184(2025).https://doi.org/10.1145/3699682.3728321
Binns,R.,VanKleek,M.,Veale,M.,etal.:’It’sreducingahumanbeingtoapercentage’:perceptionsof
justiceinalgorithmicdecisions.In:Proceedingsofthe2018CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’18,pp.1–14
(2018).https://doi.org/10.1145/3173574.3173951
Bodria,F.,Giannotti,F.,Guidotti,R.,etal.:Benchmarkingandsurveyofexplanationmethodsforblack
boxmodels.DataMin.Knowl.Disc.37(5),1719–1778(2023).https://doi.org/10.1007/s10618-023-
00933-9
Boonprakong,N.,Tag,B.,Goncalves,J.,etal.:HowdoHCIresearchersstudycognitivebiases?Ascoping
review. In: Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems.
Association for Computing Machinery, New York, NY, USA, CHI ’25 (2025). https://doi.org/10.
1145/3706598.3713450
Bove,C.,Aigrain,J.,Lesot,M.J.,etal.:Contextualizationandexplorationoflocalfeatureimportance
explanationstoimproveunderstandingandsatisfactionofnon-expertusers.In:27thInternational
ConferenceonIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,
USA,IUI’22,pp.807–819(2022).https://doi.org/10.1145/3490099.3511139
Brier,G.W.:Verificationofforecastsexpressedintermsofprobability.Mon.WeatherRev.78,1–3(1950)
Buçinca,Z.,Lin,P.,Gajos,K.Z.,etal.:Proxytasksandsubjectivemeasurescanbemisleadinginevaluat-
ingexplainableaisystems.In:Proceedingsofthe25thInternationalConferenceonIntelligentUser
123

3 Page 36 of 43 F.M.Cau,L.D.Spano
Interfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’20,pp.454–464(2020).
https://doi.org/10.1145/3377325.3377498
Buçinca,Z.,Malaya,M.B.,Gajos,K.Z.:Totrustortothink:cognitiveforcingfunctionscanreduceoverre-
lianceonAIinai-assisteddecision-making.Proc.ACMHum.Comput.Interact.(2021).https://doi.
org/10.1145/3449287
Buçinca,Z.,Swaroop,S.,Paluch,A.E.,etal.:Towardsoptimizinghuman-centricobjectivesinai-assisted
decision-makingwithofflinereinforcementlearning(2024).arxiv:2403.05911
Buçinca,Z.,Swaroop,S.,Paluch.A.E.,etal.:Contrastiveexplanationsthatanticipatehumanmisconceptions
canimprovehumandecision-makingskills.In:Proceedingsofthe2025CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’25
(2025).https://doi.org/10.1145/3706598.3713229
Cacioppo,J.,Petty,R.,Kao,C.:TheefficientassessmentofNFC.J.Pers.Assess.48,306–7(1984).https://
doi.org/10.1207/s15327752jpa4803_13
Cai,C.J.,Jongejan,J.,Holbrook,J.:Theeffectsofexample-basedexplanationsinamachinelearninginter-
face.In:Proceedingsofthe24thInternationalConferenceonIntelligentUserInterfaces.Association
forComputingMachinery,NewYork,NY,USA,IUI’19,pp.258–262(2019a).https://doi.org/10.
1145/3301275.3302289
Cai,C.J.,Reif,E.,Hegde,N.,etal.:Human-centeredtoolsforcopingwithimperfectalgorithmsduring
medicaldecision-making.In:Proceedingsofthe2019CHIConferenceonHumanFactorsinComput-
ingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’19,pp.1–14(2019b).
https://doi.org/10.1145/3290605.3300234
Candrian,C.,Scherer,A.:Riseofthemachines:delegatingdecisionstoautonomousai.Comput.Hum.
Behav.134,107308(2022).https://doi.org/10.1016/j.chb.2022.107308
Cao,S.,Liu,A.,Huang,C.M.:Designingforappropriatereliance:therolesofaiuncertaintypresentation,
initialuserdecision,anduserdemographicsinai-assisteddecision-making.ProcACMHum.Comput.
Interact.(2024a).https://doi.org/10.1145/3637318
Cao,S.,Liu,A.,Huang,C.M.:Designingforappropriatereliance:therolesofaiuncertaintypresentation,
initialuserdecision,anduserdemographicsinai-assisteddecision-making.Proc.ACMHum.Comput.
Interact.(2024b).https://doi.org/10.1145/3637318
Carenini,G.:Ananalysisoftheinfluenceofneedforcognitionondynamicqueriesusage.In:CHI’01
ExtendedAbstractsonHumanFactorsinComputingSystems.AssociationforComputingMachinery,
NewYork,NY,USA,CHIEA’01,pp.383–384(2001).https://doi.org/10.1145/634067.634293
Cau, F.M., Spano, L.D.: The influence of curiosity traits and on-demand explanations in ai-assisted
decision-making.In:Proceedingsofthe30thInternationalConferenceonIntelligentUserInterfaces.
AssociationforComputingMachinery,NewYork,NY,USA,IUI’25,pp.1440–1457(2025).https://
doi.org/10.1145/3708359.3712165
Cau,F.M.,Hauptmann,H.,Spano,L.D.,etal.:Effectsofaiandlogic-styleexplanationsonusers’decisions
underdifferentlevelsofuncertainty.ACMTrans.Interact.Intell.Syst.(2023a).https://doi.org/10.
1145/3588320
Cau,F.M.,Hauptmann,H.,Spano,L.D.,etal.:Supportinghigh-uncertaintydecisionsthroughaiandlogic-
styleexplanations.In:Proceedingsofthe28thInternationalConferenceonIntelligentUserInterfaces.
AssociationforComputingMachinery,NewYork,NY,USA,IUI’23,pp.251–263(2023b).https://
doi.org/10.1145/3581641.3584080
Cazan,A.M.,Indreica,S.E.:Needforcognitionandapproachestolearningamonguniversitystudents.
ProcediaSoc.Behav.Sci.127,134–138(2014).https://doi.org/10.1016/j.sbspro.2014.03.227
Celar,L.,Byrne,R.:Howpeoplereasonwithcounterfactualandcausalexplanationsforartificialintelligence
decisionsinfamiliarandunfamiliardomains.MemoryCogn.(2023).https://doi.org/10.3758/s13421-
023-01407-5
Chae,S.,Lee,S.,Hauptmann,H.,etal.:Theroleofexplanationstylesandperceivedaccuracyondecision
makinginpredictiveprocessmonitoring.In:Krogstie,J.,Rinderle-Ma,S.,Kappel,G.,etal.(eds.)
Adv.Inf.Syst.Eng.,pp.39–56.Springer,Cham(2025)
Chen,V.,Liao,Q.V.,WortmanVaughan,J.,etal.:Understandingtheroleofhumanintuitiononreliance
inhuman–AIdecision-makingwithexplanations.Proc.ACMHum.Comput.Interact.(2023).https://
doi.org/10.1145/3610219
Chromik,M.,Eiband,M.,Buchner,F.,etal.:Ithinkigetyourpoint,ai!theillusionofexplanatorydepth
inexplainableai.In:Proceedingsofthe26thInternationalConferenceonIntelligentUserInterfaces.
123

ExploringtheimpactofexplainableAIandcognitive… Page 37 of 43 3
AssociationforComputingMachinery,NewYork,NY,USA,IUI’21,pp.307–317(2021).https://
doi.org/10.1145/3397481.3450644
Conati,C.,Barral,O.,Putnam,V.,etal.:TowardpersonalizedXAI:acasestudyinintelligenttutoring
systems.Artif.Intell.298,103503(2021).https://doi.org/10.1016/j.artint.2021.103503
Cushing,C.A.,Lau,H.,Hofmann,S.G.,etal.:Metacognitionasawindowintosubjectiveaffectiveexpe-
rience.PsychiatryClin.Neurosci.78(8),430–437(2024)
Day,E.,Boatman,J.,Kowollik,V.,etal.:Modelingthelinksbetweenneedforcognitionandtheacquisition
ofacomplexskill.Person.Indiv.Differ.42,201–212(2007).https://doi.org/10.1016/j.paid.2006.06.
012
de Holanda Coelho, G.L., Hanel, P.H.P., Wolf, L.J.: The very efficient assessment of need for cogni-
tion:developingasix-itemversion.Assessment27(8),1870–1885(2020).https://doi.org/10.1177/
1073191118793208
Desolda,G.,Aneke,J.,Ardito,C.,etal.:Explanationsinwarningdialogstohelpusersdefendagainst
phishing attacks. Int. J. Hum. Comput. Stud. 176, 103056 (2023). https://doi.org/10.1016/j.ijhcs.
2023.103056
Dodge,J.,VeraLiao,Q.,Zhang,Y.,etal.:Explainingmodels:anempiricalstudyofhowexplanationsimpact
fairnessjudgment.pp275–285(publisherCopyright:2019AssociationforComputingMachinery.;
24thACMInternationalConferenceonIntelligentUserInterfaces,IUI2019;Conferencedate:17-
03-2019Through20-03-2019)(2019).https://doi.org/10.1145/3301275.3302310
Domingos,P.:Metacost:ageneralmethodformakingclassifierscost-sensitive.In:ProceedingsoftheFifth
ACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.Associationfor
ComputingMachinery,NewYork,NY,USA,KDD’99,pp.155–164,(1999).https://doi.org/10.1145/
312129.312220
Esfahani,S.,DeToni,G.,Lepri,B.,etal.:Preferenceelicitationininteractiveanduser-centeredalgorithmic
recourse:aninitialexploration.In:Proceedingsofthe32ndACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’24,pp.249–254(2024a).https://doi.org/10.1145/3627043.3659556
Esfahani,S.,DeToni,G.,Lepri,B.,etal.:Preferenceelicitationininteractiveanduser-centeredalgorithmic
recourse:aninitialexploration.In:Proceedingsofthe32ndACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’24,pp.249–254(2024b).https://doi.org/10.1145/3627043.3659556
Faul,F.,Erdfelder,E.,Buchner,A.,etal.:Statisticalpoweranalysesusingg*power3.1:testsforcorrelation
andregressionanalyses.Behav.Res.Methods41(4),1149–1160(2009)
Fawcett,T.:Rocgraphs:notesandpracticalconsiderationsforresearchers.Mach.Learn.31,1–38(2004)
Feldkamp,N.,Strassburger,S.:Fromexplainableaitoexplainablesimulation:usingmachinelearning
andxaitounderstandsystemrobustness.In:Proceedingsofthe2023ACMSIGSIMConferenceon
PrinciplesofAdvancedDiscreteSimulation.AssociationforComputingMachinery,NewYork,NY,
USA,SIGSIM-PADS’23,pp.96–106(2023).https://doi.org/10.1145/3573900.3591114
Fogliato,R.,Chappidi,S.,Lungren,M.,etal.:Whogoesfirst?Influencesofhuman–AIworkflowondecision
makinginclinicalimaging.In:Proceedingsofthe2022ACMConferenceonFairness,Accountability,
andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAccT’22,pp.1362–
1374(2022a).https://doi.org/10.1145/3531146.3533193
Fogliato,R.,Chappidi,S.,Lungren,M.,etal.:Whogoesfirst?Influencesofhuman-aiworkflowondecision
makinginclinicalimaging.In:Proceedingsofthe2022ACMConferenceonFairness,Accountability,
andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAccT’22,pp.1362–
1374(2022b).https://doi.org/10.1145/3531146.3533193
Fok,R.,Weld,D.S.:Insearchofverifiability:explanationsrarelyenablecomplementaryperformancein
AI-advised decision making. AI Mag. 45(3), 317–332 (2024). https://doi.org/10.1002/aaai.12182.
(https://onlinelibrary.wiley.com/doi/pdf/10.1002/aaai.12182)
Ford,C.,Keane,M.T.:Explainingclassificationstonon-experts:anxaiuserstudyofpost-hocexplanations
foraclassifierwhenpeoplelackexpertise.In:PatternRecognition,ComputerVision,andImage
Processing.ICPR2022InternationalWorkshopsandChallenges:Montreal,QC,Canada,August21–
25,2022,Proceedings,PartIII.Springer-Verlag,Berlin,Heidelberg,pp.246–260(2023).https://doi.
org/10.1007/978-3-031-37731-0_15
Foroudi,P.,Marvi,R.,Zha,D.:Aisensationandengagement:unpackingthesensoryexperienceinhuman–
AIinteraction.Int.J.Inf.Manage.84,102918(2025).https://doi.org/10.1016/j.ijinfomgt.2025.102918
123

3 Page 38 of 43 F.M.Cau,L.D.Spano
Friedman,M.:Theuseofrankstoavoidtheassumptionofnormalityimplicitintheanalysisofvariance.
J. Am. Stat. Assoc. 32(200), 675–701 (1937). https://doi.org/10.1080/01621459.1937.10503522.
(https://www.tandfonline.com/doi/pdf/10.1080/01621459.1937.10503522)
Friedman,M.:Acomparisonofalternativetestsofsignificancefortheproblemof$m$rankings.Ann.
Math.Stat.11,86–92(1940)
Gajos,K.Z.,Chauncey,K.:Theinfluenceofpersonalitytraitsandcognitiveloadontheuseofadaptive
userinterfaces.In:Proceedingsofthe22ndInternationalConferenceonIntelligentUserInterfaces.
AssociationforComputingMachinery,NewYork,NY,USA,IUI’17,pp.301–306(2017).https://
doi.org/10.1145/3025171.3025192
Gajos,K.Z.,Mamykina,L.:DopeopleengagecognitivelywithAI?ImpactofAIassistanceonincidental
learning.In:Proceedingsofthe27thInternationalConferenceonIntelligentUserInterfaces.Associ-
ationforComputingMachinery,NewYork,NY,USA,IUI’22,pp.794–806(2022).https://doi.org/
10.1145/3490099.3511138
Ghai,B.,Liao,Q.V.,Zhang,Y.,etal.:Explainableactivelearning(xal):towardaiexplanationsasinterfaces
formachineteachers.Proc.ACMHum.Comput.Interact.(2021).https://doi.org/10.1145/3432934
Gomez,O.,Holter,S.,Yuan,J.,etal.:Vice:visualcounterfactualexplanationsformachinelearningmodels.
In:Proceedingsofthe25thInternationalConferenceonIntelligentUserInterfaces.Associationfor
ComputingMachinery,NewYork,NY,USA,IUI’20,pp.531–535(2020).https://doi.org/10.1145/
3377325.3377536
Gomez,C.,Cho,S.M.,Ke,S.,etal.:Human–AIcollaborationisnotverycollaborativeyet:ataxonomy
ofinteractionpatternsinAI-assisteddecisionmakingfromasystematicreview.Front.Comput.Sci.
(2025).https://doi.org/10.3389/fcomp.2024.1521066
Grace,K.,Finch,E.,Gulbransen-Diaz,N.,etal.:Q-chef:theimpactofsurprise-elicitingsystemsonfood-
relateddecision-making.In:Proceedingsofthe2022CHIConferenceonHumanFactorsinComputing
Systems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’22(2022).https://doi.
org/10.1145/3491102.3501862
Green,B.,Chen,Y.:Disparateinteractions:analgorithm-in-the-loopanalysisoffairnessinriskassessments.
In:ProceedingsoftheConferenceonFairness,Accountability,andTransparency.Associationfor
ComputingMachinery,NewYork,NY,USA,FAT*’19,pp.90–99(2019a).https://doi.org/10.1145/
3287560.3287563
Green,B.,Chen,Y.:Theprinciplesandlimitsofalgorithm-in-the-loopdecisionmaking.Proc.ACMHum.
Comput.Interact.(2019b).https://doi.org/10.1145/3359152
Guo,C.,Pleiss,G.,Sun,Y.,etal.:Oncalibrationofmodernneuralnetworks.In:PrecupD,TehYW(eds),
Proceedings of the 34th International Conference on Machine Learning, Proceedings of Machine
LearningResearch,vol70.PMLR,pp.1321–1330(2017).https://proceedings.mlr.press/v70/guo17a.
html
Hase,P.,Bansal,M.:EvaluatingexplainableAI:Whichalgorithmicexplanationshelpuserspredictmodel
behavior?In:Jurafsky,D.,Chai,J.,Schluter,N.,etal.(eds),Proceedingsofthe58thAnnualMeet-
ing of the Association for Computational Linguistics. Association for Computational Linguistics,
Online,pp.5540–5552(2020).https://doi.org/10.18653/v1/2020.acl-main.491.https://aclanthology.
org/2020.acl-main.491
He,G.,Buijsman,S.,Gadiraju,U.:Howstatedaccuracyofanaisystemandanalogiestoexplainaccuracy
affecthumanrelianceonthesystem.Proc.ACMHum.Comput.Interact.(2023a).https://doi.org/10.
1145/3610067
He,G.,Kuiper,L.,Gadiraju,U.:Knowingaboutknowing:anillusionofhumancompetencecanhinder
appropriaterelianceonAIsystems.In:Proceedingsofthe2023CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’23(2023b).
https://doi.org/10.1145/3544548.3581025
He,G.,Balayn,A.,Buijsman,S.,etal.:Openingtheanalogicalportaltoexplainability:Cananalogies
helplaypeopleinai-assisteddecisionmaking?J.Artif.Int.Res.(2024).https://doi.org/10.1613/jair.
1.15118
He,G.,Aishwarya,N.,Gadiraju,U.:IsconversationalXAIallyouneed?Human–AIdecisionmakingwith
aconversationalxaiassistant.In:Proceedingsofthe30thInternationalConferenceonIntelligentUser
Interfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’25,pp.907–924(2025).
https://doi.org/10.1145/3708359.3712133
Herm,L.V.:ImpactofexplainableAIoncognitiveload:insightsfromanempiricalstudy.In:European
ConferenceonInformationSystems,ECIS2023Research,p.269(2023)
123

ExploringtheimpactofexplainableAIandcognitive… Page 39 of 43 3
Herzog,D.,Wörndl,W.:Auserstudyongroupsinteractingwithtouristtriprecommendersystemsin
public spaces. In: Proceedings of the 27th ACM Conference on User Modeling, Adaptation and
Personalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP’19,pp.130–
138(2019).https://doi.org/10.1145/3320435.3320449
Kahr,P.K.,Rooks,G.,Willemsen,M.C.,etal.:Itseemssmart,butitactsstupid:developmentoftrustinai
adviceinarepeatedlegaldecision-makingtask.In:Proceedingsofthe28thInternationalConference
onIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’23,
pp.528–539(2023).https://doi.org/10.1145/3581641.3584058
Kahr,P.K.,Rooks,G.,Willemsen,M.C.,etal.:Understandingtrustandreliancedevelopmentinaiadvice:
assessing model accuracy, model explanations, and experiences from previous interactions. ACM
Trans.Interact.Intell.Syst.(2024).https://doi.org/10.1145/3686164
Kashdan,T.B.,Stiksma,M.C.,Disabato,D.J.,etal.:Thefive-dimensionalcuriosityscale:capturingthe
bandwidthofcuriosityandidentifyingfouruniquesubgroupsofcuriouspeople.J.Res.Pers.73,
130–149(2018).https://doi.org/10.1016/j.jrp.2017.11.011.(https://www.sciencedirect.com/science/
article/pii/S0092656617301149)
Kenny,E.M.,Keane,M.T.:Twin-systemstoexplainartificialneuralnetworksusingcase-basedreasoning:
comparativetestsoffeature-weightingmethodsinANN-CBRtwinsforXAI.In:Proceedingsofthe
Twenty-EighthInternationalJointConferenceonArtificialIntelligence,IJCAI-19.InternationalJoint
ConferencesonArtificialIntelligenceOrganization,pp.2708–2715(2019).https://doi.org/10.24963/
ijcai.2019/376
Kenny, E.M., Keane, M.T.: Explaining deep learning using examples: optimal feature weighting
methods for twin systems using post-hoc, explanation-by-example in XAI. Knowl. Based Syst.
233,107530(2021).https://doi.org/10.1016/j.knosys.2021.107530.(https://www.sciencedirect.com/
science/article/pii/S0950705121007929)
Kim,S.,Meister,N.,Ramaswamy,V.,etal.:Hive:evaluatingthehumaninterpretabilityofvisualexpla-
nations.In:Avidan,S.,Brostow,G.,Cissé,M.,etal.(eds),ComputerVision—ECCV2022:17th
EuropeanConference,Proceedings.SpringerScienceandBusinessMediaDeutschlandGmbH,Ger-
many,LectureNotesinComputerScience(includingsubseriesLectureNotesinArtificialIntelligence
andLectureNotesinBioinformatics),pp.280–298(publisherCopyright:2022,TheAuthor(s),under
exclusivelicensetoSpringerNatureSwitzerlandAG.;17thEuropeanConferenceonComputerVision,
ECCV2022;Conferencedate:23-10-2022Through27-10-2022)(2022).https://doi.org/10.1007/
978-3-031-19775-8_17
Küper,A.,Lodde,G.C.,Livingstone,E.,etal.:Psychologicalfactorsinfluencingappropriaterelianceon
ai-enabledclinicaldecisionsupportsystems:experimentalweb-basedstudyamongdermatologists.
J.Med.Int.Res.27,e58660(2025).https://doi.org/10.2196/58660.(https://www.jmir.org/2025/1/
e58660)
Küper,A.,Krämer,N.:Psychologicaltraitsandappropriatereliance:factorsshapingtrustinAI.Int.J.
Hum.Comput.Interact.41(7),4115–4131(2025).https://doi.org/10.1080/10447318.2024.2348216
Lai,V.,Tan,C.:Onhumanpredictionswithexplanationsandpredictionsofmachinelearningmodels:a
casestudyondeceptiondetection.In:ProceedingsoftheConferenceonFairness,Accountability,
andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAT*’19,pp.29–38
(2019).https://doi.org/10.1145/3287560.3287590
Lai,V.,Chen,C.,Smith-Renner,A.,etal.:Towardsascienceofhuman–AIdecisionmaking:Anoverview
ofdesignspaceinempiricalhuman-subjectstudies.In:Proceedingsofthe2023ACMConferenceon
Fairness,Accountability,andTransparency.AssociationforComputingMachinery,NewYork,NY,
USA,FAccT’23,pp.1369–1385(2023a).https://doi.org/10.1145/3593013.3594087
Lai,V.,Zhang,Y.,Chen,C.,etal.:Selectiveexplanations:leveraginghumaninputtoalignexplainableAI.
Proc.ACMHum.Comput.Interact.(2023b).https://doi.org/10.1145/3610206
Lee,M.H.,Siewiorek,D.P.,Smailagic,A.,etal.:Co-designandevaluationofanintelligentdecisionsupport
systemforstrokerehabilitationassessment.Proc.ACMHum.Comput.Interact.(2020).https://doi.
org/10.1145/3415227
Lee,M.H.,Siewiorek,D.P.,Smailagic,A.,etal.:Ahuman–AIcollaborativeapproachforclinicaldecision
makingonrehabilitationassessment.In:Proceedingsofthe2021CHIConferenceonHumanFactors
inComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).
https://doi.org/10.1145/3411764.3445472
Li,D.,Browne,G.:Theroleofneedforcognitionandmoodinonlineflowexperience.J.Comput.Inf.
Syst.46(3),11–17(2006)
123

3 Page 40 of 43 F.M.Cau,L.D.Spano
Li,J.,Yang,Y.,Liao,Q.V.,etal.:Asconfidencealigns:understandingtheeffectofaiconfidenceonhuman
self-confidenceinhuman–AIdecisionmaking.In:Proceedingsofthe2025CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’25
(2025).https://doi.org/10.1145/3706598.3713336
Liao,M.,Sundar,S.S.,Walther,B.J.:Usertrustinrecommendationsystems:acomparisonofcontent-based,
collaborative and demographic filtering. In: Proceedings of the 2022 CHI Conference on Human
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’22
(2022).https://doi.org/10.1145/3491102.3501936
Liao,Q.V.,Varshney,K.R.:Human-centeredexplainableAI(XAI):fromalgorithmstouserexperiences
(2021)
Litman,J.A.:Interestanddeprivationfactorsofepistemiccuriosity.Person.Indvid.Differ.44(7),1585–1595
(2008). https://doi.org/10.1016/j.paid.2008.01.014. (https://www.sciencedirect.com/science/article/
pii/S0191886908000275)
Lu,J.,Yan,Y.,Huang,K.,etal.:Dowelearnfromeachother:understandingthehuman–AIco-learning
processembeddedinhuman–AIcollaboration.GroupDecis.Negot.(2024).https://doi.org/10.1007/
s10726-024-09912-x
Lundberg,S.M.,Lee,S.I.:Aunifiedapproachtointerpretingmodelpredictions.In:Proceedingsofthe31st
InternationalConferenceonNeuralInformationProcessingSystems,CurranAssociatesInc.,Red
Hook,NY,USA,NIPS’17,pp.4768–4777(2017)
Ma,S.,Lei,Y.,Wang,X.,etal.:Whoshoulditrust:Aiormyself?Leveraginghumanandaicorrectness
likelihoodtopromoteappropriatetrustinAI-assisteddecision-making.In:Proceedingsofthe2023
CHIConferenceonHumanFactorsinComputingSystems.AssociationforComputingMachinery,
NewYork,NY,USA,CHI’23(2023).https://doi.org/10.1145/3544548.3581058
Ma,S.,Wang,X.,Lei,Y.,etal.:“areyoureallysure?”Understandingtheeffectsofhumanself-confidence
calibrationinai-assisteddecisionmaking.In:Proceedingsofthe2024CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’24
(2024).https://doi.org/10.1145/3613904.3642671
Manokhin,V.:Multi-classprobabilisticclassificationusinginductiveandcrossVenn–Aberspredictors.In:
Gammerman,A.,Vovk,V.,Luo,Z.,etal.(eds),ProceedingsoftheSixthWorkshoponConformal
andProbabilisticPredictionandApplications,ProceedingsofMachineLearningResearch,vol.60.
PMLR,pp.228–240(2017).https://proceedings.mlr.press/v60/manokhin17a.html
Martijn,M.,Conati,C.,Verbert,K.:“knowingme,knowingyou”:personalizedexplanationsforamusic
recommendersystem.UserModel.UserAdap.Int.32(1),215–252(2022).https://doi.org/10.1007/
s11257-021-09304-9
Marusich, L.R., Bakdash, J.Z., Zhou, Y., et al.: Using ai uncertainty quantification to improve human
decision-making. In: Proceedings of the 41st International Conference on Machine Learning.
JMLR.org,ICML’24(2024)
Millecamp,M.,Htun,N.N.,Conati,C.,etal.:Toexplainornottoexplain:theeffectsofpersonalcharacter-
isticswhenexplainingmusicrecommendations.In:Proceedingsofthe24thInternationalConference
onIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’19,
pp.397–407(2019).https://doi.org/10.1145/3301275.3302313
Millecamp,M.,Htun,N.N.,Conati,C.,etal.:What’sinauser?Towardspersonalisingtransparencyfor
musicrecommenderinterfaces.In:Proceedingsofthe28thACMConferenceonUserModeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’20,pp.173–182(2020).https://doi.org/10.1145/3340631.3394844
Moreira,C.,Chou,Y.L.,Hsieh,C.J.,etal.:BenchmarkingcounterfactualalgorithmsforXAI:fromwhite
boxtoblackbox(2022).https://api.semanticscholar.org/CorpusID:252280631
Morrison,K.,Spitzer,P.,Turri,V.,etal.:TheimpactofimperfectXAIonhuman–AIdecision-making.
Proc.ACMHum.Comput.Interact.(2024).https://doi.org/10.1145/3641022
Mothilal,R.,Sharma,A.,Tan,C.:ExplainingMachineLearningClassifiersThroughDiverseCounterfactual
Explanations,pp.607–617(2020a).https://doi.org/10.1145/3351095.3372850
Mothilal,R.K.,Sharma,A.,Tan,C.:Explainingmachinelearningclassifiersthroughdiversecounterfactual
explanations.In:Proceedingsofthe2020ConferenceonFairness,Accountability,andTransparency.
AssociationforComputingMachinery,NewYork,NY,USA,FAT*’20,pp.607–617(2020b).https://
doi.org/10.1145/3351095.3372850
Mothilal, R.K., Mahajan, D., Tan, C., et al.: Towards unifying feature attribution and counterfactual
explanations: different means to the same end. In: AAAI/ACM Conference on AI, Ethics, and
123

ExploringtheimpactofexplainableAIandcognitive… Page 41 of 43 3
Society (AIES) (2021). https://www.microsoft.com/en-us/research/publication/towards-unifying-
feature-attribution-and-counterfactual-explanations-different-means-to-the-same-end/
Musto,C.,Starke,A.D.,Trattner,C.,etal.:Exploringtheeffectsofnaturallanguagejustificationsinfood
recommendersystems.In:Proceedingsofthe29thACMConferenceonUserModeling,Adaptation
andPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP’21,pp.
147–157(2021).https://doi.org/10.1145/3450613.3456827
Nourani,M.,Roy,C.,Block,J.E.,etal.:Anchoringbiasaffectsmentalmodelformationanduserreliance
inexplainableAIsystems.In:Proceedingsofthe26thInternationalConferenceonIntelligentUser
Interfaces.AssociationforComputingMachinery,NewYork,NY,USA,IUI’21,pp.340–350(2021).
https://doi.org/10.1145/3397481.3450639
Padilla, L.M.K., Powell, M., Kay, M., et al.: Uncertain about uncertainty: how qualitative expres-
sions of forecaster confidence impact decision-making with uncertainty visualizations. Front.
Psychol. (2021). https://doi.org/10.3389/fpsyg.2020.579267. (https://www.frontiersin.org/journals/
psychology/articles/10.3389/fpsyg.2020.579267)
Panigutti,C.,Beretta,A.,Giannotti,F.,etal.:Understandingtheimpactofexplanationsonadvice-taking:a
userstudyforai-basedclinicaldecisionsupportsystems.In:Proceedingsofthe2022CHIConference
onHumanFactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,
USA,CHI’22(2022).https://doi.org/10.1145/3491102.3502104
Platt,J.:ProbabilitiesforSupportVectorMachines(2000)
Prabhudesai,S.,Yang,L.,Asthana,S.,etal.:Understandinguncertainty:howlaydecision-makersperceive
andinterpretuncertaintyinhuman–AIdecisionmaking.In:Proceedingsofthe28thInternational
ConferenceonIntelligentUserInterfaces.AssociationforComputingMachinery,NewYork,NY,
USA,IUI’23,pp.379–396(2023).https://doi.org/10.1145/3581641.3584033
Rastogi,C.,Zhang,Y.,Wei,D.,etal.:Decidingfastandslow:theroleofcognitivebiasesinai-assisted
decision-making.Proc.ACMHum.Comput.Interact.(2022).https://doi.org/10.1145/3512930
Rechkemmer,A.,Yin,M.:Whenconfidencemeetsaccuracy:exploringtheeffectsofmultipleperformance
indicatorsontrustinmachinelearningmodels.In:Proceedingsofthe2022CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’22
(2022).https://doi.org/10.1145/3491102.3501967
Ribeiro,M.T.,Singh,S.,Guestrin,C.:“whyshoulditrustyou?”:explainingthepredictionsofanyclassifier.
In:Proceedingsofthe22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryand
DataMining.AssociationforComputingMachinery,NewYork,NY,USA,KDD’16,pp.1135–1144
(2016).https://doi.org/10.1145/2939672.2939778
Ribeiro, M.T., Singh, S., Guestrin, C.: Anchors: high-precision model-agnostic explanations. In: Pro-
ceedingsoftheThirty-SecondAAAIConferenceonArtificialIntelligenceandThirtiethInnovative
Applications of Artificial Intelligence Conference and Eighth AAAI Symposium on Educational
AdvancesinArtificialIntelligence.AAAIPress,AAAI’18/IAAI’18/EAAI’18(2018)
Rong,Y.,Leemann,T.,Nguyen,T.,etal.:Towardshuman-centeredexplainableAI:asurveyofuserstudies
formodelexplanations.IEEETrans.PatternAnal.Mach.Intell.46(04),2104–2122(2024).https://
doi.org/10.1109/TPAMI.2023.3331846
Salimzadeh,S.,He,G.,Gadiraju,U.:Amissingpieceinthepuzzle:consideringtheroleoftaskcomplexity
in human–AI decision making. In: Proceedings of the 31st ACM Conference on User Modeling,
AdaptationandPersonalization.AssociationforComputingMachinery,NewYork,NY,USA,UMAP
’23,pp.215–227(2023).https://doi.org/10.1145/3565472.3592959
Salimzadeh,S.,He,G.,Gadiraju,U.:Dealingwithuncertainty:Understandingtheimpactofprognostic
versusdiagnostictasksontrustandrelianceinhuman–AIdecisionmaking.In:Proceedingsofthe
CHIConferenceonHumanFactorsinComputingSystems.AssociationforComputingMachinery,
NewYork,NY,USA,CHI’24(2024).https://doi.org/10.1145/3613904.3641905
Sauro,J.,Dumas,J.S.:Comparisonofthreeone-question,post-taskusabilityquestionnaires.In:Proceedings
oftheSIGCHIConferenceonHumanFactorsinComputingSystems.AssociationforComputing
Machinery,NewYork,NY,USA,CHI’09,pp.1599–1608(2009).https://doi.org/10.1145/1518701.
1518946
Scharowski,N.,Perrig,S.A.C.,Svab,M.,etal.:Exploringtheeffectsofhuman-centeredAIexplanationson
trustandreliance.Front.Comput.Sci.(2023).https://doi.org/10.3389/fcomp.2023.1151150.https://
www.frontiersin.org/articles/10.3389/fcomp.2023.1151150
Schoeffer,J.,Kuehl,N.,Machowski,Y.:“thereisnotenoughinformation”:ontheeffectsofexplanations
onperceptionsofinformationalfairnessandtrustworthinessinautomateddecision-making.In:Pro-
123

3 Page 42 of 43 F.M.Cau,L.D.Spano
ceedingsofthe2022ACMConferenceonFairness,Accountability,andTransparency.Association
forComputingMachinery,NewYork,NY,USA,FAccT’22,pp.1616–1628(2022).https://doi.org/
10.1145/3531146.3533218
Shaker,M.H.,Hüllermeier,E.:Aleatoricandepistemicuncertaintywithrandomforests.In:Berthold,M.R.,
Feelders,A.,Krempl,G.(eds.)AdvancesinIntelligentDataAnalysisXVIII,pp.444–456.Springer,
Cham(2020)
SilvaFilho,T.,Song,H.,Perello-Nieto,M.,etal.:Classifiercalibration:asurveyonhowtoassessand
improvepredictedclassprobabilities.Mach.Learn.112(9),3211–3260(2023).https://doi.org/10.
1007/s10994-023-06336-7
Souchet,A.,Amokrane-Ferka,K.,Burkhardt,J.M.:Ai-assistancetodecision-makers:evaluatingusability,
inducedcognitiveload,andtrust’simpact.In:ProceedingsoftheEuropeanConferenceonCognitive
Ergonomics2024.AssociationforComputingMachinery,NewYork,NY,USA,ECCE’24(2024).
https://doi.org/10.1145/3673805.3673845
Steyvers,M.,Kumar,A.:ThreechallengesforAI-assisteddecision-making.Perspect.Psychol.Sci.19(5),
722–734(2024).https://doi.org/10.1177/17456916231181102
Strickland,L.,Farrell,S.,Wilson,M.K.,etal.:Howdohumanslearnaboutthereliabilityofautomation?
Cogn.Res.Princ.Implic.9(1),8(2024).https://doi.org/10.1186/s41235-024-00533-1
Subramanian, H.V., Canfield, C., Shank, D.B.: Designing explainable ai to improve human-
ai team performance: a medical stakeholder-driven scoping review. Artif. Intell. Med.
149,102780(2024).https://doi.org/10.1016/j.artmed.2024.102780.https://www.sciencedirect.com/
science/article/pii/S0933365724000228
Swaroop,S.,Buçinca,Z.,Gajos,K.Z.,etal.:PersonalisingaiassistancebasedonoverreliancerateinAI-
assisteddecisionmaking.In:Proceedingsofthe30thInternationalConferenceonIntelligentUser
Interfaces. Association for ComputingMachinery, New York, NY, USA, IUI ’25, pp. 1107–1122
(2025).https://doi.org/10.1145/3708359.3712128
Szymanski,M.,AbeeleV.V.,Verbert,K.:Designingandevaluatingexplanationsforapredictivehealth
dashboard:auser-centredcasestudy.In:ExtendedAbstractsofthe2024CHIConferenceonHuman
FactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHIEA
’24(2024).https://doi.org/10.1145/3613905.3637140
Teso, S., Alkan, Ö., Stammer, W., et al.: Leveraging explanations in interactive machine learning: an
overview.Front.Artif.Intell.6,1066049(2023)
Tsirtsis, S., Gomez-Rodriguez, M., Gerstenberg, T.: Towards a computational model of responsibility
judgmentsinsequentialhuman-aicollaboration.In:Proceedingsofthe46thAnnualMeetingofthe
CognitiveScienceSociety(CogSci2024),Rotterdam,Netherlands(2024).https://escholarship.org/
uc/item/5h1742zk
vanBerkel,N.,Goncalves,J.,Russo,D.etal.:Effectofinformationpresentationonfairnessperceptions
ofmachinelearningpredictors.In:Proceedingsofthe2021CHIConferenceonHumanFactorsin
ComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,CHI’21(2021).
https://doi.org/10.1145/3411764.3445365
Vasconcelos,H.,Jörke,M.,Grunde-McLaughlin,M.,etal.:Explanationscanreduceoverrelianceonai
systemsduringdecision-making.ProcACMHum.Comput.Interact.(2023).https://doi.org/10.1145/
3579605
Viswanathan,S.,Omidvar-Tehrani,B.,Renders,J.M.:Whatisyourcurrentmindset?In:Proceedingsof
the 2022 CHI Conference on Human Factors in Computing Systems. Association for Computing
Machinery,NewYork,NY,USA,CHI’22(2022).https://doi.org/10.1145/3491102.3501912
Vovk,V.,Petej,I.:Venn-aberspredictors.In:ProceedingsoftheThirtiethConferenceonUncertaintyin
ArtificialIntelligence.AUAIPress,Arlington,Virginia,USA,UAI’14,pp.829–838(2014)
Vovk,V.,Petej,I.,Fedorova,V.:Large-scaleprobabilisticpredictorswithandwithoutguaranteesofvalidity.
In: Proceedings of the 28th International Conference on Neural Information Processing Systems,
Volume1.MITPress,Cambridge,MA,USA,NIPS’15,pp.892–900(2015)
Wachter,S.,Mittelstadt,B.D.,Russell,C.:Counterfactualexplanationswithoutopeningtheblackbox:
automateddecisionsandtheGDPR.Cybersecurity(2017).https://api.semanticscholar.org/CorpusID:
3995299
Wang,D.,Yang,Q.,Abdul,A.,etal.:Designingtheory-drivenuser-centricexplainableai.In:Proceedings
ofthe2019CHIConferenceonHumanFactorsinComputingSystems.AssociationforComputing
Machinery,NewYork,NY,USA,CHI’19,pp.1–15(2019).https://doi.org/10.1145/3290605.3300831
123

ExploringtheimpactofexplainableAIandcognitive… Page 43 of 43 3
Wang,X.,Yin,M.:Areexplanationshelpful?Acomparativestudyoftheeffectsofexplanationsinai-
assisteddecision-making.In:26thInternationalConferenceonIntelligentUserInterfaces.Association
forComputingMachinery,NewYork,NY,USA,IUI’21,pp.318–328(2021).https://doi.org/10.1145/
3397481.3450650
Wang,X.,Yin,M.:EffectsofexplanationsinAI-assisteddecisionmaking:principlesandcomparisons.
ACMTrans.Interact.Intell.Syst.(2022).https://doi.org/10.1145/3519266
Xuan,Y.,Small,E.,Sokol,K.,etal.:Comprehensionisadouble-edgedsword:over-interpretingunspeci-
fiedinformationinintelligiblemachinelearningexplanations.Int.J.HumComputStud.193,103376
(2025). https://doi.org/10.1016/j.ijhcs.2024.103376. https://www.sciencedirect.com/science/article/
pii/S1071581924001599
Yin,M.,Vaughan,W.J.,Wallach,H.:Understandingtheeffectofaccuracyontrustinmachinelearning
models. In: Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems.
AssociationforComputingMachinery,NewYork,NY,USA,CHI’19,pp.1–12(2019).https://doi.
org/10.1145/3290605.3300509
Yurrita,M.,Draws,T.,Balayn,A.,etal.:Disentanglingfairnessperceptionsinalgorithmicdecision-making:
theeffectsofexplanations,humanoversight,andcontestability.In:Proceedingsofthe2023CHI
ConferenceonHumanFactorsinComputingSystems.AssociationforComputingMachinery,New
York,NY,USA,CHI’23(2023).https://doi.org/10.1145/3544548.3581161
Yurrita,M.,Verma,H.,Balayn,A.,etal.:Towardseffectivehumaninterventioninalgorithmicdecision-
making:Understandingtheeffectofdecision-makers’configurationondecision-subjects’fairness
perceptions.In:Proceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems.
AssociationforComputingMachinery,NewYork,NY,USA,CHI’25(2025).https://doi.org/10.1145/
3706598.3713145
Zadrozny,B.,Elkan,C.:ObtainingcalibratedprobabilityestimatesfromdecisiontreesandnaiveBayesian
classifiers.ICML,p.1(2001)
Zehrung,R.,Singhal,A.,Correll,M.,etal.:Visexmachina:ananalysisoftrustinhumanversusalgorith-
micallygeneratedvisualizationrecommendations.In:Proceedingsofthe2021CHIConferenceon
HumanFactorsinComputingSystems.AssociationforComputingMachinery,NewYork,NY,USA,
CHI’21(2021).https://doi.org/10.1145/3411764.3445195
Zhang, Y., Liao, Q.V., Bellamy, R.K.E.: Effect of confidence and explanation on accuracy and trust
calibration in ai-assisted decision making. In: Proceedings of the 2020 Conference on Fairness,
Accountability,andTransparency.AssociationforComputingMachinery,NewYork,NY,USA,FAT*
’20,pp.295–305.(2020).https://doi.org/10.1145/3351095.3372852
Zhao,J.,Wang,Y.,Mancenido,M.V.,etal.:Evaluatingtheimpactofuncertaintyvisualizationonmodel
reliance.IEEETrans.VisualComput.Gr.30(7),4093–4107(2024).https://doi.org/10.1109/TVCG.
2023.3251950
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmaps
andinstitutionalaffiliations.
FedericoMariaCauobtainedhisbachelor’sandmaster’sdegreesfromtheUniversityofCagliari,where
healsoearnedaPh.D.inMathematicsandComputerScience,withafocusontheeffectsofexplanation
anduncertaintyonAI-assisteduserdecisions.HeiscurrentlyapostdoctoralresearcherattheUniversity
ofCagliari.HisresearchinterestsincludeAI-assisteddecision-making,explainableAI,Human-Centered
AI,andintelligentinterfaces.
LucioDavideSpanoisanAssociateProfessorattheUniversityofCagliari,Italy,wherehehasbeenpart
oftheDepartmentofMathematicsandComputerSciencesince2012.HeearnedhisPh.D.inComputer
SciencefromtheUniversityofPisain2013.HisresearchfocusesonHuman-ComputerInteraction(HCI),
extendedReality(XR),End-UserDevelopment,andexplainableAI.Hehasauthorednumerouspublica-
tionsoninteractiontechniques,intelligentuserinterfaces,andimmersivetechnologies.Spanohasledand
contributedtovariousEuropeanandregionalresearchprojects,includingthoseunderH2020,FP7,andthe
ItalianPNRRframework.HeisactiveintheinternationalHCIcommunity,servingonprogramcommit-
teesforconferencessuchasACMIUI,INTERACT,NordiCHI,andEICS,andholdsleadershiprolesin
IFIPandSIGCHI-Italy.
123