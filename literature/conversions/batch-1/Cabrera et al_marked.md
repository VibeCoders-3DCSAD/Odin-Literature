---
conversion_metadata:
  converted_at: "2026-07-22T12:34:09Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Cabrera et al.pdf"
  source_pdf_sha256: "5b57b53fd75ff7246551d92b2b1742302303091540f58367c9735cd40d73a4ee"
  page_count: 18
  markdown_char_count: 267977
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

ARTICLE

https://doi.org/10.1057/s41599-025-05205-z

OPEN

Plastic to apparel: an analysis of sustainable
purchasing intention using a machine learning
ensemble
Carmella Andrea L. Cabrera1, Ardvin Kester S. Ong
Ma. Janice J. Gumasing4

1,2✉

, John Francis T. Diaz3, Maela Madel L. Cahigas1 &

;
,
:
)
(
0
9
8
7
6
5
4
3
2
1

The use of plastics has become a signiﬁcant component in maintaining the convenience and
suitability of modern lifestyles; however, a vast majority of the million tons of plastic man-
ufactured each year ends up in landﬁlls, contributing to plastic pollution. With this, the
fashion industry has capitalized to create recycled products. Despite the proliferation and
continued presence of recycled and upcycle products, there still is a signiﬁcant gap in the
sustainable purchasing behavior of consumers. This study aimed to identify, analyze, and
forecast the variables inﬂuencing consumers’ behavioral intention toward purchasing apparel
made from plastic. This paper established the Sustainability Theory of Planned Behavior
model to determine the purchase intentions of Filipino customers while purchasing clothing
made of recycled plastic. A total of 500 valid respondents were gathered to evaluate factors:
Perceived Economic Concern, Perceived Environmental Concern, Perceived Authority Sup-
port, Subjective Norm, Attitude, Perceived Behavioral Control, Customer Perceived Value,
and Behavioral Intention. To analyze the data, the study utilized machine learning methods,
such as Random Forest Classiﬁer (RFC) and Artiﬁcial Neural Network (ANN). Data pre-
processing using feature selection and correlation analysis was conducted to validate the
available data, performed data cleaning process, and data aggregation. Several
iterative
processes were employed to generate the optimum classiﬁcation model—obtaining a 92%
accuracy for RFC and 91% for ANN at 150 epochs under 30 hidden layer nodes. With low
error rates, the ﬁndings revealed that customer perceived value and perceived behavioral
control were the primary factors inﬂuencing consumers’ behavioral intentions toward pur-
chasing sustainable clothing. This study emphasized the consideration of these factors when
planning marketing strategies and initiatives to promote sustainable apparel.

1 School of Industrial Engineering and Engineering Management, Mapúa University, Manila, Philippines. 2 E.T. Yuchengo School of Business, Mapúa University, Makati,
Metro Manila, Philippines. 3 Department of Finance and Accounting, Asian Institute of Management, Makati, Metro Manila, Philippines. 4 Department of Industrial
and Systems Engineering Gokongwei College of Engineering, De La Salle University, Manila, Philippines.

email: aksong@mapua.edu.ph

✉

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

1

---

<!-- PAGE 2 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

IntroductionThe use of plastics has become a signiﬁcant component in

maintaining the convenience and suitability of modern
lifestyles. Considering its adaptability and remarkable cost-
performance ratio over the past several years, it has encompassed
everything from everyday life to commercial manufacturing
(Chang et al. 2019). Since then, majority of our daily activities
have incorporated the usage of plastics—ranging from various
food and beverage, cosmetics, toiletries, pharmaceuticals, and
other products. These industries require packaging for their ﬁn-
ished products in preparation of its safe and effective distribution
to customers (Evode et al. 2021).

Shams et al. (2021) discussed how the overwhelming bulk of
the annual one million tons of plastic production, including items
like water containers, bags, food containers, gloves, and cups, are
discarded after every single use. In addition, the study by Zhang
et al. (2022) stated that plastic pollution poses dangerous health
repercussions for both humans and marine species. In areas
where industrial wastes like plastics, rubber, and textiles are fre-
quently burned, fumes and the release of toxic substances into the
air, producing unpleasant odors from waste materials—con-
tributing signiﬁcantly to air pollution. Furthermore, a study
conducted by Awoyera and Adesina (2020) mentioned that out of
countless tons of plastic garbage, only 7% is recycled, approxi-
mately 8% is burned, and the remaining is landﬁlled. To which,
consequences of the increasing price and energy related to the
landﬁlling process led to water pollution caused by waste dis-
carded into bodies of water.

Tiseo (2023) posited how the Pasig River in the Philippines
releases over 63,000 metric tons of plastic debris into the ocean
every year (Fig. 1). The data in 2019 shows that the Pasig River
was estimated to have contributed 6.43 percent of all river-
derived ocean plastics, making the Philippines the world’s hea-
viest contributor of plastic-polluting rivers.

OECD (2022) reported that 22% of plastic waste was impro-
perly handled and not collected, 19% was burned, 49% ended up
in landﬁlls, and only 9% was recycled (Fig. 2). The growth in
emerging economies has caused the use of plastic to triple over
the previous 30 years.
times, plastics have been
responsible for 3.4% of global greenhouse gas emissions, with this
trend observed between 2000 and 2019, there was a double
increase in global plastics manufacturing to 460 million tons.

In recent

In the fast fashion industry, one of their objectives is to
manufacture and dispose of clothing rapidly; it pertains to the

speed at which the manufactured products are produced and then
discarded, aiming for instant consumption. This market became a
globalized industry, utilizing cheap labor and materials all around
the world (Zhang et al. 2021). This led to an increase in non-
recyclable waste in landﬁlls (Gomes de Oliveira et al. 2022).
Different studies (Niinimäki et al. 2020; Brewer 2019) explained
that fast fashion is now the industry with the second-highest
pollutant emissions at 10%. It was explained that large amounts
of raw materials are needed for manufacturing fashion, which
produces a substantial amount of waste that leaves a considerable
carbon footprint and produces a signiﬁcant level of pollution
(Grazzini et al. 2021).

Nowadays, clothing companies are widely known for putting a
lot more effort into producing environment-friendly apparel that
focuses on sustainability. H&M, Adidas, and Nike are among the
many popular international clothing companies that have com-
mitted to driving advancements toward an improved fashion
future. According to H&M Group (2023), their resources are
aimed to be either 100% recycled or obtained through more
environmentally friendly means by 2023, with 30% recycled
materials by 2025. H&M also noted the use of recycled plastic,
derived from sources like PET plastic drinking bottles, plastic
bags, shampoo containers, and various other plastic packaging is
one of its most often obtained components, in which several of
their well-known accessories are made with recycled plastic. This
approach could prevent further damage to the environment. In
addition, Adidas engages in a variety of environmental initiatives.
One of which is using recycled plastic in manufacturing their
products, which is a cornerstone of its commitment to reducing
plastic waste and reducing and preventing pollution in the
world’s oceans. The collaboration between Adidas and Parley is
one of the brand’s sustainability initiatives; Adidas gave the
plastic waste from beaches and coastal towns a new life as an
Adidas x Parley product by intercepting the waste before it
reached the ocean. Another project is initiated by Nike, starting
with the ‘Move to Zero’ program. The journey aims to reduce
waste and carbon emissions to safeguard the future of the sport.
One of the materials they utilize is recycled polyester, which is
created by shredding plastic bottles, turning them into granules,
and then twisting the granules into high-quality yarn. Nike is
currently using recycled polyester made from shredded plastic to
lessen waste, approximately as much as 30% in comparison to
newly produced polyester, and it helps keep 1 billion plastic

Fig. 1 Annual report of plastic waste emissions from selected rivers globally to the ocean as of 2019.

2

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 3 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

Fig. 2 OECD report of the management of plastic pollution growth globally, as of 2019.

bottles out of landﬁlls and rivers and streams each year (Nike
Sustainability 2024).

In recent years, much signiﬁcant research has focused on
customers’ attitudes and behavior regarding sustainable fashion
products by exploring the importance of sustainability within the
fashion sector
(Grazzini et al. 2021). Much research on
environment-friendly clothing has looked at the potential beneﬁts
of eco-conscious product development approaches (Fung et al.
2021; Provin et al. 2021), how customers engage with sustainable
fashion brands on social media platforms (Testa et al. 2021),
along with how consumers perceive, their attitudes toward, and
their willingness to invest in sustainable fashion products, and the
factors that affect these behaviors (Grazzini et al. 2021; Nike
Sustainability 2024).

Presented in Table 1 are the summarized key related studies

alongside the limitations and need for future works.

Nguyen et al. (2020) conducted a fashion-focused survey in
Vietnam and found that 86% of the respondents were aware of
the potential to incorporate recycled plastic waste into the fashion
industry. Kim et al. (2021) highlighted that concerns about the
aesthetic aspects of clothing made from recycled materials could
relate to worries about how well these garments blend with the
consumer’s existing wardrobe, their ability to align with the
consumer’s desired self-image, and their comfort in terms of size.
As a result, consumers might delay or choose not to buy products
made from recycled plastic materials (such as clothing) due to
aesthetic risk (Kim et al. 2021; Testa et al. 2021). These studies
demonstrated that aside from sustainability domains, people’s
behavior encompasses behavioral intention and actual behavior
(Park and Lin 2020; Kuah and Wang 2020; Nguyen et al. 2020;
Kim et al. 2021; German et al. 2022a).

In relation, Polyportis et al. (2022) mentioned that consumers
who experience positive emotions as a byproduct of their efforts
to lessen environmental harm are among the effective responses.
Customers perceive that selecting and valuing products crafted
from recycled materials would evoke positive and comforting
emotions, such as pride as a result of their contribution to a better
world (Adıgüzel and Donato 2021). Moreover, Magnier et al.
(2019) referred to expected moral awareness, which is char-
acterized as a consumer’s hopes regarding the way the goods
would make him or her feel from an ethical perspective. Tezer
and Bodur (2019) referred to the “warm glow” sentiments that
come with just utilizing eco-friendly products, like those made
from recycled materials; it was also highlighted that an increase in

the level of social value placed on customers as individuals, which
contributes to these warm glow feelings, which improves how
much you enjoy the accompanying consumption experience.
Thus, perceived customer value is evident among sustainable
behaviors, which should be considered when assessing consumer
behavior (German et al. 2022a).

Despite many studies exploring sustainable behaviors, it could
be deduced that this recent advancement in apparel, sustainable
still been underexplored—
practices, and consumption has
implicating a research gap in the current trend of apparels. The
holistic measurement of sustainable behavior should be investi-
gated to assess the behavioral
intentions of consumers. The
novelty of this study lies with the sustainability domains, which
were one of the factors which was adopted in this study (German
et al. 2022a). Under the sustainability domains, ﬁve factors are
being considered such as the human, environmental, economic,
productivity, and social aspects (Hajishirzi et al. 2022). On the
other hand, an established theory in the ﬁeld of behavior, known
as the Theory of Planned Behavior (TPB), has been accessible and
It measures a person’s behavioral
extensively contemplated.
characteristics, such as the social aspects that pertain to social ties
and structures that promote stability and stability cohesiveness.
To ensure social sustainability, people and organizations must
examine how to promote healthy social interactions and encou-
rage long-term social systems that promote peace in society
(German et al. 2022a; Talan et al. 2020). These domains are
crucial because they offer a framework for comprehending how
individuals behave concerning sustainability. On the other hand,
human aspects include things that improve people’s quality of
life, such as social justice, education, and health.

Studies focusing on human sustainability examined the best
ways for people and institutions to build equitable and envir-
onmentally friendly communities (Abusaﬁeh and Razem 2017).
Moreover, when it comes to determining productivity, one must
look at how effectively and efﬁciently one can generate things and
services. This aspect is important since it may help decrease waste
and maximize resource consumption by enhancing production,
which can enhance the overall performance of both people and
organizations (Abdel-Shafy and Mansour 2018). On the other
hand, environmental aspects pertain to the ecologically respon-
sible and sustainable practices that are assessed, which also pro-
tect various
and Reich 2023).
Environmental sustainability encompasses examining methods by
which people and companies can preserve resources, lessen their

aspects of

(Gansser

life

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

3

---

<!-- PAGE 4 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

i

s
g
n
d
n
ﬁ

e
h
t

h
t
i

w

t
ﬁ
e
n
e
b

,
t
a
h
t

e
t
i
p
s
e
D

e
c
ﬁ
f
u
s

l

n
o
i
t
a
u
b
a
t
-
s
s
o
r
c

d
n
a

l

n
o
i
t
a
e
r
r
o
c

.

d
e
r
e
d
i
s
n
o
c

l

d
u
o
c

l

n
o
i
t
a
e
r
r
o
c

l

y
n
o

s
a
w

l

y
n
o

d
n
a

s
t
n
e
d
u
t
s

d
e
r
e
d
i
s
n
o
c

y
r
o
t
a
r
o
p
x
e

l

e
v
i
t
a
t
i
l

a
u
q

l

y
n
O

d
e
s
u

n

i

t
n
e
m
s
s
e
s
s
a

e
v
i
t
a
t
i
l

a
u
q
r
e
d
i
s
n
o
c
o
t

d
e
t
s
e
g
g
u
s

y
d
u
t
s

e
h
T

.

l

y
g
o
o
d
o
h
t
e
m

o
t

i

s
e
d
u
t
s

d
e
t
a
e
r

l

r
o
f

e
r
u
t
u
f

e
h
t

t
n
e
c
e
r

e
r
o
m
d
n
a

a
t
a
d

e
r
o
m

.

s
l
o
o
t

l

a
c
i
t
y
a
n
a

l

l

e
b
a
n
a
t
s
u
s

i

s
s
e
s
s
a

y

l
l

a
c
i
t
s
i
l

o
h

.

e
s
a
h
c
r
u
p

l

e
r
a
p
p
a

e
e
h
t

e
r
o
m
d
n
a
t
s
r
e
d
n
u

o
t

d
e
d
n
e
t
x
e

e
b

o
t

d
e
t
s
e
g
g
u
s

o
s
l
a

s
a
w
s
r
o
t
c
a
f

e
r
o
m

f
o

n
o
i
t
a
r
o
p
x
E

l

.

s
r
e
m
u
s
n
o
c

f
o

i

r
o
v
a
h
e
b

i

g
n
y
u
b

g
n

i
l
c
y
c
e
r

e
b

o
t

d
e
t
s
e
g
g
u
s

e
r
e
w
s
d
o
h
t
e
m

e
v
i
t
a
n
r
e
t
l
a

d
n
a

)
s
t
n
e
d
n
o
p
s
e
r

0
0
4
>
(

e
z
i
s

l

e
p
m
a
s

r
e
g
r
a
L

.

d
e
s
s
e
s
s
a

y
d
u
t
s

s
u
o
u
n
i
t
n
o
c

,

k
r
o
w
e
m
a
r
f

e
h
t

n

i

l

e
r
a
p
p
a

e
h
t

f
o
n
o
i
s
s
e
r
g
o
r
p
e
h
t
o
t
e
u
d

s
r
o
t
c
a
f

e
r
o
m
e
t
a
c
i
l

p
m

i

d
n
a

d
n
a
p
x
E

e
s
e
n
h
C

i

n
o

l

y
n
o

d
e
s
u
c
o
f

,

y
r
t
s
u
d
n

i

f
o

t
n
e
m
s
s
e
s
s
a

d
n
a

,

s
r
e
m
u
s
n
o
c

h
t
i

w
s
r
o
t
c
a
f

y
t
i
l
i

i

b
a
n
a
t
s
u
s

r
e
d
a
o
r
b

e
t
a
e
r
c

o
t

s
r
o
t
c
a
f

r
e
h
t
o

g
n
i
t
a
g
i
t
s
e
v
n

I

,

s
s
e
n
e
v
i
t
c
e
f
f
e

l
i

a
t
e
r

r
o
f

d
n
a

,

y
t
i
l

a
u
q

l
l

a
r
e
v
o

i

s
e
g
e
t
a
r
t
s

,

y
t
i
l
i

b
a
r
u
d

h
t
i

w
e
c
n
a
d
r
o
c
c
a

n

i

y
t
i
l
i

i

b
a
n
a
t
s
u
s

e
b

l

d
u
o
c

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

r
e
m
u
s
n
o
c

.

d
e
s
s
e
s
s
a

r
e
h
t
r
u
f

.

s
l
o
o
t

r
e
h
t
o

l

d
u
o
c

t
u
b

,

y
d
u
t
s

e
h
t

f
o

n

i

s
l
a
i
t
n
e
d
e
r
c

l

e
b
a
n
a
t
s
u
s

i

r
i
e
h
t

t
u
o
b
a

d
n
a

t
n
e
t
n
o
c

e
r
o
m
g
n

i
l

e
e
f

e
s
o
o
h
c

l

y
e
v
i
t
c
a

l

d
u
o
w
y
e
h
t

d
e
t
a
c
i
d
n

i

t
n
e
r
a
p
s
n
a
r
t

e
r
o
m
e
r
e
w
y
e
h
t

f
i

s
d
n
a
r
b

y
u
b

o
h
w

d
e
t
r
o
p
e
r

e
c
n
i
s

l

o
o
t

s
i
s
y
a
n
a

l

s
s
e
w
o
r
p

r
e
h
g
h

i

s
d
o
o
g

d
e
c
u
d
o
r
p

l

y
b
a
n
a
t
s
u
s

i

r
e
h
t
o

h
t
i

w
e
r
o
m
d
e
r
o
p
x
e

l

e
b

l

d
u
o
h
s

s
r
o
t
c
a
f

l

i

a
r
o
v
a
h
e
b

f
o

t
n
e
d
e
c
e
t
n
A

g
n
i
s
a
h
c
r
u
p

l
l
i
t
s

o
s
l
a

e
r
a

e
h
t

e
r
e
h
T

.

i

s
e
u
q
n
h
c
e
t

n
o

i

s
e
d
u
t
s

d
e
t
i

m

i
l

h
c
i
h
w

i

,
r
o
v
a
h
e
b

l
l

a
r
e
v
o
d
n
a

n
o
i
t
n
e
t
n

i

r
e

l
l

a
m
s

d
e
r
e
d
i
s
n
o
c

l

y
n
o

e
v
a
h

y
e
h
T

I

9
1
-
D
V
O
C

e
h
t

o
t

e
u
d

e
z
i
s

l

e
p
m
a
s

e
r
e
w
s
t
n
e
d
u
t
s

l

y
n
o

,

c
i
m
e
d
n
a
p

.
t
n
e
m
s
s
e
s
s
a

r
e
h
t
r
u
f

s
d
e
e
n

p
a
G

e
s
u

o
t

d
e
t
s
e
g
g
u
s

d
n
a

,

d
e
t
a
u
a
v
e

l

e
r
a

e
v
e

i
l

e
b

y
e
h
t

s
e
s
s
e
n
i
s
u
b
m
o
r
f

y
u
b

s
r
e
m
u
s
n
o
C

.

e
r
a
f
l
e
w

l

a
t
n
e
m
n
o
r
i
v
n
e

r
o

l

a
i
c
o
s

o
t

g
n
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

e
s
a
h
c
r
u
p

r
e
g
r
a

l

a

d
e
t
i
b
h
x
e

i

l

e
r
a
p
p
a

d
e
l
c
y
c
p
u

d
n
a

d
e
l
c
y
c
e
R

s
t
c
u
d
o
r
p

f
o
%
5
3

n
a
h
t

e
r
o
m
n

i

g
n
i
t
l
u
s
e
r

,

p
a
g

e
s
e
h
t

g
n
i
s
a
h
c
r
u
p

t
o
n

s
t
n
e
d
n
o
p
s
e
r

l

e
b
a
r
o
v
a
f

i

g
n
v
a
h

e
t
i
p
s
e
d

s
t
c
u
d
o
r
p

i

s
g
n
d
n
ﬁ

n
i
a
M

,

e
r
a
u
q
s
-
i
h
c

,

s
i
s
y
a
n
a

l

e
v
i
t
p
i
r
c
s
e
D

n
o
i
s
s
e
r
g
e
r

c
i
t
s
i
g
o

l

d
n
a

)
s
(
d
o
h
t
e
M

.

s
n
o
i
t
n
e
t
n

i

e
s
a
h
c
r
u
p

g
n
o
r
t
s

d
n
a

’

o
t

e
s
o
o
h
c

s
r
e
m
u
s
n
o
c

s
e
i
r
t
n
u
o
c
U
E

l

n
o
i
t
a
u
b
a
T
-
s
s
o
r
C

d
n
a

l

n
o
i
t
a
e
r
r
o
C

l

a
t
n
e
m
n
o
r
i
v
n
e

d
n
a

,
l

a
i
c
o
s

,
l

a
n
o
s
r
e
p

l

d
e
t
a
e
r
-
t
c
u
d
o
r
p

e
h
t

e

l
i

h
w

,

s
r
o
t
c
a
f

.

e
c
n
a
c
ﬁ
n
g
i
s

i

y
n
a

e
v
a
h

t
o
n

d
d

i

s
r
o
t
c
a
f

r
i
e
h
t

d
n
a

s
t
n
e
m
e
s
i
t
r
e
v
d
a

r
i
e
h
t

h
t
o
b

.

i

g
n
g
a
k
c
a
p

o
t
n

i

e
k
a
t

o
t

s
n
o
i
t
a
r
e
d
i
s
n
o
c

l

a
i
c
u
r
c

t
s
o
m
e
h
t

f
o

e
n
o

s
a

y
t
i
l
i

i

b
a
n
a
t
s
u
s

,

i

g
n
h
t
o
l
c

g
n
i
s
a
h
c
r
u
p

n
e
h
w

t
a
h
t

d
e
w
o
h
s

i

s
e
d
u
t
s

e
h
t

t
n
u
o
c
c
a

i

n
e
r
e
h
w

i

t
n
a
n
m
o
d
e
r
p

e
h
t

d
e
t
u
t
i
t
s
n
o
c

n
e
m
o
w

s
r
e
m
u
s
n
o
c

e
r
u
s
i
e
h
t
a

l

f
o

t
n
e
m
g
e
s

n

i

l

e
o
r

i

g
n
d
a
e

l

a

d
e
y
a
p

l

d
n
a

d
e
r
e
d
i
s
n
o
c

i

s
l
a
n
n
e

l
l
i

m
S
U

l

e
b
a
n
a
t
s
u
s

i

a

r
o
f

g
n
i
t
a
c
o
v
d
a

.

l

e
y
t
s
e
f
i
l

e
r
u
s
i
e
h
t
a

l

e
h
t

s
a

d
e
t
p
m
o
r
p

s
r
o
t
c
a
f

l

a
n
o
i
t
o
m
o
r
P

y
b

d
e
w
o

l
l

o
f

,

l

e
b
a
i
r
a
v

t
n
a
c
ﬁ
n
g
i
s

i

t
s
o
m

e
v
i
s
n
e
t
n
I

:

s
i
s
y
a
n
a

l

e
v
i
t
a
t
i
l

a
u
Q

s
s
e
c
o
r
p
w
e
v
r
e
t
n

i

i

g
n

i
l

e
d
o
M
n
o
i
t
a
u
q
E

l

a
r
u
t
c
u
r
t
S

e
u
a
v

l

i

d
e
v
e
c
r
e
p

f
o

s
n
o
i
s
n
e
m
d

i

r
u
o
F

g
n

i
l

e
d
o
M
n
o
i
t
a
u
q
E

l

a
r
u
t
c
u
r
t
S

e
c
n
e
i
r
e
p
x
e

g
n
i
s
a
h
c
r
u
p

n
o

d
e
r
o
p
x
E

l

s
r
e
m
u
s
n
o
c

f
o

n
o
i
t
n
e
t
n

i

e
h
t

d
n
a

d
e
l
c
y
c
e
r

d
n
a

d
e
l
c
y
c
p
u

g
n
o
m
a

.

s
t
c
u
d
o
r
p

i

n
o
h
s
a
f

)
s
(
e
v
i
t
c
e
j
b
O

i

n
o
h
s
a
f

t
s
a
f

f
o

y
t
i
l
i

i

b
a
n
a
t
s
u
s

s
d
r
a
w
o
t

e
d
u
t
i
t
t
a

r
e
m
u
s
n
o
c

f
o

l

s
i
s
y
a
n
A

.

K
U

e
h
t

n

i

s
t
c
u
d
o
r
p

n
i
L

d
n
a

k
r
a
P

)
0
2
0
2
(

e
c
n
e
r
e
f
e
R

.
l

a

t
e

g
n
a
h
Z

)
1
2
0
2
(

.
s
p
a
g

d
n
a

s
e
i
d
u
t
s

d
e
t
a
l
e
r

y
e
k

d
e
z
i
r
a
m
m
u
S

1

e
l
b
a
T

e
d
a
m

-
r
e
t
s
e
y
o
p

l

d
e
l
c
y
c
e
r

r
o
f

s
n
o
i
t
p
e
c
r
e
p

e
u
a
v

l

s
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
s
a
h
c
r
u
p

’

l

i

a
n
n
e

l
l
i

l

m
e
a
m
e
f

i

d
e
n
m
a
x
E

)
1
2
0
2
(

.
l

a

t
e

i

h
C

.
l

e
r
a
p
p
a

e
r
u
s
i
e
h
t
a

l

f
o

t
c
a
p
m

i

e
h
t

e
t
a
g
i
t
s
e
v
n

i

o
t

d
e
m
A

i

l

a
n
o
s
r
e
p

,

s
r
o
t
c
a
f

l

d
e
t
a
e
r
-
t
c
u
d
o
r
p

l

a
i
c
o
s

,

s
r
o
t
c
a
f

l

a
n
o
i
t
o
m
o
r
p

d
n
a

l

a
t
n
e
m
n
o
r
i
v
n
e

d
n
a

,

s
r
o
t
c
a
f

,

s
r
o
t
c
a
f

d
e
l
c
y
c
e
r

n
o

s
r
o
t
c
a
f

c
i
m
o
n
o
c
e

i

.
r
o
v
a
h
e
b

i

g
n
y
u
b

i

g
n
h
t
o
l
c

r
a
h
t
k
u
M

r
e
e
h
a
J

)
4
2
0
2
(

.
l

a

t
e

i

d
e
v
e
c
r
e
p

r
e
m
o
t
s
u
c

e
h
t

i

d
e
n
b
m
o
C

-
e
d
u
t
i
t
t
a
-
e
g
d
e
w
o
n
k

l

d
n
a

e
u
a
v

l

)
4
2
0
2
(

.
l

a

t
e

n
i
J

h
t
o
b

s
s
e
s
s
a

o
t

d
e
l
c
y
c
e
r

n
o

s
r
o
t
c
a
f

c
ﬁ
i
c
e
p
s

k
r
o
w
e
m
a
r
f

i

r
o
v
a
h
e
b

c
ﬁ
i
c
e
p
s
-
r
e
m
u
s
n
o
c

4

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

l

a
r
e
v
e
s

l
l
i
t
s

s
r
a
e
y

5
4

e
r
a

r
e
v
o

r
e
g
a

s

l

i

a
u
d
v
d
n

i

i

e
r
e
h
T

.

l

y
e
v
i
t
a
r
a
p
m
o
c

m
a
e
r
t
s
n
a
m
e
h
t

i

g
n
i
t
n
e
v
e
r
p

s
e
l
c
a
t
s
b
o

l

r
e
t
s
e
y
o
p
-
n
o
t
t
o
c

d
e
l
c
y
c
e
r

f
o

e
s
u

.

i

g
n
h
t
o
l
c

d
e
d
n
e
b

l

’

l

d
o

d
n
a

5
1

w
o
e
b

l

d
e
g
a

n
e
r
d

l
i

h
c

n
e
h
t

y
t
i
l
i

i

b
a
n
a
t
s
u
s

n

i

d
e
t
s
e
r
e
t
n

i

d
n
a

f
o

s
u
o
i
c
s
n
o
c

e
r
o
m
g
n
m
o
c
e
b

i

e
r
a

d
n
u
o
r
g
k
c
a
b

l

a
n
o
i
t
a
c
u
d
e

r
e
h
g
h

i

h
t
i

w

.

g
n
i
s
i
d
n
a
h
c
r
e
m

.
l

e
r
a
p
p
a

d
e
l
c
y
c
e
r

g
n
i
s
a
h
c
r
u
p

d
r
a
w
o
t

i

d
e
v
e
c
r
e
p

t
a
h
t

d
n
u
o
f

s
a
w

t
i

,

l

y
b
a
t
o
N

d
e
c
n
u
o
n
o
r
p

e
r
o
m
a

d
a
h

e
u
a
v

l

y
t
i
l

a
u
q

t
c
u
d
o
r
p

,

l

y
g
n
i
t
s
e
r
e
t
n
I

.

s
r
o
t
c
a
f

n
a
h
t

n
o
i
t
n
e
t
n

i

e
s
a
h
c
r
u
p

n
o

t
c
e
f
f
e

r
e
h
t
o

w
o
h

s
s
e
s
s
a

o
t

l

e
b
a

s
a
w
y
d
u
t
s

e
h
T

e
b

l

d
u
o
c

s
t
c
u
d
o
r
p

i

n
o
h
s
a
f

d
e
l
c
y
c
e
r

s
t
l
u
s
e
r

e
h
T

.

e
r
u
t
u
f

e
h
t

n

i

d
e
m
u
s
n
o
c

a

e
t
a
r
t
s
n
o
m
e
d

t
o
n

d
d

i

.

s
e
d
u
t
i
t
t
a

n
o

t
c
a
p
m

i

l

e
g
d
e
w
o
n
k

t
n
a
c
ﬁ
n
g
i
s

i

d
e
g
a

s
r
e
m
u
s
n
o
c

h
g
u
o
h
t
l
a

t
a
h
t

d
n
a

a
t
a
r
t
s

l

a
i
c
o
s

i

r
e
h
g
h
m
o
r
f

5
4
–
5
2

w
o
h
s

s
a

l

e
g
d
e
w
o
n
k

l

a
t
n
e
m
n
o
r
i
v
n
e

d
n
a

l

y
e
v
i
t
i
s
o
p

s
e
d
u
t
i
t
t
a

t
a
h
t

s
r
o
t
c
a
f

’

s
r
e
m
o
t
s
u
c

t
n
a
c
ﬁ
n
g
i
s

i

d
e
c
n
e
u
ﬂ
n

i

-
t
c
u
d
o
r
p

d
n
a

i

w
e
v
r
e
t
n

i

p
u
o
r
g

f
o

d
o
h
t
e
m
d
e
x
M

i

e
h
t

r
o
f

t
n
e
m
s
s
e
s
s
a

l

r
a
u
b
a
t
-
s
s
o
r
c

d
n
a

t
n
e
m
s
s
e
s
s
a

e
v
i
t
a
t
i
l

a
u
q

s
a

.
t
c
e
p
s
a

e
v
i
t
a
t
i
t
n
a
u
q

.

s
t
c
u
d
o
r
p

d
e
t
c
e
f
f
a

e
r
a

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
s
a
h
c
r
u
p

d
n
a

i

r
o
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
w
o
h

i

d
e
n
m
a
x
E

l

r
a
u
c
i
t
r
a
p

a

h
t
i

w

,

i

g
n
h
t
o
l
c

d
e
d
n
e
b

l

l

r
e
t
s
e
y
o
p
-
n
o
t
t
o
c

d
e
l
c
y
c
e
r

y
b

)
4
2
0
2
(

.
l

a

t
e

a
t
n
a
r
P

l

e
r
a
p
p
a

l

e
b
a
n
a
t
s
u
s

i

n
o

s
i
s
a
h
p
m
e

---

<!-- PAGE 5 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

.

s
t
l
u
s
e
r

t
n
e
r
e
f
f
i
d

e
v
a
h

y
a
m

)
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
n
o
i
t
i
d
d
a

t
a
h
t

d
e
t
s
e
g
g
u
s

o
s
l
a

s
a
w

t
I

r
e
h
t
r
u
f
o
t
d
e
s
u
e
b
y
a
m
s
l
o
o
t

r
e
h
t
o
r
o

.
t
l
u
s
e
r

l
l

a
r
e
v
o

e
h
t

s
s
e
s
s
a

e
r
e
w
s
r
e
m
u
s
n
o
c

Z

n
e
G
y
n
O

l

t
n
e
r
e
f
f
i
d

t
a
h
t

d
n
a

,

d
e
s
s
e
s
s
a

c
i
h
p
a
r
g
o
e
g

,

e
g
a
(

s
r
e
m
u
s
n
o
c

p
a
G

d
n
a

,

s
r
e
m
u
s
n
o
c
K
U
n
o

l

y
n
o

d
e
s
u
c
o
F

d
e
d
e
e
n

s
i

t
n
e
m
s
s
e
s
s
a

r
e
h
t
r
u
f

t
a
h
t

d
n
a

e
d
u
t
i
t
t
a

l

d
e
t
a
e
r
r
o
c

i

s
e
d
u
t
s

e
c
n
i
s

t
u
b

,
r
a
e
n

i
l

e
r
e
w

i

r
o
v
a
h
e
b

n
o

t
c
a
p
m

i

,

n
o
i
t
i
d
d
a

n

I

.
t
o
n

s
a
w
y
d
u
t
s

r
i
e
h
t

e
b

l

d
u
o
c

s
r
o
t
c
a
f

y
t
i
l
i

i

b
a
n
a
t
s
u
s

e
h
t

n
o

n
o
i
t
a
r
o
p
x
e

l

r
e
d
a
o
r
b

s
a

h
c
u
s

,

d
e
s
s
e
s
s
a

d
n
a

d
e
r
e
d
i
s
n
o
c

.

e
c
n
e
r
e
f
e
r
p

d
n
a

n
o
i
t
p
e
c
r
e
p

i

n
a
h
c

l

y
p
p
u
s

e
h
t

f
o

s
e
i
t
r
a
p

l

e
p
i
t
l
u
M

s
a

d
e
r
e
d
i
s
n
o
c

e
b

l

d
u
o
c

l

s
e
b
a
i
r
a
v

g
n

i
l
c
y
c
e
r

r
e
d
i
s
n
o
c

,

s
n
o
i
s
n
e
t
x
e

d
n
a

s
e
u
s
s
i

i

y
t
n
a
t
r
e
c
n
u

,

s
l
e
d
o
m

l

a
c
i
t
a
m
e
h
t
a
m

f
o

t
n
e
m
p
o
e
v
e
d

l

e
h
t

n

i

d
e
r
e
d
i
s
n
o
c

e
b

l

d
u
o
c

.
t
n
e
m
s
s
e
s
s
a

r
o
f

s
t
c
u
d
o
r
p

e
c
u
d
e
r

o
t

d
e
s
u

e
b

l

d
u
o
c

n
o
i
t
a
m
o
t
u
A

l

e
d
o
m

f
o

n
o
i
s
n
e
t
x
e

,

n
o
i
s
s
i
m
e

n
o
b
r
a
c

g
n
i
t
s
e
v
n

i

r
e
d
i
s
n
o
c

o
t

d
e
t
s
e
g
g
u
s

s
a
w

,
t
n
e
m
t
s
e
v
n

i

e
t
e
r
c
s
i
d

r
o

s
u
o
u
n
i
t
n
o
c

d
n
a

s
c
i
t
s
i
g
o

l

y
t
r
a
p
-
d
r
i
h
t

r
e
g
r
a

l

d
n
a

.
l

e
d
o
m
n
a
h
c

i

l

y
p
p
u
s

l
l

a
r
e
v
o

d
n
a

s
n
o
i
t
a
c
i
l

p
m

i

r
e
h
t
o

n

i

d
e
s
s
e
s
s
a

h
t
i

w

t
u
p
t
u
o

l

e
t
a
e
r
r
o
c

,

s
t
c
e
p
s
a

s
r
o
t
c
a
f

r
e
h
t
o

d
n
a

,

s
d
n
a
m
e
d

t
e
k
r
a
m

h
t
i

i

w
s
e
i
t
n
a
t
r
e
c
n
u

l

a
i
r
e
g
a
n
a
M

e
b

l

d
u
o
c

k
r
o
w
e
m
a
r
f

r
e
d
a
o
r
b

.

d
e
s
s
e
s
s
a

e
b

y
a
m

ARTICLE

l

a
t
o
t

–

d
n
a

,

i

s
e
u
q
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
m

i
t
p
o

,

s
r
e
t
e
m
a
r
a
p

r
e
h
t
o

r
e
d
i
s
n
o
C

e
m
o
c
t
u
o

s
s
e
c
o
r
p

i

n
a
h
c

l

y
p
p
u
s

d
e
d
n
e
t
x
e

r
e
h
t
o

i

g
n
p
o
e
v
e
d

l

.

s
l
e
d
o
m

l

a
c
i
t
a
m
e
h
t
a
m

s
t
l
u
s
e
r

e
h
T

.

e
h
t

’

e
h
t

d
e
t
a
r
e
d
o
m

,

’

b
u
S

‘

,

’

d
t
A

‘

n
n
P

I

‘

f
o

’

n
n
P

I

‘

l

e
o
r

t
a
h
t

g
n
i
t
a
r
e
d
o
m

d
e
h
s
i
l

b
a
t
s
e

n
e
e
w
t
e
b

i

p
h
s
n
o
i
t
a
e
r

l

k
r
o
w
e
m
a
r
f

l

e
v
o
n

a

i

s
e
d
v
o
r
p

h
c
r
a
e
s
e
r

s
i
h
T

.

y
l
t
n
a
c
ﬁ
n
g
i
s

i

’

I

P
A
G

‘

d
n
a

,

C
C

’

‘

.

’

I

P
A
G

‘

s

’

d
n
a

’

C
C

‘

d
n
a

,

r
t

A

’

‘

,

’

K
E

‘

e
h
t

r
e
m
u
s
n
o
c

Z

n
o
i
t
a
r
e
n
e
G

l

e
b
a
i
r
a
v

f
o

d
e
s
o
p
m
o
c

s
e
c
i
t
c
a
r
p

l

a
i
c
o
s

o
t

l

e
b
i
s
s
e
c
c
a

e
r
a

t
a
h
t

s
e
i
c
n
e
t
e
p
m
o
c

d
n
a

,

s
l
a
i
r
e
t
a
m

,

i

s
g
n
n
a
e
m

o
t

o
t

f
o

y
c
n
e
u
q
e
r
f

e
v
i
t
a
e
r

l

e
h
t

g
n
i
s
a
e
r
c
n

i

e
u
n
e
v
a

e
n
o

,

y
l
t
n
e
u
q
e
s
n
o
C

.

s
r
e
h
t
o

n
e
v
o
r
p

s
a
h

y
d
u
t
s

e
h
T

.
t
n
e
m
n
r
e
v
o
g

e
h
t

m
o
r
f

i

s
e
d
i
s
b
u
s

r
e
g
r
a

l

i

n
a
t
b
o

o
t

i

g
n
p
e
h

l

,

n
o
i
s
s
i
m
e

n
o
b
r
a
c

s
s
e

l

i

s
e
d
v
o
r
p
m
e
t
s
y
s

e
h
t

n
a
h
t

t
ﬁ
o
r
p

e
r
o
m
%
6
7
8

.

d
e
s
o
p
o
r
p

e
h
t

t
a
h
t

l

a
c
i
t
y
a
n
a

l

e
h
t

d
e
w
o
h
s

.

m
e
t
s
y
s

n
o
i
t
c
u
d
o
r
p

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
t

y
d
u
t
s

e
h
T

l

a
t
o
t

e
h
t

t
a
h
t

e
v
o
r
p

h
c
i
h
w
s
t
l
u
s
e
r

i

n
a
h
c

l

y
p
p
u
s

l

e
b
a
n
a
t
s
u
s

i

e
h
t

f
o

t
ﬁ
o
r
p

e
m

i
t
d
a
e

l

h
t
o
b
f
o
n
o
i
t
c
n
u
f

x
e
v
n
o
c

s
A

.

e
m

i
t

d
a
e

l

e
h
t

f
o

e
c
n
a
i
r
a
v

a

s
i

d
n
a

o
t

l

a
i
c
u
r
c

s
i

g
n

i
l
l

e
s

l

e
n
n
a
h
c

t
n
e
r
e
f
f
i
d

r
e
m
o
t
s
u
c

g
n
i
s
a
e
r
c
n

i

r
o
f

y
r
t
s
u
d
n

i

y
n
a

o
t

e
n

i
l

n
o

s
t
c
u
d
o
r
p

r
i
e
h
t

s
e
s
i
t
r
e
v
d
a

d
n
a

l

e
n
n
a
h
c

d
i
r
b
y
h

y
b

s
t
c
u
d
o
r
p

r
i
e
h
t

s
l
l

e
s

r
e

l
i

a
t
e
r

e
h
t

,

d
n
a
m
e
d

e
v
i
t
c
e
f
f
e

t
s
o
m
e
h
t

i

d
e
n
m
r
e
t
e
D

.

s
u
o
m
a
f

e
r
o
m
m
e
h
t

e
k
a
m

-
i
t
l
u
m
e
h
t

g
n
i
t
c
e
t
o
r
p

n

i

s
e
h
c
a
o
r
p
p
a

k
r
o
w
t
e
n

)
C
S
(

i

n
a
h
c

l

y
p
p
u
s

l

e
u
f
o
b

i

,

k
s
i
r

n
o
i
t
p
u
r
s
i
d

d
n
a

l

a
n
o
i
t
a
r
e
p
o
m
o
r
f

d
n
a

,

n
o
i
t
a
t
r
o
p
s
n
a
r
t

s
a

l
l

e
w
s
a

y
g
r
e
n
e

e
c
u
d
e
r

r
o
f

s
e
i
c
i
l

o
p

d
e
t
s
e
g
g
u
s

s
n
o
i
s
s
i
m
e

n
o
b
r
a
c

d
n
a

n
o
i
t
p
m
u
s
n
o
c

l

e
b
a
t
u
t
i
t
s
b
u
s

e
p
y
t
-
e
g
n
i
s

l

h
t
i

w

l

e
d
o
m

d
e
r
e
d
i
s
n
o
c

s
a
w
n
o
i
t
c
u
d
o
r
p

t
c
u
d
o
r
p

,

y
c
i
l

o
p

x
a
t
-
d
n
a
-
p
a
c

a

g
n
i
s
o
p
m

i

y
b

d
n
a

,

l

y
g
o
o
n
h
c
e
t

n
e
e
r
g

n

i

g
n
i
t
s
e
v
n

i

.

s
t
c
u
d
o
r
p

r
o
f

g
n
i
s
i
t
r
e
v
d
a

n
o
i
t
c
u
d
o
r
p

i

l

e
b
x
e
ﬂ

.
t
s
o
c

)
E
B
C
(

i

l

e
b
a
n
a
t
s
u
S

e
h
t

o
t

s
s
e
c
c
a

f
o

r
e
t
t
a
m
a

’

s
e
m
o
c
e
b

e
s
u
e
r

s
n
a
e

j

s
r
e
m
u
s
n
o
c

i

g
n
v
o
r
p
m

i

s
n
a
e

j

d
e
s
u

r
o
f

i

g
n
p
p
o
h
s

f
o

e
c
i
t
c
a
r
p

m
r
o
f
s
n
a
r
t

o
t

g
n
i
t
p
m
e
t
t
a

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

.

s
f
e

i
l

e
b

r
o

s
e
d
u
t
i
t
t
a

r
i
e
h
t

t
i

m
e

o
t

n
e
e
s

s
a
w
m
e
t
s
y
s

n
o
i
t
c
u
d
o
r
p

l

e
b
a
i
r
a
v

e
h
t

f
o

e
g
a
t
s

y
r
e
v
E

d
e
z
i
l
i
t
u

l

e
b
a
t
ﬁ
o
r
p

s
a
w
y
c
i
l

o
p

t
s
o
m
e
h
t

d
n
ﬁ

o
t

l

e
n
n
a
h
c
-
l
a
u
d
A

y

l
l

u
f

a

s
i

s
i
h
T

.

s
n
o
i
s
i
c
e
d

l

a
i
r
e
g
a
n
a
m

y
b

d
e
r
e
v
o
c
m
e
t
s
y
s

n
o
i
t
c
u
d
o
r
p

.
t
n
e
m
t
s
e
v
n

i

l

y
g
o
o
n
h
c
e
t

n
e
e
r
g

l

e
b
a
i
r
a
v

d
e

l
l

o
r
t
n
o
c
-
n
o
i
s
s
i
m
e

-
n
i
-
p
u
k
c
i
p
-
e
n

i
l

n
o
-
y
u
b

n
e
e
w
t
e
b

d
n
a
h
-
n
o

d
n
a

,
r
e
d
r
o
k
c
a
b

,

e
r
o
t
s

n
o
i
t
a
e
r

l

c
i
t
s
i
r
e
t
c
a
r
a
h
c

a

t
l
i

u
B

l

a
t
o
t

t
c
a
x
e

n
a

i

g
n
v
g

i

y
b

y
r
o
t
n
e
v
n

i

h
g
u
o
r
h
t

n
o
i
t
c
n
u
f

e
h
t

f
o

d
a
e
t
s
n

i

t
ﬁ
o
r
p

d
e
t
c
e
p
x
e

n
o
i
t
c
n
u
f

t
ﬁ
o
r
p

,

’

d
t
A

‘

t
a
h
t

d
e
w
o
h
s

l

y
e
v
i
t
i
s
o
p

e
r
e
w

M
E
S

f
o

t
l
u
s
e
r

e
h
T

’

C
C

‘

d
n
a

,

b
u
S

’

‘

i

s
g
n
d
n
ﬁ

n
i
a
M

g
n

i
l

e
d
o
M
n
o
i
t
a
u
q
E

l

a
r
u
t
c
u
r
t
S

)
s
(
d
o
h
t
e
M

’

e
c
n
e
u
ﬂ
n

i

e
h
t

i

e
n
m
r
e
t
e
d

o
t

d
e
s
o
p
o
r
P

,
)
K
E
(

l

e
g
d
e
w
o
n
K

l

a
t
n
e
m
n
o
r
i
v
n
E

f
o

‘

)
s
(
e
v
i
t
c
e
j
b
O

s
e
s
e
h
t
o
p
y
h

x
i
s

,

o
s
l
A

.
I

P
A
G
o
t

d
e
t
a
e
r

l

r
e
m
u
s
n
o
C

,
)
r
t

A
(

m
s
i
u
r
t
l

A

g
n
i
t
s
e
t

l

d
e
t
a
u
m
r
o
f

e
r
e
w

f
o

s
t
c
u
r
t
s
n
o
c

d
n
a

)
C
C
(

‘

’

’

e
c
n
e
d
ﬁ
n
o
C

)
d
e
u
n
i
t
n
o
c
(

1

e
l
b
a
T

.
l

a

t
e

i

o
n
h
s
i
V

)
5
2
0
2
(

e
c
n
e
r
e
f
e
R

l

e
b
i
s
s
e
c
c
a
n

i

d
n
a

s
l
a
u
d
v
d
n

i

i

i

e
m
o
s

f
o

e
c
i
t
c
a
r
p

e
h
t

n
o

y

l
l

n
e
e
w
t
e
b

i

p
h
s
n
o
i
t
a
e
r

l

e
h
t

l

e
r
o
p
x
e

o
t

)
I
P
A
G
(

s
t
c
u
d
o
r
P

l

e
r
a
p
p
A
n
e
e
r
G

’

t
c
n
i
t
s
i
d

l

s
e
v
o
v
n

i

t
n
e
r
e
f
f
i
d

e
s
e
h
t

s
n
a
e

j

r
o
f

i

g
n
p
p
o
h
S

f
o

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
o
i
s
s
u
c
s
i
d

p
u
o
r
g

s
u
c
o
F

k
r
o
w
e
m
a
r
f

e
c
i
t
c
a
r
p

l

a
i
c
o
s

a

d
e
t
p
o
d
A

d
n
a

s
e
d
u
t
i
t
t
a

r
e
m
u
s
n
o
c

h
c
i
h
w
n

i

.
l

a

t
e

r
e
y
o
B

)
5
2
0
2
(

’

)
B
P
T
(

i

r
o
v
a
h
e
B

d
e
n
n
a
P

l

f
o

y
r
o
e
h
T

e
v
i
t
c
e
b
u
S

j

,
)
d
t
A
(

‘

”
e
d
u
t
i
t
t

i

d
e
v
e
c
r
e
P

d
n
a

)
b
u
S
(

’

A
e
k
i
l

m
r
o
N

e
s
a
h
c
r
u
p

o
t

n
o
i
t
n
e
t
n

i

s
r
e
m
u
s
n
o
c

’

n
o

)
c
h
b
P
(

l

o
r
t
n
o
c

l

i

a
r
o
v
a
h
e
b

‘

’

‘

‘

‘

s
e
s
u
c
o
f

y
d
u
t
s

e
h
T

.

g
n
i
s
a
h
c
r
u
p

e
k
i
l

i

r
o
v
a
h
e
b

i

i

g
n
n
a
p
x
e

l

l

e
o
r

l
l

a
m
s

l

y
e
v
i
t
a
e
r

l

a

y
a
p

l

s
f
e

i
l

e
b

s
n
o
i
s
i
c
e
d

a
c
ﬁ
i
c
e
p
s

e
g
a
t
n
a
v
d
a

g
n
i
k
a
t

,

s
n
a
e

j

r
o
f

i

g
n
p
p
o
h
s

e
h
t

n

i

s
t
l
u
d
a

h
t
i

w
s
p
u
o
r
g

s
u
c
o
f

f
o

d
e

l
i

a
t
e
d

t
i
c
i
l

e

o
t

m
o
d
g
n
K

i

d
e
t
i
n
U

r
o
f

s
e
c
n
e
r
e
f
e
r
p

r
i
e
h
t

f
o

s
n
o
i
t
a
n
a
p
x
e

l

.

s
n
a
e

j

d
e
s
u

r
o

,

d
e
l
c
y
c
e
r

,

w
e
n

w
e
i
v
e
R

r
o
f

s
l
a
n
r
u
o
J

d
e
t
s
e
g
g
u
S

r
e
w
e
i
v
e
R

r
e
d
n
u
m
e
t
s
y
s

n
o
i
t
c
u
d
o
r
p

l

e
b
a
i
r
a
v

a

f
o

s
s
e
n
e
v
i
t
c
e
f
f
e

e
h
t

d
e
s
s
e
s
s
A

s
a
w
s
e
i
c
i
l

o
p

l

o
r
t
n
o
c

s
n
o
i
s
s
i
m
e

.

d
e
v
r
e
s
b
o

,

g
n

i
l
l

e
s

e
n

i
l

n
o

d
e
r
e
d
i
s
n
o
c

y
d
u
t
s

e
h
T

-
e
n

i
l

n
o
-
y
u
b

d
n
a

,

g
n

i
l
l

e
s

i

e
n
ﬂ
f
o

g
n

i
l
l

e
s

r
o
f

s
e
i
c
i
l

o
p

e
r
o
t
s
-
n
i
-
p
u
k
c
i
p

.

s
e
r
o
t
s

l
i

a
t
e
r

m
o
r
f

s
t
c
u
d
o
r
p

.
l

a

t
e

r
a
k
r
a
S

)
2
2
0
2
(

.
l

a

t
e

r
a
k
r
a
S

)
3
2
0
2
(

.

i

s
e
u
q
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
m

i
t
p
o

c
i
s
s
a
l
c

r
o
f

l

e
d
o
m

l

a
c
i
t
a
m
e
h
t
a
m
c
i
t
s
a
h
c
o
t
S

n
o
i
t
a
z
i
m

i
t
p
o

t
s
o
c

l

a
t
o
t

d
n
a

e
m

i
t

d
a
e

l

f
o

t
c
a
p
m

i

e
h
t

i

e
n
m
a
x
E

l

y
p
p
u
s

a

n
o

t
s
o
c

s
n
o
i
s
s
i
m
e

n
o
b
r
a
c

.

k
r
o
w
t
e
n

i

n
a
h
c

.
l

a

t
e

r
a
k
r
a
S

)
4
2
0
2
(

l

a
c
i
t
a
m
e
h
t
a
m
e
d
a
r
t
-
d
n
a
-
p
a
C

d
n
a

t
n
e
m
p
o
e
v
e
d

l

l

e
d
o
m

n
o
i
t
a
z
i
m

i
t
p
o

-
d
n
a
-
p
a
c

h
g
u
o
r
h
t

n
o
i
s
s
i
m
e

n
o
b
r
a
C

i

d
e
n
m
r
e
t
e
d

s
a
w
m
s
i
n
a
h
c
e
m
e
d
a
r
t

.

d
e
z
i
m

i
t
p
o

d
n
a

)
3
2
0
2
(

.
l

a

t
e

r
a
K

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

5

---

<!-- PAGE 6 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

l

d
u
o
h
s

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
u

l

a
u
t
c
a

d
n
a

,
t
e
s
a
t
a
d

,

o
i
r
a
n
e
c
s

e
f
i
l
-
l
a
e
r

n
o

y
t
i
v
i
t
c
e
f
f
E

p
a
G

g
n
o
m
a

n
o
i
s
s
i
m
e

n
o
b
r
a
c

d
n
a

i

l

e
b
x
e
ﬂ

r
o
f

s
n
o
i
t
a
c
i
l

p
m

i

d
e
t
a
e
r
C

d
n
a
m
e
d

i

s
g
n
d
n
ﬁ

n
i
a
M

.

d
e
s
s
e
s
s
a

e
b

n
o
b
r
a
c
w
o
h

g
n
i
t
n
e
s
e
r
p

,

i

n
a
h
c

l

y
p
p
u
s

o
t

d
e
r
a
p
m
o
c

l

e
b
a
v

i

s
s
e

l

s
i

x
a
t

,
l

a
c
i
t
i
l

o
p

r
o

l

a
i
c
o
s

,
l

a
t
n
e
m
n
o
r
i
v
n
e

e
b

l

d
u
o
c

s
t
c
e
p
s
a

c
i
m
o
n
o
c
e

d
n
a

s
a

h
c
u
s

i

s
n
a
m
o
d

y
t
i
l
i

i

b
a
n
a
t
s
u
S

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
R

l

e
b
a
n
a
t
s
u
s

i

t
c
e
f
f
a

o
t

d
e
t
i
s
o
p

t
e

e
e
L
(

s
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
o
m
a

i

r
o
v
a
h
e
b

t
e
y

s
a
h

s
i
h
t

,
r
e
v
e
w
o
h
—
)
0
2
0
2

.
l

a

a

h
t
i

w
d
e
s
s
e
s
s
a

l

y
h
g
u
o
r
o
h
t

n
e
e
b

d
n
a

k
r
o
w
e
m
a
r
f

k
r
a
m
h
c
n
e
b

.
l

o
o
t

l

a
c
i
t
y
a
n
a

l

d
e
c
n
a
v
d
a

y
t
i
l
i

i

b
a
n
a
t
s
u
s

r
o
f

t
n
e
m
s
s
e
s
s
a

c
i
t
s
i
l

o
H

d
e
t
a
e
R

l

.

e
n
o
d

n
e
e
b

t
e
y

s
a
h

a

d
e
r
e
d
i
s
n
o
c

l

y
n
o

e
v
a
h

s
r
o
t
c
a
f

i

s
e
d
u
t
s

s
a
h

t
u
b

s
r
o
t
c
a
f

e
m
o
s

f
o

n
o
i
t
a
n
b
m
o
c

i

s
i
s
y
a
n
a

l

e
v
i
t
a
t
i
t
n
a
u
q

d
n
a

e
v
i
t
a
t
i
l

a
u
Q

t
u
b

,

d
e
r
e
d
i
s
n
o
c

n
e
e
b

e
v
a
h

s
l
o
o
t

e
r
o
m
e
s
u

o
t

d
e
t
s
e
g
g
u
s

e
v
a
h

i

s
e
d
u
t
s

.
t
n
e
m
s
s
e
s
s
a

c
i
t
s
i
l

o
h

l
l

a
r
e
v
o

o
n

y
t
l
e
v
o
N

.

n
o
i
s
s
i
m
e

l

i

i

a
m
n
m
d
e

l
l

o
r
t
n
o
c

e
m
o
S

.
t
n
e
m
s
s
e
s
s
a

l

a
c
i
t
y
a
n
a

l

t
n
e
c
e
r

i

e
n
h
c
a
m
e
s
u

o
t

d
e
t
s
e
g
g
u
s

e
v
a
h

r
e
h
g
h

i

e
v
a
h

,

s
l
e
d
o
m
n
o
i
t
a
c
ﬁ
i
s
s
a
l
c

d

l
i

u
b

l

p
e
h

o
t

l

e
b
m
e
s
n
e

i

g
n
n
r
a
e

l

d
n
a

r
e
ﬁ
i
s
s
a
C

l

t
s
e
r
o
F
m
o
d
n
a
R

k
r
o
w
t
e
N

l

a
r
u
e
N

l

a
i
c
ﬁ
i
t
r

A

:

l

e
b
m
e
s
n
E

i

g
n
n
r
a
e
L

i

e
n
h
c
a
M

i

s
t
n
a
n
m
r
e
t
e
d

i

r
o
v
a
h
e
b

l

e
b
a
n
a
t
s
u
s

i

s
n
o
i
t
a
u
q
e

t
s
o
c

l

a
t
o
t

e
v
i
t
c
e
p
s
o
r
P

y
r
o
t
n
e
v
n

i

d
n
a
h
-
n
o

h
t
i

w
n
o
i
t
a
e
r

l

n

i

d
e
y
o
p
m
e

l

s
a
w
n
o
i
t
a
z
i
m

i
t
p
o

.

s
r
e
d
r
o
k
c
a
b

d
n
a

)
s
(
d
o
h
t
e
M

l

—
o
o
T

l

a
c
i
t
y
a
n
A

l

d
e
c
n
a
v
d
A

s
d
o
h
t
e
M

f
o

t
n
e
m
s
s
e
s
s
a

n
o
i
s
s
i
m
e

n
o
b
r
a
C

)
s
(
e
v
i
t
c
e
j
b
O

.

i

n
a
h
c

l

y
p
p
u
s

l

e
b
a
n
a
t
s
u
s

i

s
s
e
s
s
a

o
t

d
e
m
a

i

y
d
u
t
s

s
i
h
T

e
v
i
t
c
e
j
b
O

)
d
e
u
n
i
t
n
o
c
(

1

e
l
b
a
T

6

)
5
2
0
2
(

r
a
k
r
a
S

d
n
a

a
h
d
i
r

M

e
c
n
e
r
e
f
e
R

y
d
u
t
s

s
i
h
T

m
o
r
f

e
d
a
m

l

e
r
a
p
p
a

g
n
i
s
a
h
c
r
u
p

r
o
f

l

a
t
n
e
m
n
o
r
i
v
n
e
-
o
r
p

d
e
h
s
i
l

b
a
t
s
e

e
h
t

i

g
n
d
n
e
t
x
e

e
t
s
a
w
c
i
t
s
a
p

l

f
o

y
r
o
e
h
t

e
h
t

m
o
r
f

l

e
d
o
m

e
h
t

g
n
i
t
s
e
t
—
r
o
v
a
h
e
b

i

i

r
o
v
a
h
e
b

d
e
n
n
a
p

l

d
e
n
n
a
p

l

f
o

y
r
o
e
h
t

y
t
i
l
i

i

b
a
n
a
t
s
u
s

i

.
r
o
v
a
h
e
b

e
m
o
c
r
e
v
o
d
n
a

,

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
f
o
y
c
a
r
u
c
c
a

.

s
i
s
y
a
n
a

l

l

a
c
i
t
s
i
t
a
t
s

e
t
a
i
r
a
v
i
t
l
u
m

d
n
a

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
t

f
o

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

ecological footprint, and spread environmentally friendly beha-
viors. Lastly, the economic aspect pertains to ﬁnancial structures
and processes that promote the growth and development of the
economy (Waheed et al. 2023). Studies that focus on economic
sustainability incorporate understanding ethical ﬁnancial prac-
tices, settling ﬁnancial obligations, and making socially conscious
investments (Sedliačiková et al. 2020).

With the aforementioned notions on the sustainability aspect
and TPB, this paper aimed to establish the Sustainability Theory
of Planned Behavior (STPB) to assess sustainable behavior
determinants for purchasing apparel made from plastic waste
extending the model and concept from studies (German et al.
2022a; Abusaﬁeh and Razem 2017; Abdel-Shafy and Mansour
2018; Gansser and Reich 2023; Waheed et al. 2023; Sedliačiková
et al. 2020). In addition, the objective of the study was to assess if
the developed model could be established in the ﬁeld of consumer
behavior among clothing industries using a machine learning
algorithm; similar to the studies of German et al. (2022a) on
consumer
transportation intention and
Gumasing et al. (2023) on technology intention and adoption.
This study aimed to answer several research questions:

behavior

among

1. Can the STPB framework holistically assess sustainable
behavior determinants for purchasing apparel made from
plastic waste?

2. How can machine learning ensemble be employed to create

a classiﬁcation model for behavioral analysis?

3. How accurate could the model test out the dataset for
forecasting and modeling sustainability and behavioral
domains?

4. What implications, both theoretical and practical, could be

built from the output of the study?

5. How can the study be extended based on the output and

limitations?

As a contribution, this study could be beneﬁcial to business
industries considering that this can give knowledge on how the
customers’ purchase intention can impact sustainability aspects
among apparel. The results could provide implications for sus-
tainable practices among apparel industries. This study can also
be advantageous for the government as its ﬁndings can aid in
recognizing customer needs and preferences, as well as encourage
sustainable production and consumption to create programs and
policies for sustainable apparel that are more effective. The
ﬁndings can contribute to the community, considering that this
can promote environmentally friendly behaviors in order to
minimize pollution and preserve natural resources. Customer
awareness and knowledge of
sustainable fashion could be
increased, which might encourage them to buy more sustainable
apparel. Lastly, this study can beneﬁt future generations by
identifying possible constraints to sustainable fashion using the
proposed theory, which could be utilized to inform the devel-
opment of strategies that will boost consumer demand for and
acceptance of sustainable behavior shortly.

Literature review and hypotheses
Research framework and hypothesis build-up. Figure 3 illus-
trates the established STPB model,
the research framework
employed in this study, to determine the purchase intentions of
Filipino customers while purchasing clothing made of recycled
plastic. The STPB framework in this study has been considered as
an extension of the pro-environmental planned behavior (PEPB)
from a sustainable transportation perspective (German et al.
2022a; Ong et al. 2023). It is an expanded version of the PEPB
integrating fully all sustainability
from TPB (Ajzen 1991),
factors: Perceived
domains. The model

included

eight

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 7 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

Fig. 3 Theoretical framework.

Environmental Concern (PENC), Perceived Authority Support
(PAS), Subjective Norms (SN), Attitude (AT), Perceived Beha-
vioral Control (PBC), Customer Perceived Value (CPV), Beha-
vioral Intention (BI)—PEPB (German et al. 2022a), and the
additional Perceived Economic Concern (PECC). As explained in
the study of Ong et al. (2023), PECC is an important variable to
consider for full sustainability behavioral assessment. The suc-
ceeding section provides an outlook of the hypothesis build-up
since only PECC is a new addition.

Perceived economic concern (PECC) affecting behavioral domains.
PECC can be considered as a gauge of a customer’s inclination to
allocate additional funds towards sustainable products (Saricam
and Okur 2018). Various studies mentioned that customers assert
their readiness to buy sustainable clothing, even at a higher price.
However, there are uncertainties over whether they do so, making
their purchasing behavior contradict their claims (Gomes de
Oliveira et al. 2022). Another study also mentioned that con-
sumers who are concerned with environmental issues may not
always choose to purchase eco-friendly or sustainable products.
Those customers who claim to be concerned with environmental
issues might still not engage in pro-environmental behavior upon
purchasing products since sustainable products come at a higher
cost compared to conventional alternatives (Dangelico et al.
2022), especially evident in the Philippines (Ong et al. 2023). It
was mentioned that consumers are frequently willing to invest

more when the real value of a product exceeds their perceived
value. However, according to the study of Saricam and Okur
(2018), some research efforts aimed to establish the extent to
which customers would be willing to pay an extra cost for sus-
tainable fashion products. Moreover, consumers would be ready
to spend more on clothing manufactured from organic materials.
The study conducted by Ferioli et al. (2022) and Park and Lin
(2020) also indicated that customers exhibit a greater willingness
to pay elevated prices for environmentally friendly and sustain-
able clothing products. To which, a strong positive correlation
was found between customers’ willingness to spend more (PECC)
on sustainable clothing and AT for sustainable apparel (Nam
et al. 2017). The study also mentioned that customers with greater
environmental concerns tend to show a higher inclination toward
purchasing sustainable clothing products. A study conducted by
Roh et al. (2022) showed that PECC has a positive value on both
SN and PBC, wherein the researchers discovered that the periods
when organic products had the most signiﬁcant development
were those in which people were considerably more inclined to
change their behavior to promote sustainability. However, Ong
et al. (2023) expressed that when too expensive technology is
being sold, PECC will not be signiﬁcant among buying behavior
due to price and general economic concerns. It was explained that
the more beneﬁt and cost-saving a technology is, the more
inclined people will be to purchase. In terms of clothing and
apparel, the following were hypothesized:

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

7

---

<!-- PAGE 8 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

H1. Perceived Economic Concern has a signiﬁcant impact with

Subjective Norm.

H2. Perceived Economic Concern has a direct

relationship with Attitude.

signiﬁcant

H3. Perceived Economic Concern has a positive relationship

with Perceived Behavioral Control.

Perceived Environmental Concern (PENC) affecting behavioral
domains. PENC can be viewed as a measurement of how each
person perceives the effects on the environment (German et al.
2022a; Ong et al. 2023). According to Bickart and Ruth (2012),
the degree to which a consumer cares about the environment is a
signiﬁcant personal characteristic because it is linked to their
knowledge and motivation regarding environmental matters.
Studies have shown that consumers’ intentions upon purchasing
recycled and upcycled apparel products are positively impacted
by environmental concerns (Park and Lin 2020). In a study
conducted by Lin et al. (2017), the researchers discovered that
PENC has a positive value on both SN and PBC. In contrast, there
is little association between PENC and AT in environmental
impact assessment (EIA). This correlation shows that customers’
PENC was adversely affected when they were required to actively
engage in an environmental activity. In the Philippines, it was
established that the community is now more inclined to pro-
environmental behavior, leading to sustainable options (Ong et al.
2023). Therefore, this study identiﬁed the following hypotheses:
H4. Perceived Environmental Concern has a positive relation-

ship to Subjective Norm.

H5. Perceived Environmental Concern has a positive relation-

ship with Attitude.

H6. Perceived Environmental Concern has a positive relation-

ship with Perceived Behavioral Control.

Perceived authority support (PAS) affecting behavioral domains.
PAS relates to an individual’s comprehension of the resources,
laws, regulations, and potentially additional processes provided
by a government or authoritative entity to support individuals in
adopting a speciﬁc behavior (Nadlifatin et al. 2016). According to
the study of Lin et al. (2017), PAS positively inﬂuences the
domains of TPB among citizens’ Desire and readiness to engage
in an EIA. Considering the viewpoint of AT, these regulations
offer regular opportunities for engagement and a variety of
communication channels to enhance the positive sentiments of
citizens. From the SN perspective, the regulations serve as a
means to foster cooperation between the project developer and
the broader community. From the PBC perspective, the regula-
tions offer residents the chance to participate in the EIA process
under the most convenient conditions (Ong et al. 2023). There-
fore, this study identiﬁed the following hypotheses:

H7. Perceived Authority Support has a positive relationship to

Subjective Norm.

H8. Perceived Authority Support has a positive relationship to

Attitude.

H9. Perceived Authority Support has a positive relationship with

Perceived Behavioral Control.

TPB domains affecting customer perceived value. AT pertains to
the evaluation of an individual concerning the behavior in
question, ranging from a positive assessment to a negative one
(Soorani and Ahmadvand 2019). On the other hand, SN refers to
the perception of societal inﬂuence, either encouraging partici-
pation in the behavior or discouraging it (Rausch and Kopplin
2021). In other words, SN consists of one’s opinions on whether
close friends or family members should participate in the beha-
vior. PBC relates to the perception of how easy or challenging it is
to perform the activity, encompassing past experiences and

expected obstacles, inﬂuenced by one’s self-belief and judgment of
their capability (Xu et al. 2022). PBC can be utilized to forecast
behavior in a straightforward manner as well as indirectly inﬂu-
ence behavior through intentions relating to sustainability beha-
viors (Ong et al. 2023; Soorani and Ahmadvand 2019). In the
study of Saricam and Okur (2018), both SN and AT have a sig-
niﬁcant direct relationship with CPV. Furthermore, the study of
Savari and Gharechaee (2020), Qi and Ploeger (2019), and Lin
et al. (2017) mentioned that TPB domains signiﬁcantly had a
substantial effect on customers’ purchasing intentions and played
a signiﬁcant role in inﬂuencing them. Behavioral domains in the
Philippine context have been established by German et al. (2022a)
to affect CPV. Therefore, this study identiﬁed the following
hypotheses:

H10. Subjective Norm has a positive relationship to Customer

Perceived Value.

H11. Attitude has a direct signiﬁcant relationship to Customer

Perceived Value.

H12. Perceived Behavioral Control has a positive relationship to

Customer Perceived Value.

Customer perceived value (CPV) affecting behavioral intentions. In
this study, CPV illustrates the customer’s holistic evaluation of a
product’s utility, determined by their perception of what has been
provided and what they have received (Uzir et al. 2021). It is the
outcome of how consumers feel prior to, throughout, and after a
purchase has been made (Al-Mashraie et al. 2020; Savari and
Gharechaee 2020). A study by Dangelico et al. (2022) discovered
that CPV is the best indicator of consumers’ intentions to pur-
chase sustainable apparel and their willingness to spend higher
prices for it, no matter whether eco-material is explicitly utilized.
This shows that in the general framework of sustainable clothing,
elevated CPV resulting from a product made with a particular
eco-friendly material enhances customers’ inclination to buy the
product, even at a higher price. The study ﬁndings of Dangelico
et al. (2022) aligned with ﬁndings from prior research on sus-
tainable clothing products (Chi et al. 2021). Numerous research
investigations have demonstrated that CPV exerts a signiﬁcant
and favorable impact on BI (Jalil et al. 2016; Liu et al. 2021).
Therefore, this study hypothesized that:

H13. Customer Perceived Value has a positive relationship to

Behavioral Intention.

analytical

learning algorithm as

Machine
tool. Recent
advancements in artiﬁcial intelligence (AI), big data, and machine
learning brought newly adapted methodologies for analysis. Ong
et al. (2023) explained that the application of machine learning as
an analysis tool in behavioral intention among smart transpor-
tation provided better output compared to the multivariate ana-
lysis counterpart study. This was because several path analyses
were present on the large model, creating a total of 18 hypotheses
in their study. In accordance, the study of German et al. (2022a)
that considered PEPB presented better accuracy for the nonlinear
relationship framework established with machine learning tech-
nique analyses. From their study, a total of 20 hypotheses were
considered in their study. Compared to their other study utilizing
higher-order structural equation modeling (SEM) analyses, both
generated similar output and could prove how machine learning
as another tool could be considered.

When dealing with multivariate analyses, studies such as that
of Fan et al. (2016) explained that the larger the framework, the
more path is needed to assess the target output. This usually
results in lower accuracy of relationship assessment due to errors
in the multiple paths needed to be met. Woody (2011) with the
same explanation posited that farther variables on the target

8

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 9 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

output may also result in an insigniﬁcant relationship. To which,
present studies such as that of Jamshidi et al. (2022) and Al-
Mashraie et al. (2020) expressed the advantages of using machine
learning techniques in analyzing nonlinear relationship frame-
works, which are mostly complex in nature. It was indicated that
these hybrid tools could present better output, higher accuracy,
and better predictive power. In terms of analyzing behavioral
intention among technology adoption,
it was presented that
machine learning had higher accuracy (Al-Mashraie et al. 2020;
Gumasing et al. 2023) and provided a better signiﬁcance level
with classiﬁcation techniques like neural networks and random
forest classiﬁer (RFC; Gumasing et al. 2023).

Methodology
Participants. This study assessed customers’
intentions and
behaviors regarding sustainable apparel. A total of 500 valid
responses were collected through an online survey using a con-
venience sampling approach. The sampling approach was utilized
to disseminate the online survey through various social net-
working sites and pages in order to procure a wide range of
respondents, since convenience sampling is a non-probability
sampling method where participants voluntarily choose to par-
ticipate after being informed about the study by the researcher
(Stratton 2021). The ﬁrst two pages/section of the questionnaire
contained a short introduction as well as a reference to the Data
Privacy Act and approval of the Ethics Committee (FM-RC-22-
01-01, approved on March 20, 2023). Followed by the demo-
graphic proﬁling of the respondents. Lastly, the STPB compo-
nents were then displayed after the demographic proﬁle was
completed. Presented in Table 2 are the participant demographic
characteristics, collected alongside the measured items.

According to the collected data,

it was observed that the
majority of participants were women (69.2%), while males made
up the remaining portion (30.8%). Regarding the distribution of
individuals aged 18 to 25 comprised the largest
age groups,
segment, making up (55.4%) of the sample, individuals below 18
comprised (14.4%), and those aged 26 to 35 years old constituted
around (13%), while the remaining participants were from older
age groups. In relation to marital status, a signiﬁcant proportion
identiﬁed as single (75.8%), followed by married individuals at a
rate of (20.2%), and both separated and widowed (2%). In terms
of residential areas, the majority of respondents, constituting
(80.6%), reside in urban areas, while (19.4%) hail from rural
regions Regarding employment status, the majority consists of
followed by employed individuals (31%);
students (59.2%),
unemployed individuals make up a smaller percentage at (5%),
while self-employed/business owners account for (4.8%). As for
educational level, the highest proportion attended college (40.6%),
closely followed by those who attended high school/senior high
school (37.4%). A signiﬁcant portion has completed college or
obtained graduate degrees (20.4%); lastly, only a small fraction
has attended grade school, with an occurrence rate of just (1.6%).
For the household size,
the majority of participants have
households consisting of 3–4 people (45.6%), followed by 5–6
people (26.4%), more than six people (15%), and ﬁnally, those
with households of 1–2 people
(13%). The majority of
participants fall below Php 10,000 (30.8%). Additionally, 23.4%
fall within Php 10,001–20,000, and 16.2% fall within Php
20,001–30,000. Those with an income above Php 50,000 account
for approximately 13. 8%, 10.2% had an income between 30,001
and 40,000, and 5.6% were between Php 30,001–40,000 and
between Php 40,001–50,000, respectively. Lastly,
for the fre-
quency of purchasing sustainable apparel, (33%) buy sustainable
apparel every 1–3 months. Additionally, a signiﬁcant percentage
purchase it every 3–5 months (24.8%), followed by those who buy

it every 6–9 months (23%). Lastly, a small portion of participants
make sustainable apparel purchases in 10–12 month intervals
(19.2%).

Questionnaire. The questionnaire consisted of two (2) parts:
respondents and
demographic information about potential
determinants of the STPB model, adapted from literature reviews.
Supplementary materials present
the STPB questionnaire,
employing a ﬁve-point Likert Scale ranging from 1 (Strongly
Disagree) to 5 (Strongly Agree) to evaluate the various determi-
nants that inﬂuence a user’s behavior when it comes to pur-
chasing apparel made from recycled plastic materials. The
adapted questionnaire
for buildup is presented in the
Supplementary File.

Machine learning algorithm (MLA). In this research, a machine
learning algorithm ensemble (MLE) was employed,
including
artiﬁcial neural network (ANN) and RFC, which were employed
to properly assess the latent variables at once. According to the
study by Ong et al. (2022), it was mentioned that using a machine
learning ensemble was much more efﬁcient in analyzing the
aspects inﬂuencing human behavior concerning how people uti-
lize technology compared to traditional and multivariate analysis
such as SEM. From their study regarding nuclear power plant
reopening adoption among consumers, the SEM analysis proved
higher signiﬁcance on the close variable relationship on the target
object. Utilizing MLE, they were able to provide insight into how
(1) the basic decision tree showed low accuracy rates compared to
RFC, and (2) that farther variables were more signiﬁcant com-
pared to those close to the target output. They were able to prove
that classiﬁcation techniques such as RFC provided better accu-
racy output since it generates the most probable model every
iteration as compared to the random generation when the basic
decision tree is used. Their study also justiﬁed the explanation
presented by Fan et al. (2016) and Woody (2011)—the farther the
variable, the little effect it has on the target output signiﬁcance
level. In addition, SEM is limited to smaller frameworks or
smaller path analyses for better predictive power.

Moreover, a comparison of different classiﬁcation techniques
was employed by Ong et al. (2024). They were able to present that
RFC and ANN outperformed other classiﬁcation modeling
there was a signiﬁcant difference
techniques. For example,
between XGBoost and LightGBM compared to other algorithms.
The accuracy rate obtained was lower, with higher mean square
errors. This delineates that there needs further improvement on
other classiﬁcation techniques before it could be generalized for
use in behavioral
It could be deduced that RFC
overpowered basic decision trees, XGBoost, and LightGBM, even
CATBoost, among others. Studies have also proven that these
classiﬁcation techniques using MLE may also overpower even the
advanced multivariate tools like SEM and multiple regression
analyses (Öztürk and Başar 2022).

studies.

It could be seen among recent studies that little to no studies
have used the MLE to evaluate the factors affecting consumers’
behavioral intention upon buying sustainable apparel or sustain-
able behavior in general. Most just focused on technology and its
acceptance (Ong et al. 2022), health behavior (Gumasing et al.
2023), transportation (German et al. 2022a; Ong et al. 2023), and
adoption (Milani et al. 2020) to name a few. Additionally, studies
show that in comparison to SEM (German et al. 2022a; Ong et al.
2022; Ong et al. 2023), machine learning algorithms can produce
predictions that are more accurate and models that work more
effectively (Bossi et al. 2022). Furthermore, both approaches are
capable of handling huge numbers of variables and datasets for

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

9

---

<!-- PAGE 10 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

Table 2 Respondents demographic proﬁle.

Characteristics

Category

N

%

Gender

Age

Status

Area of residence

Employment

Education level

Household size

Total Monthly Net Income/
Allowance

Frequency of buying
apparels made from
recycled plastic materials

154
30.8%
Male
346 69.2%
Female
500 100%
Total
14.4%
72
Below 18 years old
18–25 years old
55.4%
277
26–35 years old
13%
65
36–45 years old
9%
45
46–55 years old
4%
20
56–65 years old
2.8%
14
66 years old and above 7
1.4%
500 100%
Total
75.8%
379
Single
20.2%
101
Married
2%
10
Separated
10
Widowed
2%
500 100%
Total
403 80.6%
Urban
97
Rural
19.4%
500 100%
Total
59.2%
296
Student
5%
25
Unemployed
31%
155
Employed
4.8%
24
Self-Employed/
Business Owner
Total
Finished college or
graduate degree
Attended college
Attended high school/
senior high school
Attended grade school
Total
1–2 people
3–4 people
5–6 people
Above 6 people
Total
Less than 10,000
10,001–20,000
20,001–30,000
30,001–40,000
40,001–50,000
Above 50,000
Total
At least every 1–3
months
3–5 months
6–9 months
10–12 months
Total

8
1.6%
500 100%
65
228 45.6%
26.4%
132
75
15%
500 100%
30.8%
154
23.4%
177
16.2%
81
10.2%
51
5.6%
28
69
13.8%
500 100%
165

24.8%
124
23%
155
96
19.2%
500 100%

500 100%
20.4%
102

203 40.6%
37.4%
187

33%

13%

the development
(Wendorf 2002).

and evaluation of

complicated theories

Various kinds of machine learning algorithms exist, with
classiﬁcation tools being commonly utilized for recognizing
patterns. A study conducted by Ong et al. (2022) stated how
MLAs like RFC, as well as ANN, have become widely recognized
in the ﬁeld of human factors for evaluating human behavior.
However, a study conducted by Jamshidi et al. (2020) emphasized
that differences of opinion may arise regarding the utilization of
artiﬁcial intelligence and machine learning depending on how
they are applied as their utilization heavily relies on input from
users, individual behavior, and interaction among human roles.
To this, they responded by saying that data scientists are in charge
of the code and that people who write the algorithm should be in

charge of highlighting its positive features and deﬁning its limits.
Despite this, numerous studies have raised questions about the
efﬁcacy of machine learning when used independently for
measurement and prediction, or when combined with other
statistical and multivariate techniques in hybrid approaches.

Random forest classiﬁer (RFC). The RFC is among the many
machine learning algorithms commonly employed for classiﬁca-
tion tasks. It is a classiﬁcation model which takes into account a
straightforward algorithm featuring high prediction accuracy. The
study of Chen et al. (2019) mentioned the efﬁciency of RFC in
creating superior classiﬁcation models compared to a standard or
basic decision tree, as RFC consistently generates the most
accurate tree every iteration. According to related studies (Ger-
man et al. 2022a; Gumasing et al. 2023; Ong et al. 2022; Ong et al.
2023), RFC could be employed for the categorization of human
factors that affect how well an application is used and adapted or
how consumers behave. It was shown that RFC is among the
most effective tools for analyzing the factors affecting peoples’
decisions.

Adapted from the aforementioned studies, several factors were
optimized in order to construct the optimal tree when RFC is
employed within the Python Integrated Development Environ-
ment, Spyder v5.0. Similarly, the sklearn package was integrated.
To which,
tree depths between 5 and 7 were taken into
consideration, as well as criterion factors such as entropy or
Gini criteria, training-testing ratios spanning from 60:40 to 90:10,
and splitter choices including random or best. Each combination
was one of every parameter between tree depth, criterion, splitter,
and ratios. This study has therefore analyzed a total of 4800
iterations upon conducting 100 runs per combination.

Artiﬁcial neural network (ANN). ANN contains a more intricate
computation and algorithm in contrast with other MLAs. ANN
comprises neurons and layers that are connected by arcs, which
convert input into output by means of an activation function
(Abolghasemi et al. 2020). ANNs can analyze nonlinear models
and may give more realistic answers to issues that arise in real life,
and it is also capable of generating predictions, which are fre-
quently utilized in prediction areas since they produce more
signiﬁcant outcomes compared to traditional methods (Güven
and Şimşir, 2020). According to Jamshidi et al. (2022) and Alam
et al. (2021), ANNs can be an effective classiﬁcation approach for
examining factors that have a substantial
impact on human
behavior. Most research endeavors typically commence with
ANNs as a starting point before delving into other forms of
neural networks like Deep Learning. It was mentioned that deep
learning might be taken into consideration if the accuracy and
complexity capacity of ANN provides a low output. Nevertheless,
when sufﬁcient predictive power is attained, ANN is adequate. In
contrast to complexity, general neural networks are regarded as
advanced algorithms already (German et al. 2022a; Jamshidi et al.
2022).

In order to categorize elements inﬂuencing human behavior,
ANN is currently used in combination or hybrid with SEM
(Rehman et al. 2022). Research has shown that the intricate
computations within this type of machine learning algorithm can
yield more precise results, surpassing the capabilities of SEM,
which attempts to simulate the transmission of messages among
neurons in the brain (Al-Mashraie et al. 2020). In a study by
Alam et al. (2021) a SEM-ANN hybrid was taken into account to
ascertain the variables inﬂuencing users’ perceptions of
the
usefulness of a mental health application. It has been demon-
strated that the outcomes of ANN could accurately anticipate
elements inﬂuencing human behavior. Furthermore, Kalinić et al.
(2021) employed ANN to assess customer happiness. They

10

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 11 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

showed how this kind of MLA can identify components
effectively even in the face of dataset noise and can emphasize
crucial variables even when nonlinear connections are present.

they explore various methods

To create the best model, the ANN parameters were also
optimized by using identical data pre-processing methods as RFC
with a parameter setting like training and testing ratios. Similarly,
studies by Kalinić et al. (2021), Li et al. (2022), and Jang and Xing
(2020) mentioned that
for
activating the hidden layer (tanh, relu, and softmax), and output
layer (softmax, sigmoid, swish). In addition, studies by Yousefza-
deh et al. (2021), Jena et al. (2020), and Eckle and Schmidt-Hieber
(2019) also mentioned that the optimization process also involved
considerations of optimizers such as Adam, RMSProp, and SGD.
In this study, the ANN algorithm was implemented using the
Spyder v5.0—Python Integrated Development Environment in
conjunction with Tensorﬂow, and the Keras package was
employed.

In this

Furthermore, the class was set up to encompass 5 indicators
that mirrored the dataset’s normal distribution, aligning with the
5-point Likert Scale survey responses.
the
parameters were derived from an analysis of various literature
sources and their combinations. A total of 27,000 iterations were
carried out over 150 epochs,
involving 10 runs for every
combination of three activation functions for the hidden layer,
three activation functions for the output layer, and three different
optimizers. This encompassed every conceivable combination,
starting from 10 nodes and gradually increasing until reaching
100 nodes within the hidden layer.

study,

Data pre-processing and optimization. The coefﬁcient was given a
threshold of 0.20, and a 0.05 p-value was necessary for accep-
tance. It was seen that any correlation coefﬁcient below the set
threshold did not present much signiﬁcance and would disrupt
the analysis (Ong et al. 2023). Therefore, the data cleaning pro-
cess in this study through the feature selection method considered
correlation analysis. To which the items were analyzed on the
rescaled target output, behavioral
items were
deemed signiﬁcant underwent data aggregation.

intention. All

Following related studies, a 60% accuracy threshold was
considered for this study to employ signiﬁcance on the relation-
ship (German et al. 2022a). The higher accuracy rate induced
better classiﬁcation modeling for predicting factors affecting
human factors and consumer behavior. The Taylor Diagram was
then utilized in this study to compare and assess the acceptability
of accuracy rates among MLEs used in the study. Gholami et al.
(2020) conducted a study that demonstrated the use of the Taylor
Diagram in evaluating model performance through its accuracy,
standard deviation, and correlation. In the study conducted, it
was determined that a Root Mean Square Error (RMSE) value
below 20% was within the satisfactory range. The RMSE
considered in the Taylor Diagram is
the centered RMSE
difference between the simulated accuracy output and observed
pattern output
from the MLE conducted. Additionally, a
correlation value exceeding 90% was regarded as being of
signiﬁcant importance.

Marketing 7P’s. After the machine learning algorithm has been
used and demographic information about the respondents has
been collected a marketing strategy based on the Marketing 7Ps
was developed. This tool included seven distinct elements, which
are Product, Price, Place, Promotion, Process, Physical Evidence,
and People. As all aspects of service marketing fall under the
umbrella of the 7Ps in the marketing mix, the concept of the 7Ps
may be used to reﬂect the complexity of sustainable clothing for
clothing companies (Ho et al. 2022). The Marketing 7Ps would

help companies, government, and even the society. Thus, in order
to enhance the competitive edge of marketers, the concept of 7 ps
may be more suitable when studying sustainable apparel from a
wider perspective.

Results
Random forest classiﬁer (RFC) results. The RFC output was
considered with the optimum parameters of gini and best at 90:10
testing and training ratio. With a 92% accuracy rate, this pre-
sented a signiﬁcant difference upon subjecting the results through
analysis of variance. The summarized output is presented in
Table 3, which is considered depth 6.

Figure 4 represents the optimum tree with RFC. It could be
deduced that the parent node identiﬁed CPV (X1) with a value of
less than or equal to −0.248 as a determining factor inﬂuencing
customers’ purchase intentions when purchasing apparel made
from plastic. Satisfying the parent node would involve consider-
ing the Subjective Norm (X3) with values less than or equal to
2.261. In addition, meeting this requirement would also consider
Perceived Economic Concern (X4), X3, and Attitude (X2),
ultimately resulting in an increased likelihood of customers
intending to purchase apparel made from plastic. However, if X1
did not meet the expectations, both PBC (X0) and X1 would be
taken into account. This would result in signiﬁcantly increased
purchasing intentions among customers buying plastic-made
apparel.

Conversely, if the parent node is not met, it will assess X0 with
values less than or equal to 1.081. Meeting this requirement
would involve considering X4, X1, X2, and X4 leading to very high
purchasing intentions for apparel made from plastic. If this
condition was not met, it would take into account X1 and X3,
resulting in signiﬁcantly elevated purchase intent. If the child
node did not meet the criteria, it would consider X3 and X4,
resulting in a high level of purchase intent.

Therefore, according to the results, PECC (X4) is the most
important variable that signiﬁcantly inﬂuenced people’s AT (X2),
SN (X3), and PBC (X0) to have high purchasing intentions. This
implies that CPV (X1) is a highly signiﬁcant factor affecting
purchasing intentions when it comes to purchasing apparel made
from plastic. In order to establish a distinct categorization of
hidden factors that
the RFC
impact behavioral
requires supplementary assistance from other machine learning
algorithms due to the diverse range of elements that still exist.
Chen et al. (2019) adopted various approaches in addition to
incorporating outcomes from the RFC in identifying pertinent
latent variables.

intentions,

Artiﬁcial neural network (ANN) results. Performing the ANN,
two integrated development environments were used to compare
the best parameters. Using MATLAB, the ANN output showed a
mean square error of 0.75212 for the validation considering the
Elu activation function, 1.0533 for Tanh, and 0.9336 for the
sigmoid function. On the other hand, the testing mean square
error results were 0.26379, 0.20594, and 0.21595, respectively.
Considering the parameters on Spyder v5.0, the accuracy rates
were 90.20%, 89.60%, and 84.40%. To which, the ﬁnal ANN
considered the Elu function as the best activation function
parameter, which was used in both the hidden and output layer
run at 150 epochs (Pradhan and Lee 2010). In accordance, the
80% training and 10 validation fold was considered. It was evi-
dent that the model (Fig. 5) was deemed acceptable with the
R-squared test value being 0.91 at 30 nodes in the hidden layer.
From the results, it could be seen that the input layer was the
different variables considered in this study (from STPB). Because
of the nonlinear relationship present, several nodes were needed

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

11

---

<!-- PAGE 12 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

for the optimum output to be achieved. Upon optimization, 30
nodes were needed to be analyzed in the neural network model
using the Elu Activation Function. As presented in Eq. (1) (Nanni
et al. 2022), Elu is an advance of the ReLU function where the
value lies at [0.1,0.3]. Similar to ReLU, the value of x when
positive lies on the negative region, while its y value would be
below zero (Nanni et al. 2022).

f xð Þ ¼ xifx > 0 else αðex (cid:2) 1Þ

ð1Þ

The utility of Elu as an activation function has been expressed
by related studies to provide a better accuracy rate when dealing
with a nonlinear relationship framework. This is because the
analysis provides a smooth result, implicating a better accuracy
rate when passing through nodes in the hidden layer. The
consequence of Elu providing negative values pushes
the
calculation to batch normalization, thus improving the learning
process of the neural network—creating higher accuracy rates and
better to be used with multiple paths, and large, nonlinear
frameworks (Kim et al. 2020; Xiangyang et al. 2023). However,
Elu has its disadvantages; one of which is that it can only be used
in the hidden layer and that it is computationally expensive.
Compared to the adopted studies, the current study has presented
positively high output when Elu was utilized. From other studies,
common results were obtained using sigmoid, tanh, and softmax
(German et al. 2022a; Gumasing et al. 2023; Ong et al. 2023; Ong
et al. 2022). This is because there are a greater number of paths

Table 3 Random forest classiﬁer results (Depth = 6).

Category

Best

Entropy
Standard deviation
Gini
Standard deviation

Random

Entropy
Standard deviation
Gini
Standard deviation

60:40

70:30

80:20

90:10

84.41
1.215
87.27
1.021

82.87

4.003

82.61

3.805

83.30
0.894
82.81
0.664

80.51

4.515
81.03
3.991

84.47

0.852

88.47

0.502

83.78
4.967

84.94

4.886

90.94

1.003

92.00
0.000

85.82

5.590

85.30

5.888

and a larger nonlinear relationship framework in this study
compared to theirs, and Elu could be the best ﬁt for the analysis.
To further validate the output, the validation rate was obtained
showing over (under)ﬁtting—Fig. 6. For the discussion section to
be more coherent, the SHAP package was considered to generate
the relative normalized score of
importance to rank the
signiﬁcance of each latent variable affecting behavioral intention
to consider sustainable apparel. Table 4 displays the importance
scores that have been normalized and will be discussed in the
following section. From the ﬁndings, CPV emerged as the most
prominent
latent variable, with the TPB domains of PBC,
attitude, and subjective norm following in order of signiﬁcance.
Perceived economic concern was also deemed to be signiﬁcant.
However, a low signiﬁcant level was seen of PENC and PAS
(near 60%).

Discussion
Based on the results, CPV stands out as the most crucial factor in
determining customers’ purchasing intention for plastic apparel,
accounting for 100%. PBC follows closely at 94.7%, while attitude
(AT) plays a substantial role with an inﬂuence of 87.4%. This
demonstrates the signiﬁcance of CPV in inﬂuencing customers’
intentions towards purchasing apparel made of plastic. CPV is
crucial in determining how inclined customers are toward pur-
chasing sustainable apparel products. CPV measures how
numerous beneﬁts consumers estimate they will obtain from
these items concerning the prices involved. Several important
aspects are taken into consideration when customers evaluate the
perceived value of sustainable apparel products. Brandão and
Costa (2021) indicated that a positive perceived value is linked to
a favorable attitude, increased social inﬂuence, and a sense of
empowerment in addressing obstacles responsible for purchasing
sustainable fashion.

PBC pertains to the idea that customers who perceive the value
of sustainable clothing products will likely feel more empowered
and conﬁdent in their ability to make purchases effectively. The
feeling of control arises when individuals believe that their deci-
sions align with what they consider valuable, boosting conﬁdence
in their capacity to make choices that promote sustainability. The
attitude of customers played a substantial role in inﬂuencing the
outcome. Customers who perceive value are more inclined
towards developing positive attitudes when buying apparel

Fig. 4 Optimum classiﬁcation model with RFC. X0 – Perceived Behavioral Control; X1 – Customer Perceived Value; X2 – Attitude; X3 – Subjective Norm;
X4 – Perceived Economic Concern.

12

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 13 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

Table 4 Normalized score of importance.

Latent variable

Importance

Normalized score of importance

CPV
PBC
AT
SN
PECC
PENC
PAS

0.234
0.222
0.205
0.193
0.189
0.183
0.167

100%
94.7%
87.4%
82.6%
80.6%
78.4%
71.5%

materials. Businesses and organizations can leverage the power of
social approval, peer inﬂuence, and the need for acceptance to
promote wider adoption of plastic apparel among consumers—
making them actively contemplate integrating such products into
their wardrobe choices. According to a study conducted by Zhang
et al. (2019), subjective social norms show a direct and positive
correlation with pro-environmental actions and have a positive
and noteworthy inﬂuence on the inclination to buy sustainable
clothing.

This leads us to the next important factor, the perceived eco-
nomic concern (PECC), accounting for 80.6% signiﬁcance. PECC
plays a crucial role in inﬂuencing customers’ intentions regarding
purchasing apparel made of plastic. Essentially, it refers to how
customers view and contemplate the ﬁnancial aspects associated
with these products. Customers often evaluate whether selecting
apparel made from plastic or other alternatives aligns with their
budgetary constraints and monetary priorities. They consider
various factors like initial purchase price, ongoing expenses, and
potential long-term savings. Therefore, if customers perceive that
opting for eco-friendly options such as clothing made from
plastics is economically viable and can lead to cost reductions or
other ﬁnancial advantages over time, they are more inclined to
foster favorable attitudes regarding the utilization of these pro-
ducts. According to a study by Ansu-Mensah (2021), consumers
who prioritize environmental concerns are willing to buy sus-
tainable products without reservation, even if it means paying a
higher price. Thus, it can be concluded that customers’ intentions
of purchasing sustainable products are affected by the cost of
sustainable products.

The following factor in the hierarchy is known as PENC,
accounting for 78.4% of its importance. PENC refers to custo-
mers’ understanding and sensitivity towards environmental
issues, signiﬁcantly inﬂuencing their choices and actions. Custo-
mers with a strong sense of PENC are more likely to express
strong intentions to purchase clothing items made from plastic
materials. Apparel crafted from plastics is often seen as an
effective solution for addressing environmental concerns by these
environmentally conscious individuals. This group prioritizes
preserving nature and considers reduced usage of plastic-based
options as a means to lessen their ecological impact or carbon
footprint. Such perception boosts their desire even further,
leading them to utilize such products to contribute positively
towards favorable environmental outcomes. In a study conducted
by Zhang et al. (2019), it was mentioned that previous research
has typically found a positive link between PENC and the pur-
chase intention to buy sustainable products. Additionally, the
study demonstrated a positive association between PENC and
both the inclination to buy sustainable clothing products and the
attitude toward purchasing them, demonstrating how concerned
individuals are with environmental issues and how eager they are
to support attempts to address them.

At 71.5%, the PAS ranks lowest among contributing factors on
the list. This indicates that customers show importance in
receiving support, recommendations, or endorsements from

Fig. 5 Optimum ANN classiﬁcation model.

Fig. 6 Validation loss rate.

products made from plastic materials. They perceive these pro-
ducts as environmentally friendly and consider them their pre-
ferred choices for which they would willingly spend extra money
on sustainable clothing. Brandão and Costa (2021) mentioned
that attitude and perceived value are associated with one another.
The effects of these actions have an impact on how consumers
behave. Therefore, having a strong understanding of the envir-
onment may result in a positive attitude (AT) and more sig-
niﬁcant customer behavioral control (PBC) over the challenges of
achieving sustainable apparel consumption.

SN plays a signiﬁcant role, accounting for 82.6%. SN have a
signiﬁcant inﬂuence on shaping consumer behavior, particularly
with social and peer norms strongly affecting individuals’ pur-
chasing intention towards buying clothes made from plastic

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

13

---

<!-- PAGE 14 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

authoritative ﬁgures or institutions regarding their attitudes and
beliefs about purchasing sustainable apparel products. It suggests
that they value and trust advice or guidance from sources they
perceive as credible and having authority. Governments and
environmental organizations, according to the study by Lin and
Huang (2012), offer subsidies or promotions to encourage indi-
viduals to live sustainably. Additionally, it was suggested that for
green consumption to become the norm, both the government
and environmental organizations must actively promote it. Fur-
thermore,
the favorable connection between the educational
attainment of customers and their inclination to buy sustainable
clothing shows that governments should work towards creating
communities that are not just more educated but also more
mindful of the environment by investing in education (Dangelico
et al. 2022).

The signiﬁcance of every factor discussed in this paper lies in
their ability to exceed the 60% signiﬁcant level. The ranking was
determined solely based on the results derived from various
methods employed during data analysis of a survey completed by
participants. Overall,
the three most
important elements that needed to be emphasized in order to
encourage individuals to purchase sustainable apparel were CPV,
PBC, and attitude (AT).

it was concluded that

Theoretical implications. The TPB framework may be used for
evaluating consumers’ behavioral intentions when it comes to
making sustainable apparel purchases. Based on several studies,
the TPB framework can be an effective tool for understanding the
variables that affect a person’s intention when purchasing apparel
made from plastic. By considering these variables, interventions
may be created that encourage sustainable behavior and the
reduction of pollution resulting from plastic waste by means of
plastic recycling and clothing production. CPV was shown to
have the most signiﬁcant inﬂuence on how consumers felt they
had control over their behavior and how they perceived pur-
chasing products made of plastic, which has numerous important
theoretical implications. To begin with, it emphasizes the sig-
niﬁcant impact of external factors on shaping purchase intentions
and pro-environmental attitudes, especially when such factors are
related to understanding the worth of the products. This study
emphasizes the importance of external social variables in inﬂu-
encing individual decision-making and is consistent with well-
known behavioral concepts like the TPB. CPV has a beneﬁcial
impact on consumers’ intentions regarding buying and a readi-
ness to spend extra on products that support sustainable fashion.
CPV may therefore be used to assess company strategies toward
perceived sustainability and forecast consumer attitudes regard-
ing sustainable apparel. Consequently, the proposed STPB fra-
mework may evaluate individual behavior comprehensively with
regard to sustainability and sustainable behavior more holistically
than other extended TPB or PEPB frameworks.

Practical and managerial implications. To reduce plastic pol-
lution, evaluating the factors inﬂuencing customers’ behavioral
intentions toward purchasing sustainable apparel
is essential.
According to the study’s ﬁndings, Filipinos are willing to spend
extra on products that support sustainable fashion and are open
to buying clothes made of plastic. The community should con-
sider practical implications regarding people’s behavioral inten-
tions toward purchasing sustainable apparel. These implications
include initiatives and strategies the fashion industry may take to
promote a change and lean towards environmentally friendly
clothing. Companies may consider sustainable value propositions.
Businesses can develop this to improve the perception of the
sustainability of their business models. These propositions should

be in line with consumer values and preferences. From this study,
CPV—along with the functionality, consumer perception, brand
sustainability, desired values, and motivation as a strategy for
selling apparel, from plastic to apparel. Speciﬁcally,

Functionality Consumers’ perceptions of the usefulness of
sustainable clothing inﬂuence their decisions regarding their
purchase.

Consumer perception: By comprehending consumer percep-
tions and how they affect purchasing decisions, businesses may
create environmentally friendly apparel lines that satisfy demand.
Brand sustainability: The decisions consumers make for
purchasing sustainable clothing goods are favorably connected
with the importance of fashion brand sustainability.

Desired values: Recognizing what consumers want

from
environmentally friendly clothes may assist businesses in creating
sustainable clothing lines that satisfy demand.

Motivations for purchasing: Understanding customer moti-
vations for choosing eco-friendly clothes may help companies
create marketing plans
target
demographic.

resonate with their

that

By generating sustainable value propositions, gaining insight
into consumer perceptions and desired values, and implementing
marketing tactics
target market,
businesses may raise the perceived value of sustainable apparel
among their customers. Other suggestions are presented.

resonate with their

that

industries. Given the substantial environmental
For apparel
impact associated with the apparel industry, it is more crucial
than ever to use sustainable procedures. Sustainable fashion is not
merely a fashion trend but also an essential requirement for the
industry. Companies have to adapt to keep up with this per-
spective as customers take an active role in reducing fashion’s
negative environmental impacts. Ethical and sustainable fashion
has evolved from a trend to an economic imperative for the
apparel industry. The apparel sector could promote sustainable
clothing by implementing eco-design, supply chain sustainability,
consumer education, and waste management strategies. The
fashion industry must transition to sustainable manufacturing to
solve some of the social and environmental issues that societies
are now facing. Fast fashion must be reviewed considering the
environmental and social consequences it imposes on society, and
more sustainable business strategies are critically important.
Sustainable manufacturing techniques may be used through
ethical labor practices, especially using materials such as recycled
plastic bottles and promoting recycling and reuse. As more
fashion customers take up the cause of sustainability, apparel
manufacturers can advance and proﬁt from the opportunity.

For the government. Governments can play a signiﬁcant role in
advancing sustainable clothing by establishing rules, implement-
ing legislation, encouraging international collaboration, and
implementing policy interventions. Regulation may encourage
ethical, circular, and sustainable fashion, enabling businesses to
view a product’s worth as slowly lowering and boosting a circular
economy. Laws can promote sustainability in the textile and
fashion sectors by compelling companies to provide information
on their sustainability development and charging ﬁnes if they fall
short of goals. International collaboration may support initiatives
to change the apparel industry to one that is more sustainable.
Sustainable fashion consumption can be inﬂuenced by policy
changes, such as tax incentives for businesses that employ
recyclable materials or provide apparel repair services.

The results imply that companies, environmental advocacy
organizations, and political
leaders should consider utilizing
authoritative support to promote sustainable clothing. This may
include pursuing partnerships or endorsements from reputable

14

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 15 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

people or organizations, displaying certiﬁcates or stamps of
approval, or actively advertising the potential compatibility of
their goods with reliable recommendations. By doing this,
companies can increase consumers’ positive views and conﬁdence
regarding purchasing environmentally friendly products, such as
apparel made of plastic, which can encourage more people to
engage in environmentally friendly behaviors.

Conclusion
This study explored the factors that impact individuals’ beha-
vioral intentions towards purchasing apparel made from plastic.
The research utilized two machine learning methods, speciﬁcally
RFC and ANN and were employed to analyze the collected data.
The ﬁndings from this research indicated that CPV and PBC were
the main variables inﬂuencing consumers’ behavioral intention
toward purchasing apparel made of plastic. Customers who
perceive value are more likely to establish positive attitudes (AT)
while purchasing sustainable apparel products. The feeling of
control arises when individuals believe that their decisions align
with what they consider valuable, boosting conﬁdence in their
capacity to make choices that promote sustainability. The attitude
of customers played a substantial role in inﬂuencing the outcome.
Customers who perceive value are more inclined to develop
positive attitudes when buying apparel products made from
plastic materials. They perceive these products as environmen-
tally friendly and consider them their preferred choices for which
they would willingly spend extra money on sustainable clothing.
Moreover, customers’ inclination towards purchasing sustain-
able clothing is directly and positively inﬂuenced by social norms
(SN), which also have a positive and substantial effect on other
pro-environmental behaviors. Customer intentions were also
affected by perceived economic concern (PECC) because mone-
tary factors were taken into consideration when making pur-
chasing decisions towards sustainable products. Customers with
high environmental awareness were more inclined towards pur-
chasing sustainable products as a strategy to reduce their envir-
onmental
impact and promote environmental preservation,
which increases the importance of PENC. Apparel crafted from
plastics is often seen as an effective solution for addressing
environmental concerns by these environmentally conscious
individuals. This group prioritizes preserving nature and con-
siders reduced usage of plastic-based options as a means to lessen
impact or carbon footprint. Such perception
their ecological
boosts their desire even further,
leading them to utilize such
products to contribute positively towards favorable environ-
mental outcomes.

Finally, PAS refers to how important customers ﬁnd it to have
their attitudes and ideas about purchasing sustainable clothing
products supported by or endorsed by reputable individuals or
institutions. It was suggested that for green consumption to
become the norm, both the government and environmental
organizations must actively promote it. Furthermore, the favor-
able connection between the educational attainment of customers
and their inclination to buy sustainable clothing shows that
governments should work towards creating communities that are
not just more educated but also more mindful of the environment
by investing in education.

In summary, it was found that every single one of the afore-
mentioned variables was signiﬁcant and had a weight of more
than 60%. The study emphasized the crucial roles played by
perceived value, behavioral control, consumer attitude, economic
considerations, environmental concerns, and social norms in
determining sustainable consumption behavior. Additionally, it
provided important details on the complex interactions between
intentions
these variables

that affect customers’ behavioral

regarding purchasing sustainable apparel. This study highlights
how important it is to take these factors into consideration when
establishing marketing strategies and initiatives intended to raise
awareness of products made with plastic in order to make a
positive contribution towards the advancement of a sustainable
environment to reduce plastic pollution. Furthermore, it opens up
the opportunity to conduct further investigation and examination
of these factors by employing advanced machine-learning meth-
odologies and larger sets of data to enhance our understanding of
sustainable consumer behavior. For ANN, either MATLAB or
Python codes could be utilized and could still provide similar
ﬁndings.

Limitations and future research. The study could be used and
expanded to evaluate the sustainability of the apparel industry in
various nations as well as the customers’ behavioral intentions
toward purchasing sustainable apparel. It does, however, have
certain restrictions. First, in terms of demographics, the largest
portion of survey participants (55.4%) were within the age range
of 18 to 25. The research made an effort to include people of all
ages; however, because social media platforms were used to gather
data, the majority of participants were under 30. In addition, since
respondents were simply asked to categorize their region of resi-
dence as rural or urban, the study was unable to determine the
exact places of residence of the respondents. The speciﬁc coordi-
nates of the respondents’ locations may have affected the relative
importance of various elements, which led to a different view of
customer purchasing behavior. Future researchers might improve
this by utilizing a more diverse sample procedure and ensuring
that various demographic characteristics are considered in their
studies. In accordance, real-life testing of model and results could
be developed when pre- and post-purchase evaluation and data
collection is employed. This could create a better predictive model.
Moreover, the study was unable to take into account and
distinguish between online and in-person purchases of sustainable
apparel. This could enhance the total scope and depth since it
would need to explore deeper into the analysis of a person’s
intentions when purchasing a particular service or product.
the study was unable to relate the respondent’s
Second,
demographics to their behavior, which would have provided a
more comprehensive overview of their behavioral intentions when
it comes to purchasing sustainable apparel. Future researchers are,
therefore, encouraged to offer new perspectives on the subject
matter. The ﬁndings, metrics, and questionnaires may be used by
future researchers to conduct additional studies and to apply new
methods and ideas in order to come up with new perspectives and
comprehension regarding customer behavioral intentions toward
purchasing sustainable apparel. Lastly, future research could look
into the role played by customer satisfaction in environmentally
friendly purchasing behaviors by concentrating on consumers
who have ﬁrst-hand experience with sustainable clothes.

Data availability
The datasets generated during and/or analyzed during the current
study are available from the corresponding author on reasonable
request.

Received: 2 July 2024; Accepted: 2 June 2025;

References
Alam MM, Alam MZ, Rahman SA, Taghizadeh SK (2021) Factors inﬂuencing
health adoption and its impact on mental well-being during COVID-19
pandemic: a sem-ann approach. J Biomed Inform 116:103722. https://doi.
org/10.1016/j.jbi.2021.103722

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

15

---

<!-- PAGE 16 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

Abdel-Shafy HI, Mansour MSM (2018) Solid waste issue: sources, composition,
disposal, recycling, and valorization. Egypt J Pet 27(4):1275–1290. https://doi.
org/10.1016/j.ejpe.2018.07.003

Abolghasemi M, Beh E, Tarr G, Gerlach R (2020) Demand forecasting in supply
chain: the impact of demand volatility in the presence of promotion. Comput
Ind Eng 142:106380. https://doi.org/10.1016/j.cie.2020.106380

Abusaﬁeh S, Razem M (2017) Human behavior and environmental sustainability:
promoting a pro-environmental behavior by harnessing the social, psycho-
logical and physical inﬂuences of the built environment. E3S Web Conf
23:02003. https://doi.org/10.1051/e3sconf/20172302003

Adıgüzel F, Donato C (2021) Proud to be sustainable: upcycled versus recycled
luxury products. J Bus Res 130:137–146. https://doi.org/10.1016/j.jbusres.
2021.03.033

Ajzen I (1991) The theory of planned behavior. Organ Behav Hum Decis Process

50(2):179–211. https://doi.org/10.1016/0749-5978(91)90020-t

Al-Mashraie M, Chung SH, Jeon HW (2020) Customer switching behavior analysis
in the telecommunication industry via push-pull-mooring framework: a
machine learning approach. Comput Ind Eng 144:106476. https://doi.org/10.
1016/j.cie.2020.106476

Ansu-Mensah P (2021) Green product awareness effect on green purchase inten-
tions of University Students’: an emerging market’s perspective. Futur Bus J
7(1). https://doi.org/10.1186/s43093-021-00094-5

Awoyera PO, Adesina A (2020) Plastic wastes to construction products: status,
limitations and future perspective. Case Stud Constr Mater 12. https://doi.
org/10.1016/j.cscm.2020.e00330

Bickart BA, Ruth JA (2012) Green eco-seals and advertising persuasion. J Advert

41(4):51–67. https://doi.org/10.1080/00913367.2012.10672457

Bossi F, Di Gruttola F, Mastrogiorgio A, D’Arcangelo S, Lattanzi N, Malizia AP,
Ricciardi E (2022) Estimating successful
internal mobility: a comparison
between structural equation models and machine learning algorithms. Front
Artif Intell 5. https://doi.org/10.3389/frai.2022.848015

Boyer RHW, Hunka AD, Vanacore E, Brauer HB (2025) Why some consumers
choose circular and others do not: the social practice of shopping for circular
garments. Circ Econ Sustain https://doi.org/10.1007/s43615-025-00527-1
Brandão A, Costa AG (2021) Extending the theory of planned behaviour to
understand the effects of barriers towards sustainable fashion consumption.
Eur Bus Rev 33(5):742–774. https://doi.org/10.1108/ebr-11-2020-0306
Brewer MK (2019) Slow fashion in a fast fashion world: promoting sustainability
and responsibility. Laws 8(4):24. https://doi.org/10.3390/laws8040024
Chang X, Xue Y, Li J, Zou L, Tang M (2019) Potential health impact of envir-
onmental micro‐ and Nanoplastics Pollution. J Appl Toxicol 40(1):4–15.
https://doi.org/10.1002/jat.3915

Chen J, Li Q, Wang H, Deng M (2019) A machine learning ensemble approach
based on Random Forest and radial basis function neural network for risk
evaluation of Regional Flood Disaster: a case study of the yangtze river delta,
China. Int J Environ Res Public Health 17(1):49. https://doi.org/10.3390/
ijerph17010049

Chi T, Ganak J, Summers L, Adesanya O, McCoy L, Liu H, Tai Y (2021)
Understanding perceived value and purchase intention toward eco-friendly
athleisure apparel: Insights from U.S. millennials. Sustainability 13(14):7946.
https://doi.org/10.3390/su13147946

Dangelico RM, Alvino L, Fraccascia L (2022) Investigating the antecedents of
consumer behavioral intention for sustainable fashion products: Evidence
from a large survey of Italian consumers. Technol Forecast Soc Change
185:122010. https://doi.org/10.1016/j.techfore.2022.122010

Gholami H, Mohamadifar A, Sorooshian A, Jansen JD (2020) Machine-learning
algorithms for predicting land susceptibility to dust emissions: the case of the
Jazmurian Basin, Iran. Atmos Pollut Res 11(8):1303–1315. https://doi.org/10.
1016/j.apr.2020.05.009

Gomes de Oliveira L, Miranda FG, de Paula Dias MA (2022) Sustainable practices
in slow and fast fashion stores: what does the customer perceive? Clean Eng
Technol 6:100413. https://doi.org/10.1016/j.clet.2022.100413

Grazzini L, Acuti D, Aiello G (2021) Solving the puzzle of sustainable fashion
consumption: the role of consumers’ implicit attitudes and perceived warmth.
J Clean Prod 287:125579. https://doi.org/10.1016/j.jclepro.2020.125579
Gumasing MJ, Ong AK, Sy MA, Prasetyo YT, Persada SF (2023). A machine
learning ensemble approach to predicting factors affecting the intention and
usage behavior towards online groceries applications in the Philippines.
Heliyon 9(10). https://doi.org/10.1016/j.heliyon.2023.e20644

Güven İ, Şimşir F (2020) Demand forecasting with color parameter in retail apparel
industry using artiﬁcial neural networks (ANN) and support vector machines
(SVM) methods. Comput Ind Eng 147:106678

H&M Group

(2023) Retrieved

from https://hmgroup.com/sustainability/

circularity-and-climate/materials/#:~:text=Recycled%20plastic&text=We%
20then%20use%20this%20plastic,avoiding%20harm%20to%20our%20planet
Hajishirzi R, Costa CJ, Aparicio M (2022) Boosting sustainability through digital
transformation’s domains and resilience. Sustainability 14(3):1822. https://
doi.org/10.3390/su14031822

Ho C-I, Liu Y, Chen M-C (2022) Factors inﬂuencing watching and purchase
intentions on live streaming platforms: from A 7PS marketing mix per-
spective. Information 13(5):239. https://doi.org/10.3390/info13050239
Jaheer Mukthar KP, Nagadeepa C, Selvaratnam DP, Pushpa A, Shukla N (2024)
Sustainable wardrobe: recycled clothing towards sustainability and eco-
friendliness. Discov Sustain 5(1). https://doi.org/10.1007/s43621-024-00358-4
Jalil NA, Fikry A, Zainuddin A (2016) The impact of store atmospherics, perceived
value, and customer satisfaction on behavioural intention. Procedia Econ
Financ 37:538–544. https://doi.org/10.1016/s2212-5671(16)30162-9

Jamshidi M(Behdad), Roshani S, Daneshfar F, Lalbakhsh A, Roshani S, Parandin F,
Malek Z, Talla J, Peroutka Z, Jamshidi A, Hadjilooei F, Lalbakhsh P (2022)
Hybrid deep learning techniques for predicting complex phenomena: a
review on Covid-19 AI 3(2):416–433. https://doi.org/10.3390/ai3020025
Jamshidi M, Lalbakhsh A, Talla J, Peroutka Z, Hadjilooei F, Lalbakhsh P,
Mohyuddin W (2020) Artiﬁcial Intelligence and Covid-19: deep learning
approaches for diagnosis and treatment. IEEE Access 8:109581–109595.
https://doi.org/10.1109/access.2020.3001973

Jang H-S, Xing S (2020) A model to predict ammonia emission using a modiﬁed
genetic artiﬁcial neural network: analyzing Cement mixed with ﬂy ash from a
coal-ﬁred power plant. Constr Build Mater 230:117025. https://doi.org/10.
1016/j.conbuildmat.2019.117025

Jena R, Pradhan B, Beydoun G, Nizamuddin, Ardiansyah, Sofyan H, Affan M
(2020) Integrated model for earthquake risk assessment using neural network
and analytic hierarchy process: Aceh Province, Indonesia. Geosci Front
11(2):613–634. https://doi.org/10.1016/j.gsf.2019.07.006

Jin X, Omar A, Fu K (2024) Factors inﬂuencing purchase intention toward recycled
apparel: evidence from China. Sustainability 16(9):3633. https://doi.org/10.
3390/su16093633

Kalinić Z, Marinković V, Kalinić L, Liébana-Cabanillas F (2021) Neural network
modeling of consumer satisfaction in Mobile Commerce: an empirical ana-
lysis. Expert Syst Appl 175:114803. https://doi.org/10.1016/j.eswa.2021.
114803

Eckle K, Schmidt-Hieber J (2019) A comparison of deep networks with ReLU
spline-type methods. Neural Netw

activation function and linear
110:232–242. https://doi.org/10.1016/j.neunet.2018.11.005

Kar S, Basu K, Sarkar B (2023) Advertisement policy for dual-channel within
emissions-controlled Flexible production system. J Retail Consum Serv
71:103077. https://doi.org/10.1016/j.jretconser.2022.103077

Evode N, Qamar SA, Bilal M, Barceló D, Iqbal HMN (2021) Plastic waste and its
management strategies for Environmental Sustainability. Case Stud Chem
Environ Eng 4:100142. https://doi.org/10.1016/j.cscee.2021.100142

Fan Y, Chen J, Shirkey G, John R, Wu SR, Park H, Shao C (2016) Applications of
structural equation modeling (SEM) in Ecological Studies: an updated review.
Ecol Process 5(1). https://doi.org/10.1186/s13717-016-0063-3

Ferioli M, Gazzola P, Grechi D, Vătămănescu E-M (2022) Sustainable behaviour of
B Corps fashion companies during Covid-19: a quantitative economic ana-
lysis. J Clean Prod 374:134010. https://doi.org/10.1016/j.jclepro.2022.134010
Fung Y-N, Chan H-L, Choi T-M, Liu R (2021) Sustainable product development
processes in fashion: supply chains structures and classiﬁcations. Int J Prod
Econ 231:107911. https://doi.org/10.1016/j.ijpe.2020.107911

Gansser OA, Reich CS (2023) Inﬂuence of the new ecological paradigm (NEP) and
environmental concerns on pro-environmental behavioral intention based on
the theory of planned behavior (TPB). J Clean Prod 382:134629. https://doi.
org/10.1016/j.jclepro.2022.134629

German JD, Ong AK, Perwira Redi AA, Robas KP (2022a) Predicting factors
affecting the intention to use a 3PL during the COVID-19 pandemic: a
machine learning ensemble approach. Heliyon 8(11). https://doi.org/10.1016/
j.heliyon.2022.e11382

Kim D, Kim J, Kim J (2020) Elastic exponential linear units for convolutional
neural networks. Neurocomputing 406:253–266. https://doi.org/10.1016/j.
neucom.2020.03.051

Kim I, Jung HJ, Lee Y (2021) Consumers’ value and risk perceptions of circular
fashion: comparison between secondhand, upcycled, and recycled clothing.
Sustainability 13(3):1208. https://doi.org/10.3390/su13031208

Kuah ATH, Wang P (2020) Circular economy and consumer acceptance: an
exploratory study in East and Southeast Asia. J Clean Prod 247:119097.
https://doi.org/10.1016/j.jclepro.2019.119097

Lee E-J, Choi H, Han J, Kim DH, Ko E, Kim KH (2020) How to “Nudge” your
consumers toward sustainable fashion consumption: An fmri investigation. J
Bus Res 117:642–651. https://doi.org/10.1016/j.jbusres.2019.09.050

Li M, Vanberkel P, Zhong X (2022) Predicting ambulance ofﬂoad delay using a
hybrid decision tree model. Socio-Econ Plan Sci 80:101146. https://doi.org/
10.1016/j.seps.2021.101146

Lin P-C, Huang Y-H (2012) The inﬂuence factors on choice behavior regarding
green products based on the theory of consumption values. J Clean Prod
22(1):11–18. https://doi.org/10.1016/j.jclepro.2011.10.002

Lin S-C, Nadlifatin R, Amna A, Persada S, Razif M (2017) Investigating citizen
intention on mandatory and voluntary Pro-Environmental

behavior

16

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

---

<!-- PAGE 17 -->

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

ARTICLE

programs through a pro-environmental planned behavior model. Sustain-
ability 9(7):1289. https://doi.org/10.3390/su9071289

Liu P, Li M, Dai D, Guo L (2021) The effects of social commerce environmental
characteristics on customers’ purchase intentions: the chain mediating effect
of customer-to-customer interaction and customer-perceived value. Electron
Commer Res Appl 48:101073. https://doi.org/10.1016/j.elerap.2021.101073

Magnier L, Mugge R, Schoormans J (2019) Turning ocean garbage into products –
consumers’ evaluations of products made of Recycled Ocean Plastic. J Clean
Prod 215:84–98. https://doi.org/10.1016/j.jclepro.2018.12.246

Milani L, Grumi S, Camisasca E, Miragoli S, Traﬁcante D, Di Blasio P (2020)
Familial risk and protective factors affecting CPS Professionals’ Child
Removal Decision: a decision tree analysis study. Child Youth Serv Rev
109:104687. https://doi.org/10.1016/j.childyouth.2019.104687

Mridha B, Sarkar B (2025) Implications of carbon policies for ﬂexible demand and
smart production with Random lead time demand under a sustainable supply
chain management. Environ Dev Sustain https://doi.org/10.1007/s10668-025-
06038-1

Nadlifatin R, Lin S-C, Rachmaniati Y, Persada S, Razif M (2016) A pro-
environmental reasoned action model for measuring citizens’
intentions
regarding ecolabel product usage. Sustainability 8(11):1165. https://doi.org/
10.3390/su8111165

Nam C, Dong H, Lee Y-A (2017) Factors inﬂuencing consumers’ purchase
intention of Green Sportswear. Fashion Textiles 4(1). https://doi.org/10.1186/
s40691-017-0091-3

Nanni L, Brahnam S, Paci M, Ghidoni S (2022) Comparison of different con-
volutional neural network activation functions and methods for building
ensembles for small to midsize medical data sets. Sensors 22(16):6129. https://
doi.org/10.3390/s22166129

Nguyen XH, Tran HL, Nguyen QH, Luu TP, Dinh HL, Vu HT (2020) Factors
inﬂuencing the consumer’s intention to buy fashion products made by recycled
plastic waste. Manag Sci Lett 3613–3622. https://doi.org/10.5267/j.msl.2020.6.032
Niinimäki K, Peters G, Dahlbo H, Perry P, Rissanen T, Gwilt A (2020) The
environmental price of Fast Fashion. Nat Rev Earth Environ 1(4):189–200.
https://doi.org/10.1038/s43017-020-0039-9

Nike Sustainability (2024) Retrieved from https://www.nike.com/sustainability
OECD (2022) Retrieved from https://www.oecd.org/environment/plastic-pollution-
is-growing-relentlessly-as-waste-management-and-recycling-fall-short.htm
Ong AK, Cordova LN, Longanilla FA, Caprecho NL, Javier RA, Borres RD, Ger-
man JD (2023) Purchasing intentions analysis of hybrid cars using random
forest classiﬁer and deep learning. World Electr Veh J 14(8):227. https://doi.
org/10.3390/wevj14080227

Ong AK, Prasetyo YT, Salazar JM, Erfe JJ, Abella AA, Young MN, Chuenyindee T,
Nadlifatin R, Ngurah Perwira Redi AA (2022) Investigating the acceptance of
the reopening bataan nuclear power plant: integrating protection motivation
theory and extended theory of planned behavior. Nucl Eng Technol
54(3):1115–1125. https://doi.org/10.1016/j.net.2021.08.032

Ong AK, Mendoza MC, Ponce JR, Bernardo KT, Tolentino SA, Diaz JF, Young MN
(2024) Analysis of investment behavior among Filipinos: integration of social
exchange theory (SET) and the theory of planned behavior (TPB). Phys A:
Stat Mech Appl 654:130162. https://doi.org/10.1016/j.physa.2024.130162
Öztürk OB, Başar E (2022) Multiple linear regression analysis and artiﬁcial neural
networks based decision support system for energy efﬁciency in shipping.
Ocean Eng 243:110209. https://doi.org/10.1016/j.oceaneng.2021.110209
Park HJ, Lin LM (2020) Exploring attitude–behavior gap in sustainable con-
sumption: comparison of recycled and upcycled fashion products. J Bus Res
117:623–628. https://doi.org/10.1016/j.jbusres.2018.08.025

Polyportis A, Mugge R, Magnier L (2022) Consumer acceptance of products made
from recycled materials: a scoping review. Resour, Conserv Recycling
186:106533. https://doi.org/10.1016/j.resconrec.2022.106533

Pradhan B, Lee S (2010) Landslide susceptibility assessment and factor effect
analysis: backpropagation artiﬁcial neural networks and their comparison
with frequency ratio and bivariate logistic regression modelling. Environ
Model Softw 25(6):747–759. https://doi.org/10.1016/j.envsoft.2009.10.016
Pranta AD, Tareque Rahaman Md, Reazuddin Repon Md, Shikder AA (2024)
Environmentally sustainable apparel merchandising of recycled cotton-
polyester blended garments: Analysis of consumer preferences and pur-
chasing behaviors. J Open Innov: Technol Mark Complex 10(3):100357.
https://doi.org/10.1016/j.joitmc.2024.100357

Provin AP, Dutra AR, de Sousa e Silva Gouveia IC, Cubas EA (2021) Circular
economy for fashion industry: use of waste from the food industry for the
production of Biotextiles. Technol Forecast Soc Change 169:120858. https://
doi.org/10.1016/j.techfore.2021.120858

Qi X, Ploeger A (2019) Explaining consumers’ intentions towards purchasing green
food in Qingdao, China: the Amendment and extension of the theory of planned
behavior. Appetite 133:414–422. https://doi.org/10.1016/j.appet.2018.12.004
Rausch TM, Kopplin CS (2021) Bridge the gap: consumers’ purchase intention and
behavior regarding sustainable clothing. J Clean Prod 278:123882. https://doi.
org/10.1016/j.jclepro.2020.123882

Rehman IH, Ahmad A, Akhter F, Aljarallah A (2022) A dual-stage SEM-Ann
analysis to explore consumer adoption of smart wearable healthcare devices. J
Glob Inf Manag 29(6):1–30. https://doi.org/10.4018/jgim.294123

Roh T, Seok J, Kim Y (2022) Unveiling ways to reach organic purchase: green
perceived value, perceived knowledge, attitude, subjective norm, and Trust. J
Retail Consum Serv 67:102988. https://doi.org/10.1016/j.jretconser.2022.102988
Saricam C, Okur N (2018) Analysing the consumer behavior regarding sustainable
fashion using theory of planned behavior. Text Sci Clothing Technol 1–37.
https://doi.org/10.1007/978-981-13-1265-6_1

Sarkar B, Fan S-KS, Pareek S, Mridha B (2024) Sustainable multi-biofuel pro-
duction with stochastic lead time and Optimum Energy Utilization under
ﬂexible manufacturing. Comput Ind Eng 193:110223. https://doi.org/10.1016/
j.cie.2024.110223

Sarkar B, Kar S, Basu K, Guchhait R (2022) A sustainable managerial decision-
making problem for a substitutable product in a dual-channel under carbon
tax policy. Comput Ind Eng 172:108635. https://doi.org/10.1016/j.cie.2022.
108635

Sarkar B, Kar S, Basu K, Seo YW (2023) Is the online-ofﬂine buy-online-pickup-in-
store retail strategy best among other product delivery strategies under
Variable lead time? J Retail Consum Serv 73:103359. https://doi.org/10.1016/
j.jretconser.2023.103359

Savari M, Gharechaee H (2020) Application of the extended theory of planned
behavior to predict Iranian farmers’ intention for safe use of chemical ferti-
lizers. J Clean Prod 263:121512. https://doi.org/10.1016/j.jclepro.2020.121512
Sedliačiková M, Aláč P, Moresová M (2020) How behavioral aspects inﬂuence the
sustainable ﬁnancial decisions of shareholders: an empirical study and pro-
posal for a relevant decision-making concept. Sustainability 12(12):4813.
https://doi.org/10.3390/su12124813

Shams M, Alam I, Mahbub MS (2021) Plastic pollution during COVID-19: plastic
waste directives and its long-term impact on the environment. Environ Adv
5:100119. https://doi.org/10.1016/j.envadv.2021.100119

Soorani F, Ahmadvand M (2019) Determinants of consumers’ food management
behavior: applying and extending the theory of planned behavior. Waste
Manag 98:151–159. https://doi.org/10.1016/j.wasman.2019.08.025

Stratton SJ (2021) Population research: convenience sampling strategies. Prehosp
Disaster Med 36(4):373–374. https://doi.org/10.1017/s1049023x21000649
Talan A, Tyagi RD, Surampalli RY (2020) Social dimensions of sustainability.

Sustainability 183–206. https://doi.org/10.1002/9781119434016.ch9

Testa F, Di Iorio V, Cerri J, Pretner G (2021) Five shades of plastic in food: which
potentially circular packaging solutions are Italian consumers more sensitive
to. Resour, Conserv Recycling
173:105726. https://doi.org/10.1016/j.
resconrec.2021.105726

Tezer A, Bodur HO (2019) The greenconsumption effect: how using green pro-
ducts improves consumption experience. J Consum Res 47(1):25–39. https://
doi.org/10.1093/jcr/ucz045

Tiseo I (2023) Retrieved from https://www.statista.com/statistics/1270902/ocean-

plastic-pollution-from-select-rivers-worldwide

Uzir MU, Al Halbusi H, Thurasamy R, Thiam Hock RL, Aljaberi MA, Hasan N,
Hamid M (2021) The effects of service quality, perceived value and trust in
home delivery service personnel on customer satisfaction: Evidence from a
developing country. J Retail Consum Serv 63:102721. https://doi.org/10.1016/
j.jretconser.2021.102721

Vishnoi SK, Mathur S, Agarwal V, Virmani N, Jagtap S (2025) What drives gen-
eration Z to choose Green Apparel? Unraveling the impact of environmental
knowledge, altruism and perceived innovativeness. Int J Sustain Eng 18(1).
https://doi.org/10.1080/19397038.2025.2473986

Waheed R, Sarwar S, Alsaggaf MI (2023) Relevance of energy, Green and blue
factors to achieve sustainable economic growth: empirical study of Saudi
Arabia. Technol Forecast Soc Change 187:122184. https://doi.org/10.1016/j.
techfore.2022.122184

Wendorf CA (2002) Comparisons of structural equation modeling and hierarchical
linear modeling approaches to couples’ data. Struct Equ Modeling: A Mul-
tidiscip J 9(1):126–140. https://doi.org/10.1207/s15328007sem0901_7
Woody E (2011) An SEM perspective on evaluating mediation: what every clinical
researcher needs to know. J Exp Psychopathol 2(2):210–251. https://doi.org/
10.5127/jep.010410

Xiangyang L, Xing Q, Han Z, Feng C (2023) A novel activation function of deep
neural network. Sci Program 2023:1–12. https://doi.org/10.1155/2023/3873561
Xu Y, Du J, Khan MA, Jin S, Altaf M, Anwar F, Sharif I (2022) Effects of subjective
norms and environmental mechanism on Green Purchase Behavior: an
extended model of theory of planned behavior. Front Environ Sci 10. https://
doi.org/10.3389/fenvs.2022.779629

Yousefzadeh M, Hosseini SA, Farnaghi M (2021) Spatiotemporally explicit earth-
quake prediction using Deep Neural Network. Soil Dyn Earthq Eng
144:106663. https://doi.org/10.1016/j.soildyn.2021.106663

Zhang B, Zhang Y, Zhou P (2021) Consumer attitude towards sustainability of fast
fashion products in the UK. Sustainability 13(4):1646. https://doi.org/10.
3390/su13041646

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

17

---

<!-- PAGE 18 -->

ARTICLE

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-05205-z

Zhang L, Fan Y, Zhang W, Zhang S (2019) Extending the theory of planned behavior
to explain the effects of cognitive factors across different kinds of green pro-
ducts. Sustainability 11(15):4222. https://doi.org/10.3390/su11154222

Zhang Z, Malik MZ, Khan A, Ali N, Malik S, Bilal M (2022) Environmental
impacts of hazardous waste, and management strategies to reconcile circular
economy and eco-sustainability. Sci Total Environ 807:150856. https://doi.
org/10.1016/j.scitotenv.2021.150856

Acknowledgements
This research was funded by University Directed Research for Innovation and Value
Enhancement (DRIVE).

Author contributions
Carmella Andrea L. Cabrera, Ardvin Kester S. Ong, John Francis T. Diaz, Maela Madel L.
Cahigas, Ma. Janice J. Gumasing: Conceptualization; Carmella Andrea L. Cabrera,
Ardvin Kester S. Ong, John Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice J.
Gumasing: Data curation; Carmella Andrea L. Cabrera, Ardvin Kester S. Ong, John
Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice J. Gumasing: Formal analysis;
Ardvin Kester S. Ong: Funding acquisition; Carmella Andrea L. Cabrera, Ardvin Kester
S. Ong, John Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice J. Gumasing: Inves-
tigation; Carmella Andrea L. Cabrera, Ardvin Kester S. Ong: Methodology; Ardvin Kester
S. Ong, John Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice J. Gumasing: Project
administration; Carmella Andrea L. Cabrera, Ardvin Kester S. Ong, John Francis T. Diaz:
Resources; Carmella Andrea L. Cabrera, Ardvin Kester S. Ong, John Francis T. Diaz,
Maela Madel L. Cahigas, Ma. Janice J. Gumasing: Software; Ardvin Kester S. Ong, John
Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice J. Gumasing: Supervision; Carmella
Andrea L. Cabrera, Ardvin Kester S. Ong, John Francis T. Diaz, Maela Madel L. Cahigas,
Ma. Janice J. Gumasing: Validation; Carmella Andrea L. Cabrera, Ardvin Kester S. Ong,
John Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice J. Gumasing: Visualization;
Carmella Andrea L. Cabrera, Ardvin Kester S. Ong, John Francis T. Diaz, Maela Madel L.
Cahigas, Ma. Janice J. Gumasing: Roles/Writing–original draft; Carmella Andrea L.
Cabrera, Ardvin Kester S. Ong, John Francis T. Diaz, Maela Madel L. Cahigas, Ma. Janice
J. Gumasing: Writing - review & editing.

Competing interests
The authors declare no competing interests.

standard of the 1964 Helsinki Declaration. The data entails no traceable information
among respondents and was kept in a secure database. This was approved by Dr.
Josephine D. German (committee member) and Dr. Michael N. Young (committee head)
on March 20, 2023.

Informed consent
Informed consent was obtained from all subjects through written form, involved in this
study (FM-RC-22-02-01) during the data collection process from March 27, 2023—
August 2023. In accordance, a conﬁrmation question of approval among respondents
were collected as the ﬁrst question in the online questionnaire to ensure approval.
Participants were assured that traceable information would not be collected, response
would be anonymous, and their data privacy will be secured.

Additional information
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1057/s41599-025-05205-z.

Correspondence and requests for materials should be addressed to Ardvin Kester S. Ong.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and reproduction in any
medium or format, as long as you give appropriate credit to the original author(s) and
the source, provide a link to the Creative Commons licence, and indicate if you modiﬁed
the licensed material. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other third party material
in this article are included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article’s
Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder. To view a copy of this licence, visit http://creativecommons.org/
licenses/by-nc-nd/4.0/.

Ethical approval
This study was approved by the Mapua University Research Ethics Committees (FM-RC-
22-01-01), following proper relevant guidelines curated by the university and the ethical

© The Author(s) 2025

18

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS |

(2025) 12:822  | https://doi.org/10.1057/s41599-025-05205-z

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

ARTICLE
OPEN
https://doi.org/10.1057/s41599-025-05205-z
Plastic to apparel: an analysis of sustainable
purchasing intention using a machine learning
ensemble
✉
Carmella Andrea L. Cabrera1, Ardvin Kester S. Ong 1,2 , John Francis T. Diaz3, Maela Madel L. Cahigas1 &
Ma. Janice J. Gumasing4
Theuseofplasticshasbecomeasignificantcomponentinmaintainingtheconvenienceand
suitability of modern lifestyles; however, a vast majority of the million tons of plastic man-
ufactured each year ends up in landfills, contributing to plastic pollution. With this, the
fashion industry has capitalized to create recycled products. Despite the proliferation and
continued presence of recycled and upcycle products, there still is a significant gap in the
sustainable purchasing behavior of consumers. This study aimed to identify, analyze, and
forecastthevariablesinfluencingconsumers’behavioralintentiontowardpurchasingapparel
made from plastic. This paper established the Sustainability Theory of Planned Behavior
model to determine the purchase intentions of Filipino customers while purchasing clothing
madeofrecycledplastic.Atotalof500validrespondentsweregatheredtoevaluatefactors:
Perceived Economic Concern, Perceived Environmental Concern, Perceived Authority Sup-
port, Subjective Norm, Attitude, Perceived Behavioral Control, Customer Perceived Value,
and Behavioral Intention. To analyze the data, the study utilized machine learning methods,
such as Random Forest Classifier (RFC) and Artificial Neural Network (ANN). Data pre-
processing using feature selection and correlation analysis was conducted to validate the
available data, performed data cleaning process, and data aggregation. Several iterative
processes were employed to generate the optimum classification model—obtaining a 92%
accuracy for RFC and 91% for ANN at 150 epochs under 30 hidden layer nodes. With low
error rates, the findings revealed that customer perceived value and perceived behavioral
control were the primary factors influencing consumers’ behavioral intentions toward pur-
chasingsustainableclothing.Thisstudyemphasizedtheconsiderationofthesefactorswhen
planning marketing strategies and initiatives to promote sustainable apparel.
1SchoolofIndustrialEngineeringandEngineeringManagement,MapúaUniversity,Manila,Philippines.2E.T.YuchengoSchoolofBusiness,MapúaUniversity,Makati,
MetroManila,Philippines.3DepartmentofFinanceandAccounting,AsianInstituteofManagement,Makati,MetroManila,Philippines.4DepartmentofIndustrial
✉
andSystemsEngineeringGokongweiCollegeofEngineering,DeLaSalleUniversity,Manila,Philippines. email:aksong@mapua.edu.ph
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 1
;,:)(0987654321

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
ITntroduction
he use of plastics has become a significant component in speedatwhichthemanufacturedproductsareproducedandthen
maintaining the convenience and suitability of modern discarded,aimingforinstantconsumption.Thismarketbecamea
lifestyles.Consideringitsadaptabilityandremarkablecost- globalizedindustry,utilizingcheaplaborandmaterialsallaround
performanceratiooverthepastseveralyears,ithasencompassed the world (Zhang et al. 2021). This led to an increase in non-
everything from everyday life to commercial manufacturing recyclable waste in landfills (Gomes de Oliveira et al. 2022).
(Chang et al. 2019). Since then, majority of our daily activities Different studies (Niinimäki et al. 2020; Brewer 2019) explained
have incorporated the usage of plastics—ranging from various that fast fashion is now the industry with the second-highest
food and beverage, cosmetics, toiletries, pharmaceuticals, and pollutant emissions at 10%. It was explained that large amounts
other products. These industries require packaging for their fin- of raw materials are needed for manufacturing fashion, which
ishedproductsinpreparationofitssafeandeffectivedistribution producesasubstantialamountofwastethatleavesaconsiderable
to customers (Evode et al. 2021). carbon footprint and produces a significant level of pollution
Shams et al. (2021) discussed how the overwhelming bulk of (Grazzini et al. 2021).
theannualonemilliontonsofplasticproduction,includingitems Nowadays,clothingcompaniesarewidelyknownforputtinga
likewatercontainers,bags,foodcontainers,gloves,andcups,are lotmoreeffortintoproducingenvironment-friendlyapparelthat
discarded after every single use. In addition, the study by Zhang focusesonsustainability.H&M,Adidas,andNikeareamongthe
et al. (2022) stated that plastic pollution poses dangerous health many popular international clothing companies that have com-
repercussions for both humans and marine species. In areas mitted to driving advancements toward an improved fashion
where industrial wastes like plastics, rubber, and textiles are fre- future. According to H&M Group (2023), their resources are
quentlyburned,fumesandthereleaseoftoxicsubstancesintothe aimed to be either 100% recycled or obtained through more
air, producing unpleasant odors from waste materials—con- environmentally friendly means by 2023, with 30% recycled
tributing significantly to air pollution. Furthermore, a study materials by 2025. H&M also noted the use of recycled plastic,
conductedbyAwoyeraandAdesina(2020)mentionedthatoutof derived from sources like PET plastic drinking bottles, plastic
countless tons of plastic garbage, only 7% is recycled, approxi- bags, shampoocontainers,andvariousotherplasticpackagingis
mately 8% is burned, and the remaining is landfilled. To which, one of its most often obtained components, in which several of
consequences of the increasing price and energy related to the theirwell-knownaccessoriesaremadewithrecycledplastic.This
landfilling process led to water pollution caused by waste dis- approach could prevent further damage to the environment. In
carded into bodies of water. addition,Adidasengagesinavarietyofenvironmentalinitiatives.
Tiseo (2023) posited how the Pasig River in the Philippines One of which is using recycled plastic in manufacturing their
releases over 63,000 metric tons of plastic debris into the ocean products, which is a cornerstone of its commitment to reducing
every year (Fig. 1). The data in 2019 shows that the Pasig River plastic waste and reducing and preventing pollution in the
was estimated to have contributed 6.43 percent of all river- world’s oceans. The collaboration between Adidas and Parley is
derived ocean plastics, making the Philippines the world’s hea- one of the brand’s sustainability initiatives; Adidas gave the
viest contributor of plastic-polluting rivers. plastic waste from beaches and coastal towns a new life as an
OECD (2022) reported that 22% of plastic waste was impro- AdidasxParley product by intercepting the waste before it
perlyhandledandnotcollected,19%wasburned,49%endedup reached the ocean. Another project is initiated by Nike, starting
in landfills, and only 9% was recycled (Fig. 2). The growth in with the ‘Move to Zero’ program. The journey aims to reduce
emerging economies has caused the use of plastic to triple over waste and carbon emissions to safeguard the future of the sport.
the previous 30 years. In recent times, plastics have been One of the materials they utilize is recycled polyester, which is
responsiblefor3.4%ofglobalgreenhousegasemissions,withthis created by shredding plastic bottles, turning them into granules,
trend observed between 2000 and 2019, there was a double and then twisting the granules into high-quality yarn. Nike is
increase in global plastics manufacturing to 460 million tons. currentlyusingrecycledpolyestermadefromshreddedplasticto
In the fast fashion industry, one of their objectives is to lessen waste, approximately as much as 30% in comparison to
manufacture and dispose of clothing rapidly; it pertains to the newly produced polyester, and it helps keep 1 billion plastic
Fig.1Annualreportofplasticwasteemissionsfromselectedriversgloballytotheoceanasof2019.
2 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Fig.2OECDreportofthemanagementofplasticpollutiongrowthglobally,asof2019.
bottles out of landfills and rivers and streams each year (Nike thelevelofsocialvalueplacedoncustomersasindividuals,which
Sustainability 2024). contributes to these warm glow feelings, which improves how
In recent years, much significant research has focused on much you enjoy the accompanying consumption experience.
customers’ attitudes and behavior regarding sustainable fashion Thus, perceived customer value is evident among sustainable
productsbyexploringtheimportanceofsustainabilitywithinthe behaviors,whichshouldbeconsideredwhenassessingconsumer
fashion sector (Grazzini et al. 2021). Much research on behavior (German et al. 2022a).
environment-friendlyclothinghaslookedatthepotentialbenefits Despite many studiesexploring sustainable behaviors, it could
of eco-conscious product development approaches (Fung et al. be deduced that this recent advancement in apparel, sustainable
2021;Provinetal.2021),howcustomersengagewithsustainable practices, and consumption has still been underexplored—
fashion brands on social media platforms (Testa et al. 2021), implicating a research gap in the current trend of apparels. The
along with how consumers perceive, their attitudes toward, and holistic measurement of sustainable behavior should be investi-
theirwillingnesstoinvestinsustainablefashionproducts,andthe gated to assess the behavioral intentions of consumers. The
factors that affect these behaviors (Grazzini et al. 2021; Nike novelty of this study lies with the sustainability domains, which
Sustainability 2024). wereoneofthefactorswhichwasadoptedinthisstudy(German
Presented in Table 1 are the summarized key related studies et al. 2022a). Under the sustainability domains, five factors are
alongside the limitations and need for future works. being considered such as the human, environmental, economic,
Nguyen et al. (2020) conducted a fashion-focused survey in productivity, and social aspects (Hajishirzi et al. 2022). On the
Vietnam and found that 86% of the respondents were aware of otherhand,anestablishedtheoryinthefieldofbehavior,known
thepotentialtoincorporaterecycledplasticwasteintothefashion astheTheoryofPlannedBehavior(TPB),hasbeenaccessibleand
industry. Kim et al. (2021) highlighted that concerns about the extensively contemplated. It measures a person’s behavioral
aesthetic aspects of clothing made from recycled materials could characteristics,suchasthesocialaspectsthatpertaintosocialties
relate to worries about how well these garments blend with the and structures that promote stability and stability cohesiveness.
consumer’s existing wardrobe, their ability to align with the To ensure social sustainability, people and organizations must
consumer’sdesiredself-image,andtheircomfortintermsofsize. examine how to promote healthy social interactions and encou-
Asaresult,consumersmightdelayorchoosenottobuyproducts rage long-term social systems that promote peace in society
made from recycled plastic materials (such as clothing) due to (German et al. 2022a; Talan et al. 2020). These domains are
aesthetic risk (Kim et al. 2021; Testa et al. 2021). These studies crucial because they offer a framework for comprehending how
demonstrated that aside from sustainability domains, people’s individuals behave concerning sustainability. On the other hand,
behavior encompasses behavioral intention and actual behavior human aspects include things that improve people’s quality of
(Park and Lin 2020; Kuah and Wang 2020; Nguyen et al. 2020; life, such as social justice, education, and health.
Kim et al. 2021; German et al. 2022a). Studies focusing on human sustainability examined the best
In relation, Polyportiset al.(2022) mentioned that consumers ways for people and institutions to build equitable and envir-
who experience positive emotions as a byproduct of their efforts onmentally friendly communities (Abusafieh and Razem 2017).
tolessenenvironmental harmareamong theeffectiveresponses. Moreover, when it comes to determining productivity, one must
Customers perceive that selecting and valuing products crafted lookathoweffectivelyandefficientlyonecangeneratethingsand
from recycled materials would evoke positive and comforting services.Thisaspectisimportantsinceitmayhelpdecreasewaste
emotions,suchasprideasaresultoftheircontributiontoabetter and maximize resource consumption by enhancing production,
world (Adıgüzel and Donato 2021). Moreover, Magnier et al. which can enhance the overall performance of both people and
(2019) referred to expected moral awareness, which is char- organizations (Abdel-Shafy and Mansour 2018). On the other
acterized as a consumer’s hopes regarding the way the goods hand, environmental aspects pertain to the ecologically respon-
would make him or her feel from an ethical perspective. Tezer sible and sustainable practices that are assessed, which also pro-
and Bodur (2019) referred to the “warm glow” sentiments that tect various aspects of life (Gansser and Reich 2023).
come with just utilizing eco-friendly products, like those made Environmentalsustainabilityencompassesexaminingmethodsby
fromrecycledmaterials;itwasalsohighlightedthatanincreasein whichpeople andcompaniescan preserve resources,lessentheir
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 3

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
rehtohtiweromderolpxeebdluohs hcihw,roivahebllarevodnanoitnetni noitalubat-ssorcdnanoitalerrocylno sgnidnfiehtecfifusdluocnoitalerroc nitnemssessaevitatilauqredisnocot lerappaehtfonoissergorpehtoteud etaercotsrotcafrehtognitagitsevnI
|     | rellamsderedisnocylnoevahyehT ecnislootsisylanasseworprehgih | htiwtfienebdluoctub,ydutsehtfo | ylnodnastnedutsderedisnocylnO detseggusydutsehT.ygolodohtem | eehteromdnatsrednuotdednetxe | srotcaferometacilpmidnadnapxE ydutssuounitnoc,krowemarfehtni esenihCnoylnodesucof,yrtsudni htiwsrotcafytilibaniatsusredaorb |     |
| --- | ------------------------------------------------------------ | ------------------------------ | ----------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --- |
srotcaflaroivahebfotnedecetnA gnisahcrupehtnoseidutsdetimil 91-DIVOCehtoteudeziselpmas esuotdetseggusdna,detaulave ebotdetseggusoslasawsrotcaf ,ssenevitceffeliaterrofseigetarts htiwecnadroccaniytilibaniatsus
llitsoslaeraerehT.seuqinhcet otseidutsdetalerroferutufeht ebotdetsegguserewsdohtem eromfonoitarolpxE.sremusnoc fotnemssessadna,sremusnoc ebdluoctnemegagneremusnoc
|     | erewstnedutsylno,cimednap | ,tahtetipseD.deredisnocsaw | elbaniatsusssessayllacitsiloh |                                                      |     | dna,ytilauqllarevo,ytilibarud |
| --- | ------------------------- | -------------------------- | ----------------------------- | ---------------------------------------------------- | --- | ----------------------------- |
|     |                           | tnecereromdnaataderom      | yrotarolpxeevitatilauqdesu    | evitanretladna)stnednopser foroivahebgniyubgnilcycer |     |                               |
|     | .tnemssessarehtrufsdeen   |                            |                               | 004>(eziselpmasregraL                                |     |                               |
|     |                           |                            | .esahcruplerappa              |                                                      |     | .dessessarehtruf              |
.slootlacitylana
.slootrehto
.dessessa
paG
esahcrupregraladetibihxestcudorp eraeveilebyehtsessenisubmorfyub sdoogdecudorpylbaniatsusyubohw esoohcylevitcadluowyehtdetacidni tnerapsnarteromerewyehtfisdnarb nislaitnedercelbaniatsusriehttuoba tnanimoderpehtdetutitsnocnemow ehtsadetpmorpsrotcaflanoitomorP ybdewollof,elbairavtnacfiingistsom .ecnacfiingisynaevahtondidsrotcaf .lerappadelcycergnisahcrupdrawot deviecreptahtdnuofsawti,ylbatoN decnuonorperomadaheulavytilauq stluserehT.erutufehtnidemusnoc degasremusnochguohtlatahtwohs dnaatartslaicosrehgihmorf54–52 dnuorgkcablanoitacuderehgihhtiw dnafosuoicsnoceromgnimocebera larevesllitseraerehT.ylevitarapmoc maertsniamehtgnitneverpselcatsbo
fo%53nahteromnignitluser,pag esehtgnisahcruptonstnednopser otesoohcsremusnoc’seirtnuocUE sremusnoC.eraflewlatnemnorivne dnatnetnoceromgnileefdetroper riehtdnastnemesitrevdariehthtob ,gnihtolcgnisahcrupnehwtnuocca latnemnorivnedna,laicos,lanosrep eulavdeviecrepfosnoisnemidruoF tcudorp,ylgnitseretnI.srotcafrehto wohssessaotelbasawydutsehT ebdluocstcudorpnoihsafdelcycer
elbarovafgnivahetipsedstcudorp tsomehtfoenosaytilibaniatsus otniekatotsnoitaredisnoclaicurc tahtdewohsseidutsehtnierehw sremusnocerusielhtafotnemges detaler-tcudorpehtelihw,srotcaf saegdelwonklatnemnorivnedna ylevitisoptahtsrotcaftnacfiingis nahtnoitnetniesahcrupnotceffe aetartsnomedtondidegdelwonk retseylop-nottocdelcycerfoesu
lerappadelcycpudnadelcyceR .snoitnetniesahcrupgnortsdna sedutitta’sremotsucdecneuflni .sedutittanotcapmitnacfiingis nehtytilibaniatsusnidetseretni dlodna51wolebdeganerdlihc sraey54revoregas’laudividni
|     |     |     | nielorgnidaeladeyalpdna | elbaniatsusarofgnitacovda |     |     |
| --- | --- | --- | ----------------------- | ------------------------- | --- | --- |
deredisnocslainnellimSU
rolaicosotgnitubirtnoc
.elytsefilerusielhta .gnihtolcdednelb
sgnidnfiniaM
.gnigakcap
|     | noitalubaT-ssorCdnanoitalerroC |     |     |     |     | weivretnipuorgfodohtemdexiM ehtroftnemssessaralubat-ssorc |
| --- | ------------------------------ | --- | --- | --- | --- | --------------------------------------------------------- |
,erauqs-ihc,sisylanaevitpircseD
|     |     |     | evisnetnI:sisylanaevitatilauQ | gniledoMnoitauqElarutcurtS | gniledoMnoitauqElarutcurtS | dnatnemssessaevitatilauqsa |
| --- | --- | --- | ----------------------------- | -------------------------- | -------------------------- | -------------------------- |
noissergercitsigoldna
.tcepsaevitatitnauq
ssecorpweivretni
)s(dohteM
|     | noihsaftsaffoytilibaniatsussdrawot |     | edam-retseylopdelcycergnisahcrup | fotcapmiehtetagitsevniotdemiA | htobssessaotkrowemarfroivaheb | detceffaeranrettapgnisahcrupdna |
| --- | ---------------------------------- | --- | -------------------------------- | ----------------------------- | ----------------------------- | ------------------------------- |
ecneirepxegnisahcrupnoderolpxE laicos,srotcaflanoitomorp,srotcaf deviecrepremotsucehtdenibmoC roivahebremusnocwohdenimaxE ralucitrapahtiw,gnihtolcdednelb
.spag rofsnoitpecrepeulav’sremusnoc lanosrep,srotcafdetaler-tcudorp -tcudorpdnacfiiceps-remusnoc lerappaelbaniatsusnosisahpme
| sremusnocfonoitnetniehtdna | edutittaremusnocfosisylanA |     |     | dnalatnemnorivnedna,srotcaf | -edutitta-egdelwonkdnaeulav |     |
| -------------------------- | -------------------------- | --- | --- | --------------------------- | --------------------------- | --- |
delcycerdnadelcycpugnoma delcycernosrotcafcimonoce retseylop-nottocdelcyceryb
|     |     |     | lainnellimelamefdenimaxE |     | delcycernosrotcafcfiiceps |     |
| --- | --- | --- | ------------------------ | --- | ------------------------- | --- |
.roivahebgniyubgnihtolc
dnaseidutsdetaleryekdezirammuS1
|     | .KUehtnistcudorp |     | .lerappaerusielhta |     |     |     |
| --- | ---------------- | --- | ------------------ | --- | --- | --- |
.stcudorpnoihsaf
.gnisidnahcrem
)s(evitcejbO
.stcudorp
|            |     |     | )1202(.lateihC | rahtkuMreehaJ | )4202(.lateniJ |             |
| ---------- | --- | --- | -------------- | ------------- | -------------- | ----------- |
| niLdnakraP |     |     |                | )4202(.late   |                | )4202(.late |
.lategnahZ
ecnerefeR
elbaT )0202(
|     | )1202( |     |     |     |     | atnarP |
| --- | ------ | --- | --- | --- | --- | ------ |
4 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
|     | .stlusertnereffidevahyam)noitacol lanoitiddatahtdetseggusoslasawtI rehtrufotdesuebyamslootrehtoro | dna,sremusnocKUnoylnodesucoF  | dnaedutittadetalerrocseidutsecnis |                                 |                              | ecuderotdesuebdluocnoitamotuA ledomfonoisnetxe,noissimenobrac | gnitsevniredisnocotdetseggussaw                                  |                                                              |                                 |
| --- | ------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------- | ------------------------------- | ---------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------- |
|     |                                                                                                   | dedeensitnemssessarehtruftaht | tub,raenilerewroivahebnotcapmi    | niahcylppusehtfoseitrapelpitluM |                              |                                                               | ,tnemtsevnietercsidrosuounitnoc dnascitsigolytrap-drihtregraldna | dnasnoitacilpmirehtonidessessa srotcafrehtodna,sdnamedtekram |                                 |
|     |                                                                                                   |                               | sahcus,dessessadnaderedisnoc      |                                 | saderedisnocebdluocselbairav |                                                               |                                                                  |                                                              | latotdna,seuqinhcetnoitazimitpo |
|     |                                                                                                   |                               | ,noitiddanI.tonsawydutsrieht      |                                 | dnaseussiytniatrecnu,sledom  |                                                               |                                                                  |                                                              | –emoctuossecorpniahcylppus      |
erewsremusnocZneGylnO ebdluocsrotcafytilibaniatsus lacitamehtamfotnempoleved gnilcycerredisnoc,snoisnetxe htiwseitniatrecnulaireganaM htiwtuptuoetalerroc,stcepsa
tnereffidtahtdna,dessessa cihpargoeg,ega(sremusnoc ebdluockrowemarfredaorb ,sretemaraprehtoredisnoC
|     |                         |     | ehtnonoitarolpxeredaorb .ecnereferpdnanoitpecrep | ehtnideredisnocebdluoc |     |                        | .ledomniahcylppusllarevo |     | dednetxerehtognipoleved |
| --- | ----------------------- | --- | ------------------------------------------------ | ---------------------- | --- | ---------------------- | ------------------------ | --- | ----------------------- |
|     | .tluserllarevoehtssessa |     |                                                  |                        |     | .tnemssessarofstcudorp |                          |     |                         |
.sledomlacitamehtam
.dessessaebyam
paG
,’dtA‘tahtdewohsMESfotluserehT sesehtopyhxis,oslA.IPAGotdetaler stluserehT.’nnIP‘foelorgnitaredom ehtdetaredom’nnIP‘tahtdehsilbatse krowemarflevonasedivorphcraeser elbairavfodesopmocsecitcarplaicos otelbisseccaeratahtseicnetepmoc otelbisseccanidnaslaudividniemos oteunevaeno,yltneuqesnoC.srehto ehtotssecca’sremusnocgnivorpmi mrofsnartotgnitpmettanahtrehtar timeotneessawmetsysnoitcudorp niahcylppuselbaniatsusehtfotfiorp emitdaelhtobfonoitcnufxevnocasi otlaicurcsignilleslennahctnereffid remotsucgnisaercnirofyrtsudniyna ,ksirnoitpursiddnalanoitarepomorf ygreneecuderrofseicilopdetseggus elbatutitsbusepyt-elgnishtiwledom
neewtebpihsnoitalerehterolpxeot tcnitsidsevlovnisnaejfoseirogetac foycneuqerfevitalerehtgnisaercni snaejdesurofgnippohsfoecitcarp nevorpsahydutsehT.tnemnrevog sedivorpmetsysdesoporpehttaht otenilnostcudorpriehtsesitrevda -itlumehtgnitcetorpnisehcaorppa krowten)CS(niahcylppusleufoib snoissimenobracdnanoitpmusnoc deredisnocsawnoitcudorptcudorp dna,ygolonhcetneergnignitsevni
,’buS‘,’dtA‘neewtebpihsnoitaler sihT.yltnacfiingis’IPAG‘dna,’CC‘ .’IPAG‘s’remusnocZnoitareneG forettamasemocebesuersnaej lacitylanaehtdewohsydutsehT latotehttahtevorphcihwstluser sA.emitdaelehtfoecnairavdna ,ycilopxat-dna-pacagnisopmiyb
|     |     |     |     |     | otgnipleh,noissimenobracssel ehtmorfseidisbusregralniatbo |     | dnalennahcdirbyhybstcudorp |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | -------------------------- | --- | --- |
ylevitisoperew’CC‘dna,’buS‘ .metsysnoitcudorplanoitidart riehtsllesreliatereht,dnamed evitceffetsomehtdenimreteD dna,noitatropsnartsallewsa noitcudorpelbixeflelbaniatsuS
|     | ehtgnitsetdetalumroferew | dna’CC‘dna,’rtA‘,’KE‘eht tnereffidesehtrofgnippohS |     |                         |     | ehtnahttfiorperom%67.8 |     |                     |     |
| --- | ------------------------ | -------------------------------------------------- | --- | ----------------------- | --- | ---------------------- | --- | ------------------- | --- |
|     |                          |                                                    |     | elbairavehtfoegatsyrevE |     |                        |     | .suomaferommehtekam |     |
dna,slairetam,sgninaem .sfeilebrosedutittarieht .stcudorprofgnisitrevda
sgnidnfiniaM
.tsoc)EBC(
|     |     |     |     | dezilitusawyciloplennahc-laudA | yllufasisihT.snoisicedlaireganam |     |     | rofledomlacitamehtamcitsahcotS |     |
| --- | --- | --- | --- | ------------------------------ | -------------------------------- | --- | --- | ------------------------------ | --- |
latottcaxenagnivigybyrotnevni hguorhtnoitcnuftfiorpdetcepxe
.seuqinhcetnoitazimitpocissalc
| gniledoMnoitauqElarutcurtS |     |     |     |     | ybderevocmetsysnoitcudorp .tnemtsevniygolonhcetneerg | -ni-pukcip-enilno-yubneewteb | dnah-nodna,redrokcab,erots |     |                           |
| -------------------------- | --- | --- | --- | --- | ---------------------------------------------------- | ---------------------------- | -------------------------- | --- | ------------------------- |
|                            |     |     |     |     | elbairavdellortnoc-noissime                          | noitalercitsiretcarahcatliuB | ehtfodaetsninoitcnuftfiorp |     | lacitamehtamedart-dna-paC |
elbatfiorptsomehtdnfiot
dnatnempolevedledom
|     |     | noissucsidpuorgsucoF |     |     |     |     |     | noitazimitpotsoclatot |     |
| --- | --- | -------------------- | --- | --- | --- | --- | --- | --------------------- | --- |
noitazimitpo
)s(dohteM
ecneuflniehtenimretedotdesoporP ,)KE(’egdelwonKlatnemnorivnE‘fo fostcurtsnocdna)CC(’ecnedfinoC )BPT(’roivaheBdennalPfoyroehT‘ krowemarfecitcarplaicosadetpodA egatnavdagnikat,snaejrofgnippohs rofsecnereferpriehtfosnoitanalpxe ,gnillesenilnoderedisnocydutsehT dnaemitdaelfotcapmiehtenimaxE
esahcrupotnoitnetni’sremusnoc elorllamsylevitalerayalpsfeileb gnisahcrupekilroivahebgninialpxe ehtnistludahtiwspuorgsucoffo rednumetsysnoitcudorpelbairav gnillesrofseiciloperots-ni-pukcip ylppusanotsocsnoissimenobrac -dna-pachguorhtnoissimenobraC denimretedsawmsinahcemedart
|     |                                                   | )IPAG(’stcudorPlerappAneerG‘ dnasedutittaremusnochcihwni | deliatedticileotmodgniKdetinU                                                   |                             |                             |                               |                           |               |               |
| --- | ------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------- | --------------------------- | ----------------------------- | ------------------------- | ------------- | ------------- |
|     | evitcejbuS‘,)dtA(”edutittAekil                    |                                                          |                                                                                 | afossenevitceffeehtdessessA | sawseiciloplortnocsnoissime | -enilno-yubdna,gnilleseniflfo |                           |               |               |
|     | no)chbP(’lortnoclaroivaheb                        |                                                          | sesucofydutsehT.snoisiced foecitcarpehtnoyllacfiiceps .snaejdesuro,delcycer,wen |                             |                             |                               |                           |               |               |
|     | remusnoC‘,)rtA(’msiurtlA‘ deviecreP‘dna)buS(’mroN |                                                          |                                                                                 |                             |                             |                               | .serotsliatermorfstcudorp |               |               |
|     |                                                   |                                                          |                                                                                 |                             |                             |                               |                           | .krowtenniahc | .dezimitpodna |
)s(evitcejbO
.devresbo
weiveRrofslanruoJdetsegguSreweiveR
)deunitnoc(1
)3202(.lateraK
.lateionhsiV
|     |     | .latereyoB |     | .laterakraS |     | .laterakraS |     | .laterakraS |     |
| --- | --- | ---------- | --- | ----------- | --- | ----------- | --- | ----------- | --- |
ecnerefeR
)4202(
| elbaT | )5202( | )5202( |     | )2202( |     | )3202( |     |     |     |
| ----- | ------ | ------ | --- | ------ | --- | ------ | --- | --- | --- |
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 5

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
dluohsnoitazilitulautcadna,tesatad ecological footprint, and spread environmentally friendly beha-
teeeL(sremusnocgnomaroivaheb
,lacitiloprolaicos,latnemnorivne teysahsiht,revewoh—)0202.la ahtiwdessessaylhguorohtneeb viors. Lastly, the economic aspect pertains to financial structures
| ,oiranecsefil-laernoytivitceffE | sahcussniamodytilibaniatsuS | ebdluocstcepsacimonocedna |     |               |     |              |     |        |     |             |        |
| ------------------------------- | --------------------------- | ------------------------- | --- | ------------- | --- | ------------ | --- | ------ | --- | ----------- | ------ |
|                                 |                             |                           |     | and processes |     | that promote | the | growth | and | development | of the |
elbaniatsustceffaotdetisop
dnakrowemarfkramhcneb economy (Waheed et al. 2023). Studies that focus on economic
.lootlacitylanadecnavda
|     |     |     |     | sustainability | incorporate |     | understanding |     | ethical | financial | prac- |
| --- | --- | --- | --- | -------------- | ----------- | --- | ------------- | --- | ------- | --------- | ----- |
tices,settlingfinancialobligations,andmakingsociallyconscious
(Sedliačiková
|     | paGhcraeseR |     |     | investments |     |     | et  | al. 2020). |     |     |     |
| --- | ----------- | --- | --- | ----------- | --- | --- | --- | ---------- | --- | --- | --- |
.dessessaeb
|     |     |     |     | With     | the aforementioned |         |     | notions      | on the         | sustainability | aspect |
| --- | --- | --- | --- | -------- | ------------------ | ------- | --- | ------------ | -------------- | -------------- | ------ |
|     |     |     |     | and TPB, | thispaper          | aimedto |     | establishthe | Sustainability |                | Theory |
paG of Planned Behavior (STPB) to assess sustainable behavior
|     |     |     |     | determinants     | for | purchasing |             | apparel | made        | from    | plastic waste |
| --- | --- | --- | --- | ---------------- | --- | ---------- | ----------- | ------- | ----------- | ------- | ------------- |
|     |     |     |     | extending        | the | model      | and concept | from    | studies     | (German | et al.        |
|     |     |     |     | 2022a; Abusafieh |     | and        | Razem       | 2017;   | Abdel-Shafy | and     | Mansour       |
|     |     |     |     | 2018; Gansser    |     | and Reich  | 2023;       | Waheed  | et al.      | 2023;   | Sedliačiková  |
etal.2020).Inaddition,theobjectiveofthestudywastoassessif
thedevelopedmodelcouldbeestablishedinthefieldofconsumer
| gnomanoissimenobracdnadnamed nobracwohgnitneserp,niahcylppus | ytilibaniatsusroftnemssessacitsiloH | sahtubsrotcafemosfonoitanibmoc sisylanaevitatitnauqdnaevitatilauQ | eromesuotdetseggusevahseiduts emocrevodna,noitciderpfoycarucca |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                              |                                     | detaleR.enodneebteysahsrotcaf                                     | emoS.tnemssessalacitylanatnecer                                |     |     |     |     |     |     |     |     |
rehgihevah,sledomnoitacfiissalc behavior among clothing industries using a machine learning
| elbixeflrofsnoitacilpmidetaerC |     | aderedisnocylnoevahseiduts tub,deredisnocneebevahsloot | enihcamesuotdetseggusevah dliubplehotelbmesnegninrael .sisylanalacitsitatsetairavitlum |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | ------------------------------------------------------ | -------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
otderapmocelbaivsselsixat .tnemssessacitsilohllarevoon algorithm; similar to the studies of German et al. (2022a) on
|     | .noissimelaminimdellortnoc |     | dnalanoitidartfosnoitatimil |            |          |           |               |                |           |            |           |
| --- | -------------------------- | --- | --------------------------- | ---------- | -------- | --------- | ------------- | -------------- | --------- | ---------- | --------- |
|     |                            |     |                             | consumer   | behavior |           | among         | transportation |           | intention  | and       |
|     |                            |     |                             | Gumasing   | et al.   | (2023)    | on technology |                | intention | and        | adoption. |
|     |                            |     |                             | This study | aimed    | to answer | several       | research       |           | questions: |           |
sgnidnfiniaM 1. Can the STPB framework holistically assess sustainable
|     |         |     |     | behavior |        | determinants |     | for purchasing |     | apparel | made from |
| --- | ------- | --- | --- | -------- | ------ | ------------ | --- | -------------- | --- | ------- | --------- |
|     | ytlevoN |     |     | plastic  | waste? |              |     |                |     |         |           |
2. Howcanmachinelearningensemblebeemployedtocreate
classification
|     |     |     |     | a           |          | model | for       | behavioral     | analysis? |         |             |
| --- | --- | --- | --- | ----------- | -------- | ----- | --------- | -------------- | --------- | ------- | ----------- |
|     |     |     |     | 3. How      | accurate |       | could the | model          | test      | out the | dataset for |
|     |     |     |     | forecasting |          | and   | modeling  | sustainability |           | and     | behavioral  |
domains?
|     |     |     |     | 4. Whatimplications,boththeoreticaland |      |            |     |            |     | practical,couldbe |     |
| --- | --- | --- | --- | -------------------------------------- | ---- | ---------- | --- | ---------- | --- | ----------------- | --- |
|     |     |     |     | built                                  | from | the output | of  | the study? |     |                   |     |
snoitauqetsoclatotevitcepsorP
yrotnevnidnah-nohtiwnoitaler 5. How can the study be extended based on the output and
| nideyolpmesawnoitazimitpo |                         | :elbmesnEgninraeLenihcaM dnarefiissalCtseroFmodnaR |     |              |     |     |     |     |     |     |     |
| ------------------------- | ----------------------- | -------------------------------------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|                           | —looTlacitylanAdecnavdA |                                                    |     | limitations? |     |     |     |     |     |     |     |
krowteNlarueNlaicfiitrA
|     |     |     |     | As a       | contribution, |     | this study | could | be beneficial  |     | to business |
| --- | --- | --- | --- | ---------- | ------------- | --- | ---------- | ----- | -------------- | --- | ----------- |
|     |     |     |     | industries | considering   |     | that this  | can   | give knowledge |     | on how the  |
.sredrokcabdna customers’ purchase intention can impact sustainability aspects
|     |     |     |     | among apparel. |     | The | results | could provide | implications |     | for sus- |
| --- | --- | --- | --- | -------------- | --- | --- | ------- | ------------- | ------------ | --- | -------- |
)s(dohteM
sdohteM
|     |     |     |     | tainable | practices | among | apparel | industries. |     | This study | can also |
| --- | --- | --- | --- | -------- | --------- | ----- | ------- | ----------- | --- | ---------- | -------- |
findings
|     |     |     |     | be advantageous |     | for | the government |     | as its |     | can aid in |
| --- | --- | --- | --- | --------------- | --- | --- | -------------- | --- | ------ | --- | ---------- |
recognizingcustomerneedsandpreferences,aswellasencourage
sustainableproductionandconsumptiontocreateprogramsand
|     |     |     |     | policies    | for sustainable |                 | apparel  | that       | are       | more effective. | The         |
| --- | --- | --- | --- | ----------- | --------------- | --------------- | -------- | ---------- | --------- | --------------- | ----------- |
|     |     |     |     | findings    | can contribute  |                 | to the   | community, |           | considering     | that this   |
|     |     |     |     | can promote |                 | environmentally |          | friendly   | behaviors |                 | in order to |
|     |     |     |     | minimize    | pollution       | and             | preserve | natural    |           | resources.      | Customer    |
stnanimretedroivahebelbaniatsus morfedamlerappagnisahcruprof foyroehtehtmorfledomroivaheb awareness and knowledge of sustainable fashion could be
fotnemssessanoissimenobraC
latnemnorivne-orpdehsilbatse ehtgnitset—roivahebdennalp dennalpfoyroehtytilibaniatsus increased, which might encourage them to buy more sustainable
ssessaotdemiaydutssihT ehtgnidnetxeetsawcitsalp apparel. Lastly, this study can benefit future generations by
.niahcylppuselbaniatsus
|              |     |     |     | identifying | possible       | constraints |           | to sustainable |          | fashion | using the  |
| ------------ | --- | --- | --- | ----------- | -------------- | ----------- | --------- | -------------- | -------- | ------- | ---------- |
|              |     |     |     | proposed    | theory,        | which       | could     | be utilized    | to       | inform  | the devel- |
|              |     |     |     | opment      | of strategies  |             | that will | boost          | consumer | demand  | for and    |
| )s(evitcejbO |     |     |     | acceptance  | of sustainable |             | behavior  | shortly.       |          |         |            |
evitcejbO
.roivaheb
|     |     |     |     | Literature | review      | and    | hypotheses     |        |              |          |               |
| --- | --- | --- | --- | ---------- | ----------- | ------ | -------------- | ------ | ------------ | -------- | ------------- |
|     |     |     |     | Research   | framework   |        | and hypothesis |        | build-up.    | Figure   | 3 illus-      |
|     |     |     |     | trates the | established |        | STPB           | model, | the          | research | framework     |
|     |     |     |     | employed   | in this     | study, | to determine   |        | the purchase |          | intentions of |
)deunitnoc(1
|     |     |     |     | Filipino | customers | while | purchasing |     | clothing | made | of recycled |
| --- | --- | --- | --- | -------- | --------- | ----- | ---------- | --- | -------- | ---- | ----------- |
plastic.TheSTPBframeworkinthisstudyhasbeenconsideredas
)5202(rakraS anextensionofthepro-environmentalplannedbehavior(PEPB)
dnaahdirM ydutssihT from a sustainable transportation perspective (German et al.
ecnerefeR
|     |     |     |     | 2022a; Ong | et  | al. 2023). | It is | an expanded |     | version | of the PEPB |
| --- | --- | --- | --- | ---------- | --- | ---------- | ----- | ----------- | --- | ------- | ----------- |
elbaT
|     |     |     |     | from TPB | (Ajzen | 1991), |          | integrating | fully | all      | sustainability |
| --- | --- | --- | --- | -------- | ------ | ------ | -------- | ----------- | ----- | -------- | -------------- |
|     |     |     |     | domains. | The    | model  | included |             | eight | factors: | Perceived      |
6 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Fig.3Theoreticalframework.
Environmental Concern (PENC), Perceived Authority Support more when the real value of a product exceeds their perceived
(PAS), Subjective Norms (SN), Attitude (AT), Perceived Beha- value. However, according to the study of Saricam and Okur
vioral Control (PBC), Customer Perceived Value (CPV), Beha- (2018), some research efforts aimed to establish the extent to
vioral Intention (BI)—PEPB (German et al. 2022a), and the which customers would be willing to pay an extra cost for sus-
additionalPerceivedEconomicConcern(PECC).Asexplainedin tainable fashion products. Moreover, consumers would be ready
thestudy of Ong et al.(2023), PECC isan importantvariable to tospendmoreonclothingmanufacturedfromorganicmaterials.
consider for full sustainability behavioral assessment. The suc- ThestudyconductedbyFeriolietal.(2022)andParkandLin
ceeding section provides an outlook of the hypothesis build-up (2020)alsoindicatedthatcustomersexhibitagreaterwillingness
since only PECC is a new addition. to pay elevated prices for environmentally friendly and sustain-
able clothing products. To which, a strong positive correlation
Perceivedeconomicconcern(PECC)affectingbehavioraldomains. wasfoundbetweencustomers’willingnesstospendmore(PECC)
PECCcanbeconsideredasagaugeofacustomer’sinclinationto on sustainable clothing and AT for sustainable apparel (Nam
allocate additional funds towards sustainable products (Saricam etal.2017).Thestudyalsomentionedthatcustomerswithgreater
andOkur2018).Variousstudiesmentionedthatcustomersassert environmentalconcernstendtoshowahigherinclinationtoward
theirreadinesstobuysustainableclothing,evenatahigherprice. purchasing sustainable clothing products. A study conducted by
However,thereareuncertaintiesoverwhethertheydoso,making Rohetal.(2022)showedthatPECChasapositivevalueonboth
their purchasing behavior contradict their claims (Gomes de SNandPBC,whereintheresearchersdiscoveredthattheperiods
Oliveira et al. 2022). Another study also mentioned that con- when organic products had the most significant development
sumers who are concerned with environmental issues may not were those in which people were considerably more inclined to
always choose to purchase eco-friendly or sustainable products. change their behavior to promote sustainability. However, Ong
Thosecustomerswhoclaimtobeconcernedwithenvironmental et al. (2023) expressed that when too expensive technology is
issuesmightstillnotengageinpro-environmentalbehaviorupon being sold, PECC will not be significant among buying behavior
purchasingproductssincesustainable productscomeatahigher duetopriceandgeneraleconomicconcerns.Itwasexplainedthat
cost compared to conventional alternatives (Dangelico et al. the more benefit and cost-saving a technology is, the more
2022), especially evident in the Philippines (Ong et al. 2023). It inclined people will be to purchase. In terms of clothing and
was mentioned that consumers are frequently willing to invest apparel, the following were hypothesized:
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 7

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
H1. Perceived Economic Concern has a significant impact with expectedobstacles,influencedbyone’sself-beliefandjudgmentof
Subjective Norm. their capability (Xu et al. 2022). PBC can be utilized to forecast
H2. Perceived Economic Concern has a direct significant behavior in a straightforward manner as well as indirectly influ-
relationship with Attitude. ence behavior through intentions relating to sustainability beha-
H3. Perceived Economic Concern has a positive relationship viors (Ong et al. 2023; Soorani and Ahmadvand 2019). In the
with Perceived Behavioral Control. study of Saricam and Okur (2018), both SN and AT have a sig-
nificant direct relationship with CPV. Furthermore, the study of
Perceived Environmental Concern (PENC) affecting behavioral Savari and Gharechaee (2020), Qi and Ploeger (2019), and Lin
domains. PENC can be viewed as a measurement of how each et al. (2017) mentioned that TPB domains significantly had a
person perceives the effects on the environment (German et al. substantialeffectoncustomers’purchasingintentionsandplayed
2022a; Ong et al. 2023). According to Bickart and Ruth (2012), a significantrolein influencing them.Behavioraldomainsin the
thedegreetowhichaconsumercaresabouttheenvironmentisa PhilippinecontexthavebeenestablishedbyGermanetal.(2022a)
significant personal characteristic because it is linked to their to affect CPV. Therefore, this study identified the following
knowledge and motivation regarding environmental matters. hypotheses:
Studies have shown that consumers’ intentions upon purchasing H10. Subjective Norm has a positive relationship to Customer
recycled and upcycled apparel products are positively impacted Perceived Value.
by environmental concerns (Park and Lin 2020). In a study H11. Attitude has a direct significant relationship to Customer
conducted by Lin et al. (2017), the researchers discovered that Perceived Value.
PENChasapositivevalueonbothSNandPBC.Incontrast,there H12.PerceivedBehavioralControlhasapositiverelationshipto
is little association between PENC and AT in environmental Customer Perceived Value.
impactassessment(EIA). Thiscorrelationshowsthatcustomers’
PENCwasadverselyaffectedwhentheywererequiredtoactively Customerperceivedvalue(CPV)affectingbehavioralintentions.In
engage in an environmental activity. In the Philippines, it was this study, CPV illustratesthe customer’s holistic evaluation of a
established that the community is now more inclined to pro- product’sutility,determinedbytheirperceptionofwhathasbeen
environmentalbehavior,leadingtosustainableoptions(Ongetal. providedandwhattheyhavereceived(Uziretal.2021).Itisthe
2023). Therefore, this study identified the following hypotheses: outcomeofhowconsumersfeelpriorto,throughout,andaftera
H4. Perceived Environmental Concern has a positive relation- purchase has been made (Al-Mashraie et al. 2020; Savari and
ship to Subjective Norm. Gharechaee2020).AstudybyDangelicoetal.(2022)discovered
H5. Perceived Environmental Concern has a positive relation- that CPV is the best indicator of consumers’ intentions to pur-
ship with Attitude. chase sustainable apparel and their willingness to spend higher
H6. Perceived Environmental Concern has a positive relation- pricesforit,nomatterwhethereco-materialisexplicitlyutilized.
ship with Perceived Behavioral Control. Thisshowsthatinthegeneralframeworkofsustainableclothing,
elevated CPV resulting from a product made with a particular
Perceived authority support (PAS) affecting behavioral domains. eco-friendly material enhances customers’ inclination to buy the
PAS relates to an individual’s comprehension of the resources, product, even at a higher price. The study findings of Dangelico
laws, regulations, and potentially additional processes provided et al. (2022) aligned with findings from prior research on sus-
byagovernmentorauthoritativeentitytosupportindividualsin tainable clothing products (Chi et al. 2021). Numerous research
adoptingaspecificbehavior(Nadlifatinetal.2016).Accordingto investigations have demonstrated that CPV exerts a significant
the study of Lin et al. (2017), PAS positively influences the and favorable impact on BI (Jalil et al. 2016; Liu et al. 2021).
domains of TPB among citizens’ Desire and readiness to engage Therefore, this study hypothesized that:
in an EIA. Considering the viewpoint of AT, these regulations H13. Customer Perceived Value has a positive relationship to
offer regular opportunities for engagement and a variety of Behavioral Intention.
communication channels to enhance the positive sentiments of
citizens. From the SN perspective, the regulations serve as a
means to foster cooperation between the project developer and Machine learning algorithm as analytical tool. Recent
the broader community. From the PBC perspective, the regula- advancementsinartificialintelligence(AI),bigdata,andmachine
tions offer residents the chance to participate in the EIA process learning brought newly adaptedmethodologiesfor analysis. Ong
under the most convenient conditions (Ong et al. 2023). There- etal.(2023)explainedthattheapplicationofmachinelearningas
fore, this study identified the following hypotheses: an analysis tool in behavioral intention among smart transpor-
H7. Perceived Authority Support has a positive relationship to tation provided better output compared to the multivariate ana-
Subjective Norm. lysis counterpart study. This was because several path analyses
H8. Perceived Authority Support has a positive relationship to werepresentonthelargemodel,creatingatotalof18hypotheses
Attitude. intheir study.Inaccordance,thestudyofGermanetal. (2022a)
H9.PerceivedAuthoritySupporthasapositiverelationshipwith thatconsideredPEPBpresentedbetteraccuracyforthenonlinear
Perceived Behavioral Control. relationship framework established with machine learning tech-
nique analyses. From their study, a total of 20 hypotheses were
TPB domains affecting customer perceived value. AT pertains to consideredintheirstudy.Comparedtotheirotherstudyutilizing
the evaluation of an individual concerning the behavior in higher-order structural equation modeling (SEM) analyses, both
question, ranging from a positive assessment to a negative one generated similar output and could prove how machine learning
(SooraniandAhmadvand2019).Ontheotherhand,SNrefersto as another tool could be considered.
the perception of societal influence, either encouraging partici- When dealing with multivariate analyses, studies such as that
pation in the behavior or discouraging it (Rausch and Kopplin of Fan et al. (2016) explained that the larger the framework, the
2021). In other words,SN consists of one’s opinions on whether more path is needed to assess the target output. This usually
close friends or family members should participate in the beha- resultsinloweraccuracyofrelationshipassessmentduetoerrors
vior.PBCrelatestotheperceptionofhoweasyorchallengingitis in the multiple paths needed to be met. Woody (2011) with the
to perform the activity, encompassing past experiences and same explanation posited that farther variables on the target
8 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
outputmayalsoresultinaninsignificantrelationship.Towhich, itevery6–9months(23%).Lastly,asmallportionofparticipants
present studies such as that of Jamshidi et al. (2022) and Al- make sustainable apparel purchases in 10–12 month intervals
Mashraieetal.(2020)expressedtheadvantagesofusingmachine (19.2%).
learning techniques in analyzing nonlinear relationship frame-
works,whicharemostlycomplexinnature.Itwasindicatedthat
these hybrid tools could present better output, higher accuracy, Questionnaire. The questionnaire consisted of two (2) parts:
and better predictive power. In terms of analyzing behavioral demographic information about potential respondents and
intention among technology adoption, it was presented that determinantsoftheSTPBmodel,adaptedfromliteraturereviews.
machine learning had higher accuracy (Al-Mashraie et al. 2020; Supplementary materials present the STPB questionnaire,
Gumasing et al. 2023) and provided a better significance level employing a five-point Likert Scale ranging from 1 (Strongly
with classification techniques like neural networks and random Disagree) to 5 (Strongly Agree) to evaluate the various determi-
forest classifier (RFC; Gumasing et al. 2023). nants that influence a user’s behavior when it comes to pur-
chasing apparel made from recycled plastic materials. The
adapted questionnaire for buildup is presented in the
Methodology Supplementary File.
Participants. This study assessed customers’ intentions and
behaviors regarding sustainable apparel. A total of 500 valid
responses were collected through an online survey using a con- Machinelearningalgorithm(MLA).Inthisresearch,amachine
veniencesamplingapproach.Thesamplingapproachwasutilized learning algorithm ensemble (MLE) was employed, including
to disseminate the online survey through various social net- artificial neural network (ANN) and RFC, which were employed
working sites and pages in order to procure a wide range of to properly assess the latent variables at once. According to the
respondents, since convenience sampling is a non-probability studybyOngetal.(2022),itwasmentionedthatusingamachine
sampling method where participants voluntarily choose to par- learning ensemble was much more efficient in analyzing the
ticipate after being informed about the study by the researcher aspects influencing human behavior concerning how people uti-
(Stratton 2021). The first two pages/section of the questionnaire lizetechnologycomparedtotraditionalandmultivariateanalysis
contained a short introduction as well as a reference to theData such as SEM. From their study regarding nuclear power plant
Privacy Act and approval of the Ethics Committee (FM-RC-22- reopening adoption among consumers, the SEM analysis proved
01-01, approved on March 20, 2023). Followed by the demo- highersignificanceontheclosevariablerelationshiponthetarget
graphic profiling of the respondents. Lastly, the STPB compo- object.UtilizingMLE,theywereabletoprovideinsightintohow
nents were then displayed after the demographic profile was (1)thebasicdecisiontreeshowedlowaccuracyratescomparedto
completed.PresentedinTable2aretheparticipantdemographic RFC, and (2) that farther variables were more significant com-
characteristics, collected alongside the measured items. paredtothoseclosetothetargetoutput.Theywereabletoprove
According to the collected data, it was observed that the that classification techniques such as RFC provided better accu-
majority of participants were women (69.2%), while males made racy output since it generates the most probable model every
up the remaining portion (30.8%). Regarding the distribution of iteration as compared to the random generation when the basic
age groups, individuals aged 18 to 25 comprised the largest decision tree is used. Their study also justified the explanation
segment,makingup(55.4%)ofthesample,individuals below18 presentedbyFanetal.(2016)andWoody(2011)—thefartherthe
comprised(14.4%),andthoseaged26to35yearsoldconstituted variable, the little effect it has on the target output significance
around (13%), while the remaining participants were from older level. In addition, SEM is limited to smaller frameworks or
age groups. In relation to marital status, a significant proportion smaller path analyses for better predictive power.
identified as single (75.8%), followed by married individuals at a Moreover, a comparison of different classification techniques
rateof (20.2%),andboth separatedand widowed(2%).Interms wasemployedbyOngetal.(2024).Theywereabletopresentthat
of residential areas, the majority of respondents, constituting RFC and ANN outperformed other classification modeling
(80.6%), reside in urban areas, while (19.4%) hail from rural techniques. For example, there was a significant difference
regions Regarding employment status, the majority consists of betweenXGBoostandLightGBMcomparedtootheralgorithms.
students (59.2%), followed by employed individuals (31%); The accuracy rate obtained was lower, with higher mean square
unemployed individuals make up a smaller percentage at (5%), errors. This delineates that there needs further improvement on
while self-employed/business owners account for (4.8%). As for other classification techniques before it could be generalized for
educationallevel,thehighestproportionattendedcollege(40.6%), use in behavioral studies. It could be deduced that RFC
closely followed by those who attended high school/senior high overpoweredbasicdecisiontrees,XGBoost,andLightGBM,even
school (37.4%). A significant portion has completed college or CATBoost, among others. Studies have also proven that these
obtained graduate degrees (20.4%); lastly, only a small fraction classificationtechniquesusingMLEmayalsooverpowereventhe
hasattendedgradeschool,withanoccurrencerateofjust(1.6%). advanced multivariate tools like SEM and multiple regression
For the household size, the majority of participants have analyses (Öztürk and Başar 2022).
households consisting of 3–4 people (45.6%), followed by 5–6 It could be seen among recent studies that little to no studies
people (26.4%), more than six people (15%), and finally, those have used the MLE to evaluate the factors affecting consumers’
with households of 1–2 people (13%). The majority of behavioral intention uponbuying sustainable apparel orsustain-
participants fall below Php 10,000 (30.8%). Additionally, 23.4% ablebehavioringeneral.Mostjustfocusedontechnologyandits
fall within Php 10,001–20,000, and 16.2% fall within Php acceptance (Ong et al. 2022), health behavior (Gumasing et al.
20,001–30,000.ThosewithanincomeabovePhp50,000account 2023),transportation(Germanetal.2022a;Ongetal.2023),and
for approximately 13. 8%, 10.2% had an income between 30,001 adoption(Milanietal.2020)tonameafew.Additionally,studies
and 40,000, and 5.6% were between Php 30,001–40,000 and showthatincomparisontoSEM(Germanetal.2022a;Ongetal.
between Php 40,001–50,000, respectively. Lastly, for the fre- 2022;Ongetal.2023),machinelearningalgorithmscanproduce
quency of purchasing sustainable apparel, (33%) buy sustainable predictions that are more accurate and models that work more
apparel every 1–3 months. Additionally, a significant percentage effectively (Bossi et al. 2022). Furthermore, both approaches are
purchaseitevery3–5months(24.8%),followedbythosewhobuy capable of handling huge numbers of variables and datasets for
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 9

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
profile. chargeofhighlightingitspositivefeaturesanddefiningitslimits.
Table2 Respondentsdemographic
|                 |     |          |     |     |     | Despite     | this, numerous |                 | studies | have raised | questions |               | about the |
| --------------- | --- | -------- | --- | --- | --- | ----------- | -------------- | --------------- | ------- | ----------- | --------- | ------------- | --------- |
|                 |     |          |     |     |     | efficacy    | of machine     | learning        |         | when        | used      | independently | for       |
| Characteristics |     | Category |     | N   | %   |             |                |                 |         |             |           |               |           |
|                 |     |          |     |     |     | measurement |                | and prediction, |         | or when     | combined  | with          | other     |
Gender Male 154 30.8% statistical and multivariate techniques in hybrid approaches.
|     |     | Female          |     | 346 | 69.2% |        |        |            |        |         |     |       |             |
| --- | --- | --------------- | --- | --- | ----- | ------ | ------ | ---------- | ------ | ------- | --- | ----- | ----------- |
|     |     | Total           |     | 500 | 100%  |        |        | classifier |        |         |     |       |             |
|     |     |                 |     |     |       | Random | forest |            | (RFC). | The RFC | is  | among | the many    |
| Age |     | Below18yearsold |     | 72  | 14.4% |        |        |            |        |         |     |       | classifica- |
18–25yearsold machine learning algorithms commonly employed for
|     |     |     |     | 277 | 55.4% |     |     | classification |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | -------------- | --- | --- | --- | --- | --- |
26–35yearsold tion tasks. It is a model which takes into account a
65 13%
36–45yearsold 45 9% straightforwardalgorithmfeaturinghighpredictionaccuracy.The
efficiency
46–55yearsold 20 4% study of Chen et al. (2019) mentioned the of RFC in
56–65yearsold 14 2.8% creatingsuperiorclassificationmodelscomparedtoastandardor
66yearsoldandabove 7 1.4% basic decision tree, as RFC consistently generates the most
Total 500 100% accurate tree every iteration. According to related studies (Ger-
Status Single 379 75.8% manetal.2022a;Gumasingetal.2023;Ongetal.2022;Ongetal.
Married 101 20.2% 2023), RFC could be employed for the categorization of human
|     |     | Separated |     | 10  | 2%  |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
factorsthataffecthowwellanapplicationisusedandadaptedor
|                 |     | Widowed |     | 10  | 2%    |                |     |           |           |       |          |           |          |
| --------------- | --- | ------- | --- | --- | ----- | -------------- | --- | --------- | --------- | ----- | -------- | --------- | -------- |
|                 |     |         |     |     |       | how consumers  |     | behave.   | It was    | shown | that RFC | is among  | the      |
|                 |     | Total   |     | 500 | 100%  |                |     |           |           |       |          |           | peoples’ |
|                 |     |         |     |     |       | most effective |     | tools for | analyzing | the   | factors  | affecting |          |
| Areaofresidence |     | Urban   |     | 403 | 80.6% |                |     |           |           |       |          |           |          |
decisions.
|     |     | Rural |     | 97  | 19.4% |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Adaptedfromtheaforementionedstudies,severalfactorswere
|            |     | Total      |     | 500 | 100%  |           |          |            |           |             |             |           |          |
| ---------- | --- | ---------- | --- | --- | ----- | --------- | -------- | ---------- | --------- | ----------- | ----------- | --------- | -------- |
|            |     |            |     |     |       | optimized | in order | to         | construct | the optimal |             | tree when | RFC is   |
| Employment |     | Student    |     | 296 | 59.2% |           |          |            |           |             |             |           |          |
|            |     |            |     |     |       | employed  | within   | the Python |           | Integrated  | Development |           | Environ- |
|            |     | Unemployed |     | 25  | 5%    |           |          |            |           |             |             |           |          |
Employed 155 31% ment, Spyderv5.0. Similarly, thesklearn package was integrated.
Self-Employed/ 24 4.8% To which, tree depths between 5 and 7 were taken into
BusinessOwner consideration, as well as criterion factors such as entropy or
Total 500 100% Ginicriteria,training-testingratiosspanningfrom60:40to90:10,
| Educationlevel |     | Finishedcollegeor |     | 102 | 20.4% |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
andsplitterchoicesincludingrandomorbest.Eachcombination
graduatedegree
wasoneofeveryparameterbetweentreedepth,criterion,splitter,
|     |     | Attendedcollege     |     | 203 | 40.6% |             |      |            |               |          |              |         |         |
| --- | --- | ------------------- | --- | --- | ----- | ----------- | ---- | ---------- | ------------- | -------- | ------------ | ------- | ------- |
|     |     |                     |     |     |       | and ratios. | This | study      | has therefore |          | analyzed     | a total | of 4800 |
|     |     | Attendedhighschool/ |     | 187 | 37.4% |             |      |            |               |          |              |         |         |
|     |     |                     |     |     |       | iterations  | upon | conducting | 100           | runs per | combination. |         |         |
seniorhighschool
|     |     | Attendedgradeschool |     | 8   | 1.6% |            |        |         |        |     |          |        |           |
| --- | --- | ------------------- | --- | --- | ---- | ---------- | ------ | ------- | ------ | --- | -------- | ------ | --------- |
|     |     |                     |     |     |      | Artificial | neural | network | (ANN). | ANN | contains | a more | intricate |
|     |     | Total               |     | 500 | 100% |            |        |         |        |     |          |        |           |
1–2people computation and algorithm in contrast with other MLAs. ANN
| Householdsize |     |     |     | 65  | 13% |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3–4people comprises neurons and layers that are connected by arcs, which
228 45.6%
5–6people convert input into output by means of an activation function
132 26.4%
|     |     |              |     |     |     | (Abolghasemi |     | et al. 2020). | ANNs | can | analyze | nonlinear | models |
| --- | --- | ------------ | --- | --- | --- | ------------ | --- | ------------- | ---- | --- | ------- | --------- | ------ |
|     |     | Above6people |     | 75  | 15% |              |     |               |      |     |         |           |        |
Total 500 100% andmaygivemorerealisticanswerstoissuesthatariseinreallife,
| TotalMonthlyNetIncome/ |     | Lessthan10,000 |     | 154 | 30.8% |             |          |               |               |                |      |         |          |
| ---------------------- | --- | -------------- | --- | --- | ----- | ----------- | -------- | ------------- | ------------- | -------------- | ---- | ------- | -------- |
|                        |     |                |     |     |       | and it      | is also  | capable       | of generating | predictions,   |      | which   | are fre- |
| Allowance              |     | 10,001–20,000  |     | 177 | 23.4% |             |          |               |               |                |      |         |          |
|                        |     |                |     |     |       | quently     | utilized | in prediction |               | areas since    | they | produce | more     |
|                        |     | 20,001–30,000  |     | 81  | 16.2% | significant |          |               |               |                |      |         |          |
|                        |     |                |     |     |       |             | outcomes | compared      |               | to traditional |      | methods | (Güven   |
30,001–40,000 51 10.2% andŞimşir,2020).AccordingtoJamshidietal.(2022)andAlam
40,001–50,000 28 5.6% etal.(2021),ANNscanbeaneffectiveclassificationapproachfor
|                          |     | Above50,000     |     | 69  | 13.8% |           |               |           |           |               |               |          |           |
| ------------------------ | --- | --------------- | --- | --- | ----- | --------- | ------------- | --------- | --------- | ------------- | ------------- | -------- | --------- |
|                          |     |                 |     |     |       | examining | factors       | that      | have      | a substantial | impact        | on       | human     |
|                          |     | Total           |     | 500 | 100%  |           |               |           |           |               |               |          |           |
|                          |     |                 |     |     |       | behavior. | Most          | research  | endeavors | typically     |               | commence | with      |
| Frequencyofbuying        |     | Atleastevery1–3 |     | 165 | 33%   |           |               |           |           |               |               |          |           |
|                          |     |                 |     |     |       | ANNs      | as a starting | point     | before    | delving       | into          | other    | forms of  |
| apparelsmadefrom         |     | months          |     |     |       |           |               |           |           |               |               |          |           |
|                          |     |                 |     |     |       | neural    | networks      | like Deep | Learning. | It            | was mentioned |          | that deep |
| recycledplasticmaterials |     | 3–5months       |     | 124 | 24.8% |           |               |           |           |               |               |          |           |
6–9months learning might be taken into consideration if the accuracy and
155 23%
10–12months complexitycapacityofANNprovidesalowoutput.Nevertheless,
96 19.2%
whensufficientpredictivepowerisattained,ANNisadequate.In
|     |     | Total |     | 500 | 100% |          |                |     |         |        |          |              |     |
| --- | --- | ----- | --- | --- | ---- | -------- | -------------- | --- | ------- | ------ | -------- | ------------ | --- |
|     |     |       |     |     |      | contrast | to complexity, |     | general | neural | networks | are regarded | as  |
advancedalgorithmsalready(Germanetal.2022a;Jamshidietal.
| the development | and | evaluation | of complicated |     | theories | 2022). |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | -------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
influencing
(Wendorf 2002). In order to categorize elements human behavior,
Various kinds of machine learning algorithms exist, with ANN is currently used in combination or hybrid with SEM
classification tools being commonly utilized for recognizing (Rehman et al. 2022). Research has shown that the intricate
patterns. A study conducted by Ong et al. (2022) stated how computationswithinthistypeofmachinelearningalgorithmcan
MLAslikeRFC,aswellasANN,havebecomewidelyrecognized yield more precise results, surpassing the capabilities of SEM,
in the field of human factors for evaluating human behavior. which attempts to simulate the transmission of messages among
However,astudyconductedbyJamshidietal.(2020)emphasized neurons in the brain (Al-Mashraie et al. 2020). In a study by
that differences of opinion may arise regarding the utilization of Alametal.(2021)aSEM-ANNhybridwastakenintoaccountto
| artificial |     |     |     |     |     |     |     |     | influencing | users’ |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | --- | --- |
intelligence and machine learning depending on how ascertain the variables perceptions of the
they are applied as their utilization heavily relies on input from usefulness of a mental health application. It has been demon-
users, individual behavior, and interaction among human roles. strated that the outcomes of ANN could accurately anticipate
elementsinfluencinghumanbehavior.Furthermore,Kalinićetal.
Tothis,theyrespondedbysayingthatdatascientistsareincharge
ofthecodeandthatpeoplewhowritethealgorithmshouldbein (2021) employed ANN to assess customer happiness. They
10 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
showed how this kind of MLA can identify components helpcompanies,government,andeventhesociety.Thus,inorder
effectively even in the face of dataset noise and can emphasize toenhancethecompetitiveedgeofmarketers,theconceptof7ps
crucial variables even when nonlinear connections are present. may be more suitable when studying sustainable apparel from a
To create the best model, the ANN parameters were also wider perspective.
optimizedbyusingidenticaldatapre-processingmethodsasRFC
withaparametersettingliketrainingandtestingratios.Similarly,
Results
studiesbyKalinićetal.(2021),Lietal.(2022),andJangandXing
Random forest classifier (RFC) results. The RFC output was
(2020) mentioned that they explore various methods for
consideredwiththeoptimumparametersofginiandbestat90:10
activatingthehiddenlayer(tanh, relu,andsoftmax), and output
testing and training ratio. With a 92% accuracy rate, this pre-
layer(softmax,sigmoid,swish).Inaddition,studiesbyYousefza- sentedasignificantdifferenceuponsubjectingtheresultsthrough
dehetal.(2021),Jenaetal.(2020),andEckleandSchmidt-Hieber
analysis of variance. The summarized output is presented in
(2019)alsomentionedthattheoptimizationprocessalsoinvolved
Table 3, which is considered depth 6.
considerationsofoptimizerssuchasAdam,RMSProp,andSGD.
Figure 4 represents the optimum tree with RFC. It could be
I S c n o p n y t d j h u e i n r s ct s v i t 5 o u . n 0 d — y, w P t i y h th t e ho A T n N en I N n so te a r g l fl g r o o a w r te i , t d hm a D n e d w ve a l t s o h p e im m p K e l n e e t r m a E s en n t v p e i a d r c o k n u a m s g in e e g nt w th i a n e s d c le u e s d s s t u o t c h m e a d e n r t s o h ’ r a p t e u t q h r u c e a h l p a a s to e re − n in t 0 te n .2 n o 4 t d i 8 o e n a id s s e a w nt d h i e e fi t n e e d r p m C u i P r n c V i h n a g ( s X i f n 1 a ) g ct w o a i r p th p in a a fl re u v l a e l n m u c e a in d o g e f
employed.
from plastic. Satisfying the parent node would involve consider-
Furthermore, the class was set up to encompass 5 indicators
thatmirroredthedataset’snormaldistribution,aligningwiththe ing the Subjective Norm (X 3 ) with values less than or equal to
2.261.Inaddition,meetingthisrequirementwouldalsoconsider
5-point Likert Scale survey responses. In this study, the
Perceived Economic Concern (X ), X , and Attitude (X ),
parameters were derived from an analysis of various literature 4 3 2
ultimately resulting in an increased likelihood of customers
sourcesandtheircombinations.Atotalof27,000iterationswere
intendingtopurchaseapparelmadefromplastic.However,ifX
carried out over 150 epochs, involving 10 runs for every 1
did not meet the expectations, both PBC (X ) and X would be
combination of three activation functions for the hidden layer, taken into account. This would result in sig 0 nificantly 1 increased
threeactivationfunctionsfortheoutputlayer,andthreedifferent
purchasing intentions among customers buying plastic-made
optimizers. This encompassed every conceivable combination,
apparel.
starting from 10 nodes and gradually increasing until reaching
Conversely,iftheparentnodeisnotmet,itwillassessX with
100 nodes within the hidden layer. 0
values less than or equal to 1.081. Meeting this requirement
Datapre-processingandoptimization.Thecoefficientwasgivena wouldinvolveconsideringX 4 ,X 1 ,X 2 ,andX 4 leadingtoveryhigh
purchasing intentions for apparel made from plastic. If this
threshold of 0.20, and a 0.05 p-value was necessary for accep-
t t h an re c s e h . o I l t d w d a i s d s n ee o n t p th re a s t en an t y m c u o c r h re s la ig ti n o i n fic c a o n e c f e fic a i n en d t w b o el u o l w d d th is e ru s p e t t r c e o s n u d lt i i t n io g n in wa s s ig n n o ifi t c m an e t t l , y it el w ev o a u t l e d d t p ak u e rc i h n a t s o e a i c n c t o en un t. t I X f 1 th a e nd ch X il 3 d ,
node did not meet the criteria, it would consider X and X ,
the analysis (Ong et al. 2023). Therefore, the data cleaning pro- 3 4
resulting in a high level of purchase intent.
cessinthisstudythroughthefeatureselectionmethodconsidered
Therefore, according to the results, PECC (X ) is the most
correlation analysis. To which the items were analyzed on the importantvariablethatsignificantlyinfluencedpeo 4 ple’sAT(X ),
rescaled target output, behavioral intention. All items were 2
deemed significant underwent data aggregation. i S m N p ( li X es 3 ), th an at d C PB PV C ( ( X X 0 ) ) to is h a ave hi h gh ig l h y p s u ig r n c i h fi a c s a in n g t i f n a t c e t n or tio a n ff s e . c T ti h n i g s
Following related studies, a 60% accuracy threshold was 1
considered for this study to employ significance on the relation- purchasingintentionswhenitcomestopurchasingapparelmade
from plastic. In order to establish a distinct categorization of
ship (German et al. 2022a). The higher accuracy rate induced
better classification modeling for predicting factors affecting hidden factors that impact behavioral intentions, the RFC
requires supplementary assistance from other machine learning
humanfactorsandconsumerbehavior.TheTaylorDiagramwas
algorithms due to the diverse range of elements that still exist.
thenutilizedinthisstudytocompareandassesstheacceptability
Chen et al. (2019) adopted various approaches in addition to
of accuracy rates among MLEs used in the study. Gholami et al.
incorporating outcomes from the RFC in identifying pertinent
(2020)conductedastudythatdemonstratedtheuseoftheTaylor
latent variables.
Diagram in evaluating model performance through its accuracy,
standard deviation, and correlation. In the study conducted, it
was determined that a Root Mean Square Error (RMSE) value Artificial neural network (ANN) results. Performing the ANN,
below 20% was within the satisfactory range. The RMSE twointegrateddevelopmentenvironmentswereusedtocompare
considered in the Taylor Diagram is the centered RMSE thebestparameters.UsingMATLAB,theANNoutputshoweda
difference between the simulated accuracy output and observed mean square error of 0.75212 for the validation considering the
pattern output from the MLE conducted. Additionally, a Elu activation function, 1.0533 for Tanh, and 0.9336 for the
correlation value exceeding 90% was regarded as being of sigmoid function. On the other hand, the testing mean square
significant importance. error results were 0.26379, 0.20594, and 0.21595, respectively.
Considering the parameters on Spyder v5.0, the accuracy rates
were 90.20%, 89.60%, and 84.40%. To which, the final ANN
Marketing 7P’s. After the machine learning algorithm has been considered the Elu function as the best activation function
used and demographic information about the respondents has parameter, which was used in both the hidden and output layer
been collected a marketing strategy based on the Marketing 7Ps run at 150 epochs (Pradhan and Lee 2010). In accordance, the
wasdeveloped.Thistoolincludedsevendistinctelements,which 80% training and 10 validation fold was considered. It was evi-
areProduct, Price,Place,Promotion,Process, PhysicalEvidence, dent that the model (Fig. 5) was deemed acceptable with the
and People. As all aspects of service marketing fall under the R-squared test value being 0.91 at 30 nodes in the hidden layer.
umbrellaofthe7Psinthemarketingmix,theconceptofthe7Ps From the results, it could be seen that the input layer was the
may be used to reflect the complexity of sustainable clothing for differentvariablesconsideredinthisstudy(fromSTPB).Because
clothing companies (Ho et al. 2022). The Marketing 7Ps would of the nonlinear relationship present, several nodes were needed
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 11

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
for the optimum output to be achieved. Upon optimization, 30 and a larger nonlinear relationship framework in this study
nodes were needed to be analyzed in the neural network model comparedtotheirs,andElucouldbethebestfitfortheanalysis.
usingtheEluActivationFunction.AspresentedinEq.(1)(Nanni Tofurthervalidatetheoutput,thevalidationratewasobtained
et al. 2022), Elu is an advance of the ReLU function where the showingover(under)fitting—Fig.6.Forthediscussionsectionto
value lies at [0.1,0.3]. Similar to ReLU, the value of x when bemorecoherent,theSHAPpackagewasconsideredtogenerate
positive lies on the negative region, while its y value would be the relative normalized score of importance to rank the
significance
below zero (Nanni et al. 2022). of each latent variable affecting behavioral intention
|     |     |     |     |     |     |     | to consider | sustainable | apparel. | Table | 4 displays |     | the importance |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | -------- | ----- | ---------- | --- | -------------- | --- |
fðxÞ¼xifx>0elseαðex(cid:2)1Þ ð1Þ scores that have been normalized and will be discussed in the
findings,
|     |     |     |     |     |     |     | following | section. | From the  |      | CPV     | emerged | as  | the most |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ---- | ------- | ------- | --- | -------- |
|     |     |     |     |     |     |     | prominent | latent   | variable, | with | the TPB | domains |     | of PBC,  |
TheutilityofEluasanactivationfunctionhasbeenexpressed
|                   |            |                |             |           |          |              | attitude,   | and subjective | norm        | following | in          | order | of significance.   |         |
| ----------------- | ---------- | -------------- | ----------- | --------- | -------- | ------------ | ----------- | -------------- | ----------- | --------- | ----------- | ----- | ------------------ | ------- |
| by related        | studies to | providea       | better      | accuracy  | ratewhen | dealing      |             |                |             |           |             |       |                    |         |
|                   |            |                |             |           |          |              | Perceived   | economic       | concern     | was       | also deemed |       | to be significant. |         |
| with a nonlinear  |            | relationship   | framework.  |           | This is  | because the  |             |                |             |           |             |       |                    |         |
|                   |            |                |             |           |          |              | However,    | a low          | significant | level     | was seen    | of    | PENC               | and PAS |
| analysis provides | a          | smooth result, | implicating |           | a better | accuracy     |             |                |             |           |             |       |                    |         |
|                   |            |                |             |           |          |              | (near 60%). |                |             |           |             |       |                    |         |
| rate when         | passing    | through        | nodes       | in the    | hidden   | layer. The   |             |                |             |           |             |       |                    |         |
| consequence       | of Elu     | providing      | negative    |           | values   | pushes the   |             |                |             |           |             |       |                    |         |
| calculation       | to batch   | normalization, | thus        | improving |          | the learning | Discussion  |                |             |           |             |       |                    |         |
processoftheneuralnetwork—creatinghigheraccuracyratesand Basedontheresults,CPVstandsoutasthemostcrucialfactorin
|           |         |               |        |     |        |           | determining | customers’ | purchasing |     | intention | for | plastic | apparel, |
| --------- | ------- | ------------- | ------ | --- | ------ | --------- | ----------- | ---------- | ---------- | --- | --------- | --- | ------- | -------- |
| better to | be used | with multiple | paths, | and | large, | nonlinear |             |            |            |     |           |     |         |          |
frameworks (Kim et al. 2020; Xiangyang et al. 2023). However, accountingfor100%.PBCfollowscloselyat94.7%,whileattitude
influence
Eluhasitsdisadvantages;oneofwhichisthatitcanonlybeused (AT) plays a substantial role with an of 87.4%. This
|     |     |     |     |     |     |     |     |     | significance |     |     | influencing | customers’ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----------- | ---------- | --- |
in the hidden layer and that it is computationally expensive. demonstrates the of CPV in
Comparedtotheadoptedstudies,thecurrentstudyhaspresented intentions towards purchasing apparel made of plastic. CPV is
positivelyhighoutputwhenEluwasutilized.Fromotherstudies, crucial in determining how inclined customers are toward pur-
commonresultswereobtainedusingsigmoid,tanh,andsoftmax chasing sustainable apparel products. CPV measures how
(Germanetal.2022a;Gumasingetal.2023;Ongetal.2023;Ong numerous benefits consumers estimate they will obtain from
et al. 2022). This is because there are a greater number of paths these items concerning the prices involved. Several important
aspectsaretakenintoconsiderationwhencustomersevaluatethe
|        |                                |     |     |            |     |     | perceived | value | of sustainable | apparel |     | products. | Brandão | and |
| ------ | ------------------------------ | --- | --- | ---------- | --- | --- | --------- | ----- | -------------- | ------- | --- | --------- | ------- | --- |
| Table3 | Random forestclassifierresults |     |     | (Depth=6). |     |     |           |       |                |         |     |           |         |     |
Costa(2021)indicatedthatapositiveperceivedvalueislinkedto
influence,
|          |     |       |       |     |       |       | a favorable | attitude, | increased | social |     |     | and a | sense of |
| -------- | --- | ----- | ----- | --- | ----- | ----- | ----------- | --------- | --------- | ------ | --- | --- | ----- | -------- |
| Category |     | 60:40 | 70:30 |     | 80:20 | 90:10 |             |           |           |        |     |     |       |          |
empowermentinaddressingobstaclesresponsibleforpurchasing
Best
|         |     |       |       |     |       |       | sustainable | fashion. |     |     |     |     |     |     |
| ------- | --- | ----- | ----- | --- | ----- | ----- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| Entropy |     | 84.41 | 83.30 |     | 84.47 | 90.94 |             |          |     |     |     |     |     |     |
PBCpertainstotheideathatcustomerswhoperceivethevalue
| Standarddeviation |     | 1.215 | 0.894 |     | 0.852 | 1.003 |                |          |               |             |                |           |              |       |
| ----------------- | --- | ----- | ----- | --- | ----- | ----- | -------------- | -------- | ------------- | ----------- | -------------- | --------- | ------------ | ----- |
|                   |     |       |       |     |       |       | of sustainable | clothing | products      | will        | likely         | feel more | empowered    |       |
| Gini              |     | 87.27 | 82.81 |     | 88.47 | 92.00 |                |          |               |             |                |           |              |       |
|                   |     |       |       |     |       |       | and confident  | in       | their ability | to          | make purchases |           | effectively. | The   |
| Standarddeviation |     | 1.021 | 0.664 |     | 0.502 | 0.000 |                |          |               |             |                |           |              |       |
|                   |     |       |       |     |       |       | feeling of     | control  | arises when   | individuals |                | believe   | that their   | deci- |
Random
sionsalignwithwhattheyconsidervaluable,boostingconfidence
| Entropy |     | 82.87 | 80.51 |     | 83.78 | 85.82 |     |     |     |     |     |     |     |     |
| ------- | --- | ----- | ----- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
intheircapacitytomakechoicesthatpromotesustainability.The
| Standarddeviation |     | 4.003 | 4.515 |     | 4.967 | 5.590 |             |           |        |               |     |         |             |     |
| ----------------- | --- | ----- | ----- | --- | ----- | ----- | ----------- | --------- | ------ | ------------- | --- | ------- | ----------- | --- |
|                   |     |       |       |     |       |       | attitude of | customers | played | a substantial |     | role in | influencing | the |
| Gini              |     | 82.61 | 81.03 |     | 84.94 | 85.30 |             |           |        |               |     |         |             |     |
Standarddeviation 3.805 3.991 4.886 5.888 outcome. Customers who perceive value are more inclined
|     |     |     |     |     |     |     | towards | developing | positive | attitudes |     | when | buying | apparel |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------- | --------- | --- | ---- | ------ | ------- |
Fig.4OptimumclassificationmodelwithRFC.X –PerceivedBehavioralControl;X –CustomerPerceivedValue;X –Attitude;X –SubjectiveNorm;
|     |     |     |     | 0   |     |     | 1   |     |     |     | 2   | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X –PerceivedEconomicConcern.
4
12 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Table 4Normalized score of importance.
Latentvariable Importance Normalizedscoreofimportance
CPV 0.234 100%
PBC 0.222 94.7%
AT 0.205 87.4%
SN 0.193 82.6%
PECC 0.189 80.6%
PENC 0.183 78.4%
PAS 0.167 71.5%
materials.Businessesandorganizationscanleveragethepowerof
social approval, peer influence, and the need for acceptance to
promote wider adoption of plastic apparel among consumers—
makingthemactivelycontemplateintegratingsuchproductsinto
theirwardrobechoices.AccordingtoastudyconductedbyZhang
et al. (2019), subjective social norms show a direct and positive
correlation with pro-environmental actions and have a positive
and noteworthy influence on the inclination to buy sustainable
clothing.
This leads us to the next important factor, the perceived eco-
nomicconcern(PECC),accountingfor80.6%significance.PECC
playsacrucialroleininfluencingcustomers’intentionsregarding
purchasing apparel made of plastic. Essentially, it refers to how
customers view and contemplate the financial aspects associated
with these products. Customers often evaluate whether selecting
apparel made from plastic or other alternatives aligns with their
budgetary constraints and monetary priorities. They consider
various factors like initial purchase price, ongoing expenses, and
potentiallong-termsavings.Therefore,ifcustomersperceivethat
Fig.5OptimumANNclassificationmodel. opting for eco-friendly options such as clothing made from
plasticsiseconomicallyviableandcanleadtocostreductionsor
other financial advantages over time, they are more inclined to
foster favorable attitudes regarding the utilization of these pro-
ducts. According to a study by Ansu-Mensah (2021), consumers
who prioritize environmental concerns are willing to buy sus-
tainable products without reservation, even if it means paying a
higherprice.Thus,itcanbeconcludedthatcustomers’intentions
of purchasing sustainable products are affected by the cost of
sustainable products.
The following factor in the hierarchy is known as PENC,
accounting for 78.4% of its importance. PENC refers to custo-
mers’ understanding and sensitivity towards environmental
issues, significantly influencing their choices and actions. Custo-
mers with a strong sense of PENC are more likely to express
strong intentions to purchase clothing items made from plastic
materials. Apparel crafted from plastics is often seen as an
effectivesolutionforaddressingenvironmentalconcernsbythese
Fig.6Validationlossrate. environmentally conscious individuals. This group prioritizes
preserving nature and considers reduced usage of plastic-based
options as a means to lessen their ecological impact or carbon
products made from plastic materials. They perceive these pro- footprint. Such perception boosts their desire even further,
ducts as environmentally friendly and consider them their pre- leading them to utilize such products to contribute positively
ferredchoicesforwhichtheywouldwillinglyspendextramoney towardsfavorableenvironmentaloutcomes.Inastudyconducted
on sustainable clothing. Brandão and Costa (2021) mentioned by Zhang et al. (2019), it was mentioned that previous research
thatattitudeandperceivedvalueareassociatedwithoneanother. has typically found a positive link between PENC and the pur-
The effects of these actions have an impact on how consumers chase intention to buy sustainable products. Additionally, the
behave. Therefore, having a strong understanding of the envir- study demonstrated a positive association between PENC and
onment may result in a positive attitude (AT) and more sig- boththeinclinationtobuysustainableclothingproductsandthe
nificantcustomerbehavioralcontrol(PBC)overthechallengesof attitude toward purchasing them, demonstrating how concerned
achieving sustainable apparel consumption. individualsarewithenvironmentalissuesandhoweagertheyare
SN plays a significant role, accounting for 82.6%. SN have a to support attempts to address them.
significant influence on shaping consumer behavior, particularly At71.5%,thePASrankslowestamongcontributingfactorson
with social and peer norms strongly affecting individuals’ pur- the list. This indicates that customers show importance in
chasing intention towards buying clothes made from plastic receiving support, recommendations, or endorsements from
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 13

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
authoritative figures or institutions regarding their attitudes and beinlinewithconsumervaluesandpreferences.Fromthisstudy,
beliefsaboutpurchasingsustainableapparelproducts.Itsuggests CPV—along with the functionality, consumer perception, brand
that they value and trust advice or guidance from sources they sustainability, desired values, and motivation as a strategy for
perceive as credible and having authority. Governments and selling apparel, from plastic to apparel. Specifically,
environmental organizations, according to the study by Lin and Functionality Consumers’ perceptions of the usefulness of
Huang (2012), offer subsidies or promotions to encourage indi- sustainable clothing influence their decisions regarding their
vidualstolivesustainably.Additionally,itwassuggestedthatfor purchase.
green consumption to become the norm, both the government Consumer perception: By comprehending consumer percep-
and environmental organizations must actively promote it. Fur- tions and how they affect purchasing decisions, businesses may
thermore, the favorable connection between the educational createenvironmentallyfriendlyapparellinesthatsatisfydemand.
attainment of customers and their inclination to buy sustainable Brand sustainability: The decisions consumers make for
clothing shows that governments should work towards creating purchasing sustainable clothing goods are favorably connected
communities that are not just more educated but also more with the importance of fashion brand sustainability.
mindfuloftheenvironmentbyinvestingineducation(Dangelico Desired values: Recognizing what consumers want from
et al. 2022). environmentallyfriendlyclothesmayassistbusinessesincreating
The significance of every factor discussed in this paper lies in sustainable clothing lines that satisfy demand.
their ability to exceed the 60%significant level. The ranking was Motivations for purchasing: Understanding customer moti-
determined solely based on the results derived from various vations for choosing eco-friendly clothes may help companies
methodsemployedduringdataanalysisofasurveycompletedby create marketing plans that resonate with their target
participants. Overall, it was concluded that the three most demographic.
important elements that needed to be emphasized in order to By generating sustainable value propositions, gaining insight
encourageindividualstopurchasesustainableapparelwereCPV, intoconsumerperceptionsanddesiredvalues,andimplementing
PBC, and attitude (AT). marketing tactics that resonate with their target market,
businesses may raise the perceived value of sustainable apparel
among their customers. Other suggestions are presented.
Theoretical implications. The TPB framework may be used for
evaluating consumers’ behavioral intentions when it comes to
For apparel industries. Given the substantial environmental
making sustainable apparel purchases. Based on several studies,
impact associated with the apparel industry, it is more crucial
theTPBframeworkcanbeaneffectivetoolforunderstandingthe
variablesthataffectaperson’sintentionwhenpurchasingapparel thanevertousesustainableprocedures.Sustainablefashionisnot
merely a fashion trend but also an essential requirement for the
made from plastic. By considering these variables, interventions
industry. Companies have to adapt to keep up with this per-
may be created that encourage sustainable behavior and the spective as customers take an active role in reducing fashion’s
reduction of pollution resulting from plastic waste by means of
negative environmental impacts. Ethical and sustainable fashion
plastic recycling and clothing production. CPV was shown to
have the most significant influence on how consumers felt they has evolved from a trend to an economic imperative for the
apparel industry. The apparel sector could promote sustainable
had control over their behavior and how they perceived pur-
clothingbyimplementingeco-design,supplychainsustainability,
chasingproductsmadeofplastic,whichhasnumerousimportant
consumer education, and waste management strategies. The
theoretical implications. To begin with, it emphasizes the sig-
nificantimpactofexternalfactorsonshapingpurchaseintentions fashionindustrymusttransitiontosustainable manufacturingto
solve some of the social and environmental issues that societies
andpro-environmentalattitudes,especiallywhensuchfactorsare
are now facing. Fast fashion must be reviewed considering the
related to understanding the worth of the products. This study
emphasizes the importance of external social variables in influ- environmentalandsocialconsequencesitimposesonsociety,and
more sustainable business strategies are critically important.
encing individual decision-making and is consistent with well-
known behavioral concepts like the TPB. CPV has a beneficial Sustainable manufacturing techniques may be used through
impact on consumers’ intentions regarding buying and a readi- ethicallaborpractices,especiallyusingmaterialssuchasrecycled
plastic bottles and promoting recycling and reuse. As more
nesstospendextraonproductsthatsupportsustainablefashion.
fashion customers take up the cause of sustainability, apparel
CPV may therefore be used to assess company strategies toward manufacturers can advance and profit from the opportunity.
perceived sustainability and forecast consumer attitudes regard-
ing sustainable apparel. Consequently, the proposed STPB fra- For the government. Governments can play a significant role in
mework may evaluate individual behavior comprehensively with
advancing sustainable clothing by establishing rules, implement-
regardtosustainabilityandsustainablebehaviormoreholistically
ing legislation, encouraging international collaboration, and
than other extended TPB or PEPB frameworks.
implementing policy interventions. Regulation may encourage
ethical, circular, and sustainable fashion, enabling businesses to
Practical and managerial implications. To reduce plastic pol- viewaproduct’sworthasslowlyloweringandboostingacircular
lution, evaluating the factors influencing customers’ behavioral economy. Laws can promote sustainability in the textile and
intentions toward purchasing sustainable apparel is essential. fashion sectors by compelling companies to provide information
According to the study’s findings, Filipinos are willing to spend ontheirsustainabilitydevelopmentandchargingfinesiftheyfall
extra on products that support sustainable fashion and are open shortofgoals.Internationalcollaborationmaysupportinitiatives
to buying clothes made of plastic. The community should con- to change the apparel industry to one that is more sustainable.
sider practical implications regarding people’s behavioral inten- Sustainable fashion consumption can be influenced by policy
tions toward purchasing sustainable apparel. These implications changes, such as tax incentives for businesses that employ
includeinitiativesandstrategiesthefashionindustrymaytaketo recyclable materials or provide apparel repair services.
promote a change and lean towards environmentally friendly The results imply that companies, environmental advocacy
clothing.Companiesmayconsidersustainablevaluepropositions. organizations, and political leaders should consider utilizing
Businesses can develop this to improve the perception of the authoritative support to promote sustainable clothing. This may
sustainabilityoftheirbusinessmodels.Thesepropositionsshould include pursuing partnerships or endorsements from reputable
14 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
people or organizations, displaying certificates or stamps of regarding purchasing sustainable apparel. This study highlights
approval, or actively advertising the potential compatibility of howimportantitistotakethesefactorsintoconsiderationwhen
their goods with reliable recommendations. By doing this, establishing marketing strategies and initiatives intended to raise
companiescanincreaseconsumers’positiveviewsandconfidence awareness of products made with plastic in order to make a
regarding purchasing environmentally friendly products, such as positive contribution towards the advancement of a sustainable
apparel made of plastic, which can encourage more people to environmenttoreduceplasticpollution.Furthermore,itopensup
engage in environmentally friendly behaviors. theopportunitytoconductfurtherinvestigationandexamination
|     |     |     |     |     |     |     |     | of these | factors by | employing | advanced |     | machine-learning |     | meth- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --------- | -------- | --- | ---------------- | --- | ----- |
odologiesandlargersetsofdatatoenhanceourunderstandingof
Conclusion sustainable consumer behavior. For ANN, either MATLAB or
individuals’
This study explored the factors that impact beha- Python codes could be utilized and could still provide similar
| vioral intentions |          | towards | purchasing | apparel  | made     | from         | plastic. | findings. |     |     |     |     |     |     |     |
| ----------------- | -------- | ------- | ---------- | -------- | -------- | ------------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| The research      | utilized | two     | machine    | learning | methods, | specifically |          |           |     |     |     |     |     |     |     |
RFCandANNandwereemployedtoanalyzethecollecteddata.
|     |     |     |     |     |     |     |     | Limitations | and | future | research. | The study | could | be  | used and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | --------- | --------- | ----- | --- | -------- |
ThefindingsfromthisresearchindicatedthatCPVandPBCwere
|     |     |     |     |     |     |     |     | expanded | to evaluate | the | sustainabilityof |     | the apparel | industry | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ---------------- | --- | ----------- | -------- | --- |
the main variables influencing consumers’ behavioral intention customers’
|     |     |     |     |     |     |     |     | various | nations | as well | as the |     | behavioral | intentions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ------ | --- | ---------- | ---------- | --- |
toward purchasing apparel made of plastic. Customers who toward purchasing sustainable apparel. It does, however, have
perceivevaluearemorelikelytoestablishpositiveattitudes(AT) certain restrictions. First, in terms of demographics, the largest
while purchasing sustainable apparel products. The feeling of portion of survey participants (55.4%) were within the age range
control arises when individuals believe that their decisions align of 18 to 25. The research made an effort to include people of all
confidence
with what they consider valuable, boosting in their ages;however,becausesocialmediaplatformswereusedtogather
capacitytomakechoicesthatpromotesustainability.Theattitude data,themajorityofparticipantswereunder30.Inaddition,since
ofcustomersplayedasubstantialroleininfluencingtheoutcome. respondents were simply asked to categorize their region of resi-
Customers who perceive value are more inclined to develop dence as rural or urban, the study was unable to determine the
positive attitudes when buying apparel products made from specific
|     |     |     |     |     |     |     |     | exact places | of residence |     | of the respondents. |     | The |     | coordi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ------------------- | --- | --- | --- | ------- |
plastic materials. They perceive these products as environmen- therespondents’
|     |     |     |     |     |     |     |     | nates of |     |     | locations | mayhave | affectedtherelative |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --------- | ------- | ------------------- | --- | --- |
tallyfriendlyandconsiderthemtheirpreferredchoicesforwhich
|     |     |     |     |     |     |     |     | importance | of various | elements, | which | led | to a | different | view of |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ----- | --- | ---- | --------- | ------- |
they would willingly spend extra money on sustainable clothing. customerpurchasingbehavior.Futureresearchersmightimprove
customers’
Moreover, inclination towards purchasing sustain- this by utilizing a more diverse sample procedure and ensuring
ableclothingisdirectlyandpositivelyinfluencedbysocialnorms
|     |     |     |     |     |     |     |     | that various | demographic |     | characteristics |     | are considered |     | in their |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | --------------- | --- | -------------- | --- | -------- |
(SN), which also have a positive and substantial effect on other studies.Inaccordance,real-lifetestingofmodelandresultscould
pro-environmental behaviors. Customer intentions were also be developed when pre- and post-purchase evaluation and data
affected by perceived economic concern (PECC) because mone- collectionisemployed.Thiscouldcreateabetterpredictivemodel.
tary factors were taken into consideration when making pur- Moreover, the study was unable to take into account and
chasing decisions towards sustainable products. Customers with distinguishbetweenonlineandin-personpurchasesofsustainable
| high environmental |     | awareness |     | were more | inclined | towards | pur- |          |            |         |     |             |     |       |          |
| ------------------ | --- | --------- | --- | --------- | -------- | ------- | ---- | -------- | ---------- | ------- | --- | ----------- | --- | ----- | -------- |
|                    |     |           |     |           |          |         |      | apparel. | This could | enhance | the | total scope | and | depth | since it |
chasing sustainable products as a strategy to reduce their envir- person’s
|          |        |     |         |               |     |               |     | would need | to   | explore    | deeper into | the        | analysis | of a |          |
| -------- | ------ | --- | ------- | ------------- | --- | ------------- | --- | ---------- | ---- | ---------- | ----------- | ---------- | -------- | ---- | -------- |
| onmental | impact | and | promote | environmental |     | preservation, |     |            |      |            |             |            |          |      |          |
|          |        |     |         |               |     |               |     | intentions | when | purchasing | a           | particular | service  | or   | product. |
respondent’s
which increases the importance of PENC. Apparel crafted from Second, the study was unable to relate the
plastics is often seen as an effective solution for addressing demographics to their behavior, which would have provided a
environmental concerns by these environmentally conscious morecomprehensiveoverviewoftheirbehavioralintentionswhen
individuals. This group prioritizes preserving nature and con- itcomestopurchasingsustainableapparel.Futureresearchersare,
sidersreducedusageofplastic-basedoptionsasameanstolessen therefore, encouraged to offer new perspectives on the subject
their ecological impact or carbon footprint. Such perception matter.Thefindings,metrics,andquestionnairesmaybeusedby
boosts their desire even further, leading them to utilize such futureresearcherstoconductadditionalstudiesandtoapplynew
products to contribute positively towards favorable environ- methodsandideasinordertocomeupwithnewperspectivesand
mental outcomes.
|     |     |     |     |     |     |     |     | comprehension | regarding |     | customer | behavioral | intentions |     | toward |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | -------- | ---------- | ---------- | --- | ------ |
Finally,PASreferstohowimportantcustomersfindittohave
|                 |     |           |       |            |             |     |          | purchasingsustainable |             | apparel.Lastly, |     | future       | researchcould |                 | look |
| --------------- | --- | --------- | ----- | ---------- | ----------- | --- | -------- | --------------------- | ----------- | --------------- | --- | ------------ | ------------- | --------------- | ---- |
| their attitudes |     | and ideas | about | purchasing | sustainable |     | clothing |                       |             |                 |     |              |               |                 |      |
|                 |     |           |       |            |             |     |          | into the              | role played | by customer     |     | satisfaction | in            | environmentally |      |
products supported by or endorsed by reputable individuals or friendly purchasing behaviors by concentrating on consumers
first-hand
institutions. It was suggested that for green consumption to who have experience withsustainable clothes.
| become        | the norm, | both     | the     | government | and          | environmental |        |                   |     |     |     |     |     |     |     |
| ------------- | --------- | -------- | ------- | ---------- | ------------ | ------------- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
| organizations | must      | actively | promote | it.        | Furthermore, | the           | favor- | Data availability |     |     |     |     |     |     |     |
ableconnectionbetweentheeducationalattainmentofcustomers
Thedatasetsgeneratedduringand/oranalyzedduringthecurrent
| and their | inclination |     | to buy | sustainable | clothing | shows | that |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------ | ----------- | -------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
studyareavailablefromthecorrespondingauthoronreasonable
governmentsshouldworktowardscreatingcommunitiesthatare
request.
notjustmoreeducatedbutalsomoremindfuloftheenvironment
| by investing | in        | education. |             |            |         |              |         |           |                      |     |        |       |     |     |     |
| ------------ | --------- | ---------- | ----------- | ---------- | ------- | ------------ | ------- | --------- | -------------------- | --- | ------ | ----- | --- | --- | --- |
|              |           |            |             |            |         |              |         | Received: | 2 July2024;Accepted: |     | 2 June | 2025; |     |     |     |
| In summary,  |           | it was     | found       | that every | single  | one of the   | afore-  |           |                      |     |        |       |     |     |     |
| mentioned    | variables | was        | significant | and        | had     | a weight     | of more |           |                      |     |        |       |     |     |     |
| than 60%.    | The       | study      | emphasized  | the        | crucial | roles played | by      |           |                      |     |        |       |     |     |     |
perceivedvalue,behavioralcontrol,consumerattitude,economic
References
| considerations, |             | environmental |             | concerns,   | and          | social norms  |         | in        |           |           |                |        |             |         |              |
| --------------- | ----------- | ------------- | ----------- | ----------- | ------------ | ------------- | ------- | --------- | --------- | --------- | -------------- | ------ | ----------- | ------- | ------------ |
|                 |             |               |             |             |              |               |         | Alam MM,  | Alam MZ,  | Rahman    | SA, Taghizadeh |        | SK (2021)   | Factors | influencing  |
| determining     | sustainable |               | consumption |             | behavior.    | Additionally, |         | it        |           |           |                |        |             |         |              |
|                 |             |               |             |             |              |               |         | health    | adoption  | and its   | impact on      | mental | well-being  | during  | COVID-19     |
| provided        | important   | details       | on          | the complex | interactions |               | between |           |           |           |                |        |             |         |              |
|                 |             |               |             |             |              |               |         | pandemic: | a sem-ann | approach. | J Biomed       | Inform | 116:103722. |         | https://doi. |
these variables that affect customers’ behavioral intentions org/10.1016/j.jbi.2021.103722
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|         (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 15

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
Abdel-Shafy HI, Mansour MSM (2018) Solid waste issue: sources, composition, GholamiH,MohamadifarA,SorooshianA,Jansen JD(2020)Machine-learning
disposal,recycling,andvalorization.EgyptJPet27(4):1275–1290.https://doi. algorithmsforpredictinglandsusceptibilitytodustemissions:thecaseofthe
org/10.1016/j.ejpe.2018.07.003 JazmurianBasin,Iran.AtmosPollutRes11(8):1303–1315.https://doi.org/10.
AbolghasemiM,BehE,TarrG,GerlachR(2020)Demandforecastinginsupply 1016/j.apr.2020.05.009
chain:theimpactofdemandvolatilityinthepresenceofpromotion.Comput GomesdeOliveiraL,MirandaFG,dePaulaDiasMA(2022)Sustainablepractices
IndEng142:106380.https://doi.org/10.1016/j.cie.2020.106380 inslowandfastfashionstores:whatdoesthecustomerperceive?CleanEng
AbusafiehS,RazemM(2017)Humanbehaviorandenvironmentalsustainability: Technol6:100413.https://doi.org/10.1016/j.clet.2022.100413
promotingapro-environmentalbehaviorbyharnessingthesocial,psycho- Grazzini L, Acuti D, Aiello G (2021) Solving the puzzle of sustainable fashion
logical and physical influences of the built environment. E3S Web Conf consumption:theroleofconsumers’implicitattitudesandperceivedwarmth.
23:02003.https://doi.org/10.1051/e3sconf/20172302003 JCleanProd287:125579.https://doi.org/10.1016/j.jclepro.2020.125579
Adıgüzel F, Donato C (2021) Proud to be sustainable: upcycled versus recycled Gumasing MJ, Ong AK, Sy MA, Prasetyo YT, Persada SF (2023). A machine
luxury products. J Bus Res 130:137–146. https://doi.org/10.1016/j.jbusres. learningensembleapproachtopredictingfactorsaffectingtheintentionand
2021.03.033 usage behavior towards online groceries applications in the Philippines.
AjzenI(1991)Thetheoryofplannedbehavior.OrganBehavHumDecisProcess Heliyon9(10).https://doi.org/10.1016/j.heliyon.2023.e20644
50(2):179–211.https://doi.org/10.1016/0749-5978(91)90020-t Güvenİ,ŞimşirF(2020)Demandforecastingwithcolorparameterinretailapparel
Al-MashraieM,ChungSH,JeonHW(2020)Customerswitchingbehavioranalysis industryusingartificialneuralnetworks(ANN)andsupportvectormachines
in the telecommunication industry via push-pull-mooring framework: a (SVM)methods.ComputIndEng147:106678
machinelearningapproach.ComputIndEng144:106476.https://doi.org/10. H&M Group (2023) Retrieved from https://hmgroup.com/sustainability/
1016/j.cie.2020.106476 circularity-and-climate/materials/#:~:text=Recycled%20plastic&text=We%
Ansu-MensahP(2021)Greenproductawarenesseffectongreenpurchaseinten- 20then%20use%20this%20plastic,avoiding%20harm%20to%20our%20planet
tionsofUniversityStudents’:anemergingmarket’sperspective.FuturBusJ HajishirziR,CostaCJ,AparicioM(2022)Boostingsustainabilitythroughdigital
7(1).https://doi.org/10.1186/s43093-021-00094-5 transformation’s domains and resilience. Sustainability 14(3):1822. https://
Awoyera PO, Adesina A (2020) Plastic wastes to construction products: status, doi.org/10.3390/su14031822
limitations and future perspective. Case Stud Constr Mater 12. https://doi. Ho C-I, Liu Y, Chen M-C (2022) Factors influencing watching and purchase
org/10.1016/j.cscm.2020.e00330 intentions on live streaming platforms: from A 7PS marketing mix per-
BickartBA,RuthJA(2012)Greeneco-sealsandadvertisingpersuasion.JAdvert spective.Information13(5):239.https://doi.org/10.3390/info13050239
41(4):51–67.https://doi.org/10.1080/00913367.2012.10672457 JaheerMuktharKP,NagadeepaC,SelvaratnamDP,PushpaA,ShuklaN(2024)
BossiF,DiGruttolaF,MastrogiorgioA,D’ArcangeloS,LattanziN,MaliziaAP, Sustainable wardrobe: recycled clothing towards sustainability and eco-
Ricciardi E (2022) Estimating successful internal mobility: a comparison friendliness.DiscovSustain5(1).https://doi.org/10.1007/s43621-024-00358-4
betweenstructuralequationmodelsandmachinelearningalgorithms.Front JalilNA,FikryA,ZainuddinA(2016)Theimpactofstoreatmospherics,perceived
ArtifIntell5.https://doi.org/10.3389/frai.2022.848015 value, and customer satisfaction on behavioural intention. Procedia Econ
BoyerRHW,HunkaAD,VanacoreE,Brauer HB(2025)Whysomeconsumers Financ37:538–544.https://doi.org/10.1016/s2212-5671(16)30162-9
choosecircularandothersdonot:thesocialpracticeofshoppingforcircular JamshidiM(Behdad),RoshaniS,DaneshfarF,LalbakhshA,RoshaniS,ParandinF,
garments.CircEconSustainhttps://doi.org/10.1007/s43615-025-00527-1 MalekZ,TallaJ,PeroutkaZ,JamshidiA,HadjilooeiF,LalbakhshP(2022)
Brandão A, Costa AG (2021) Extending the theory of planned behaviour to Hybrid deep learning techniques for predicting complex phenomena: a
understandtheeffectsofbarrierstowardssustainablefashionconsumption. reviewonCovid-19AI3(2):416–433.https://doi.org/10.3390/ai3020025
EurBusRev33(5):742–774.https://doi.org/10.1108/ebr-11-2020-0306 Jamshidi M, Lalbakhsh A, Talla J, Peroutka Z, Hadjilooei F, Lalbakhsh P,
BrewerMK(2019)Slowfashioninafastfashionworld:promotingsustainability Mohyuddin W (2020) Artificial Intelligence and Covid-19: deep learning
andresponsibility.Laws8(4):24.https://doi.org/10.3390/laws8040024 approaches for diagnosis and treatment. IEEE Access 8:109581–109595.
Chang X, Xue Y, LiJ, Zou L, TangM (2019) Potential health impact ofenvir- https://doi.org/10.1109/access.2020.3001973
onmental micro‐ and Nanoplastics Pollution. J Appl Toxicol 40(1):4–15. JangH-S,XingS(2020)Amodeltopredictammoniaemissionusingamodified
https://doi.org/10.1002/jat.3915 geneticartificialneuralnetwork:analyzingCementmixedwithflyashfroma
ChenJ,LiQ,WangH,DengM(2019)Amachinelearningensembleapproach coal-fired power plant. Constr Build Mater 230:117025. https://doi.org/10.
basedonRandomForestandradialbasisfunctionneuralnetworkforrisk 1016/j.conbuildmat.2019.117025
evaluationofRegionalFloodDisaster:acasestudyoftheyangtzeriverdelta, Jena R, Pradhan B, Beydoun G, Nizamuddin, Ardiansyah, Sofyan H, Affan M
China. Int J Environ Res Public Health 17(1):49. https://doi.org/10.3390/ (2020)Integratedmodelforearthquakeriskassessmentusingneuralnetwork
ijerph17010049 and analytic hierarchy process: Aceh Province, Indonesia. Geosci Front
Chi T, Ganak J, Summers L, Adesanya O, McCoy L, Liu H, Tai Y (2021) 11(2):613–634.https://doi.org/10.1016/j.gsf.2019.07.006
Understandingperceivedvalueandpurchaseintentiontowardeco-friendly JinX,OmarA,FuK(2024)Factorsinfluencingpurchaseintentiontowardrecycled
athleisureapparel:InsightsfromU.S.millennials.Sustainability13(14):7946. apparel: evidence from China. Sustainability 16(9):3633. https://doi.org/10.
https://doi.org/10.3390/su13147946 3390/su16093633
Dangelico RM, Alvino L, Fraccascia L (2022) Investigating the antecedents of KalinićZ,MarinkovićV,KalinićL,Liébana-CabanillasF(2021)Neuralnetwork
consumer behavioral intention for sustainable fashion products: Evidence modelingofconsumersatisfactioninMobileCommerce:anempiricalana-
from a large survey of Italian consumers. Technol Forecast Soc Change lysis. Expert Syst Appl 175:114803. https://doi.org/10.1016/j.eswa.2021.
185:122010.https://doi.org/10.1016/j.techfore.2022.122010 114803
Eckle K, Schmidt-Hieber J (2019) A comparison of deep networks with ReLU Kar S, Basu K, Sarkar B (2023) Advertisement policy for dual-channel within
activation function and linear spline-type methods. Neural Netw emissions-controlled Flexible production system. J Retail Consum Serv
110:232–242.https://doi.org/10.1016/j.neunet.2018.11.005 71:103077.https://doi.org/10.1016/j.jretconser.2022.103077
EvodeN,QamarSA,BilalM,BarcelóD,IqbalHMN(2021)Plasticwasteandits Kim D, Kim J, Kim J (2020) Elastic exponential linear units for convolutional
management strategies for Environmental Sustainability. Case Stud Chem neural networks. Neurocomputing 406:253–266. https://doi.org/10.1016/j.
EnvironEng4:100142.https://doi.org/10.1016/j.cscee.2021.100142 neucom.2020.03.051
FanY,ChenJ,ShirkeyG,JohnR,WuSR,ParkH,ShaoC(2016)Applicationsof KimI,JungHJ,LeeY(2021)Consumers’valueandriskperceptionsofcircular
structuralequationmodeling(SEM)inEcologicalStudies:anupdatedreview. fashion:comparisonbetween secondhand, upcycled, andrecycledclothing.
EcolProcess5(1).https://doi.org/10.1186/s13717-016-0063-3 Sustainability13(3):1208.https://doi.org/10.3390/su13031208
FerioliM,GazzolaP,GrechiD,VătămănescuE-M(2022)Sustainablebehaviourof Kuah ATH, Wang P (2020) Circular economy and consumer acceptance: an
BCorpsfashioncompaniesduringCovid-19:aquantitativeeconomicana- exploratory study in East and Southeast Asia. J Clean Prod 247:119097.
lysis.JCleanProd374:134010.https://doi.org/10.1016/j.jclepro.2022.134010 https://doi.org/10.1016/j.jclepro.2019.119097
FungY-N,ChanH-L,ChoiT-M,LiuR(2021)Sustainableproductdevelopment LeeE-J,ChoiH,HanJ,KimDH,KoE,KimKH(2020)Howto“Nudge”your
processesinfashion:supplychainsstructuresandclassifications.IntJProd consumerstowardsustainablefashionconsumption:Anfmriinvestigation.J
Econ231:107911.https://doi.org/10.1016/j.ijpe.2020.107911 BusRes117:642–651.https://doi.org/10.1016/j.jbusres.2019.09.050
GansserOA,ReichCS(2023)Influenceofthenewecologicalparadigm(NEP)and LiM,VanberkelP,ZhongX(2022)Predictingambulanceoffloaddelayusinga
environmentalconcernsonpro-environmentalbehavioralintentionbasedon hybriddecisiontreemodel.Socio-EconPlanSci80:101146.https://doi.org/
thetheoryofplannedbehavior(TPB).JCleanProd382:134629.https://doi. 10.1016/j.seps.2021.101146
org/10.1016/j.jclepro.2022.134629 LinP-C,HuangY-H(2012)Theinfluencefactorsonchoicebehaviorregarding
German JD, Ong AK, Perwira Redi AA, Robas KP (2022a) Predicting factors green products based on the theory of consumption values. J Clean Prod
affecting the intention to use a 3PL during the COVID-19 pandemic: a 22(1):11–18.https://doi.org/10.1016/j.jclepro.2011.10.002
machinelearningensembleapproach.Heliyon8(11).https://doi.org/10.1016/ Lin S-C, Nadlifatin R, Amna A,Persada S, Razif M (2017) Investigating citizen
j.heliyon.2022.e11382 behavior intention on mandatory and voluntary Pro-Environmental
16 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
programs through a pro-environmental planned behavior model. Sustain- Rehman IH, Ahmad A, Akhter F, Aljarallah A (2022) A dual-stage SEM-Ann
ability9(7):1289.https://doi.org/10.3390/su9071289 analysistoexploreconsumeradoptionofsmartwearablehealthcaredevices.J
LiuP,LiM,DaiD,GuoL(2021)Theeffectsofsocialcommerceenvironmental GlobInfManag29(6):1–30.https://doi.org/10.4018/jgim.294123
characteristicsoncustomers’purchaseintentions:thechainmediatingeffect Roh T, Seok J, Kim Y (2022) Unveiling ways to reach organic purchase: green
ofcustomer-to-customerinteractionandcustomer-perceivedvalue.Electron perceivedvalue,perceivedknowledge,attitude,subjectivenorm,andTrust.J
CommerResAppl48:101073.https://doi.org/10.1016/j.elerap.2021.101073 RetailConsumServ67:102988.https://doi.org/10.1016/j.jretconser.2022.102988
MagnierL,MuggeR,SchoormansJ(2019)Turningoceangarbageintoproducts– SaricamC,OkurN(2018)Analysingtheconsumerbehaviorregardingsustainable
consumers’evaluationsofproductsmadeofRecycledOceanPlastic.JClean fashionusingtheoryofplannedbehavior.TextSciClothingTechnol1–37.
Prod215:84–98.https://doi.org/10.1016/j.jclepro.2018.12.246 https://doi.org/10.1007/978-981-13-1265-6_1
Milani L, Grumi S, Camisasca E, Miragoli S, Traficante D, Di Blasio P (2020) Sarkar B, Fan S-KS, Pareek S, Mridha B (2024) Sustainable multi-biofuel pro-
Familial risk and protective factors affecting CPS Professionals’ Child duction with stochastic lead time and Optimum Energy Utilization under
Removal Decision: a decision tree analysis study. Child Youth Serv Rev flexiblemanufacturing.ComputIndEng193:110223.https://doi.org/10.1016/
109:104687.https://doi.org/10.1016/j.childyouth.2019.104687 j.cie.2024.110223
MridhaB,SarkarB(2025)Implicationsofcarbonpoliciesforflexibledemandand Sarkar B, KarS,Basu K,GuchhaitR (2022) Asustainablemanagerial decision-
smartproductionwithRandomleadtimedemandunderasustainablesupply makingproblemforasubstitutableproductinadual-channelundercarbon
chainmanagement.EnvironDevSustainhttps://doi.org/10.1007/s10668-025- tax policy. Comput Ind Eng 172:108635. https://doi.org/10.1016/j.cie.2022.
06038-1 108635
Nadlifatin R, Lin S-C, Rachmaniati Y, Persada S, Razif M (2016) A pro- SarkarB,KarS,BasuK,SeoYW(2023)Istheonline-offlinebuy-online-pickup-in-
environmental reasoned action model for measuring citizens’ intentions store retail strategy best among other product delivery strategies under
regarding ecolabel product usage. Sustainability 8(11):1165. https://doi.org/ Variableleadtime?JRetailConsumServ73:103359.https://doi.org/10.1016/
10.3390/su8111165 j.jretconser.2023.103359
Nam C, Dong H, Lee Y-A (2017) Factors influencing consumers’ purchase Savari M, Gharechaee H (2020) Application of the extended theory of planned
intentionofGreenSportswear.FashionTextiles4(1).https://doi.org/10.1186/ behaviortopredictIranianfarmers’intentionforsafeuseofchemicalferti-
s40691-017-0091-3 lizers.JCleanProd263:121512.https://doi.org/10.1016/j.jclepro.2020.121512
Nanni L, Brahnam S, Paci M, Ghidoni S (2022) Comparison of different con- SedliačikováM,AláčP,MoresováM(2020)Howbehavioralaspectsinfluencethe
volutional neural network activation functions and methods for building sustainablefinancialdecisionsofshareholders:anempiricalstudyandpro-
ensemblesforsmalltomidsizemedicaldatasets.Sensors22(16):6129.https:// posal for a relevant decision-making concept. Sustainability 12(12):4813.
doi.org/10.3390/s22166129 https://doi.org/10.3390/su12124813
Nguyen XH, Tran HL, Nguyen QH, Luu TP, Dinh HL, Vu HT (2020) Factors ShamsM,AlamI,MahbubMS(2021)PlasticpollutionduringCOVID-19:plastic
influencingtheconsumer’sintentiontobuyfashionproductsmadebyrecycled wastedirectivesanditslong-termimpactontheenvironment.EnvironAdv
plasticwaste.ManagSciLett3613–3622.https://doi.org/10.5267/j.msl.2020.6.032 5:100119.https://doi.org/10.1016/j.envadv.2021.100119
Niinimäki K, Peters G, Dahlbo H, Perry P, Rissanen T, Gwilt A (2020) The SooraniF,AhmadvandM(2019)Determinantsofconsumers’foodmanagement
environmentalpriceofFastFashion.NatRevEarthEnviron1(4):189–200. behavior: applying and extending the theory of planned behavior. Waste
https://doi.org/10.1038/s43017-020-0039-9 Manag98:151–159.https://doi.org/10.1016/j.wasman.2019.08.025
NikeSustainability(2024)Retrievedfromhttps://www.nike.com/sustainability StrattonSJ(2021)Populationresearch:conveniencesamplingstrategies.Prehosp
OECD(2022)Retrievedfromhttps://www.oecd.org/environment/plastic-pollution- DisasterMed36(4):373–374.https://doi.org/10.1017/s1049023x21000649
is-growing-relentlessly-as-waste-management-and-recycling-fall-short.htm Talan A, Tyagi RD, Surampalli RY (2020) Social dimensions of sustainability.
OngAK,CordovaLN,LonganillaFA,CaprechoNL,JavierRA,BorresRD,Ger- Sustainability183–206.https://doi.org/10.1002/9781119434016.ch9
manJD(2023)Purchasingintentionsanalysisofhybridcarsusingrandom TestaF,DiIorioV,CerriJ,PretnerG(2021)Fiveshadesofplasticinfood:which
forestclassifieranddeeplearning.WorldElectrVehJ14(8):227.https://doi. potentiallycircularpackagingsolutionsareItalianconsumersmoresensitive
org/10.3390/wevj14080227 to. Resour, Conserv Recycling 173:105726. https://doi.org/10.1016/j.
OngAK,PrasetyoYT,SalazarJM,ErfeJJ,AbellaAA,YoungMN,ChuenyindeeT, resconrec.2021.105726
NadlifatinR,NgurahPerwiraRediAA(2022)Investigatingtheacceptanceof TezerA,BodurHO(2019)Thegreenconsumption effect:howusinggreenpro-
thereopeningbataannuclearpowerplant:integratingprotectionmotivation ductsimprovesconsumptionexperience.JConsumRes47(1):25–39.https://
theory and extended theory of planned behavior. Nucl Eng Technol doi.org/10.1093/jcr/ucz045
54(3):1115–1125.https://doi.org/10.1016/j.net.2021.08.032 Tiseo I (2023) Retrieved from https://www.statista.com/statistics/1270902/ocean-
OngAK,MendozaMC,PonceJR,BernardoKT,TolentinoSA,DiazJF,YoungMN plastic-pollution-from-select-rivers-worldwide
(2024)AnalysisofinvestmentbehavioramongFilipinos:integrationofsocial UzirMU,AlHalbusiH,ThurasamyR,ThiamHockRL,AljaberiMA,HasanN,
exchangetheory(SET)andthetheoryofplannedbehavior(TPB).PhysA: HamidM(2021)Theeffectsofservicequality,perceivedvalueandtrustin
StatMechAppl654:130162.https://doi.org/10.1016/j.physa.2024.130162 homedeliveryservicepersonneloncustomersatisfaction:Evidencefroma
ÖztürkOB,BaşarE(2022)Multiplelinearregressionanalysisandartificialneural developingcountry.JRetailConsumServ63:102721.https://doi.org/10.1016/
networks based decision support system for energy efficiency in shipping. j.jretconser.2021.102721
OceanEng243:110209.https://doi.org/10.1016/j.oceaneng.2021.110209 VishnoiSK,MathurS,AgarwalV,VirmaniN,JagtapS(2025)Whatdrivesgen-
Park HJ, Lin LM (2020) Exploring attitude–behavior gap in sustainable con- erationZtochooseGreenApparel?Unravelingtheimpactofenvironmental
sumption:comparisonofrecycledandupcycledfashionproducts.JBusRes knowledge,altruismandperceivedinnovativeness.IntJSustainEng18(1).
117:623–628.https://doi.org/10.1016/j.jbusres.2018.08.025 https://doi.org/10.1080/19397038.2025.2473986
PolyportisA,MuggeR,MagnierL(2022)Consumeracceptanceofproductsmade Waheed R, Sarwar S, Alsaggaf MI (2023) Relevance of energy, Green and blue
from recycled materials: a scoping review. Resour, Conserv Recycling factors to achieve sustainable economic growth: empirical study of Saudi
186:106533.https://doi.org/10.1016/j.resconrec.2022.106533 Arabia.TechnolForecastSocChange187:122184.https://doi.org/10.1016/j.
Pradhan B, Lee S (2010) Landslide susceptibility assessment and factor effect techfore.2022.122184
analysis: backpropagation artificial neural networks and their comparison WendorfCA(2002)Comparisonsofstructuralequationmodelingandhierarchical
with frequency ratio and bivariate logistic regression modelling. Environ linearmodelingapproachestocouples’data.StructEquModeling:AMul-
ModelSoftw25(6):747–759.https://doi.org/10.1016/j.envsoft.2009.10.016 tidiscipJ9(1):126–140.https://doi.org/10.1207/s15328007sem0901_7
Pranta AD, Tareque Rahaman Md, Reazuddin Repon Md, Shikder AA (2024) WoodyE(2011)AnSEMperspectiveonevaluatingmediation:whateveryclinical
Environmentally sustainable apparel merchandising of recycled cotton- researcherneedstoknow.JExpPsychopathol2(2):210–251.https://doi.org/
polyester blended garments: Analysis of consumer preferences and pur- 10.5127/jep.010410
chasing behaviors. J Open Innov: Technol Mark Complex 10(3):100357. XiangyangL,XingQ,HanZ,FengC(2023)Anovelactivationfunctionofdeep
https://doi.org/10.1016/j.joitmc.2024.100357 neuralnetwork.SciProgram2023:1–12.https://doi.org/10.1155/2023/3873561
Provin AP, Dutra AR, de Sousa e Silva Gouveia IC, Cubas EA (2021) Circular XuY,DuJ,KhanMA,JinS,AltafM,AnwarF,SharifI(2022)Effectsofsubjective
economyforfashionindustry:useofwastefromthefoodindustryforthe norms and environmental mechanism on Green Purchase Behavior: an
productionofBiotextiles.TechnolForecastSocChange169:120858.https:// extendedmodeloftheoryofplannedbehavior.FrontEnvironSci10.https://
doi.org/10.1016/j.techfore.2021.120858 doi.org/10.3389/fenvs.2022.779629
QiX,PloegerA(2019)Explainingconsumers’intentionstowardspurchasinggreen YousefzadehM,HosseiniSA,FarnaghiM(2021)Spatiotemporallyexplicitearth-
foodinQingdao,China:theAmendmentandextensionofthetheoryofplanned quake prediction using Deep Neural Network. Soil Dyn Earthq Eng
behavior.Appetite133:414–422.https://doi.org/10.1016/j.appet.2018.12.004 144:106663.https://doi.org/10.1016/j.soildyn.2021.106663
RauschTM,KopplinCS(2021)Bridgethegap:consumers’purchaseintentionand ZhangB,ZhangY,ZhouP(2021)Consumerattitudetowardssustainabilityoffast
behaviorregardingsustainableclothing.JCleanProd278:123882.https://doi. fashion products in the UK. Sustainability 13(4):1646. https://doi.org/10.
org/10.1016/j.jclepro.2020.123882 3390/su13041646
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z 17

ARTICLE
HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS|https://doi.org/10.1057/s41599-025-05205-z
ZhangL,FanY,ZhangW,ZhangS(2019)Extendingthetheoryofplannedbehavior standardofthe1964HelsinkiDeclaration.Thedataentailsnotraceableinformation
toexplaintheeffectsofcognitivefactorsacrossdifferentkindsofgreenpro- amongrespondentsandwaskeptinasecuredatabase.ThiswasapprovedbyDr.
ducts.Sustainability11(15):4222.https://doi.org/10.3390/su11154222 JosephineD.German(committeemember)andDr.MichaelN.Young(committeehead)
Zhang Z, Malik MZ, Khan A, Ali N, Malik S, Bilal M (2022) Environmental onMarch20,2023.
impactsofhazardouswaste,andmanagementstrategiestoreconcilecircular
economy and eco-sustainability. Sci Total Environ 807:150856. https://doi. Informed consent
org/10.1016/j.scitotenv.2021.150856
Informedconsentwasobtainedfromallsubjectsthroughwrittenform,involvedinthis
study(FM-RC-22-02-01)duringthedatacollectionprocessfromMarch27,2023—
Acknowledgements August2023.Inaccordance,aconfirmationquestionofapprovalamongrespondents
werecollectedasthefirstquestionintheonlinequestionnairetoensureapproval.
ThisresearchwasfundedbyUniversityDirectedResearchforInnovationandValue
Participantswereassuredthattraceableinformationwouldnotbecollected,response
Enhancement(DRIVE).
wouldbeanonymous,andtheirdataprivacywillbesecured.
Author contributions
Additional information
CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.
SupplementaryinformationTheonlineversioncontainssupplementarymaterial
Cahigas,Ma.JaniceJ.Gumasing:Conceptualization;CarmellaAndreaL.Cabrera,
availableathttps://doi.org/10.1057/s41599-025-05205-z.
ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.
Gumasing:Datacuration;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,John
CorrespondenceandrequestsformaterialsshouldbeaddressedtoArdvinKesterS.Ong.
FrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Formalanalysis;
ArdvinKesterS.Ong:Fundingacquisition;CarmellaAndreaL.Cabrera,ArdvinKester
Reprintsandpermissioninformationisavailableathttp://www.nature.com/reprints
S.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Inves-
tigation;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong:Methodology;ArdvinKester Publisher’snoteSpringerNatureremainsneutralwithregardtojurisdictionalclaimsin
S.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Project publishedmapsandinstitutionalaffiliations.
administration;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz:
Resources;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,
MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Software;ArdvinKesterS.Ong,John
Open Access This article is licensed under a Creative Commons
FrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Supervision;Carmella
AndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas, Attribution-NonCommercial-NoDerivatives 4.0 International License,
Ma.JaniceJ.Gumasing:Validation;CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong, whichpermitsanynon-commercialuse,sharing,distributionandreproductioninany
JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.JaniceJ.Gumasing:Visualization; mediumorformat,aslongasyougiveappropriatecredittotheoriginalauthor(s)and
CarmellaAndreaL.Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.
thesource,providealinktotheCreativeCommonslicence,andindicateifyoumodified
Cahigas,Ma.JaniceJ.Gumasing:Roles/Writing–originaldraft;CarmellaAndreaL. thelicensedmaterial.Youdonothavepermissionunderthislicencetoshareadapted
Cabrera,ArdvinKesterS.Ong,JohnFrancisT.Diaz,MaelaMadelL.Cahigas,Ma.Janice materialderivedfromthisarticleorpartsofit.Theimagesorotherthirdpartymaterial
J.Gumasing:Writing-review&editing.
inthisarticleareincludedinthearticle’sCreativeCommonslicence,unlessindicated
otherwise in a credit line to the material. If material is not included in the article’s
Creative Commons licence and your intended use is not permitted by statutory
Competing interests
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfrom
Theauthorsdeclarenocompetinginterests. thecopyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/
licenses/by-nc-nd/4.0/.
Ethical approval
ThisstudywasapprovedbytheMapuaUniversityResearchEthicsCommittees(FM-RC-
©TheAuthor(s)2025
22-01-01),followingproperrelevantguidelinescuratedbytheuniversityandtheethical
18 HUMANITIESANDSOCIALSCIENCESCOMMUNICATIONS| (2025) 12:822 |https://doi.org/10.1057/s41599-025-05205-z