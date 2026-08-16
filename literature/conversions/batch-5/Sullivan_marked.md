---
conversion_metadata:
  converted_at: "2026-07-21T08:53:49Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Sullivan.pdf"
  source_pdf_sha256: "717296693bc939f485c7d8de741cfd066dcde0373d144d602e2ce8420fa04c99"
  page_count: 24
  markdown_char_count: 83079
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

COMPREHENDING LEVELS OF EXPLAINABILITY AND AI 
RECOMMENDATIONS (CLEAR) STUDY SERIES

Virginia Sullivan

A DISSERTATION

Submitted in partial fulfillment of the requirements 
for the degree of Doctor of Philosophy 
in 
Applied Experimental Psychology 
to 
The Graduate School 
of 
The University of Alabama in Huntsville 
May 2026

Approved by:

Dr. Kristin Weger, Research Advisor & Committee Chair 
Dr. Jodi Price, Committee Member 
Dr. Lauren Meaux, Committee Member 
Dr. Bryan Mesmer, Committee Member 
Dr. Vineetha Menon, Committee Member 
Dr. Daniel Krenn, Committee Member 
Dr. Daniel Morrison, Interim Department Chair 
Dr. Jodi Price, College Dean 
Dr. Jon Hakkila, Graduate Dean

---

<!-- PAGE 2 -->

Abstract

COMPREHENDING LEVELS OF EXPLAINABILITY AND AI 
RECOMMENDATIONS (CLEAR) STUDY SERIES

Virginia Sullivan, M.A.

A dissertation submitted in partial fulfillment of the requirements 
for the degree of Doctor of Philosophy

Applied Experimental Psychology – Human Factors

The University of Alabama in Huntsville 
May 2026

Artificial Intelligence (AI) systems can offer a great deal to improve decision-making

through efficiency and predictive accuracy due to their unique ability to rapidly analyze large

amounts of data relevant to the decision. Yet many AI systems remain opaque, limiting users’

ability to evaluate outputs and leading to issues of mistrust or over-reliance. This dissertation

investigates how varying levels of AI explainability affect trust, perceived reliability,

understanding, and confidence, and identifies perceptual and behavioral indicators of over-

reliance behavior in AI-assisted decision-making scenarios. This dissertation is organized as a

three-study series. The CLEAR survey study uses a mixed design to examine the impact of

explanation depth on trust-related outcomes. Participants engage with AI-assisted decision

scenarios and respond to measures of trust, perceived reliability, confidence in the accuracy of

the AI, and understanding of the explanation. Scenario context is also evaluated as a potential

moderator. Study 2 builds on this by constructing an Over-Reliance Index (ORI), a combined

measure of potential over-reliance built on user perceptions that are related to reliance behavior

ii

---

<!-- PAGE 3 -->

in previous literature. Using data from the CLEAR survey, this study identifies dispositional and

contextual predictors of over-reliance and employs regression analysis to examine differences in

reliance behaviors by explanation complexity level and cluster analysis to reveal user profiles.

The CLEAR-Engage study shifts from self-report to decision behavior by examining responses

to AI recommendations within a simulated, screenshot-based decision-making task. Participants

completed a hostage-rescue task in which they were presented with varying levels of AI support.

Behavioral measures (e.g., agreement with AI recommendations and detection of AI errors),

along with self-report measures of trust and understanding, were used to validate the ORI and

identify behavioral markers of over-reliance. Together, these studies aim to advance

understanding of explainability’s role in trust calibration, establish behavioral measures of over-

reliance, and inform the design of user-centered AI systems that support effective human-AI

teaming in a variety of contexts.

iii

---

<!-- PAGE 4 -->

I have followed the approved guidelines of my graduate program and the UAH Graduate

School for the use of generative Artificial Intelligence (AI) in the writing of this dissertation. The

following generative AI tools were used for the associated purpose(s) listed after each tool:

ChatGPT: Scenario generation in the CLEAR survey study. Revising, editing, and

proofreading text for clarity and coherence.

iv

---

<!-- PAGE 5 -->

Acknowledgements

I am incredibly lucky to have many generous and encouraging people in my life, without

whom I would not have been able to complete this dissertation. First and foremost, I would like

to thank my parents, Elroy and Debra Sullivan, for their constant encouragement and support

throughout my Ph.D., for always encouraging me to follow my curiosities, and for creating a

home that fostered open and meaningful discourse on any subject. Those conversations are what

led me to pursue a career in research and higher education.

I would also like to thank my fiancé, Dylan Pietzsch, without whose support and

encouragement this dissertation would not have been possible. Through studying for

comprehensive exams, late nights coding, and long writing sessions, he was a constant source of

reassurance and made sure everything else was taken care of so I could focus on my work. I hope

that one day I can repay the incredible gift of easing life’s worries, and I cannot wait to be Dr.

Pietzsch.

This project would not exist, nor be as strong as it is, without the support of my advisor,

Dr. Kristin Weger. I am very fortunate to have found an advisor who supported my ideas, gave

me the space to create my own path in research, and ensured that my work met the highest

standards. For that, I am deeply grateful. I would also like to thank my committee members for

their time, feedback, and thoughtful engagement with this work. I am also grateful to the

undergraduate students who worked with me on this project, especially Maggie Glass, for their

collaboration, feedback, and willingness to pilot and refine study materials. Many of my close

family and friends also completed my surveys and shared them with others without hesitation. I

am beyond grateful for their generosity and support.

v

---

<!-- PAGE 6 -->

Completing this dissertation required more resilience and growth than I anticipated, and I

am proud of the perseverance it represents. Lastly, I would like to thank my dogs, Eevee and

Jack, for the comfort, joy, and anxiety-relieving cuddles that carried me through this process.

vi

---

<!-- PAGE 7 -->

Table of Contents

Abstract .......................................................................................................................................... ii

Acknowledgements ....................................................................................................................... v

Table of Contents ........................................................................................................................ vii

List of Figures ............................................................................................................................. xiii

List of Tables ............................................................................................................................... xv

Epigraph ..................................................................................................................................... xvi

Chapter 1.

Introduction ................................................................................................... 1

1.1

1.2

1.3

Artificial Intelligence ......................................................................................... 1

Explainable Artificial Intelligence ..................................................................... 4

Organization of the Dissertation ........................................................................ 5

Chapter 2.

Literature Review ......................................................................................... 8

2.1

2.2

Definitions and Terminology ............................................................................. 8

Computer Science XAI Techniques ................................................................. 10

2.2.1  Post-Hoc Explanations ................................................................................ 10

2.2.2

Intrinsically Interpretable Models ............................................................... 11

2.2.3  Bridging the Gap between Computer Science and Psychology .................. 12

2.3

Psychological and Cognitive Foundations ....................................................... 12

2.3.1  Cognitive Load Theory ............................................................................... 14

2.3.2  Complacency & Automation Bias ............................................................... 16

2.3.3  Trust Calibration ......................................................................................... 18

2.3.4  AI Reliance .................................................................................................. 21

2.3.5  Predictors of Over-Reliance ........................................................................ 22

2.4

Usability and Human Factors Principles .......................................................... 24

vii

---

<!-- PAGE 8 -->

2.5

Brief Summary of Literature ............................................................................ 26

Chapter 3.  Research Objective 1: CLEAR Survey on XAI Complexity ................... 27

3.1

Methodology .................................................................................................... 28

3.1.1  Participants .................................................................................................. 29

3.1.2  Materials ...................................................................................................... 29

3.1.2.1  Scenarios ........................................................................................... 30

3.1.2.2  Scenario Generation .......................................................................... 31

3.1.2.3  Outcome Measures ............................................................................ 32

3.1.2.4  User Experience and Expertise ......................................................... 34

3.1.3  Procedure ..................................................................................................... 35

3.2

3.3

Analysis Approach ........................................................................................... 36

Results .............................................................................................................. 37

3.3.1  Descriptive Statistics ................................................................................... 37

3.3.2  Correlational Analysis ................................................................................. 41

3.3.3  Primary Regression Analysis (H1a) ............................................................ 42

3.3.3.1  Trust .................................................................................................. 43

3.3.3.2  Perceived Reliability ......................................................................... 44

3.3.3.3  Confidence in the AI ......................................................................... 44

3.3.3.4  Ease of Understanding of the AI Explanation................................... 45

3.3.3.5  Summary of H1a Results .................................................................. 45

3.3.4  Moderation Analysis (H1b) ......................................................................... 46

3.3.4.1  Trust .................................................................................................. 46

3.3.4.2  Perceived Reliability ......................................................................... 47

3.3.4.3  Confidence in the Accuracy of the AI............................................... 47

3.3.4.4  Ease of Understanding of the AI explanation ................................... 48

viii

---

<!-- PAGE 9 -->

3.3.4.5  Summary of Moderation Analysis .................................................... 49

3.3.5  Order Effects ............................................................................................... 49

3.3.6  Robustness and Exploratory Demographic Analyses ................................. 50

3.4

Discussion ........................................................................................................ 50

3.4.1  Scenario-Specific Effects ............................................................................ 51

3.4.2  Limitations and Future Directions ............................................................... 52

3.4.3  Design Implications ..................................................................................... 52

Chapter 4.  Research Objective 2: Identifying Predictors of Over-Reliance ............ 54

4.1

Methodology .................................................................................................... 55

4.1.1  Participants .................................................................................................. 55

4.1.2  Materials ...................................................................................................... 56

4.1.3  Procedure ..................................................................................................... 57

4.1.4  ORI Construction ........................................................................................ 58

4.2

4.3

Analysis Approach ........................................................................................... 58

Results .............................................................................................................. 60

4.3.1  Descriptive Statistics ................................................................................... 60

4.3.1.1

Information-Seeking Behavior .......................................................... 60

4.3.1.2  Habitual AI Use................................................................................. 61

4.3.1.3  AI Agreement .................................................................................... 62

4.3.2  ORI Construction ........................................................................................ 62

4.3.3  Demographic Differences in ORI Scores and Agreement .......................... 64

4.3.4  ORI Dimensions and ORI Scores (H2a) ..................................................... 65

4.3.4.1  Correlational Analysis ....................................................................... 65

4.3.4.2  Multiple Linear Regression ............................................................... 66

4.3.5  Explanation Complexity and ORI Scores (H2b) ......................................... 67

ix

---

<!-- PAGE 10 -->

4.3.6  Exploratory Cluster Analysis ...................................................................... 68

4.4

Discussion ........................................................................................................ 70

4.4.1  The Relationship Between Confidence and Understanding (H2a) ............. 70

4.4.2  Explanation Complexity and Over-Reliance (H2b) .................................... 72

4.4.3  Cluster Analysis: Reliance Groups ............................................................. 73

4.4.4  Theoretical and Design Implications ........................................................... 73

4.4.5  Limitations and Future Directions ............................................................... 74

Chapter 5.  Research Objective 3: CLEAR-Engage (Comprehending Levels of 
Explainability and AI Recommendations – Engagement with Explanations) ............... 76

5.1

Methodology .................................................................................................... 77

5.1.1  Participants .................................................................................................. 78

5.1.2  Materials ...................................................................................................... 79

5.1.2.1  Simulation Task ................................................................................ 79

5.1.2.2  Behavioral and Perceptual Measures ................................................ 80

5.1.3  Procedure ..................................................................................................... 81

5.2

5.3

Analysis Approach ........................................................................................... 83

Results .............................................................................................................. 85

5.3.1  Descriptive Statistics ................................................................................... 85

5.3.1.1  Trust, Perceived Reliability, Confidence, and Understanding .......... 85

5.3.1.2  Hostage Order & Agreement Ratings ............................................... 86

5.3.1.3  Propensity to Trust AI ....................................................................... 88

5.3.1.4  AI Familiarity, Information-Seeking, and Habitual AI Use ............. 89

5.3.2  Behavioral ORI Construction ...................................................................... 91

5.3.3  Perceptual ORI Construction ...................................................................... 92

5.3.4  Correlations between Key Variables ........................................................... 93

5.3.5  Behavioral Patterns and Reliance (H3a) ..................................................... 94

x

---

<!-- PAGE 11 -->

5.3.6  Explanation Complexity and Reliance (H3b) ............................................. 95

5.3.6.1  Behavioral Agreement with AI Recommendations .......................... 95

5.3.6.2  Perceived Understanding and Information Sufficiency .................... 96

5.3.6.3  Summary of H3b Results .................................................................. 97

5.3.7  Behavioral and Perceptual ORI Convergent Validity ................................. 97

5.3.8  Order Effects ............................................................................................... 98

5.3.9  Robustness and Student Differences ........................................................... 99

5.3.10  Exploratory Analysis ............................................................................... 100

5.3.10.1  Minimal vs. Complex Explanation Preferences ............................ 100

5.3.10.2  Helpful Aspects of the Complex Explanation ............................... 100

5.3.10.3  Most Helpful Explanation Aspects Overall .................................. 101

5.4

Discussion ...................................................................................................... 101

5.4.1  Behavioral Patterns and Reliance (H3a) ................................................... 102

5.4.2  Explanation Complexity and Reliance Behavior (H3b) ............................ 102

5.4.3  Convergent Validity of Behavioral and Perceptual ORI (H3c) ................ 103

5.4.4  Explanation Preferences ............................................................................ 103

5.4.5  Limitations and Future Directions ............................................................. 104

5.4.6  Theoretical and Design Implications ......................................................... 105

5.4.6.1  Theoretical Implications.................................................................. 105

5.4.6.2  Design Implications ........................................................................ 106

Chapter 6.  General Discussion .................................................................................... 107

6.1

Integrating Perceptual and Behavioral Findings ............................................ 107

6.1.1  Refining and Measuring Over-Reliance .................................................... 108

6.1.2  The Inverted-U Hypothesis ....................................................................... 109

6.2

Overall Practical and Applied Implications ................................................... 110

xi

---

<!-- PAGE 12 -->

6.2.1  Research Implications ............................................................................... 110

6.2.2

Industry and Practice Implications ............................................................ 111

6.3

6.4

Limitations and Delimitations ........................................................................ 112

Scope and Delimitations ................................................................................ 113

Chapter 7.

Intellectual Merit ...................................................................................... 114

Chapter 8.  Conclusion ................................................................................................. 117

8.1

8.2

Summary ........................................................................................................ 117

Statement on the Use of Generative Artificial Intelligence ........................... 117

References .................................................................................................................................. 119

Appendix A.

CLEAR Survey Scenarios ........................................................................... 130

Appendix B.

Propensity to Trust ...................................................................................... 137

Appendix C.

CLEAR Survey Scenario Questions ........................................................... 139

Appendix D.

UTAUT Items ............................................................................................... 144

Appendix E.

Study 3 Trial Images .................................................................................... 145

Appendix F.

Trial Items .................................................................................................... 150

xii

---

<!-- PAGE 13 -->

List of Figures

Figure 1.1 Organization of the Dissertation and Study Flow. ....................................................... 7

Figure 2.1 Visual Representation of Trust Calibration taken from de Visser et al. (2014). ........ 19

Figure 2.2 Visualization of the Potential Inverted-U Pattern. ..................................................... 20

Figure 3.1 Means and Standard Deviations for Each of the Dependent Variables ...................... 38

Figure 3.2 Effects of Explanations on Outcomes Across Scenarios ............................................ 39

Figure 3.3 Distribution of Scores on the Propensity to Trust Technology Scale ........................ 40

Figure 3.4 Distribution of Scores on Familiarity with AI Items .................................................. 41

Figure 3.5 Spearman Rank-Order Correlation Coefficients between Study Variables ............... 42

Figure 4.1 Distribution of ORI Scores ......................................................................................... 64

Figure 4.2 Changes in ORI Scores across Explanation Complexity Levels. ............................... 68

Figure 4.3 Scree Plot .................................................................................................................... 69

Figure 4.4 Raincloud Plot Representing 3 Distinct AI Reliance Groups..................................... 69

Figure 5.1 Means and Standard Deviations for Trust, Reliability, Confidence, and 
Understanding ............................................................................................................................... 86

Figure 5.2 First-Selected Hostage for Each Trial and Scene ....................................................... 87

Figure 5.3 Participant Agreement with AI-Recommended Hostage Rescue Order .................... 88

Figure 5.4 Distribution of Scores on the Propensity to Trust AI Scale. ...................................... 89

Figure 5.5 Distribution of Scores on the Self-Report Item Assessing Participant Familiarity  
with AI Systems. ........................................................................................................................... 90

Figure 5.6 Distribution of Normalized (z-scored) Behavioral ORI Scores. ................................ 92

Figure 5.7 Distribution of Perceptual ORI Scores in Study 3. ..................................................... 93

Figure 5.8 Pearson’s Correlations Between Study Variables ...................................................... 94

Figure 5.9 Visual Representation of the Relationship Between Perceptual and Behavioral  
ORI Scores. ................................................................................................................................... 98

xiii

---

<!-- PAGE 14 -->

Figure A.1 Visual Shown to Participants in the High Complexity, Résumé Screening  
Scenario....................................................................................................................................... 134

Figure E.1 Scene 1 Visual Shown to Participants with No AI Recommendation. .................... 145

Figure E.2 Scene 1 Visual Shown to Participants with Best AI Recommended Path. .............. 145

Figure E.3 Scene 1 Visual Shown to Participants with Best AI Recommended Path and 
Explanation. ................................................................................................................................ 146

Figure E.4 Scene 1 Visual Shown to Participants with Alternate AI Recommended Path. ...... 146

Figure E.5 Scene 1 Visual Shown to Participants with Alternate AI Recommended Path and 
Explanation. ................................................................................................................................ 147

Figure E.6 Scene 2 Visual Shown to Participants with No AI Recommendation. .................... 147

Figure E.7 Scene 2 Visual Shown to Participants with Best AI Recommended Path. .............. 148

Figure E.8 Scene 2 Visual Shown to Participants with Best AI Recommended Path and 
Explanation. ................................................................................................................................ 148

Figure E.9 Scene 2 Visual Shown to Participants with Alternate AI Recommended Path. ...... 149

Figure E.10 Scene 2 Visual Shown to Participants with Alternate AI Recommended Path and 
Explanation. ................................................................................................................................ 149

xiv

---

<!-- PAGE 15 -->

List of Tables

Table 2.1 Key Features of Three Critical Terms in AI Transparency............................................ 9

Table 3.1 Results of Regression Models Testing H1a ................................................................. 43

Table 4.1 Survey Items Used to Create the ORI .......................................................................... 56

Table 4.2 Descriptive Statistics for Information-Seeking Behavior. ........................................... 61

Table 4.3 Agreement Rates with the AI Decision by Explanation Level. ................................... 62

Table 5.1 Correlations Among Behavioral Predictors of Over-Reliance Behavior. .................... 95

xv

---

<!-- PAGE 16 -->

Epigraph

It is hoped that by trying to imitate the behavior of a human brain (or that of some other animal)

by means of an electronic device—or by failing to do so—one may learn something of

importance concerning the brain’s workings. Finally, there is the optimistic hope that for similar

reasons AI might have something to say about deep questions of philosophy, by providing

insights into the meaning of the concept of mind.

– Roger Penrose, The Emperor’s New Mind (1989)

xvi

---

<!-- PAGE 17 -->

Chapter 1.

Introduction

The purpose of this dissertation is to investigate the relationship between Explainable

Artificial Intelligence (XAI) complexity and user perceptions (trust, understanding, perceived

reliability, and accuracy confidence), as well as factors that lead to over-reliance and over-trust

in artificial intelligence (AI), despite explanation complexity. More specifically, this research

seeks to identify the conditions under which users accurately rely on recommendations from AI

versus when they over-rely (accepting AI output without sufficient understanding or

engagement). Across three interrelated studies, this project aims to determine the optimal level of

explainability for calibrating trust and reliability, develop a composite over-reliance index (ORI)

based on perceptual and behavioral indicators, and validate the ORI through tasks designed to

mimic real-world decision-making contexts. The findings will contribute to a more nuanced

understanding of XAI in human-AI interaction and inform XAI design that supports effective

and informed decision-making. Overall, this research aims to examine how different AI

explanations influence user perceptions and reliance behaviors across a variety of decision-

making contexts.

1.1

Artificial Intelligence

This dissertation closely examines user behaviors during their interactions with AI

systems. The idea of AI computational systems was conceived in the late 1940s and early 1950s,

and the idea was first fully conceptualized by Alan Turing (1950) when he asked the question,

“Can machines think?” in his landmark article, “Computing Machinery and Intelligence.” In

1

---

<!-- PAGE 18 -->

1956, scientists at Dartmouth University were inspired by Turing and the possibilities of artificial

intelligence and began a 6-week summer workshop aimed at creating machines capable of out-

smarting humans (Bostrom, 2014). Over the next six decades, progress in the field of artificial

intelligence ebbed and flowed and coincidingly investor interest and disinterest. A major change

in the field occurred in 2012 when Krizhevsky et al. (2012) published results of a deep

convolutional neural network (CNN) that vastly outperformed any prior models at visual

recognition. The findings of Krizhevsky et al. showed the power that deep learning could have to

transform AI and inspired applications of deep learning techniques across various other fields.

A second landmark finding came in 2014 when Goodfellow et al. introduced generative

adversarial nets (GANs), which use two neural networks to generate realistic text and images.

These seminal findings led to a boom in AI research and advancements in a wide range of fields.

In healthcare, a CNN was trained to identify skin cancer at a level comparable to dermatologists

(Esteva et al., 2017). Large language models (LLMs) were developed based on findings by

Vaswani et al. (2017) that improved performance and reduced training times. The AI systems

that resulted from these findings quickly became mainstream and have already had a profound

impact on the lives of many individuals and organizations. For example, a study on

automatization of jobs examined 702 occupations and found that around 47% of jobs in the US

are at a high risk of being automated within the next decade or two (Frey & Osborne, 2017).

Other researchers have examined the likely effects of AI on security, transportation, healthcare,

entertainment, and multiple other areas of life (Brundage et al., 2018; Dul, 2022; Mollick, 2024;

Stone et al., 2022).

These advances in AI technology have made it clear that AI systems have a broad range

of uses and applications. One particular advantage of AI that increases its usefulness in many of

2

---

<!-- PAGE 19 -->

these applications is its ability to quickly and effectively make decisions and provide information

to aid in the decision-making process. AI can offer a great deal to improved decision-making

through efficiency and predictive accuracy, due to its unique ability to rapidly analyze large

amounts of data relevant to a decision. The human brain also has the ability to process and

analyze data relevant to a decision, but there are limitations to the amount of data the brain is

able to process, especially in time critical situations (C. D. Wickens et al., 2015). The brain often

fills in gaps in knowledge and processing ability by using mental shortcuts (e.g., gestalt

organizational principles and heuristics) and will often attend to only salient, expected, or high

value information (Kahneman, 2011; Proctor & Van Zandt, 2018; J. R. Wickens et al., 2003). AI

excels where the human brain falls short due to its ability to rapidly process vast amounts of

information relevant to a decision.

However, there are challenges associated with the use of AI in decision-making.

Informed decision making requires consideration of shared understanding, user cognitive load,

automation bias, user trust, perceived reliability of the AI, and user confidence in the decision,

among other cognitive and computing considerations. It can be difficult for the user to feel their

decision is informed and well-made if the AI system is unable to provide information and

explanations that allow for shared understanding of context, consider cognitive load, and give the

information necessary for trust calibration and perceived reliability. Many AI systems operate as

so-called “black boxes,” where the logic behind decisions remains opaque even to developers, let

alone end-users. In this case an explanation describing how the system arrived at a decision can

provide needed context to the user.

3

---

<!-- PAGE 20 -->

1.2

Explainable Artificial Intelligence

One proposed solution to the challenges associated with human-AI decision making and

the need for explanation is the use of XAI. XAI refers to a broad class of approaches designed to

make the decision-making process of AI systems more transparent, interpretable, and

understandable to human users (Ghela et al., 2024). The field of XAI has received a great deal of

attention in recent years but remains in a state of flux. There is disagreement among computer

scientists, human-computer interaction (HCI) researchers, and psychologists about how to best

implement and visualize explanations to the user. The type and delivery method of explanations

should be context and function dependent due to the wide range of AI applications, but it must

also be trustworthy, understandable, and useful to the user, regardless of context or function.

Therefore, research must be done to measure user perceptions of AI that will aid in the design of

effective XAI systems.

Initially, XAI implementation largely relied on the assumption that increasing the amount

of explanations leads to enhanced user trust and understanding, as providing detailed

explanations can help users evaluate AI recommendations (Druce et al., 2021; Othman, 2025;

Waltl & Vogl, 2018). However, other research suggests that user perceptions have an inverted-U

relationship with explanation complexity (Abdul et al., 2020; Ghai et al., 2021; Walmsley,

2021). At high levels of complexity, some studies have shown that explanations begin to have a

negative impact on user perceptions (Abdul et al., 2020; Ghai et al., 2021; Walmsley, 2021).

Explanations that are too robust or overly complex can increase cognitive load, overwhelm users,

or paradoxically increase over-reliance on the AI system by creating a false sense of

understanding (Abdul et al., 2020; Ghai et al., 2021; Ngo, 2025; Walmsley, 2021).

4

---

<!-- PAGE 21 -->

Alternatively, the absence of explanations or explanations that are too simple may fail to

convey essential decision-making information, leaving users unable to judge the system’s

reliability (Choung et al., 2023; Parasuraman & Riley, 1997a). Ideally, users are able to obtain

the exact amount of information they need to reach a decision that is based on accurately

calibrated trust and perceived reliability of the system.

This dissertation addresses the critical need for user sensitive XAI frameworks that

promote calibrated trust and reliability based on appropriate user understanding and confidence

to inform user decision-making. Building on existing research in human factors and cognitive

psychology, this study series aims to examine how different levels of explanation complexity

affect user perceptions of trust, confidence, understanding, and perceived reliability, while also

identifying when those effects contribute to over-reliance behavior in human-AI decision making

interactions.

1.3  Organization of the Dissertation

This dissertation is organized into eight chapters that together build the Comprehending

Levels of Explainability and AI Recommendations (CLEAR) study series. The series integrates

three primary research objectives that examine how varying levels of explainability influence

user trust and reliance on AI systems.

Chapter 1 introduces the overarching topic, establishing the context of AI, XAI, and the

psychological foundations that motivate this research. The chapter concludes by outlining the

structure and objectives of the clear study series.

Chapter 2 presents a comprehensive literature review that bridges the computer science

and psychological perspectives of XAI. The chapter reviews relevant terminology and theoretical

5

---

<!-- PAGE 22 -->

frameworks that inform the design of the CLEAR study series and identifies critical gaps this

research aims to address.

Chapter 3 covers research objective 1, the CLEAR survey. The chapter begins by

defining the specific research questions and hypotheses associated with the CLEAR survey. The

overall objective of this study is to: determine the optimal amount of explanation complexity

(low, medium, high) that leads to accurately calibrated trust, reliance, understanding, and

confidence across a variety of decision-making scenarios, while examining variations in these

effects across contexts (scenarios). Methodology, analysis approach, results, and discussion for

the CLEAR survey are then outlined.

Chapter 4 covers research objective 2, the ORI and identifying predictors of over-reliance

behavior. The chapter begins by defining the specific research questions and hypotheses for the

ORI study. The overall objective of this study is to: identify when and why over-reliance on AI

occurs by developing a novel index (ORI) and to determine the impact of XAI on over-reliance.

Methodology, analysis approach, results, and discussion for the ORI study are then outlined.

Chapter 5 covers research objective 3, the CLEAR-Engage study. The chapter begins by

defining the specific research questions and hypotheses for the CLEAR-Engage study. The

overall objective of this study is to: validate the ORI using behavioral measures collected during

a simulated AI-assisted decision-making task, identify behavioral markers of over-reliance, and

examine how varying levels of explanation complexity influence reliance on AI

recommendations. Methodology, analysis approach, results, and discussion for the CLEAR-

Engage study are then outlined.

Chapter 6 covers the overall discussion for the implications of the CLEAR study series as

a whole and integrates findings across the three studies to discuss theoretical, methodological,

6

---

<!-- PAGE 23 -->

and practical implications for XAI design, trust calibration, and human-AI interaction.

Limitations are also addressed. Chapter 7 outlines the intellectual merit and broader impacts of

the research, situating its contributions within both theoretical and applied domains of Human-AI

Interaction and human factors psychology.

Chapter 8 concludes the dissertation by synthesizing contributions across the three

studies and articulating the cumulative impact of the CLEAR study series.

• Introduction and Literature

Review

• Defines context, theory, and

gaps leading to research 
objectives

Chapter 1-2: 
Foundations

Chapter 3-5: Research 
Framework

• Study 1 (CLEAR survey) -> 
Study 2 (ORI) -> Study 3 
(CLEAR-Engage)

• Describes research aims,

methods, analysis approach, 
results, and discussion

• Integrates theoretical and 
practical implications; 
concludes with contributions 
and future directions

Chapter 6-7: 
Discussion, Merit, & 
Conclusion

Figure 1.1 Organization of the Dissertation and Study Flow.

7

---

<!-- PAGE 24 -->

Chapter 2.  Literature Review

This review examines the current state of XAI from a human-centered perspective, with a

focus on how explanations are perceived, processed, and used in decision-making contexts.

Drawing on research from psychology, human factors, and human-AI interaction, the review

synthesizes findings related to cognitive load theory (CLT), trust in technology, automation bias,

and AI reliance behaviors, and identifies gaps in our understanding of how explanation design

influences user trust calibration and reliance behavior.

2.1

Definitions and Terminology

First, a preliminary overview of terms related to XAI research is provided. Inherently, AI

systems are typically “black box” systems, meaning that the inner workings of the system are

completely opaque. Ideally, XAI allows the inner workings of the system to become more

transparent to the user, sometimes referred to as “white box” AI. The term black box is not

unique to AI and has been used widely to describe what happens in between the input and output

of a system when the internal structure is unknown. In behavioral psychology, the mind can be

thought of as a black box because what is happening between the stimulus input and behavioral

output/reaction cannot be directly observed (Skinner, 1987). Neural network AI systems are

modeled on the brain and diffuse stored information in several complex networks that are

incredibly difficult to decipher, which makes their inner workings a black box, much like the

human mind (Castelvecchi, 2016). Neural network algorithms are exceptionally complex black

8

Reproduced with permission of copyright owner. Further reproduction prohibited without permission.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

COMPREHENDING LEVELS OF EXPLAINABILITY AND AI
RECOMMENDATIONS (CLEAR) STUDY SERIES

Virginia Sullivan

A DISSERTATION

Submitted in partial fulfillment of the requirements
for the degree of Doctor of Philosophy
in
Applied Experimental Psychology
to
The Graduate School
of
The University of Alabama in Huntsville
May 2026

Approved by:

Dr. Kristin Weger, Research Advisor & Committee Chair
Dr. Jodi Price, Committee Member
Dr. Lauren Meaux, Committee Member
Dr. Bryan Mesmer, Committee Member
Dr. Vineetha Menon, Committee Member
Dr. Daniel Krenn, Committee Member
Dr. Daniel Morrison, Interim Department Chair
Dr. Jodi Price, College Dean
Dr. Jon Hakkila, Graduate Dean

Abstract

COMPREHENDING LEVELS OF EXPLAINABILITY AND AI
RECOMMENDATIONS (CLEAR) STUDY SERIES

Virginia Sullivan, M.A.

A dissertation submitted in partial fulfillment of the requirements
for the degree of Doctor of Philosophy

Applied Experimental Psychology – Human Factors

The University of Alabama in Huntsville
May 2026

Artificial Intelligence (AI) systems can offer a great deal to improve decision-making

through efficiency and predictive accuracy due to their unique ability to rapidly analyze large

amounts of data relevant to the decision. Yet many AI systems remain opaque, limiting users’

ability to evaluate outputs and leading to issues of mistrust or over-reliance. This dissertation

investigates how varying levels of AI explainability affect trust, perceived reliability,

understanding, and confidence, and identifies perceptual and behavioral indicators of over-

reliance behavior in AI-assisted decision-making scenarios. This dissertation is organized as a

three-study series. The CLEAR survey study uses a mixed design to examine the impact of

explanation depth on trust-related outcomes. Participants engage with AI-assisted decision

scenarios and respond to measures of trust, perceived reliability, confidence in the accuracy of

the AI, and understanding of the explanation. Scenario context is also evaluated as a potential

moderator. Study 2 builds on this by constructing an Over-Reliance Index (ORI), a combined

measure of potential over-reliance built on user perceptions that are related to reliance behavior

ii

in previous literature. Using data from the CLEAR survey, this study identifies dispositional and

contextual predictors of over-reliance and employs regression analysis to examine differences in

reliance behaviors by explanation complexity level and cluster analysis to reveal user profiles.

The CLEAR-Engage study shifts from self-report to decision behavior by examining responses

to AI recommendations within a simulated, screenshot-based decision-making task. Participants

completed a hostage-rescue task in which they were presented with varying levels of AI support.

Behavioral measures (e.g., agreement with AI recommendations and detection of AI errors),

along with self-report measures of trust and understanding, were used to validate the ORI and

identify behavioral markers of over-reliance. Together, these studies aim to advance

understanding of explainability’s role in trust calibration, establish behavioral measures of over-

reliance, and inform the design of user-centered AI systems that support effective human-AI

teaming in a variety of contexts.

iii

I have followed the approved guidelines of my graduate program and the UAH Graduate

School for the use of generative Artificial Intelligence (AI) in the writing of this dissertation. The

following generative AI tools were used for the associated purpose(s) listed after each tool:

ChatGPT: Scenario generation in the CLEAR survey study. Revising, editing, and

proofreading text for clarity and coherence.

iv

Acknowledgements

I am incredibly lucky to have many generous and encouraging people in my life, without

whom I would not have been able to complete this dissertation. First and foremost, I would like

to thank my parents, Elroy and Debra Sullivan, for their constant encouragement and support

throughout my Ph.D., for always encouraging me to follow my curiosities, and for creating a

home that fostered open and meaningful discourse on any subject. Those conversations are what

led me to pursue a career in research and higher education.

I would also like to thank my fiancé, Dylan Pietzsch, without whose support and

encouragement this dissertation would not have been possible. Through studying for

comprehensive exams, late nights coding, and long writing sessions, he was a constant source of

reassurance and made sure everything else was taken care of so I could focus on my work. I hope

that one day I can repay the incredible gift of easing life’s worries, and I cannot wait to be Dr.

Pietzsch.

This project would not exist, nor be as strong as it is, without the support of my advisor,

Dr. Kristin Weger. I am very fortunate to have found an advisor who supported my ideas, gave

me the space to create my own path in research, and ensured that my work met the highest

standards. For that, I am deeply grateful. I would also like to thank my committee members for

their time, feedback, and thoughtful engagement with this work. I am also grateful to the

undergraduate students who worked with me on this project, especially Maggie Glass, for their

collaboration, feedback, and willingness to pilot and refine study materials. Many of my close

family and friends also completed my surveys and shared them with others without hesitation. I

am beyond grateful for their generosity and support.

v

Completing this dissertation required more resilience and growth than I anticipated, and I

am proud of the perseverance it represents. Lastly, I would like to thank my dogs, Eevee and

Jack, for the comfort, joy, and anxiety-relieving cuddles that carried me through this process.

vi

Table of Contents

Abstract .......................................................................................................................................... ii

Acknowledgements ....................................................................................................................... v

Table of Contents ........................................................................................................................ vii

List of Figures ............................................................................................................................. xiii

List of Tables ............................................................................................................................... xv

Epigraph ..................................................................................................................................... xvi

Chapter 1.

Introduction ................................................................................................... 1

1.1

1.2

1.3

Artificial Intelligence ......................................................................................... 1

Explainable Artificial Intelligence ..................................................................... 4

Organization of the Dissertation ........................................................................ 5

Chapter 2.

Literature Review ......................................................................................... 8

2.1

2.2

Definitions and Terminology ............................................................................. 8

Computer Science XAI Techniques ................................................................. 10

2.2.1  Post-Hoc Explanations ................................................................................ 10

2.2.2

Intrinsically Interpretable Models ............................................................... 11

2.2.3  Bridging the Gap between Computer Science and Psychology .................. 12

2.3

Psychological and Cognitive Foundations ....................................................... 12

2.3.1  Cognitive Load Theory ............................................................................... 14

2.3.2  Complacency & Automation Bias ............................................................... 16

2.3.3  Trust Calibration ......................................................................................... 18

2.3.4  AI Reliance .................................................................................................. 21

2.3.5  Predictors of Over-Reliance ........................................................................ 22

2.4

Usability and Human Factors Principles .......................................................... 24

vii

2.5

Brief Summary of Literature ............................................................................ 26

Chapter 3.  Research Objective 1: CLEAR Survey on XAI Complexity ................... 27

3.1

Methodology .................................................................................................... 28

3.1.1  Participants .................................................................................................. 29

3.1.2  Materials ...................................................................................................... 29

3.1.2.1  Scenarios ........................................................................................... 30

3.1.2.2  Scenario Generation .......................................................................... 31

3.1.2.3  Outcome Measures ............................................................................ 32

3.1.2.4  User Experience and Expertise ......................................................... 34

3.1.3  Procedure ..................................................................................................... 35

3.2

3.3

Analysis Approach ........................................................................................... 36

Results .............................................................................................................. 37

3.3.1  Descriptive Statistics ................................................................................... 37

3.3.2  Correlational Analysis ................................................................................. 41

3.3.3  Primary Regression Analysis (H1a) ............................................................ 42

3.3.3.1  Trust .................................................................................................. 43

3.3.3.2  Perceived Reliability ......................................................................... 44

3.3.3.3  Confidence in the AI ......................................................................... 44

3.3.3.4  Ease of Understanding of the AI Explanation................................... 45

3.3.3.5  Summary of H1a Results .................................................................. 45

3.3.4  Moderation Analysis (H1b) ......................................................................... 46

3.3.4.1  Trust .................................................................................................. 46

3.3.4.2  Perceived Reliability ......................................................................... 47

3.3.4.3  Confidence in the Accuracy of the AI............................................... 47

3.3.4.4  Ease of Understanding of the AI explanation ................................... 48

viii

3.3.4.5  Summary of Moderation Analysis .................................................... 49

3.3.5  Order Effects ............................................................................................... 49

3.3.6  Robustness and Exploratory Demographic Analyses ................................. 50

3.4

Discussion ........................................................................................................ 50

3.4.1  Scenario-Specific Effects ............................................................................ 51

3.4.2  Limitations and Future Directions ............................................................... 52

3.4.3  Design Implications ..................................................................................... 52

Chapter 4.  Research Objective 2: Identifying Predictors of Over-Reliance ............ 54

4.1

Methodology .................................................................................................... 55

4.1.1  Participants .................................................................................................. 55

4.1.2  Materials ...................................................................................................... 56

4.1.3  Procedure ..................................................................................................... 57

4.1.4  ORI Construction ........................................................................................ 58

4.2

4.3

Analysis Approach ........................................................................................... 58

Results .............................................................................................................. 60

4.3.1  Descriptive Statistics ................................................................................... 60

4.3.1.1

Information-Seeking Behavior .......................................................... 60

4.3.1.2  Habitual AI Use................................................................................. 61

4.3.1.3  AI Agreement .................................................................................... 62

4.3.2  ORI Construction ........................................................................................ 62

4.3.3  Demographic Differences in ORI Scores and Agreement .......................... 64

4.3.4  ORI Dimensions and ORI Scores (H2a) ..................................................... 65

4.3.4.1  Correlational Analysis ....................................................................... 65

4.3.4.2  Multiple Linear Regression ............................................................... 66

4.3.5  Explanation Complexity and ORI Scores (H2b) ......................................... 67

ix

4.3.6  Exploratory Cluster Analysis ...................................................................... 68

4.4

Discussion ........................................................................................................ 70

4.4.1  The Relationship Between Confidence and Understanding (H2a) ............. 70

4.4.2  Explanation Complexity and Over-Reliance (H2b) .................................... 72

4.4.3  Cluster Analysis: Reliance Groups ............................................................. 73

4.4.4  Theoretical and Design Implications ........................................................... 73

4.4.5  Limitations and Future Directions ............................................................... 74

Chapter 5.  Research Objective 3: CLEAR-Engage (Comprehending Levels of
Explainability and AI Recommendations – Engagement with Explanations) ............... 76

5.1

Methodology .................................................................................................... 77

5.1.1  Participants .................................................................................................. 78

5.1.2  Materials ...................................................................................................... 79

5.1.2.1  Simulation Task ................................................................................ 79

5.1.2.2  Behavioral and Perceptual Measures ................................................ 80

5.1.3  Procedure ..................................................................................................... 81

5.2

5.3

Analysis Approach ........................................................................................... 83

Results .............................................................................................................. 85

5.3.1  Descriptive Statistics ................................................................................... 85

5.3.1.1  Trust, Perceived Reliability, Confidence, and Understanding .......... 85

5.3.1.2  Hostage Order & Agreement Ratings ............................................... 86

5.3.1.3  Propensity to Trust AI ....................................................................... 88

5.3.1.4  AI Familiarity, Information-Seeking, and Habitual AI Use ............. 89

5.3.2  Behavioral ORI Construction ...................................................................... 91

5.3.3  Perceptual ORI Construction ...................................................................... 92

5.3.4  Correlations between Key Variables ........................................................... 93

5.3.5  Behavioral Patterns and Reliance (H3a) ..................................................... 94

x

5.3.6  Explanation Complexity and Reliance (H3b) ............................................. 95

5.3.6.1  Behavioral Agreement with AI Recommendations .......................... 95

5.3.6.2  Perceived Understanding and Information Sufficiency .................... 96

5.3.6.3  Summary of H3b Results .................................................................. 97

5.3.7  Behavioral and Perceptual ORI Convergent Validity ................................. 97

5.3.8  Order Effects ............................................................................................... 98

5.3.9  Robustness and Student Differences ........................................................... 99

5.3.10  Exploratory Analysis ............................................................................... 100

5.3.10.1  Minimal vs. Complex Explanation Preferences ............................ 100

5.3.10.2  Helpful Aspects of the Complex Explanation ............................... 100

5.3.10.3  Most Helpful Explanation Aspects Overall .................................. 101

5.4

Discussion ...................................................................................................... 101

5.4.1  Behavioral Patterns and Reliance (H3a) ................................................... 102

5.4.2  Explanation Complexity and Reliance Behavior (H3b) ............................ 102

5.4.3  Convergent Validity of Behavioral and Perceptual ORI (H3c) ................ 103

5.4.4  Explanation Preferences ............................................................................ 103

5.4.5  Limitations and Future Directions ............................................................. 104

5.4.6  Theoretical and Design Implications ......................................................... 105

5.4.6.1  Theoretical Implications.................................................................. 105

5.4.6.2  Design Implications ........................................................................ 106

Chapter 6.  General Discussion .................................................................................... 107

6.1

Integrating Perceptual and Behavioral Findings ............................................ 107

6.1.1  Refining and Measuring Over-Reliance .................................................... 108

6.1.2  The Inverted-U Hypothesis ....................................................................... 109

6.2

Overall Practical and Applied Implications ................................................... 110

xi

6.2.1  Research Implications ............................................................................... 110

6.2.2

Industry and Practice Implications ............................................................ 111

6.3

6.4

Limitations and Delimitations ........................................................................ 112

Scope and Delimitations ................................................................................ 113

Chapter 7.

Intellectual Merit ...................................................................................... 114

Chapter 8.  Conclusion ................................................................................................. 117

8.1

8.2

Summary ........................................................................................................ 117

Statement on the Use of Generative Artificial Intelligence ........................... 117

References .................................................................................................................................. 119

Appendix A.

CLEAR Survey Scenarios ........................................................................... 130

Appendix B.

Propensity to Trust ...................................................................................... 137

Appendix C.

CLEAR Survey Scenario Questions ........................................................... 139

Appendix D.

UTAUT Items ............................................................................................... 144

Appendix E.

Study 3 Trial Images .................................................................................... 145

Appendix F.

Trial Items .................................................................................................... 150

xii

List of Figures

Figure 1.1 Organization of the Dissertation and Study Flow. ....................................................... 7

Figure 2.1 Visual Representation of Trust Calibration taken from de Visser et al. (2014). ........ 19

Figure 2.2 Visualization of the Potential Inverted-U Pattern. ..................................................... 20

Figure 3.1 Means and Standard Deviations for Each of the Dependent Variables ...................... 38

Figure 3.2 Effects of Explanations on Outcomes Across Scenarios ............................................ 39

Figure 3.3 Distribution of Scores on the Propensity to Trust Technology Scale ........................ 40

Figure 3.4 Distribution of Scores on Familiarity with AI Items .................................................. 41

Figure 3.5 Spearman Rank-Order Correlation Coefficients between Study Variables ............... 42

Figure 4.1 Distribution of ORI Scores ......................................................................................... 64

Figure 4.2 Changes in ORI Scores across Explanation Complexity Levels. ............................... 68

Figure 4.3 Scree Plot .................................................................................................................... 69

Figure 4.4 Raincloud Plot Representing 3 Distinct AI Reliance Groups..................................... 69

Figure 5.1 Means and Standard Deviations for Trust, Reliability, Confidence, and
Understanding ............................................................................................................................... 86

Figure 5.2 First-Selected Hostage for Each Trial and Scene ....................................................... 87

Figure 5.3 Participant Agreement with AI-Recommended Hostage Rescue Order .................... 88

Figure 5.4 Distribution of Scores on the Propensity to Trust AI Scale. ...................................... 89

Figure 5.5 Distribution of Scores on the Self-Report Item Assessing Participant Familiarity
with AI Systems. ........................................................................................................................... 90

Figure 5.6 Distribution of Normalized (z-scored) Behavioral ORI Scores. ................................ 92

Figure 5.7 Distribution of Perceptual ORI Scores in Study 3. ..................................................... 93

Figure 5.8 Pearson’s Correlations Between Study Variables ...................................................... 94

Figure 5.9 Visual Representation of the Relationship Between Perceptual and Behavioral
ORI Scores. ................................................................................................................................... 98

xiii

Figure A.1 Visual Shown to Participants in the High Complexity, Résumé Screening
Scenario....................................................................................................................................... 134

Figure E.1 Scene 1 Visual Shown to Participants with No AI Recommendation. .................... 145

Figure E.2 Scene 1 Visual Shown to Participants with Best AI Recommended Path. .............. 145

Figure E.3 Scene 1 Visual Shown to Participants with Best AI Recommended Path and
Explanation. ................................................................................................................................ 146

Figure E.4 Scene 1 Visual Shown to Participants with Alternate AI Recommended Path. ...... 146

Figure E.5 Scene 1 Visual Shown to Participants with Alternate AI Recommended Path and
Explanation. ................................................................................................................................ 147

Figure E.6 Scene 2 Visual Shown to Participants with No AI Recommendation. .................... 147

Figure E.7 Scene 2 Visual Shown to Participants with Best AI Recommended Path. .............. 148

Figure E.8 Scene 2 Visual Shown to Participants with Best AI Recommended Path and
Explanation. ................................................................................................................................ 148

Figure E.9 Scene 2 Visual Shown to Participants with Alternate AI Recommended Path. ...... 149

Figure E.10 Scene 2 Visual Shown to Participants with Alternate AI Recommended Path and
Explanation. ................................................................................................................................ 149

xiv

List of Tables

Table 2.1 Key Features of Three Critical Terms in AI Transparency............................................ 9

Table 3.1 Results of Regression Models Testing H1a ................................................................. 43

Table 4.1 Survey Items Used to Create the ORI .......................................................................... 56

Table 4.2 Descriptive Statistics for Information-Seeking Behavior. ........................................... 61

Table 4.3 Agreement Rates with the AI Decision by Explanation Level. ................................... 62

Table 5.1 Correlations Among Behavioral Predictors of Over-Reliance Behavior. .................... 95

xv

Epigraph

It is hoped that by trying to imitate the behavior of a human brain (or that of some other animal)

by means of an electronic device—or by failing to do so—one may learn something of

importance concerning the brain’s workings. Finally, there is the optimistic hope that for similar

reasons AI might have something to say about deep questions of philosophy, by providing

insights into the meaning of the concept of mind.

– Roger Penrose, The Emperor’s New Mind (1989)

xvi

Chapter 1.

Introduction

The purpose of this dissertation is to investigate the relationship between Explainable

Artificial Intelligence (XAI) complexity and user perceptions (trust, understanding, perceived

reliability, and accuracy confidence), as well as factors that lead to over-reliance and over-trust

in artificial intelligence (AI), despite explanation complexity. More specifically, this research

seeks to identify the conditions under which users accurately rely on recommendations from AI

versus when they over-rely (accepting AI output without sufficient understanding or

engagement). Across three interrelated studies, this project aims to determine the optimal level of

explainability for calibrating trust and reliability, develop a composite over-reliance index (ORI)

based on perceptual and behavioral indicators, and validate the ORI through tasks designed to

mimic real-world decision-making contexts. The findings will contribute to a more nuanced

understanding of XAI in human-AI interaction and inform XAI design that supports effective

and informed decision-making. Overall, this research aims to examine how different AI

explanations influence user perceptions and reliance behaviors across a variety of decision-

making contexts.

1.1

Artificial Intelligence

This dissertation closely examines user behaviors during their interactions with AI

systems. The idea of AI computational systems was conceived in the late 1940s and early 1950s,

and the idea was first fully conceptualized by Alan Turing (1950) when he asked the question,

“Can machines think?” in his landmark article, “Computing Machinery and Intelligence.” In

1

1956, scientists at Dartmouth University were inspired by Turing and the possibilities of artificial

intelligence and began a 6-week summer workshop aimed at creating machines capable of out-

smarting humans (Bostrom, 2014). Over the next six decades, progress in the field of artificial

intelligence ebbed and flowed and coincidingly investor interest and disinterest. A major change

in the field occurred in 2012 when Krizhevsky et al. (2012) published results of a deep

convolutional neural network (CNN) that vastly outperformed any prior models at visual

recognition. The findings of Krizhevsky et al. showed the power that deep learning could have to

transform AI and inspired applications of deep learning techniques across various other fields.

A second landmark finding came in 2014 when Goodfellow et al. introduced generative

adversarial nets (GANs), which use two neural networks to generate realistic text and images.

These seminal findings led to a boom in AI research and advancements in a wide range of fields.

In healthcare, a CNN was trained to identify skin cancer at a level comparable to dermatologists

(Esteva et al., 2017). Large language models (LLMs) were developed based on findings by

Vaswani et al. (2017) that improved performance and reduced training times. The AI systems

that resulted from these findings quickly became mainstream and have already had a profound

impact on the lives of many individuals and organizations. For example, a study on

automatization of jobs examined 702 occupations and found that around 47% of jobs in the US

are at a high risk of being automated within the next decade or two (Frey & Osborne, 2017).

Other researchers have examined the likely effects of AI on security, transportation, healthcare,

entertainment, and multiple other areas of life (Brundage et al., 2018; Dul, 2022; Mollick, 2024;

Stone et al., 2022).

These advances in AI technology have made it clear that AI systems have a broad range

of uses and applications. One particular advantage of AI that increases its usefulness in many of

2

these applications is its ability to quickly and effectively make decisions and provide information

to aid in the decision-making process. AI can offer a great deal to improved decision-making

through efficiency and predictive accuracy, due to its unique ability to rapidly analyze large

amounts of data relevant to a decision. The human brain also has the ability to process and

analyze data relevant to a decision, but there are limitations to the amount of data the brain is

able to process, especially in time critical situations (C. D. Wickens et al., 2015). The brain often

fills in gaps in knowledge and processing ability by using mental shortcuts (e.g., gestalt

organizational principles and heuristics) and will often attend to only salient, expected, or high

value information (Kahneman, 2011; Proctor & Van Zandt, 2018; J. R. Wickens et al., 2003). AI

excels where the human brain falls short due to its ability to rapidly process vast amounts of

information relevant to a decision.

However, there are challenges associated with the use of AI in decision-making.

Informed decision making requires consideration of shared understanding, user cognitive load,

automation bias, user trust, perceived reliability of the AI, and user confidence in the decision,

among other cognitive and computing considerations. It can be difficult for the user to feel their

decision is informed and well-made if the AI system is unable to provide information and

explanations that allow for shared understanding of context, consider cognitive load, and give the

information necessary for trust calibration and perceived reliability. Many AI systems operate as

so-called “black boxes,” where the logic behind decisions remains opaque even to developers, let

alone end-users. In this case an explanation describing how the system arrived at a decision can

provide needed context to the user.

3

1.2

Explainable Artificial Intelligence

One proposed solution to the challenges associated with human-AI decision making and

the need for explanation is the use of XAI. XAI refers to a broad class of approaches designed to

make the decision-making process of AI systems more transparent, interpretable, and

understandable to human users (Ghela et al., 2024). The field of XAI has received a great deal of

attention in recent years but remains in a state of flux. There is disagreement among computer

scientists, human-computer interaction (HCI) researchers, and psychologists about how to best

implement and visualize explanations to the user. The type and delivery method of explanations

should be context and function dependent due to the wide range of AI applications, but it must

also be trustworthy, understandable, and useful to the user, regardless of context or function.

Therefore, research must be done to measure user perceptions of AI that will aid in the design of

effective XAI systems.

Initially, XAI implementation largely relied on the assumption that increasing the amount

of explanations leads to enhanced user trust and understanding, as providing detailed

explanations can help users evaluate AI recommendations (Druce et al., 2021; Othman, 2025;

Waltl & Vogl, 2018). However, other research suggests that user perceptions have an inverted-U

relationship with explanation complexity (Abdul et al., 2020; Ghai et al., 2021; Walmsley,

2021). At high levels of complexity, some studies have shown that explanations begin to have a

negative impact on user perceptions (Abdul et al., 2020; Ghai et al., 2021; Walmsley, 2021).

Explanations that are too robust or overly complex can increase cognitive load, overwhelm users,

or paradoxically increase over-reliance on the AI system by creating a false sense of

understanding (Abdul et al., 2020; Ghai et al., 2021; Ngo, 2025; Walmsley, 2021).

4

Alternatively, the absence of explanations or explanations that are too simple may fail to

convey essential decision-making information, leaving users unable to judge the system’s

reliability (Choung et al., 2023; Parasuraman & Riley, 1997a). Ideally, users are able to obtain

the exact amount of information they need to reach a decision that is based on accurately

calibrated trust and perceived reliability of the system.

This dissertation addresses the critical need for user sensitive XAI frameworks that

promote calibrated trust and reliability based on appropriate user understanding and confidence

to inform user decision-making. Building on existing research in human factors and cognitive

psychology, this study series aims to examine how different levels of explanation complexity

affect user perceptions of trust, confidence, understanding, and perceived reliability, while also

identifying when those effects contribute to over-reliance behavior in human-AI decision making

interactions.

1.3  Organization of the Dissertation

This dissertation is organized into eight chapters that together build the Comprehending

Levels of Explainability and AI Recommendations (CLEAR) study series. The series integrates

three primary research objectives that examine how varying levels of explainability influence

user trust and reliance on AI systems.

Chapter 1 introduces the overarching topic, establishing the context of AI, XAI, and the

psychological foundations that motivate this research. The chapter concludes by outlining the

structure and objectives of the clear study series.

Chapter 2 presents a comprehensive literature review that bridges the computer science

and psychological perspectives of XAI. The chapter reviews relevant terminology and theoretical

5

frameworks that inform the design of the CLEAR study series and identifies critical gaps this

research aims to address.

Chapter 3 covers research objective 1, the CLEAR survey. The chapter begins by

defining the specific research questions and hypotheses associated with the CLEAR survey. The

overall objective of this study is to: determine the optimal amount of explanation complexity

(low, medium, high) that leads to accurately calibrated trust, reliance, understanding, and

confidence across a variety of decision-making scenarios, while examining variations in these

effects across contexts (scenarios). Methodology, analysis approach, results, and discussion for

the CLEAR survey are then outlined.

Chapter 4 covers research objective 2, the ORI and identifying predictors of over-reliance

behavior. The chapter begins by defining the specific research questions and hypotheses for the

ORI study. The overall objective of this study is to: identify when and why over-reliance on AI

occurs by developing a novel index (ORI) and to determine the impact of XAI on over-reliance.

Methodology, analysis approach, results, and discussion for the ORI study are then outlined.

Chapter 5 covers research objective 3, the CLEAR-Engage study. The chapter begins by

defining the specific research questions and hypotheses for the CLEAR-Engage study. The

overall objective of this study is to: validate the ORI using behavioral measures collected during

a simulated AI-assisted decision-making task, identify behavioral markers of over-reliance, and

examine how varying levels of explanation complexity influence reliance on AI

recommendations. Methodology, analysis approach, results, and discussion for the CLEAR-

Engage study are then outlined.

Chapter 6 covers the overall discussion for the implications of the CLEAR study series as

a whole and integrates findings across the three studies to discuss theoretical, methodological,

6

and practical implications for XAI design, trust calibration, and human-AI interaction.

Limitations are also addressed. Chapter 7 outlines the intellectual merit and broader impacts of

the research, situating its contributions within both theoretical and applied domains of Human-AI

Interaction and human factors psychology.

Chapter 8 concludes the dissertation by synthesizing contributions across the three

studies and articulating the cumulative impact of the CLEAR study series.

• Introduction and Literature

Review

• Defines context, theory, and

gaps leading to research
objectives

Chapter 1-2:
Foundations

Chapter 3-5: Research
Framework

• Study 1 (CLEAR survey) ->
Study 2 (ORI) -> Study 3
(CLEAR-Engage)

• Describes research aims,

methods, analysis approach,
results, and discussion

• Integrates theoretical and
practical implications;
concludes with contributions
and future directions

Chapter 6-7:
Discussion, Merit, &
Conclusion

Figure 1.1 Organization of the Dissertation and Study Flow.

7

Chapter 2.  Literature Review

This review examines the current state of XAI from a human-centered perspective, with a

focus on how explanations are perceived, processed, and used in decision-making contexts.

Drawing on research from psychology, human factors, and human-AI interaction, the review

synthesizes findings related to cognitive load theory (CLT), trust in technology, automation bias,

and AI reliance behaviors, and identifies gaps in our understanding of how explanation design

influences user trust calibration and reliance behavior.

2.1

Definitions and Terminology

First, a preliminary overview of terms related to XAI research is provided. Inherently, AI

systems are typically “black box” systems, meaning that the inner workings of the system are

completely opaque. Ideally, XAI allows the inner workings of the system to become more

transparent to the user, sometimes referred to as “white box” AI. The term black box is not

unique to AI and has been used widely to describe what happens in between the input and output

of a system when the internal structure is unknown. In behavioral psychology, the mind can be

thought of as a black box because what is happening between the stimulus input and behavioral

output/reaction cannot be directly observed (Skinner, 1987). Neural network AI systems are

modeled on the brain and diffuse stored information in several complex networks that are

incredibly difficult to decipher, which makes their inner workings a black box, much like the

human mind (Castelvecchi, 2016). Neural network algorithms are exceptionally complex black

8

Reproduced with permission of copyright owner. Further reproduction prohibited without permission.

