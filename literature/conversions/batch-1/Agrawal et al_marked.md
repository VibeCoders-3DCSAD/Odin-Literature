---
conversion_metadata:
  converted_at: "2026-07-22T11:48:03Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Agrawal et al.pdf"
  source_pdf_sha256: "189392ac6f3a2730fc374a2b7c82a2058c1d4a9cf3253dfd665242b0315c8597"
  page_count: 21
  markdown_char_count: 131589
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Int J Comput Intell Syst          (2025) 18:165

RESEARCH ARTICLE

Analyzing and Rewarding Credit Card Spending Habits 
in India: a Machine Learning Approach
 · Safa Hamdare2 
 · Aryan Khanna1 
Renuka Agrawal1

Received: 24 February 2025 / Revised: 15 May 2025 / Accepted: 17 June 2025 
© The Author(s) 2025

Abstract
With the rapid adoption of digital payments in India, credit card companies are focusing on customer loyalty and 
planning rewards to incentivize spending, especially during peak periods like festivals. However, there is a gap 
in developing a tailored system that optimizes sales and reward structures for these companies. The proposed 
work addresses this gap by leveraging machine learning techniques to analyze and assess credit card spending 
patterns and propose design targeted reward programs. Besides this, this study focuses on categories as luxury, 
travel, groceries, EMIs payments, and others and employs ML methods, using K-Means clustering to segment 
users based on card types (Silver, Gold, Platinum, and Signature). Feature engineering is another key in improving 
the model’s understanding and providing insights, particularly in calculating reward points based on various 
attributes and spending behavior. The usage of original and synthetic datasets ensured scalability and adaptability 
across different financial domains as well. The results highlight the potential and need of ML to optimize reward 
allocation and provide real-time predictions, enabling financial institutions to tailor their offerings for increased 
customer engagement and retention. By aligning rewards with high-margin spending categories and leveraging 
adaptive frameworks, this study offers strategies to enhance credit card reward programs. The proposed ML model 
achieved an R2 value of 0.99, demonstrating superior accuracy in optimizing reward point distribution.

Keywords  Credit card rewards · Spending analysis · Reward optimization

1  Introduction

India has witnessed an exponential leap in usage of credit card, driven by rapid digital adoption, urbanization, and 
increasing incomes in all categories of earners. As of 2024, over 83 million active credit cards are in circulation, 
supported by the government’s Digital India initiative, the major stakeholders being the expanding middle class, 
and the increasing preference for digital payments. In this expanding landscape of digital transactions, financial 
institutions face increasing pressure to attract and hold customers by adopting innovative strategies, especially 
through reward programs. These reward systems, offering cashback, discounts, air miles, and points in both 
indispensable categories like groceries and EMIs and selected categories like luxury goods and travel, play a 
major role in promoting spending, customer acquisition, and retention by aligning benefits with consumer interests 
and spending patterns [1, 2].

Despite  the  success  of  traditional  reward  models,  credit  card  companies  often  fail  to  meet  the  diverse 
expectations of modern tech-savvy credit card users. Today’s cardholders vary widely, from essential buyers who 
focus primarily on necessities such as groceries and bills, to affluent and luxurious spenders seeking premium

Int J Comput Intell Syst          (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0

---

<!-- PAGE 2 -->

165

Page 2 of 21

https://doi.org/10.1007/s44196-025-00899-0

experiences in luxury goods and travel. The generalized, one-size-fits-all nature of traditional reward structures 
does not effectively cater to these varied preferences [3]. This lack of adaptability as per the needs of customers 
results in missed opportunities to increase customer engagement and loyalty, particularly among high-valued 
customers. The core problem faced by credit card companies in India is differentiating their offerings in a 
competitive market to retain high-value customers. Current reward programs often fail to incentivize spending 
among affluent and frequent spenders due to their generic structures, which fail to distinguish between nominal 
and high-value spenders [4, 5].

The importance of customizing reward systems becomes especially evident during peak sales seasons like 
Diwali, Christmas, and New Year, when consumer spending spikes. During these times, many consumers actively 
seek cards that offer better benefits for large purchases. This presents an opportunity for financial institutions to 
introduce customized incentives that align with changing consumer preferences [6, 7]. Advancements in data 
analytics and machine learning now offer credit card companies the ability to analyze transaction data, segment 
users, and create adaptive reward structures. These technologies can be harnessed to target high-value customers 
with personalized incentives, ultimately driving greater customer satisfaction and retention [8]. Moreover, by 
shifting the focus of reward systems toward discretionary categories like luxury goods and travel, institutions can 
enhance customer loyalty and profitability [9].

The objective of this research is to leverage ML techniques to analyze and predict the spending habits of credit 
card users in India, with an intention on optimizing reward programs to enhance customer engagement and loyalty 
[10]. This study aims to enable financial institutions to personalize reward systems by identifying key spending 
categories such as luxury goods, travel, groceries, and EMIs. The specific goals of the research are as follows:

1.  Segment Spending Behavior: implement K-Means clustering to categorize users based on their spending 
habits, identifying profiles as luxury spenders, frequent travelers, and nominal spenders and rewarding 
accordingly.

2.  Optimize Reward Programs: develop reward systems that allocate higher points for luxury and travel-related

spending, motivating users to boost discretionary expenditures with a justified approach for rewards.

3.  Prevent  Overfitting  and  Ensure  Generalization:  employ  synthetic  data  and  regularization  techniques 
to counteract overfitting, allowing models to perform accurately on new, unseen data while maintaining 
scalability.

4.  Enhance Accuracy with Feature Engineering: engineer features such as reward points per transaction and

spending frequency to improve model precision and deepen insights into user behavior.

This research seeks to provide financial institutions especially credit card companies with a data-driven 
framework for developing personalized reward programs that promote higher discretionary spending, improve 
customer retention, and increase overall customer satisfaction in the competitive Indian credit card market.

2   Related Work

The application of ML techniques for analyzing credit card spending behaviors has gained prominence due to 
the availability of vast transactional datasets. Previous studies have explored various aspects, including user 
segmentation, behavior prediction, and reward program optimization. Cheema and Van der Stede [11] examined 
how reward programs tailored to user preferences, particularly in high-spending categories like luxury goods 
and travel, can enhance customer engagement and usage frequency. However, their approach lacked dynamic 
adaptation to shifts in spending patterns. Li, Ngai, and Hu [12, 13] reviewed ML applications in financial 
services, focusing on K-Means clustering, Random Forest, and Gradient Boosting for consumer prediction and 
segmentation. While effective, these methods were static and struggled to adjust to real-time changes in user 
behavior. Predictive models for spending patterns have also been extensively studied. Gan et al. [14] employed

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 3 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 3 of 21

165

ensemble models like XGBoost and LightGBM to predict consumer behavior in high-value categories, improving 
reward allocation and incentive design. Despite their effectiveness, these models were prone to overfitting, 
particularly when handling high-dimensional data. Sadat Akash’s “Credit Card Transaction Dataset” [15] has been 
widely used to train predictive models. However, most studies utilizing this dataset focused on general prediction 
tasks rather than aligning predictive models with targeted reward structures for high-value spending categories.
Broader ML applications in financial behavior prediction have also been explored. Sun and Vasarhelyi [16] 
and Sayjadah et al. [17] applied ML models to predict credit card defaults, demonstrating the potential of neural 
networks in financial forecasting. Although these models exhibited high accuracy for risk assessment, they did 
not focus on consumer spending behaviors in reward-eligible categories. Teng and Lee [18] used decision trees 
and Support Vector Machines (SVMs) to predict default risks and spending patterns, yet these methods struggled 
to generalize spending prediction in high-value segments due to limited dataset specificity. Despite extensive 
research on credit card user segmentation and behavior prediction, several limitations remain. Many existing 
models lack adaptability to evolving user preferences, resulting in static reward structures that fail to align with 
current spending trends. Ensemble models like XGBoost and LightGBM, while promising, often suffer from 
overfitting when applied to high-dimensional datasets. Additionally, most studies overlook discretionary spend-
ing categories such as luxury and travel, which are crucial for customer loyalty programs. Moreover, existing 
methods tend to be static and fail to accommodate real-time shifts in user behavior, limiting their effectiveness.
Table 1 provides a comparative analysis of previous research, identifies existing gaps, and highlights how the 
proposed work addresses these limitations using ML-driven reward personalization and real-time adaptability. To 
address these limitations, this research introduces a machine learning model that leverages clustering techniques, 
such as K-Means, for detailed user segmentation based on spending in discretionary categories like luxury and 
travel. Unlike prior studies, this work specifically focuses on predicting high-value spending to optimize reward 
distribution, ensuring enhanced personalization for these segments. Furthermore, real-time adaptability is intro-
duced to adjust rewards based on evolving user behaviors, providing credit card issuers with a scalable solution 
for dynamic reward allocation. By overcoming the limitations of previous approaches, this research offers a 
refined and adaptable framework for optimizing credit card rewards, ultimately improving customer satisfaction 
and loyalty in the Indian market [19, 20].

2.1   Discussion of Traditional Reward Programs and Their Limitations

Traditional credit card reward programs have long relied on mechanisms such as points, cashback, and discounts 
to incentivize spending. While effective in fostering customer loyalty, these programs face significant limitations 
as consumer preferences evolve and data analytics capabilities advance. A key limitation is the lack of personali-
zation. Currently available rewards systems provide fixed incentives irrespective of individual spending habits, 
leading to a disconnect between consumer preferences and program benefits. For example, whether a customer 
spends primarily on groceries or luxury goods, the rewards remain the same, failing to foster deeper engagement 
of influential customers. Similarly, cashback programs appeal to a broad audience but do not account for varying 
spending patterns. Luxury shoppers and everyday spenders may receive identical cashback rates, even though 
high-value customers have greater profitability potential. This lack of differentiation can cause affluent users to 
switch to competitors credit card companies which offer personalized rewards.

Tiered reward structures attempt to introduce differentiation by providing better reward points for specific 
categories like travel and dining. However, these programs are typically static and do not align with individual 
spending behaviors. Furthermore, they target broad consumer groups, often overlooking niche markets that could 
benefit from more granular incentives. Seasonal promotions also present limitations; while increased points during 
holidays may drive short-term spending, they fail to sustain engagement throughout the year and do not cater 
to personalized needs. Traditional reward programs also rely on rigid, rule-based systems that do not leverage 
real-time data to adjust rewards based on evolving consumer behavior. Unlike modern, data-driven approaches,

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 4 -->

165

Page 4 of 21

https://doi.org/10.1007/s44196-025-00899-0

g
n
i
d
n
e
p
s

e
m

i
t
-
l
a
e
r

n
o

d
e
s
a
b
y
l
l
a
c
i
m
a
n
y
d

t
s
u
j
d
a

s
e
i
g
e
t
a
r
t
s

n
o
i
t
a
c
o
l
l
a

s
e
i
r
o
g
e
t
a
c

g
n
i
d
n
e
p
s
-
h
g
i
h

o
t

d
e
r
o
l
i
a
t

s
m
a
r
g
o
r
p

t
a
h
t

s
d
r
a
w
e
r

d
e
z
i
l
a
n
o
s
r
e
p

n
e
v
i
r
d
-
L
M

s
t
n
e
m
e
l
p
m

I

d
r
a
w
e
r

c
i
t
a
t
s

n
o

d
e
i
l
e
r

s
l
e
d
o
m
d
r
a
w
e
r

g
n
i
t
s
i
x
E

d
r
a
w
e
r

d
e
r
o
l
p
x
e

]
1
1
[

e
d
e
t
S
r
e
d
n
a
V
d
n
a

a
m
e
e
h
C

n
o
i
t
a
z
i
l
a
n
o
s
r
e
p

d
r
a
w
e
R

s
d
n
e
r
t

l
e
v
a
r
t

d
n
a
y
r
u
x
u
l

e
k
i
l

k
r
o
w
s
i
h
t

n
i

d
e
s
s
e
r
d
d
A

d
e
fi

i
t
n
e
d
I

s
p
a
G

h
c
r
a
e
s
e
r

s
u
o
i
v
e
r
P

s
n
o
i
t
u
b
i
r
t
n
o
c

r
u
o

d
n
a

,
s
p
a
g

d
e
fi

i
t
n
e
d
i

,
h
c
r
a
e
s
e
r

s
u
o
i
v
e
r
p

f
o

n
o
s
i
r
a
p
m
o
C

1
e
l
b
a
T

t
c
e
p
s
A

e
m

i
t
-
l
a
e
r

h
t
i

w
g
n
i
r
e
t
s
u
l
c

s
n
a
e

-

M
K
s
e
g
a
r
e
v
e
L

,
s
n
r
e
t
t
a
p
g
n
i
d
n
e
p
s

n
i

s
t
f
i
h
s

o
t

y
t
i
l
i
b
a
t
p
a
d
a

d
e
k
c
a
L

m
o
d
n
a
R

,
s
n
a
e

-

M
K
d
e
s
u

]
3
1

,
2
1
[

u
H
d
n
a

,
i
a
g
N

,
i

L

n
o
i
t
a
t
n
e
m
g
e
s

r
o
f

s
e
u
q
i
n
h
c
e
t

L
M

o
t

l
e
v
a
r
t

d
n
a

y
r
u
x
u
l

s
a

h
c
u
s

s
e
i
r
o
g
e
t
a
c

n
i

g
n
i
d
n
e
p
s

e
u
l
a
v
-
h
g
i
h

r
o
f

s
e
r
u
t
c
u
r
t
s

d
r
a
w
e
r

d
e
t
e
g
r
a
t

h
t
i

w

n
o
i
t
a
c
o
l
l
a

d
r
a
w
e
r

e
n
fi
e
r

g
n
i
d
n
e
p
s

t
n
e
m
e
g
a
g
n
e

y
r
a
n
o
i
t
e
r
c
s
i
d

n
o

d
e
s
a
b
s
r
e
s
u

t
n
e
m
g
e
s

o
t

s
e
t
a
d
p
u

s
e
r
u
t
c
u
r
t
s

d
r
a
w
e
r

c
i
t
a
t
s

o
t

g
n
i
d
a
e
l

r
e
m
u
s
n
o
c

r
o
f

g
n
i
t
s
o
o
B

t
n
e
i
d
a
r
G
d
n
a

,
t
s
e
r
o
F

g
n
i
d
n
e
p
s

n
o
i
t
a
t
n
e
m
g
e
s

s
t
e
s
a
t
a
d

l
a
n
o
i
s
n
e
m
i
d

s
e
i
r
o
g
e
t
a
c

e
u
l
a
v
-
h
g
i
h

-
h
g
i
h

n
i

g
n
i
t
t

fi
r
e
v
o

e
c
u
d
e
r

d
n
a

s
s
e
n
t
s
u
b
o
r

l
e
d
o
m

r
o
i
v
a
h
e
b

r
e
s
u

g
n
i
v
l
o
v
e

n
i

r
o
i
v
a
h
e
b

r
e
m
u
s
n
o
c

g
n
i
t
c
i
d
e
r
p

r
o
f

M
B
G
t
h
g
i
L

e
c
n
a
h
n
e

o
t

s
e
u
q
i
n
h
c
e
t

n
o
i
t
a
z
i
r
a
l
u
g
e
r

s
e
c
u
d
o
r
t
n
I

o
t

t
p
a
d
a

t
o
n

d
i
d

d
n
a

c
i
t
a
t
s

e
r
e
w
s
l
e
d
o
m
e
s
e
h
T

d
n
a

t
s
o
o
B
G
X
d
e
y
o
l
p
m
e

]
4
1
[

n
e
h
C
&

,
u
X

,
n
a
G

n
o
i
t
c
i
d
e
r
P
n
r
e
t
t
a
P
g
n
i
d
n
e
p
S

d
r
a
w
e
r

e
z
i
m

i
t
p
o

o
t

l
e
v
a
r
t

d
n
a

y
r
u
x
u
l

n
i

g
n
i
d
n
e
p
s

s
n
o
i
t
a
t
i

m

i
l

t
e
s
a
t
a
d

o
t

e
u
d
s
t
n
e
m
g
e
s

e
u
l
a
v
-
h
g
i
h

n
i

l
a
r
e
n
e
g

n
o

d
e
s
u
c
o
f

]
5
1
[

”
t
e
s
a
t
a
D
n
o
i
t
c
a
s
n
a
r
T

y
r
a
n
o
i
t
e
r
c
s
i
d

h
t
i

w
s
l
e
d
o
m
e
v
i
t
c
i
d
e
r
p
s
n
g
i
l

A

s
n
r
e
t
t
a
p

g
n
i
d
n
e
p
s

e
z
i
l
a
r
e
n
e
g

o
t

d
e
l
g
g
u
r
t
s

s
d
o
h
t
e

M

d
r
a
C

t
i
d
e
r
C
“

s
’
h
s
a
k
A

t
a
d
a
S
g
n
i
z
i
l
i
t
u

s
e
i
d
u
t
S

n
o
i
t
a
z
i
l
i
t

U

t
e
s
a
t
a
D

n
o
i
t
u
b
i
r
t
s
i
d

s
n
o
i
t
c
i
d
e
r
p

r
e
s
u

e
c
n
a
h
n
e

d
n
a

s
e
r
u
t
c
u
r
t
s

d
r
a
w
e
r

e
z
i
m

i
t
p
o

o
t

s
e
i
r
o
g
e
t
a
c

e
l
b
i
g
i
l
e
-
d
r
a
w
e
r

n
i

s
r
o
i
v
a
h
e
b

g
n
i

s
t
l
u
a
f
e
d

d
r
a
c

t
i
d
e
r
c

t
c
i
d
e
r
p

o
t

s
l
e
d
o
m
L
M
d
e
i
l
p
p
a

g
n
i
d
n
e
p
s

y
r
a
n
o
i
t
e
r
c
s
i
d

g
n
i
t
c
i
d
e
r
p

o
t

s
u
c
o
f

s
t
f
i
h
S

-
d
n
e
p
s

r
e
m
u
s
n
o
c
n
a
h
t

r
e
h
t
a
r
k
s
i
r

t
i
d
e
r
c
n
o
d
e
s
u
c
o
F

]
7
1
[

.
l
a

t
e

h
a
d
a
j
y
a
S
d
n
a

]
6
1
[

i
y
l
e
h
r
a
s
a
V
d
n
a

n
u
S

n
o
i
t
c
i
d
e
r
P
r
o
i
v
a
h
e
B

l
a
i
c
n
a
n
i
F

e
u
l
a
v
-
h
g
i
h
t
e
g
r
a
t

t
a
h
t

s
l
e
d
o
m
L
M

s
e
t
a
r
o
p
r
o
c
n
I

s
l
e
d
o
m
e
v
i
t
c
i
d
e
r
p

n
g
i
l
a

t
o
n

d
i
d

s
k
r
o
w
g
n
i
t
s
i
x
E

s

M
V
S
d
n
a

s
e
e
r
t

n
o
i
s
i
c
e
d

d
e
s
u

]
8
1
[

e
e
L
d
n
a

g
n
e
T

s
d
r
a
w
e
R
c
fi
i
c
e
p
S
-
y
r
o
g
e
t
a
C

s
t
i
b
a
h

r
e
m
u
s
n
o
c
g
n
i
v
l
o
v
e
h
t
i

w

t
n
e
m
n
g
i
l
a
g
n
i
r
u
s
n
e

,
s
m
a
r
g

r
o
i
v
a
h
e
b

g
n
i

s
e
i
g
e
t
a
r
t
s

n
o
i
t
a
c
o
l
l
a

-
o
r
p

d
r
a
w
e
r

o
t

y
t
i
l
i
b
a
t
p
a
d
a

e
m

i
t
-
l
a
e
r

s
e
c
u
d
o
r
t
n
I

-
d
n
e
p
s

e
m

i
t
-
l
a
e
r

n
o

d
e
s
a
b

s
e
t
a
d
p
u

c
i
m
a
n
y
d

d
e
k
c
a
L

d
r
a
w
e
r

c
i
t
a
t
s

n
o

d
e
i
l
e
r

s
l
e
d
o
m
d
r
a
w
e
r

g
n
i
t
s
i
x
E

y
t
i
l
i
b
a
t
p
a
d
A
e
m
T
-
l
a
e
R

i

e
l
i
h
w
s
e
i
r
o
g
e
t
a
c

g
n
i
d
n
e
p
s

n
i
g
r
a
m
-
h
g
i
h

d
r
a
w
o
t

s
a
e
r
a

n
i
g
r
a
m
w
o
l

-

n
i

s
t
s
o
c

g
n
i
z
i
m
i
n
i
m

s
e
i
r
o
g
e
t
a
c

g
n
i
d
n
e
p
s

s
e
v
i
t
n
e
c
n
i

s
e
v
i
t
n
e
c
n
i

g
n
i
t
c
e
r
i
d

y
b

n
o
i
t
a
c
o
l
l
a

d
r
a
w
e
r

s
e
z
i
m

i
t
p
O

t
n
e
r
e
ff
i
d

s
s
o
r
c
a

s
d
r
a
w
e
r

f
o

n
o
i
t
a
c
o
l
l
a

t
n
e
i
c
ffi
e
n
I

d
a
o
r
b

d
n
a

k
c
a
b
h
s
a
c

d
e
x
fi
d
e
s
u
s
l
e
d
o
m

l
a
n
o
i
t
i
d
a
r
T

y
c
n
e
i
c
ffi
E

t
s
o
C

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 5 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 5 of 21

165

they lack the ability to dynamically tailor incentives based on spending patterns and life events. Additionally, the 
one-size-fits-all approach diminishes the potential for high-value customers to feel incentivized. Without targeted 
rewards, companies miss opportunities to retain and maximize the spending of their most profitable users.

2.2   Benefits of Personalized Rewards Based on Spending Habits

The implementation of ML and data analytics in personalized rewards systems provides numerous benefits over 
traditional models. By aligning incentives with individual preferences, these systems enhance customer loyalty, as 
tailored rewards create stronger emotional connections with users. When customers receive incentives relevant to 
their spending behaviors such as travel points for frequent travelers or luxury bonuses for high-end shoppers, they 
are more likely to remain engaged with their credit cards, leading to higher retention rates and increased spending.
Personalized rewards also optimize program efficiency by directing incentives toward profitable categories, such 
as travel and luxury, while reducing rewards for low-margin purchases like groceries or usage for EMI payments. 
This targeted approach allows credit card companies to manage costs more effectively while maximizing customer 
satisfaction. Additionally, real-time insights enable companies to create dynamic, behavior-driven promotions, 
such as double points during specific periods, prompting users to spend more in key categories. Personalized 
offers further create a sense of exclusivity, fostering higher engagement with the credit card’s app or services.

By encouraging spending in targeted categories, personalized rewards help prioritize high-value transac-
tions. For example, users may shift more travel or luxury purchases to a card offering superior rewards in those 
categories, increasing transaction volumes and overall spend. Improved customer satisfaction and retention are 
also achieved, as users who feel valued through relevant incentives experience greater contentment, reducing the 
likelihood of churn. Retaining satisfied customers is significantly more cost effective than acquiring new ones, 
reinforcing long-term loyalty.

Furthermore, spending data enables tailored marketing efforts by providing relevant offers based on individual 
behavior. For instance, a customer who frequently dines at restaurants could receive targeted dining promotions, 
improving conversion rates and enhancing the overall customer experience. Additionally, machine learning models 
facilitate better customer insights and predictive modeling by analyzing spending patterns and forecasting future 
behaviors. This allows issuers to proactively adjust rewards, such as increasing travel points before peak holiday 
seasons for users likely to spend more on trips. Ultimately, personalized reward systems provide a competitive 
advantage in the financial industry. In a highly competitive market, offering tailored incentives differentiates 
card issuers and attracts customers seeking meaningful benefits. Companies that implement such data-driven 
approaches position themselves as innovators, strengthening their brand image and market appeal.

3   Proposed Methodology

Steps involved in proposed methodology for credit card users reward calculation is outlined in Fig. 1. Detailed 
description of steps is covered in subsequent sections. The process of credit score calculation starts with gathering 
data from open-source repository and its exploration for usage in reward calculation.

3.1   Analysis of Dataset

The original dataset, referred to as the Analyzing Credit Card Spending Habits in India, had several limitations 
that hindered its utility for advanced analysis and model development [21]. The key columns and their descrip-
tions are outlined in Table 2.

The provided figures showcase different visualizations of the dataset. Figure 2 helps in identifying patterns 
associated with original dataset and reflects the data as they are explored on various parameters including in 
central tendency, skewness, and variability. Figure 2a, reflecting a plot of transaction amounts, is particularly

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 6 -->

165

Page 6 of 21

Fig. 1   Methodology for calculation 
of credit score

https://doi.org/10.1007/s44196-025-00899-0

Table 2   Description 
of attributes in original 
dataset

Column

Index
City
Date

Card Type
Exp Type
Gender
Amount

Description

Sequential Identifier for each transaction
The location where the transaction took place
The transaction date (with outdated values,

primarily from 2014 to 2015)

The type of card used for the transaction
Type of Expense
Gender of the cardholder
Monetary value of the transaction

useful for detecting outliers and patterns followed by users, as it visually demonstrates the spread of the data. 
Figure 2b shows the distribution of original data based on gender of holder of the card, a look clearly reflects that 
female are using card more than male spenders. Figure 2c shows the distribution of card types helps interpret the

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 7 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 7 of 21

165

(a) Distribution of Transaction Amounts

(b) Distribution of Gender

(c) Distribution  of Card type

(d) Distribution of Expense type

Fig. 2   Exploratory data analysis of original dataset

variety and frequency of credit card usage, providing insights into behavior of customers. Figure 2d representing 
the plot of expenditure types shows how transaction amounts are allocated across different categories of expenses, 
offering an enhanced understanding of consumer spending behavior.

After visualizing the dataset available in public repository, limitations are found that deter more detailed 
analysis for fair calculation of reward points. Firstly, the Index attribute lacks user-specific identifiers, hindering 
effective segmentation of the data and making it difficult to analyze user-level behaviors or generate personalized 
insights for analysis. Also, the Date field contains many missing or outdated values, especially from 2014 to 2015 
which is quite obsolete as well; this makes temporal analysis challenging and prevents tracking of trends over 
time. Amounts spend monthly in the field is significant, it lacks contextual details, and this added information 
would enrich the analysis and offer deeper insights into spending behaviors of customers. This indicates a need 
for generating a synthetic dataset to better capture and represent the real transaction distribution. These limita-
tions underscore the need for further data enhancement and preprocessing to improve the quality of data analysis.

3.2   Generation and Analysis of Synthetically Generated Dataset

To address the limitations of the original dataset and to have a fair distribution of reward points, a new dataset is 
generated, which includes more relevant and detailed columns. To generate synthetic credit card data, the Faker 
library in Python was used, defining column names, ranges, and relationships between values. It was ensured that

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 8 -->

165

Page 8 of 21

https://doi.org/10.1007/s44196-025-00899-0

certain attributes like credit score and attrition risk were correlated. To determine the attribute values, multiple 
GitHub repositories were explored and datasets related to credit card transactions. Later, a list of potential 
attributes were compiled and fed into an LLM and asked it to suggest the most potent ones for our project. The 
suggestions were reviewed to ensure they made sense and used a trial-and-error approach with feature engineering 
to identify the most significant attributes. We used a correlation matrix to determine the attributes with the highest 
positive correlation and dropped the ones that were not significant.

Explanation of Key Steps:

•  Synthetic Data Generation: The generate_synthetic_data() function creates synthetic records for credit card 
users, incorporating random values for attributes such as credit_score, monthly_spend, and attrition_risk.
•  Feature Engineering: A correlation matrix is computed to identify and select the most relevant attributes. The

dataset is filtered to include only the most important features.

•  Reward Points Calculation: A custom function calculate_reward_points() is defined to calculate reward points

based on monthly_spend.

This enhanced dataset allows for a more comprehensive analysis of customer behavior and the development

of personalized reward strategies. Table 3 outlines the features included in the new dataset.

The inclusion of added attributes significantly improves the dataset’s ability to support personalized analysis 
and predictions for credit points. The User ID helps individual-level tracking and segmentation, allowing for 
more tailored insights into customer behavior. The Card Promotion Date provides valuable information on 
customer progression to higher card levels, which enhances the ability to personalize reward programs based 
on a customer’s status. The Expense Type categorizes spending into luxury, travel, and nominal types, enabling 
a more refined analysis of customer spending patterns and preferences. The inclusion of the Income Category 
allows for a better understanding of the customer’s spending power, which is critical for customizing reward 
offers. Furthermore, the Number of Cards held by a customer offers insight into their overall spending behavior, 
providing another dimension for creating targeted rewards. The addition of Number of active Loans of a card 
holder helps contextualize the customer’s financial behavior and spending limitations, and this attribute finds 
usage in predicting a customer future purchasing behavior. Demographic information such as Customer Age and 
the Months Spent with Bank allows for customer segmentation depending on life stage, offering opportunities 
for more effective marketing strategies. The Risk of Attrition flag is a vital indicator for identifying at-risk

Table 3   Description of 
attributes in synthetic 
dataset

Column

Description

User ID
City
Date of Transaction
Card Type
Card Promotion Date
Expense Type
Amount
Income Category
Number of Cards
Number of Loans
Customer Age
Months Spent with Bank
Risk of Attrition
# Transactions per month)
Month of Transaction
Monthly Spending (on average)

Unique Identifier for each customer, enabling user level tracking
The location where the customer uses the card
The transaction date, indicating when the card is used
Type of card used
Date when the customer is promoted to a new card level
Categorized type of expense
Monetary value of the transaction
Salary range of the customer
Number of credit cards held by the customer
Number of loans the customer has taken
Age of the customer
Duration of the customer’s relationship with the bank
Flag indicating whether the customer is likely to leave the bank
The average number of transactions made per month
The month of the transaction
Total amount spent by the customer in the given month

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 9 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 9 of 21

165

customers, which can guide customer retention efforts. Lastly, attributes like Number of Transactions (per month) 
and Monthly Spending (average) provide information about spending frequency and overall expenditure, helping 
more precisely calculate reward points and user’s eligibility. These additions make the dataset much more suitable 
and customized for ML models, allowing for better customer profiling and more personalized reward structures 
[22, 23].

Figure 3 presents an exploratory data analysis of the synthetic dataset, with each subplot providing insights 
into different features of the dataset generated for reward points calculations. Figure 3a illustrates the distribution 
of transaction amounts, showcasing how the amounts are spread across the card types in dataset.

Figure 3b highlights the monthly spending trends across 15 months. It can be inferred that during festive sea-
sons as Diwali, Christmas, and Holi, the spending by credit card users shows an increasing trend substantiating 
the claim made that for customer retention credits need to be given for increased spending during festive seasons.

Fig. 3   Exploratory data 
analysis of synthetic dataset

(a) Box Plot of Spending Amount with Card Type

Int J Comput Intell Syst          (2025) 18:165

(b) Monthly spending Trends Generated by synthetic Dataset

---

<!-- PAGE 10 -->

165

Page 10 of 21

https://doi.org/10.1007/s44196-025-00899-0

3.3   Data Cleaning and Transformation

Before preparing the credit card transaction dataset for analysis and model training the data need to be ensured 
for readiness. The steps performed to clean and transform the dataset include the following:

1.  Date Conversion: The Date field in the dataset was originally in string format. To facilitate easier date manipu-
lation and enable temporal analysis, this field was converted into a datetime format. This transformation allows 
for the extraction of specific components such as month, year, and day, which are essential for time-based 
analysis and trends in customer behavior.

2.  Encoding Categorical Variables: Variables which are of specific category such as Gender, Card Type, and 
Expense Type are encoded using One-Hot Encoding, transforming these variables into numerical format [24]. 
This is done to ensure their efficient usage and processing by ML models that necessitates numerical input.

3.4   Unsupervised Learning: K‑Means Clustering

In the next stage, clustering techniques to segment users based on their credit card type are employed. The cus-
tomized synthetic dataset consists of four distinct card types: Platinum, Gold, Silver, and Signature. Each of these 
cards offers different privileges, bonuses, and benefits that affect credit card users’ usage patterns and financial 
engagements. The clustering process and results obtained are interpreted. Besides K-means, Density-Based Spatial 
Clustering of Applications with Noise (DBSCAN), and Gaussian Mixture Models (GMM) [25] clustering are 
employed and Clustering Evaluation Matrices Silhouette Scores and Davies-Bouldin Index (DBI) are evaluated for 
the clusters made on the basis of card types for synthetic dataset. Since a high silhouette score confirms meaning-
ful segmentation, it reinforces that Card Type aligns well with spending behavior and is a strong clustering factor.
A look on Fig. 4 reveals that for K-Means and DBSCAN clustering techniques both performance indices of 
clustering models, viz., silhouette score and DB index, are appreciable. Either of these can be used to validate 
the proposed hypothesis that clustering based on card types will better segment users. Silhouettes score which 
range from -1 to + 1, and values near 1 are considered better as this indicates how well each of data points is 
clustered. Moreover, DB index, which is a validation index used by researchers in order to assess the optimal 
number of clusters to use, should be less than 1. A lower value of DB index suggests compactness and minimal 
overlap between clusters.

•  Feature Selection for Clustering Card Types: Several features were chosen for clustering, that efficiently capture

the spending behavior of credit card users:

–  Monthly Spend: This attribute considers the total amount spent per month on the card, thus helping dif-

ferentiate card types based on spending patterns.

–  Transactions Per Month: Indicates the frequency of card usage, with higher values typically seen in Plati-

num and Signature cardholders.

–  Credit Utilization: Expense Category: Credit utilization is a factor considered for rewarding customers 
who have utilized the spending till their credit limit. Customers who have spent much to their credit limit 
will be rewarded more than who have spent less.

Fig. 4   Performance scores of clustering models

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 11 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 11 of 21

165

–  Year and Month of Transaction: Helps in recognizing temporal patterns in spending through usage of cards.

Also to reward customers who have used card in festive seasons.

–  K-Means Clustering Algorithm: The clustering is done using the K-Means algorithm as the selected model 
Selecting the Number of Clusters (K): The number of clusters for assessment is set to 4, based on the dif-
ferent card types. The value of K can be changed based on types of cards issued by credit card companies.

•  Practical Use Cases for Proposed Clusters: The insights received from clustering are applicable in multiple

ways [26]:

–  Targeted Marketing: Customized marketing and card promotional strategies to each cluster, offering Plati-

num card holders luxury goods promotions, and silver users shopping deals or cashback offers.

–  Customized Reward Programs: Design reward by credit points programs aligned with the spending behavior

of each category of users to enhance satisfaction by fair distribution.

–  Customer Retention: Develop strategies to retain customers, as providing personalized bonuses to high-

spenders and cardholders.

3.5   Clustering Analysis

The users are segmented based on their spending behavior and card type, using clustering techniques to group 
them into four clusters. These clusters represent different user types based on their spending categories, which 
help in understanding the underlying patterns in card usage [27, 28]. The clusters and their characteristics are as 
follows:

•  Interpreting the Clusters: The resulting four based on card types of clusters are analyzed as follows:

–  Cluster 1 (Platinum Cardholders): Credit card holders in this cluster show high spending, frequent usage,

and a preference for luxury and travel expenses.

–  Cluster 2 (Gold Cardholders): Users in this group demonstrate moderate spending and balanced transac-

tion frequency, mixing luxury and basic purchases.

–  Cluster 3 (Silver Cardholders): This group focuses on lower spending, mainly on essential items like

groceries, and has lower income.

–  Cluster 4 (Signature Cardholders): Users here focus on routine expenses with minimal variability in spend-

ing

Table 4   Base reward points

Card type

Platinum
Signature
Gold
Silver

Int J Comput Intell Syst          (2025) 18:165

Base reward rate

5 points
4 points
3 points
2 points

---

<!-- PAGE 12 -->

165

Page 12 of 21

Table 5   Base multiplier for 
card types (RCT)

Table 6   Expense type 
bonus (ET) and associated 
reward points

Card type

Platinum
Signature
Gold
Silver

Expense type

Travel/Dining
Luxury
Entertainment
Groceries/Bills
Other Expenses

https://doi.org/10.1007/s44196-025-00899-0

Base multi-
plier (RCT)

2.0
1.5
1.0
0.5

Bonus 
points 
(ET)

+ 3.0
 + 2.0
 + 1.0
0.5
0.0

3.6   Reward Points Calculation

The reward points calculation method is discussed for both the original and synthetic datasets. The original dataset 
lacks detailed transaction-level data, so the calculation is based on the card type alone. On the other hand, the 
synthetic dataset allows for a more granular calculation considering multiple factors.

3.6.1   Original Dataset

In the original dataset, since transaction-level data are unavailable, reward points are calculated based solely on 
the card type. The base reward points for each card type are shown in Table 4.

Reward Points (Old dataset) =

Amount Spent Monthly ∗ Points Scored (Based on Card Type)
500

.

3.6.2   Synthetic Dataset

For the synthetic dataset, reward points are calculated using a more detailed approach that considers several fac-
tors. These include the card type, promotion status, expense type, income category, number of cards, and attrition 
risk. The calculation is as follows:

Reward Points (Synthetic Dataset) =

Scored Points ∗ Amount Spent
500

,

Scored Points = [RCT + CPD + ET + IC + NoC + AR],

where. RCT = Base multiplier based on Card Type (refer to Table 5), CPD = Card Promotion Date bonus, 
ET = Expense Type bonus (refer to Table 6), IC = Income Category bonus, NoC = Penalty for additional cards, 
AR = Attrition Risk bonus.

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 13 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 13 of 21

165

•  Base Multiplier for Card Types (RCT): The base multiplier for reward points is determined based on the type 
of card owned by a customer. Higher multipliers are assigned to premium card types, as detailed in Table 5.

•  Income Category Bonus (IC): Customers in the high-income category receive a bonus of 1 or for middle

income a reward point of 0.5 is suggested.

•  Number of Cards (NoC): Customers with more cards receive a slight penalty to encourage consolidation.

For every additional card beyond the first, a multiplier of -0.5 is done.

•  Attrition Risk (AR): Customers with a higher attrition risk receive an additional reward of + 1.0 points to

incentivize loyalty.

•  Expense Type Bonus (ET): Customers earn higher rewards for discretionary categories like Travel and

Dining. The bonus rewards for different expense types are detailed in Table 6.

To summarize, the total reward points are computed by summing the values from all six factors mentioned 
above. These reward points are then scaled by the monthly amount spent to determine the final reward points. 
Thus, K-Means clustering was used for segmenting users based on their spending patterns, allowing one to 
group users by likely card types. In the original dataset, reward points were based on card type, while in the 
synthetic dataset, the calculation was more intricate, incorporating multiple factors such as expense type, card 
promotion, and income category.

Table 6 shows expense types, bonuses, and associated reward points. The logic here is that customers earn 
higher rewards for categories like travel and dining, and lower rewards for groceries, bills, and other expenses. 
The scaling factor used is arbitrary and can be adjusted. The goal is to encourage spending on discretionary 
expenses like travel, luxury shopping, and dining by providing higher reward points, while discouraging 
spending on necessities like groceries and bills.

For example, in Table 6, travel and dining have a bonus factor of + 2.0, luxury has + 1.5, entertainment

has + 1.0, and groceries and bills have + 0.5.

–  If the scaling factor is changed, all other values should be scaled similarly.
–  This allocation of reward points is up to the discretion of the credit card company.

Our research aims to demonstrate the effectiveness of reward point calculation, and banks can use and 
modify our approach according to their needs. The specific values are suggestive and not meant to be taken 
as a standard. Banks can adjust the factors to allocate reward points differently based on spending categories.
The multipliers + 2.0, + 1.5, + 1.0, and + 0.5 are chosen for ease of calculation and because they are rela-
tively close to each other. Since banks and credit card companies do not publicly disclose their actual multipli-
ers for calculating reward points, these values are subjective and intended to provide a reasonable approxima-
tion. They are not fixed and can be adjusted as needed by the credit card company.

4   Results and Discussions

In this section, we present the results from the clustering analysis and reward points calculation, followed by 
a detailed discussion of the insights and how they align with the expected patterns.

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 14 -->

165

Page 14 of 21

https://doi.org/10.1007/s44196-025-00899-0

Fig. 5   Cluster-based analysis based on card type

Fig. 6   Distribution of reward points

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 15 -->

https://doi.org/10.1007/s44196-025-00899-0

4.1   Cluster Analysis Results

Page 15 of 21

165

Validating Card Type as the Best Clustering Approach has been done to segregate user. The goal was to 
determine whether Card Type (Platinum, Gold, Silver, Signature) is the most effective way to segment users. 
Through multiple evaluations, strong evidence supporting this hypothesis is obtained. By clustering users and 
analyzing the distribution of card types within each group, a clear separation based on card type is observed. 
This helps in understanding how users behave according to their spending patterns. Figure  5 shows 2D 
visualization of the cluster obtained by K-means clustering technique. Visualization in 3D clearly segregates 
the 4 clusters made based on card type held by customers. Clear separation of Card Types within clusters 
proves its natural segmentation power.

K-Means achieved a score of 0.42, outperforming other clustering techniques (DBSCAN, Hierarchical, GMM). 
The performance of clustering models used in this work is compared to Silhouette Scores and Davies-Bouldin 
Index (DBI) for the clusters made based on card types for synthetic datasets. High silhouette score confirms 
meaningful segmentation [29], and it reinforces that Card Type aligns well with spending behavior and is a strong 
clustering factor. Thus, the clustering analysis effectively differentiates user behaviors and spending patterns, 
providing a clear framework to associate spending habits with card types.

4.2   Reward Points Distribution

Figure 6 presents the distribution of reward points for both the original and synthetic datasets.

Figure 6 illustrates the reward point distribution based on five columns present in the original dataset, as well 
as in a synthetically generated dataset that incorporates additional features necessary for a systematic reward 
point calculation [30, 31]. These five columns were also synthetically created since the original dataset lacks 
certain essential features, as discussed earlier. The analysis in Fig. 6 indicates that, with only five features as in

Fig. 7   Cumulative distribution of reward points

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 16 -->

165

Page 16 of 21

https://doi.org/10.1007/s44196-025-00899-0

the original dataset, the reward points are restricted to a maximum value of 1000 in synthetic dataset due to the 
absence of detailed information.

However, in the synthetic dataset, including the additional features outlined in Table 3, the reward point 
distribution extends over a broader and more justified range, ranging from 0 to 3500. Figure 7 presents the 
cumulative distribution of reward points. The figure clearly demonstrates that utilizing synthetic data with 
additional significant features results in a more systematic and justified approach to rewarding credit card users. 
This method considers multiple parameters rather than relying solely on the five features present in the original 
dataset. Figure 7 underlines the distribution of reward points categorized by spending type, highlighting how 
different spending patterns influence reward allocation.

4.3   Comparative Evaluation of Reward Point: Original vs. Synthetic Dataset

The use of a synthetic dataset for reward point calculation in credit card transactions offers several key benefits. It 
effectively captures clear and explainable relationships between variables, ensuring transparency in data analysis. 
Despite having less features, the synthetic dataset maintains strong predictive performance due to its thoughtful 
and systematic design. The inclusion of additional features significantly increases model performance, leveraging 
more significant data for calculation. Furthermore, the synthetic dataset is inherently superior, as its theoretical 
framework translates into durable predictive capabilities, making it an asset for modeling and analysis of reward 
points.

Case study: Cardholder XYZ's Reward Calculation Analysis
Cardholder Profile:

•  Card Type: Signature (Original: 4 points/500, Synthetic: RCT = 1.5)
•  Monthly Spending on Card: 50,000
•  Card Promotion Date Bonus (CPD): + 2 (new card promotion)
•  Expense Type Bonus (ET): + 3 (60% travel expenses)
•  Income Category Bonus (IC): + 1 (high-income bracket)
•  Number of Cards Penalty (NoC): − 1 (holds 3 cards)
•  Attrition Risk Bonus (AR): + 0 (medium-risk customer)
•  Original Dataset Calculation:

The original formula for calculating reward points is given by the following equation:

Reward Points (Synthetic Dataset) =

Scored Points ∗ Amount Spent
500

.

For Cardholder XYZ, the calculation proceeds as follows:

•  Card Type Multiplier for Signature: 4 points per 500 spent
•  Reward Points Calculation:

Reward Points (Synthetic Dataset) =

4 ∗ 50000
500

= 400 points.

The original formula has several limitations. First, it solely considers the amount spent and the card type, pro-
viding a simplistic calculation that does not incorporate any personalization. This approach overlooks important 
customer information, such as spending patterns, income levels, and specific behaviors like travel expenses or 
promotional offers. Additionally, the formula fails to adjust for factors that could impact the reward calculation, 
such as promotional bonuses or penalties related to customer behavior, like holding multiple cards. As a result, 
it lacks the flexibility and adaptability required to accurately reflect individual customer profiles and behaviors.

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 17 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 17 of 21

165

2.  Synthetic Dataset Calculation:

In contrast, the synthetic dataset approach introduces a more personalized and dynamic reward calculation

formula:

Scored Points = [RCT + CPD + ET + IC + NoC + AR],

Reward Points (Synthetic Dataset) =

Scored Points ∗ Amount Spent
500

.

The steps for calculating the reward points in the synthetic dataset are as follows:
Step 1: Calculate Scored Points

•  RCT (Signature Card) = 1.5
•  CPD (Promotion Bonus) =  + 2
•  ET (Travel Expenses) =  + 3
•  IC (High Income) =  + 1
•  NoC (Penalty for Holding 3 Cards) = − 1
•  AR (Attrition Risk) =  + 0

Scored Points = [1.5 + 2 + 3 + 1 + −1 + 0] = 6.5

Step 2: Calculate Reward Points

Reward Points (Synthetic Dataset) =

6.5 ∗ 50000
500

= 650 points.

The synthetic dataset formula provides several advantages over the original approach:

1.  Personalization: The synthetic formula considers the cardholder’s individual characteristics, such as their 
travel spending (+ 3 ET) and high income (+ 1 IC), which the original formula overlooks. This allows for 
a more tailored and accurate calculation of reward points, reflecting XYZ’s specific spending behavior and 
profile.

2.  Flexibility: Unlike the original method, the synthetic formula can adjust for various factors such as promo-
tions (e.g., + 2 CPD for new cards) and penalties (e.g., − 1 NoC for holding multiple cards). This flexibility 
ensures that the reward system can evolve with changing customer behavior.

3.  Behavioral Incentives: The synthetic formula encourages desired behaviors, such as spending on travel, by 
offering higher rewards for such expenses. Conversely, it penalizes behaviors that are less profitable for the 
company, such as holding multiple cards. This creates a reward structure that aligns more closely with both 
customer engagement and business goals.

4.  Attrition Risk Mitigation: The formula incorporates an attrition risk factor (AR) to identify and potentially 
retain customers at risk of leaving. In the case of XYZ, despite being classified as a medium-risk customer, 
the formula’s ability to factor in such risks can be leveraged to develop targeted retention strategies.

Fig. 8   Comparison of reward points

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 18 -->

165

Page 18 of 21

https://doi.org/10.1007/s44196-025-00899-0

5.  Higher Granularity: The synthetic formula provides a more nuanced calculation of rewards. For example, 
while the original formula awards a flat 400 points for a $50,000 spend, the synthetic formula, accounting for 
the cardholder’s profile, results in 650 points. This granularity helps ensure that the reward structure better 
reflects customer behavior.

The clusters align with the expected card types, providing a clear differentiation between various user behaviors 
based on their spending patterns. Additionally, the reward points calculation methods for both datasets reveal a well-
aligned approach to incentivizing customers based on their spending habits and engagement. The clustering analysis 
and reward points calculations have resulted in providing significant insights into customer segmentation based on 
their card type and spending patterns. These results can be used to further improve targeted marketing, strategies for 
customer retention, and overall design of reward program where credits are distributed fairly.

4.4   Model Performance

Machine learning Models such as Linear Regression, XGBoost, and Random Forest are applied for predictions of 
reward points in synthetic dataset. The results obtained from these models substantiate the claims that synthetic 
dataset generated for reward point calculations offers a justified and varied distribution of reward points across discrete 
category of users based on parameters selected for calculating score points. The ML models whose performance for 
predictions outcomes others is selected for calculating score points. Figure 8 presents a comparative analysis of the 
reward points obtained for credit card customers using a synthetically generated dataset. By incorporating additional 
significant features for a more equitable distribution and calculation of reward points, the mean reward points have 
increased to approximately 1000, highlighting a considerable improvement in the system's efficiency.

The model performance results demonstrate a highly impressive  R2 value of 0.99 for both the Random Forest 
and XGBoost models, indicating an almost perfect fit to their respective datasets. However, when comparing the 
models based on performance metrics such as RMSE and MAE, the Random Forest model clearly outperforms 
both Linear Regression and XGBoost. Specifically, the Random Forest model achieves the lowest RMSE and 
MAE values, making it the most accurate and reliable model for predicting customer credit scores. This dem-
onstrates that, while all three models fit the data well, Random Forest excels in minimizing prediction errors, 
making it the most suitable choice for this particular task.

5   Conclusion

The clustering analysis successfully segregated spending behaviors across different card types, thus aligning with 
expected financial patterns. Usage of ML demonstrated strong performance in predicting user spending behaviors 
across both for the original as well as synthetic datasets. Additionally, the credit point distribution highlighted the 
benefits of including additional features, leading to a more systematic and justified reward calculation process.

The goal with this experiment is to showcase the efficiency of proposed formula for allocating reward points. 
Due to the unavailability of real credit card transaction data and reward point calculation methods, synthetic 
datasets have been used, and a formula has been developed accordingly. Machine learning models verify the 
effectiveness of formula, achieving an R2 score of 0.99, which indicates a near-perfect formula. The formula is 
flexible and can be modified to accommodate different variables and multipliers. The machine learning model can 
be used to test the efficiency of the formula, providing valuable insights for credit card companies. Ultimately, our 
goal is to demonstrate the effectiveness of our approach, which can be tailored to meet the specific needs of credit 
card companies. In our research, we developed a formula to calculate reward points based on various attributes, 
such as transaction type and credit card type. We then used a machine learning model to validate our formula by 
calculating reward points independently and comparing the results. The model gave information about everyone’s

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 19 -->

https://doi.org/10.1007/s44196-025-00899-0

Page 19 of 21

165

transactions and credit card type but not our specific formula or multipliers. The machine learning model's purpose 
was to provide an independent evaluation of our formula's performance. By comparing the model's results to our 
manually calculated reward points, we obtained an  R2 score of 0.99, indicating a high degree of accuracy. This 
suggests that our formula is robust and effective in calculating reward points.

For financial institutions and credit card companies, these findings emphasize the potential of machine learning 
to optimize reward programs, improve customer loyalty, and improve retention rates by following a justified and 
fair approach for reward points calculations. By leveraging transaction data, institutions can refine reward alloca-
tion, ensuring fair and personalized experience for customers. The insights gained also enable targeted marketing 
strategies, increasing engagement, and maximizing the effectiveness of promotional campaigns.

Expanding the model with demographic attributes could refine customer segmentation, allowing for deeper 
personalization. Beyond rewards, this framework can be extended to applications in fraud detection, credit risk 
assessment, and adaptive credit limit recommendations, reinforcing its value in financial decision-making.

Acknowledgements  The authors would like to thank the Symbiosis Institute of Technology, Symbiosis International (Deemed 
University) for the support.

Author contributions  All authors have contributed significantly to this research. Renuka Agrawal was responsible for con-
ceptualization, methodology, and provided supervision for writing—original draft. Aryan Khanna contributed to writing of 
original draft, data curation, software implementation, and validation. Safa Hamdare handled formal analysis, investigation, 
and writing—review and editing.  All authors reviewed and approved the final manuscript.

Funding  Open access funding provided by Symbiosis International (Deemed University). The authors received no financial 
support for the research and authorship of this article. However, they may receive funding from the Symbiosis Institute of 
Technology for publication.

Data availability  No datasets were generated or analysed during the current study.

Declarations

Conflict of interest  The authors declare no competing interests.

Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, 
and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material 
derived from this article or parts of it. The images or other third party material in this article are included in the article’s 
Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the 
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.

References

1.  Wu, J., Zhao, X., Yuan, H., et al.: CDGAT: a graph attention network method for credit card defaulters’ prediction. Appl.

Intell. 53, 11538–11552 (2023). https:// doi. org/ 10. 1007/ s10489- 022- 03996-1

2.  Ho, A.T., Morin, L., Paarsch, H.J., Huynh, K.P.: A flexible framework for intervention analysis applied to credit-card

usage during the coronavirus pandemic. Int. J. Forecast. 38(3), 1129–1157 (2022)

3.  Krivorotov, G.: Machine learning-based profit modeling for credit card underwriting-implications for credit risk. J. Bank.

Finance 149, 106785 (2023)

4.  Chang, V., Sivakulasingam, S., Wang, H., Wong, S.T., Ganatra, M.A., Luo, J.: Credit risk prediction using machine

learning and deep learning: a study on credit card customers. Risks 12(11), 174 (2024)

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 20 -->

165

Page 20 of 21

https://doi.org/10.1007/s44196-025-00899-0

5.  Patel, P., Chauhan, S., Gupta, S., Gupta, T., Agrawal, R.: Mitigating class imbalance with ensemble SMOTEfied-GAN: 
advancing detection strategies for automobile insurance fraud. Int. J. Fuzzy Logic Intell. Syst. 24(4), 333–342 (2024)

6.  deHaan, E., Kim, J., Lourie, B., Zhu, C.: Buy now pay (pain?) later. In: Management Science (2024)
 7.  Bello, O.A.: Machine learning algorithms for credit risk assessment: an economic and financial analysis. Int. J. Manag.

10(1), 109–133 (2023)

8.  Dal Colle, L.: Phygital: where and how we could intervene in the customer journey to provide a better customer

experience (2022)

9.  Xu, D., Zhang, X., Hu, J., Chen, J.: A novel ensemble credit scoring model based on extreme learning machine and

generalized fuzzy soft sets. Math. Probl. Eng. 2020(1), 7504764 (2020)

10.  Tripathi, D., Edla, D.R., Cheruku, R., Kuppili, V.: A novel hybrid credit scoring model based on ensemble feature

selection and multilayer ensemble classification. Comput. Intell. 35(2), 371–394 (2019)

11.  Cheema, A., Van der Stede, W.: Consumer spending habits and reward programs: a case study. J. Financ. Stud. 45(3),

89–112 (2019)

12.  Li, T., Ngai, E., Hu, Y.: Machine learning in financial services: applications, challenges, and future directions. J. Artif.

Intell. Res. 14(1), 78–102 (2021)

13.  Ngai, E., Hu, Y., Wong, Y.H., Chen, J.: AI and financial services: a comprehensive review. J. Mach. Learn. Res. 8(5),

34–56 (2022)

14.  Gan, Y., Xu, Z., Chen, L.: Predicting consumer behavior through machine learning: implications for credit card

companies. Int. J. Data Sci. 12(2), 45–67 (2021)

15.  Ho, H., Tien, K.M.T., Wu, A., Singh, S.: A sequence analysis approach to segmenting credit card customers. J. Retail.

Consum. Serv. 59, 102391 (2021)

16.  Sun, T., Vasarhelyi, M.A.: Predicting credit card delinquencies: an application of deep neural networks. Intell Syst.

Account. Financ. Manag. 25(4), 174–189 (2018)

17.  Sayjadah, Y., Hashem, I. A. T., Alotaibi, F., Kasmiran, K. A.: Credit card default prediction using machine learning 
techniques. In: 2018 Fourth International Conference on Advances in Computing, Communication & Automation 
(ICACCA), IEEE, pp. 1–4 (2018)

18.  Teng, H.W., Lee, M.: Estimation procedures of using five alternative machine learning methods for predicting credit

card default. Rev. Pac. Basin Financ. Mark. Policies 22(3), 1950021 (2019)

19.  Mittal, S., Tyagi, S.: Performance Evaluation of Machine Learning Algorithms for Credit Card Fraud Detection, pp.

320–324. https:// doi. org/ 10. 1109/ CON- FLUEN CE. 2019. 87769 25 (2019)

20.  Makki, S., Assaghir, Z., Taher, Y., Haque, R., Hacid, M., Zeineddine, H.: An experimental study with imbalanced

classification approaches for credit card fraud detection. IEEE Access 7, 93010–93022 (2019)

21.  Altman, E.: Synthesizing credit card transactions. In Proceedings of the Second ACM International Conference on AI

in Finance (ICAIF ’21), Association for Computing Machinery, New York, NY, USA (2022)

22.  Sadat, A.: Credit Card Spending Habits in India https:// www. kaggle. com/.  www. kaggle. com/ datas ets/ thede vasta tor/

analy zing- credit- card- spend ing- habits- in- India (2024). Accessed 24 Sept 2024

23.  Gkikas, D., Theodoridis, P.: AI in Consumer behavior (2022). https:// doi. org/ 10. 1007/ 978-3- 030- 80571-5
 24.  Yahaya, S.N., Bakar, M.H.: The critical factors influencing consumer spending by using credit card. J. Technol. Manag.

Technopreneurship 8(1), 117–128 (2020)

25.  Aniceto, M.C., Barboza, F., Kimura, H.: Machine learning predictivity applied to consumer creditworthiness. Futur Bus

J 6, 37 (2020)

26.  Aluri, A., Price, B.S., McIntyre, N.H.: Using machine learning to cocreate value through dynamic customer engagement

in a brand loyalty program. J. Hosp. Tour. Res. 43(1), 78–100 (2019)

27.  Nasir, M., Ezeife, C.I., Gidado, A.: Improving e-commerce product recommendation using semantic context and

sequential historical purchases. Soc. Netw. Anal. Min. 11(1), 82 (2021)

28.  Rane, N.: Enhancing customer loyalty through Artificial Intelligence (AI), Internet of Things (IoT), and big data

technologies: improving customer satisfaction, engagement, relationship, and experience, October 13, (2023)

29.  Kasaian, K., Murthi, B.P.S., Steffes, E.: Effects of teaser rates on new credit card customers’ spending and borrowing:

an empirical analysis. Int. J. Bank Market. 40(7), 1555–1574 (2022)

30.  Zarkesh, B.: Exploring the impact of AI-driven pricing on customer loyalty and churn rates in the banking industry,

Master’s thesis, NTNU (2023)

31.  Chen, Y., Lin, C., Zhao, Y., Xie, X., Zhang, M.: Modeling evolving user preferences for sequential recommendation

with credit card transactions. Preprint at arXiv arXiv: 2207. 06225. https:// arxiv. org/ abs/ 2207. 06225 (2022)

Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional 
affiliations.

Int J Comput Intell Syst          (2025) 18:165

---

<!-- PAGE 21 -->

https://doi.org/10.1007/s44196-025-00899-0

Authors and Affiliations

Page 21 of 21

165

Renuka Agrawal1

· Aryan Khanna1

· Safa Hamdare2

*  Renuka Agrawal

renuka.agrawal@sitpune.edu.in

Aryan Khanna

aryan.khanna.btech2023@sitpune.edu.in

Safa Hamdare 
safa.hamdare2021@my.ntu.ac.uk

1  Symbiosis International (Deemed University), Symbiosis Institute of Technology, Lavale Hill Base Campus, Pune, 
Maharashtra 412115, India
2  Department of Computer Science, Nottingham Trent University, Clifton Lane, Nottingham, 
Nottinghamshire NG11 8NS, UK

Int J Comput Intell Syst          (2025) 18:165

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Int J Comput Intell Syst (2025) 18:165
RESEARCH ARTICLE
Analyzing and Rewarding Credit Card Spending Habits
in India: a Machine Learning Approach
Renuka Agrawal1 · Aryan Khanna1 · Safa Hamdare2
Received: 24 February 2025 / Revised: 15 May 2025 / Accepted: 17 June 2025
© The Author(s) 2025
Abstract
With the rapid adoption of digital payments in India, credit card companies are focusing on customer loyalty and
planning rewards to incentivize spending, especially during peak periods like festivals. However, there is a gap
in developing a tailored system that optimizes sales and reward structures for these companies. The proposed
work addresses this gap by leveraging machine learning techniques to analyze and assess credit card spending
patterns and propose design targeted reward programs. Besides this, this study focuses on categories as luxury,
travel, groceries, EMIs payments, and others and employs ML methods, using K-Means clustering to segment
users based on card types (Silver, Gold, Platinum, and Signature). Feature engineering is another key in improving
the model’s understanding and providing insights, particularly in calculating reward points based on various
attributes and spending behavior. The usage of original and synthetic datasets ensured scalability and adaptability
across different financial domains as well. The results highlight the potential and need of ML to optimize reward
allocation and provide real-time predictions, enabling financial institutions to tailor their offerings for increased
customer engagement and retention. By aligning rewards with high-margin spending categories and leveraging
adaptive frameworks, this study offers strategies to enhance credit card reward programs. The proposed ML model
achieved an R2 value of 0.99, demonstrating superior accuracy in optimizing reward point distribution.
Keywords Credit card rewards · Spending analysis · Reward optimization
1 Introduction
India has witnessed an exponential leap in usage of credit card, driven by rapid digital adoption, urbanization, and
increasing incomes in all categories of earners. As of 2024, over 83 million active credit cards are in circulation,
supported by the government’s Digital India initiative, the major stakeholders being the expanding middle class,
and the increasing preference for digital payments. In this expanding landscape of digital transactions, financial
institutions face increasing pressure to attract and hold customers by adopting innovative strategies, especially
through reward programs. These reward systems, offering cashback, discounts, air miles, and points in both
indispensable categories like groceries and EMIs and selected categories like luxury goods and travel, play a
major role in promoting spending, customer acquisition, and retention by aligning benefits with consumer interests
and spending patterns [1, 2].
Despite the success of traditional reward models, credit card companies often fail to meet the diverse
expectations of modern tech-savvy credit card users. Today’s cardholders vary widely, from essential buyers who
focus primarily on necessities such as groceries and bills, to affluent and luxurious spenders seeking premium
Int J Comput Intell Syst (2025) 18:165 https://doi.org/10.1007/s44196-025-00899-0
Vol.:(0123456789)

165 Page 2 of 21 https://doi.org/10.1007/s44196-025-00899-0
experiences in luxury goods and travel. The generalized, one-size-fits-all nature of traditional reward structures
does not effectively cater to these varied preferences [3]. This lack of adaptability as per the needs of customers
results in missed opportunities to increase customer engagement and loyalty, particularly among high-valued
customers. The core problem faced by credit card companies in India is differentiating their offerings in a
competitive market to retain high-value customers. Current reward programs often fail to incentivize spending
among affluent and frequent spenders due to their generic structures, which fail to distinguish between nominal
and high-value spenders [4, 5].
The importance of customizing reward systems becomes especially evident during peak sales seasons like
Diwali, Christmas, and New Year, when consumer spending spikes. During these times, many consumers actively
seek cards that offer better benefits for large purchases. This presents an opportunity for financial institutions to
introduce customized incentives that align with changing consumer preferences [6, 7]. Advancements in data
analytics and machine learning now offer credit card companies the ability to analyze transaction data, segment
users, and create adaptive reward structures. These technologies can be harnessed to target high-value customers
with personalized incentives, ultimately driving greater customer satisfaction and retention [8]. Moreover, by
shifting the focus of reward systems toward discretionary categories like luxury goods and travel, institutions can
enhance customer loyalty and profitability [9].
The objective of this research is to leverage ML techniques to analyze and predict the spending habits of credit
card users in India, with an intention on optimizing reward programs to enhance customer engagement and loyalty
[10]. This study aims to enable financial institutions to personalize reward systems by identifying key spending
categories such as luxury goods, travel, groceries, and EMIs. The specific goals of the research are as follows:
1. Segment Spending Behavior: implement K-Means clustering to categorize users based on their spending
habits, identifying profiles as luxury spenders, frequent travelers, and nominal spenders and rewarding
accordingly.
2. Optimize Reward Programs: develop reward systems that allocate higher points for luxury and travel-related
spending, motivating users to boost discretionary expenditures with a justified approach for rewards.
3. Prevent Overfitting and Ensure Generalization: employ synthetic data and regularization techniques
to counteract overfitting, allowing models to perform accurately on new, unseen data while maintaining
scalability.
4. Enhance Accuracy with Feature Engineering: engineer features such as reward points per transaction and
spending frequency to improve model precision and deepen insights into user behavior.
This research seeks to provide financial institutions especially credit card companies with a data-driven
framework for developing personalized reward programs that promote higher discretionary spending, improve
customer retention, and increase overall customer satisfaction in the competitive Indian credit card market.
2 Related Work
The application of ML techniques for analyzing credit card spending behaviors has gained prominence due to
the availability of vast transactional datasets. Previous studies have explored various aspects, including user
segmentation, behavior prediction, and reward program optimization. Cheema and Van der Stede [11] examined
how reward programs tailored to user preferences, particularly in high-spending categories like luxury goods
and travel, can enhance customer engagement and usage frequency. However, their approach lacked dynamic
adaptation to shifts in spending patterns. Li, Ngai, and Hu [12, 13] reviewed ML applications in financial
services, focusing on K-Means clustering, Random Forest, and Gradient Boosting for consumer prediction and
segmentation. While effective, these methods were static and struggled to adjust to real-time changes in user
behavior. Predictive models for spending patterns have also been extensively studied. Gan et al. [14] employed
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 3 of 21 165
ensemble models like XGBoost and LightGBM to predict consumer behavior in high-value categories, improving
reward allocation and incentive design. Despite their effectiveness, these models were prone to overfitting,
particularly when handling high-dimensional data. Sadat Akash’s “Credit Card Transaction Dataset” [15] has been
widely used to train predictive models. However, most studies utilizing this dataset focused on general prediction
tasks rather than aligning predictive models with targeted reward structures for high-value spending categories.
Broader ML applications in financial behavior prediction have also been explored. Sun and Vasarhelyi [16]
and Sayjadah et al. [17] applied ML models to predict credit card defaults, demonstrating the potential of neural
networks in financial forecasting. Although these models exhibited high accuracy for risk assessment, they did
not focus on consumer spending behaviors in reward-eligible categories. Teng and Lee [18] used decision trees
and Support Vector Machines (SVMs) to predict default risks and spending patterns, yet these methods struggled
to generalize spending prediction in high-value segments due to limited dataset specificity. Despite extensive
research on credit card user segmentation and behavior prediction, several limitations remain. Many existing
models lack adaptability to evolving user preferences, resulting in static reward structures that fail to align with
current spending trends. Ensemble models like XGBoost and LightGBM, while promising, often suffer from
overfitting when applied to high-dimensional datasets. Additionally, most studies overlook discretionary spend-
ing categories such as luxury and travel, which are crucial for customer loyalty programs. Moreover, existing
methods tend to be static and fail to accommodate real-time shifts in user behavior, limiting their effectiveness.
Table 1 provides a comparative analysis of previous research, identifies existing gaps, and highlights how the
proposed work addresses these limitations using ML-driven reward personalization and real-time adaptability. To
address these limitations, this research introduces a machine learning model that leverages clustering techniques,
such as K-Means, for detailed user segmentation based on spending in discretionary categories like luxury and
travel. Unlike prior studies, this work specifically focuses on predicting high-value spending to optimize reward
distribution, ensuring enhanced personalization for these segments. Furthermore, real-time adaptability is intro-
duced to adjust rewards based on evolving user behaviors, providing credit card issuers with a scalable solution
for dynamic reward allocation. By overcoming the limitations of previous approaches, this research offers a
refined and adaptable framework for optimizing credit card rewards, ultimately improving customer satisfaction
and loyalty in the Indian market [19, 20].
2.1 Discussion of Traditional Reward Programs and Their Limitations
Traditional credit card reward programs have long relied on mechanisms such as points, cashback, and discounts
to incentivize spending. While effective in fostering customer loyalty, these programs face significant limitations
as consumer preferences evolve and data analytics capabilities advance. A key limitation is the lack of personali-
zation. Currently available rewards systems provide fixed incentives irrespective of individual spending habits,
leading to a disconnect between consumer preferences and program benefits. For example, whether a customer
spends primarily on groceries or luxury goods, the rewards remain the same, failing to foster deeper engagement
of influential customers. Similarly, cashback programs appeal to a broad audience but do not account for varying
spending patterns. Luxury shoppers and everyday spenders may receive identical cashback rates, even though
high-value customers have greater profitability potential. This lack of differentiation can cause affluent users to
switch to competitors credit card companies which offer personalized rewards.
Tiered reward structures attempt to introduce differentiation by providing better reward points for specific
categories like travel and dining. However, these programs are typically static and do not align with individual
spending behaviors. Furthermore, they target broad consumer groups, often overlooking niche markets that could
benefit from more granular incentives. Seasonal promotions also present limitations; while increased points during
holidays may drive short-term spending, they fail to sustain engagement throughout the year and do not cater
to personalized needs. Traditional reward programs also rely on rigid, rule-based systems that do not leverage
real-time data to adjust rewards based on evolving consumer behavior. Unlike modern, data-driven approaches,
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0
  165   Page 4 of 21
 remusnoc gnivlove htiw tnemngila gnirusne ,smarg
|                                                                                                 |                                                  |                                                   |                                                                                                    |  ot levart dna yruxul sa hcus seirogetac ni gnidneps                                            |  sevitnecni gnitcerid yb noitacolla drawer sezimitpO |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
|                                                                                                 |  yranoitercsid no desab sresu tnemges ot setadpu |  drawer ezimitpo ot levart dna yruxul ni gnidneps |                                                                                                    |                                                                                                 |                                                      |
|  taht sdrawer dezilanosrep nevird-LM stnemelpmI  gnidneps emit-laer no desab yllacimanyd tsujda |                                                  | -hgih ni gnittfirevo ecuder dna ssentsubor ledom  |  gnidneps yranoitercsid gnitciderp ot sucof stfihS  resu ecnahne dna serutcurts drawer ezimitpo ot |                                                                                                 |  elihw seirogetac gnidneps nigram-hgih drawot        |
|                                                                                                 |                                                  |  ecnahne ot seuqinhcet noitaziraluger secudortnI  |                                                                                                    |  eulav-hgih tegrat taht sledom LM setaroprocnI -orp drawer ot ytilibatpada emit-laer secudortnI |                                                      |
 emit-laer htiw gniretsulc snaeM-K segareveL
 yranoitercsid htiw sledom evitciderp sngilA
saera nigram-wol ni stsoc gniziminim
noitacolla drawer enfier
| krow siht ni desserddA |     | stesatad lanoisnemid |     |     |     |
| ---------------------- | --- | -------------------- | --- | --- | --- |
tnemegagne
noitubirtsid
gnidneps
|                                                 | sdnert                                               |                                                                                                      |                                                    |                                                                                                 | stibah                                              |
| ----------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- |
|                                                 |  ,snrettap gnidneps ni stfihs ot ytilibatpada dekcaL |  snrettap gnidneps ezilareneg ot delggurts sdohteM snoitatimil tesatad ot eud stnemges eulav-hgih ni | -dneps remusnoc naht rehtar ksir tiderc no desucoF | -dneps emit-laer no desab setadpu cimanyd dekcaL                                                |                                                     |
|                                                 |                                                      |                                                                                                      |                                                    |  sledom evitciderp ngila ton did skrow gnitsixE  eulav-hgih rof serutcurts drawer detegrat htiw |  tnereffid ssorca sdrawer fo noitacolla tneicffienI |
|  drawer citats no deiler sledom drawer gnitsixE |                                                      |  ot tpada ton did dna citats erew sledom esehT                                                       |                                                    |                                                                                                 |                                                     |
seirogetac elbigile-drawer ni sroivaheb gni
serutcurts drawer citats ot gnidael
roivaheb resu gnivlove
| seigetarts noitacolla |     |     |     |     | seirogetac gnidneps |
| --------------------- | --- | --- | --- | --- | ------------------- |
defiitnedI spaG
roivaheb gni
gnidneps
snoitubirtnoc ruo dna ,spag defiitnedi ,hcraeser suoiverp fo nosirapmoC
|                                                |  modnaR ,snaeM-K desu ]31 ,21[ uH dna ,iagN ,iL |                                                                                          | stluafed drac tiderc tciderp ot sledom LM deilppa |                                                 |  daorb dna kcabhsac dexfi desu sledom lanoitidarT |
| ---------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------- |
|  drawer derolpxe ]11[ edetS red naV dna ameehC |                                                 |  ni roivaheb remusnoc gnitciderp rof MBGthgiL                                            |                                                   | sMVS dna seert noisiced desu ]81[ eeL dna gneT  |                                                   |
|  seirogetac gnidneps-hgih ot deroliat smargorp |                                                 |  dna tsooBGX deyolpme ]41[ nehC & ,uX ,naG  lareneg no desucof ]51[ ”tesataD noitcasnarT |  ]71[ .la te hadajyaS dna ]61[ iylehrasaV dna nuS |                                                 |                                                   |
|                                                |  remusnoc rof gnitsooB tneidarG dna ,tseroF     |                                                                                          |                                                   |  drawer citats no deiler sledom drawer gnitsixE |                                                   |
 draC tiderC“ s’hsakA tadaS gnizilitu seidutS
|     | levart dna yruxul ekil | seirogetac eulav-hgih |     |     |     |
| --- | ---------------------- | --------------------- | --- | --- | --- |
seigetarts noitacolla
hcraeser suoiverP
noitatnemges
snoitciderp
sevitnecni
noitatnemges rof seuqinhcet LM
noitciderP roivaheB laicnaniF
noitciderP nrettaP gnidnepS
sdraweR cfiicepS-yrogetaC
| noitazilanosrep draweR |     |     |     | ytilibatpadA emiT-laeR |     |
| ---------------------- | --- | --- | --- | ---------------------- | --- |
noitazilitU tesataD
ycneicffiE tsoC
 1 elbaT
tcepsA
  Int J Comput Intell Syst          (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 5 of 21 165
they lack the ability to dynamically tailor incentives based on spending patterns and life events. Additionally, the
one-size-fits-all approach diminishes the potential for high-value customers to feel incentivized. Without targeted
rewards, companies miss opportunities to retain and maximize the spending of their most profitable users.
2.2 Benefits of Personalized Rewards Based on Spending Habits
The implementation of ML and data analytics in personalized rewards systems provides numerous benefits over
traditional models. By aligning incentives with individual preferences, these systems enhance customer loyalty, as
tailored rewards create stronger emotional connections with users. When customers receive incentives relevant to
their spending behaviors such as travel points for frequent travelers or luxury bonuses for high-end shoppers, they
are more likely to remain engaged with their credit cards, leading to higher retention rates and increased spending.
Personalized rewards also optimize program efficiency by directing incentives toward profitable categories, such
as travel and luxury, while reducing rewards for low-margin purchases like groceries or usage for EMI payments.
This targeted approach allows credit card companies to manage costs more effectively while maximizing customer
satisfaction. Additionally, real-time insights enable companies to create dynamic, behavior-driven promotions,
such as double points during specific periods, prompting users to spend more in key categories. Personalized
offers further create a sense of exclusivity, fostering higher engagement with the credit card’s app or services.
By encouraging spending in targeted categories, personalized rewards help prioritize high-value transac-
tions. For example, users may shift more travel or luxury purchases to a card offering superior rewards in those
categories, increasing transaction volumes and overall spend. Improved customer satisfaction and retention are
also achieved, as users who feel valued through relevant incentives experience greater contentment, reducing the
likelihood of churn. Retaining satisfied customers is significantly more cost effective than acquiring new ones,
reinforcing long-term loyalty.
Furthermore, spending data enables tailored marketing efforts by providing relevant offers based on individual
behavior. For instance, a customer who frequently dines at restaurants could receive targeted dining promotions,
improving conversion rates and enhancing the overall customer experience. Additionally, machine learning models
facilitate better customer insights and predictive modeling by analyzing spending patterns and forecasting future
behaviors. This allows issuers to proactively adjust rewards, such as increasing travel points before peak holiday
seasons for users likely to spend more on trips. Ultimately, personalized reward systems provide a competitive
advantage in the financial industry. In a highly competitive market, offering tailored incentives differentiates
card issuers and attracts customers seeking meaningful benefits. Companies that implement such data-driven
approaches position themselves as innovators, strengthening their brand image and market appeal.
3 Proposed Methodology
Steps involved in proposed methodology for credit card users reward calculation is outlined in Fig. 1. Detailed
description of steps is covered in subsequent sections. The process of credit score calculation starts with gathering
data from open-source repository and its exploration for usage in reward calculation.
3.1 Analysis of Dataset
The original dataset, referred to as the Analyzing Credit Card Spending Habits in India, had several limitations
that hindered its utility for advanced analysis and model development [21]. The key columns and their descrip-
tions are outlined in Table 2.
The provided figures showcase different visualizations of the dataset. Figure 2 helps in identifying patterns
associated with original dataset and reflects the data as they are explored on various parameters including in
central tendency, skewness, and variability. Figure 2a, reflecting a plot of transaction amounts, is particularly
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0
  165   Page 6 of 21
Fig. 1   Methodology for calculation
of credit score
Table 2   Description
|     | Column | Description |
| --- | ------ | ----------- |
of attributes in original
| dataset | Index | Sequential Identifier for each transaction    |
| ------- | ----- | --------------------------------------------- |
|         | City  | The location where the transaction took place |
|         | Date  | The transaction date (with outdated values,   |
primarily from 2014 to 2015)
|     | Card Type | The type of card used for the transaction |
| --- | --------- | ----------------------------------------- |
|     | Exp Type  | Type of Expense                           |
|     | Gender    | Gender of the cardholder                  |
|     | Amount    | Monetary value of the transaction         |
useful for detecting outliers and patterns followed by users, as it visually demonstrates the spread of the data.
Figure 2b shows the distribution of original data based on gender of holder of the card, a look clearly reflects that
female are using card more than male spenders. Figure 2c shows the distribution of card types helps interpret the
  Int J Comput Intell Syst          (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 7 of 21 165
(a) Distribution of Transaction Amounts (b) Distribution of Gender
(c) Distribution of Card type (d) Distribution of Expense type
Fig. 2 Exploratory data analysis of original dataset
variety and frequency of credit card usage, providing insights into behavior of customers. Figure 2d representing
the plot of expenditure types shows how transaction amounts are allocated across different categories of expenses,
offering an enhanced understanding of consumer spending behavior.
After visualizing the dataset available in public repository, limitations are found that deter more detailed
analysis for fair calculation of reward points. Firstly, the Index attribute lacks user-specific identifiers, hindering
effective segmentation of the data and making it difficult to analyze user-level behaviors or generate personalized
insights for analysis. Also, the Date field contains many missing or outdated values, especially from 2014 to 2015
which is quite obsolete as well; this makes temporal analysis challenging and prevents tracking of trends over
time. Amounts spend monthly in the field is significant, it lacks contextual details, and this added information
would enrich the analysis and offer deeper insights into spending behaviors of customers. This indicates a need
for generating a synthetic dataset to better capture and represent the real transaction distribution. These limita-
tions underscore the need for further data enhancement and preprocessing to improve the quality of data analysis.
3.2 Generation and Analysis of Synthetically Generated Dataset
To address the limitations of the original dataset and to have a fair distribution of reward points, a new dataset is
generated, which includes more relevant and detailed columns. To generate synthetic credit card data, the Faker
library in Python was used, defining column names, ranges, and relationships between values. It was ensured that
Int J Comput Intell Syst (2025) 18:165

165 Page 8 of 21 https://doi.org/10.1007/s44196-025-00899-0
certain attributes like credit score and attrition risk were correlated. To determine the attribute values, multiple
GitHub repositories were explored and datasets related to credit card transactions. Later, a list of potential
attributes were compiled and fed into an LLM and asked it to suggest the most potent ones for our project. The
suggestions were reviewed to ensure they made sense and used a trial-and-error approach with feature engineering
to identify the most significant attributes. We used a correlation matrix to determine the attributes with the highest
positive correlation and dropped the ones that were not significant.
Explanation of Key Steps:
• Synthetic Data Generation: The generate_synthetic_data() function creates synthetic records for credit card
users, incorporating random values for attributes such as credit_score, monthly_spend, and attrition_risk.
• Feature Engineering: A correlation matrix is computed to identify and select the most relevant attributes. The
dataset is filtered to include only the most important features.
• Reward Points Calculation: A custom function calculate_reward_points() is defined to calculate reward points
based on monthly_spend.
This enhanced dataset allows for a more comprehensive analysis of customer behavior and the development
of personalized reward strategies. Table 3 outlines the features included in the new dataset.
The inclusion of added attributes significantly improves the dataset’s ability to support personalized analysis
and predictions for credit points. The User ID helps individual-level tracking and segmentation, allowing for
more tailored insights into customer behavior. The Card Promotion Date provides valuable information on
customer progression to higher card levels, which enhances the ability to personalize reward programs based
on a customer’s status. The Expense Type categorizes spending into luxury, travel, and nominal types, enabling
a more refined analysis of customer spending patterns and preferences. The inclusion of the Income Category
allows for a better understanding of the customer’s spending power, which is critical for customizing reward
offers. Furthermore, the Number of Cards held by a customer offers insight into their overall spending behavior,
providing another dimension for creating targeted rewards. The addition of Number of active Loans of a card
holder helps contextualize the customer’s financial behavior and spending limitations, and this attribute finds
usage in predicting a customer future purchasing behavior. Demographic information such as Customer Age and
the Months Spent with Bank allows for customer segmentation depending on life stage, offering opportunities
for more effective marketing strategies. The Risk of Attrition flag is a vital indicator for identifying at-risk
Table 3 Description of
Column Description
attributes in synthetic
dataset User ID Unique Identifier for each customer, enabling user level tracking
City The location where the customer uses the card
Date of Transaction The transaction date, indicating when the card is used
Card Type Type of card used
Card Promotion Date Date when the customer is promoted to a new card level
Expense Type Categorized type of expense
Amount Monetary value of the transaction
Income Category Salary range of the customer
Number of Cards Number of credit cards held by the customer
Number of Loans Number of loans the customer has taken
Customer Age Age of the customer
Months Spent with Bank Duration of the customer’s relationship with the bank
Risk of Attrition Flag indicating whether the customer is likely to leave the bank
# Transactions per month) The average number of transactions made per month
Month of Transaction The month of the transaction
Monthly Spending (on average) Total amount spent by the customer in the given month
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 9 of 21 165
customers, which can guide customer retention efforts. Lastly, attributes like Number of Transactions (per month)
and Monthly Spending (average) provide information about spending frequency and overall expenditure, helping
more precisely calculate reward points and user’s eligibility. These additions make the dataset much more suitable
and customized for ML models, allowing for better customer profiling and more personalized reward structures
[22, 23].
Figure 3 presents an exploratory data analysis of the synthetic dataset, with each subplot providing insights
into different features of the dataset generated for reward points calculations. Figure 3a illustrates the distribution
of transaction amounts, showcasing how the amounts are spread across the card types in dataset.
Figure 3b highlights the monthly spending trends across 15 months. It can be inferred that during festive sea-
sons as Diwali, Christmas, and Holi, the spending by credit card users shows an increasing trend substantiating
the claim made that for customer retention credits need to be given for increased spending during festive seasons.
Fig. 3 Exploratory data
analysis of synthetic dataset
(a) Box Plot of Spending Amount with Card Type
(b) Monthly spending Trends Generated by synthetic Dataset
Int J Comput Intell Syst (2025) 18:165

165 Page 10 of 21 https://doi.org/10.1007/s44196-025-00899-0
3.3 Data Cleaning and Transformation
Before preparing the credit card transaction dataset for analysis and model training the data need to be ensured
for readiness. The steps performed to clean and transform the dataset include the following:
1. Date Conversion: The Date field in the dataset was originally in string format. To facilitate easier date manipu-
lation and enable temporal analysis, this field was converted into a datetime format. This transformation allows
for the extraction of specific components such as month, year, and day, which are essential for time-based
analysis and trends in customer behavior.
2. Encoding Categorical Variables: Variables which are of specific category such as Gender, Card Type, and
Expense Type are encoded using One-Hot Encoding, transforming these variables into numerical format [24].
This is done to ensure their efficient usage and processing by ML models that necessitates numerical input.
3.4 Unsupervised Learning: K‑Means Clustering
In the next stage, clustering techniques to segment users based on their credit card type are employed. The cus-
tomized synthetic dataset consists of four distinct card types: Platinum, Gold, Silver, and Signature. Each of these
cards offers different privileges, bonuses, and benefits that affect credit card users’ usage patterns and financial
engagements. The clustering process and results obtained are interpreted. Besides K-means, Density-Based Spatial
Clustering of Applications with Noise (DBSCAN), and Gaussian Mixture Models (GMM) [25] clustering are
employed and Clustering Evaluation Matrices Silhouette Scores and Davies-Bouldin Index (DBI) are evaluated for
the clusters made on the basis of card types for synthetic dataset. Since a high silhouette score confirms meaning-
ful segmentation, it reinforces that Card Type aligns well with spending behavior and is a strong clustering factor.
A look on Fig. 4 reveals that for K-Means and DBSCAN clustering techniques both performance indices of
clustering models, viz., silhouette score and DB index, are appreciable. Either of these can be used to validate
the proposed hypothesis that clustering based on card types will better segment users. Silhouettes score which
range from -1 to + 1, and values near 1 are considered better as this indicates how well each of data points is
clustered. Moreover, DB index, which is a validation index used by researchers in order to assess the optimal
number of clusters to use, should be less than 1. A lower value of DB index suggests compactness and minimal
overlap between clusters.
• Feature Selection for Clustering Card Types: Several features were chosen for clustering, that efficiently capture
the spending behavior of credit card users:
– Monthly Spend: This attribute considers the total amount spent per month on the card, thus helping dif-
ferentiate card types based on spending patterns.
– Transactions Per Month: Indicates the frequency of card usage, with higher values typically seen in Plati-
num and Signature cardholders.
– Credit Utilization: Expense Category: Credit utilization is a factor considered for rewarding customers
who have utilized the spending till their credit limit. Customers who have spent much to their credit limit
will be rewarded more than who have spent less.
Fig. 4 Performance scores of clustering models
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 11 of 21 165
– Year and Month of Transaction: Helps in recognizing temporal patterns in spending through usage of cards.
Also to reward customers who have used card in festive seasons.
– K-Means Clustering Algorithm: The clustering is done using the K-Means algorithm as the selected model
Selecting the Number of Clusters (K): The number of clusters for assessment is set to 4, based on the dif-
ferent card types. The value of K can be changed based on types of cards issued by credit card companies.
• Practical Use Cases for Proposed Clusters: The insights received from clustering are applicable in multiple
ways [26]:
– Targeted Marketing: Customized marketing and card promotional strategies to each cluster, offering Plati-
num card holders luxury goods promotions, and silver users shopping deals or cashback offers.
– Customized Reward Programs: Design reward by credit points programs aligned with the spending behavior
of each category of users to enhance satisfaction by fair distribution.
– Customer Retention: Develop strategies to retain customers, as providing personalized bonuses to high-
spenders and cardholders.
3.5 Clustering Analysis
The users are segmented based on their spending behavior and card type, using clustering techniques to group
them into four clusters. These clusters represent different user types based on their spending categories, which
help in understanding the underlying patterns in card usage [27, 28]. The clusters and their characteristics are as
follows:
• Interpreting the Clusters: The resulting four based on card types of clusters are analyzed as follows:
– Cluster 1 (Platinum Cardholders): Credit card holders in this cluster show high spending, frequent usage,
and a preference for luxury and travel expenses.
– Cluster 2 (Gold Cardholders): Users in this group demonstrate moderate spending and balanced transac-
tion frequency, mixing luxury and basic purchases.
– Cluster 3 (Silver Cardholders): This group focuses on lower spending, mainly on essential items like
groceries, and has lower income.
– Cluster 4 (Signature Cardholders): Users here focus on routine expenses with minimal variability in spend-
ing
Table 4 Base reward points
Card type Base reward rate
Platinum 5 points
Signature 4 points
Gold 3 points
Silver 2 points
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0
  165   Page 12 of 21
Table 5   Base multiplier for
|     | Card type |     |     |     | Base multi- |
| --- | --------- | --- | --- | --- | ----------- |
card types (RCT)
plier (RCT)
|     | Platinum  |     |     |     | 2.0 |
| --- | --------- | --- | --- | --- | --- |
|     | Signature |     |     |     | 1.5 |
|     | Gold      |     |     |     | 1.0 |
|     | Silver    |     |     |     | 0.5 |
Table 6   Expense type
|                            | Expense type    |     |     |     | Bonus   |
| -------------------------- | --------------- | --- | --- | --- | ------- |
| bonus (ET) and associated  |                 |     |     |     | points  |
| reward points              |                 |     |     |     | (ET)    |
|                            | Travel/Dining   |     |     |     |  + 3.0  |
|                            | Luxury          |     |     |     |  + 2.0  |
|                            | Entertainment   |     |     |     |  + 1.0  |
|                            | Groceries/Bills |     |     |     | 0.5     |
|                            | Other Expenses  |     |     |     | 0.0     |
3.6   Reward Points Calculation
The reward points calculation method is discussed for both the original and synthetic datasets. The original dataset
lacks detailed transaction-level data, so the calculation is based on the card type alone. On the other hand, the
synthetic dataset allows for a more granular calculation considering multiple factors.
3.6.1   Original Dataset
In the original dataset, since transaction-level data are unavailable, reward points are calculated based solely on
the card type. The base reward points for each card type are shown in Table 4.
∗ PointsScored(BasedonCardType)
AmountSpentMonthly
| RewardPoints(Olddataset) |     | =   |     |     | .   |
| ------------------------ | --- | --- | --- | --- | --- |
500
3.6.2   Synthetic Dataset
For the synthetic dataset, reward points are calculated using a more detailed approach that considers several fac-
tors. These include the card type, promotion status, expense type, income category, number of cards, and attrition
risk. The calculation is as follows:
∗
ScoredPoints AmountSpent
|     | RewardPoints(SyntheticDataset) |     | =   | ,   |     |
| --- | ------------------------------ | --- | --- | --- | --- |
500
|     | ScoredPoints | = [RCT +CPD+ET | +IC+NoC+AR], |     |     |
| --- | ------------ | -------------- | ------------ | --- | --- |
where. RCT = Base multiplier based on Card Type (refer to Table 5), CPD = Card Promotion Date bonus,
ET = Expense Type bonus (refer to Table 6), IC = Income Category bonus, NoC = Penalty for additional cards,
AR = Attrition Risk bonus.
  Int J Comput Intell Syst          (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 13 of 21 165
• Base Multiplier for Card Types (RCT): The base multiplier for reward points is determined based on the type
of card owned by a customer. Higher multipliers are assigned to premium card types, as detailed in Table 5.
• Income Category Bonus (IC): Customers in the high-income category receive a bonus of 1 or for middle
income a reward point of 0.5 is suggested.
• Number of Cards (NoC): Customers with more cards receive a slight penalty to encourage consolidation.
For every additional card beyond the first, a multiplier of -0.5 is done.
• Attrition Risk (AR): Customers with a higher attrition risk receive an additional reward of + 1.0 points to
incentivize loyalty.
• Expense Type Bonus (ET): Customers earn higher rewards for discretionary categories like Travel and
Dining. The bonus rewards for different expense types are detailed in Table 6.
To summarize, the total reward points are computed by summing the values from all six factors mentioned
above. These reward points are then scaled by the monthly amount spent to determine the final reward points.
Thus, K-Means clustering was used for segmenting users based on their spending patterns, allowing one to
group users by likely card types. In the original dataset, reward points were based on card type, while in the
synthetic dataset, the calculation was more intricate, incorporating multiple factors such as expense type, card
promotion, and income category.
Table 6 shows expense types, bonuses, and associated reward points. The logic here is that customers earn
higher rewards for categories like travel and dining, and lower rewards for groceries, bills, and other expenses.
The scaling factor used is arbitrary and can be adjusted. The goal is to encourage spending on discretionary
expenses like travel, luxury shopping, and dining by providing higher reward points, while discouraging
spending on necessities like groceries and bills.
For example, in Table 6, travel and dining have a bonus factor of + 2.0, luxury has + 1.5, entertainment
has + 1.0, and groceries and bills have + 0.5.
– If the scaling factor is changed, all other values should be scaled similarly.
– This allocation of reward points is up to the discretion of the credit card company.
Our research aims to demonstrate the effectiveness of reward point calculation, and banks can use and
modify our approach according to their needs. The specific values are suggestive and not meant to be taken
as a standard. Banks can adjust the factors to allocate reward points differently based on spending categories.
The multipliers + 2.0, + 1.5, + 1.0, and + 0.5 are chosen for ease of calculation and because they are rela-
tively close to each other. Since banks and credit card companies do not publicly disclose their actual multipli-
ers for calculating reward points, these values are subjective and intended to provide a reasonable approxima-
tion. They are not fixed and can be adjusted as needed by the credit card company.
4 Results and Discussions
In this section, we present the results from the clustering analysis and reward points calculation, followed by
a detailed discussion of the insights and how they align with the expected patterns.
Int J Comput Intell Syst (2025) 18:165

165 Page 14 of 21 https://doi.org/10.1007/s44196-025-00899-0
Fig. 5 Cluster-based analysis based on card type
Fig. 6 Distribution of reward points
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 15 of 21 165
4.1 Cluster Analysis Results
Validating Card Type as the Best Clustering Approach has been done to segregate user. The goal was to
determine whether Card Type (Platinum, Gold, Silver, Signature) is the most effective way to segment users.
Through multiple evaluations, strong evidence supporting this hypothesis is obtained. By clustering users and
analyzing the distribution of card types within each group, a clear separation based on card type is observed.
This helps in understanding how users behave according to their spending patterns. Figure 5 shows 2D
visualization of the cluster obtained by K-means clustering technique. Visualization in 3D clearly segregates
the 4 clusters made based on card type held by customers. Clear separation of Card Types within clusters
proves its natural segmentation power.
K-Means achieved a score of 0.42, outperforming other clustering techniques (DBSCAN, Hierarchical, GMM).
The performance of clustering models used in this work is compared to Silhouette Scores and Davies-Bouldin
Index (DBI) for the clusters made based on card types for synthetic datasets. High silhouette score confirms
meaningful segmentation [29], and it reinforces that Card Type aligns well with spending behavior and is a strong
clustering factor. Thus, the clustering analysis effectively differentiates user behaviors and spending patterns,
providing a clear framework to associate spending habits with card types.
4.2 Reward Points Distribution
Figure 6 presents the distribution of reward points for both the original and synthetic datasets.
Figure 6 illustrates the reward point distribution based on five columns present in the original dataset, as well
as in a synthetically generated dataset that incorporates additional features necessary for a systematic reward
point calculation [30, 31]. These five columns were also synthetically created since the original dataset lacks
certain essential features, as discussed earlier. The analysis in Fig. 6 indicates that, with only five features as in
Fig. 7 Cumulative distribution of reward points
Int J Comput Intell Syst (2025) 18:165

165 Page 16 of 21 https://doi.org/10.1007/s44196-025-00899-0
the original dataset, the reward points are restricted to a maximum value of 1000 in synthetic dataset due to the
absence of detailed information.
However, in the synthetic dataset, including the additional features outlined in Table 3, the reward point
distribution extends over a broader and more justified range, ranging from 0 to 3500. Figure 7 presents the
cumulative distribution of reward points. The figure clearly demonstrates that utilizing synthetic data with
additional significant features results in a more systematic and justified approach to rewarding credit card users.
This method considers multiple parameters rather than relying solely on the five features present in the original
dataset. Figure 7 underlines the distribution of reward points categorized by spending type, highlighting how
different spending patterns influence reward allocation.
4.3 Comparative Evaluation of Reward Point: Original vs. Synthetic Dataset
The use of a synthetic dataset for reward point calculation in credit card transactions offers several key benefits. It
effectively captures clear and explainable relationships between variables, ensuring transparency in data analysis.
Despite having less features, the synthetic dataset maintains strong predictive performance due to its thoughtful
and systematic design. The inclusion of additional features significantly increases model performance, leveraging
more significant data for calculation. Furthermore, the synthetic dataset is inherently superior, as its theoretical
framework translates into durable predictive capabilities, making it an asset for modeling and analysis of reward
points.
Case study: Cardholder XYZ's Reward Calculation Analysis
Cardholder Profile:
• Card Type: Signature (Original: 4 points/500, Synthetic: RCT = 1.5)
• Monthly Spending on Card: 50,000
• Card Promotion Date Bonus (CPD): + 2 (new card promotion)
• Expense Type Bonus (ET): + 3 (60% travel expenses)
• Income Category Bonus (IC): + 1 (high-income bracket)
• Number of Cards Penalty (NoC): − 1 (holds 3 cards)
• Attrition Risk Bonus (AR): + 0 (medium-risk customer)
• Original Dataset Calculation:
The original formula for calculating reward points is given by the following equation:
ScoredPoints ∗ AmountSpent
RewardPoints(SyntheticDataset) = .
500
For Cardholder XYZ, the calculation proceeds as follows:
• Card Type Multiplier for Signature: 4 points per 500 spent
• Reward Points Calculation:
4 ∗ 50000
RewardPoints(SyntheticDataset) = = 400points.
500
The original formula has several limitations. First, it solely considers the amount spent and the card type, pro-
viding a simplistic calculation that does not incorporate any personalization. This approach overlooks important
customer information, such as spending patterns, income levels, and specific behaviors like travel expenses or
promotional offers. Additionally, the formula fails to adjust for factors that could impact the reward calculation,
such as promotional bonuses or penalties related to customer behavior, like holding multiple cards. As a result,
it lacks the flexibility and adaptability required to accurately reflect individual customer profiles and behaviors.
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 17 of 21 165
2. Synthetic Dataset Calculation:
In contrast, the synthetic dataset approach introduces a more personalized and dynamic reward calculation
formula:
ScoredPoints = [RCT +CPD+ET +IC+NoC+AR],
ScoredPoints ∗ AmountSpent
RewardPoints(SyntheticDataset) = .
500
The steps for calculating the reward points in the synthetic dataset are as follows:
Step 1: Calculate Scored Points
• RCT (Signature Card) = 1.5
• CPD (Promotion Bonus) = + 2
• ET (Travel Expenses) = + 3
• IC (High Income) = + 1
• NoC (Penalty for Holding 3 Cards) = − 1
• AR (Attrition Risk) = + 0
ScoredPoints = [1.5+2+3+1+−1+0] = 6.5
Step 2: Calculate Reward Points
6.5 ∗ 50000
RewardPoints(SyntheticDataset) = = 650points.
500
The synthetic dataset formula provides several advantages over the original approach:
1. Personalization: The synthetic formula considers the cardholder’s individual characteristics, such as their
travel spending (+ 3 ET) and high income (+ 1 IC), which the original formula overlooks. This allows for
a more tailored and accurate calculation of reward points, reflecting XYZ’s specific spending behavior and
profile.
2. Flexibility: Unlike the original method, the synthetic formula can adjust for various factors such as promo-
tions (e.g., + 2 CPD for new cards) and penalties (e.g., − 1 NoC for holding multiple cards). This flexibility
ensures that the reward system can evolve with changing customer behavior.
3. Behavioral Incentives: The synthetic formula encourages desired behaviors, such as spending on travel, by
offering higher rewards for such expenses. Conversely, it penalizes behaviors that are less profitable for the
company, such as holding multiple cards. This creates a reward structure that aligns more closely with both
customer engagement and business goals.
4. Attrition Risk Mitigation: The formula incorporates an attrition risk factor (AR) to identify and potentially
retain customers at risk of leaving. In the case of XYZ, despite being classified as a medium-risk customer,
the formula’s ability to factor in such risks can be leveraged to develop targeted retention strategies.
Fig. 8 Comparison of reward points
Int J Comput Intell Syst (2025) 18:165

165 Page 18 of 21 https://doi.org/10.1007/s44196-025-00899-0
5. Higher Granularity: The synthetic formula provides a more nuanced calculation of rewards. For example,
while the original formula awards a flat 400 points for a $50,000 spend, the synthetic formula, accounting for
the cardholder’s profile, results in 650 points. This granularity helps ensure that the reward structure better
reflects customer behavior.
The clusters align with the expected card types, providing a clear differentiation between various user behaviors
based on their spending patterns. Additionally, the reward points calculation methods for both datasets reveal a well-
aligned approach to incentivizing customers based on their spending habits and engagement. The clustering analysis
and reward points calculations have resulted in providing significant insights into customer segmentation based on
their card type and spending patterns. These results can be used to further improve targeted marketing, strategies for
customer retention, and overall design of reward program where credits are distributed fairly.
4.4 Model Performance
Machine learning Models such as Linear Regression, XGBoost, and Random Forest are applied for predictions of
reward points in synthetic dataset. The results obtained from these models substantiate the claims that synthetic
dataset generated for reward point calculations offers a justified and varied distribution of reward points across discrete
category of users based on parameters selected for calculating score points. The ML models whose performance for
predictions outcomes others is selected for calculating score points. Figure 8 presents a comparative analysis of the
reward points obtained for credit card customers using a synthetically generated dataset. By incorporating additional
significant features for a more equitable distribution and calculation of reward points, the mean reward points have
increased to approximately 1000, highlighting a considerable improvement in the system's efficiency.
The model performance results demonstrate a highly impressive R2 value of 0.99 for both the Random Forest
and XGBoost models, indicating an almost perfect fit to their respective datasets. However, when comparing the
models based on performance metrics such as RMSE and MAE, the Random Forest model clearly outperforms
both Linear Regression and XGBoost. Specifically, the Random Forest model achieves the lowest RMSE and
MAE values, making it the most accurate and reliable model for predicting customer credit scores. This dem-
onstrates that, while all three models fit the data well, Random Forest excels in minimizing prediction errors,
making it the most suitable choice for this particular task.
5 Conclusion
The clustering analysis successfully segregated spending behaviors across different card types, thus aligning with
expected financial patterns. Usage of ML demonstrated strong performance in predicting user spending behaviors
across both for the original as well as synthetic datasets. Additionally, the credit point distribution highlighted the
benefits of including additional features, leading to a more systematic and justified reward calculation process.
The goal with this experiment is to showcase the efficiency of proposed formula for allocating reward points.
Due to the unavailability of real credit card transaction data and reward point calculation methods, synthetic
datasets have been used, and a formula has been developed accordingly. Machine learning models verify the
effectiveness of formula, achieving an R2 score of 0.99, which indicates a near-perfect formula. The formula is
flexible and can be modified to accommodate different variables and multipliers. The machine learning model can
be used to test the efficiency of the formula, providing valuable insights for credit card companies. Ultimately, our
goal is to demonstrate the effectiveness of our approach, which can be tailored to meet the specific needs of credit
card companies. In our research, we developed a formula to calculate reward points based on various attributes,
such as transaction type and credit card type. We then used a machine learning model to validate our formula by
calculating reward points independently and comparing the results. The model gave information about everyone’s
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 19 of 21 165
transactions and credit card type but not our specific formula or multipliers. The machine learning model's purpose
was to provide an independent evaluation of our formula's performance. By comparing the model's results to our
manually calculated reward points, we obtained an R2 score of 0.99, indicating a high degree of accuracy. This
suggests that our formula is robust and effective in calculating reward points.
For financial institutions and credit card companies, these findings emphasize the potential of machine learning
to optimize reward programs, improve customer loyalty, and improve retention rates by following a justified and
fair approach for reward points calculations. By leveraging transaction data, institutions can refine reward alloca-
tion, ensuring fair and personalized experience for customers. The insights gained also enable targeted marketing
strategies, increasing engagement, and maximizing the effectiveness of promotional campaigns.
Expanding the model with demographic attributes could refine customer segmentation, allowing for deeper
personalization. Beyond rewards, this framework can be extended to applications in fraud detection, credit risk
assessment, and adaptive credit limit recommendations, reinforcing its value in financial decision-making.
Acknowledgements The authors would like to thank the Symbiosis Institute of Technology, Symbiosis International (Deemed
University) for the support.
Author contributions All authors have contributed significantly to this research. Renuka Agrawal was responsible for con-
ceptualization, methodology, and provided supervision for writing—original draft. Aryan Khanna contributed to writing of
original draft, data curation, software implementation, and validation. Safa Hamdare handled formal analysis, investigation,
and writing—review and editing. All authors reviewed and approved the final manuscript.
Funding Open access funding provided by Symbiosis International (Deemed University). The authors received no financial
support for the research and authorship of this article. However, they may receive funding from the Symbiosis Institute of
Technology for publication.
Data availability No datasets were generated or analysed during the current study.
Declarations
Conflict of interest The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party material in this article are included in the article’s
Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
References
1. Wu, J., Zhao, X., Yuan, H., et al.: CDGAT: a graph attention network method for credit card defaulters’ prediction. Appl.
Intell. 53, 11538–11552 (2023). https://d oi.o rg/1 0.1 007/s 10489-0 22-0 3996-1
2. Ho, A.T., Morin, L., Paarsch, H.J., Huynh, K.P.: A flexible framework for intervention analysis applied to credit-card
usage during the coronavirus pandemic. Int. J. Forecast. 38(3), 1129–1157 (2022)
3. Krivorotov, G.: Machine learning-based profit modeling for credit card underwriting-implications for credit risk. J. Bank.
Finance 149, 106785 (2023)
4. Chang, V., Sivakulasingam, S., Wang, H., Wong, S.T., Ganatra, M.A., Luo, J.: Credit risk prediction using machine
learning and deep learning: a study on credit card customers. Risks 12(11), 174 (2024)
Int J Comput Intell Syst (2025) 18:165

165 Page 20 of 21 https://doi.org/10.1007/s44196-025-00899-0
5. Patel, P., Chauhan, S., Gupta, S., Gupta, T., Agrawal, R.: Mitigating class imbalance with ensemble SMOTEfied-GAN:
advancing detection strategies for automobile insurance fraud. Int. J. Fuzzy Logic Intell. Syst. 24(4), 333–342 (2024)
6. deHaan, E., Kim, J., Lourie, B., Zhu, C.: Buy now pay (pain?) later. In: Management Science (2024)
7. Bello, O.A.: Machine learning algorithms for credit risk assessment: an economic and financial analysis. Int. J. Manag.
10(1), 109–133 (2023)
8. Dal Colle, L.: Phygital: where and how we could intervene in the customer journey to provide a better customer
experience (2022)
9. Xu, D., Zhang, X., Hu, J., Chen, J.: A novel ensemble credit scoring model based on extreme learning machine and
generalized fuzzy soft sets. Math. Probl. Eng. 2020(1), 7504764 (2020)
10. Tripathi, D., Edla, D.R., Cheruku, R., Kuppili, V.: A novel hybrid credit scoring model based on ensemble feature
selection and multilayer ensemble classification. Comput. Intell. 35(2), 371–394 (2019)
11. Cheema, A., Van der Stede, W.: Consumer spending habits and reward programs: a case study. J. Financ. Stud. 45(3),
89–112 (2019)
12. Li, T., Ngai, E., Hu, Y.: Machine learning in financial services: applications, challenges, and future directions. J. Artif.
Intell. Res. 14(1), 78–102 (2021)
13. Ngai, E., Hu, Y., Wong, Y.H., Chen, J.: AI and financial services: a comprehensive review. J. Mach. Learn. Res. 8(5),
34–56 (2022)
14. Gan, Y., Xu, Z., Chen, L.: Predicting consumer behavior through machine learning: implications for credit card
companies. Int. J. Data Sci. 12(2), 45–67 (2021)
15. Ho, H., Tien, K.M.T., Wu, A., Singh, S.: A sequence analysis approach to segmenting credit card customers. J. Retail.
Consum. Serv. 59, 102391 (2021)
16. Sun, T., Vasarhelyi, M.A.: Predicting credit card delinquencies: an application of deep neural networks. Intell Syst.
Account. Financ. Manag. 25(4), 174–189 (2018)
17. Sayjadah, Y., Hashem, I. A. T., Alotaibi, F., Kasmiran, K. A.: Credit card default prediction using machine learning
techniques. In: 2018 Fourth International Conference on Advances in Computing, Communication & Automation
(ICACCA), IEEE, pp. 1–4 (2018)
18. Teng, H.W., Lee, M.: Estimation procedures of using five alternative machine learning methods for predicting credit
card default. Rev. Pac. Basin Financ. Mark. Policies 22(3), 1950021 (2019)
19. Mittal, S., Tyagi, S.: Performance Evaluation of Machine Learning Algorithms for Credit Card Fraud Detection, pp.
320–324. https://d oi.o rg/1 0.1 109/C ON-F LUENC E.2 019.8 77692 5 (2019)
20. Makki, S., Assaghir, Z., Taher, Y., Haque, R., Hacid, M., Zeineddine, H.: An experimental study with imbalanced
classification approaches for credit card fraud detection. IEEE Access 7, 93010–93022 (2019)
21. Altman, E.: Synthesizing credit card transactions. In Proceedings of the Second ACM International Conference on AI
in Finance (ICAIF ’21), Association for Computing Machinery, New York, NY, USA (2022)
22. Sadat, A.: Credit Card Spending Habits in India https://w ww.k aggle.c om/. www.k aggle.c om/d atase ts/t hedev astat or/
analyz ing-c redit-c ard-s pendi ng-h abits-i n-I ndia (2024). Accessed 24 Sept 2024
23. Gkikas, D., Theodoridis, P.: AI in Consumer behavior (2022). https://d oi.o rg/1 0.1 007/9 78-3-0 30-8 0571-5
24. Yahaya, S.N., Bakar, M.H.: The critical factors influencing consumer spending by using credit card. J. Technol. Manag.
Technopreneurship 8(1), 117–128 (2020)
25. Aniceto, M.C., Barboza, F., Kimura, H.: Machine learning predictivity applied to consumer creditworthiness. Futur Bus
J 6, 37 (2020)
26. Aluri, A., Price, B.S., McIntyre, N.H.: Using machine learning to cocreate value through dynamic customer engagement
in a brand loyalty program. J. Hosp. Tour. Res. 43(1), 78–100 (2019)
27. Nasir, M., Ezeife, C.I., Gidado, A.: Improving e-commerce product recommendation using semantic context and
sequential historical purchases. Soc. Netw. Anal. Min. 11(1), 82 (2021)
28. Rane, N.: Enhancing customer loyalty through Artificial Intelligence (AI), Internet of Things (IoT), and big data
technologies: improving customer satisfaction, engagement, relationship, and experience, October 13, (2023)
29. Kasaian, K., Murthi, B.P.S., Steffes, E.: Effects of teaser rates on new credit card customers’ spending and borrowing:
an empirical analysis. Int. J. Bank Market. 40(7), 1555–1574 (2022)
30. Zarkesh, B.: Exploring the impact of AI-driven pricing on customer loyalty and churn rates in the banking industry,
Master’s thesis, NTNU (2023)
31. Chen, Y., Lin, C., Zhao, Y., Xie, X., Zhang, M.: Modeling evolving user preferences for sequential recommendation
with credit card transactions. Preprint at arXiv arXiv:2 207.0 6225. https://a rxiv.o rg/a bs/2 207.0 6225 (2022)
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
affiliations.
Int J Comput Intell Syst (2025) 18:165

https://doi.org/10.1007/s44196-025-00899-0 Page 21 of 21 165
Authors and Affiliations
Renuka Agrawal1 · Aryan Khanna1 · Safa Hamdare2
*
Renuka Agrawal
renuka.agrawal@sitpune.edu.in
Aryan Khanna
aryan.khanna.btech2023@sitpune.edu.in
Safa Hamdare
safa.hamdare2021@my.ntu.ac.uk
1 Symbiosis International (Deemed University), Symbiosis Institute of Technology, Lavale Hill Base Campus, Pune,
Maharashtra 412115, India
2 Department of Computer Science, Nottingham Trent University, Clifton Lane, Nottingham,
Nottinghamshire NG11 8NS, UK
Int J Comput Intell Syst (2025) 18:165