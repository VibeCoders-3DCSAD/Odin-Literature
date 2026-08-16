---
conversion_metadata:
  converted_at: "2026-07-22T13:22:48Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Fei.pdf"
  source_pdf_sha256: "27955b5ad3a20d5aaaa7968494260ac2cdf0ab9b0f99453e0f0c51a2e916bb11"
  page_count: 24
  markdown_char_count: 81175
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

THE UNIVERSITY OF CHICAGO

IMPACT OF MENTAL REPRESENTATION ON CONSUMER BEHAVIORS:

IMPLICATIONS FOR MENTAL BUDGETING AND PREDICTION ALGORITHM

PREFERENCES

A DISSERTATION SUBMITTED TO

THE FACULTY OF THE UNIVERSITY OF CHICAGO

BOOTH SCHOOL OF BUSINESS

IN CANDIDACY FOR THE DEGREE OF

DOCTOR OF PHILOSOPHY

BY

LIN FEI

CHICAGO, ILLINOIS

JUNE 2023

---

<!-- PAGE 2 -->

Table of Contents

List of Tables ................................................................................................................................. iii

List of Figures ................................................................................................................................ iv

Acknowledgements ......................................................................................................................... v

Overview ......................................................................................................................................... 1

Introduction ..................................................................................................................................... 2

Chapter 1: Consumers’ Mental Representation of Expenditures: Implications for Spending and 
Savings Decisions ........................................................................................................................... 5

Abstract ....................................................................................................................................... 6

Study 1: Representation of Expenditures .................................................................................. 19

Study 2: Taxonomic Distance and Spending Adjustment ......................................................... 25

Study 3: Taxonomic Distance and Promotions ......................................................................... 36

Study 4: Examination of Grocery Purchase .............................................................................. 42

Chapter 2: Prediction by Replication: People Prefer Prediction Algorithms That Replicate the 
Event Being Predicted................................................................................................................... 54

Abstract ..................................................................................................................................... 55

Study 1: Prediction of Die Roll Outcomes ................................................................................ 65

Study 2: Prediction in Real-world Domains ............................................................................. 75

Study 3: Multiple Predictions and Choices ............................................................................... 83

Study 4: Simulation as Intervention .......................................................................................... 88

General Discussion .................................................................................................................... 90

Appendix 1: Tables ....................................................................................................................... 96

Appendix 2: Figures .................................................................................................................... 103

References ................................................................................................................................... 116

Supplemental Files: Web Appendix ........................................................................................... 129

ii

---

<!-- PAGE 3 -->

List of Tables

Table 1.1: Stimuli from Study 2b, Chapter 1 ................................................................................ 96

Table 1.2: Stimuli from Study 3a and 3b, Chapter 1 .................................................................... 97

Table 1.3: Product Sets from Study 4, Chapter 1 ......................................................................... 98

Table 2.1: Recommendation Description from Study 2c, Chapter 2 ............................................ 99

Table 2.2: Dimension Wording from Study 2c, Chapter 2 ......................................................... 100

Table 2.3: Conditions from Study 3, Chapter 2 .......................................................................... 101

Table 2.4: Regression from Study 3, Chapter 2 .......................................................................... 102

iii

---

<!-- PAGE 4 -->

List of Figures

Figure 1.1: Possible Representation of Expenditures, Chapter 1................................................ 103

Figure 1.2: Successive Pile Sort Interface, Chapter 1 ................................................................. 104

Figure 1.3: Multidimensional Scaling Reduction with Clustered Groups from Study 1, Chapter 1
..................................................................................................................................................... 106

Figure 1.4: Dendrogram of the Products on Aggregate Level from Study 1, Chapter 1 ............ 107

Figure 1.5: Spending Adjustment on Comparison Items from Study 2a, Chapter 1 .................. 108

Figure 1.6: Spending Adjustment on Comparison Items from Study 2b, Chapter 1 .................. 109

Figure 1.7: Raw Ratings and Estimated Marginal Means of Study 2c, Chapter 1 ..................... 110

Figure 1.8: Proportions Choosing the Closest Comparison Product from Study 3, Chapter 1... 111

Figure 1.9: Regression Coefficients by Year on Close Focal vs Far Focal from Study 4, Chapter 
1................................................................................................................................................... 112

Figure 2.1: Likelihood-to-Use and Replicativeness Rating from Study 1b, Chapter 2 .............. 113

Figure 2.2: Replicativeness & Willingness-to-Use Ratings from Study 2c, Chapter 2 .............. 114

Figure 2.3: Percentage Choosing the Target Algorithm from Study 3, Chapter 2 ..................... 115

iv

---

<!-- PAGE 5 -->

Acknowledgements

I am extremely grateful to my co-advisors Dan Bartels and Berkeley Dietvorst, for

showing me how rigorous and scientific research is and should be, for challenging me to

articulate and explain my thinking, and for always giving thoughtful advice and words of

encouragement. I am also incredibly thankful to Luxi Shen, whose mentorship and friendship

have been essential to my research experience and personal development, as well as Reid Hastie,

who has always been so generous with his time and wisdom and has always given out careful

thoughts to my projects. I deeply appreciate my fellow cohort Danny Katz and Minkwang Jang

who are always there for their peer, as well as the HOCAG group which is always an

encouraging and fun environment to discuss research.

Finally, I am extremely grateful for Ignatius Liu, who has been incredibly supportive of

me as a researcher and a person. Your help and your company have contributed much to this

dissertation and this wonderful journey.

v

---

<!-- PAGE 6 -->

Overview

People constantly encode and represent the information around them, and they make

various inferences, judgments, and decisions based on their representation. The dissertation aims

to connect mental representations to consumer behaviors. Investigating how consumers represent

their choices and contexts allows us to generate new predictions about their behaviors and

provide novel insights into the cognitive processes under these enriched contexts. In Chapter 1, I

explore the relationship between the representation of concepts and spending behaviors. In

Chapter 2, I explore how people represent prediction events and consequently how it influences

their prediction algorithm choices. Additional norming studies and detailed study stimuli are

available in Supplemental Files: Web Appendix.

1

---

<!-- PAGE 7 -->

Introduction

People constantly encode and represent the information around them, and they make

various inferences, judgement, and decisions based on their representation. For example, people

could use groups of exemplars or prototypes to represent concepts, could leverage maps or

networks to represent relationships, and could adopt mental models or scripts to represent

processes. The study of mental representations is foundational in understanding the human mind

because it is central to how humans process and make use of information.

Understanding how people represent the world around them has much merit particularly

in consumer contexts (Bartels and Johnson 2015). A coherent theory on people’s representation

can help highlight the potential common ground of seemingly distinct findings and unify

multiple established phenomena. For example, how people represent monetary values can

provide an explanation to concave utility function, loss aversion, and hyperbolic discounting

(Stewart, Charter, and Brown 2006). In addition, understanding consumer’s representations

allows us to further predict their reactions and behaviors in contexts like new product launches

(Moreau, Markman, and Lehmann 2001), product bundles, and service failures. In applying

representation to the study of consumer behaviors, we simultaneously learn about the behavior

and the thinking behind it.

More generally, identifying the role of representation and cognition complements the

common economic approach to studying consumer behavior. The study of consumer behaviors

has long been focused on how people’s behaviors and judgments deviate from those that are

economically optimal (Thaler 2015). The cognitive approach on the other hand puts much

emphasis on why people are behaving the way they are and where the phenomena come from.

Combining the two approaches provides a better understanding of why consumers make

2

---

<!-- PAGE 8 -->

decisions in particular ways and generates predictions on when consumers will deviate from the

economic prediction.

Studying representation with these enriched environments and complex decision

problems in consumer contexts also provides new insights into the human mind. Consumers face

some of the most complicated decisions such as purchasing a house, and the study of these

choices invites new theories on problem solving and decision making (Payne, Bettman, and

Johnson 1993). For example, the study of brand and product categorization expands our

understanding on how a category prompts the objects in it (Nedungadi 1990), and the study of

context effects in product choices (Huber, Payne, and Puto 1982) has inspired much theorization

on how contexts shape decisions (Trueblood et al. 2014).

Finally, connecting representation with behavior allows us to identify contexts where

behaviors pertaining to daily lives, spending, and decisions, and thinking are related. In this

dissertation, I aim to identify two of these contexts. Specifically, I found that representations

influence people’s behaviors in how they manage their budgets and how they choose prediction

algorithms, in ways that are distinct from predictions of simple normative models.

In Chapter 1, I explore the relationship between the representation of concepts and

spending behaviors. Through 4 sets of studies, I find that when consumers deviate from budget

on one item, they are more likely to adjust spending for items closer in representation than

further. In Study 1, I recover the taxonomy that people use to represent common expenditures

with a successive pile-sort paradigm. Study 2 found that recovered taxonomy predicts people’s

self-reported spending adjustment, while Study 3 and 4 found that the taxonomy predicts

people’s consequential choices and actual grocery purchase behavior. This chapter provides

evidence that representation influences spendings, even when money is theoretically fungible.

3

---

<!-- PAGE 9 -->

In Chapter 2, I explore how people represent prediction events and consequently how

they choose prediction algorithms. Through 4 sets of studies, I found that people prefer to use

prediction algorithms that replicate the same process of the even being predicted, which implies

that the mental models of a prediction event include the exact process through which the

outcome is generated. I found that when predicting both simple but random tasks (Study 1) and

real-world outcomes (Study 2), people prefer algorithms that replicate the process of the

prediction event, even when the algorithms might prefer worse. Study 3 provides a boundary of

this preference, while Study 4 designs and tests an intervention based on this preference. This

chapter highlights how people’s representation changes consumers’ preferences and choices.

4

---

<!-- PAGE 10 -->

Chapter 1: Consumers’ Mental Representation of Expenditures: Implications for Spending

and Savings Decisions

5

---

<!-- PAGE 11 -->

Abstract

People’s mental representation of expenditures is crucial to how they budget. We propose

that much like how people represent natural objects, people represent expenditures in a

hierarchical taxonomy. Across seven studies, we found evidence of a hierarchical representation

of expenditures. We first recover people’s mental representation using a successive pile-sort

method that asks people to form hierarchies of categories with common expenditures (e.g., rent,

dining out, etc.). We found that there is consensus in people’s hierarchical representations of

expenditures and that their representations are relatively stable over time. Further, we found that

people’s adjustment in their spending behavior can be predicted by the distance between items in

their representation. Specifically, when people overspent on an item, they were more likely to

spontaneously adjust spending for items closer in representation than further. We examine this

spontaneous adjustment behavior using both lab studies and field data with over 7-million

grocery shopping trips. The findings highlight the connection between mental representation and

consumer behavior, and emphasize the importance of studying cognitive representation in the

context of consumption.

6

---

<!-- PAGE 12 -->

Consumers often maintain budgets. That is, they set restrictions on how much they wish

to spend, and they behave as though money is nonfungible (Thaler 1985; 1999) and earmarked

for specific functions (e.g., gas, food; Antonides et al. 2011; Hasting and Shapiro 2013, 2018;

Heath and Soll 1996; Cheema and Soman 2006; Soman and Cheema 2011; Thaler 1999). For

example, consumers might set a budget specifically intended for gas. When gas prices drops,

consumers, who now have a gas-budget surplus, may use it to purchase premium gas (Hastings

and Shapiro 2013). In a recent survey, 80% of people reported that they have formally or

informally budgeted at some point in their lives, and the practice of budgeting is positively

correlated with financial wellbeing (Zhang et al. 2020). Therefore, understanding how budgeting

works is essential for understanding consumer financial decision making and consumer welfare.

Research on budgeting mostly theorizes that consumers group expenditures into a single

level of budgeting categories (Heath and Soll 1996; Cheema and Soman 2006, Zhang et al. 2020,

cf. Henderson and Peterson 1992). Some consumers might group items into relatively general

categories such as “Food” and “Entertainment”, while others group to more detailed levels such

as “Groceries”, “Dining Out”, and “Movies” (Zhang et al. 2020). In this paper, we propose and

test a more complete account that people mentally represent expenditures in hierarchical

taxonomies. In other words, people represent expenditures in multiple, nested levels of

categories where lower levels of the categories are more specific and higher levels are more

general. For example, people might think of cereal as “breakfast food” before they think of it

more generally as “food” (Markman, Brendl, and Kim 2007), and hence the “breakfast food”

category is nested within the higher-level “food” category (Figure 1).

Consequently, we hypothesize that the taxonomic distance between items is important for

people’s spending decisions in situations where they deviate from their budget. We define

7

---

<!-- PAGE 13 -->

taxonomic distance as the level at which the expenditures are categorized together in consumers’

taxonomies, and we predict that when people’s spending on an item deviates from their budget,

they will adjust more on the items that are taxonomically closer than further. This prediction is

important to marketers who are interested in understanding the type of products consumers

adjust and the degree of adjustment when consumers encounter spending deviations such as

holiday splurges. Further, past research that hypothesizes single level budgeting categories

cannot account for this adjustment. In this paper, we adopt a method from cognitive

anthropology to approximate the represented taxonomy of expenditures. Then, we use the

taxonomy to predict how people adjust their spending in various contexts, including real

shopping behaviors.

Connecting Mental Representation to Mental Accounting

Theoretical Background

Mental accounting is grounded in the way that people categorize and represent concepts

(Henderson and Peterson 1992). Mental accounting refers to the cognitive operations by which

prospects are evaluated with respect to some specific “topical” account instead of a

“comprehensive” account (Linville and Fischer 1991; Thaler and Johnson 1990; Kahneman and

Tversky 1984; Soman 2004; Thaler 1999; Zhang et al. 2020). For example, people are more

likely to travel to save $5 on a calculator that originally costs $15 than when it costs $125. This

is likely because they evaluate the $5 with respect to the total “topical” expenditure ($15 or

$125) but not their total wealth. In doing so, people are associating money with different

expenditure concepts, and how people represent the concepts will consequently influence how

they spend the resources.

8

---

<!-- PAGE 14 -->

Researchers have connected mental representation with mental accounting (Arkes et al.

1994; Levav and McGraw 2009; Evers, Imas, and Kang 2022) and have provided insights on

how people form and use mental accounts. For example, representation of the source of money

influences the types of mental accounts that are constructed (Levav and McGraw 2009,

Reinholtz, Bartels, and Parker 2015): money associated with negative emotions is less likely to

be spent on hedonic purchases, and money associated with brand-specific gift cards is more

likely to be spent on brand-typical items. Representation of expenditures also influences the

membership of expenditures with respect to a mental account. Expenditures that have a high

degree of feature-based (i.e., attribute) similarity are often integrated together as a larger loss

(Evers, Imas, and Kang 2022).

Similarly, mental representation has provided much insight into how people mentally

budget (Henderson and Peterson 1992; Heath and Soll 1996). If people mentally represent

expenditures, for example, they would spontaneously categorize expenditures and organize them

in categories when prompted to think about budgets, which is what researchers have found

(Cheema and Soman 2006; Sussman and Alter 2012). The expenditures in a category are often

similar to each other in some respects: they may share similar features (e.g., electronics) or fulfill

similar goals (e.g., entertainment; Felcher, Malaviya, and McGill 2001). Expenditures that are

grouped into a budgeting category have graded membership—the typicality of an expenditure

within a category can differ (Reinholtz et al. 2015), which is another prediction from research on

mental representation. For example, shirts can be more typical of the clothing category than

gloves (Heath and Soll 1996).

However, previous research has not connected the hierarchical nature of representation

with mental accounting. To the authors’ knowledge, only one paper has provided preliminary

9

---

<!-- PAGE 15 -->

tests that people represent mental accounts hierarchically (Henderson and Peterson 1992).

Specifically, Henderson and Peterson (1992) mentioned that people have a larger budget for

higher-level categories but did not provide predictions on how people make spending decisions

when there are hierarchical budgets. However, the researchers did not make concrete predictions

on how the hierarchy influences budgeting behavior. In the sections below, we detail the

reasoning for proposing a hierarchical representation of expenditures, and we highlight

additional contributions of introducing a hierarchical representation in budgeting.

Hierarchical Representation of Expenditures

There are several reasons why we think consumers group expenditures hierarchically.

First, research suggests that people represent concepts of the natural world and of their everyday

lives in taxonomies (Berlin 1992). People may group cats and dogs into the category “mammals”

and then group mammals together with birds and fish into the superordinate category “animal”.

Organizing concepts at multiple, nested levels is a cognitively efficient way for people to store

and access information related to different objects (Collins and Quillian 1969; Smith 1978) and

generalize the information to more specific concepts (e.g., a dog inherits the properties of a

mammal; Osherson et al. 1990). Research suggests that people hierarchically represent animals

(e.g., Lopez et al. 1997), trees (Collins and Quillian 1969; Medin et al. 1997), furniture (Rosch et

al. 1976), and clothing (Rosch and Lloyd. 1978), and we suspect that people represent concepts

of expenditures in terms of multiple, nested categories as well.

Further, people also represent objects in a way that reflects their experience and their

knowledge of the world (Markman 1999; Medin and Atran 2004). For example, the taxonomy

for trees that landscapers use tends to reflect differences between trees in shape and appearance,

while botanists focus more on the scientific taxonomy. Each group’s taxonomy reflects the

10

---

<!-- PAGE 16 -->

knowledge of trees that is most useful for the way that each group typically interacts with and

thinks about trees. Similarly, people’s interactions with consumer goods likely also shape the

categories they use to represent them. For example, grocery items are often subdivided into aisles

that serve different functions (breakfast food, frozen meals, paper products, etc.). Further, aisles

typically have different sections dedicated to smaller groupings of products (e.g., baking goods

aisle may contain both kitchen appliances and flour). As consumers navigate through these

shopping environments, they will likely internalize this organizational scheme into their

representation.

Finally, previous research on consumer behavior has hinted that people represent

expenditures hierarchically. Several studies have suggested that consumers represent snack foods

and fast-food brands in taxonomies (Ratneshwar and Shocker 1991; Nedungadi, 1990).

Specifically, Ratneshwar and Shocker (1991) recovered a hierarchical structure from their

similarity rating data. Nedungadi (1990) investigated the relationship between brand hierarchy

and brand recall. In this paper, we extend the view that people represent objects hierarchically

and apply it to spending and budgeting.

Some Contributions of a Taxonomy-Based Theory of Mental Budgeting

The notion that expenditures are represented in terms of a taxonomy addresses some

limitations in the existing literature on mental budgeting. First, the current budgeting literature

often assumes that people have predefined budgeting categories. Papers that investigate the type

of budgets people construct often elicit those categories in a top-down fashion, asking directly

for the budgeting categories people have in mind (Heath and Soll 1996, Zhang et al. 2020).

However, people might come up with the most common categories they budget for (e.g.,

“food”), and hence the listed budgets might often miss categories like exceptional expenditures

11

---

<!-- PAGE 17 -->

(Sussman and Alter 2012). Relatedly, previous papers on mental budgeting also often prompted

people with pre-defined categorical labels when investigating budgeting behaviors (Heath and

Soll 1996; Cheema and Soman 2006). For example, participants would be examining their

budgets for “food” and for “entertainment”, which are researcher-defined categories, when they

are deciding how to categorize their expenditure of “dining out”. Yet not every constructs these

specific budgeting categories (Zhang et al. 2020), and we have limited insights into how people

budget in absence of these given categories.

In addition, much of the budgeting literature suggests that consumers have defined

expenditure membership with respect to the predefined budgeting categories. Consumers tend to

adjust more on items that are typical to these categories (Heath and Soll 1996, Reinholtz et al.

2015), and are worse at evaluating expenditures that are exceptional (Sussman and Alter 2012).

However, it is still unclear how consumers define the typicality or exceptionality of an

expenditure. Further, consumers often are flexible in the way they categorize expenses (Cheema

and Soman 2006) and might categorize a specific expenditure differently depending on the

context (“dining out” can belong to “food” or “entertainment”). This suggests that consumers

might not have clear categorical membership for expenditures.

A hierarchical representation, on the other hand, puts less emphasis on how expenditures

relate to categories and focuses more on how expenditures relate to each other. In this paper, we

recover the representation through a bottom-up approach that asks people to group expenditures

into a hierarchy. We therefore only argue that the distance in the hierarchy matters for people’s

budget and do not need to make assumptions on the categories consumers construct or the

membership of expenditures. Further, distances in a hierarchical representation can also reveal

expenditures that are clustered together. This complements the current literature by providing

12

---

<!-- PAGE 18 -->

insight into the expenditures that are often thought of together and the categories that people

naturally construct. With a hierarchical representation, the recovered structure will also reveal

the items that are exceptional (e.g., items that are higher up in the hierarchy) or items that can be

flexibly categorized (e.g., items that are in the middle of different concepts), which provides

additional insight into people’s budgeting behaviors.

The ideas in the current manuscript add new, refined predictions about how people adjust

their spending when they have overspent or underspent on an item. We first extend the

framework of budgeting beyond binary categorical restrictions. Heath and Soll (1996) theorized

that consumers set budget categories, and then track and post spending with respect to the

category. In this case, spending decisions are binary: when consumers overspent with respect to

their budget for a category, they were more likely to adjust their consequent spending on other

items in the category than those outside of the category. However, people’s purchase behaviors

could be influenced by their out-of-category purchases (Chintagunta and Haldar 1998;

Manchanda et al. 1999). For example, the purchases of soup and yogurt, which are presumably

of different product categories, influence each other (Chintagunta and Halder 1998). Therefore,

the framework of budgeting should extend beyond binary categorical restrictions. Our proposed

hierarchical representation allows us to examine expenditures at different taxonomic distances

beyond binary categorical restrictions. We make a concrete prediction that when a consumer

deviates from their budget on a spending, they will adjust more on items that are closer in

taxonomic distance than further.

More generally, our paper aims to expand on the theorization of mental accounting

beyond the binary distinction of “topical accounts” and “comprehensive accounts” (Kahneman

and Tversky 1984; Thaler 1999). Mental accounting is often seen as the behavior that “relates the

13

---

<!-- PAGE 19 -->

consequences of possible choices to a reference level that is determined by the context within

which the decision arises” (Thaler 1999). For example, people evaluate a discount of a calculator

against the topical account of a calculator purchase rather than against their comprehensive

wealth. In contrast, a hierarchical structure implies that there could be multiple nested reference

accounts, and people might recruit different reference levels depending on the expenditures they

are evaluating. In other words, consumers might be referencing nested mental accounts on a

more continuous spectrum than just “topical” and “comprehensive” accounts.

Our prediction not only extends the budgeting literature but also provides insight into

consumer research related to cross-product elasticities. Specifically, we predict that after

spending on some items, people might adjust down on taxonomically close items due to their

budget restraint, resulting in a pattern that is similar to positive cross elasticity. Much

examination on cross-product elasticities either recovers the relationship from an observed

dataset (Tian, Lautz, Wallis and Lambiotte 2021), or theorizes that the cross-product elasticities

were results of substitutes and complements (Koszegi and Matejka 2020). Our theorization

suggests an alternative mechanism that cross-product elasticities could emerge from the

influence of taxonomic distance on budgeting behaviors. The construct of taxonomic distance is

relevant but distinct from substitutability, because it requires people to evaluate their spending

with respect to a budget. Further, a close association between items (i.e., a smaller taxonomic

distance) might form because of multiple factors. Items closely associated might overlap in their

usage contexts (Ratneshwar and Shocker 1991) or related to the same spending goals (Barsalou

1983, 1985). Therefore, people might group items together because the items are substitutes

14

---

<!-- PAGE 20 -->

(e.g., burger and pizza), complements (e.g., shirt and jeans), both (e.g., detergents and soap) or

neither (e.g., sunglasses and watch)1.

We note that the theory of a hierarchical representation in budgeting is an expansion but

not an alternative account to the current budgeting literature. We replicate and extend the finding

that consumers construct budgeting categories and within a predefined category, expenditure

characteristics like typicality matter for spending behaviors. Our paper tests whether consumers

also naturally construct categories in a nested fashion, and such hierarchical representation

allows us to examine and address open questions within the budgeting literature.

Implications of a Hierarchical Taxonomy

Although we cannot directly examine how people represent expenditures in their minds,

we test several implications from our proposal that people represent expenditures hierarchically.

First, we can test if consumers have a shared understanding that some items are more closely

related than others. For example, we could evaluate whether consumers share the understanding

that shampoo and sunscreen are grouped together at a more specific, lower level than shampoo

and movie tickets. We test this commonality between people’s understanding by testing whether

there is statistical consensus among their representations. The term “consensus” is adopted from

the Cultural Consensus Model (CCM; Romney, Weller, and Batchelder 1986, Medin et al. 1997)

to suggest statistical agreement or commonality across individuals’ representations. The CCM

establishes consensus by testing whether participants’ representations are positively correlated,

and whether the first latent root of the interpersonal correlation matrix is large (Weller, 2007). A

consensus between participants would suggest not only that people can represent expenditures in

1 These examples are from our Study 2c, where we collected substitutability and complementarity ratings for all the 
product pairs that share the smallest taxonomic distance. The details of the collection method are reported in Study 
2c.

15

---

<!-- PAGE 21 -->

a taxonomy, but also that this representation is relatively natural to majority of people. Past

research has found that members of a culture have a consensual understanding of animal

categories (Lopez et al. 1997) and consumers largely agree on product hierarchies of snack foods

(Ratneshwar and Shocker 1991).

However, it is also possible that people have systematically different representations and

that there might not be consensus across consumers. Literature has found that representations of

the same objects can vary across cultures (Lopez et al. 1997) and occupations (Medin et al.

1997). For example, the way people represent animals and trees is influenced by their

environment and the functions the objects fulfill. If there are large differences between consumer

segments, there could be discrepancy in how people represent expenditures. Therefore, we first

explore the competing hypotheses of whether there is consensus in people’s representations.

H1a: Consumers represent expenditures similarly, establishing consensus across their

individual taxonomies.

H1b: Consumers do not reach consensus in how they represent expenditures—people’s

taxonomies are substantially different.

Also, if a hierarchical representation is unnatural to people, their taxonomy might be

different across time because there could be large variances in how they choose to build a

taxonomy out of expenditures. Consequently, if people form similar hierarchical representations

of expenditures over time, it would be suggestive of a hierarchical representation. Similar

representations over time is also indictive of some stability in the way people represent

relationships between expenditures, which would make it easier for people to recruit the

taxonomic distance when making spending and savings decisions.

16

---

<!-- PAGE 22 -->

Second, a taxonomic representation predicts how much people will adjust their spending

on items at different levels of the hierarchy. Specifically, we predict that, all else equal,

consumers’ spending adjustment on an item will be influenced by the taxonomic distance (i.e.,

the level at which items are categorized together) between the item they just spent on and an item

they are considering purchasing. When a consumer deviates from her budget (i.e., overspends or

underspends), she would adjust spending for items that are more closely related than those

distantly related. If a consumer categorizes movies and scarves together as discretionary

spending and treats bread as a necessity, the taxonomic distance between scarves and movies

would be closer than that between scarves and bread. Consequently, we would predict that the

consumer adjusts more on movies (i.e., the closer item) than on bread (i.e., the farther item).2

Several restrictions apply to the proposition that hierarchical taxonomy can predict

spending adjustment. First, we do not suggest or believe that taxonomic distance is the only

factor that consumers consider. Characteristics of expenditures such as the necessity of the

spending will influence consumers spending intentions, and there are necessities that people

cannot adjust onto such as rent or phone bills (Zhang et al. 2020). We argue that controlling for

the other plausible factors, taxonomic distance will influence spending behaviors on items that

have room for adjustment. Further, spending deviations from necessities might not allow room

for choices on other items that need to be cut back on: if someone struggles to pay rent, then they

will cut back on all the expenditures they possibly can. Therefore, we follow the previous

literature (Heath and Soll 1996, Cheema and Soman 2006) and focus on spending adjustments in

discretionary spending—that is, purchases that are not absolute necessities. Finally, we note that

2 We note that this hypothesis holds regardless of whether H1a or H1b obtains. If H1b obtains, we can use 
information about each person’s taxonomy of expenditures to predict her spending and saving decisions. If H1a 
obtains, we can use the consensus taxonomy to make predictions about a group’s decisions.

17

---

<!-- PAGE 23 -->

we are attempting to characterize how people adjust their spending and savings when they are

thinking about alternatives. This is the standard shopping context as people are almost always

evaluating alternatives on product shelves or recommended lists on webpages. Therefore, we will

always present alternatives for people to evaluate in our studies.

H2: All else equal, when consumers deviate from their budget, their taxonomy of

expenditures influences their spending and saving decisions. Specifically, when they deviate

from their budget (i.e., over- or under-spend) on an item, they are likely to adjust more on items

that are closer in taxonomic distance to the purchased item.

Finally, if people naturally represent expenditures in hierarchically-organized categories,

they will spontaneously adjust their spending in accordance with taxonomic distances. Here we

use the term “spontaneous” to highlight that—contrary to previous literature (Heath and Soll

1996, Cheema and Soman 2006)—we do not prompt participants with predefined categories. We

predict that consumers will make spending adjustments even when not explicitly prompted with

budget category labels.

H3: People spontaneously recruit their taxonomy when making spending decisions. That

is, the adjustment stated in H2 happens even without reminding people of the categories to which

the expenditures belong.

In what follows, we first investigate how expenditures are represented. Then, we assess

whether people spontaneously adjust their spending based on their representations even when

they are not primed to think about budgeting categories.

Study Overview

In seven studies, we examine how consumers represent expenditures and how their

representation of expenditures influences their budgetary decisions. In study 1a, we elicit

18

---

<!-- PAGE 24 -->

consumers’ represented taxonomy of expenditures and find consensus in their representations.

We find that people’s representations are relatively stable across time in Study 1b. Study 2a and

2b investigate how people make spending and savings adjustments based on both each

respondent’s own individual taxonomy and the aggregate taxonomy, and Study 2c finds that

people’s hierarchical taxonomies influence their budgeting behaviors in a way not accounted for

by the principles of substitutability and complementarity. The results are consistent with the

hypothesis that people adjust their spending more on items that are taxonomically closer

(whether the items are substitutes, complements, both, or neither). Studies 3a and 3b use

consequential choices to test whether similar patterns generalize to purchasing items on

promotion. Finally, Study 4 examines more than seven million trips to grocery stores across a

decade, and finds analogous patterns—consumers spend more on items when taxonomically

close items are on sale. The findings from all studies suggest that mental representation is

important for studying how people budget and spend. The Web Appendix and all lab study

materials (pre-registration, data, and analyses) are available on OSF

(https://osf.io/bcknx/?view_only=94e720c38d014813bd1f672682d5b9a2).

Study 1: Representation of Expenditures

Study 1a investigates whether there is consensus in people’s representations (H1) of

expenditures while study 1b investigates the consistency of the representations across 3 months.

Regardless of whether consensus is obtained, we will further qualitatively examine how

consumers represent expenditures.

Study 1a: Initial Exploration

Participants & Procedures. Twenty-seven participants (all located in the US) were

recruited on Amazon Mechanical Turk (MTurk). The average age was 38.4 and 37.0% were

19

Reproduced with permission of copyright owner. Further reproduction prohibited without permission.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

THE UNIVERSITY OF CHICAGO

IMPACT OF MENTAL REPRESENTATION ON CONSUMER BEHAVIORS:

IMPLICATIONS FOR MENTAL BUDGETING AND PREDICTION ALGORITHM

PREFERENCES

A DISSERTATION SUBMITTED TO

THE FACULTY OF THE UNIVERSITY OF CHICAGO

BOOTH SCHOOL OF BUSINESS

IN CANDIDACY FOR THE DEGREE OF

DOCTOR OF PHILOSOPHY

BY

LIN FEI

CHICAGO, ILLINOIS

JUNE 2023

Table of Contents

List of Tables ................................................................................................................................. iii

List of Figures ................................................................................................................................ iv

Acknowledgements ......................................................................................................................... v

Overview ......................................................................................................................................... 1

Introduction ..................................................................................................................................... 2

Chapter 1: Consumers’ Mental Representation of Expenditures: Implications for Spending and
Savings Decisions ........................................................................................................................... 5

Abstract ....................................................................................................................................... 6

Study 1: Representation of Expenditures .................................................................................. 19

Study 2: Taxonomic Distance and Spending Adjustment ......................................................... 25

Study 3: Taxonomic Distance and Promotions ......................................................................... 36

Study 4: Examination of Grocery Purchase .............................................................................. 42

Chapter 2: Prediction by Replication: People Prefer Prediction Algorithms That Replicate the
Event Being Predicted................................................................................................................... 54

Abstract ..................................................................................................................................... 55

Study 1: Prediction of Die Roll Outcomes ................................................................................ 65

Study 2: Prediction in Real-world Domains ............................................................................. 75

Study 3: Multiple Predictions and Choices ............................................................................... 83

Study 4: Simulation as Intervention .......................................................................................... 88

General Discussion .................................................................................................................... 90

Appendix 1: Tables ....................................................................................................................... 96

Appendix 2: Figures .................................................................................................................... 103

References ................................................................................................................................... 116

Supplemental Files: Web Appendix ........................................................................................... 129

ii

List of Tables

Table 1.1: Stimuli from Study 2b, Chapter 1 ................................................................................ 96

Table 1.2: Stimuli from Study 3a and 3b, Chapter 1 .................................................................... 97

Table 1.3: Product Sets from Study 4, Chapter 1 ......................................................................... 98

Table 2.1: Recommendation Description from Study 2c, Chapter 2 ............................................ 99

Table 2.2: Dimension Wording from Study 2c, Chapter 2 ......................................................... 100

Table 2.3: Conditions from Study 3, Chapter 2 .......................................................................... 101

Table 2.4: Regression from Study 3, Chapter 2 .......................................................................... 102

iii

List of Figures

Figure 1.1: Possible Representation of Expenditures, Chapter 1................................................ 103

Figure 1.2: Successive Pile Sort Interface, Chapter 1 ................................................................. 104

Figure 1.3: Multidimensional Scaling Reduction with Clustered Groups from Study 1, Chapter 1
..................................................................................................................................................... 106

Figure 1.4: Dendrogram of the Products on Aggregate Level from Study 1, Chapter 1 ............ 107

Figure 1.5: Spending Adjustment on Comparison Items from Study 2a, Chapter 1 .................. 108

Figure 1.6: Spending Adjustment on Comparison Items from Study 2b, Chapter 1 .................. 109

Figure 1.7: Raw Ratings and Estimated Marginal Means of Study 2c, Chapter 1 ..................... 110

Figure 1.8: Proportions Choosing the Closest Comparison Product from Study 3, Chapter 1... 111

Figure 1.9: Regression Coefficients by Year on Close Focal vs Far Focal from Study 4, Chapter
1................................................................................................................................................... 112

Figure 2.1: Likelihood-to-Use and Replicativeness Rating from Study 1b, Chapter 2 .............. 113

Figure 2.2: Replicativeness & Willingness-to-Use Ratings from Study 2c, Chapter 2 .............. 114

Figure 2.3: Percentage Choosing the Target Algorithm from Study 3, Chapter 2 ..................... 115

iv

Acknowledgements

I am extremely grateful to my co-advisors Dan Bartels and Berkeley Dietvorst, for

showing me how rigorous and scientific research is and should be, for challenging me to

articulate and explain my thinking, and for always giving thoughtful advice and words of

encouragement. I am also incredibly thankful to Luxi Shen, whose mentorship and friendship

have been essential to my research experience and personal development, as well as Reid Hastie,

who has always been so generous with his time and wisdom and has always given out careful

thoughts to my projects. I deeply appreciate my fellow cohort Danny Katz and Minkwang Jang

who are always there for their peer, as well as the HOCAG group which is always an

encouraging and fun environment to discuss research.

Finally, I am extremely grateful for Ignatius Liu, who has been incredibly supportive of

me as a researcher and a person. Your help and your company have contributed much to this

dissertation and this wonderful journey.

v

Overview

People constantly encode and represent the information around them, and they make

various inferences, judgments, and decisions based on their representation. The dissertation aims

to connect mental representations to consumer behaviors. Investigating how consumers represent

their choices and contexts allows us to generate new predictions about their behaviors and

provide novel insights into the cognitive processes under these enriched contexts. In Chapter 1, I

explore the relationship between the representation of concepts and spending behaviors. In

Chapter 2, I explore how people represent prediction events and consequently how it influences

their prediction algorithm choices. Additional norming studies and detailed study stimuli are

available in Supplemental Files: Web Appendix.

1

Introduction

People constantly encode and represent the information around them, and they make

various inferences, judgement, and decisions based on their representation. For example, people

could use groups of exemplars or prototypes to represent concepts, could leverage maps or

networks to represent relationships, and could adopt mental models or scripts to represent

processes. The study of mental representations is foundational in understanding the human mind

because it is central to how humans process and make use of information.

Understanding how people represent the world around them has much merit particularly

in consumer contexts (Bartels and Johnson 2015). A coherent theory on people’s representation

can help highlight the potential common ground of seemingly distinct findings and unify

multiple established phenomena. For example, how people represent monetary values can

provide an explanation to concave utility function, loss aversion, and hyperbolic discounting

(Stewart, Charter, and Brown 2006). In addition, understanding consumer’s representations

allows us to further predict their reactions and behaviors in contexts like new product launches

(Moreau, Markman, and Lehmann 2001), product bundles, and service failures. In applying

representation to the study of consumer behaviors, we simultaneously learn about the behavior

and the thinking behind it.

More generally, identifying the role of representation and cognition complements the

common economic approach to studying consumer behavior. The study of consumer behaviors

has long been focused on how people’s behaviors and judgments deviate from those that are

economically optimal (Thaler 2015). The cognitive approach on the other hand puts much

emphasis on why people are behaving the way they are and where the phenomena come from.

Combining the two approaches provides a better understanding of why consumers make

2

decisions in particular ways and generates predictions on when consumers will deviate from the

economic prediction.

Studying representation with these enriched environments and complex decision

problems in consumer contexts also provides new insights into the human mind. Consumers face

some of the most complicated decisions such as purchasing a house, and the study of these

choices invites new theories on problem solving and decision making (Payne, Bettman, and

Johnson 1993). For example, the study of brand and product categorization expands our

understanding on how a category prompts the objects in it (Nedungadi 1990), and the study of

context effects in product choices (Huber, Payne, and Puto 1982) has inspired much theorization

on how contexts shape decisions (Trueblood et al. 2014).

Finally, connecting representation with behavior allows us to identify contexts where

behaviors pertaining to daily lives, spending, and decisions, and thinking are related. In this

dissertation, I aim to identify two of these contexts. Specifically, I found that representations

influence people’s behaviors in how they manage their budgets and how they choose prediction

algorithms, in ways that are distinct from predictions of simple normative models.

In Chapter 1, I explore the relationship between the representation of concepts and

spending behaviors. Through 4 sets of studies, I find that when consumers deviate from budget

on one item, they are more likely to adjust spending for items closer in representation than

further. In Study 1, I recover the taxonomy that people use to represent common expenditures

with a successive pile-sort paradigm. Study 2 found that recovered taxonomy predicts people’s

self-reported spending adjustment, while Study 3 and 4 found that the taxonomy predicts

people’s consequential choices and actual grocery purchase behavior. This chapter provides

evidence that representation influences spendings, even when money is theoretically fungible.

3

In Chapter 2, I explore how people represent prediction events and consequently how

they choose prediction algorithms. Through 4 sets of studies, I found that people prefer to use

prediction algorithms that replicate the same process of the even being predicted, which implies

that the mental models of a prediction event include the exact process through which the

outcome is generated. I found that when predicting both simple but random tasks (Study 1) and

real-world outcomes (Study 2), people prefer algorithms that replicate the process of the

prediction event, even when the algorithms might prefer worse. Study 3 provides a boundary of

this preference, while Study 4 designs and tests an intervention based on this preference. This

chapter highlights how people’s representation changes consumers’ preferences and choices.

4

Chapter 1: Consumers’ Mental Representation of Expenditures: Implications for Spending

and Savings Decisions

5

Abstract

People’s mental representation of expenditures is crucial to how they budget. We propose

that much like how people represent natural objects, people represent expenditures in a

hierarchical taxonomy. Across seven studies, we found evidence of a hierarchical representation

of expenditures. We first recover people’s mental representation using a successive pile-sort

method that asks people to form hierarchies of categories with common expenditures (e.g., rent,

dining out, etc.). We found that there is consensus in people’s hierarchical representations of

expenditures and that their representations are relatively stable over time. Further, we found that

people’s adjustment in their spending behavior can be predicted by the distance between items in

their representation. Specifically, when people overspent on an item, they were more likely to

spontaneously adjust spending for items closer in representation than further. We examine this

spontaneous adjustment behavior using both lab studies and field data with over 7-million

grocery shopping trips. The findings highlight the connection between mental representation and

consumer behavior, and emphasize the importance of studying cognitive representation in the

context of consumption.

6

Consumers often maintain budgets. That is, they set restrictions on how much they wish

to spend, and they behave as though money is nonfungible (Thaler 1985; 1999) and earmarked

for specific functions (e.g., gas, food; Antonides et al. 2011; Hasting and Shapiro 2013, 2018;

Heath and Soll 1996; Cheema and Soman 2006; Soman and Cheema 2011; Thaler 1999). For

example, consumers might set a budget specifically intended for gas. When gas prices drops,

consumers, who now have a gas-budget surplus, may use it to purchase premium gas (Hastings

and Shapiro 2013). In a recent survey, 80% of people reported that they have formally or

informally budgeted at some point in their lives, and the practice of budgeting is positively

correlated with financial wellbeing (Zhang et al. 2020). Therefore, understanding how budgeting

works is essential for understanding consumer financial decision making and consumer welfare.

Research on budgeting mostly theorizes that consumers group expenditures into a single

level of budgeting categories (Heath and Soll 1996; Cheema and Soman 2006, Zhang et al. 2020,

cf. Henderson and Peterson 1992). Some consumers might group items into relatively general

categories such as “Food” and “Entertainment”, while others group to more detailed levels such

as “Groceries”, “Dining Out”, and “Movies” (Zhang et al. 2020). In this paper, we propose and

test a more complete account that people mentally represent expenditures in hierarchical

taxonomies. In other words, people represent expenditures in multiple, nested levels of

categories where lower levels of the categories are more specific and higher levels are more

general. For example, people might think of cereal as “breakfast food” before they think of it

more generally as “food” (Markman, Brendl, and Kim 2007), and hence the “breakfast food”

category is nested within the higher-level “food” category (Figure 1).

Consequently, we hypothesize that the taxonomic distance between items is important for

people’s spending decisions in situations where they deviate from their budget. We define

7

taxonomic distance as the level at which the expenditures are categorized together in consumers’

taxonomies, and we predict that when people’s spending on an item deviates from their budget,

they will adjust more on the items that are taxonomically closer than further. This prediction is

important to marketers who are interested in understanding the type of products consumers

adjust and the degree of adjustment when consumers encounter spending deviations such as

holiday splurges. Further, past research that hypothesizes single level budgeting categories

cannot account for this adjustment. In this paper, we adopt a method from cognitive

anthropology to approximate the represented taxonomy of expenditures. Then, we use the

taxonomy to predict how people adjust their spending in various contexts, including real

shopping behaviors.

Connecting Mental Representation to Mental Accounting

Theoretical Background

Mental accounting is grounded in the way that people categorize and represent concepts

(Henderson and Peterson 1992). Mental accounting refers to the cognitive operations by which

prospects are evaluated with respect to some specific “topical” account instead of a

“comprehensive” account (Linville and Fischer 1991; Thaler and Johnson 1990; Kahneman and

Tversky 1984; Soman 2004; Thaler 1999; Zhang et al. 2020). For example, people are more

likely to travel to save $5 on a calculator that originally costs $15 than when it costs $125. This

is likely because they evaluate the $5 with respect to the total “topical” expenditure ($15 or

$125) but not their total wealth. In doing so, people are associating money with different

expenditure concepts, and how people represent the concepts will consequently influence how

they spend the resources.

8

Researchers have connected mental representation with mental accounting (Arkes et al.

1994; Levav and McGraw 2009; Evers, Imas, and Kang 2022) and have provided insights on

how people form and use mental accounts. For example, representation of the source of money

influences the types of mental accounts that are constructed (Levav and McGraw 2009,

Reinholtz, Bartels, and Parker 2015): money associated with negative emotions is less likely to

be spent on hedonic purchases, and money associated with brand-specific gift cards is more

likely to be spent on brand-typical items. Representation of expenditures also influences the

membership of expenditures with respect to a mental account. Expenditures that have a high

degree of feature-based (i.e., attribute) similarity are often integrated together as a larger loss

(Evers, Imas, and Kang 2022).

Similarly, mental representation has provided much insight into how people mentally

budget (Henderson and Peterson 1992; Heath and Soll 1996). If people mentally represent

expenditures, for example, they would spontaneously categorize expenditures and organize them

in categories when prompted to think about budgets, which is what researchers have found

(Cheema and Soman 2006; Sussman and Alter 2012). The expenditures in a category are often

similar to each other in some respects: they may share similar features (e.g., electronics) or fulfill

similar goals (e.g., entertainment; Felcher, Malaviya, and McGill 2001). Expenditures that are

grouped into a budgeting category have graded membership—the typicality of an expenditure

within a category can differ (Reinholtz et al. 2015), which is another prediction from research on

mental representation. For example, shirts can be more typical of the clothing category than

gloves (Heath and Soll 1996).

However, previous research has not connected the hierarchical nature of representation

with mental accounting. To the authors’ knowledge, only one paper has provided preliminary

9

tests that people represent mental accounts hierarchically (Henderson and Peterson 1992).

Specifically, Henderson and Peterson (1992) mentioned that people have a larger budget for

higher-level categories but did not provide predictions on how people make spending decisions

when there are hierarchical budgets. However, the researchers did not make concrete predictions

on how the hierarchy influences budgeting behavior. In the sections below, we detail the

reasoning for proposing a hierarchical representation of expenditures, and we highlight

additional contributions of introducing a hierarchical representation in budgeting.

Hierarchical Representation of Expenditures

There are several reasons why we think consumers group expenditures hierarchically.

First, research suggests that people represent concepts of the natural world and of their everyday

lives in taxonomies (Berlin 1992). People may group cats and dogs into the category “mammals”

and then group mammals together with birds and fish into the superordinate category “animal”.

Organizing concepts at multiple, nested levels is a cognitively efficient way for people to store

and access information related to different objects (Collins and Quillian 1969; Smith 1978) and

generalize the information to more specific concepts (e.g., a dog inherits the properties of a

mammal; Osherson et al. 1990). Research suggests that people hierarchically represent animals

(e.g., Lopez et al. 1997), trees (Collins and Quillian 1969; Medin et al. 1997), furniture (Rosch et

al. 1976), and clothing (Rosch and Lloyd. 1978), and we suspect that people represent concepts

of expenditures in terms of multiple, nested categories as well.

Further, people also represent objects in a way that reflects their experience and their

knowledge of the world (Markman 1999; Medin and Atran 2004). For example, the taxonomy

for trees that landscapers use tends to reflect differences between trees in shape and appearance,

while botanists focus more on the scientific taxonomy. Each group’s taxonomy reflects the

10

knowledge of trees that is most useful for the way that each group typically interacts with and

thinks about trees. Similarly, people’s interactions with consumer goods likely also shape the

categories they use to represent them. For example, grocery items are often subdivided into aisles

that serve different functions (breakfast food, frozen meals, paper products, etc.). Further, aisles

typically have different sections dedicated to smaller groupings of products (e.g., baking goods

aisle may contain both kitchen appliances and flour). As consumers navigate through these

shopping environments, they will likely internalize this organizational scheme into their

representation.

Finally, previous research on consumer behavior has hinted that people represent

expenditures hierarchically. Several studies have suggested that consumers represent snack foods

and fast-food brands in taxonomies (Ratneshwar and Shocker 1991; Nedungadi, 1990).

Specifically, Ratneshwar and Shocker (1991) recovered a hierarchical structure from their

similarity rating data. Nedungadi (1990) investigated the relationship between brand hierarchy

and brand recall. In this paper, we extend the view that people represent objects hierarchically

and apply it to spending and budgeting.

Some Contributions of a Taxonomy-Based Theory of Mental Budgeting

The notion that expenditures are represented in terms of a taxonomy addresses some

limitations in the existing literature on mental budgeting. First, the current budgeting literature

often assumes that people have predefined budgeting categories. Papers that investigate the type

of budgets people construct often elicit those categories in a top-down fashion, asking directly

for the budgeting categories people have in mind (Heath and Soll 1996, Zhang et al. 2020).

However, people might come up with the most common categories they budget for (e.g.,

“food”), and hence the listed budgets might often miss categories like exceptional expenditures

11

(Sussman and Alter 2012). Relatedly, previous papers on mental budgeting also often prompted

people with pre-defined categorical labels when investigating budgeting behaviors (Heath and

Soll 1996; Cheema and Soman 2006). For example, participants would be examining their

budgets for “food” and for “entertainment”, which are researcher-defined categories, when they

are deciding how to categorize their expenditure of “dining out”. Yet not every constructs these

specific budgeting categories (Zhang et al. 2020), and we have limited insights into how people

budget in absence of these given categories.

In addition, much of the budgeting literature suggests that consumers have defined

expenditure membership with respect to the predefined budgeting categories. Consumers tend to

adjust more on items that are typical to these categories (Heath and Soll 1996, Reinholtz et al.

2015), and are worse at evaluating expenditures that are exceptional (Sussman and Alter 2012).

However, it is still unclear how consumers define the typicality or exceptionality of an

expenditure. Further, consumers often are flexible in the way they categorize expenses (Cheema

and Soman 2006) and might categorize a specific expenditure differently depending on the

context (“dining out” can belong to “food” or “entertainment”). This suggests that consumers

might not have clear categorical membership for expenditures.

A hierarchical representation, on the other hand, puts less emphasis on how expenditures

relate to categories and focuses more on how expenditures relate to each other. In this paper, we

recover the representation through a bottom-up approach that asks people to group expenditures

into a hierarchy. We therefore only argue that the distance in the hierarchy matters for people’s

budget and do not need to make assumptions on the categories consumers construct or the

membership of expenditures. Further, distances in a hierarchical representation can also reveal

expenditures that are clustered together. This complements the current literature by providing

12

insight into the expenditures that are often thought of together and the categories that people

naturally construct. With a hierarchical representation, the recovered structure will also reveal

the items that are exceptional (e.g., items that are higher up in the hierarchy) or items that can be

flexibly categorized (e.g., items that are in the middle of different concepts), which provides

additional insight into people’s budgeting behaviors.

The ideas in the current manuscript add new, refined predictions about how people adjust

their spending when they have overspent or underspent on an item. We first extend the

framework of budgeting beyond binary categorical restrictions. Heath and Soll (1996) theorized

that consumers set budget categories, and then track and post spending with respect to the

category. In this case, spending decisions are binary: when consumers overspent with respect to

their budget for a category, they were more likely to adjust their consequent spending on other

items in the category than those outside of the category. However, people’s purchase behaviors

could be influenced by their out-of-category purchases (Chintagunta and Haldar 1998;

Manchanda et al. 1999). For example, the purchases of soup and yogurt, which are presumably

of different product categories, influence each other (Chintagunta and Halder 1998). Therefore,

the framework of budgeting should extend beyond binary categorical restrictions. Our proposed

hierarchical representation allows us to examine expenditures at different taxonomic distances

beyond binary categorical restrictions. We make a concrete prediction that when a consumer

deviates from their budget on a spending, they will adjust more on items that are closer in

taxonomic distance than further.

More generally, our paper aims to expand on the theorization of mental accounting

beyond the binary distinction of “topical accounts” and “comprehensive accounts” (Kahneman

and Tversky 1984; Thaler 1999). Mental accounting is often seen as the behavior that “relates the

13

consequences of possible choices to a reference level that is determined by the context within

which the decision arises” (Thaler 1999). For example, people evaluate a discount of a calculator

against the topical account of a calculator purchase rather than against their comprehensive

wealth. In contrast, a hierarchical structure implies that there could be multiple nested reference

accounts, and people might recruit different reference levels depending on the expenditures they

are evaluating. In other words, consumers might be referencing nested mental accounts on a

more continuous spectrum than just “topical” and “comprehensive” accounts.

Our prediction not only extends the budgeting literature but also provides insight into

consumer research related to cross-product elasticities. Specifically, we predict that after

spending on some items, people might adjust down on taxonomically close items due to their

budget restraint, resulting in a pattern that is similar to positive cross elasticity. Much

examination on cross-product elasticities either recovers the relationship from an observed

dataset (Tian, Lautz, Wallis and Lambiotte 2021), or theorizes that the cross-product elasticities

were results of substitutes and complements (Koszegi and Matejka 2020). Our theorization

suggests an alternative mechanism that cross-product elasticities could emerge from the

influence of taxonomic distance on budgeting behaviors. The construct of taxonomic distance is

relevant but distinct from substitutability, because it requires people to evaluate their spending

with respect to a budget. Further, a close association between items (i.e., a smaller taxonomic

distance) might form because of multiple factors. Items closely associated might overlap in their

usage contexts (Ratneshwar and Shocker 1991) or related to the same spending goals (Barsalou

1983, 1985). Therefore, people might group items together because the items are substitutes

14

(e.g., burger and pizza), complements (e.g., shirt and jeans), both (e.g., detergents and soap) or

neither (e.g., sunglasses and watch)1.

We note that the theory of a hierarchical representation in budgeting is an expansion but

not an alternative account to the current budgeting literature. We replicate and extend the finding

that consumers construct budgeting categories and within a predefined category, expenditure

characteristics like typicality matter for spending behaviors. Our paper tests whether consumers

also naturally construct categories in a nested fashion, and such hierarchical representation

allows us to examine and address open questions within the budgeting literature.

Implications of a Hierarchical Taxonomy

Although we cannot directly examine how people represent expenditures in their minds,

we test several implications from our proposal that people represent expenditures hierarchically.

First, we can test if consumers have a shared understanding that some items are more closely

related than others. For example, we could evaluate whether consumers share the understanding

that shampoo and sunscreen are grouped together at a more specific, lower level than shampoo

and movie tickets. We test this commonality between people’s understanding by testing whether

there is statistical consensus among their representations. The term “consensus” is adopted from

the Cultural Consensus Model (CCM; Romney, Weller, and Batchelder 1986, Medin et al. 1997)

to suggest statistical agreement or commonality across individuals’ representations. The CCM

establishes consensus by testing whether participants’ representations are positively correlated,

and whether the first latent root of the interpersonal correlation matrix is large (Weller, 2007). A

consensus between participants would suggest not only that people can represent expenditures in

1 These examples are from our Study 2c, where we collected substitutability and complementarity ratings for all the
product pairs that share the smallest taxonomic distance. The details of the collection method are reported in Study
2c.

15

a taxonomy, but also that this representation is relatively natural to majority of people. Past

research has found that members of a culture have a consensual understanding of animal

categories (Lopez et al. 1997) and consumers largely agree on product hierarchies of snack foods

(Ratneshwar and Shocker 1991).

However, it is also possible that people have systematically different representations and

that there might not be consensus across consumers. Literature has found that representations of

the same objects can vary across cultures (Lopez et al. 1997) and occupations (Medin et al.

1997). For example, the way people represent animals and trees is influenced by their

environment and the functions the objects fulfill. If there are large differences between consumer

segments, there could be discrepancy in how people represent expenditures. Therefore, we first

explore the competing hypotheses of whether there is consensus in people’s representations.

H1a: Consumers represent expenditures similarly, establishing consensus across their

individual taxonomies.

H1b: Consumers do not reach consensus in how they represent expenditures—people’s

taxonomies are substantially different.

Also, if a hierarchical representation is unnatural to people, their taxonomy might be

different across time because there could be large variances in how they choose to build a

taxonomy out of expenditures. Consequently, if people form similar hierarchical representations

of expenditures over time, it would be suggestive of a hierarchical representation. Similar

representations over time is also indictive of some stability in the way people represent

relationships between expenditures, which would make it easier for people to recruit the

taxonomic distance when making spending and savings decisions.

16

Second, a taxonomic representation predicts how much people will adjust their spending

on items at different levels of the hierarchy. Specifically, we predict that, all else equal,

consumers’ spending adjustment on an item will be influenced by the taxonomic distance (i.e.,

the level at which items are categorized together) between the item they just spent on and an item

they are considering purchasing. When a consumer deviates from her budget (i.e., overspends or

underspends), she would adjust spending for items that are more closely related than those

distantly related. If a consumer categorizes movies and scarves together as discretionary

spending and treats bread as a necessity, the taxonomic distance between scarves and movies

would be closer than that between scarves and bread. Consequently, we would predict that the

consumer adjusts more on movies (i.e., the closer item) than on bread (i.e., the farther item).2

Several restrictions apply to the proposition that hierarchical taxonomy can predict

spending adjustment. First, we do not suggest or believe that taxonomic distance is the only

factor that consumers consider. Characteristics of expenditures such as the necessity of the

spending will influence consumers spending intentions, and there are necessities that people

cannot adjust onto such as rent or phone bills (Zhang et al. 2020). We argue that controlling for

the other plausible factors, taxonomic distance will influence spending behaviors on items that

have room for adjustment. Further, spending deviations from necessities might not allow room

for choices on other items that need to be cut back on: if someone struggles to pay rent, then they

will cut back on all the expenditures they possibly can. Therefore, we follow the previous

literature (Heath and Soll 1996, Cheema and Soman 2006) and focus on spending adjustments in

discretionary spending—that is, purchases that are not absolute necessities. Finally, we note that

2 We note that this hypothesis holds regardless of whether H1a or H1b obtains. If H1b obtains, we can use
information about each person’s taxonomy of expenditures to predict her spending and saving decisions. If H1a
obtains, we can use the consensus taxonomy to make predictions about a group’s decisions.

17

we are attempting to characterize how people adjust their spending and savings when they are

thinking about alternatives. This is the standard shopping context as people are almost always

evaluating alternatives on product shelves or recommended lists on webpages. Therefore, we will

always present alternatives for people to evaluate in our studies.

H2: All else equal, when consumers deviate from their budget, their taxonomy of

expenditures influences their spending and saving decisions. Specifically, when they deviate

from their budget (i.e., over- or under-spend) on an item, they are likely to adjust more on items

that are closer in taxonomic distance to the purchased item.

Finally, if people naturally represent expenditures in hierarchically-organized categories,

they will spontaneously adjust their spending in accordance with taxonomic distances. Here we

use the term “spontaneous” to highlight that—contrary to previous literature (Heath and Soll

1996, Cheema and Soman 2006)—we do not prompt participants with predefined categories. We

predict that consumers will make spending adjustments even when not explicitly prompted with

budget category labels.

H3: People spontaneously recruit their taxonomy when making spending decisions. That

is, the adjustment stated in H2 happens even without reminding people of the categories to which

the expenditures belong.

In what follows, we first investigate how expenditures are represented. Then, we assess

whether people spontaneously adjust their spending based on their representations even when

they are not primed to think about budgeting categories.

Study Overview

In seven studies, we examine how consumers represent expenditures and how their

representation of expenditures influences their budgetary decisions. In study 1a, we elicit

18

consumers’ represented taxonomy of expenditures and find consensus in their representations.

We find that people’s representations are relatively stable across time in Study 1b. Study 2a and

2b investigate how people make spending and savings adjustments based on both each

respondent’s own individual taxonomy and the aggregate taxonomy, and Study 2c finds that

people’s hierarchical taxonomies influence their budgeting behaviors in a way not accounted for

by the principles of substitutability and complementarity. The results are consistent with the

hypothesis that people adjust their spending more on items that are taxonomically closer

(whether the items are substitutes, complements, both, or neither). Studies 3a and 3b use

consequential choices to test whether similar patterns generalize to purchasing items on

promotion. Finally, Study 4 examines more than seven million trips to grocery stores across a

decade, and finds analogous patterns—consumers spend more on items when taxonomically

close items are on sale. The findings from all studies suggest that mental representation is

important for studying how people budget and spend. The Web Appendix and all lab study

materials (pre-registration, data, and analyses) are available on OSF

(https://osf.io/bcknx/?view_only=94e720c38d014813bd1f672682d5b9a2).

Study 1: Representation of Expenditures

Study 1a investigates whether there is consensus in people’s representations (H1) of

expenditures while study 1b investigates the consistency of the representations across 3 months.

Regardless of whether consensus is obtained, we will further qualitatively examine how

consumers represent expenditures.

Study 1a: Initial Exploration

Participants & Procedures. Twenty-seven participants (all located in the US) were

recruited on Amazon Mechanical Turk (MTurk). The average age was 38.4 and 37.0% were

19

Reproduced with permission of copyright owner. Further reproduction prohibited without permission.

