---
conversion_metadata:
  converted_at: "2026-07-22T12:23:39Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Boniol et al.pdf"
  source_pdf_sha256: "8b6df2d250d9fbbf868a557cef169279cf744c7c39fbb156f1055875527280ad"
  page_count: 51
  markdown_char_count: 378119
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

4
2
0
2

c
e
D
9
2

]

G
L
.
s
c
[

1
v
2
1
5
0
2
.
2
1
4
2
:
v
i
X
r
a

Dive into Time-Series Anomaly Detection: A Decade Review

PAUL BONIOL, Inria, DI ENS, PSL, CNRS, France
QINGHUA LIU, The Ohio State University, USA
MINGYI HUANG, The Ohio State University, USA
THEMIS PALPANAS, Université Paris Cité; IUF, France
JOHN PAPARRIZOS, The Ohio State University, USA

Recent advances in data collection technology, accompanied by the ever-rising volume and velocity of streaming data, underscore the

vital need for time series analytics. In this regard, time-series anomaly detection has been an important activity, entailing various

applications in fields such as cyber security, financial markets, law enforcement, and health care. While traditional literature on

anomaly detection is centered on statistical measures, the increasing number of machine learning algorithms in recent years call for a

structured, general characterization of the research methods for time-series anomaly detection. This survey groups and summarizes

anomaly detection existing solutions under a process-centric taxonomy in the time series context. In addition to giving an original

categorization of anomaly detection methods, we also perform a meta-analysis of the literature and outline general trends in time-series

anomaly detection research.

ACM Reference Format:

Paul Boniol, Qinghua Liu, Mingyi Huang, Themis Palpanas, and John Paparrizos. 2024. Dive into Time-Series Anomaly Detection: A

Decade Review. In Proceedings of Make sure to enter the correct conference title from your rights confirmation emai (Conference acronym

’XX). ACM, New York, NY, USA, 51 pages. https://doi.org/XXXXXXX.XXXXXXX

1 Introduction

A wide range of cost-effective sensing, networking, storage, and processing solutions enable the collection of enormous

amounts of measurements over time [109–111, 122, 137, 138, 141, 143, 179, 181, 186]. Recording these measurements

results in an ordered sequence of real-valued data points commonly referred to as time series. More generic terms, such

as data series or data sequences, have also been used to refer to cases where the ordering of data relies on a dimension

other than time (e.g., the angle in data from astronomy, the mass in data from spectrometry, or the position in data

from biology) [176]. Analytical tasks over time series data are necessary virtually in every scientific discipline and

their corresponding industries [14, 61, 62, 78, 161, 182, 190–192, 201], including in astronomy [4, 102, 245], biology

[11–13, 64], economics [36, 74, 148, 155, 213, 221, 240], energy sciences [6, 9, 158], engineering [112, 162, 203, 243, 248],

environmental sciences [77, 84, 100, 101, 164, 207, 247], medicine [57, 199, 206], neuroscience [21, 119], and social

sciences [36, 160]. The analysis of time series has become increasingly prevalent for understanding a multitude of

natural or human-made processes [187, 188]. Unfortunately, inherent complexities in the data generation of these

Authors’ Contact Information: Paul Boniol, Inria, DI ENS, PSL, CNRS, Paris, France, paul.boniol@inria.fr; Qinghua Liu, The Ohio State University,
Columbus, USA, liu.11085@osu.edu; Mingyi Huang, The Ohio State University, Columbus, USA, huang.5749@osu.edu; Themis Palpanas, Université Paris
Cité; IUF, Paris, France, themis@mi.parisdescartes.fr; John Paparrizos, The Ohio State University, Columbus, USA, paparrizos.1@osu.edu.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not
made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components
of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on
servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Manuscript submitted to ACM

Manuscript submitted to ACM

1

---

<!-- PAGE 2 -->

2

Paparrizos et al.

processes, combined with imperfections in the measurement systems as well as interactions with malicious actors,

often result in abnormal phenomena. Such abnormal events appear subsequently in the collected data as anomalies.

Considering that the volume of the produced time series will continue to rise due to the explosion of Internet-of-Things

(IoT) applications [75, 105, 151], an abundance of anomalies is expected in time series collections.

The detection of anomalies in time series has received ample academic and industrial attention for over six decades

[1, 27–30, 32, 39, 69, 121, 142, 159, 165, 175, 180, 185, 235, 239]. With the term anomalies we refer to data points or

groups of data points that do not conform to some notion of normality or an expected behavior based on previously

observed data [16, 45, 80, 91, 107]. In the literature, alternative terms such as outliers, novelties, exceptions, peculiarities,

aberrations, deviants, or discords often appear to describe the occurrences of such rare, unusual, often hard-to-explain

anomalous patterns [2, 40, 65]. Depending on the application, anomalies can constitute [2]: (i) noise or erroneous data,

which hinders the data analysis; or (ii) actual data of interest. In the former case, the anomalies are unwanted data that

are removed or corrected. In the latter case, the anomalies may identify meaningful events, such as failures or changes

in behavior, which are the basis for subsequent analysis.

Regardless of the purpose of the time series and the semantic meaning of anomalies, anomaly detection describes the

process of analyzing a time series for identifying unusual patterns, which is a challenging task because many types of

anomalies exist. They appear in different sizes and shapes. According to Foorthuis [68], research on general-purpose

anomaly detection dates back to 1777, where Bernoulli’s work seems to be the first addressing issues of accepting or

rejecting extreme cases of observations [19]. Robust theory in that area was developed during the 1800s (e.g., method of

least squares in 1805 [225]) [63, 76, 83, 198, 230] and 1900s [60, 85, 106, 197, 212] but it was not until the 1950s when

the first works focused specifically in time series data [175]. In 1972, Fox conducted one of the first studies to examine

anomalous behaviors across time and defined two types of anomalies: (i) an anomaly affecting a single observation; and

(ii) an anomaly affecting an observation and subsequent observations [69]. In 1988, Tsay extended these definitions into

four types for univariate time series [239] and subsequently for multivariate time series [241]. In the same time frame,

the first few approaches appear for detecting anomalies in time series, with a focus on utilizing statistical tests such as

the Likelihood-ratio test [48, 242]

Since then, a large number of works have appeared in this area, which continues to expand at a rapid pace. Additionally,

numerous surveys have been published to provide an overview of the current advancements in this field [22, 33, 43, 46,

47, 54, 56, 86, 99]. Unfortunately, the majority of the surveys focus on general-purpose anomaly detection methods and

only a portion of them briefly review methods for time-series anomaly detection. Even though traditional anomaly

detection methods may treat time series as any other high-dimensional vector and attempt to detect anomalies, our focus

is on approaches that are specifically designed to consider characteristics of time series. To illustrate the importance of

this point, in Figure 1, we present three examples of anomalies in time series applications where the temporal ordering

and the collective consideration of points enable the detection of anomalies. For example, in 1(a), considering each

point in isolation cannot reveal the underlying anomaly in data.

Therefore, time-ordering features are important to be considered in the anomaly detection pipeline. Depending on

the research community, multiple solutions have been proposed to tackle the above-mentioned challenge. For example,

a group of methods proposed in the literature will propose a transformation step that converts time information into a

relevant vector space and then apply traditional outlier detection techniques. In addition, other groups of methods will

consider distances (or similarity measures dedicated to time series) to identify unusual time series or subsequences.

Then, methods proposed in the deep learning community will benefit from specific architectures that embed time

information (such as recurrent neural networks or convolutional-based approaches).

Manuscript submitted to ACM

---

<!-- PAGE 3 -->

Dive into Time-Series Anomaly Detection: A Decade Review

3

Fig. 1. Examples of different time series applications and types of anomalies.

Unfortunately, these areas remain mostly disconnected, using different datasets, baselines, and evaluation measures.

New algorithms are evaluated only against non-representative subsets of approaches and it is virtually impossible

to find the best state-of-the-art approach for a concrete use case. To remedy this issue, this survey presents a novel,

comprehensive, process-centric taxonomy for the multiple detection methods in each category. We collected a compre-

hensive range of algorithms in the literature and grouped them into families of algorithms with similar approaches. In

addition, to identify research trends, we also provide statistics on the type and area of proposed approaches over time.

Then, we also list existing benchmarks that can be used as a common ground on which new proposed methods

(regardless of the community) should be evaluated. Finally, we enumerate existing evaluation measures usually used to

evaluate anomaly detection methods while discussing their limitation and benefits when applied to the specific case of

time series.

2 Time-Series Anomaly Detection Overview

In this section, we discuss the problem formulation for time-series anomaly detection algorithms and motivate our

process-centric taxonomy.

Manuscript submitted to ACM

---

<!-- PAGE 4 -->

4

Paparrizos et al.

2.1 On the Definition of Anomalies in Time Series

Attesting to the challenging nature of the problem at hand, we observe that there does not exist a single, universal,

precise definition of anomalies or outliers. Traditionally, anomalies are observations that deviate considerably from the

majority of other samples in a distribution. The anomalous points raise suspicions that a mechanism different from

those of the other data generated the specific observation. Such a mechanism usually represents either an erroneous

data measurement procedure or an unusual event.

In cases of errors in the data measurement procedure, the anomalous observations are marked as “noise" – unwanted

data that are not attractive to the analyst and should be removed in the data cleaning process. Many pieces of literature

have been dedicated to this type of problem, particularly in the sensor setting, where the main objective is to eliminate

transmission error and render accurate predictions. In time-series anomaly detection, however, recent literature begins

to center on detecting anomalous events, which indicate “novelty" – unusual but interesting phenomena that originate

from an inherent variability in the domain of the data. A natural example of this type of problem is fraud detection for

credit information, where the principal aim is to detect and analyze the fraud itself.

The detection of these two types of anomalies (anomalies and outliers can be used interchangeably) can be achieved

via expert knowledge. By knowing exactly how the system works, the experts can set the parameter to fit a distribution

of values that represent the healthy functioning state. Anomalies are then detected by marking points of more than

three standard deviations away from the mean of data distribution estimated by the experts. To validate the detection

process, we also need to perform extensive tests to test the distribution (and its parameters) against the dataset.

Nevertheless, in several real-world problems, we do not know precisely the data distribution that has generated a set

of points (and all the different artifacts that played a role). Besides, the data distributions that we encounter in practice,

are almost always rather complex and very hard to identify or approximate effectively. Consequently, defining and

identifying anomalies using their distance from a mean value defined by experts is sometimes hardly practical.

Despite the challenge of estimating distribution parameters by experts, recent developments in computational power

have liberated us from an alternative approach to analyzing data distribution from the data itself. Using a variety of

learning methods, researchers may apply computer algorithms to analyze raw data, estimate a fair distribution, and

detect anomalies without expert knowledge. Even though being strongly dependent on the quality and the context of

the datasets, these methods seem to show strong results in achieving relatively complex tasks. In this paper, we focus

on this type of method.

2.2 Types of Anomalies in Time Series

There is a further complication in time-series anomaly detection. Due to the temporality of the data, anomalies can

occur in the form of a single value or collectively in the form of sub-sequences. In the specific context of point, we are

interested in finding points that are far from the usual distribution of values that correspond to healthy states. In the

specific context of sequences, we are interested in identifying anomalous sub-sequences, which are usually not outliers

but exhibit rare and, hence, anomalous patterns. In real-world applications, such a distinction between points and

sub-sequences becomes crucial because even though individual points might seem normal against their neighboring

points, the shape generated by the sequence of these points may be anomalous.

Formally, we define three types of time series anomalies: point, contextual, and collective anomalies. Point anomalies

refer to data points that deviate remarkably from the rest of the data. Figure 2(a) depicts a synthetic time series with a

point anomaly: the value of the anomaly is outside the expected range of normal values. Contextual anomalies refer to

Manuscript submitted to ACM

---

<!-- PAGE 5 -->

Dive into Time-Series Anomaly Detection: A Decade Review

5

Fig. 2. Synthetic illustration of the three time series anomaly types: (a) point; (b) contextual; and (c) collective anomalies.

data points within the expected range of the distribution (in contrast to point anomalies) but deviate from the expected

data distribution, given a specific context (e.g., a window). Figure 2(b) illustrates a time series with a contextual anomaly:

the anomaly is within the usual range of values (left distribution plot of Figure 2(b)) but outside the normal range

of values for a local window (right distribution plot of Figure 2(b)). Collective anomalies refer to sequences of points

that do not repeat a typical (previously observed) pattern. Figure 2(c) depicts a synthetic collective anomaly. The first

two categories, namely, point and contextual anomalies, are referred to as point-based anomalies. whereas, collective

anomalies are referred to as sequence-based anomalies.

As an additional note, there is another case of sub-sequence anomaly detection referred to as whole-sequence

detection, relative to the point detection. In this case, the period of the sub-sequence is that of the entire time series,

and the entire time series is evaluated for anomaly detection as a whole. This is typically the case in the sensor cleaning

environment where researchers are interested in finding an abnormal sensor among all the functioning sensors.

2.3 Univariate versus Multivariate

Another characteristic of time-series anomaly detection algorithms comes from the dimensionality of the data. Univariate

time series consists of an ordered sequence of real values on a single dimension, and the anomalies are detected based

on one single feature. In this case, as illustrated in Figure 3(b.1), a subsequence can be represented as a vector. On the

other hand, Multivariate time series is either a set of ordered sequences of real values (with each ordered sequence

having the same length) or an ordered sequence of vectors composed of real values. In this specific case, as illustrated

in Figure 3(b.2), a subsequence is a matrix in which each line corresponds to a subsequence of one single dimension.

Instances of anomalies are detected according to multiple features, where values of one feature, when singled out, may

look normal despite the abnormality of the sequence as a whole.

2.4 Unsupervised, Semi-supervised versus Supervised

This task can be divided into three distinct cases: (i) experts do not have information on what anomalies to detect;

(ii) experts only have information on the expected normal behaviors; (iii) experts have precise examples of which

Manuscript submitted to ACM

---

<!-- PAGE 6 -->

6

Paparrizos et al.

Fig. 3. Synthetic example comparing anomalies in univariate and multivariate time series for (a) a point outlier and (b) a sequence
outlier.

anomalies they have to detect (and have a collection of known anomalies). This gives rise to the distinction among (i)

unsupervised, (ii) semi-supervised, and (iii) supervised methods.

Unsupervised: In case (i), one can decide to adopt a fully unsupervised method. These methods have the benefit of

working without the need for a large collection of known anomalies and can detect unknown abnormal behavior

automatically. Such methods can be used either to monitor the health state or to mine the historical time series of a

system (to build a collection of abnormal behaviors that can then be used on a supervised framework).

Semi-supervised: In case (ii), methods can learn to detect anomalies based on annotated examples of normal sequences

provided by the experts. This is the classical case for most of the anomaly detection methods in the literature. One

should note that this category is often defined as Unsupervised. However, we consider it unfair to group such methods

with the category mentioned above, knowing that they require much more prior knowledge than the previous one.

Supervised: While in case (i) and (ii) anomalies were considered unknown, in case (iii), we consider that the experts

know precisely, what type of pattern(s) they want to detect, and that a collection of time series with labeled anomalies

is available. In that case, we have a database of anomalies at our disposal. In a supervised setting, one may be interested

in predicting the abnormal sub-sequence by its prior sub-sequences. Such sub-sequences can be called precursors of

anomalies.

2.5 Anomaly Detection Pipelines

Upon summarizing the various different algorithms on different domains, we realized a common pipeline for time-series

anomaly detection algorithms. The pipeline consists of four parts: data pre-processing, detection method, scoring, and

post-processing. Figure 4 illustrates the process. The decomposition of the general anomaly detection process into small

steps of a pipeline is beneficial for comparing different algorithms on various dimensions. Understanding of algorithms’

function in the pre-processing step helps interpret its treatment of time series data specifically.

Manuscript submitted to ACM

---

<!-- PAGE 7 -->

Dive into Time-Series Anomaly Detection: A Decade Review

7

Fig. 4. Time series anomaly detection pipeline.

The data processing step represents how the anomaly detection method processes the time series data at the initial step.

We have noticed all the anomaly detection models are somehow based on a windowed approach initially - converting

the time series data into a matrix with rows of sliding window slices of the original time series. The pre-processing

step consists of the additional processing procedure besides the window transformation, which varies from statistical

feature extraction to fitting a machine learning model and building a neural network.

After the data is processed, different detection methods are implemented on the dataset, which might be simply

calculating distances among the processed sub-sequences, fitting a classification hyper-plane, or using the processed

model to generate new sub-sequences and comparing them with original sub-sequences. The detection methods are

usually traditional outlier detection methods for vector data.

Then, during the scoring process, the results derived in the detection methods will be converted to an anomaly score

that assesses the abnormality of individual sub-sequences by a real value (such as a probability of being an anomaly).

The scores will be further used to infer the score of the individual point. The resulting score is a time series of the same

length as the initial time series.

Lastly, during the post-processing step, the anomaly score time series is processed to extract the anomalous points or

intervals. Usually, a threshold value will be determined, where the points with anomaly scores surpassing the threshold

will be marked as the anomaly.

This categorization of time-series anomaly detection pipelines inspires our process-centric taxonomy of the detection

methods, which will be discussed thoroughly in the next section.

3 Anomaly Detection Taxonomy

In this section, we describe our proposed process-centric taxonomy of the detection methods. We divide methods

into three categories: (i) distance-based, (ii) density-based, and (iii) prediction-based. The first family contains methods

that focus on the analysis of sub-sequences for the purpose of detecting anomalies in time series, mainly by utilizing

distances to a given model. Second, instead of measuring nearest-neighbor distances, density-based methods focus on

detecting globally normal or isolated behaviors. Third, prediction-based methods aim to train a model (on anomaly-free

time series or with very few anomalies) to reconstruct the normal data or predict the future expected normal points.

Manuscript submitted to ACM

---

<!-- PAGE 8 -->

8

Paparrizos et al.

Fig. 5. Process-centric anomaly detection taxonomy.

In the following sections, we break down each category into process-centric subcategories. Figure 5 illustrates our

proposed process-centric taxonomy.

Note that the second-level categorization is not mutually exclusive. A model might compress the time series data

while adopting a discord-based identification strategy. In this case, the model falls within two different sub-categories.

In the table of methods, only one of the second-level will be listed to give a clearer representation.

3.0.1 Distance-based. As its name suggests, the distance-based method detects anomalies purely from the raw time
series using distance measures. Given two sequences (or univariate time series), 𝐴 ∈ Rℓ and 𝐵 ∈ Rℓ , of the same length,
ℓ, we define the distance between 𝐴 and 𝐵 as 𝑑 (𝐴, 𝐵) ∈ R, such as 𝑑 (𝐴, 𝐵) = 0 when 𝐴 and 𝐵 are the same. There
exist different definitions of 𝑑 in the literature. The classical distance widely used is the Euclidean distance or the
Z-normalized Euclidean distance (Euclidean distance with sequences of mean values equal to 0 and standard deviations

equal to 1). Then, Dynamic Time Warping (DTW) is commonly used to cope with misalignment issues. Overall, the

distance-based algorithms merely treat the numerical value of time series as it is, without further modifications such as

removing seasonality or introducing a new structure built on the data. Within the distance-based models, there come

three second-level categories: proximity-based, clustering-based, and discord-based models.

(1) The proximity-based model measures proximity by calculating the distance of a given sub-sequence to its

close neighborhood. The isolation of a sub-sequence with regards to its closest neighbors is the main criterion to

consider if this sub-sequence is an anomaly or not. This notion of isolation with regard to a given neighborhood

has been proposed for non-time series data. Thus, the methods contained in this category have been introduced

for the general case of multi-dimensional outlier detection. In our specific case, the sub-sequence of a time

series can be considered a multi-dimensional point with the number of dimensions equal to the length of the

sub-sequence.

(2) The clustering-based model infers anomalies from a cluster partition of the time series sub-sequences. In

practice, the anomaly score is calculated by the non-membership of a sub-sequence of each of the clusters learned

by the model. Other considerations, such as cluster distance and cluster capacity, can also be considered. The

clustering issue is related to the anomaly detection problem in that points may either belong to a cluster or

be deemed anomalies. In practice, the fact that a sub-sequence belongs or not to a cluster is assessed by the

computation of the distance between this sub-sequence and the cluster centroid or medoid.

Manuscript submitted to ACM

---

<!-- PAGE 9 -->

Dive into Time-Series Anomaly Detection: A Decade Review

9

(3) The discord-based model tries to identify efficiently specific types of sub-sequences in the time series named
discord. Formally, a sub-sequence 𝐴 (or a given length ℓ) is a discord, if the distance between its nearest neighbor
is the largest among all the nearest neighbors’ distances computed between sub-sequences of length ℓ in the
time series. Overall, similarly to proximity-based methods, The isolation of a sub-sequence with regards to

its closest neighbors is the main criterion to consider if this sub-sequence is an anomaly or not. However, on

contrary to proximity-based methods, discord-based methods have been introduced for the specific case of

anomaly detection in time series. Thus, as such methods introduced efficient processes for time series distance

computation specifically, we group them into one different sub-category.

3.0.2 Density-based. The density-based does not treat the time series as simple numerical values but imbues them

with more complex architecture. The density-based method processes time series data on top of a representation of

the time series that aims to measure the density of the points or sub-sequence space. Such representation varies from

graphs, trees, and histograms to a grammar induction rule. The density-based models have four second-level categories:

distribution-based, graph-based, tree-based, and encoding-based.

(1) The distribution-based anomaly detection approach is building a distribution from statistical features of the

points or sub-sequences of the time series. By examining the distributions of features of the normal sub-sequences,

it tries to recover relevant statistical models and then uses them to infer the abnormality of the data.

(2) A graph-based method represents the time series and the corresponding sub-sequences as a graph. The nodes

and edges represent the different types of sub-sequences (or representative features) and their evolution in time.

For instance, the nodes can be sets of similar sub-sequences (using a predefined distance measure), and the edge

weights can be the number of times a sub-sequence of a given node has been followed by a sub-sequence of

another node. The detection of anomalies is then achieved using characteristics of the graph, such as the node

and edge weights, but also the degree of the nodes.

(3) A tree-based approach aims to divide the point or sub-sequence of a time series using trees. For instance, such

trees can be used to split different points or sub-sequences based on their similarity. The detection of anomalies

is then based on the statistics and characteristics of the tree, such as its depth.

(4) A encoding-based anomaly detection model compresses or represents the time series into different forms of

symbols. The encoding-based model suggests that a time series can be interpreted as a sequence of context-free,

discrete symbols or states. For instance, anomalies can be detected by using grammar rules with the symbols

extracted from the time series. It should be noted that an encoding-based model is not exclusive to itself; it may

even be based on a graph-based or tree-based model.

3.0.3 Prediction-based. Prediction-based methods aim to detect anomalies by predicting the expected normal

behaviors based on a training set of time series or sub-sequences (containing anomalies or not). For instance, some

methods will be trained to predict the next value or sub-sequence based on the previous one. The prediction is then

post-processed to detect abnormal points or sub-sequences. Then, the prediction error is used as an anomaly score.

The underlying assumption of prediction-based methods is that normal data are easier to predict, while anomalies

are unexpected, leading to higher prediction errors. Such assumptions are valid when the training set contains no or

few time series with anomalies. Therefore, prediction-based methods are usually more optimal under semi-supervised

settings.

Manuscript submitted to ACM

---

<!-- PAGE 10 -->

10

Paparrizos et al.

Fig. 6. The scoring process.

(1) The forecasting-based method is a model that, for a given index or timestamp, takes as input points or sub-

sequences before this given timestamp and predicts its corresponding value or sub-sequence. In other words,

such methods use past values as input to predict the following one. The forecasting error (the difference between

the predicted and the real value) is used as an anomaly score. Indeed, such forecasting error is representative of

the expectation of the current value based on the previous points or sub-sequences. The larger the error, the more

unexpected the value, and thus, potentially abnormal. Forecasting-based approaches assume that the training

data (past values or sub-sequences) is almost anomaly-free. Thus, such methods are mostly semi-supervised.

(2) The reconstruction-based method corresponds to a model that compresses the input time series (or sub-

sequence) into a latent space (smaller than the input size) and is trained to reconstruct the input time series

from the latent space. The difference between the input time series and the reconstructed one (named the

reconstruction error) is used as an anomaly score. As for forecasting-based methods, the larger the error, the

more unexpected the value, and thus, potentially abnormal. Moreover, as the reconstruction error is likely to be

small for the time series used to train the model, such reconstruction methods are optimal in semi-supervised

settings.

3.1 Scoring Process

As summarized in the pipeline, anomaly detection algorithms distinguish outliers by inference on the “anomaly scores"

of each temporal data point. The anomalies are marked by points whose scores exceed the threshold value. Due to the

special features of time series data, a further general categorization can be provided based on the algorithm’s strategy

of scoring the anomalies. We include this generalization as a complement to our taxonomy.

Manuscript submitted to ACM

---

<!-- PAGE 11 -->

Dive into Time-Series Anomaly Detection: A Decade Review

11

Fig. 7. Result using | Z | = 16 for a autoencoder Encoder(𝐶𝑜𝑛𝑣 (64, 3)-𝑅𝑒𝑙𝑢 ()-𝐷𝑒𝑛𝑠𝑒 ()-𝑇 𝑎𝑛ℎ ()), Decoder(𝐷𝑒𝐶𝑜𝑛𝑣 (64, 3)-𝑅𝑒𝑙𝑢 ()-
𝐷𝑒𝑛𝑠𝑒 ()-𝑇 𝑎𝑛ℎ ()). Top plot: Input time series snippet. Bottom plot: 𝑆 (using mean square error) for all the sub-sequences of length 80.

A forecasting-first approach first infers the values of interested time series, without knowing the actual values of the

dataset, and then determines if the coming data points are anomalies (based on their distance to the inferred values).

This gives possibilities for streaming data anomaly detection. A data-first approach, on the other hand, reads the data

first to update the model. Then, the entire training data samples will be used to compare with the arriving data via the

detection model. Figure 6 gives an illustration of the two.

Just like forecasting-first algorithms, data-first algorithms may also be capable of generating new sub-sequences to

compare with original sequences. Figure 7 gives such an example, where the autoencoder reconstructs an estimated
sequence 𝑇 ′
𝑖,𝑙 to calculate the error 𝑆 on the ECG data. Although it behaves like a forecasting-first method by trying to
“forecast" the original sub-sequences, it is technically data-first because it requires the arrival of new data to make valid

comparisons.

4 Survey Organization

In the following sections, we will present the State-Of-The-Art (SOTA) in the three major categories and elaborate on

the specific variants of the SOTA proposed in the past literature. Figure 8 illustrates our detailed proposed taxonomy

listing all the methods discussed in this paper. Note that, in Figure 8, the names of the methods (the first letter) are

positioned on the y-axis based on their publication date. Even though some concepts might be anterior to the date

indicated in Figure 8 (for instance the concept of k-means was introduced in 1967), the dates correspond to the first

paper discussing the concepts applied to anomaly detection. The rest of this paper is organized as follows:

• We first present distance-based methods that perform anomaly detection using distance computation and

comparisons on points or sub-sequences of the time series.

• Next we enumerate the density-based methods. These approaches process time series data on top of a represen-

tation that aims to measure the density of the points or sub-sequences within the time series space.

• We furnish with two groups of prediction-based methods that aim to predict the expected normal behaviors
from a training set of time series. These two groups are forecasting-based methods (that use the forecasting error

as anomaly score) and reconstruction-based methods (that are trained to reconstruct an input time series and

use the reconstruction error as anomaly score).

• We will also include a table of all the methods in each section to reveal their other characteristics (such as the
requirement for supervision, the capability of handling streaming data, etc) as complements to our taxonomy.

Manuscript submitted to ACM

---

<!-- PAGE 12 -->

12

Paparrizos et al.

Fig. 8. Illustration of Anomaly Detection Taxonomy for all methods.

• After briefly describing all the methods, we will discuss a meta-analysis of the time-series anomaly detection
community by examining the evolution and the trends of each category (distance-based, density-based, prediction-

based). We will also have a closer look at the evolution in time of proposed methods that are semi-supervised,

unsupervised, and able to handle multivariate time series.

• We will conclude this survey with the evaluation of such methods. We will first enumerate existing benchmarks
proposed in the literature, as well as different evaluation measures and their limitations when applied to time-

series anomaly detection.

5 Time Series Notations
We now introduce some formal notations related to time series. We define a time series 𝑇 ∈ R𝑛 as a sequence of
real-valued numbers 𝑇𝑖 ∈ R [𝑇0,𝑇2, ...,𝑇𝑛−1], where 𝑛 = |𝑇 | is the length of 𝑇 , and 𝑇𝑖 is the 𝑖𝑡ℎ point of 𝑇 .

A multivariate, or 𝐷-dimensional time series T ∈ R(𝐷,𝑛) is a set of 𝐷 univariate time series of length 𝑛. We note
]. A

T = [𝑇 (0), ...,𝑇 (𝐷 −1) ] and for 𝑗 ∈ [0, 𝐷 − 1], we note the univariate time series 𝑇 ( 𝑗 ) = [𝑇 ( 𝑗 )
Manuscript submitted to ACM

, ...,𝑇 ( 𝑗 )
𝑛−1

,𝑇 ( 𝑗 )
1

0

---

<!-- PAGE 13 -->

Dive into Time-Series Anomaly Detection: A Decade Review

13

subsequence 𝑇 ( 𝑗 )
of length ℓ (usually ℓ ≪ 𝑛) starting at position 𝑖; formally, 𝑇 ( 𝑗 )
, ...,𝑇 (𝐷 −1)
is defined as 𝑇𝑖,ℓ = [𝑇 (0)
𝑖,ℓ
𝑖,ℓ
defined as Tℓ = {𝑇0,ℓ,𝑇1,ℓ, ...,𝑇|𝑇 | −ℓ,ℓ }.

𝑖,ℓ ∈ Rℓ of the dimension 𝑇 ( 𝑗 ) of the multivariate time series 𝑇 is a subset of contiguous values from 𝑇 ( 𝑗 )
𝑖,ℓ = [𝑇 ( 𝑗 )
]. The multivariate subsequence
]. For a given univariate time series 𝑇 , the set of all subsequences in 𝑇 of length ℓ is

, ...,𝑇 ( 𝑗 )

,𝑇 ( 𝑗 )
𝑖+1

𝑖+ℓ −1

𝑖

6 Distance-based Methods

In this section, various distance-based anomaly detection methods are introduced. We enumerate the methods in three

categories described in the following section. We enumerate all the mentioned methods in Table 1.

Table 1. Summary of the distance-based anomaly detection methods.

Second Level

Prototype

Dim Method

KNN [91]
KnorrSeq2 [177]
LOF [34]
COF [236]
LOCI [178]
ILOF [200]
DILOF [168]
HSDE [131]
k-means [91]
Hybrid-k-means [228]
DeepkMeans [163]
DBSCAN [215]
DBStream [88]
MCOD [120]
CBLOF [93]
sequenceMiner [38]
NorM (SAD) [23]
NormA [25]
SAND [31]
TARZAN[115]
HOT SAX [114]
DAD [258]
AMD [257]
STAMPI [262]
STOMP [269]
MERLIN [169]
MERLIN++ [170]
SCRIMP [268]
SCAMP [271]
VALMOD [135]
DAMP [146]
LAMP [272]

Proximity-based
Proximity-based
Proximity-based
Proximity-based
Proximity-based
Proximity-based
Proximity-based
Proximity-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Clustering-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based
Discord-based

Nearest Neighbor
Nearest Neighbor
LOF
LOF
LOF
LOF
LOF
LOF
k-means
k-means
k-means
DBSCAN
DBSCAN
-
LOF
-
NormA
NormA
NormA
-
-
-
-
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile
Matrix Profile

M
M
M
M
M
M
M
I
M
M
M
M
M
I
M
I
I
I
I
I
I
I
I
M
M
I
I
I
I
I
I
I

U
U
U
U
U
U
U
U
U
U
Se
U
U
U
U
U
U
U
U
S
U
U
U
U
U
U
U
U
U
U
U
Se

Stream
✗
✗
✗
✗
✓
✓
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
✗
✗
✓
✗
✗
✗
✗
✓
✗
✗
✗
✗
✗
✓
✓
✓

I: Univariate; M: Multivariate // S: Supervised; Se: Semi-Supervised U: Unsupervised

6.1 Proximity-based Methods

Proximity-based methods use distance to close neighborhoods as the main step to detect anomalies. We detail below

two method types of proximity-based methods.

6.1.1 Kth Nearest Neighbor. One of the first distance-based and proximity-based methods introduced in the literature

for anomaly detection is using K-th Nearest Neighbor (KNN) principle [91]. KNN-type methods utilize a metric among

neighboring sub-sequences to infer the abnormality scores of the time series’ sub-sequences. A distance measure
𝑑 (·, ·) (also called dissimilarity measure) is used to find the nearest neighbors for each subsequence. Common distance
measures are Euclidean, Manhatten, or in general, Minkowski distances. The k-anomaly score A𝑘 : {𝑇𝑖,ℓ }𝑖 ∈ I → R for
the set of time series’ sub-sequences {𝑇𝑖,ℓ }𝑖 ∈ I is calculated based on each sub-sequences’ 𝑘𝑡ℎ nearest neighbors using a
Manuscript submitted to ACM

---

<!-- PAGE 14 -->

14

Paparrizos et al.

variable aggregation function 𝑎𝑔𝑔 : R𝑘 → R:

A𝑘 (𝑇𝑖,ℓ ) =

inf
J ⊂ I,| J |=𝑘+1

𝑎𝑔𝑔𝑗 ∈ J𝑑 (𝑇𝑖,ℓ,𝑇𝑗,ℓ )

(1)

In the above equation, ℓ is the fixed length of the sliding window, and 𝑘 + 1 accounts for trivial matches. Following the
intuition of [202] that the anomaly score for a subsequence 𝑇𝑖,ℓ is the distance to its 𝑘𝑡ℎ nearest neighbor, we can use
𝑎𝑔𝑔 = (cid:205). Alternative proposals for A𝑘 may utilize other aggregation methods, such as median, minimum, or other
functions that pool the distances into scalar scores. With different aggregation functions and distance metrics choices,

one can propose different KNN-type models that are appropriate for various anomaly detection problems.

In addition to the standard KNN technique [202], where the maximum distance to the 𝑘𝑡ℎ nearest neighbor is used as
anomaly score, other variants of KNNs have been suggested by researchers. For instance, KnorrSeq and KnorrSeq2 are

also two variants of KNNs proposed in the litterature [177]. The first algorithm KnorrSeq is based on a tumbling window
and discovers only global outliers by marking those sub-sequences for which at least 𝑝% of the other subsequence
are further away than a threshold 𝐷. Their second algorithm KnorrSeq2 is an implementation of KNN that detects
sub-sequences as outliers if at least 𝑝% of the 𝑘 preceding or 𝑘 succeeding sub-sequences are further away than a
threshold 𝐷. The anomaly score is calculated using (cid:205) as the aggregation function:

A𝑘 (𝑇𝑖,ℓ ) =

inf
J ⊂ I,| J |=2𝑘+1,∀ 𝑗 ∈ J,| 𝑗 −𝑖 | ≤𝑘

∑︁

𝑗 ∈ J

1,

0,

if 𝑑 (𝑇𝑖,ℓ,𝑇𝑗,ℓ ) > 𝐷

otherwise

(2)





The anomalous sub-sequences are selected using a threshold 𝜏 = 𝑝𝑘 on the anomaly scores: A𝑘 (𝑇𝑖,ℓ ) <= 𝜏.

6.1.2 Local Outlier Factor. The most commonly used proximity-based approach is the Local Outlier Factor (LOF) [35],

which measures the degree of being an outlier for each instance. Unlike the previous proximity-based models, which

directly compute the distance of sub-sequences, LOF depends on how the instance is isolated to the surrounding

neighborhood. This method aims to solve the outlier detection task where an outlier is considered as “an observation

that deviates so much from other observations as to arouse suspicion that it was generated by a different mechanism"

(Hawkins definition [91]). This definition is coherent with the anomaly detection task in time series where the different

mechanism can be either an arrhythmia in an electrocardiogram or a failure in the components of an industrial machine.
First, let’s consider 𝑇𝑖,ℓ and 𝑇𝑗,ℓ two sub-sequences of the same time series. In the following paragraphs, we note these
two sub-sequences, A and B, respectively. Given 𝑘-𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 (𝐴) the distance between 𝐴 and its 𝑘𝑡ℎ nearest neighbor
(𝑁𝑘 (𝐴) the set of these 𝑘 neighbors), LOF is based on the following reachability distance definition:

𝑟𝑑𝑘 (𝐴, 𝐵) = 𝑚𝑎𝑥 (𝑘-𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒 (𝐵), 𝑑 (𝐴, 𝐵))

(3)

As illustrated in Figure 9, the main concept behind this distance definition is to stress out the homogeneity of
distances between instances within the 𝑘-neighborhood (i.e., the 𝑘-neighborhood will have the same distance between
each other). Thus the local reachability can be defined as follow:

𝑙𝑟𝑑𝑘 (𝐴) =

|𝑁𝑘 (𝐴)|
(cid:205)𝐵 ∈𝑁𝑘 (𝐴) 𝑟𝑑𝑘 (𝐴, 𝐵)

(4)

Given an instance, 𝐴, 𝑙𝑟𝑑𝑘 (𝐴) is the inverse of the average reachability of A from its neighborhood, i.e., the average

distance at which 𝐴 can be reached from its neighbors. Therefore, LOF is given by:

Manuscript submitted to ACM

---

<!-- PAGE 15 -->

Dive into Time-Series Anomaly Detection: A Decade Review

15

Fig. 9. (a) Reachability distance between A and B, A and C for 𝑘 = 4. (b) Difference between 𝑟𝑑𝑘 (𝐴, 𝑋 ), 𝑋 ∈ 𝑁𝑘 (𝐴), when A is an
anomaly and B, C, and D are regular instances.

𝐿𝑂𝐹𝑘 (𝐴) =

(cid:205)𝐵 ∈𝑁𝑘 (𝐴)

𝑙𝑟𝑑𝑘 (𝐵)
𝑙𝑟𝑑𝑘 (𝐴)

|𝑁𝑘 (𝐴)|

(cid:205)𝐵 ∈𝑁𝑘 (𝐴) 𝑙𝑟𝑑𝑘 (𝐵)
|𝑁𝑘 (𝐴) |
𝑙𝑟𝑑𝑘 (𝐴)

=

(5)

Intuitively, the 𝐿𝑂𝐹𝑘 of an instance is the average of the local reachability density of the neighbors divided by its
own reachability density. Therefore, if we set sub-sequences of length ℓ as the length of the sub-sequence, this factor
can be used as an anomaly score.

In the past decade, researchers also suggested many variants of the LOF method [35]. COF [236], for example, is

a connectivity-based variant of LOF. It indicates how far away a point shifts from a pattern, adjusting the notion of

isolation to not depend on the density of data clouds. LOCI [178] is another LOF-like algorithm that utilizes different

statistics (correlation integral and MDEF) to infer individual points’ isolation. Other LOF variants are the ILOF [200]

and DILOF [168] method, which adopts a faster algorithm and detects anomalies incrementally. Finally, the hierarchy-

segmentation-based data extraction method (HSDE) [131] is inspired by the strategy of LOF to detect abnormal points

in time series.

6.2 Discord-based Methods

A practical modification to the KNN-type model is to use the discord, which evolves from comparing distances to the
nearest neighbor to comparing distances to the 𝑘𝑡ℎ neighbor. Such adaptations assist in edge conditions where a small
number of anomalies are clustered along with limited distances, and the conventional KNN approach struggles to

recognize them. The following gives the specific definitions of discord:

Definition 6.1 (Top-k 𝑚𝑡ℎ-discord).

[25, 37, 70, 116, 144, 147, 219, 261] Suppose the window is of length ℓ. Given
a collection of sub-sequences {𝑇𝑗,ℓ } 𝑗 ∈ I , let 𝑓𝑚 denote 𝑚𝑡ℎ-discord function measuring the distance to 𝑚𝑡ℎ nearest
neighborhood so that 𝑓𝑚 (𝑇𝑗,𝑙 ) = min𝑚
𝑑 (𝑇𝑖,𝑙 ,𝑇𝑗,𝑙 ). A sub-sequence 𝑇𝑖,ℓ is a Top-k 𝑚𝑡ℎ-discord if 𝑓𝑚 (𝑇𝑖,ℓ ) is the
𝑘𝑡ℎ maximum among the set {𝑇𝑗,ℓ } 𝑗 ∈ I .

𝑗 ∈ I\{𝑖 }

Note that the 𝑚𝑡ℎ-discord is the special case of Top-k 𝑚𝑡ℎ-discord when 𝑘 = 1, and discord is the special case of

𝑚𝑡ℎ-discord when 𝑚 = 1.

Manuscript submitted to ACM

---

<!-- PAGE 16 -->

16

Paparrizos et al.

Fig. 10. A dataset with 16 sub-sequences (of the same length ℓ) depicted as points in 2-dimensional space; 12 sub-sequences are
normal (hollow points), and 4 are anomalous (solid, red points).

Figure 10 illustrates these notions with an example, where for ease of exposition, we represent each sub-sequence as
a point in 2-dimensional space. The figure depicts two 1𝑠𝑡 -discords: the discord in the top-right (𝑇𝑜𝑝-1) has its 1-NN
at a larger distance than the discord in the bottom-right (𝑇𝑜𝑝-2). The figure also shows a group of two anomalous
sub-sequences: one of them is the 𝑇𝑜𝑝-1 2𝑛𝑑 -discord, and the other sub-sequence is its 1-NN (also a discord).

There exist several studies that have proposed fast and scalable discord discovery algorithms in various settings [37,
70, 116, 144, 147, 219, 259, 261], including simple and 𝑚𝑡ℎ-discords1, in-memory and disk-aware techniques, exact and
approximate algorithms, using either their Symbolic Aggregate Approximation (SAX) [116, 219] or Haar wavelets

[37, 70]. In the following sections, we present the state-of-the-art solutions to the sub-sequence anomaly detection
problem. Note that in this discussion, we focus on the 𝑇𝑜𝑝-𝑘 anomalies (using instead a threshold 𝜖 to detect anomalies
would be a straightforward modification of the solution).

Disk Aware Discord Discovery method (DAD) [259] is a method that proposes a new exact algorithm to discover

discord requiring only two linear scans of the disk thought for managing very large datasets. The algorithm uses the

raw sequences directly. First, it addresses the simpler problem of detecting range discord, then generalizes the problem
to detect the 𝑇𝑜𝑝-𝑘 discord.

Other than DAD, several other discord-like anomaly identification approaches have also been proposed. TARZAN [115]

is a discord method via SAX discretization through the sliding window. The approach processes data by building a

suffix tree and calculating its anomaly score by applying inferences on the discord. Like TARZAN, HOT SAX [114]

also adopts SAX discretization throughout the processing step; it then measures the distance to the nearest non-self

match for sub-sequences to identify abnormalities. AMD [257] further improves HOT SAX, which performs dynamic

segmentation to vary the window length.

As a final note, we observe that in situations with multiple similar anomalies, we should either use a method that
supports 𝑚𝑡ℎ-discords, or use a simple discord (i.e., 1𝑠𝑡 -discord) method as follows. Starting at the beginning of the
series and proceeding to the right, we apply the discord method by only considering the points to the left of the current

position, and every time an anomaly is detected, we search the entire series for similar anomalies (this will reveal all

occurrences of the multiple similar anomalies). As we proceed to the right, the discord method will detect only the

first occurrence of each set of similar anomalies (the rest being detected by the similarity search operation mentioned

1The authors of these papers define the problem as 𝑘𝑡ℎ-discord discovery.

Manuscript submitted to ACM

---

<!-- PAGE 17 -->

Dive into Time-Series Anomaly Detection: A Decade Review

17

Fig. 11. (a) Matrix profile (𝑎2) applied on the SED (Nasa disk failure datasets) time series snippet (𝑎1). The highest value in the matrix
profile (𝑎1) points to the discord of the SED time series. (b) Matrix profile (𝑏2) applied on a synthetic time series (𝑏1). The smallest
values in the matrix profile (𝑎1) point to a motif pair in the time series.

above). Note that this solution implies that we have accumulated enough data at the beginning of the series for the first

execution of the discord method.

6.2.1 Matrix Profile. Matrix Profile [261, 270] is a discord-based method that represents time series as a matrix of

closest neighbor distances. Compared to its predecessor, Matrix Profile proposed a new metadata time series computed

effectively, capable of providing various valuable details about the examined time series, such as discords. For simplicity,

we can call this metadata series matrix profile, and we can define it as follows:

Definition 6.2 (Matrix Profile). A matrix profile 𝑀𝑃 of a time series 𝑇 of length 𝑛 is a time series of length 𝑛 − ℓ − 1
where the 𝑖𝑡ℎ element of 𝑀𝑃 contains the Euclidean normalized distance of the sub-sequence of length ℓ of 𝑇 starting
at 𝑖 to its nearest neighbor.

However, the latter definition does not tell us where that neighbor is located. This information is recorded in the

matrix profile index:

Definition 6.3 (Matrix Profile Index). A matrix profile index 𝐼𝑀𝑃 is a vector of the index where 𝐼𝑀𝑃 [𝑖] = 𝑗 and 𝑗 is the

index of the nearest neighbor of 𝑖.

Two general definitions of Join matrix computation can be inferred. The first, called Self-Join, corresponds exactly to

the matrix profile. The second, called Join, corresponds to the same operation for two different time series. Formally we

have the following:

Definition 6.4 (Time Series Self-Join). Given a time series 𝑇 , the self-join of 𝑇 with sub-sequence length ℓ, denoted by
𝑇 ⊲⊳ℓ 𝑇 , is a meta time series, where: |𝑇 ⊲⊳ℓ 𝑇 | = |𝑇 | − ℓ + 1 and ∀𝑖.1 ≤ 𝑖 ≤ |𝑇 ⊲⊳ℓ 𝑇 |, (𝑇 ⊲⊳ℓ 𝑇 )𝑖,1 = 𝑑𝑖𝑠𝑡 (𝑇𝑖,ℓ , 1𝑠𝑡 𝑁 𝑁 of 𝑇𝑖,ℓ ).

Definition 6.5 (Time Series Join). Given two time series 𝐴 and 𝐵, and a sub-sequence length ℓ, the 𝐽𝑜𝑖𝑛 between
𝐴 and 𝐵 denoted by (𝐴 ⊲⊳ℓ 𝐵), is a meta time series, where: |𝐴 ⊲⊳ℓ 𝐵| = |𝐵| − ℓ + 1 and ∀𝑖.1 ≤ 𝑖 ≤ |𝐴 ⊲⊳ℓ 𝐵|,
(𝐴⊲⊳ℓ 𝐵)𝑖,1 = 𝑚𝑖𝑛(𝑑𝑖𝑠𝑡 (𝐵𝑖,ℓ, 𝐴1,ℓ ), ..., 𝑑𝑖𝑠𝑡 (𝐵𝑖,ℓ, 𝐴|𝐴| −ℓ+1,ℓ )).

These metadata are computed using Mueen’s ultra-fast Algorithm for Similarity Search (MASS) [166] that requires
just 𝑂 (𝑛 ∗ 𝑙𝑜𝑔(𝑛)) time by exploiting the Fast Fourier Transform (FFT) to calculate the dot products between the query
and all the sub-sequences of the time series. Once these metadata are generated, retrieving the 𝑇𝑜𝑝-𝑘 discord is possible
Manuscript submitted to ACM

---

<!-- PAGE 18 -->

18

Paparrizos et al.

by considering the maximum value of the Matrix Profile and ordering it, excluding the trivial matches (overlapping
sub-sequences). Retrieving the sub-sequences with the shortest distance to their nearest neighbor (called 𝑚𝑜𝑡𝑖 𝑓 𝑠) is
also possible. These sub-sequences correspond to a recurrent motif in the time series and can be useful in the anomaly

search.

Figure 11 shows an example of the Matrix Profile metadata. On the one hand, Figure 11 (a) shows that the identified

discord corresponds to a sub-sequence that deviates significantly from the normal cycles. On the other hand, Figure 11

(b) shows that the singular shapes are well-identified as motifs.

A family of Matrix Profile anomaly detection methods has also been proposed in the last decade. STAMP [262]

proposed an algorithm that can provide an accurate answer at any time during the full computation with time complexity
of 𝑂 (𝑛2𝑙𝑜𝑔(𝑛)). STAMPI [262] not only performs the standard all-pairs-similarity-join of sub-sequences for matrix
profile methods but also adapts the method incrementally to accommodate streaming purposes. STOMP [269], based on

STAMP, developed a faster algorithm taking advantage of the sub-sequences order and achieving the computation with
time complexity of 𝑂 (𝑛2). Moreover, a GPU implementation of STOMP has been proposed. Like STOMP, SCAMP [271]
also adopts GPU for the matrix profile anomaly detection process. The SCRIMP method [268] combines the STAMP

algorithm (anytime) and STOMP (ordered) to make a hybrid approach. Moreover, the LAMP approach [272] is able to

compute a constant time approximation of the MP value given a newly arriving time series subsequence. While every

aforementioned method can extract discords of a predefined length, VALMOD [134] and MAD [136] have been proposed

to extract discords of variable length within a predefined length interval. Moreover, MERLIN [169] and MERLIN++ [170]

have been proposed to identify discords of arbitrary length. Finally, DAMP [146], a discord-based method, is able to

work on online settings, and scale to fast-arriving streams.

6.3 Clustering-based Methods

Approaches based on clustering strategies have been proposed for the anomaly detection task. The main idea behind

these methods is to partition the sub-sequence space and then evaluate how one sub-sequence fits into the partition.

6.3.1 K-means Method. The k-means clustering algorithm is a widely used unsupervised learning technique in data
mining and machine learning. Its main objective is to partition a given dataset into 𝑘 distinct clusters, where each data
point belongs to the cluster with the closest mean value. The algorithm operates iteratively, starting with an initial
random assignment of 𝑘 centroids. For the specific case of time series, the Euclidean or the DTW distance is commonly
used. K-means algorithm can also be used for anomaly detection in time series [91]. The computational steps are the

following:

• All the sub-sequences of a given length ℓ (provided by the user) are clustered using the k-means algorithm. The

Euclidean distance is used, and the number of clusters has to be provided by the user.

• Once the partition is learned. We compute the anomaly scores of each sub-sequence based on the distance to the

centroid of its assigned cluster.

• The larger the distance, the more abnormal the time series will be considered.

Such a method is straightforward but has been shown to be very effective for the specific case of multivariate time

series [216]. Moreover, extensions such as Hybrid-k-means [228] can be used for anomaly detection as well. Finally, the

k-means method can be used on top of other pre-processing and representation steps. For instance, DeepKMeans [163]

uses an Autoencoder to learn a latent representation of the time series and applies k-means on top of the latent space to

identify anomalies.

Manuscript submitted to ACM

---

<!-- PAGE 19 -->

Dive into Time-Series Anomaly Detection: A Decade Review

19

6.3.2 DBSCAN. Another commonly used clustering-based method is the Density-Based Spatial Clustering of Appli-

cation with Noise algorithm (DBSCAN) [215]. When identifying anomalies, DBSCAN marks data points into three

categories: (i) core points, (ii) border points, and (iii) anomalies. To classify the points, two non-parametric parameters
are important to detect the potential anomalies using DBSCAN: the radius 𝜖 of neighbors of the analyzed point and the
minimum number 𝜇 of points in each normal cluster. Given these parameters, one can identify the anomalous following
the categorization of the sub-sequences as follows:

• A 𝜖−neighborhood of 𝑇𝑖,ℓ is 𝐵𝜙 (𝑇𝑖,ℓ, 𝜖) ∩ 𝑇 , where 𝑇 is the training data {𝑇𝑖,ℓ }𝑖 ∈𝐼 . And 𝐵𝜙 (𝑇𝑖,ℓ, 𝜖) is the ball of

radius 𝜖 centered at 𝑇𝑖,ℓ with respect to the norm 𝜙 (·, ·).

• 𝑇𝑖,ℓ is a core point if the size of the 𝜖−neighborhood of 𝑇𝑖,ℓ is greater than 𝜇.
• 𝑇𝑖,ℓ is a border point if 𝑇𝑖,ℓ contains a core point in its 𝜖−neighborhood.
• 𝑇𝑖,ℓ is identified as an anomalous sub-sequence if 𝑇𝑖,ℓ is neither a border nor a core point.

DBSCAN has been applied for anomaly detection on a univariate time series that contains observations with average

daily temperature over 33 years [41]. The processing step is to first convert the dataset into sub-sequences set with a

sliding window, which are further z-normalized. After the processing step, DBSCAN is applied to the sub-sequences,

and the anomalies are detected accordingly, as the method above prescribes. Similar clustering approaches such as

DBStream [88] can be used for anomaly detection.

6.3.3 Other Clustering-based Methods. Another clustering-based time-series anomaly detection method is the MCOD [120]

method. MCOD maintains a set of micro-clusters containing only normal objects (in our case: sub-sequences) to effi-
ciently and robustly detect outliers in the event stream. MCOD determines an object 𝑥 as an outlier if there are less
than 𝑘 clusters at a distance of 𝑅 from 𝑥. We can represent this binary decision using the following product function:

A𝑘 (𝑇𝑖,ℓ ) =

inf
J ⊂ I,| J |=𝑘+1

(cid:214)

𝑗 ∈ J

1,

0,

if 𝑑 (𝑇𝑖,ℓ,𝑇𝑗,ℓ ) > 𝑅

otherwise

(6)





The function above returns discrete values 1 and 0 only. So A𝑘 is 1 if and only if all 𝑘 nearest neighbors are at
least 𝑅 distance apart from the considered subsequence. Moreover, due to its similarity with KNN-based methods, it is
important to note that MCOD can also be associated with proximity-based approaches.

Another clustering-based approach is CBLOF [93], a LOF-based clustering algorithm, which first clusters the data

and then assigns the CBLOF factor to each entry to measure both the size and relative of and among the individual

clusters.

Then, Sequenceminer [38] is an approach proposed by NASA. It clusters the sequences using the longest common
sub-sequence (LCS) metric and ranks cluster members based on LCS, and selects the top 𝑝% as anomalies. The anomalies
are identified by the parts of the sequence that differ the most and characterizes anomalous edit.

More recently, NormA [23–25] is a clustering-based algorithm that summarizes the time series with a weighted set

of sub-sequences. The normal set (weighted collection of sub-sequences to feature the training dataset) results from a

clustering algorithm (Hierarchical), and the weights are derived from cluster properties (cardinality, extra-distance

clustering, time coverage). An extension of NormA, called SAND [31], has been proposed for streaming time series.

The main difference between NormA and SAND lies in the approach used to update the weight in a streaming manner.

Additionally, the clustering step in SAND is performed using the k-Shape method [183, 184, 189], whereas NormA

employs a hierarchical clustering method.

Manuscript submitted to ACM

---

<!-- PAGE 20 -->

20

7 Density-based Methods

Paparrizos et al.

Unlike distance-based approaches, the density-based approach does not treat the time series as simple numerical values

but imbues them with more complex representations. The density-based method processes time series data on top

of a representation of the time series that aims to measure the density of the points or sub-sequence space. Such

representation varies from graphs, trees, and histograms to a grammar induction rule. The density-based models have

four second-level categories: distribution-based, graph-based, tree-based, and encoding-based. We enumerate all the

mentioned methods in Table 2.

Table 2. Summary of the density-based anomaly detection methods.

Second Level

Prototype

Dim Method

FAST-MCD [210]
MC-MCD [89]
OCSVM [150]
AOSVM [81]
Eros-SVMs [124]
S-SVM [20]
MS-SVDD [253]
NetworkSVM [266]
HMAD [87]
DeepSVM [250]
HBOS [79]
COPOD [133]
ConInd [7]
MGDD [233]
OC-KFD [208]
SmartSifter [256]
MedianMethod [18]
S-ESD [97]
S-H-ESD [97]
SH-ESD+ [244]
TwoFinger [156]
GeckoFSM [214]
Series2Graph [26]
DADS [217]
IForest [139]
IF-LOF [53]
Extended IForest [90]
Hybrid IForest [157]
SurpriseEncode [42]
GranmmarViz [220]
Ensemble GI [71]
PST [234]
EM-HMM [193]
LaserDBN [173]
EDBN [195]
KDE-EDBN [196]
PCA [223]
RobustPCA [174]
DeepPCA [44]
POLY [260]
SSA [260]

Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Distribution-based
Graph-based
Graph-based
Graph-based
Graph-based
Tree-based
Tree-based
Tree-based
Tree-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based
Encoding-based

MCD
MCD
SVM
SVM
SVM
SVM
SVM
SVM
SVM
SVM
-
-
-
-
-
-
-
ESD
ESD
ESD
-
-
Series2Graph
Series2Graph
IForest
IForest/LOF
IForest
IForest
-
-
-
Markov Ch.
Markov Ch.
Bayseian Net.
Bayseian Net.
Bayseian Net.
PCA
PCA
PCA
-
-

M
M
M
M
M
I
M
M
I
M
M
M
M
M
M
M
I
I
I
I
I
M
I
I
M
M
M
M
M
I
I
M
M
M
M
M
M
M
M
I
I

Se
Se
Se
U
Se
Se
Se
Se
Se
U
U
U
Se
U
U
U
U
U
U
U
Se
S
U
U
U
U
U
Se
U
U
U
U
Se
Se
Se
Se
Se
U
Se
U
U

Stream
✗
✗
✗
✓
✗
✗
✗
✗
✗
✗
✗
✗
✗
✓
✗
✓
✓
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✗
✓
✗
✗
✗
✗
✗
✗
✗
✗

I: Univariate; M: Multivariate // S: Supervised; Se: Semi-Supervised U: Unsupervised

7.1 Distribution-based Methods

The first category of density-based approaches is distribution-based anomaly detection approaches. Distribution-based

methods involve building a distribution from statistical features of the points or sub-sequences of the time series. By

examining the distributions of features of the normal sub-sequences, the distribution-based approach tries to recover

Manuscript submitted to ACM

---

<!-- PAGE 21 -->

Dive into Time-Series Anomaly Detection: A Decade Review

21

relevant statistical models. It uses them to infer the abnormality of the data. In the following sections, we describe

important anomaly detection methods belonging to this category.

7.1.1 Minimum Covariance Determinant. The Minimum Covariance Determinant (MCD) is a common distribution-
based statistic in use [209]. The algorithm seeks to find a subset (of a given size ℎ) of all the sequences to estimate 𝜇
(mean of the subset) and 𝑆 (covariance matrix of the subset) with minimal determinant. In other words, the objective is
to find the subset that is the least likely to include anomalies. Once the estimation is done, Mahalanobis distance is

utilized to calculate the distance from sub-sequences to the mean, which is regarded as the anomaly score.

FAST-MCD [210] is a faster version of the MCD algorithm. Within small datasets, the result of the FAST-MCD

algorithm usually aligns with that of the exact MCD. In contrast, faster and more accurate results are derived through

the FAST-MCD rather than the classical MCD for large time series. Finally, MC-MCD [89], an extension of MCD, has

been proposed for the multi-cluster setting.

7.1.2 One-Class SVM. One-Class Support Vector Machine (OCSVM) is a typical distribution-based example, which

aims to separate the instances from an origin and maximize the distance from the hyperplane separation [218] or

spherical separation [238]. The anomalies are identified with points of high decision score, i.e., far away from the

separation hyper-plane. This method is a variant of the classical Support Vector Machine for classification tasks [94].
Mathematically, given ℓ-dimensional training data points 𝑥0, ...𝑥𝑛 ∈ X, a. non-linear function 𝜙 that map the feature
space X to a dot product space 𝐹 , a kernel 𝑘 (𝑥, 𝑦) = (𝜙 (𝑥), 𝜙 (𝑦)) (usually set to a Gaussian kernel 𝑘 (𝑥, 𝑦) = 𝑒 − | |𝑥 −𝑦 | |2/𝑐 ),
the quadratic program to solve using a hyperplane is the following:

min
𝜔 ∈𝐹,𝜉 ∈R,𝜌 ∈R

||𝑤 ||2 +

1
2

1
𝜈ℓ

∑︁

𝑖

𝜉𝑖 − 𝜌

subject to: (𝜔.𝜙 (𝑥𝑖 )) ≥ 𝜌 − 𝜉𝑖,

𝜉𝑖 ≥ 0.

For a given new instance 𝑥, by deriving the dual problem, the decision function can be defined as follow:

𝑓 (𝑥) = 𝑠𝑔𝑛(

∑︁

𝑖

𝛼𝑖𝑘 (𝑥𝑖, 𝑥) − 𝜌)

Assuming that the optimization problem above can be solved, we can use such a decision function as an anomaly

score. To be able to do it, one has to ensure to train the OCSVM model on a normal section of the time series only (those

have to be annotated by a knowledge expert and therefore require extra work to be used). Figure 12 illustrates the

anomaly detection process. It is also important to note that OCSVM is very similar to Support vector Data Description

(SVDD) that has also been used for anomaly detection [253].

In recent decades, an array of SVM variants have been applied in the time series setting. AOSVM [81] is an efficient

streaming anomaly detection algorithm based on SVM that accommodates SVM to an online detection. The model

is also adaptive, i.e., it forgets old data, featuring low computational and memory requirements. Eros-SVMs [124] is

another variant of the SVM algorithm. It adopts a semi-supervised approach to train the model in the normal data. The

algorithm then measures time windows’ metrics as features fed into multiple OCSVMs, which are further selected

based on the EROS similarity metric. Moreover, multiple other methods based on OCSVM have been proposed in the

literature. These methods either propose processing steps before applying OCSVM (such as NetworkSVM [266] or

Manuscript submitted to ACM

---

<!-- PAGE 22 -->

22

Paparrizos et al.

Fig. 12. OCSVM illustration in which a point corresponds to a subsequence and only the green points are provided for the training
step.

S-SVM [20] that proposed seasonality decomposition or Stockwell transformation) or combine OCSVM with other

methods (such as HMAD [87] that uses hidden Markov chain to represent the time series into a latent space, on which

OCSVM is applied). Finally, DeepSVM [250] proposes to use an Autoencoder architecture to extract meaningful features

that use OCSVM on top of the learned latent space to detect anomalies.

7.1.3 Histogram-based Outlier Score. Histogram-based Outlier Score (HBOS) [79] is another distribution-based al-

gorithm for anomaly detection. For every single dimension (i.e., timestamps of a sub-sequence for univariate time

series or values across multiple dimensions for multivariate time series), a univariate histogram is constructed with
𝑘 equal width bins. Each histogram is further normalized so that the height is 1. For a given multivariate point 𝑝 (or
univariate sub-sequence 𝑇𝑖,ℓ ), we count the bin that contains 𝑝 for each dimension and multiply together the inverse of
the frequency of bins where 𝑝 belongs for all dimensions. The algorithm assumes mutual Independence among the
time series’ dimensions (or the timestamps for univariate sub-sequence anomaly detection). Moreover, HBOS suits the

particular case of highly unbalanced time series (i.e., very few anomalies) and unknown distribution.

7.1.4 Extreme Studentized Deviate. Various statistics, such as Extreme Studentized Deviate (ESD), are useful for inferring
time series abnormality. The latter computes the statistical test for 𝑘 extreme values by 𝐶𝑘 = max𝑘 |𝑥𝑘 − ¯𝑥 |/𝑠, where ¯𝑥
and 𝑠 denote the mean and the variance. The test is then compared with other critical values to determine if a value is
abnormal. If so, then the value is removed, and the statistical test is re-calculated iteratively. Built on ESD, the S-ESD

and SH-ESD [97] methods remove the seasonal component using Seasonal-Trend decomposition (STL) and subtract the

robust median. The pure, normalized data is then applied with ESD to detect anomalies. SH-ESD+ [244], on a further

step than SH-ESD, applies the STL decomposition using a Loess regression and then generalizes the ESD on the residual

part of seasonal decomposition to detect anomalies.

7.1.5 Other Distribution-based Methods. Besides the distribution-based algorithms presented above, many other

methods are proposed using different models. First, the MedianMethod [18] is a simple anomaly detection method

proposed initially to filter outliers. The main idea is to measure the deviation from the median of the previous points

and the median of their successive differences. Moreover, SmartSifter [256] aims to build a histogram for categorical

values and a finite mixture model for continuous data. The proposed method aims to update those histograms/density

as new points arrive in an unsupervised manner and then compute a score that estimates how the new point updated

Manuscript submitted to ACM

---

<!-- PAGE 23 -->

Dive into Time-Series Anomaly Detection: A Decade Review

23

Fig. 13. Illustration of the Finite State Machine (FSM).

has changed the histogram/density. Then, OC-KFD [208] utilizes linear quantile models. The model is selected via cross-

validated likelihood, from which a linear quantile model is fitted, and outliers are detected by considering confidence

intervals. Moreover, MGDD [233] utilizes kernel density estimation on sliding windows of the original time series. The

estimated distribution is then used to identify the anomalies. Then, COPOD [133] is a copula-based anomaly detection

method and an ideal choice for multivariate data. Finally, unlike the previous models, ConInd [7] is an algorithm based

on domain knowledge. The model can detect only the known anomalies, where multiple statistical anomaly indicators

(condition indicators) are proposed based on different distribution assumptions.

7.2 Graph-based Methods

Then, graph-based methods are another category of density-based approaches. Graph-based methods represent the

time series and the corresponding sub-sequences as a graph. The nodes and edges represent the different types of

sub-sequences (or representative features) and their evolution in time. In this section, we describe the most important

approaches in this category.

7.2.1

Finite State Machine. Finally, Finite State Machine (FSM) is a general categorization of machine learning algorithms

that can be only in exactly one of a finite number of states at any given time. In reaction to any inputs, the FSM will

shift from one state to another; such changes between states are called a transition. In anomaly detection, input time

series will, upon certain machine-learned rules, change the state of the algorithms. If the state turns into an anomaly,

the input is identified as anomalous.

Figure 13 gives an illustration of such a process. In many ways, FSM is similar to a dynamic Bayesian network, which

also uses Directed Acyclic Graph (DAG). However, the transition rule between FSM states is usually parametric, and

thus the entire process is machine learning based. However, Finite State Machine is a general categorization where

particular methods might be vastly different, each of which is unique to its own specific rules of the learning algorithm.

TwoFingers [156], for example, builds a database of normal behavior by constructing a suffix tree for variable-length

N-grams from the training data. The trees are transformed within the finite state machine and are further compacted

to a DAG. Finally, the Finite State Machine, endowed with the architecture of DAG, matches the new series to detect

anomalies. GeckFSM [214], however, is vastly different from TwoFingers, despite also following a finite-state machine

structure. The proposed approach, GeckoFSM, aims to cluster the points (based on their slope) in the univariate time

series and then extract some non-overlapping sub-sequences. A slope-based cluster merging operation then finds an

optimal number of clusters, where transition human-readable rules of FSM for each cluster are further computed using

the RIPPER algorithm [55]. Anomalies are identified as points that derive significantly from these rules.

7.2.2 Graph Representation of Sub-sequences. A second approach is to convert the time series into a directed graph with

nodes representing the usual types of subsequences and edges representing the frequency of the transitions between

Manuscript submitted to ACM

---

<!-- PAGE 24 -->

24

Paparrizos et al.

Fig. 14. Example of Series2graph representation.

types of subsequences. Series2Graph [26] is building such kinds of graphs. Moreover, an extension of Series2Graph

proposed in the literature, named DADS [217], proposes a distributed implementation and, therefore, a much more

scalable method for large time series.

For a given data series 𝑇 , the overall process of Series2Graph is divided into the following four main steps.

(1) Subsequence Embedding: Project all the subsequences (of a given length ℓ) of 𝑇 in a two-dimensional space,

where shape similarity is preserved.

(2) Node Creation: Create a node for each one of the densest parts of the above two-dimensional space. These

nodes can be seen as a summarization of all the major patterns of length ℓ that occurred in 𝑇 .

(3) Edge Creation: Retrieve all transitions between pairs of subsequences represented by two different nodes: each

transition corresponds to a pair of subsequences, where one occurs immediately after the other in the input data
series 𝑇 . We represent transitions with an edge between the corresponding nodes. The weights of the edges are
set to the number of times the corresponding pair of subsequences was observed in 𝑇 .

(4) Subsequence Scoring: Compute the normality (or anomaly) score of a subsequence of length ℓ𝑞 ≥ ℓ (within or

outside of 𝑇 ), based on the previously computed edges/nodes and their weights/degrees.

Figure 14 depicts the resulting graph returned by Series2Graph. The unusual path in the graph (with edges with low

weights and nodes with low degrees) corresponds to anomalies in the time series.

7.3 Tree-based Methods

Instead of modeling the time series into a graph, the different points or sub-sequences can also be organized in trees to

highlight potential isolated instances that could correspond to anomalies. Isolation Forest (IForest) is density-based and

the most famous tree-based approach for anomaly detection. IForest tries to isolate the outlier from the rest [140]. The

key idea remains on the fact that, in a normal distribution, anomalies are more likely to be isolated (i.e., requiring fewer

Manuscript submitted to ACM

---

<!-- PAGE 25 -->

Dive into Time-Series Anomaly Detection: A Decade Review

25

Fig. 15. Set of isolation trees that randomly partition a dataset. On average, instance N has a longer path to the root than instance A.
Thus, instance A’s anomaly score will be higher.

random partitions to be isolated) than normal instances. If we assume the latter statement, we only have to produce a

partitioning process that indicates well the isolation degree (i.e., anomalous degree) of instances.

Let first define the concept of Isolation Tree as stated in [140]. Let be 𝑇 𝑟 a binary tree where each node has zero or
two children and a test that consists of an attribute 𝑞 and a split 𝑝 such that 𝑝 < 𝑞 divides data points into the two
children. 𝑇 𝑟 is built by dividing recursively the training dataset 𝑇 = {𝑇𝑖,ℓ,𝑇𝑖+1,ℓ, ...,𝑇|𝑇 | −ℓ,ℓ } randomly selecting 𝑝 and 𝑞
until, the maximal depth of the tree is reached, or the number of different instances is equal to 1. Figure 15 depicts an

example of isolation trees.

Using that kind of data structure, the path length into the tree 𝑇 𝑟 to reach an instance 𝑇𝑖,ℓ is directly correlated to

the anomaly degree of that instance. Therefore, we can define the anomaly score as follow:

𝑆 (𝑥, 𝑛) = 2

𝑠𝑠 =

(cid:205)𝑇 𝑟 ∈ T ℎ(𝑥,𝑇𝑟 )
|T |𝑐 (𝑛)

, 𝑐 (𝑛) = 𝐻 (𝑛 − 1) −

2(𝑛 − 1)
𝑛

(7)

With ℎ(𝑥,𝑇 𝑟 ) the length of the path to reach 𝑥 in the tree 𝑇 𝑟 , T a set of different isolation trees built, 𝑛 the number
of instances in the training set, and H is the harmonic number. It can be simply but surely estimated using the Euler

constant.

Other IForest-based algorithms have also been proposed recently. Extended IForest [90] is an extension of the

traditional Isolation Forest algorithm, which removes the branching bias using hyperplanes with random slopes. The

random sloping hyperplanes enable an unbiased selection of features free of the branching structure within the dataset.

Hybrid IForest [157] is another improvement on IForest, enabling a supervised setting and eliminating the dataset’s

potential confounding due to unbalanced clusters. Finally, IF-LOF [53] combines IForest and LOF by applying IForest

and then utilizes LOF to refine the results, which speeds up the process.

7.4 Encoding-based Methods

Encoding-based methods represent the sub-sequences of a time series into a low-dimensional latent space or data

structure. The anomaly score is directly from the latent space representations. More specifically, the anomaly scores are

attributed to the points that correspond to the encoded sub-sequences in the latent space.

7.4.1 Principal Component Analysis. The first encoding-based approach is to encode and represent the time series with

its principal components. Principal Components Analysis (PCA) investigates the major components of the time series

that contribute the most to the covariance structure. The anomaly score is measured by the sub-sequences distance from
0 along the principal components weighted by their eigenvalues. A standard routine is to pick 𝑞 significant components
Manuscript submitted to ACM

---

<!-- PAGE 26 -->

26

Paparrizos et al.

that can explain 50% variations of the time series and 𝑟 minor components that explain less than 20% variations. A
point is an anomaly if its values of major principles components, 𝑦1, 𝑦2..., have a weighted sum exceeding the threshold
its minor one has. So 𝑥 (or a sub-sequence 𝑇𝑖,ℓ of a given time series) is an anomaly if:

𝑞
∑︁

1

𝑦𝑖
𝜆𝑖

> 𝑐1 or,

𝑝
∑︁

𝑝 −𝑟 +1

𝑦𝑖
𝜆𝑖

> 𝑐2

(8)

In the equation above, 𝑐1 and 𝑐2 are predefined threshold values, and 𝜆s are the eigenvalues. RobustPCA [174] aims
to recover the principal matrix 𝐿0 by decomposing the original covariance matrix into 𝑀 = 𝐿0 + 𝑆0 to minimize the rank
of 𝐿0. The residual term 𝑆0 helps separate the anomalous subsets and makes the algorithm applicable to time series
containing many anomalies. Finally, deepPCA [44] is similar to robustPCA but with an autoencoder preprocessing step

first. The autoencoder maps the time series into a latent space, and then the PCA (described above) is used to identify

anomalies.

7.4.2 Grammar and Itemset Representations. Another approach is to represent the time series into a set of symbols

associated with rules. GrammarViz [219] adopts an approach to find anomalies based on the concept of Kolmogorov

complexity where the randomness in a sequence is a function of its algorithmic incompressibility. The main idea is that

it is possible to represent a time series as context-free grammar (a set of symbols associated with rules), and the sections

of the time series that match a few grammar rules are considered anomalies. In addition, A feature of this algorithm is

also centered on its ability to find anomalies of different lengths.

More precisely, the algorithm can be divided into different phases. First, the whole time series is summarized using

Symbolic Aggregate Approximation (SAX) to have discrete values and not continuous ones. Next, context-free grammar

is built using Sequitur, a linear space and time algorithm able to derive context-free grammar from a string incrementally.

Finally, a rule density curve is built, which is the metadata that allows the detection of anomalies. It is possible to obtain

a rule density curve by iterating over all grammar rules and incrementing a counter for each time series that points to

the rule spans. Once the rule density curve is obtained, it is possible to discover anomalies by picking the minimum

values of the curve. Otherwise, it is possible to discover the least frequent sub-sequences (and possible anomalies) by

applying the Rare Rule Anomaly (RRA) algorithm.

Other grammar-based methods have been proposed in the literature. First, Ensemble GI [71] is an extension of

the GrammarViz algorithm, which further implements grammar induction on an ensemble approach that obtains

the anomaly detection result based on the ensemble detection of models with different parameter values. Unlike the

previous two, SupriseEncode [42] adopts a distinct compression-based method representing the record as an itemset.

The compression ratio of segments (code-length encoding) derived from each sub-sequence is compared among the

training data set to derive the anomaly score.

7.4.3 Hidden Markov Model. Another type of Encoder-based method is Hidden Markov Model (HMM). The latter
assumes the existence of a Markov process 𝑋 such that the time series data observed is dependent on that 𝑋 . The goal
is to derive 𝑋 by observing the data. The anomalies are detected by measuring the ability of the encoding to represent
the time series. For instance, EM-HMM [193] is a time-series anomaly detection method based on HMM.

More precisely, PST [234] is another detection method based on HMM. It proposes an efficient algorithm for computing

the Probabilistic Suffix Tree (PST), a compact variable-order Markov chain. In practice, the algorithm embeds possible

chains of values (and their probability) into the trees and infers the anomaly score by computing the probabilities of the

chains of values.

Manuscript submitted to ACM

---

<!-- PAGE 27 -->

Dive into Time-Series Anomaly Detection: A Decade Review

27

7.4.4 Bayesian Networks. Bayesian Network builds a graph denoting the relationship between random variables in

terms of Directed Acyclic Graph (DAG). Each node in the DAG stands for a random variable, and the edges represent the

probabilistic relationships among the variables. Dynamic Bayesian Network, or temporal Bayesian Network, generalizes

the Bayesian Network graph model to the time series setting. The model is capable of modeling the temporal relationship

for different random variables with first-order assumption.

Fig. 16. Illustration of Dynamic Bayesian Network (DBN).

As displayed in Figure 16, the random variables at different timestamps are connected by probabilistic edges, which

are referenced by the model to characterize the temporal change of the random variables in the dataset. The joint
probability distribution of a given DBN variable 𝑋𝑖 is given by the following equation:

𝑃 (𝑋𝑖:𝑡,1, 𝑋𝑖:𝑡,2, 𝑋𝑖:𝑡,𝑅−1...𝑋𝑖:𝑡,𝑅) =

(cid:214)

𝑡 ≤𝑇 ,𝑟 ≤𝑅

𝑃 (𝑋𝑖:𝑡,𝑟 |𝑃𝑎𝑟 (𝑋𝑖:𝑡,𝑟 ))

(9)

𝑃𝑎𝑟 (𝑋𝑖:𝑡,𝑟 ) denotes the parent of 𝑋𝑖:𝑡,𝑟 , which are either inside the previous timestamps or just the parent inside the

same timestamps, due to the first order assumption.

Various time-series anomaly detection methods have implemented DBN in their algorithms. LaserDBN [173] is

a method proposed for image time series. The data is first preprocessed by k-means clustering to perform feature

selection, and then Dynamic Bayesian Network is implemented to compute the probabilities of individual sub-sequences.

EDBN [195] proposes an extension of DBN to suit the particular case of textual time-series anomaly detection (specifically

for business processes and logs). Finally, KDE-EDBN [196] is an extension of EDBN that uses Kernel Density Estimation

(KDE) to handle numerical attributes in logs.

7.4.5 Other Encoding-based Methods. In addition to all the methods described above, several more anomaly detection

methods could be grouped in the encoding-based category, such as polynomial approximation methods to detect

anomalies, like POLY [132] or SSA [260]. The latter is training multiple polynomial approximation models for each time

series (or sub-sequence in the time series). A similarity measure between the trained models is used to detect anomalies.

8 Prediction-based Methods

Prediction-based methods aim to detect anomalies by predicting the expected normal behaviors based on a training set of

time series or sub-sequences (containing anomalies or not). For instance, some methods will be trained to predict the next

value or sub-sequence based on the previous one. Then, the prediction error is used as an anomaly score. The underlying

assumption of prediction-based methods is that normal data are easier to predict, while anomalies are unexpected,

leading to higher prediction error. Such assumptions are valid when the training set contains no or few time series with

anomalies. Therefore, prediction-based methods are usually more optimal under semi-supervised settings. Within the

Manuscript submitted to ACM

---

<!-- PAGE 28 -->

28

Paparrizos et al.

prediction-based methods, there come two second-level categories: forecasting-based and reconstruction-based. We

enumerate all the mentioned methods in Table 3.

Table 3. Summary of the prediction-based anomaly detection methods.

Second Level

Prototype

Dim Method

ES [226]
DES [226]
TES [226]
ARIMA [211]
NoveltySVR [149]
PCI [263]
OceanWNN [246]
MTAD-GAT [267]
AD-LTI [252]
CoalESN [172]
MoteESN [49]
HealthESN [51]
Torsk [96]
LSTM-AD [153]
DeepLSTM [50]
DeepAnT [167]
Telemanom★ [103]
RePAD [127]
NumentaHTM [3]
MultiHTM [249]
RADM [59]
MAD-GAN [129]
VAE-GAN [171]
TAnoGAN [17]
USAD [8]
EncDec-AD [152]
LSTM-VAE [194]
DONUT [254]
BAGEL [130]
OmniAnomaly [231]
MSCRED [265]
VELC [264]
CAE [72, 73]
DeepNAP [117]
STORN [227]

Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Forecasting-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based
Reconstruction-based

-
-
-
ARIMA
SVM
ARIMA
-
GRU
GRU
ESN
ESN
ESN
ESN
LSTM
LSTM
LSTM
LSTM
LSTM
HTM
HTM
HTM
GAN
GAN
GAN
GAN
AE
AE
AE
AE
AE
AE
AE
AE
AE
AE

I
I
I
I
I
I
I
M
M
M
I
I
M
M
I
M
M
M
I
M
M
M
M
M
M
M
M
I
I
M
I
I
I
M
M

Se
Se
U
U
U
U
Se
Se
Se
Se
Se
Se
U
Se
Se
Se
Se
U
U
U
Se
Se
Se
Se
Se
Se
Se
Se
Se
Se
U
Se
Se
Se
Se

Stream
✗
✗
✗
✓
✓
✓
✗
✓
✓
✓
✓
✗
✓
✗
✗
✗
✗
✗
✓
✓
✓
✓
✗
✗
✗
✗
✓
✗
✗
✗
✗
✗
✗
✓
✓

I: Univariate; M: Multivariate // S: Supervised; Se: Semi-Supervised U: Unsupervised

8.1 Forecasting-based Methods

Forecasting-based methods use a model trained to forecast several time steps based on previous points or sequences.

The forecasting results are thus directly connected to previous observations in the time series. The forecasted points or

sequences are then compared to the original ones to determine how anomalous or unusual these original points are.

8.1.1 Exponential Smoothing. One of the first forecasting-based approaches proposed in the literature is the Exponential

Smoothing [226]. The latter is a non-linear smoothing technique to predict the time series points by taking the previous

time series data and assigning exponential weights to these previous individual observations. The anomalies are then
detected by comparing the predicted and actual results. Formally, the prediction of the current value ˆ𝑇𝑖 is defined as
follows:

ˆ𝑇𝑖 = (1 − 𝛼)𝑁 −1𝑇𝑖 −𝑁 +

𝑁 −1
∑︁

𝑗=1

𝛼 (1 − 𝛼) 𝑗 −1𝑇𝑖 − 𝑗 𝛼 ∈ [0, 1]

(10)

Manuscript submitted to ACM

---

<!-- PAGE 29 -->

Dive into Time-Series Anomaly Detection: A Decade Review

29

Thus, the estimated sub-sequence is a linear combination of the previous data points, with the weights varying
exponentially. The parameter 𝛼 stands for the rate of exponential decrease. The smaller the 𝛼 is, the more the weight is
assigned to the distant data points.

In addition, several approaches based on exponential smoothing have been proposed. For example, Double Exponential

Smoothing (DES) and Triple Exponential Smoothing (TES) [226] are variants of the exponential smoothing techniques
for non-stationary time series. In DES, a further parameter 𝛽 is utilized to smooth the trend that a time series can have.
For the special case of time series containing seasonality, TES enables another parameter 𝛾 to control it.

8.1.2 ARIMA. Another early category of forecasting-based approaches proposed in the literature is ARIMA mod-

els [211]. The latter assumes a linear correlation among the time series data. The algorithm fits the ARIMA model on

the time series and draws anomalies by comparing the prediction of the ARIMA model and real data. Formally, An
ARIMA(𝑝′, 𝑞) model is built upon the following iterative equations:

𝑇𝑖 =

𝑝 ′
∑︁

𝑘=1

𝛼𝑘𝑇𝑡 −𝑘 + 𝜖𝑖 +

𝑞
∑︁

𝑗=1

𝜃 𝑝
𝑗 𝜖𝑖 − 𝑗

(11)

Overall, using ARIMA models, we assume that every next time series values correspond to a linear combination of

the previous values and residuals. Note that the residuals must be estimated in an iterated manner. Moreover, Prediction

Confidence Interval (PCI) [263] is an extension of the ARIMA model, which further combines the nearest neighbor

method. The prediction confidence interval allows dynamic thresholding. The threshold can be estimated on the

historical nearest neighbors.

8.1.3 Long Short-Term Memory. Long Short-Term Memory (LSTM) [98] network has been demonstrated to be par-

ticularly efficient in learning inner features for sub-sequences classification or time series forecasting. Such a model

can also be used for anomaly detection purposes [67, 154]. The two latter papers’ principle is as follows: A stacked
LSTM model is trained on normal parts of the data that we call 𝑁 . The objective is to predict the point 𝑁𝑖 ∈ 𝑁 or the
sub-sequence 𝑁𝑖,𝑙1 using the sub-sequence 𝑁𝑖 −𝑙,𝑙 . Consequently, the model will be trained to forecast a healthy state of
the time series, and, therefore, will fail to forecast when it will encounter an anomaly.

LSTM network is a special type of Recurrent Neural Network (RNN), based on LSTM units as memory cells to encode

hidden information. Figure 17 depicts the components and interactions within an LSTM cell. The various components

are given by:

𝑓𝑡 = 𝜎𝑔 (𝑊𝑓 𝑥𝑡 + 𝑈𝑓 ℎ𝑡 −1 + 𝑏 𝑓 )
𝑖𝑡 = 𝜎𝑔 (𝑊𝑖𝑥𝑡 + 𝑈𝑖ℎ𝑡 −1 + 𝑏𝑖 )
𝑜𝑡 = 𝜎𝑔 (𝑊0𝑥𝑡 + 𝑈0ℎ𝑡 −1 + 𝑏0)
𝑐𝑡 = 𝑓𝑡 ◦ 𝑐𝑡 −1 + 𝑖𝑡 ◦ 𝜎𝑐 (𝑊𝑐𝑥𝑡 + 𝑈𝑐ℎ𝑡 −1 + 𝑏𝑐 )
ℎ𝑡 = 𝑜𝑡 ◦ 𝜎ℎ (𝑐𝑡 )

By combining a large number of cell (outlined in Figure 17) and stacking them [154], one can fit the weights to

forecast the time series in two different ways described as follow: (i) The first is to train the network using a fixed time
window length 𝑇𝑡 −ℓ −1,ℓ = [𝑇𝑡 −ℓ, ...,𝑇𝑡 −1] to predict 𝑇𝑡 , (ii) or using the same input to predict the incoming sequence
𝑇𝑡,ℓ ′ = [𝑇𝑡 , ...,𝑇𝑡 +ℓ ′ ]. For the specific purpose of anomaly detection, we will assume that such a model can be trained
Manuscript submitted to ACM

---

<!-- PAGE 30 -->

30

Paparrizos et al.

Fig. 17. LSTM cell architecture.

to achieve both of the previously enumerated tasks. Then, what has to be done is to train this model on the normal

section of the time series (apriori annotated by the knowledge expert) and use the forecasting error as an anomaly

score. Therefore, one can expect to obtain a bigger forecasting error for a sub-sequence that the model has never seen

(like an anomaly), rather than a usual sub-sequence.

There exists a large variety of methods based on LSTM neural networks proposed in the literature. First, DeepLSTM [50]

is a standard implementation of LSTM networks. The generative model stacks the LSTM network trained from normal

sections of the time series. Then, LSTM-AD [153] adopts a similar approach to DeepLSTM. In addition to training the

LSTM model to predict time series, LSTM-AD also estimates the training dataset’s errors with multivariate normal

distribution and calculates the anomaly score with the Mahalanobis distance.

Moreover, Telemanom [103] is an LSTM-based approach that focuses on channeled data (i.e., multivariate time series).

An LSTM network is trained for each channel. The prediction error is further smoothed over time, and low errors are

pruned retroactively. Then, RePad [127] is another LSTM-based algorithm that considers short-term historical data

points to predict future anomalies in streaming data. The detection is based on the Average Absolute Relative Error

(AARE) of LSTM, and RePad also implements a dynamic threshold adjustment to vary the threshold value at different

timestamps.

8.1.4 Gated Recurrent Unit. In addition to LSTM cells frequently implemented in time series settings, other neural

network architectures have also been in use. One example is the Gated Recurrent Unit (GRU) which is also an RNN but

operates in a different gated unit than LSTM to forecast time series values. We will summarize some of the approaches

used in these different architectures.

MTAD-GAT [267] is the first example of anomaly detection methods based on GRU units. The latter uses both the

prediction error and reconstruction error for the detection of anomalies (This method could fit in both forecasting

and reconstruction-based categories). The model utilizes two parallel graph attention layers to preprocess the time

series dataset and then implements a GRU network to reconstruct and predict the next values. AD-ITL [252] is another

Manuscript submitted to ACM

---

<!-- PAGE 31 -->

Dive into Time-Series Anomaly Detection: A Decade Review

31

GRU-based algorithm with seasonal and raw features as input. The input time series is first used to extract seasonal

features and further fed to the GRU network. The GRU then predicts each value of the window, and Local Trend

Inconsistency (LTI) is used as a measure of the error to assess the abnormality between predicted and actual values.

8.1.5 Echo State Networks. Researchers have also proposed multiple Echo State Networks for detecting anomalies in

time series. An Echo State Network (ESN) is a variant of RNN, which has a sparsely connected random hidden layer.

The model randomizes the weights in hidden and input layers and also connects neurons randomly. Only the values in

the output layers are learned, rendering the method a linear model that is easily trained. The random hidden layers act

as a dynamic reservoir that transforms the input into sequences of non-linear, complicated processes. The trainable

output layer organizes the encoding of the inputs in the dynamic reservoir, enabling complex representation of the data

despite its linearity. The initial values of input and hidden layers are also chosen carefully, usually tuned with multiple

parameters.

First, CoalESN [172] is a simple implementation of Echo State by predicting time series values and comparing the

estimated results with real ones to determine abnormality. MoteESN [49] adopts a similar approach to CoalESN but uses

the absolute difference to measure the anomaly score. The model is optimized for a sensor device, where the network is

trained offline before deployment on the sensor. Torsk [96] is another adaptation of ESN. Like its precursors, Torsk uses

the previous window as training data and then predicts the following ones. The model further implements automatic

thresholding. Finally, HealthESN [51] is an Echo State Network applied to the medical and health domain. The algorithm

utilizes the default architecture with training and testing steps; after a sequence of data preprocessing, intelligent

threshold computation is used to estimate the adaptive threshold and declare anomalies by the ESN predictions.

8.1.6 Hierarchical Temporal Memory. Another recurrent neural network type of approach is Hierarchical Temporal

Memory (HTM). The latter is the core component of multiple anomaly detection methods proposed in the literature.

The HTM method is based on the theory and ideas proposed in the Thousand Brains Theory of Intelligence [92]. The

latter proposes that many models are learned for each object or concept, rather than only one single model per object,

as most of the methods described in the previous sections usually handle.

In particular, HTM focuses on three main tasks: sequence learning, continual learning, and sparse distributed

representations. Even though HTM-based methods can be seen as RNN-based methods (such as LSTM, GRU, and

ESN-based approach), the main difference is between the neuron definition and the learning process. For HTM, the

unsupervised Hebbian-learning rule [95] is applied to train the model rather than the classical back-propagation is not

applied.

The first time-series anomaly detection method using HTM proposed in the literature is the NumentaHTM [3] and

MultiHTM [249] approaches. Moreover, RADM [59] combines HTM with Naive Bayesian Networks to detect anomalies

in multivariate time series.

8.1.7 Other Forecasting-based Methods. Finally, it is important to note that forecasting-based approaches are a generic

concept that requires to have a model that can predict the incoming value from historical data. Therefore, any regression

approach can be used as a forecasting-based approach. In the previous sections, we described on a high-level the most

popular methods used to perform anomaly detection using forecasting-based techniques. We can complement the list

with methods using more specific architecture on specific applications such as OceanWNN [246] using Wavelet-Neural

Networks, or more classical regression techniques used as forecasting-based core units such as NoveltySVR [149] using

Support-Vector-Machine (SVM).

Manuscript submitted to ACM

---

<!-- PAGE 32 -->

32

Paparrizos et al.

Fig. 18. Overview of autoencoders methods for time-series anomaly detection.

8.2 Reconstruction-based Methods

Reconstruction-based methods represent normal behavior by encoding sub-sequences of a normal training time series

into a low-dimensional space. The sub-sequences are then reconstructed from the low-dimensional space, and the

reconstructed sub-sequences are then compared to the original sub-sequences. The difference between the reconstruction

and the original sequence is used to detect anomalies. In general, the inputs to the reconstruction process are training

sub-sequences.

8.2.1 Autoencoder. Autoencoder is a type of artificial neural network used to learn to reconstruct the dataset given as

input using a smaller encoding size to avoid identity reconstruction. As a general idea, the autoencoder will try to learn

the best latent representation (also called encoding) using a reconstruction loss. Therefore, it will learn to compress the

dataset into a shorter code and then uncompress it into a dataset that closely matches the original. Figure 18 depicts an
overview of autoencoders for time series. Formally, given two transition functions 𝐸 and 𝐷, respectively called encoder
and decoder, the task of an autoencoder is the following one:

𝜙 :Tℓ → Z

𝜓 :Z → Tℓ

𝜙,𝜓 =𝑎𝑟𝑔 min
𝜙,𝜓

L (𝑇𝑖,ℓ,𝜓 (𝜙 (𝑇𝑖,ℓ )))

(12)

(13)

(14)

L is a loss function that is usually set to the mean square error of the input and its reconstruction, formally written
||𝑋 − 𝜓 (𝜙 (𝑇𝑖,ℓ ))||2. This loss fits the task well for the specific case of sub-sequences in a time series since it coincides
with the Euclidian distance.

The reconstruction error can be used as an anomalous score for the specific anomaly detection task. As the model is

trained on the non-anomalous sub-sequence of the time series, it is optimized to reconstruct the normal sub-sequences.

Therefore, all the sub-sequences far from the training set will have a bigger reconstruction error.

As autoencoder has been a popular method in the recent decade, many anomaly detection algorithms are based on

autoencoder algorithms’ implementation. EncDec-AD [152] is the first model that implements an encoder-decoder

by using reconstruction error to score anomalies. LSTM-VAE [194] and MSCRED [265] use LSTM and Convolutional

Manuscript submitted to ACM

---

<!-- PAGE 33 -->

Dive into Time-Series Anomaly Detection: A Decade Review

33

Fig. 19. Overview of GAN methods for time-series anomaly detection.

LSTM cells in the autoencoder architecture. Similarly, Omnianomaly [231] is another autoencoder method where the

autoencoder architecture uses GRU and planar normalizing flow.

Then, STORN [227] and DONUT [254] proposed a Varational Autoencoder (VAE) method to detect abnormal

sub-sequences. For DONUT, it further preprocesses the time series using the MCMC-based missing data imputation

technique [205]. Improving from DONUT, BAGEL [130] implements conditional VAE instead of VAE. VELC [264] sets

up additional constraints to the VAE. The Decoder phase is regularized due to anomalies in training data, which helps

fit normal data and prevent generalization to model abnormalities.

Moreover, CAE [72, 73] uses a convolutional autoencoder to convert time series sub-sequences to image encoding.

The algorithm also speeds up nested-loop-search using sub-sequences approximation with SAX word embedding.

Finally, DeepNAP [117] is a sequence-to-sequence AE-based model. However, unlike other AE-based models,

DeepNAP detects anomalies before they occur.

8.2.2 Generative Adversarial Networks. Generative Adversarial Network (GAN) is initially proposed for image gener-

ation purposes [82] but can also be used to generate time series. GAN has two components: (i) one to generate new

time series and (ii) one to discriminate the existing time series. Both of the components are useful for the detection of

anomalies. Figure 19 depicts the overview of GAN methods for anomaly time series.

More precisely, a GAN is composed of two networks. The first is called the generator 𝐺 (𝑧, 𝜃𝑔) with 𝜃𝑔 its parameters.
The second one is called the discriminant 𝐺 (𝑥, 𝜃𝑑 ) with 𝜃𝑑 its parameters. The output of 𝐺 is the same shape as the input,
and the output of 𝐷 is a scalar 𝐷 (𝑥) that represents the probability that 𝑥 came from the original dataset. Therefore
1 − 𝐷 (𝑥) is the probability that 𝐺 has generated 𝑥. Formally, 𝐺 and 𝐷 have to be optimized, such as the two-player
optimization problem where the accuracy of the discriminator has to be maximized but also minimized regarding the
generator. The value to be minimized, denoted as 𝑉 (𝐺, 𝐷), is defined in the following manner.

min
𝐺

max
𝐷

𝑉 (𝐺, 𝐷) = E𝑥∼𝑝𝑑𝑎𝑡𝑎 (𝑥 ) [𝑙𝑜𝑔𝐷 (𝑥)] + E𝑧∼𝑝𝑧 (𝑧 ) [𝑙𝑜𝑔(1 − 𝐷 (𝐺 (𝑧)))]

(15)

Manuscript submitted to ACM

---

<!-- PAGE 34 -->

34

Paparrizos et al.

For Tℓ the set of sub-sequences to train on, and Z the corresponding set of sub-sequences from the latent space

(noise sample), we have the following stochastic gradient descend:

𝐷𝑖𝑠𝑐𝑟𝑖𝑚𝑖𝑛𝑎𝑛𝑡 :∇𝜃𝑑

𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟 :∇𝜃𝑔

1
|T|

1
|Z|

∑︁

(𝑇 ,𝑍 ) ∈ (T,Z)

[−𝑙𝑜𝑔𝐷 (𝑇 ) − 𝑙𝑜𝑔(1 − 𝐷 (𝐺 (𝑍 )))]

[1 − 𝑙𝑜𝑔(1 − 𝐷 (𝐺 (𝑍 )))]

∑︁

𝑍 ∈Z

(16)

(17)

This architecture has been tried for the specific case of time-series anomaly detection [128]. For the purpose of

anomaly detection, the generator is trained to produce sub-sequences labeled as normal, and the discriminator is

trained to discriminate the anomalies. Thus training such a model requires having a training dataset with normal

sub-sequences. One can use the discriminator and the generator simultaneously to detect the anomaly. First, given that

the discriminator has been trained to separate real (i.e., normal) from fake (i.e., anomaly) sub-sequences, it can be used

as a direct tool for anomaly detection. Nevertheless, the generator can also be helpful. Given that the generator has

been trained to produce a realistic sub-sequence, it will most probably fail to produce a realistic anomaly. Therefore, the

Euclidian distance between the sub-sequence to evaluate and what would have generated the generator with the same

latent input can have some significance in discriminating anomaly.

Several anomaly detection methods based on GAN have been proposed in the literature, such as MAD-GAN [129],

USAD [8] and TAnoGAN [17]. These approaches train GAN on the normal sections of the time series. The anomaly

score is based on the combination of discriminator and reconstruction loss. VAE-GAN [171] is another GAN-based

model that combines GAN and Variational Autoencoder. More specifically, the generator is a VAE, which further

competes with the discriminator. The anomaly score is computed the same as the previous two.

9 Evolution of Methods over Time: A Meta-Analysis

At this point, we described the main methods proposed in the literature to detect anomalies in time series. We grouped

them into three first-level categories and 9 second-level categories. However, these first or second-level categories do

not share the same distribution in time. Figure 20 shows the number of methods proposed per interval of years (left)

and the cumulative number over the years (right).

We first observe that the number of methods proposed yearly was constant between 1990 and 2016. The number of

methods proposed in the literature significantly increased after 2016. This first confirms the growing academic interest

in the topic of time-series anomaly detection.

We can then dive into the second-level categories, and we observe that the significant increase in methods proposed

is caused mainly by the prediction-based approach and, more specifically, by LSTM and autoencoder-based approaches.

Between 2020 and 2023, such methods represent almost 50% of the newly introduced anomaly detection methods. The

great success of deep learning for computer vision causes such growth. Moreover, thanks to the open-source deep

learning library such as TensorFlow and PyTorch, generic deep learning methods are easy to adapt to time series.

We can then inspect the evolution of the number of methods proposed in the literature that can handle univariate or

multivariate time series. Figure 21(right) shows the number of methods for multivariate and univariate time series per

interval of years listed on the x-axis.

Surprisingly, we observe that most of the methods proposed between 1990 and 2016 were proposed for multivariate

time series, whereas, in the last three years, most of the proposed methods are for univariate time series. However,

Manuscript submitted to ACM

---

<!-- PAGE 35 -->

Dive into Time-Series Anomaly Detection: A Decade Review

35

Fig. 20. Relative number of methods proposed over time per category, at different times-intervals (left), and cumulative (right).

Fig. 21. Number of methods proposed over time that are Unsupervised/Semi-supervised (left), and that can handle univari-
ate/multivariate time series (right).

after a deep inspection, most of the methods proposed before 2016 were designed for point anomaly detection (i.e.,

well-defined problems for multivariate time series). The recent interest in sub-sequence anomaly detection, joined by

the fact that the subsequence anomaly detection problem for multivariate time series is harder to define, leads to a

significant increase in methods for univariate time series.

Finally, we can measure the evolution of the number of unsupervised and semi-supervised methods over the years.

The latter is illustrated in Figure 21(left). We observe that 65% of the anomaly detection methods proposed in the

literature were unsupervised between 1980 and 2000, whereas 50% of the methods proposed between 2012 and 2018

were unsupervised.

Manuscript submitted to ACM

---

<!-- PAGE 36 -->

36

Paparrizos et al.

Table 4. Summary of existing benchmarks for time-series anomaly detection.

Benchmark

NAB [126]
Yahoo [125]
Exathlon [108]
KDD21 [113]
TODS [123]
TimeEval [216]
TSB-UAD [185]
TSB-AD [142]

# Time
Series

58
367
93
250
54
976
14046
1070 (Curated)

Average
Length

6301.7
1561.2
25115.9
77415.1
13469.9
30991
34043.6
105485.2

Average #
Anomalies

Average
Anomaly Length

2
5.9
1
1
266.7
5.5
86.3
104.2

287.8
1.8
9537.6
196.5
2.3
106.7
24.9
409.5

Dim

I
I
M
I
I&M
I&M
I
I&M

Anomaly
Type

P&S
P&S
S
P&S
P&S
P&S
P&S
P&S

I: Univariate; M: Multivariate // P: Point; S: Subsequence
The statistics are based on the datasets downloaded during the writing of this article.

10 Evaluating Anomaly Detection

With the continuous advancement of time-series anomaly detection methods, it becomes evident that different methods

possess distinct properties and may be more suitable for specific domains. Moreover, the metrics used to evaluate

these methods vary significantly in terms of their characteristics. Consequently, evaluating and selecting the most

appropriate method for a given scenario has emerged as a major challenge in this field. In this section, we will begin

by presenting the benchmarks that have been proposed in the literature for evaluating time-series anomaly detection

methods. Then, we will discuss different evaluation measures commonly used in the field and examine their limitations

when applied to anomaly detection.

10.1 Existing Benchmarks

In previous sections, we noted that a substantial number of time-series anomaly detection methods have been developed

over the past several decades. Multiple surveys and experimental studies have evaluated the performance of various

anomaly detectors across different datasets [185, 216, 235]. These investigations have consistently highlighted the

absence of a one-size-fits-all anomaly detector. The emerging consensus acknowledges that a model performing well on

one dataset is not sufficient to declare an anomaly detection algorithm useful. The effectiveness of an anomaly detector

should be demonstrated across a wide range of datasets rather than several cherry-picking datasets. Consequently,

there have been efforts made to establish benchmarks incorporating multiple datasets from various domains to ensure

thorough and comprehensive evaluation.

In the following, we will overview recent benchmarks for time-series anomaly detection. These benchmarks are

presented chronologically, as illustrated in Table 4, with brief descriptions to demonstrate advancements in this field.

NAB [126] provides 58 labeled real-world and artificial time series, primarily focusing on real-time anomaly detection

for streaming data. It comprises diverse domains such as AWS server metrics, online advertisement clicking rates,

real-time traffic data, and a collection of Twitter mentions of large publicly-traded companies.

Yahoo [125] comprises a collection of real and synthetic time series datasets, which are derived from the real production

traffic to some of the Yahoo production systems.

Exathlon [108] is proposed for explainable anomaly detection over high-dimensional time series data. It is constructed

based on real data traces from repeated executions of large-scale stream processing jobs on an Apache Spark cluster.

KDD21 (or UCR Anomaly Archive) [113] is a composite dataset that covers various domains, such as medicine, sports,

and space science. It was designed to address the pitfalls of previous benchmarks [251].

TODS [123] refines synthetic criterion and includes five anomaly scenarios categorized by behavior-driven taxonomy

Manuscript submitted to ACM

---

<!-- PAGE 37 -->

Dive into Time-Series Anomaly Detection: A Decade Review

37

as point-global, pattern-contextual, pattern-shapelet, pattern-seasonal, and pattern-trend.

TimeEval [216] comprises a collection of datasets (both real and synthetic) from very different domains. This benchmark

contains both univariate and multivariate time series mixing both point and sequence anomalies. In addition, this
benchmark has been filtered such that there is no time series that have a normal/abnormal ratio above 0.1, and that at
least one method performs more than 0.8 AUC-ROC for each time series.

TSB-UAD [185] is a comprehensive and unified benchmark designed for evaluating univariate time-series anomaly

detection methods. It includes public datasets that contain real-world anomalies, as well as synthetic datasets that

provide eleven transformation methods to emulate different anomaly types. Additionally, the benchmark incorporates

artificial datasets that are transformed from time-series classification datasets with varying levels of similarity between

normal and abnormal subsequences. This comprehensive coverage of different anomaly scenarios makes TSB-UAD a

uniform platform to compare different methods across different realistic scenarios.

We note that there are ongoing discussions regarding the limitations of certain datasets used in existing benchmarks.

Wu et al. [251] identify four common flaws: (i) triviality, (ii) unrealistic anomaly density, (iii) mislabeled ground truth, and

(iv) run-to-failure bias. Such issues underscore the substantial challenges in designing truly representative benchmarks.

In response, Wu et al. develop a manually curated dataset consisting primarily of univariate time series featuring a

single, often artificially introduced anomaly. However, this dataset may not accurately reflect real-world scenarios

(given that most previously published real-world datasets contain multiple anomalies) and excludes other potentially

anomalous regions, resulting in a new set of labeling ambiguities. To address these concerns, TSB-AD [142] introduces

the first large-scale, heterogeneous, and meticulously curated dataset, combining human perception with model-driven

interpretation to offer improved reliability.

TSB-AD [142] is the largest benchmark to date, comprising 1,000 rigorously curated, high-quality time series datasets.

This benchmark include both univariate and multivariate cases, ensuring coverage of a wide range of real-world

scenarios for anomaly detection. It establishes a reliable framework for evaluating methods and includes comprehensive
benchmarking of 40 anomaly detection approaches (continuously updating2). Each method undergoes a thorough
hyperparameter tuning to ensure optimal performance. The benchmark also incorporates the latest advances in

foundation model-based methods, highlighting their potential for time series anomaly detection.

10.2 Evaluation Measures

In this section, we present an overview of evaluation metrics used to assess the performance of anomaly detectors.

There are various ways to categorize the evaluation metrics. It can be classified based on whether a threshold needs to

be set or if the evaluation is conducted on independent time points or sequences. In the following, we will categorize

the evaluation based on the requirement of threshold setting.

10.2.1 Threshold-based Evaluation. Threshold-based evaluation requires setting a threshold to classify each point (time
step) as an anomaly or not based on the anomaly score 𝑆𝑇 . Generally, a higher anomaly score value indicates a more
abnormal point. The most straightforward approach is to set the threshold to 𝜇 (𝑆𝑇 ) + 𝛼 ∗ 𝜎 (𝑆𝑇 ), with 𝛼 set to 3 [15],
where 𝜇 (𝑆𝑇 ) is the mean and 𝜎 (𝑆𝑇 ) is the standard deviation of 𝑆𝑇 . However, this approach is sensitive to extreme
values in the anomaly score and can result in unfair comparisons between different methods due to variations in their

statistical properties.

2https://thedatumorg.github.io/TSB-AD

Manuscript submitted to ACM

---

<!-- PAGE 38 -->

38

Paparrizos et al.

Fig. 22. Illustration of evaluation measures for time-series anomaly detection.

To address this issue, researchers in the field have developed alternative methods for threshold selection that operate

automatically, eliminating the need for statistical assumptions regarding errors. For instance, [5] introduced an adaptive

thresholding technique that exploits the consistent time correlation structure observed in anomaly scores during

benign activity periods. This technique dynamically adjusts the threshold based on predicted future anomaly scores.

Non-parametric dynamic thresholding, proposed in [104], aims to find a threshold such that removing all values above

it results in the greatest percentage decrease in the mean and standard deviation of the anomaly scores. Another

approach, known as Peaks-Over-Threshold (POT) [224, 232], involves an initial threshold selection, identification of

extreme values in the tails of a probability distribution, fitting the tail portion with a generalized Pareto distribution

with parameters, computing anomaly scores based on the estimated distribution, and applying a secondary threshold to

identify anomalies.

After setting the threshold, we can classify the points as either normal or abnormal based on whether they exceed

the threshold. In the subsequent section, we will review common evaluation measures. We begin by presenting

the necessary definitions and formulations for introducing these measures, followed by a brief explanation of their
distinctions. Formally, the binary predictions 𝑝𝑟𝑒𝑑 ∈ {0, 1}𝑛 are obtained by comparing 𝑆𝑇 with threshold 𝑇ℎ as:




By comparing 𝑝𝑟𝑒𝑑 to the true-labeled anomalies 𝑙𝑎𝑏𝑒𝑙 ∈ {0, 1}𝑛, the points can fall into one of the following four

if: 𝑆𝑇 𝑖 < 𝑇ℎ
if: 𝑆𝑇 𝑖 ≥ 𝑇ℎ

∀𝑖 ∈ [1, |𝑆𝑇 |], 𝑝𝑟𝑒𝑑𝑖 =

(18)

1,

0,

categories:

• True Positive (TP): Number of points that have been correctly identified as anomalies.
• True Negative (TN): Number of points that have been correctly identified as normal.
• False Positive (FP): Number of points that have been wrongly identified as anomalies.
• False Negative (FN): Number of points that have been wrongly identified as normal.

Given these four categories, several point-wise evaluation measures have been proposed to assess the accuracy of

anomaly detection methods.

Precision (or positive predictive value) is the number of correctly identified anomalies over the total number of points

Manuscript submitted to ACM

---

<!-- PAGE 39 -->

Dive into Time-Series Anomaly Detection: A Decade Review

39

detected as anomalies by the method:

𝑇 𝑃
𝑇 𝑃 +𝐹 𝑃 .

Recall (or True Positive Rate, TPR) is the number of correctly identified anomalies over all anomalies:

𝑇 𝑃
𝑇 𝑃 +𝐹 𝑁 .

False Positive Rate (or FPR) is the number of points wrongly identified as anomalies over the total number of normal

points:

𝐹 𝑃

𝐹 𝑃 +𝑇 𝑁 . Contrary to Recall, the optimal score is obtained by predicting all the points as normal.

F-Score combines precision and recall into a single metric by taking their harmonic mean, with a non-negative real
value of 𝛽:
Precision@k is the precision of a subset of anomalies corresponding to 𝑘 highest value in the anomaly score 𝑆𝑇 .

. Usually, 𝛽 is set to 1, balancing the importance between Precision and Recall.

(1+𝛽 2 )∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙
𝛽 2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙

While most current methods [222, 232, 255] calculate these metrics by treating time points as independent samples,

they often employ point adjustment techniques to account for consecutive anomalies. This means that detecting any

point within an anomalous segment is considered as if all points within that segment were detected, as is shown in

Figure 22(a). However, the work of [118] criticizes the use of point-adjusted metrics, demonstrating that they have a high

likelihood of overestimating detection performance and that even a random anomaly score can yield seemingly good
results. In light of this critique, [118] propose Point-adjusted metrics at 𝐾%, wherein a predetermined proportion 𝐾%
of anomalies must be detected before the application of point adjustment. Other refined point-adjusted metrics include

Delay thresholded point-adjusted F-score in [52, 204]. This metric considers an anomaly to be detected only if it is
predicted within the first 𝑘 time steps of the truth-labeled anomaly.

Furthermore, the above-mentioned metrics ignore the sequential nature of time series. A range-based quality

measure [237] was recently proposed to address the shortcomings of point-based measures. This definition considers

several factors: (i) whether a subsequence is detected or not (ExistenceReward); (ii) how many points in the subsequence

are detected (OverlapReward); (iii) which part of the subsequence is detected (position-dependent weight function);

and (iv) how many fragmented regions correspond to one real subsequence outlier (CardinalityFactor). In this way,

point-based Precision and Recall can be extended to calculating Range-based F-score.

Other metrics include NAB score [126], which penalizes false positive points by assigning a negative value and

provides positive value rewards for accurately detecting anomalous segments, with the reward being higher for early

prediction of the first anomalous point. It is noteworthy that the utilization of the NAB score itself is not widespread;

however, the benchmark introduced in this paper is widely adopted in the research community for evaluation using

other metrics.

10.2.2 Threshold-independent Evaluation. The requirement to apply a threshold to the anomaly score significantly

affects the accuracy measures. They can vary significantly when the threshold changes. According to a recent work [180],

threshold-based measures are particularly sensitive to the noisy anomaly score, which stem from noise in the original time

series. As the score fluctuates around the threshold, they become less robust to noise. Moreover, the normal/abnormal

ratio, which exhibits considerable variability across different tasks, further influences the threshold. Notably, variations

in this ratio can lead to variations in the threshold, consequently impacting the values of threshold-based accuracy

measures. Additionally, detectors may introduce a lag into the anomaly score, and there may be inherent lag resulting

from the approximation made during the labeling phase. Even small lags can have a significant impact on these

evaluation measures. Therefore, many works consider threshold selection as a problem orthogonal to model evaluation

and use metrics that summarize the model performance across all possible thresholds. We will introduce several

threshold-independent evaluation measures as follows.

Best F-Score: Maximum F-Score over all possible thresholds.

AUC: The Area Under the Receiver Operating Characteristics curve (AUC-ROC) [66] is a widely used evaluation

Manuscript submitted to ACM

---

<!-- PAGE 40 -->

40

Paparrizos et al.

metric in anomaly detection, as well as in binary classification in general. It quantifies the performance of a model

by measuring the area under the curve that represents the true positive rate (TPR) on the y-axis against the false

positive rate (FPR) on the x-axis, as depicted in Figure 22(b.1). AUC-ROC represents the probability that a randomly

chosen positive example will be ranked higher than a randomly chosen negative example. It is computed using the
trapezoidal rule. For that purpose, we define an ordered set of thresholds, denoted as 𝑇ℎ, ranging from 0 to 1, where
𝑇ℎ = [𝑇ℎ0,𝑇ℎ1, ...𝑇ℎ𝑁 ] with 0 = 𝑇ℎ0 < 𝑇ℎ1 < ... < 𝑇ℎ𝑁 = 1. Therefore, 𝐴𝑈 𝐶-𝑅𝑂𝐶 is defined as follows:
𝑁
1
∑︁
2

𝑇 𝑃𝑅 ∗ Δ𝑘
Δ𝑘

𝐴𝑈𝐶-𝑅𝑂𝐶 =

𝐹 𝑃𝑅

𝑘=1

(19)

with:





Δ𝑘
𝐹 𝑃𝑅 = 𝐹 𝑃𝑅(𝑇ℎ𝑘 ) − 𝐹 𝑃𝑅(𝑇ℎ𝑘 −1)
Δ𝑘
𝑇 𝑃𝑅 = 𝑇 𝑃𝑅(𝑇ℎ𝑘 −1) + 𝑇 𝑃𝑅(𝑇ℎ𝑘 )

The Area Under the Precision-Recall curve (AUC-PR) [58] is similar, but with the Recall (TPR) on the x-axis and

Precision on the y-axis. The Precision and FPR exhibit distinct responses to changes in false positives in the context of

anomaly detection. In this domain, the number of true negatives tends to be substantially larger than the number of

false positives, resulting in low FPR values for various threshold choices that are relevant. Consequently, only a small

portion of the ROC curve holds relevance under such circumstances. One potential approach to address this issue is to

focus solely on specific segments of the curve [10]. Alternatively, the use of the AUC-PR has been advocated as a more

informative alternative to ROC for imbalanced datasets [145].

Range-AUC: AUC-ROC and AUC-PR are primarily designed for point-based anomalies, treating each point inde-

pendently and assigning equal weight to the detection of each point in calculating the overall AUC. However, these

metrics may not be ideal for assessing subsequence anomalies. There are several reasons for this limitation, including

the importance of detecting even small segments within subsequence outliers, the absence of consistent labeling con-

ventions across datasets, especially for subsequences, and the sensitivity of the anomaly scores to time lags introduced

by detectors. To address these limitations, an extension of the ROC and PR curves called Range-AUC [180] has been

introduced specifically for subsequences. By adding a buffer region at the outliers’ boundaries as shown in Figure

22(b.2), it accounts for the false tolerance of labeling in the ground truth and assigns higher anomaly scores near the

outlier boundaries. It replaces binary labels with continuous values in the range [0, 1]. This refinement enables the

adaptation of point-based TPR, FPR, and Precision to better suit subsequence anomaly cases.
Volume Under the Surface (VUS) [180]: The buffer length in Range-AUC, denoted as 𝑙, needs to be predefined. If not
properly set, it can strongly influence range-AUC measures. To eliminate this influence, VUS computes Range-AUC
for different buffer lengths from 0 to the 𝑙, which leads to the creation of a three-dimensional surface in the ROC-PR
space as shown in Figure 22(b.3). The VUS family of measures, including VUS-ROC and VUS-PR, are parameter-free

and threshold-independent, applicable for evaluating both point-based and range-based anomalies.

Different evaluation methods have different properties, including robustness to lag and noise, the separability to

differentiate between accurate and inaccurate methods, and the need for parameters, etc. Therefore, the selection of

evaluation metrics should be approached with caution, considering the specific requirements of the task. For detailed

case studies highlighting the properties of different metrics, we recommend referring to the following papers [180, 229].

In terms of key takeaways, we recommend utilizing threshold-independent evaluation measures to mitigate potential

biases introduced by threshold selection. AUC-based measures have been widely adopted in this regard. However, their

limitations lie in the lack of consideration for the consistency of time series. To address this, Range-AUC has refined

Manuscript submitted to ACM

---

<!-- PAGE 41 -->

Dive into Time-Series Anomaly Detection: A Decade Review

41

the AUC-based measures. Among the range-based measures, VUS-ROC stands out for its robustness, separability,

and consistency in ranking the accuracy of detectors across diverse datasets, making it a recommended choice as the

evaluation measure of preference.

11 Conclusions

In this survey, we examined into the anomaly detection problem in time series. We started by defining a taxonomy of

time series types, anomaly types, and anomaly detection methods. We grouped the methods into multiple process-centric

categories. We then described the most popular anomaly detection methods for each category in detail, and provided an

extensive list of other existing methods. We finally discussed the problem of benchmarking and evaluation of anomaly

detection methods in time series. We initiated this discussion by listing the time series dataset and benchmark proposed

in the literature. We then listed the traditional evaluation measures used to assess the detection quality, discussed their

limitations, and introduced a recent effort to adapt these measures to the context of time series.

Despite the decades-long worth of research in this area, time-series anomaly detection remains a challenging problem.

Several communities have tackled the problem separately, introducing methods that follow their corresponding

fundamental concepts. Since these methods were not compared on the same basis (i.e., using the same evaluation

measures and datasets), the progress of anomaly detection methods has been challenging to assess. However, the recent

efforts in proposing benchmarks [113, 185] has helped to evaluate the progress and identify appropriate methods for

specific problems [185, 216].

Nevertheless, multiple research directions remain open. First, there is no agreement yet on a single benchmark

that the entire community should use. Even though numerous benchmarks have been proposed, they have their own

limitations concerning the diversity of time series, anomaly types, or uncertain labels. There is a need to agree as a

community on a common basis for comparing the anomaly detection methods.

Second, encouraged by the current momentum, many novel methods are proposed every year. However, recent

evaluations suggested [185, 216] that no single best method exists (i.e., achieving the best performance on every dataset).

This observation opens a new direction of research towards ensembling, model selection, and AutoML. A recent

experimental evaluation [235] concluded that simple time series classification baselines can be used for model selection

for time-series anomaly detection, leading to accuracy improvements by a factor of 2 compared to the best performing

individual anomaly detection method. This study suggests that we can be optimistic about further improvements in

accuracy, by continuing the research in this direction.

Finally, even though a large number of unsupervised methods have been proposed for univariate time-series anomaly

detection, not much attention has been paid to multivariate time series, streaming time series, series with missing

values, series with non-continuous timestamps, heterogeneous time series, or a combination of the above. Such times

series are often encountered in practice, thus we need robust and accurate methods for these cases, as well.

References

[1] Ali Abdul-Aziz, Mark Woike, Nikunj Oza, Bryan Matthews, and George Baakilini. 2010. Propulsion health monitoring of a turbine engine disk
using spin test data. In Health Monitoring of Structural and Biological Systems 2010, Tribikram Kundu (Ed.), Vol. 7650. International Society for
Optics and Photonics, SPIE, 431 – 440. https://doi.org/10.1117/12.847574

[2] Charu C Aggarwal. 2017. An introduction to outlier analysis. In Outlier analysis. Springer, 1–34.
[3] Subutai Ahmad, Alexander Lavin, Scott Purdy, and Zuha Agha. 2017. Unsupervised Real-Time Anomaly Detection for Streaming Data. 262 (2017),

134–147. https://doi.org/10.1016/j.neucom.2017.04.070

[4] Shadab Alam, Franco D Albareti, Carlos Allende Prieto, Friedrich Anders, Scott F Anderson, Timothy Anderton, Brett H Andrews, Eric Armengaud,
Éric Aubourg, Stephen Bailey, et al. 2015. The eleventh and twelfth data releases of the Sloan Digital Sky Survey: final data from SDSS-III. The

Manuscript submitted to ACM

---

<!-- PAGE 42 -->

42

Paparrizos et al.

Astrophysical Journal Supplement Series 219, 1 (2015), 12.

[5] Muhammad Qasim Ali, Ehab Al-Shaer, Hassan Khan, and Syed Ali Khayam. 2013. Automated anomaly detector adaptation using adaptive threshold

tuning. ACM Transactions on Information and System Security (TISSEC) 15, 4 (2013), 1–30.

[6] Francisco Martinez Alvarez, Alicia Troncoso, Jose C Riquelme, and Jesus S Aguilar Ruiz. 2010. Energy time series forecasting based on pattern

sequence similarity. IEEE Transactions on Knowledge and Data Engineering 23, 8 (2010), 1230–1243.

[7] Jérôme Antoni and Pietro Borghesani. 2019. A Statistical Methodology for the Design of Condition Indicators. 114 (2019), 290–327. https:

//doi.org/10.1016/j.ymssp.2018.05.012

[8] Julien Audibert, Pietro Michiardi, Frédéric Guyard, Sébastien Marti, and Maria A Zuluaga. 2020. Usad: Unsupervised anomaly detection on

multivariate time series. In SIGKDD. 3395–3404.

[9] Martin Bach-Andersen, Bo Rømer-Odgaard, and Ole Winther. 2017. Flexible non-linear predictive models for large-scale wind turbine diagnostics.

Wind Energy 20, 5 (2017), 753–764.

[10] Stuart G Baker and Paul F Pinsky. 2001. A proposed design and analysis for comparing digital and analog mammography: special receiver operating

characteristic methods for cancer screening. J. Amer. Statist. Assoc. 96, 454 (2001), 421–428.

[11] Ziv Bar-Joseph. 2004. Analyzing time series gene expression data. Bioinformatics 20, 16 (2004), 2493–2503.
[12] Ziv Bar-Joseph, Georg K Gerber, David K Gifford, Tommi S Jaakkola, and Itamar Simon. 2003. Continuous representations of time-series gene

expression data. Journal of Computational Biology 10, 3-4 (2003), 341–356.

[13] Ziv Bar-Joseph, Anthony Gitter, and Itamar Simon. 2012. Studying and modelling dynamic biological processes using time-series gene expression

data. Nature Reviews Genetics 13, 8 (2012), 552.

[14] Mohini Bariya, Alexandra von Meier, John Paparrizos, and Michael J Franklin. 2021. k-ShapeStream: Probabilistic Streaming Clustering for Electric

Grid Events. In 2021 IEEE Madrid PowerTech. IEEE, 1–6.

[15] V. Barnet and T. Lewis. 1994. Outliers in Statistical Data. John Wiley and Sons, Inc.
[16] Vic Barnett and Toby Lewis. 1984. Outliers in statistical data. Wiley Series in Probability and Mathematical Statistics. Applied Probability and

Statistics (1984).

[17] Md Abul Bashar and Richi Nayak. 2020. TAnoGAN: Time series anomaly detection with generative adversarial networks. In SSCI. IEEE, 1778–1785.
[18] Sabyasachi Basu and Martin Meckesheimer. 2007. Automatic Outlier Detection for Time Series: An Application to Sensor Data. 11, 2 (2007),

137–154. https://doi.org/10.1007/s10115-006-0026-6

[19] Daniel Bernoulli and CG Allen. 1961. The most probable choice between several discrepant observations and the formation therefrom of the most

likely induction. Biometrika 48, 1-2 (1961), 3–18.

[20] Arpita Bhargava and AS Raghuvanshi. 2013. Anomaly detection in wireless sensor networks using S-Transform in combination with SVM. In 2013

5th International Conference and Computational Intelligence and Communication Networks. IEEE, 111–116.

[21] Bharat B Biswal, Maarten Mennes, Xi-Nian Zuo, Suril Gohel, Clare Kelly, Steve M Smith, Christian F Beckmann, Jonathan S Adelstein, Randy L
Buckner, Stan Colcombe, et al. 2010. Toward discovery science of human brain function. Proceedings of the National Academy of Sciences 107, 10
(2010), 4734–4739.

[22] Ane Blázquez-García, Angel Conde, Usue Mori, and Jose A Lozano. 2021. A review on outlier/anomaly detection in time series data. ACM

Computing Surveys (CSUR) 54, 3 (2021), 1–33.

[23] Paul Boniol, Michele Linardi, Federico Roncallo, and Themis Palpanas. 2020. Automated Anomaly Detection in Large Sequences. In Proceedings of

the International Conference on Data Engineering (ICDE). 1834–1837. https://doi.org/10.1109/ICDE48307.2020.00182

[24] Paul Boniol, Michele Linardi, Federico Roncallo, and Themis Palpanas. 2020. SAD: An Unsupervised System for Subsequence Anomaly Detection.

In Proceedings of the International Conference on Data Engineering (ICDE). 1778–1781. https://doi.org/10.1109/ICDE48307.2020.00168

[25] Paul Boniol, Michele Linardi, Federico Roncallo, Themis Palpanas, Mohammed Meftah, and Emmanuel Remy. 2021. Unsupervised and scalable

subsequence anomaly detection in large data series. The VLDB Journal (March 2021). https://doi.org/10.1007/s00778-021-00655-8

[26] Paul Boniol and Themis Palpanas. 2020. Series2Graph: Graph-Based Subsequence Anomaly Detection for Time Series. 13, 11 (2020), 14.

https://doi.org/10.14778/3407790.3407792

[27] Paul Boniol, John Paparrizos, Yuhao Kang, Themis Palpanas, Ruey S Tsay, Aaron J Elmore, and Michael J Franklin. 2022. Theseus: navigating the

labyrinth of time-series anomaly detection. Proceedings of the VLDB Endowment 15, 12 (2022), 3702–3705.

[28] Paul Boniol, John Paparrizos, and Themis Palpanas. 2023. New Trends in Time Series Anomaly Detection.. In EDBT. 847–850.
[29] Paul Boniol, John Paparrizos, and Themis Palpanas. 2024. An Interactive Dive into Time-Series Anomaly Detection. In 2024 IEEE 40th International

Conference on Data Engineering (ICDE).

[30] Paul Boniol, John Paparrizos, Themis Palpanas, and Michael J Franklin. 2021. Sand in action: subsequence anomaly detection for streams. Proceedings

of the VLDB Endowment 14, 12 (2021), 2867–2870.

[31] Paul Boniol, John Paparrizos, Themis Palpanas, and Michael J Franklin. 2021. SAND: streaming subsequence anomaly detection. PVLDB 14, 10

(2021), 1717–1729.

[32] Paul Boniol, Emmanouil Sylligardos, John Paparrizos, Panos Trahanias, and Themis Palpanas. 2024. ADecimo: Model Selection for Time Series

Anomaly Detection. In 2024 IEEE 40th International Conference on Data Engineering (ICDE).

[33] Mohammad Braei and Sebastian Wagner. 2020. Anomaly detection in univariate time-series: A survey on the state-of-the-art. arXiv preprint

arXiv:2004.00433 (2020).

Manuscript submitted to ACM

---

<!-- PAGE 43 -->

Dive into Time-Series Anomaly Detection: A Decade Review

43

[34] Markus M Breunig, Hans-Peter Kriegel, Raymond T Ng, and Jörg Sander. 2000. LOF: identifying density-based local outliers. In Proceedings of the

2000 ACM SIGMOD international conference on Management of data. 93–104.

[35] Markus M. Breunig, Hans-Peter Kriegel, Raymond T. Ng, and Jörg Sander. 2000. LOF: Identifying Density-based Local Outliers. In SIGMOD.
[36] Peter J Brockwell and Richard A Davis. 2016. Introduction to time series and forecasting. springer.
[37] Yingyi Bu, Oscar Tat-Wing Leung, Ada Wai-Chee Fu, Eamonn J. Keogh, Jian Pei, and Sam Meshkin. 2007. WAT: Finding Top-K Discords in Time

Series Database. In SIAM.

[38] Suratna Budalakoti, Ashok N Srivastava, and Matthew Eric Otey. 2008. Anomaly detection and diagnosis algorithms for discrete symbol sequences

with applications to airline safety. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 39, 1 (2008), 101–113.

[39] C. Bui, N. Pham, A. Vo, A. Tran, A. Nguyen, and T. Le. 2018. Time Series Forecasting for Healthcare Diagnosis and Prognostics with the Focus
on Cardiovascular Diseases. In International Conference on the Development of Biomedical Engineering in Vietnam (BME6). Springer Singapore,
Singapore, 809–818.

[40] Ander Carreño, Iñaki Inza, and Jose A Lozano. 2020. Analyzing rare event, anomaly, novelty and outlier detection terms under the supervised

classification framework. Artificial Intelligence Review 53, 5 (2020), 3575–3594.

[41] Mete Celik, Filiz Dadaser-Celik, and Ahmet Sakir Dokuz. 2011. Anomaly detection in temperature data using DBSCAN algorithm. 2011 International

Symposium on Innovations in Intelligent Systems and Applications (2011), 91–95.

[42] Soumen Chakrabarti, Sunita Sarawagi, and Byron Dom. 1998. Mining Surprising Patterns Using Temporal Description Length. In Proceedings of the
International Conference on Very Large Databases (VLDB) (VLDB ’98, Vol. 24). Morgan Kaufmann Publishers Inc., 606–617. https://dl.acm.org/doi/10.
5555/645924.671328

[43] Raghavendra Chalapathy and Sanjay Chawla. 2019. Deep Learning for Anomaly Detection: A Survey. arXiv:1901.03407 [cs, stat] http://arxiv.org/

abs/1901.03407

[44] Raghavendra Chalapathy, Aditya Krishna Menon, and Sanjay Chawla. 2017. Robust, Deep and Inductive Anomaly Detection. In Machine Learning
and Knowledge Discovery in Databases, Michelangelo Ceci, Jaakko Hollmén, Ljupčo Todorovski, Celine Vens, and Sašo Džeroski (Eds.). Springer
International Publishing, Cham, 36–51.

[45] Varun Chandola, Arindam Banerjee, and Vipin Kumar. 2009. Anomaly detection: A survey. ACM computing surveys (CSUR) 41, 3 (2009), 1–58.
[46] Varun Chandola, Arindam Banerjee, and Vipin Kumar. 2009. Anomaly Detection: A Survey. 41, 3 (2009), 1–58. https://doi.org/10.1145/1541880.

1541882

[47] V. Chandola, A. Banerjee, and V. Kumar. 2012. Anomaly Detection for Discrete Sequences: A Survey. 24, 5 (2012), 823–839. https://doi.org/10.

1109/TKDE.2010.235

[48] Ih Chang, George C Tiao, and Chung Chen. 1988. Estimation of time series parameters in the presence of outliers. Technometrics 30, 2 (1988),

193–204.

[49] Marcus Chang, Andreas Terzis, and Philippe Bonnet. 2009. Mote-Based Online Anomaly Detection Using Echo State Networks. In Proceedings of the
International Conference on Distributed Computing in Sensor Systems (DCOOS) (Lecture Notes in Computer Science, Vol. 5516), Bhaskar Krishnamachari,
Subhash Suri, Wendi Heinzelman, and Urbashi Mitra (Eds.). Springer Berlin Heidelberg, 72–86. https://doi.org/10.1007/978-3-642-02085-8_6
[50] S. Chauhan and L. Vig. 2015. Anomaly Detection in ECG Time Signals via Deep Long Short-Term Memory Networks. In Proceedings of the

International Conference on Data Science and Advanced Analytics (DSAA). 1–7. https://doi.org/10.1109/DSAA.2015.7344872

[51] Qing Chen, Anguo Zhang, Tingwen Huang, Qianping He, and Yongduan Song. 2020. Imbalanced Dataset-Based Echo State Networks for Anomaly

Detection. 32, 8 (2020), 3685–3694. https://doi.org/10.1007/s00521-018-3747-z

[52] Run-Qing Chen, Guang-Hui Shi, Wan-Lei Zhao, and Chang-Hui Liang. 2021. A joint model for IT operation series prediction and anomaly detection.

Neurocomputing 448 (2021), 130–139.

[53] Zhangyu Cheng, Chengming Zou, and Jianwei Dong. 2019. Outlier Detection Using Isolation Forest and Local Outlier Factor. In Proceedings of the

Conference on Research in Adaptive and Convergent Systems (RACS). ACM, 161–168. https://doi.org/10.1145/3338840.3355641

[54] Dhruv Choudhary, Arun Kejariwal, and Francois Orsini. 2017. On the Runtime-Efficacy Trade-off of Anomaly Detection Techniques for Real-Time

Streaming Data. arXiv:1710.04735 [cs, eess, stat] http://arxiv.org/abs/1710.04735

[55] William W. Cohen. 1995. Fast Effective Rule Induction. In Machine Learning Proceedings 1995, Armand Prieditis and Stuart Russell (Eds.). Morgan

Kaufmann, San Francisco (CA), 115–123. https://doi.org/10.1016/B978-1-55860-377-6.50023-2

[56] Andrew A. Cook, Goksel Misirli, and Zhong Fan. 2020. Anomaly Detection for IoT Time-Series Data: A Survey. 7, 7 (2020), 6481–6494.

https://doi.org/10.1109/JIOT.2019.2958185

[57] Madalena Costa, Ary L Goldberger, and C-K Peng. 2002. Multiscale entropy analysis of complex physiologic time series. Physical review letters 89,

6 (2002), 068102.

[58] Jesse Davis and Mark Goadrich. 2006. The relationship between Precision-Recall and ROC curves. In ICML. 233–240.
[59] Nan Ding, Huanbo Gao, Hongyu Bu, Haoxuan Ma, and Huaiwei Si. 2018. Multivariate-Time-Series-Driven Real-Time Anomaly Detection Based on

Bayesian Network. 18, 10 (2018), 3367. https://doi.org/10.3390/s18103367

[60] Wilfred J Dixon. 1950. Analysis of extreme values. The Annals of Mathematical Statistics 21, 4 (1950), 488–506.
[61] Adam Dziedzic, John Paparrizos, Sanjay Krishnan, Aaron Elmore, and Michael Franklin. 2019. Band-limited training and inference for convolutional

neural networks. In ICML. PMLR, 1745–1754.

Manuscript submitted to ACM

---

<!-- PAGE 44 -->

44

Paparrizos et al.

[62] Jens E d’Hondt, Odysseas Papapetrou, and John Paparrizos. 2024. Beyond the Dimensions: A Structured Evaluation of Multivariate Time Series

Distance Measures. In 2024 IEEE 40th International Conference on Data Engineering Workshops (ICDEW). IEEE, 107–112.

[63] Francis Ysidro Edgeworth. 1887. Xli. on discordant observations. The london, edinburgh, and dublin philosophical magazine and journal of science 23,

143 (1887), 364–375.

[64] Jason Ernst and Ziv Bar-Joseph. 2006. STEM: a tool for the analysis of short time series gene expression data. BMC bioinformatics 7, 1 (2006), 191.
[65] Philippe Esling and Carlos Agon. 2012. Time-series data mining. ACM Computing Surveys (CSUR) 45, 1 (2012), 12.
[66] Tom Fawcett. 2006. An introduction to ROC analysis. Pattern Recognition Letters 27, 8 (2006), 861–874. https://doi.org/10.1016/j.patrec.2005.10.010

ROC Analysis in Pattern Recognition.

[67] Pavel Filonov, Andrey Lavrentyev, and Artem Vorontsov. 2016. Multivariate industrial time series with cyber-attack simulation: Fault detection

using an lstm-based predictive data model. arXiv preprint arXiv:1612.06676 (2016).

[68] Ralph Foorthuis. 2020. On the Nature and Types of Anomalies: A Review. arXiv preprint arXiv:2007.15634 (2020).
[69] Anthony J Fox. 1972. Outliers in time series. Journal of the Royal Statistical Society: Series B (Methodological) 34, 3 (1972), 350–363.
[70] Ada Wai-Chee Fu, Oscar Tat-Wing Leung, Eamonn J. Keogh, and Jessica Lin. 2006. Finding Time Series Discords Based on Haar Transform. In

ADMA.

[71] Yifeng Gao, Jessica Lin, and Constantin Brif. 2020. Ensemble Grammar Induction For Detecting Anomalies in Time Series. In Proceedings of the

International Conference on Extending Database Technology (EDBT). https://doi.org/10.5441/002/edbt.2020.09

[72] Gabriel Garcia, Gabriel Michau, Mélanie Ducoffe, Jayant Sen Gupta, and Olga Fink. 2020. Time Series to Images: Monitoring the Condition of

Industrial Assets with Deep Learning Image Processing Algorithms. (05 2020).

[73] Gabriel Rodriguez Garcia, Gabriel Michau, Mélanie Ducoffe, Jayant Sen Gupta, and Olga Fink. 2020. Time Series to Images: Monitoring the Condition

of Industrial Assets with Deep Learning Image Processing Algorithms. arXiv:2005.07031 [cs, eess, stat] http://arxiv.org/abs/2005.07031

[74] Martin Gavrilov, Dragomir Anguelov, Piotr Indyk, and Rajeev Motwani. 2000. Mining the stock market: Which measure is best. In Proc. of the 6th

ACM SIGKDD. 487–496.

[75] Sam George. 2019. IoT Signals report: IoT’s promise will be unlocked by addressing skills shortage, complexity and security. https://blogs.microsoft.

com/blog/2019/07/30/.

[76] JWL Glaisher. 1873. On the rejection of discordant observations. Monthly Notices of the Royal Astronomical Society 33 (1873), 391–402.
[77] Steve Goddard, Sherri K Harms, Stephen E Reichenbach, Tsegaye Tadesse, and William J Waltman. 2003. Geospatial decision support for drought

risk management. Commun. ACM 46, 1 (2003), 35–37.

[78] Rahul Goel, Sandeep Soni, Naman Goyal, John Paparrizos, Hanna Wallach, Fernando Diaz, and Jacob Eisenstein. 2016. The social dynamics of
language change in online networks. In Social Informatics: 8th International Conference, SocInfo 2016, Bellevue, WA, USA, November 11-14, 2016,
Proceedings, Part I 8. Springer, 41–57.

[79] Markus Goldstein and Andreas Dengel. 2013. Histogram-based Outlier Score (HBOS): A fast Unsupervised Anomaly Detection Algorithm.
[80] Markus Goldstein and Seiichi Uchida. 2016. A comparative evaluation of unsupervised anomaly detection algorithms for multivariate data. PloS

one 11, 4 (2016), e0152173.

[81] Vanessa Gómez-Verdejo, Jerónimo Arenas-García, Miguel Lazaro-Gredilla, and Ángel Navia-Vazquez. 2011. Adaptive one-class support vector

machine. IEEE Transactions on Signal Processing 59, 6 (2011), 2975–2981.

[82] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio. 2014. Generative

adversarial nets. NeurIPS 27 (2014).

[83] BA Gould. 1855. On Peirce’s Criterion for the Rejection of Doubtful Observations, with tables for facilitating its application. The Astronomical

Journal 4 (1855), 81–87.

[84] Aditya Grover, Ashish Kapoor, and Eric Horvitz. 2015. A deep hybrid model for weather forecasting. In Proceedings of the 21th ACM SIGKDD

International Conference on Knowledge Discovery and Data Mining. ACM, 379–386.

[85] Frank E Grubbs. 1950. Sample criteria for testing outlying observations. The Annals of Mathematical Statistics (1950), 27–58.
[86] Manish Gupta, Jing Gao, Charu C. Aggarwal, and Jiawei Han. 2014. Outlier Detection for Temporal Data: A Survey. 26, 9 (2014), 2250–2267.

https://doi.org/10.1109/TKDE.2013.184

[87] Nico Görnitz, Mikio Braun, and Marius Kloft. 2015. Hidden Markov Anomaly Detection. In Proceedings of the International Conference on Machine

Learning (ICML) (ICML’15). JMLR.org, 1833–1842. https://dl.acm.org/doi/10.5555/3045118.3045313

[88] Michael Hahsler and Matthew Bolaos. 2016. Clustering Data Streams Based on Shared Density between Micro-Clusters. IEEE Trans. on Knowl. and

Data Eng. 28, 6 (jun 2016), 1449–1461. https://doi.org/10.1109/TKDE.2016.2522412

[89] Johanna Hardin and David M Rocke. 2004. Outlier detection in the multiple cluster setting using the minimum covariance determinant estimator.

Computational Statistics & Data Analysis 44, 4 (2004), 625 – 638. https://doi.org/10.1016/S0167-9473(02)00280-3

[90] Sahand Hariri, Matias Carrasco Kind, and Robert J. Brunner. 2019. Extended Isolation Forest. (2019). https://doi.org/10.1109/TKDE.2019.2947676

arXiv:1811.02141

[91] D. M Hawkins. 1980. Identification of Outliers. Springer Netherlands, Dordrecht. OCLC: 945065134.
[92] Jeff Hawkins and Richard Dawkins. 2021. A thousand brains : a new theory of intelligence. (2021).
[93] Zengyou He, Xiaofei Xu, and Shengchun Deng. 2003. Discovering cluster-based local outliers. Pattern recognition letters 24, 9-10 (2003), 1641–1650.

Manuscript submitted to ACM

---

<!-- PAGE 45 -->

Dive into Time-Series Anomaly Detection: A Decade Review

45

[94] M. A. Hearst, S. T. Dumais, E. Osuna, J. Platt, and B. Scholkopf. 1998. Support vector machines. IEEE Intelligent Systems and their Applications 13, 4

(July 1998), 18–28. https://doi.org/10.1109/5254.708428

[95] Donald O. Hebb. 1949. The organization of behavior: A neuropsychological theory. Wiley, New York.
[96] Niklas Heim and James E. Avery. 2019. Adaptive Anomaly Detection in Chaotic Time Series with a Spatially Aware Echo State Network.

arXiv:1909.01709 [cs, stat] http://arxiv.org/abs/1909.01709

[97] Jordan Hochenbaum, Owen S. Vallis, and Arun Kejariwal. 2017. Automatic Anomaly Detection in the Cloud Via Statistical Learning.

arXiv:1704.07706 [cs] http://arxiv.org/abs/1704.07706

[98] Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long Short-Term Memory. Neural Comput. 9, 8 (Nov. 1997), 1735–1780. https://doi.org/10.1162/

neco.1997.9.8.1735

[99] Victoria J. Hodge and Jim Austin. 2004. A Survey of Outlier Detection Methodologies. 22, 2 (2004), 85–126. https://doi.org/10.1007/s10462-004-4304-y
[100] Ove Hoegh-Guldberg, Peter J Mumby, Anthony J Hooten, Robert S Steneck, Paul Greenfield, Edgardo Gomez, C Drew Harvell, Peter F Sale,
Alasdair J Edwards, Ken Caldeira, et al. 2007. Coral reefs under rapid climate change and ocean acidification. science 318, 5857 (2007), 1737–1742.
[101] Rie Honda, Shuai Wang, Tokio Kikuchi, and Osamu Konishi. 2002. Mining of moving objects from time-series images and its application to satellite

weather imagery. Journal of Intelligent Information Systems 19, 1 (2002), 79–93.

[102] Pablo Huijse, Pablo A Estevez, Pavlos Protopapas, Jose C Principe, and Pablo Zegers. 2014. Computational intelligence challenges and applications

on large-scale astronomical time series databases. IEEE Computational Intelligence Magazine 9, 3 (2014), 27–39.

[103] Kyle Hundman, Valentino Constantinou, Christopher Laporte, Ian Colwell, and Tom Soderstrom. 2018. Detecting Spacecraft Anomalies Using

LSTMs and Nonparametric Dynamic Thresholding. In SIGKDD. ACM, 387–395. https://doi.org/10.1145/3219819.3219845

[104] Kyle Hundman, Valentino Constantinou, Christopher Laporte, Ian Colwell, and Tom Soderstrom. 2018. Detecting spacecraft anomalies using lstms

and nonparametric dynamic thresholding. In SIGKDD. 387–395.

[105] Mark Hung. 2017. Leading the iot, gartner insights on how to lead in a connected world. Gartner Research (2017), 1–29.
[106] JO Irwin. 1925. On a criterion for the rejection of outlying observations. Biometrika (1925), 238–250.
[107] Alan Julian Izenman. 2008. Modern multivariate statistical techniques. Regression, classification and manifold learning 10 (2008), 978–0.
[108] Vincent Jacob, Fei Song, Arnaud Stiegler, Bijan Rad, Yanlei Diao, and Nesime Tatbul. 2021. Exathlon: a benchmark for explainable anomaly detection

over time series. PVLDB 14, 11 (2021), 2613–2626.

[109] Hoyoung Jeung, Sofiane Sarni, Ioannis Paparrizos, Saket Sathe, Karl Aberer, Nicholas Dawes, Thanasis G Papaioannou, and Michael Lehning.
2010. Effective metadata management in federated sensor networks. In 2010 IEEE International Conference on Sensor Networks, Ubiquitous, and
Trustworthy Computing. IEEE, 107–114.

[110] Hao Jiang, Chunwei Liu, Qi Jin, John Paparrizos, and Aaron J Elmore. 2020. Pids: attribute decomposition for improved compression and query

performance in columnar storage. Proc. VLDB Endow 13, 6 (2020), 925–938.

[111] Hao Jiang, Chunwei Liu, John Paparrizos, Andrew A Chien, Jihong Ma, and Aaron J Elmore. 2021. Good to the Last Bit: Data-Driven Encoding

with CodecDB. In SIGMOD. 843–856.

[112] Kunio Kashino, Gavin Smith, and Hiroshi Murase. 1999. Time-series active search for quick retrieval of audio and video. In 1999 IEEE International

Conference on Acoustics, Speech, and Signal Processing. Proceedings. ICASSP99 (Cat. No. 99CH36258), Vol. 6. IEEE, 2993–2996.

[113] E. Keogh, T. Dutta Roy, U. Naik, and A Agrawal. 2021. Multi-dataset Time-Series Anomaly Detection Competition 2021, https://compete.hexagon-

ml.com/practice/competition/39/.

[114] Eamonn Keogh, Jessica Lin, and Ada Fu. 2005. Hot sax: Efficiently finding the most unusual time series subsequence. In Fifth IEEE International

Conference on Data Mining (ICDM’05). Ieee, 8–pp.

[115] Eamonn Keogh, Stefano Lonardi, and Bill’Yuan-chi’ Chiu. 2002. Finding surprising patterns in a time series database in linear time and space. In

Proceedings of the eighth ACM SIGKDD international conference on Knowledge discovery and data mining. 550–556.

[116] Eamonn Keogh, Stefano Lonardi, Chotirat Ann Ratanamahatana, Li Wei, Sang-Hee Lee, and John Handley. 2007. Compression-based data mining

of sequential data. Data Mining and Knowledge Discovery (2007).

[117] Chunggyeom Kim, Jinhyuk Lee, Raehyun Kim, Youngbin Park, and Jaewoo Kang. 2018. DeepNAP: Deep Neural Anomaly Pre-Detection in a

Semiconductor Fab. 457-458 (2018), 1–11. https://doi.org/10.1016/j.ins.2018.05.020

[118] Siwon Kim, Kukjin Choi, Hyun-Soo Choi, Byunghan Lee, and Sungroh Yoon. 2022. Towards a rigorous evaluation of time-series anomaly detection.

In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 36. 7194–7201.

[119] S Knieling, J Niediek, E Kutter, J Bostroem, CE Elger, and F Mormann. 2017. An online adaptive screening procedure for selective neuronal

responses. Journal of neuroscience methods 291 (2017), 36–42.

[120] Maria Kontaki, Anastasios Gounaris, Apostolos N Papadopoulos, Kostas Tsichlas, and Yannis Manolopoulos. 2011. Continuous monitoring of

distance-based outliers over data streams. In 2011 IEEE 27th International Conference on Data Engineering. IEEE, 135–146.

[121] Peter Krensky and Jim Hare. 2018. Hype Cycle for Data Science and Machine Learning, 2018. Gartner Company (2018).
[122] Sanjay Krishnan, Aaron J Elmore, Michael Franklin, John Paparrizos, Zechao Shang, Adam Dziedzic, and Rui Liu. 2019. Artificial intelligence in

resource-constrained and shared environments. ACM SIGOPS Operating Systems Review 53, 1 (2019), 1–6.

[123] Kwei-Herng Lai, Daochen Zha, Junjie Xu, Yue Zhao, Guanchu Wang, and Xia Hu. 2021. Revisiting Time Series Outlier Detection: Definitions and

Benchmarks. In NeurIPS.

Manuscript submitted to ACM

---

<!-- PAGE 46 -->

46

Paparrizos et al.

[124] Bouchra Lamrini, Augustin Gjini, Simon Daudin, Pascal Pratmarty, François Armando, and Louise Travé-Massuyès. 2018. Anomaly Detection

using Similarity-based One-Class SVM for Network Traffic Characterization.. In DX.

[125] N. Laptev, S. Amizadeh, and Y. Billawala. 2015. S5 - A Labeled Anomaly Detection Dataset, version 1.0(16M). https://webscope.sandbox.yahoo.com/

catalog.php?datatype=s&did=70

[126] Alexander Lavin and Subutai Ahmad. 2015. Evaluating real-time anomaly detection algorithms–the Numenta anomaly benchmark. In ICMLA.

IEEE, 38–44.

[127] Ming-Chang Lee, Jia-Chun Lin, and Ernst Gunnar Gran. 2020. RePAD: Real-Time Proactive Anomaly Detection for Time Series. In AINA,
Leonard Barolli, Flora Amato, Francesco Moscato, Tomoya Enokido, and Makoto Takizawa (Eds.). Springer International Publishing, 1291–1302.
https://doi.org/10.1007/978-3-030-44041-1_110

[128] Dan Li, Dacheng Chen, Jonathan Goh, and See-Kiong Ng. 2018. Anomaly Detection with Generative Adversarial Networks for Multivariate Time

Series. CoRR abs/1809.04758 (2018). arXiv:1809.04758 http://arxiv.org/abs/1809.04758

[129] Dan Li, Dacheng Chen, Baihong Jin, Lei Shi, Jonathan Goh, and See-Kiong Ng. 2019. MAD-GAN: Multivariate anomaly detection for time series

data with generative adversarial networks. In International conference on artificial neural networks. Springer, 703–716.

[130] Zeyan Li, Wenxiao Chen, and Dan Pei. 2018. Robust and Unsupervised KPI Anomaly Detection Based on Conditional Variational Autoencoder. In
Proceedings of the International Performance Computing and Communications Conference (IPCCC). IEEE, 1–9. https://doi.org/10.1109/PCCC.2018.
8710885

[131] Zhihua Li, Ziyuan Li, Ning Yu, Steven Wen, et al. 2017. Locality-based visual outlier detection algorithm for time series. Security and Communication

Networks 2017 (2017).

[132] Zhi Li, Hong Ma, and Yongbing Mei. 2007. A Unifying Method for Outlier and Change Detection from Data Streams Based on Local Polynomial
Fitting. In Advances in Knowledge Discovery and Data Mining, Zhi-Hua Zhou, Hang Li, and Qiang Yang (Eds.). Springer Berlin Heidelberg, Berlin,
Heidelberg, 150–161.

[133] Zheng Li, Yue Zhao, Nicola Botta, Cezar Ionescu, and Xiyang Hu. 2020. COPOD: Copula-Based Outlier Detection. In IEEE International Conference

on Data Mining (ICDM). IEEE.

[134] Michele Linardi, Yan Zhu, Themis Palpanas, and Eamonn Keogh. 2018. Matrix Profile X: VALMOD - Scalable Discovery of Variable-Length
Motifs in Data Series. In Proceedings of the International Conference on Management of Data (SIGMOD) (2018). ACM Press, 1053–1066. https:
//doi.org/10.1145/3183713.3183744

[135] Michele Linardi, Yan Zhu, Themis Palpanas, and Eamonn Keogh. 2020. Matrix profile goes MAD: variable-length motif and discord discovery in

data series. Data Mining and Knowledge Discovery 34 (2020), 1022–1071.

[136] Michele Linardi, Yan Zhu, Themis Palpanas, and Eamonn J. Keogh. 2020. Matrix Profile Goes MAD: Variable-Length Motif And Discord Discovery

in Data Series. In DAMI.

[137] Chunwei Liu, Hao Jiang, John Paparrizos, and Aaron J Elmore. 2021. Decomposed bounded floats for fast compression and queries. Proc. VLDB

Endow 14, 11 (2021), 2586–2598.

[138] Chunwei Liu, John Paparrizos, and Aaron J Elmore. 2024. Adaedge: A dynamic compression selection framework for resource constrained devices.

In 2024 IEEE 40th International Conference on Data Engineering (ICDE). IEEE, 1506–1519.

[139] Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. 2008. Isolation Forest. In Proceedings of the International Conference on Data Mining (ICDM). IEEE,

413–422. https://doi.org/10.1109/ICDM.2008.17

[140] Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. 2008. Isolation forest. In ICDM. IEEE, 413–422.
[141] Qinghua Liu, Paul Boniol, Themis Palpanas, and John Paparrizos. 2024. Time-Series Anomaly Detection: Overview and New Trends. PVLDB 17, 12

(2024), 4229–4232.

[142] Qinghua Liu and John Paparrizos. 2024. The Elephant in the Room: Towards A Reliable Time-Series Anomaly Detection Benchmark. In NeurIPS

2024.

[143] Shinan Liu, Tarun Mangla, Ted Shaowang, Jinjin Zhao, John Paparrizos, Sanjay Krishnan, and Nick Feamster. 2023. Amir: Active multimodal
interaction recognition from video and network traffic in connected environments. Proceedings of the ACM on Interactive, Mobile, Wearable and
Ubiquitous Technologies 7, 1 (2023), 1–26.

[144] Yubao Liu, Xiuwei Chen, and Fei Wang. 2009. Efficient Detection of Discords for Time Series Stream. Advances in Data and Web Management

(2009), 629–634. http://www.springerlink.com/index/n546h380446p95r7.pdf

[145] Jorge M Lobo, Alberto Jiménez-Valverde, and Raimundo Real. 2008. AUC: a misleading measure of the performance of predictive distribution

models. Global ecology and Biogeography 17, 2 (2008), 145–151.

[146] Yue Lu, Renjie Wu, Abdullah Mueen, Maria A Zuluaga, and Eamonn Keogh. 2022. Matrix profile XXIV: scaling time series anomaly detection to

trillions of datapoints and ultra-fast arriving data streams. In SIGKDD. 1173–1182.

[147] Wei Luo and Marcus Gallagher. 2011. Faster and Parameter-Free Discord Search in Quasi-Periodic Time Series. In Advances in Knowledge Discovery

and Data Mining, Joshua Zhexue Huang, Longbing Cao, and Jaideep Srivastava (Eds.).

[148] Helmut Lütkepohl, Markus Krätzig, and Peter CB Phillips. 2004. Applied time series econometrics. Cambridge university press.
[149] Junshui Ma and Simon Perkins. 2003. Online Novelty Detection on Temporal Sequences. In Proceedings of the International Conference on Knowledge

Discovery and Data Mining (SIGKDD). ACM Press, 613. https://doi.org/10.1145/956750.956828

Manuscript submitted to ACM

---

<!-- PAGE 47 -->

Dive into Time-Series Anomaly Detection: A Decade Review

47

[150] Junshui Ma and Simon Perkins. 2003. Time-series novelty detection using one-class support vector machines. In Proceedings of the International

Joint Conference on Neural Networks, 2003., Vol. 3. IEEE, 1741–1745.

[151] Mohammad Saeid Mahdavinejad, Mohammadreza Rezvan, Mohammadamin Barekatain, Peyman Adibi, Payam Barnaghi, and Amit P Sheth. 2017.

Machine learning for Internet of Things data analysis: A survey. Digital Communications and Networks (2017).

[152] Pankaj Malhotra, Anusha Ramakrishnan, Gaurangi Anand, Lovekesh Vig, Puneet Agarwal, and Gautam Shroff. 2016. LSTM-Based Encoder-Decoder

for Multi-Sensor Anomaly Detection. arXiv:1607.00148 [cs, stat] http://arxiv.org/abs/1607.00148

[153] Pankaj Malhotra, Lovekesh Vig, Gautam Shroff, and Puneet Agarwal. 2015. Long Short Term Memory Networks for Anomaly Detection in Time
Series. In Proceedings of the European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning (ESANN), Vol. 23.
http://www.elen.ucl.ac.be/Proceedings/esann/esannpdf/es2015-56.pdf

[154] Pankaj Malhotra, Lovekesh Vig, Gautam Shroff, Puneet Agarwal, et al. 2015. Long Short Term Memory Networks for Anomaly Detection in Time

Series.. In Esann, Vol. 2015. 89.

[155] Rosario N Mantegna. 1999. Hierarchical structure in financial markets. The European Physical Journal B-Condensed Matter and Complex Systems 11,

1 (1999), 193–197.

[156] Carla Marceau. 2000. Characterizing the Behavior of a Program Using Multiple-Length N-Grams. In Proceedings of the Workshop on New Security

Paradigms (NSPW). ACM Press, 101–110. https://doi.org/10.1145/366173.366197

[157] Pierre-François Marteau, Saeid Soheily-Khah, and Nicolas Béchet. 2017.

Hybrid Isolation Forest - Application to Intrusion Detection.

arXiv:1705.03800 [cs] http://arxiv.org/abs/1705.03800

[158] Francisco Martínez-Álvarez, Alicia Troncoso, Gualberto Asencio-Cortés, and José Riquelme. 2015. A survey on data mining techniques applied to

electricity-related time series forecasting. Energies 8, 11 (2015), 13162–13193.

[159] Robert L Mason and John C Young. 2002. Multivariate statistical process control with industrial applications. SIAM.
[160] Richard McCleary, Richard A Hay, Erroll E Meidinger, and David McDowall. 1980. Applied time series analysis for the social sciences. Sage

Publications Beverly Hills, CA.

[161] Kathy McKeown, Hal Daume III, Snigdha Chaturvedi, John Paparrizos, Kapil Thadani, Pablo Barrio, Or Biran, Suvarna Bothe, Michael Collins,
Kenneth R Fleischmann, et al. 2016. Predicting the impact of scientific concepts using full-text features. Journal of the Association for Information
Science and Technology 67, 11 (2016), 2684–2696.

[162] Katsiaryna Mirylenka, Vassilis Christophides, Themis Palpanas, Ioannis Pefkianakis, and Martin May. 2016. Characterizing home device usage

from wireless traffic time series.

[163] Maziar Moradi Fard, Thibaut Thonet, and Eric Gaussier. 2020. Deep k-Means: Jointly clustering with k-Means and learning representations. Pattern

Recognition Letters 138 (2020), 185 – 192. https://doi.org/10.1016/j.patrec.2020.07.028

[164] A Morales-Esteban, Francisco Martínez-Álvarez, A Troncoso, JL Justo, and Cristina Rubio-Escudero. 2010. Pattern recognition to forecast seismic

time series. Expert Systems with Applications 37, 12 (2010), 8333–8342.

[165] Cristina Morariu and Theodor Borangiu. 2018. Time series forecasting for dynamic scheduling of manufacturing processes. In 2018 IEEE International

Conference on Automation, Quality and Testing, Robotics (AQTR). 1–6. https://doi.org/10.1109/AQTR.2018.8402748

[166] Abdullah Mueen, Yan Zhu, Michael Yeh, Kaveh Kamgar, Krishnamurthy Viswanathan, Chetan Gupta, and Eamonn Keogh. 2017. The Fastest

Similarity Search Algorithm for Time Series Subsequences under Euclidean Distance.

[167] Mohsin Munir, Shoaib Ahmed Siddiqui, Andreas Dengel, and Sheraz Ahmed. 2019. DeepAnT: A Deep Learning Approach for Unsupervised

Anomaly Detection in Time Series. 7 (2019), 1991–2005. https://doi.org/10.1109/ACCESS.2018.2886457

[168] Gyoung S Na, Donghyun Kim, and Hwanjo Yu. 2018. Dilof: Effective and memory efficient local outlier detection in data streams. In SIGKDD.

1993–2002.

[169] Takaaki Nakamura, Makoto Imamura, Ryan Mercer, and Eamonn J. Keogh. 2020. MERLIN: Parameter-Free Discovery of Arbitrary Length Anomalies
in Massive Time Series Archives. In ICDM, Claudia Plant, Haixun Wang, Alfredo Cuzzocrea, Carlo Zaniolo, and Xindong Wu (Eds.). IEEE, 1190–1195.
https://doi.org/10.1109/ICDM50108.2020.00147

[170] Takaaki Nakamura, Ryan Mercer, Makoto Imamura, and Eamonn Keogh. 2023. MERLIN++: parameter-free discovery of time series anomalies.

Data Mining and Knowledge Discovery 37, 2 (2023), 670–709. https://doi.org/10.1007/s10618-022-00876-7

[171] Zijian Niu, Ke Yu, and Xiaofei Wu. 2020. LSTM-based VAE-GAN for time-series anomaly detection. Sensors 20, 13 (2020), 3738.
[172] Oliver Obst, X. Rosalind Wang, and Mikhail Prokopenko. 2008. Using Echo State Networks for Anomaly Detection in Underground Coal Mines. In
Proceedings of the International Conference on Information Processing in Sensor Networks (IPSN). IEEE, 219–229. https://doi.org/10.1109/IPSN.2008.35
[173] Alberto Ogbechie, Javier Díaz-Rozo, Pedro Larrañaga, and Concha Bielza. 2017. Dynamic Bayesian Network-Based Anomaly Detection for
In-Process Visual Inspection of Laser Surface Heat Treatment. In Proceedings of the International Conference on Machine Learning for Cyber Physical
Systems (ML4CPS), Jürgen Beyerer, Oliver Niggemann, and Christian Kühnert (Eds.). Springer Berlin Heidelberg, 17–24. https://doi.org/10.1007/978-
3-662-53806-7_3

[174] Randy Paffenroth, Kathleen Kay, and Les Servi. 2018. Robust PCA for Anomaly Detection in Cyber Networks. arXiv:1801.01571 [cs] http:

//arxiv.org/abs/1801.01571

[175] ES Page. 1957. On problems in which a change in a parameter occurs at an unknown point. Biometrika 44, 1/2 (1957), 248–252.
[176] Themis Palpanas. 2015. Data Series Management: The Road to Big Sequence Analytics. SIGMOD Rec. 44, 2 (2015), 47–52.

Manuscript submitted to ACM

---

<!-- PAGE 48 -->

48

Paparrizos et al.

[177] Girish Keshav Palshikar. 2005. Distance-based outliers in sequences. In Distributed Computing and Internet Technology: Second International

Conference, ICDCIT 2005, Bhubaneswar, India, December 22-24, 2005. Proceedings 2. Springer, 547–552.

[178] Spiros Papadimitriou, Hiroyuki Kitagawa, Phillip B Gibbons, and Christos Faloutsos. 2003. Loci: Fast outlier detection using the local correlation

integral. In ICDE. IEEE, 315–326.

[179] Ioannis Paparrizos. 2018. Fast, Scalable, and Accurate Algorithms for Time-Series Analysis. Ph. D. Dissertation. Columbia University.
[180] John Paparrizos, Paul Boniol, Themis Palpanas, Ruey S Tsay, Aaron Elmore, and Michael J Franklin. 2022. Volume under the surface: a new accuracy

evaluation measure for time-series anomaly detection. PVLDB 15, 11 (2022), 2774–2787.

[181] John Paparrizos, Ikraduya Edian, Chunwei Liu, Aaron J Elmore, and Michael J Franklin. 2022. Fast adaptive similarity search through variance-aware

quantization. In ICDE. IEEE, 2969–2983.

[182] John Paparrizos and Michael J Franklin. 2019. GRAIL: efficient time-series representation learning. Proceedings of the VLDB Endowment 12, 11

(2019), 1762–1777.

[183] John Paparrizos and Luis Gravano. 2016. k-Shape: Efficient and Accurate Clustering of Time Series. SIGMOD 45, 1 (June 2016), 69–76. https:

//doi.org/10.1145/2949741.2949758

[184] John Paparrizos and Luis Gravano. 2017. Fast and Accurate Time-Series Clustering. ACM Transactions on Database Systems (TODS) 42, 2 (2017), 8.
[185] John Paparrizos, Yuhao Kang, Paul Boniol, Ruey S Tsay, Themis Palpanas, and Michael J Franklin. 2022. TSB-UAD: an end-to-end benchmark suite

for univariate time-series anomaly detection. PVLDB 15, 8 (2022), 1697–1711.

[186] John Paparrizos, Chunwei Liu, Bruno Barbarioli, Johnny Hwang, Ikraduya Edian, Aaron J Elmore, Michael J Franklin, and Sanjay Krishnan. 2021.

VergeDB: A Database for IoT Analytics on Edge Devices.. In CIDR.

[187] John Paparrizos, Chunwei Liu, Aaron Elmore, and Michael J. Franklin. 2023. Querying Time-Series Data: A Comprehensive Comparison of Distance

Measures. IEEE Data Engineering Bulletin (DEB 2023) 47 (2023), 69–88.

[188] John Paparrizos, Chunwei Liu, Aaron J Elmore, and Michael J Franklin. 2020. Debunking four long-standing misconceptions of time-series distance

measures. In SIGMOD. 1887–1905.

[189] John Paparrizos and Sai Prasanna Teja Reddy. 2023. Odyssey: An engine enabling the time-series clustering journey. Proceedings of the VLDB

Endowment 16, 12 (2023), 4066–4069.

[190] John Paparrizos, Ryen W White, and Eric Horvitz. 2016. Detecting devastating diseases in search logs. In SIGKDD. 559–568.
[191] John Paparrizos, Ryen W White, and Eric Horvitz. 2016. Screening for pancreatic adenocarcinoma using signals from web search logs: Feasibility

study and results. Journal of oncology practice 12, 8 (2016), 737–744.

[192] John Paparrizos, Kaize Wu, Aaron Elmore, Christos Faloutsos, and Michael J Franklin. 2023. Accelerating similarity search for elastic measures: A

study and new generalization of lower bounding distances. Proceedings of the VLDB Endowment 16, 8 (2023), 2019–2032.

[193] Daehyung Park, Zackory Erickson, Tapomayukh Bhattacharjee, and Charles C. Kemp. 2016. Multimodal Execution Monitoring for Anomaly
Detection during Robot Manipulation. In Proceedings of the International Conference on Robotics and Automation (ICRA). IEEE, 407–414. https:
//doi.org/10.1109/ICRA.2016.7487160

[194] Daehyung Park, Yuuna Hoshi, and Charles C. Kemp. 2018. A Multimodal Anomaly Detector for Robot-Assisted Feeding Using an LSTM-Based

Variational Autoencoder. 3, 3 (2018), 1544–1551. https://doi.org/10.1109/LRA.2018.2801475

[195] Stephen Pauwels and Toon Calders. 2019. An Anomaly Detection Technique for Business Processes Based on Extended Dynamic Bayesian
Networks. In Proceedings of the ACM/SIGAPP Symposium on Applied Computing (SAC). ACM, 494–501. https://doi.org/10.1145/3297280.3297326
[196] Stephen Pauwels and Toon Calders. 2019. Detecting Anomalies in Hybrid Business Process Logs. 19, 2 (2019), 18–30. https://doi.org/10.1145/

3357385.3357387

[197] ERWIN S Pearson and C Chandra Sekar. 1936. The efficiency of statistical tools and a criterion for the rejection of outlying observations. Biometrika

28, 3/4 (1936), 308–320.

[198] Benjamin Peirce. 1852. Criterion for the rejection of doubtful observations. The Astronomical Journal 2 (1852), 161–163.
[199] C-K Peng, Shlomo Havlin, H Eugene Stanley, and Ary L Goldberger. 1995. Quantification of scaling exponents and crossover phenomena in

nonstationary heartbeat time series. Chaos: An Interdisciplinary Journal of Nonlinear Science 5, 1 (1995), 82–87.

[200] Dragoljub Pokrajac, Aleksandar Lazarevic, and Longin Jan Latecki. 2007.

Incremental local outlier detection for data streams. In 2007 IEEE

symposium on computational intelligence and data mining. IEEE, 504–515.

[201] Xiangfei Qiu, Jilin Hu, Lekui Zhou, Xingjian Wu, Junyang Du, Buang Zhang, Chenjuan Guo, Aoying Zhou, Christian S. Jensen, Zhenli Sheng,
and Bin Yang. 2024. TFB: Towards Comprehensive and Fair Benchmarking of Time Series Forecasting Methods. Proc. VLDB Endow. 17, 9 (2024),
2363–2377.

[202] Sridhar Ramaswamy, Rajeev Rastogi, and Kyuseok Shim. 2000. Efficient Algorithms for Mining Outliers from Large Data Sets. SIGMOD Rec. 29, 2

(may 2000), 427–438. https://doi.org/10.1145/335191.335437

[203] Usman Raza, Alessandro Camerra, Amy L Murphy, Themis Palpanas, and Gian Pietro Picco. 2015. Practical data prediction for real-world wireless

sensor networks. IEEE Transactions on Knowledge and Data Engineering 27, 8 (2015), 2231–2244.

[204] Hansheng Ren, Bixiong Xu, Yujing Wang, Chao Yi, Congrui Huang, Xiaoyu Kou, Tony Xing, Mao Yang, Jie Tong, and Qi Zhang. 2019. Time-series
anomaly detection service at microsoft. In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining.
3009–3017.

Manuscript submitted to ACM

---

<!-- PAGE 49 -->

Dive into Time-Series Anomaly Detection: A Decade Review

49

[205] Danilo Jimenez Rezende, Shakir Mohamed, and Daan Wierstra. 2014. Stochastic Backpropagation and Approximate Inference in Deep Generative

Models. In Proceedings of the 31st International Conference on ICML - Volume 32 (Beijing, China) (ICML’14). JMLR.org, II–1278–II–1286.

[206] Joshua S Richman and J Randall Moorman. 2000. Physiological time-series analysis using approximate entropy and sample entropy. American

Journal of Physiology-Heart and Circulatory Physiology 278, 6 (2000), H2039–H2049.

[207] Kexin Rong, Clara E Yoon, Karianne J Bergen, Hashem Elezabi, Peter Bailis, Philip Levis, and Gregory C Beroza. 2018. Locality-sensitive hashing

for earthquake detection: A case study of scaling data-driven science. Proceedings of the VLDB Endowment 11, 11 (2018), 1674–1687.

[208] Volker Roth. 2006. Kernel Fisher Discriminants for Outlier Detection. 18, 4 (2006), 942–960. https://doi.org/10.1162/neco.2006.18.4.942
[209] Peter Rousseeuw. 1984. Least Median of Squares Regression. Journal of The American Statistical Association - J AMER STATIST ASSN 79 (12 1984),

871–880. https://doi.org/10.1080/01621459.1984.10477105

[210] Peter J. Rousseeuw and Katrien Van Driessen. 1999. A Fast Algorithm for the Minimum Covariance Determinant Estimator. Technometrics 41, 3

(1999), 212–223. https://doi.org/10.1080/00401706.1999.10485670 arXiv:https://www.tandfonline.com/doi/pdf/10.1080/00401706.1999.10485670

[211] Peter J. Rousseeuw and Annick M. Leroy. 1987. Robust regression and outlier detection. Wiley, New York.
[212] Peter J Rousseeuw and Annick M Leroy. 2005. Robust regression and outlier detection. Vol. 589. John wiley & sons.
[213] Eduardo J Ruiz, Vagelis Hristidis, Carlos Castillo, Aristides Gionis, and Alejandro Jaimes. 2012. Correlating financial time series with micro-blogging

activity. In Proceedings of the fifth ACM international conference on Web search and data mining. ACM, 513–522.

[214] Stan Salvador and Philip Chan. 2005. Learning States and Rules for Detecting Anomalies in Time Series. 23, 3 (2005), 241–255.

https:

//doi.org/10.1007/s10489-005-4610-3

[215] Jörg Sander, Martin Ester, Hans-Peter Kriegel, and Xiaowei Xu. 1998. Density-Based Clustering in Spatial Databases: The Algorithm GDBSCAN

and Its Applications. Data Mining and Knowledge Discovery 2, 2 (01 Jun 1998), 169–194. https://doi.org/10.1023/A:1009745219419

[216] Sebastian Schmidl, Phillip Wenig, and Thorsten Papenbrock. 2022. Anomaly Detection in Time Series: A Comprehensive Evaluation. PVLDB 15, 9

(may 2022), 1779–1797. https://doi.org/10.14778/3538598.3538602

[217] Johannes Schneider, Phillip Wenig, and Thorsten Papenbrock. 2021. Distributed Detection of Sequential Anomalies in Univariate Time Series. The

VLDB Journal 30, 4 (mar 2021), 579–602. https://doi.org/10.1007/s00778-021-00657-6

[218] Bernhard Schölkopf, Robert C Williamson, Alex Smola, John Shawe-Taylor, and John Platt. 1999. Support vector method for novelty detection.

NeurIPS 12 (1999).

[219] Pavel Senin, Jessica Lin, Xing Wang, Tim Oates, Sunil Gandhi, Arnold P. Boedihardjo, Crystal Chen, and Susan Frankenstein. 2015. Time series

anomaly discovery with grammar-based compression. In EDBT.

[220] Pavel Senin, Jessica Lin, Xing Wang, Tim Oates, Sunil Gandhi, Arnold P. Boedihardjo, Crystal Chen, and Susan Frankenstein. 2015. Time Series

Anomaly Discovery with Grammar-Based Compression. , 481–492 pages. https://doi.org/10.5441/002/edbt.2015.42

[221] Dennis Shasha. 1999. Tuning time series queries in finance: Case studies and recommendations. IEEE Data Eng. Bull. 22, 2 (1999), 40–46.
[222] Lifeng Shen, Zhuocong Li, and James Kwok. 2020. Timeseries anomaly detection using temporal hierarchical one-class network. NeurIPS 33 (2020),

13016–13026.

[223] S-C. Chen K. Sarinnapakorn Shyu, M-L. and LW. Chang. 2003. A Novel Anomaly Detection Scheme Based on Principal Component Classifier.

(2003).

[224] Alban Siffer, Pierre-Alain Fouque, Alexandre Termier, and Christine Largouet. 2017. Anomaly detection in streams with extreme value theory. In

Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 1067–1075.

[225] David Eugene Smith. 2012. A source book in mathematics. Courier Corporation.
[226] Ralph D. Snyder and Stephen J. Withers. 1983. Exponential smoothing with finite sample correction. Number 1983,1 in Working paper. Department

of Econometrics and Operations Research. Monash University. Dept., Univ, Clayton.

[227] Maximilian Soelch, Justin Bayer, Marvin Ludersdorfer, and Patrick van der Smagt. 2016. Variational Inference for On-Line Anomaly Detection in

High-Dimensional Time Series. arXiv:1602.07109 [cs, stat] http://arxiv.org/abs/1602.07109

[228] Hongchao Song, Zhuqing Jiang, Aidong Men, and Bo Yang. 2017. A Hybrid Semi-Supervised Anomaly Detection Model for High-Dimensional

Data. Computational Intelligence and Neuroscience 2017 (15 Nov 2017), 8501683. https://doi.org/10.1155/2017/8501683

[229] Sondre Sørbø and Massimiliano Ruocco. 2023. Navigating the Metric Maze: A Taxonomy of Evaluation Metrics for Anomaly Detection in Time

Series. arXiv preprint arXiv:2303.01272 (2023).

[230] EJ Stone. 1873. On the rejection of discordant observations. Monthly Notices of the Royal Astronomical Society 34 (1873), 9.
[231] Ya Su, Youjian Zhao, Chenhao Niu, Rong Liu, Wei Sun, and Dan Pei. 2019. Robust Anomaly Detection for Multivariate Time Series through

Stochastic Recurrent Neural Network. In SIGKDD. ACM, 2828–2837. https://doi.org/10.1145/3292500.3330672

[232] Ya Su, Youjian Zhao, Chenhao Niu, Rong Liu, Wei Sun, and Dan Pei. 2019. Robust anomaly detection for multivariate time series through stochastic

recurrent neural network. In SIGKDD. 2828–2837.

[233] S. Subramaniam, T. Palpanas, D. Papadopoulos, V. Kalogeraki, and D. Gunopulos. 2006. Online Outlier Detection in Sensor Data Using Non-
Parametric Models. In Proceedings of the International Conference on Very Large Databases (VLDB) (VLDB ’06). VLDB Endowment, 187–198.
https://dl.acm.org/doi/10.5555/1182635.1164145

[234] Pei Sun, Sanjay Chawla, and Bavani Arunasalam. 2006. Mining for Outliers in Sequential Databases. In Proceedings of the International Conference

on Data Mining (ICDM). Society for Industrial and Applied Mathematics, 94–105. https://doi.org/10.1137/1.9781611972764.9

Manuscript submitted to ACM

---

<!-- PAGE 50 -->

50

Paparrizos et al.

[235] Emmanouil Sylligardos, Paul Boniol, John Paparrizos, Panos E. Trahanias, and Themis Palpanas. 2023. Choose Wisely: An Extensive Evaluation of

Model Selection for Anomaly Detection in Time Series. Proc. VLDB Endow. 16, 11 (2023), 3418–3432. https://doi.org/10.14778/3611479.3611536

[236] Jian Tang, Zhixiang Chen, Ada Wai-Chee Fu, and David W Cheung. 2002. Enhancing effectiveness of outlier detections for low density patterns. In

PAKDD. 535–548.

[237] Nesime Tatbul, Tae Jun Lee, Stan Zdonik, Mejbah Alam, and Justin Gottschlich. 2018. Precision and recall for time series. In NeurIPS. 1924–1934.
[238] David MJ Tax and Robert PW Duin. 2004. Support vector data description. Machine learning 54, 1 (2004), 45–66.
[239] Ruey S Tsay. 1988. Outliers, level shifts, and variance changes in time series. Journal of forecasting 7, 1 (1988), 1–20.
[240] Ruey S Tsay. 2014. Financial Time Series. Wiley StatsRef: Statistics Reference Online (2014), 1–23.
[241] Ruey S Tsay, Daniel Pena, and Alan E Pankratz. 2000. Outliers in multivariate time series. Biometrika 87, 4 (2000), 789–804.
[242] John W Tukey et al. 1977. Exploratory data analysis. Vol. 2. Reading, Mass.
[243] Kuniaki Uehara and Mitsuomi Shimada. 2002. Extraction of primitive motion and discovery of association rules from human motion data. In

Progress in Discovery Science. Springer, 338–348.

[244] Rafael G. Vieira, Marcos A. Leone Filho, and Robinson Semolini. 2018. An Enhanced Seasonal-Hybrid ESD Technique for Robust Anomaly Detection

on Time Series. In Simpósio Brasileiro de Redes de Computadores (SBRC), Vol. 36.

[245] Gabriel Wachman, Roni Khardon, Pavlos Protopapas, and Charles R Alcock. 2009. Kernels for periodic time series arising in astronomy. In Joint

European Conference on Machine Learning and Knowledge Discovery in Databases. Springer, 489–505.

[246] Yi Wang, Linsheng Han, Wei Liu, Shujia Yang, and Yanbo Gao. 2019. Study on Wavelet Neural Network Based Anomaly Detection in Ocean

Observing Data Series. 186 (2019), 106129. https://doi.org/10.1016/j.oceaneng.2019.106129

[247] Peter J Webster, Greg J Holland, Judith A Curry, and H-R Chang. 2005. Changes in tropical cyclone number, duration, and intensity in a warming

environment. Science 309, 5742 (2005), 1844–1846.

[248] Billy M Williams and Lester A Hoel. 2003. Modeling and forecasting vehicular traffic flow as a seasonal ARIMA process: Theoretical basis and

empirical results. Journal of transportation engineering 129, 6 (2003), 664–672.

[249] Jia Wu, Weiru Zeng, and Fei Yan. 2018. Hierarchical Temporal Memory Method for Time-Series-Based Anomaly Detection. 273 (2018), 535–546.

https://doi.org/10.1016/j.neucom.2017.08.026

[250] P. Wu, J. Liu, and F. Shen. 2020. A Deep One-Class Neural Network for Anomalous Event Detection in Complex Scenes. IEEE Transactions on

Neural Networks and Learning Systems 31, 7 (2020), 2609–2622. https://doi.org/10.1109/TNNLS.2019.2933554

[251] Renjie Wu and Eamonn J. Keogh. 2023. Current Time Series Anomaly Detection Benchmarks are Flawed and are Creating the Illusion of Progress.

IEEE Trans. Knowl. Data Eng. 35, 3 (2023), 2421–2429. https://doi.org/10.1109/TKDE.2021.3112126

[252] Wentai Wu, Ligang He, Weiwei Lin, Yi Su, Yuhua Cui, Carsten Maple, and Stephen Jarvis. 2020. Developing an Unsupervised Real-Time Anomaly

Detection Scheme for Time Series with Multi-Seasonality. arXiv:1908.01146 [cs, eess, stat] http://arxiv.org/abs/1908.01146

[253] Yanshan Xiao, Bo Liu, Longbing Cao, Xindong Wu, Chengqi Zhang, Zhifeng Hao, Fengzhao Yang, and Jie Cao. 2009. Multi-sphere support vector

data description for outliers detection on multi-distribution data. In 2009 IEEE international conference on data mining workshops. IEEE, 82–87.

[254] Haowen Xu, Wenxiao Chen, Nengwen Zhao, Zeyan Li, Jiahao Bu, Zhihan Li, Ying Liu, Youjian Zhao, Dan Pei, Yang Feng, et al. 2018. Unsupervised
Anomaly Detection via Variational Auto-Encoder for Seasonal KPIs in Web Applications. In Proceedings of the International Conference on World
Wide Web (WWW). International World Wide Web Conferences Steering Committee, International World Wide Web Conferences Steering
Committee, 187–196. https://doi.org/10.1145/3178876.3185996

[255] Haowen Xu, Wenxiao Chen, Nengwen Zhao, Zeyan Li, Jiahao Bu, Zhihan Li, Ying Liu, Youjian Zhao, Dan Pei, Yang Feng, et al. 2018. Unsupervised
anomaly detection via variational auto-encoder for seasonal kpis in web applications. In Proceedings of the 2018 world wide web conference. 187–196.
[256] Kenji Yamanishi, Jun-ichi Takeuchi, Graham Williams, and Peter Milne. 2004. On-Line Unsupervised Outlier Detection Using Finite Mixtures with

Discounting Learning Algorithms. 8, 3 (2004), 275–300. https://doi.org/10.1023/B:DAMI.0000023676.72185.7c

[257] Chao-Lung Yang and Wei-Ju Liao. 2017. Adjacent Mean Difference (AMD) method for dynamic segmentation in time series anomaly detection. In

2017 IEEE/SICE International Symposium on System Integration (SII). IEEE, 241–246.

[258] Dragomir Yankov, Eamonn Keogh, and Umaa Rebbapragada. 2008. Disk aware discord discovery: Finding unusual time series in terabyte sized

datasets. Knowledge and Information Systems 17 (2008), 241–262.

[259] Dragomir Yankov, Eamonn J. Keogh, and Umaa Rebbapragada. 2007. Disk Aware Discord Discovery: Finding Unusual Time Series in Terabyte

Sized Datasets. In ICDM.

[260] Yuan Yao, Abhishek Sharma, Leana Golubchik, and Ramesh Govindan. 2010. Online Anomaly Detection for Sensor Systems: A Simple and Efficient

Approach. Perform. Eval. 67, 11 (nov 2010), 1059–1075. https://doi.org/10.1016/j.peva.2010.08.018

[261] C.-C.M. Yeh, Y. Zhu, L. Ulanova, N. Begum, Y. Ding, H.A. Dau, D.F. Silva, A. Mueen, and E.J. Keogh. 2016. Matrix Profile I: All Pairs Similarity Joins

for Time Series: A Unifying View That Includes Motifs, Discords and Shapelets. In ICDM.

[262] Chin-Chia Michael Yeh, Yan Zhu, Liudmila Ulanova, Nurjahan Begum, Yifei Ding, Hoang Anh Dau, Diego Furtado Silva, Abdullah Mueen, and
Eamonn Keogh. 2016. Matrix Profile I: All Pairs Similarity Joins for Time Series: A Unifying View That Includes Motifs, Discords and Shapelets. In
Proceedings of the International Conference on Data Mining (ICDM). 1317–1322. https://doi.org/10.1109/ICDM.2016.0179

[263] Yufeng Yu, Yuelong Zhu, Shijin Li, and Dingsheng Wan. 2014. Time Series Outlier Detection Based on Sliding Window Prediction. 2014 (2014),

1–14. https://doi.org/10.1155/2014/879736

Manuscript submitted to ACM

---

<!-- PAGE 51 -->

Dive into Time-Series Anomaly Detection: A Decade Review

51

[264] Chunkai Zhang, Shaocong Li, Hongye Zhang, and Yingyang Chen. 2020. VELC: A New Variational AutoEncoder Based Model for Time Series

Anomaly Detection. arXiv:1907.01702 [cs, stat] http://arxiv.org/abs/1907.01702

[265] Chuxu Zhang, Dongjin Song, Yuncong Chen, Xinyang Feng, Cristian Lumezanu, Wei Cheng, Jingchao Ni, Bo Zong, Haifeng Chen, and Nitesh V.
Chawla. 2019. A Deep Neural Network for Unsupervised Anomaly Detection and Diagnosis in Multivariate Time Series Data. In AAAI, Vol. 33.
1409–1416. https://doi.org/10.1609/aaai.v33i01.33011409

[266] Rui Zhang, Shaoyan Zhang, Sethuraman Muthuraman, and Jianmin Jiang. 2007. One Class Support Vector Machine for Anomaly Detection in the
Communication Network Performance Data. In Proceedings of the Conference on Applied Electromagnetics, Wireless and Optical Communications
(ELECTROSCIENCE) (ELECTROSCIENCE’07). World Scientific and Engineering Academy and Society (WSEAS), 31–37.

[267] Hang Zhao, Yujing Wang, Juanyong Duan, Congrui Huang, Defu Cao, Yunhai Tong, Bixiong Xu, Jing Bai, Jie Tong, and Qi Zhang. 2020. Multivariate

time-series anomaly detection via graph attention network. In ICDM. IEEE, 841–850.

[268] Yan Zhu, Chin-Chia Michael Yeh, Zachary Zimmerman, Kaveh Kamgar, and Eamonn Keogh. 2018. Matrix profile XI: SCRIMP++: time series motif

discovery at interactive speeds. In 2018 IEEE International Conference on Data Mining (ICDM). IEEE, 837–846.

[269] Yan Zhu, Zachary Zimmerman, Nader Shakibay Senobari, Chin-Chia Michael Yeh, Gareth Funning, Abdullah Mueen, Philip Brisk, and Eamonn
Keogh. 2016. Matrix profile ii: Exploiting a novel algorithm and gpus to break the one hundred million barrier for time series motifs and joins. In
2016 IEEE 16th international conference on data mining (ICDM). IEEE, 739–748.

[270] Yan Zhu, Zachary Zimmerman, Nader Shakibay Senobari, Chin-Chia Michael Yeh, Gareth Funning, Abdullah Mueen, Philip Brisk, and Eamonn
Keogh. 2016. Matrix profile ii: Exploiting a novel algorithm and gpus to break the one hundred million barrier for time series motifs and joins. In
2016 IEEE 16th international conference on data mining (ICDM). IEEE, 739–748.

[271] Zachary Zimmerman, Kaveh Kamgar, Nader Shakibay Senobari, Brian Crites, Gareth Funning, Philip Brisk, and Eamonn Keogh. 2019. Matrix
profile XIV: scaling time series motif discovery with GPUs to break a quintillion pairwise comparisons a day and beyond. In Proceedings of the
ACM Symposium on Cloud Computing. 74–86.

[272] Zachary Zimmerman, Nader Shakibay Senobari, Gareth Funning, Evangelos Papalexakis, Samet Oymak, Philip Brisk, and Eamonn Keogh. 2019.
Matrix profile XVIII: time series mining in the face of fast moving streams using a learned approximate matrix profile. In 2019 IEEE International
Conference on Data Mining (ICDM). IEEE, 936–945.

Manuscript submitted to ACM

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

DiveintoTime-SeriesAnomalyDetection:ADecadeReview
PAULBONIOL,Inria,DIENS,PSL,CNRS,France
QINGHUALIU,TheOhioStateUniversity,USA
MINGYIHUANG,TheOhioStateUniversity,USA
THEMISPALPANAS,UniversitéParisCité;IUF,France
JOHNPAPARRIZOS,TheOhioStateUniversity,USA
Recentadvancesindatacollectiontechnology,accompaniedbytheever-risingvolumeandvelocityofstreamingdata,underscorethe
vitalneedfortimeseriesanalytics.Inthisregard,time-seriesanomalydetectionhasbeenanimportantactivity,entailingvarious
applicationsinfieldssuchascybersecurity,financialmarkets,lawenforcement,andhealthcare.Whiletraditionalliteratureon
anomalydetectioniscenteredonstatisticalmeasures,theincreasingnumberofmachinelearningalgorithmsinrecentyearscallfora
structured,generalcharacterizationoftheresearchmethodsfortime-seriesanomalydetection.Thissurveygroupsandsummarizes
anomalydetectionexistingsolutionsunderaprocess-centrictaxonomyinthetimeseriescontext.Inadditiontogivinganoriginal
categorizationofanomalydetectionmethods,wealsoperformameta-analysisoftheliteratureandoutlinegeneraltrendsintime-series
anomalydetectionresearch.
ACMReferenceFormat:
PaulBoniol,QinghuaLiu,MingyiHuang,ThemisPalpanas,andJohnPaparrizos.2024.DiveintoTime-SeriesAnomalyDetection:A
DecadeReview.InProceedingsofMakesuretoenterthecorrectconferencetitlefromyourrightsconfirmationemai(Conferenceacronym
’XX).ACM,NewYork,NY,USA,51pages.https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Awiderangeofcost-effectivesensing,networking,storage,andprocessingsolutionsenablethecollectionofenormous
amountsofmeasurementsovertime[109–111,122,137,138,141,143,179,181,186].Recordingthesemeasurements
resultsinanorderedsequenceofreal-valueddatapointscommonlyreferredtoastimeseries.Moregenericterms,such
asdataseriesordatasequences,havealsobeenusedtorefertocaseswheretheorderingofdatareliesonadimension
otherthantime(e.g.,theangleindatafromastronomy,themassindatafromspectrometry,orthepositionindata
frombiology)[176].Analyticaltasksovertimeseriesdataarenecessaryvirtuallyineveryscientificdisciplineand
theircorrespondingindustries[14,61,62,78,161,182,190–192,201],includinginastronomy[4,102,245],biology
[11–13,64],economics[36,74,148,155,213,221,240],energysciences[6,9,158],engineering[112,162,203,243,248],
environmentalsciences[77,84,100,101,164,207,247],medicine[57,199,206],neuroscience[21,119],andsocial
sciences[36,160].Theanalysisoftimeserieshasbecomeincreasinglyprevalentforunderstandingamultitudeof
naturalorhuman-madeprocesses[187,188].Unfortunately,inherentcomplexitiesinthedatagenerationofthese
Authors’ContactInformation:PaulBoniol,Inria,DIENS,PSL,CNRS,Paris,France,paul.boniol@inria.fr;QinghuaLiu,TheOhioStateUniversity,
Columbus,USA,liu.11085@osu.edu;MingyiHuang,TheOhioStateUniversity,Columbus,USA,huang.5749@osu.edu;ThemisPalpanas,UniversitéParis
Cité;IUF,Paris,France,themis@mi.parisdescartes.fr;JohnPaparrizos,TheOhioStateUniversity,Columbus,USA,paparrizos.1@osu.edu.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesarenot
madeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitationonthefirstpage.Copyrightsforcomponents
ofthisworkownedbyothersthantheauthor(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,toposton
serversortoredistributetolists,requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ManuscriptsubmittedtoACM
ManuscriptsubmittedtoACM 1
4202
ceD
92
]GL.sc[
1v21502.2142:viXra

2 Paparrizosetal.
processes,combinedwithimperfectionsinthemeasurementsystemsaswellasinteractionswithmaliciousactors,
oftenresultinabnormalphenomena.Suchabnormaleventsappearsubsequentlyinthecollecteddataasanomalies.
ConsideringthatthevolumeoftheproducedtimeserieswillcontinuetoriseduetotheexplosionofInternet-of-Things
(IoT)applications[75,105,151],anabundanceofanomaliesisexpectedintimeseriescollections.
Thedetectionofanomaliesintimeserieshasreceivedampleacademicandindustrialattentionforoversixdecades
[1,27–30,32,39,69,121,142,159,165,175,180,185,235,239].Withthetermanomalieswerefertodatapointsor
groupsofdatapointsthatdonotconformtosomenotionofnormalityoranexpectedbehaviorbasedonpreviously
observeddata[16,45,80,91,107].Intheliterature,alternativetermssuchasoutliers,novelties,exceptions,peculiarities,
aberrations,deviants,ordiscordsoftenappeartodescribetheoccurrencesofsuchrare,unusual,oftenhard-to-explain
anomalouspatterns[2,40,65].Dependingontheapplication,anomaliescanconstitute[2]:(i)noiseorerroneousdata,
whichhindersthedataanalysis;or(ii)actualdataofinterest.Intheformercase,theanomaliesareunwanteddatathat
areremovedorcorrected.Inthelattercase,theanomaliesmayidentifymeaningfulevents,suchasfailuresorchanges
inbehavior,whicharethebasisforsubsequentanalysis.
Regardlessofthepurposeofthetimeseriesandthesemanticmeaningofanomalies,anomalydetectiondescribesthe
processofanalyzingatimeseriesforidentifyingunusualpatterns,whichisachallengingtaskbecausemanytypesof
anomaliesexist.Theyappearindifferentsizesandshapes.AccordingtoFoorthuis[68],researchongeneral-purpose
anomalydetectiondatesbackto1777,whereBernoulli’sworkseemstobethefirstaddressingissuesofacceptingor
rejectingextremecasesofobservations[19].Robusttheoryinthatareawasdevelopedduringthe1800s(e.g.,methodof
leastsquaresin1805[225])[63,76,83,198,230]and1900s[60,85,106,197,212]butitwasnotuntilthe1950swhen
thefirstworksfocusedspecificallyintimeseriesdata[175].In1972,Foxconductedoneofthefirststudiestoexamine
anomalousbehaviorsacrosstimeanddefinedtwotypesofanomalies:(i)ananomalyaffectingasingleobservation;and
(ii)ananomalyaffectinganobservationandsubsequentobservations[69].In1988,Tsayextendedthesedefinitionsinto
fourtypesforunivariatetimeseries[239]andsubsequentlyformultivariatetimeseries[241].Inthesametimeframe,
thefirstfewapproachesappearfordetectinganomaliesintimeseries,withafocusonutilizingstatisticaltestssuchas
theLikelihood-ratiotest[48,242]
Sincethen,alargenumberofworkshaveappearedinthisarea,whichcontinuestoexpandatarapidpace.Additionally,
numeroussurveyshavebeenpublishedtoprovideanoverviewofthecurrentadvancementsinthisfield[22,33,43,46,
47,54,56,86,99].Unfortunately,themajorityofthesurveysfocusongeneral-purposeanomalydetectionmethodsand
onlyaportionofthembrieflyreviewmethodsfortime-seriesanomalydetection.Eventhoughtraditionalanomaly
detectionmethodsmaytreattimeseriesasanyotherhigh-dimensionalvectorandattempttodetectanomalies,ourfocus
isonapproachesthatarespecificallydesignedtoconsidercharacteristicsoftimeseries.Toillustratetheimportanceof
thispoint,inFigure1,wepresentthreeexamplesofanomaliesintimeseriesapplicationswherethetemporalordering
andthecollectiveconsiderationofpointsenablethedetectionofanomalies.Forexample,in1(a),consideringeach
pointinisolationcannotrevealtheunderlyinganomalyindata.
Therefore,time-orderingfeaturesareimportanttobeconsideredintheanomalydetectionpipeline.Dependingon
theresearchcommunity,multiplesolutionshavebeenproposedtotackletheabove-mentionedchallenge.Forexample,
agroupofmethodsproposedintheliteraturewillproposeatransformationstepthatconvertstimeinformationintoa
relevantvectorspaceandthenapplytraditionaloutlierdetectiontechniques.Inaddition,othergroupsofmethodswill
considerdistances(orsimilaritymeasuresdedicatedtotimeseries)toidentifyunusualtimeseriesorsubsequences.
Then,methodsproposedinthedeeplearningcommunitywillbenefitfromspecificarchitecturesthatembedtime
information(suchasrecurrentneuralnetworksorconvolutional-basedapproaches).
ManuscriptsubmittedtoACM

(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engine disks data (c) Data series example: Snippet of spaceshuttlemarottavalve
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk revolution, in red: failed disk revolution) (in blue:normal cycle, in red: anomalous cycle)
DiveintoTime-SeriesAnomalyDetection:ADecadeReview 3
(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engine disks data (c) Data series example: Snippet of spaceshuttlemarottavalve
(a) Timb(elau )se eD:nraiotears mseearxli ehasem aerxptablmee:ap Stlesn,: iiSnpn priepedpt:e pot rofe fam anna t eeullreeecc thtreoraocractrbaderioadtgi)roagmr a(imn (in blu(ine(b :b) nl uDoear:tmua ssauealr lih edesi saekrx rtaebmveopalluett:s iS,o nnini,p iprnee rtde od:f:p sfraimeilmeudlaa dtteiusdkr eerenhvgoienlauert ditoibsnke)sa dt)a ta (c) D(aint ab slueeri:enso erxmamal pclyec:l eS,n iinp preedt :o af nsopmacaelosuhsu tctyleclem)arottavalve
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk revolution, in red: failed disk revolution) (in blue:normal cycle, in red: anomalous cycle)
Premature Anomalous
heartbeat energizing
phase
Unusual disk
revolution
(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engineT idmiseks idnadtea x (c) Data series example: Snippet of spaceshuttlemaroTttiamvea lvinedex
b(alu) e D:antoar smearile hse eaxratbmepaltes:, Sinn irpepde: tp oref mana teulerect hroecaartrbdeioagtr)am (in (b) T(imi(nb )eb l Duseaet:raui esseusraeile xdsa iesmkx arpmelvepo:lle uS:t nSioninpip,p pinee ttr eoodff :s faiam islueilmda tdueidslak e trneegvdioneleu ntdigoisinkn)se d adtias ks(in blu(ce) : Du(aisntau b asleulredie:isns koerxrmaemavlpo clleyuc: tlSeino, iinpnp, reientd o:r fea sndpo:amcfaeailsloehuudst ctdlyeicslmke)arreovttoaluvatlivoen)
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk Prerevmoalututrieo n, in red: failed disk revolution) (in blue:normal cycle, in red: anomalous cycle) Anomalous
heartbeat energizing
Premature phAansoemalous
heartbeat energizing
phase
Unusual disk
revolution
Unusual disk
revolution
(a) Data series example: Snippet of an electrocardiogram (in (b) Data series example: Snippet of simulated engine disks data (c) Data series example: Snippet of spaceshuttlemaTroimttaev ianlvdeex Time index
blue:normal heartbeats, in red: premature heartbeat) (in blue:usual disk revolution, in red: failed disk revolution) (c) Tim(ine bsleueri:ensoremxaalm cypcllee,: iSnn reipdp: aentoomfa alo sups acycceles)huttlemarottavalve(in blue:normal cycle, in red:anomalouscycle)
Premature Anomalous
heartbeat energizing
P
h
r
e
e
a
m
rt
a
b
t
e
u
a
r
t
e phA ean nso eem
rg
a
iz
l
i
o
n
u
g
s
phase
Unusual disk
revolution
Unusual disk
revolution
Time index Time index
Premature AnomaloFuisg .1. Examplesofdifferenttimeseriesapplicationsandtypesofanomalies.
heartbeat energizing
phase
Unusual disk Unfortunately,theseareasremainmostlydisconnected,usingdifferentdatasets,baselines,andevaluationmeasures.
revolution
Newalgorithmsareevaluatedonlyagainstnon-representativesubsetsofapproachesanditisvirtuallyimpossible
tofindthebeststate-of-the-artapproachforaconcreteusecase.Toremedythisissue,thissurveypresentsanovel,
comprehensive,process-centrictaxonomyforthemultipledetectionmethodsineachcategory.Wecollectedacompre-
hensiverangeofalgorithmsintheliteratureandgroupedthemintofamiliesofalgorithmswithsimilarapproaches.In
addition,toidentifyresearchtrends,wealsoprovidestatisticsonthetypeandareaofproposedapproachesovertime.
Then,wealsolistexistingbenchmarksthatcanbeusedasacommongroundonwhichnewproposedmethods
(regardlessofthecommunity)shouldbeevaluated.Finally,weenumerateexistingevaluationmeasuresusuallyusedto
evaluateanomalydetectionmethodswhilediscussingtheirlimitationandbenefitswhenappliedtothespecificcaseof
timeseries.
2 Time-SeriesAnomalyDetectionOverview
Inthissection,wediscusstheproblemformulationfortime-seriesanomalydetectionalgorithmsandmotivateour
process-centrictaxonomy.
ManuscriptsubmittedtoACM

4 Paparrizosetal.
2.1 OntheDefinitionofAnomaliesinTimeSeries
Attestingtothechallengingnatureoftheproblemathand,weobservethattheredoesnotexistasingle,universal,
precisedefinitionofanomaliesoroutliers.Traditionally,anomaliesareobservationsthatdeviateconsiderablyfromthe
majorityofothersamplesinadistribution.Theanomalouspointsraisesuspicionsthatamechanismdifferentfrom
thoseoftheotherdatageneratedthespecificobservation.Suchamechanismusuallyrepresentseitheranerroneous
datameasurementprocedureoranunusualevent.
Incasesoferrorsinthedatameasurementprocedure,theanomalousobservationsaremarkedas“noise"–unwanted
datathatarenotattractivetotheanalystandshouldberemovedinthedatacleaningprocess.Manypiecesofliterature
havebeendedicatedtothistypeofproblem,particularlyinthesensorsetting,wherethemainobjectiveistoeliminate
transmissionerrorandrenderaccuratepredictions.Intime-seriesanomalydetection,however,recentliteraturebegins
tocenterondetectinganomalousevents,whichindicate“novelty"–unusualbutinterestingphenomenathatoriginate
fromaninherentvariabilityinthedomainofthedata.Anaturalexampleofthistypeofproblemisfrauddetectionfor
creditinformation,wheretheprincipalaimistodetectandanalyzethefrauditself.
Thedetectionofthesetwotypesofanomalies(anomaliesandoutlierscanbeusedinterchangeably)canbeachieved
viaexpertknowledge.Byknowingexactlyhowthesystemworks,theexpertscansettheparametertofitadistribution
ofvaluesthatrepresentthehealthyfunctioningstate.Anomaliesarethendetectedbymarkingpointsofmorethan
threestandarddeviationsawayfromthemeanofdatadistributionestimatedbytheexperts.Tovalidatethedetection
process,wealsoneedtoperformextensiveteststotestthedistribution(anditsparameters)againstthedataset.
Nevertheless,inseveralreal-worldproblems,wedonotknowpreciselythedatadistributionthathasgeneratedaset
ofpoints(andallthedifferentartifactsthatplayedarole).Besides,thedatadistributionsthatweencounterinpractice,
arealmostalwaysrathercomplexandveryhardtoidentifyorapproximateeffectively.Consequently,definingand
identifyinganomaliesusingtheirdistancefromameanvaluedefinedbyexpertsissometimeshardlypractical.
Despitethechallengeofestimatingdistributionparametersbyexperts,recentdevelopmentsincomputationalpower
haveliberatedusfromanalternativeapproachtoanalyzingdatadistributionfromthedataitself.Usingavarietyof
learningmethods,researchersmayapplycomputeralgorithmstoanalyzerawdata,estimateafairdistribution,and
detectanomalieswithoutexpertknowledge.Eventhoughbeingstronglydependentonthequalityandthecontextof
thedatasets,thesemethodsseemtoshowstrongresultsinachievingrelativelycomplextasks.Inthispaper,wefocus
onthistypeofmethod.
2.2 TypesofAnomaliesinTimeSeries
Thereisafurthercomplicationintime-seriesanomalydetection.Duetothetemporalityofthedata,anomaliescan
occurintheformofasinglevalueorcollectivelyintheformofsub-sequences.Inthespecificcontextofpoint,weare
interestedinfindingpointsthatarefarfromtheusualdistributionofvaluesthatcorrespondtohealthystates.Inthe
specificcontextofsequences,weareinterestedinidentifyinganomaloussub-sequences,whichareusuallynotoutliers
butexhibitrareand,hence,anomalouspatterns.Inreal-worldapplications,suchadistinctionbetweenpointsand
sub-sequencesbecomescrucialbecauseeventhoughindividualpointsmightseemnormalagainsttheirneighboring
points,theshapegeneratedbythesequenceofthesepointsmaybeanomalous.
Formally,wedefinethreetypesoftimeseriesanomalies:point,contextual,andcollectiveanomalies.Pointanomalies
refertodatapointsthatdeviateremarkablyfromtherestofthedata.Figure2(a)depictsasynthetictimeserieswitha
pointanomaly:thevalueoftheanomalyisoutsidetheexpectedrangeofnormalvalues.Contextualanomaliesreferto
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 5
𝑃𝑜𝑖𝑛𝑡-𝑏𝑎𝑠𝑒𝑑 𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒-𝑏𝑎𝑠𝑒𝑑
𝑎.1 𝑇𝑖𝑚𝑒 𝑠𝑒𝑟𝑖𝑒𝑠 𝑏.1 𝑇𝑖𝑚𝑒 𝑠𝑒𝑟𝑖𝑒𝑠 𝑐.1 𝑇𝑖𝑚𝑒 𝑠𝑒𝑟𝑖𝑒𝑠
20 𝑃𝑜𝑖𝑛𝑡 𝐶𝑜𝑛𝑡𝑒𝑥𝑡𝑢𝑎𝑙 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝐶𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑣𝑒
𝑎𝑛𝑜𝑚𝑎𝑙𝑦
𝑎𝑛𝑜𝑚𝑎𝑙𝑦
0
0 300 600 900 1200 0 300 600 900 1200 0 300 600 900 1200
𝑎.2 𝐷𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛 𝑏.2 𝑏.3 𝑐.2 𝐷𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑖𝑜𝑛
0 5 10 15 20 0 5 10 15 20 0 5 10 15 20 0 5 10 15 20
𝑎 𝑃𝑜𝑖𝑛𝑡 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝑜𝑢𝑡𝑠𝑖𝑑𝑒 𝑡ℎ𝑒 𝑏 𝐶𝑜𝑛𝑡𝑒𝑥𝑡𝑢𝑎𝑙 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝑜𝑢𝑡𝑠𝑖𝑑𝑒 𝑡ℎ𝑒 𝑙𝑜𝑐𝑎𝑙 𝑐 𝐶𝑜𝑙𝑙𝑒𝑐𝑡𝑖𝑣𝑒 𝑎𝑛𝑜𝑚𝑎𝑙𝑦 𝑖𝑛𝑠𝑖𝑑𝑒 𝑡ℎ𝑒 ℎ𝑒𝑎𝑙𝑡ℎ𝑦
ℎ𝑒𝑎𝑙𝑡ℎ𝑦 𝑟𝑎𝑛𝑔𝑒 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 (𝑑𝑜𝑡𝑡𝑒𝑑 𝑏𝑙𝑎𝑐𝑘 𝑙𝑖𝑛𝑒) ℎ𝑒𝑎𝑙𝑡ℎ𝑦 𝑟𝑎𝑛𝑔𝑒 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 (𝑑𝑜𝑡𝑡𝑒𝑑 𝑏𝑙𝑎𝑐𝑘 𝑏𝑜𝑥) 𝑟𝑎𝑛𝑔𝑒 𝑜𝑓 𝑣𝑎𝑙𝑢𝑒𝑠 (𝑑𝑜𝑡𝑡𝑒𝑑 𝑏𝑙𝑎𝑐𝑘 𝑙𝑖𝑛𝑒)
𝑠𝑒𝑢𝑙𝑎𝑉
𝑦𝑐𝑛𝑒𝑢𝑞𝑒𝑟𝐹
Fig.2. Syntheticillustrationofthethreetimeseriesanomalytypes:(a)point;(b)contextual;and(c)collectiveanomalies.
datapointswithintheexpectedrangeofthedistribution(incontrasttopointanomalies)butdeviatefromtheexpected
datadistribution,givenaspecificcontext(e.g.,awindow).Figure2(b)illustratesatimeserieswithacontextualanomaly:
theanomalyiswithintheusualrangeofvalues(leftdistributionplotofFigure2(b))butoutsidethenormalrange
ofvaluesforalocalwindow(rightdistributionplotofFigure2(b)).Collectiveanomaliesrefertosequencesofpoints
thatdonotrepeatatypical(previouslyobserved)pattern.Figure2(c)depictsasyntheticcollectiveanomaly.Thefirst
twocategories,namely,pointandcontextualanomalies,arereferredtoaspoint-basedanomalies.whereas,collective
anomaliesarereferredtoassequence-basedanomalies.
Asanadditionalnote,thereisanothercaseofsub-sequenceanomalydetectionreferredtoaswhole-sequence
detection,relativetothepointdetection.Inthiscase,theperiodofthesub-sequenceisthatoftheentiretimeseries,
andtheentiretimeseriesisevaluatedforanomalydetectionasawhole.Thisistypicallythecaseinthesensorcleaning
environmentwhereresearchersareinterestedinfindinganabnormalsensoramongallthefunctioningsensors.
2.3 UnivariateversusMultivariate
Anothercharacteristicoftime-seriesanomalydetectionalgorithmscomesfromthedimensionalityofthedata.Univariate
timeseriesconsistsofanorderedsequenceofrealvaluesonasingledimension,andtheanomaliesaredetectedbased
ononesinglefeature.Inthiscase,asillustratedinFigure3(b.1),asubsequencecanberepresentedasavector.Onthe
otherhand,Multivariatetimeseriesiseitherasetoforderedsequencesofrealvalues(witheachorderedsequence
havingthesamelength)oranorderedsequenceofvectorscomposedofrealvalues.Inthisspecificcase,asillustrated
inFigure3(b.2),asubsequenceisamatrixinwhicheachlinecorrespondstoasubsequenceofonesingledimension.
Instancesofanomaliesaredetectedaccordingtomultiplefeatures,wherevaluesofonefeature,whensingledout,may
looknormaldespitetheabnormalityofthesequenceasawhole.
2.4 Unsupervised,Semi-supervisedversusSupervised
Thistaskcanbedividedintothreedistinctcases:(i)expertsdonothaveinformationonwhatanomaliestodetect;
(ii)expertsonlyhaveinformationontheexpectednormalbehaviors;(iii)expertshavepreciseexamplesofwhich
ManuscriptsubmittedtoACM

| 6   |     |     |     |     |     | Paparrizosetal. |
| --- | --- | --- | --- | --- | --- | --------------- |
𝑼𝒏𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑎𝑛𝑑	𝑴𝒖𝒍𝒕𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑝𝑜𝑖𝑛𝑡	𝑎𝑛𝑜𝑚𝑎𝑙𝑖𝑒𝑠 !"#$%&#%'()*+,-.'#$%&#%'(/01*2)*03)45 𝑼𝒏𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑎𝑛𝑑	𝑴𝒖𝒍𝒕𝒊𝒗𝒂𝒓𝒊𝒂𝒕𝒆	𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒	𝑎𝑛𝑜𝑚𝑎𝑙𝑖𝑒𝑠 !"#$%&#%'()*+,-.'#$%&#%'(67897*:7)*03)45
𝑇(")
| ,(")       | 𝑇(") |              | ,(")       |        |     |              |
| ---------- | ---- | ------------ | ---------- | ------ | --- | ------------ |
| ,($)       | 𝑇($) |              | ,($)       |        |     |              |
| !"#$%&#%'( | 𝑇    | -*)'#$%&#%'( | !"#$%&#%'( | 𝑇 𝑇($) |     | -*)'#$%&#%'( |
$%)*(+*')#(& $%)*(+*')#(& /*6/(=*("7(+*')#(& /*6/(=*("7(+*')#(&
|       | …       |      |        | …    |     |      |
| ----- | ------- | ---- | ------ | ---- | --- | ---- |
| ,𝑇(%) | 𝑇(%)    |      | ,(%) 𝑇 | 𝑇(%) |     |      |
| 0 300 | 600 900 | 1200 | 0 300  | 600  | 900 | 1200 |
|       | 200     |      |        |      | 200 |      |
|       | 150     |      |        |      | 150 |      |
|       | 100     |      |        |      | 100 |      |
|       | 50      |      |        |      | 50  |      |
|       | 0       |      |        |      | 0   |      |
0 50 100 150 200 0 50 100 150 200 0 50 100 150 200 0 50 100 150 200
| %.1 !"#$%&#%'(7%/( | %.2 -*)'#$%&#%'(7%/( |     | 6.1 !"#$%&#%'(7%/( |     | 6.2 -*)'#$%&#%'(7%/( |     |
| ------------------ | -------------------- | --- | ------------------ | --- | -------------------- | --- |
6 >*6/(=*("7(+*')#(&#"/#0('ℎ(ℎ(%)'ℎ2&%"3(+4$%)*(/
% .+#"'+*')#(&+*'/#0('ℎ(ℎ(%)'ℎ2&%"3(+4$%)*(/
|     | (0+''(06)%78)#"() |     |     | (0+''(06)%78)#"() |     |     |
| --- | ----------------- | --- | --- | ----------------- | --- | --- |
Fig.3. Syntheticexamplecomparinganomaliesinunivariateandmultivariatetimeseriesfor(a)apointoutlierand(b)asequence
outlier.
anomaliestheyhavetodetect(andhaveacollectionofknownanomalies).Thisgivesrisetothedistinctionamong(i)
unsupervised,(ii)semi-supervised,and(iii)supervisedmethods.
Unsupervised:Incase(i),onecandecidetoadoptafullyunsupervisedmethod.Thesemethodshavethebenefitof
workingwithouttheneedforalargecollectionofknownanomaliesandcandetectunknownabnormalbehavior
automatically.Suchmethodscanbeusedeithertomonitorthehealthstateortominethehistoricaltimeseriesofa
system(tobuildacollectionofabnormalbehaviorsthatcanthenbeusedonasupervisedframework).
Semi-supervised:Incase(ii),methodscanlearntodetectanomaliesbasedonannotatedexamplesofnormalsequences
providedbytheexperts.Thisistheclassicalcaseformostoftheanomalydetectionmethodsintheliterature.One
shouldnotethatthiscategoryisoftendefinedasUnsupervised.However,weconsideritunfairtogroupsuchmethods
withthecategorymentionedabove,knowingthattheyrequiremuchmorepriorknowledgethanthepreviousone.
Supervised:Whileincase(i)and(ii)anomalieswereconsideredunknown,incase(iii),weconsiderthattheexperts
knowprecisely,whattypeofpattern(s)theywanttodetect,andthatacollectionoftimeserieswithlabeledanomalies
isavailable.Inthatcase,wehaveadatabaseofanomaliesatourdisposal.Inasupervisedsetting,onemaybeinterested
inpredictingtheabnormalsub-sequencebyitspriorsub-sequences.Suchsub-sequencescanbecalledprecursorsof
anomalies.
2.5 AnomalyDetectionPipelines
Uponsummarizingthevariousdifferentalgorithmsondifferentdomains,werealizedacommonpipelinefortime-series
anomalydetectionalgorithms.Thepipelineconsistsoffourparts:datapre-processing,detectionmethod,scoring,and
post-processing.Figure4illustratestheprocess.Thedecompositionofthegeneralanomalydetectionprocessintosmall
stepsofapipelineisbeneficialforcomparingdifferentalgorithmsonvariousdimensions.Understandingofalgorithms’
functioninthepre-processingstephelpsinterpretitstreatmentoftimeseriesdataspecifically.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 7
Anomalies
Time Series
Pre-Processing
0 2000 4000
Anomaly Detection
Model Post-Processing
Scoring
Anomaly score
0 2000 4000 6000 8000
Fig.4. Timeseriesanomalydetectionpipeline.
Thedataprocessingsteprepresentshowtheanomalydetectionmethodprocessesthetimeseriesdataattheinitialstep.
Wehavenoticedalltheanomalydetectionmodelsaresomehowbasedonawindowedapproachinitially-converting
thetimeseriesdataintoamatrixwithrowsofslidingwindowslicesoftheoriginaltimeseries.Thepre-processing
stepconsistsoftheadditionalprocessingprocedurebesidesthewindowtransformation,whichvariesfromstatistical
featureextractiontofittingamachinelearningmodelandbuildinganeuralnetwork.
Afterthedataisprocessed,differentdetectionmethodsareimplementedonthedataset,whichmightbesimply
calculatingdistancesamongtheprocessedsub-sequences,fittingaclassificationhyper-plane,orusingtheprocessed
modeltogeneratenewsub-sequencesandcomparingthemwithoriginalsub-sequences.Thedetectionmethodsare
usuallytraditionaloutlierdetectionmethodsforvectordata.
Then,duringthescoringprocess,theresultsderivedinthedetectionmethodswillbeconvertedtoananomalyscore
thatassessestheabnormalityofindividualsub-sequencesbyarealvalue(suchasaprobabilityofbeingananomaly).
Thescoreswillbefurtherusedtoinferthescoreoftheindividualpoint.Theresultingscoreisatimeseriesofthesame
lengthastheinitialtimeseries.
Lastly,duringthepost-processingstep,theanomalyscoretimeseriesisprocessedtoextracttheanomalouspointsor
intervals.Usually,athresholdvaluewillbedetermined,wherethepointswithanomalyscoressurpassingthethreshold
willbemarkedastheanomaly.
Thiscategorizationoftime-seriesanomalydetectionpipelinesinspiresourprocess-centrictaxonomyofthedetection
methods,whichwillbediscussedthoroughlyinthenextsection.
3 AnomalyDetectionTaxonomy
Inthissection,wedescribeourproposedprocess-centrictaxonomyofthedetectionmethods.Wedividemethods
intothreecategories:(i)distance-based,(ii)density-based,and(iii)prediction-based.Thefirstfamilycontainsmethods
thatfocusontheanalysisofsub-sequencesforthepurposeofdetectinganomaliesintimeseries,mainlybyutilizing
distancestoagivenmodel.Second,insteadofmeasuringnearest-neighbordistances,density-basedmethodsfocuson
detectinggloballynormalorisolatedbehaviors.Third,prediction-basedmethodsaimtotrainamodel(onanomaly-free
timeseriesorwithveryfewanomalies)toreconstructthenormaldataorpredictthefutureexpectednormalpoints.
ManuscriptsubmittedtoACM

8 Paparrizosetal.
Time series anomaly detection methods
Distance-based Density-based Prediction-based
Proximity- Clustering- Discord- Distribution- Graph- Tree- Encoding- Forecasting- Reconstruction
based based based based based based based based -based
A BC A B C A D E A BC
ℬ A → BC
A → DE
…
Fig.5. Process-centricanomalydetectiontaxonomy.
Inthefollowingsections,webreakdowneachcategoryintoprocess-centricsubcategories.Figure5illustratesour
proposedprocess-centrictaxonomy.
Notethatthesecond-levelcategorizationisnotmutuallyexclusive.Amodelmightcompressthetimeseriesdata
whileadoptingadiscord-basedidentificationstrategy.Inthiscase,themodelfallswithintwodifferentsub-categories.
Inthetableofmethods,onlyoneofthesecond-levelwillbelistedtogiveaclearerrepresentation.
3.0.1 Distance-based. Asitsnamesuggests,thedistance-basedmethoddetectsanomaliespurelyfromtherawtime
seriesusingdistancemeasures.Giventwosequences(orunivariatetimeseries),𝐴∈Rℓ and𝐵 ∈Rℓ ,ofthesamelength,
ℓ,wedefinethedistancebetween𝐴and𝐵 as𝑑(𝐴,𝐵) ∈ R,suchas𝑑(𝐴,𝐵) = 0when𝐴and𝐵 arethesame.There
existdifferentdefinitionsof𝑑 intheliterature.TheclassicaldistancewidelyusedistheEuclideandistanceorthe
Z-normalizedEuclideandistance(Euclideandistancewithsequencesofmeanvaluesequalto0andstandarddeviations
equalto1).Then,DynamicTimeWarping(DTW)iscommonlyusedtocopewithmisalignmentissues.Overall,the
distance-basedalgorithmsmerelytreatthenumericalvalueoftimeseriesasitis,withoutfurthermodificationssuchas
removingseasonalityorintroducinganewstructurebuiltonthedata.Withinthedistance-basedmodels,therecome
threesecond-levelcategories:proximity-based,clustering-based,anddiscord-basedmodels.
(1) Theproximity-basedmodelmeasuresproximitybycalculatingthedistanceofagivensub-sequencetoits
closeneighborhood.Theisolationofasub-sequencewithregardstoitsclosestneighborsisthemaincriterionto
considerifthissub-sequenceisananomalyornot.Thisnotionofisolationwithregardtoagivenneighborhood
hasbeenproposedfornon-timeseriesdata.Thus,themethodscontainedinthiscategoryhavebeenintroduced
forthegeneralcaseofmulti-dimensionaloutlierdetection.Inourspecificcase,thesub-sequenceofatime
seriescanbeconsideredamulti-dimensionalpointwiththenumberofdimensionsequaltothelengthofthe
sub-sequence.
(2) Theclustering-basedmodelinfersanomaliesfromaclusterpartitionofthetimeseriessub-sequences.In
practice,theanomalyscoreiscalculatedbythenon-membershipofasub-sequenceofeachoftheclusterslearned
bythemodel.Otherconsiderations,suchasclusterdistanceandclustercapacity,canalsobeconsidered.The
clusteringissueisrelatedtotheanomalydetectionprobleminthatpointsmayeitherbelongtoaclusteror
bedeemedanomalies.Inpractice,thefactthatasub-sequencebelongsornottoaclusterisassessedbythe
computationofthedistancebetweenthissub-sequenceandtheclustercentroidormedoid.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 9
(3) Thediscord-basedmodeltriestoidentifyefficientlyspecifictypesofsub-sequencesinthetimeseriesnamed
discord.Formally,asub-sequence𝐴(oragivenlengthℓ)isadiscord,ifthedistancebetweenitsnearestneighbor
isthelargestamongallthenearestneighbors’distancescomputedbetweensub-sequencesoflengthℓ inthe
timeseries.Overall,similarlytoproximity-basedmethods,Theisolationofasub-sequencewithregardsto
itsclosestneighborsisthemaincriteriontoconsiderifthissub-sequenceisananomalyornot.However,on
contrarytoproximity-basedmethods,discord-basedmethodshavebeenintroducedforthespecificcaseof
anomalydetectionintimeseries.Thus,assuchmethodsintroducedefficientprocessesfortimeseriesdistance
computationspecifically,wegroupthemintoonedifferentsub-category.
3.0.2 Density-based. Thedensity-baseddoesnottreatthetimeseriesassimplenumericalvaluesbutimbuesthem
withmorecomplexarchitecture.Thedensity-basedmethodprocessestimeseriesdataontopofarepresentationof
thetimeseriesthataimstomeasurethedensityofthepointsorsub-sequencespace.Suchrepresentationvariesfrom
graphs,trees,andhistogramstoagrammarinductionrule.Thedensity-basedmodelshavefoursecond-levelcategories:
distribution-based,graph-based,tree-based,andencoding-based.
(1) Thedistribution-basedanomalydetectionapproachisbuildingadistributionfromstatisticalfeaturesofthe
pointsorsub-sequencesofthetimeseries.Byexaminingthedistributionsoffeaturesofthenormalsub-sequences,
ittriestorecoverrelevantstatisticalmodelsandthenusesthemtoinfertheabnormalityofthedata.
(2) Agraph-basedmethodrepresentsthetimeseriesandthecorrespondingsub-sequencesasagraph.Thenodes
andedgesrepresentthedifferenttypesofsub-sequences(orrepresentativefeatures)andtheirevolutionintime.
Forinstance,thenodescanbesetsofsimilarsub-sequences(usingapredefineddistancemeasure),andtheedge
weightscanbethenumberoftimesasub-sequenceofagivennodehasbeenfollowedbyasub-sequenceof
anothernode.Thedetectionofanomaliesisthenachievedusingcharacteristicsofthegraph,suchasthenode
andedgeweights,butalsothedegreeofthenodes.
(3) Atree-basedapproachaimstodividethepointorsub-sequenceofatimeseriesusingtrees.Forinstance,such
treescanbeusedtosplitdifferentpointsorsub-sequencesbasedontheirsimilarity.Thedetectionofanomalies
isthenbasedonthestatisticsandcharacteristicsofthetree,suchasitsdepth.
(4) Aencoding-basedanomalydetectionmodelcompressesorrepresentsthetimeseriesintodifferentformsof
symbols.Theencoding-basedmodelsuggeststhatatimeseriescanbeinterpretedasasequenceofcontext-free,
discretesymbolsorstates.Forinstance,anomaliescanbedetectedbyusinggrammarruleswiththesymbols
extractedfromthetimeseries.Itshouldbenotedthatanencoding-basedmodelisnotexclusivetoitself;itmay
evenbebasedonagraph-basedortree-basedmodel.
3.0.3 Prediction-based. Prediction-based methods aim to detect anomalies by predicting the expected normal
behaviorsbasedonatrainingsetoftimeseriesorsub-sequences(containinganomaliesornot).Forinstance,some
methodswillbetrainedtopredictthenextvalueorsub-sequencebasedonthepreviousone.Thepredictionisthen
post-processedtodetectabnormalpointsorsub-sequences.Then,thepredictionerrorisusedasananomalyscore.
Theunderlyingassumptionofprediction-basedmethodsisthatnormaldataareeasiertopredict,whileanomalies
areunexpected,leadingtohigherpredictionerrors.Suchassumptionsarevalidwhenthetrainingsetcontainsnoor
fewtimeserieswithanomalies.Therefore,prediction-basedmethodsareusuallymoreoptimalundersemi-supervised
settings.
ManuscriptsubmittedtoACM

10 Paparrizosetal.
Time Series T ∈ ℝ! T T
!"#,ℓ !,ℓ
𝑇
Model &,ℓ
Predictor
Builder
Forecasting First Data First
𝑇%
&,ℓ Detection
Distance
Update model Model
𝑦
Raw Score 𝑌 ∈ ℝ!"ℓ$% & ℓ
Scoring
e.g. padding with 0
Final Score 𝑌 ∈ ℝ!
Fig.6. Thescoringprocess.
(1) Theforecasting-basedmethodisamodelthat,foragivenindexortimestamp,takesasinputpointsorsub-
sequencesbeforethisgiventimestampandpredictsitscorrespondingvalueorsub-sequence.Inotherwords,
suchmethodsusepastvaluesasinputtopredictthefollowingone.Theforecastingerror(thedifferencebetween
thepredictedandtherealvalue)isusedasananomalyscore.Indeed,suchforecastingerrorisrepresentativeof
theexpectationofthecurrentvaluebasedonthepreviouspointsorsub-sequences.Thelargertheerror,themore
unexpectedthevalue,andthus,potentiallyabnormal.Forecasting-basedapproachesassumethatthetraining
data(pastvaluesorsub-sequences)isalmostanomaly-free.Thus,suchmethodsaremostlysemi-supervised.
(2) Thereconstruction-basedmethodcorrespondstoamodelthatcompressestheinputtimeseries(orsub-
sequence)intoalatentspace(smallerthantheinputsize)andistrainedtoreconstructtheinputtimeseries
fromthelatentspace.Thedifferencebetweentheinputtimeseriesandthereconstructedone(namedthe
reconstructionerror)isusedasananomalyscore.Asforforecasting-basedmethods,thelargertheerror,the
moreunexpectedthevalue,andthus,potentiallyabnormal.Moreover,asthereconstructionerrorislikelytobe
smallforthetimeseriesusedtotrainthemodel,suchreconstructionmethodsareoptimalinsemi-supervised
settings.
3.1 ScoringProcess
Assummarizedinthepipeline,anomalydetectionalgorithmsdistinguishoutliersbyinferenceonthe“anomalyscores"
ofeachtemporaldatapoint.Theanomaliesaremarkedbypointswhosescoresexceedthethresholdvalue.Duetothe
specialfeaturesoftimeseriesdata,afurthergeneralcategorizationcanbeprovidedbasedonthealgorithm’sstrategy
ofscoringtheanomalies.Weincludethisgeneralizationasacomplementtoourtaxonomy.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 11
*+,(803)
0 1250 2500 3750 5000
!= # − #( )
$,& $,&
0 1250 2500 3750 5000
Fig.7. Resultusing|Z|=16foraautoencoderEncoder(𝐶𝑜𝑛𝑣(64,3)-𝑅𝑒𝑙𝑢()-𝐷𝑒𝑛𝑠𝑒()-𝑇𝑎𝑛ℎ()),Decoder(𝐷𝑒𝐶𝑜𝑛𝑣(64,3)-𝑅𝑒𝑙𝑢()-
𝐷𝑒𝑛𝑠𝑒()-𝑇𝑎𝑛ℎ()).Topplot:Inputtimeseriessnippet.Bottomplot:𝑆(usingmeansquareerror)forallthesub-sequencesoflength80.
Aforecasting-firstapproachfirstinfersthevaluesofinterestedtimeseries,withoutknowingtheactualvaluesofthe
dataset,andthendeterminesifthecomingdatapointsareanomalies(basedontheirdistancetotheinferredvalues).
Thisgivespossibilitiesforstreamingdataanomalydetection.Adata-firstapproach,ontheotherhand,readsthedata
firsttoupdatethemodel.Then,theentiretrainingdatasampleswillbeusedtocomparewiththearrivingdataviathe
detectionmodel.Figure6givesanillustrationofthetwo.
Justlikeforecasting-firstalgorithms,data-firstalgorithmsmayalsobecapableofgeneratingnewsub-sequencesto
comparewithoriginalsequences.Figure7givessuchanexample,wheretheautoencoderreconstructsanestimated
sequence𝑇′ tocalculatetheerror𝑆ontheECGdata.Althoughitbehaveslikeaforecasting-firstmethodbytryingto
𝑖,𝑙
“forecast"theoriginalsub-sequences,itistechnicallydata-firstbecauseitrequiresthearrivalofnewdatatomakevalid
comparisons.
4 SurveyOrganization
Inthefollowingsections,wewillpresenttheState-Of-The-Art(SOTA)inthethreemajorcategoriesandelaborateon
thespecificvariantsoftheSOTAproposedinthepastliterature.Figure8illustratesourdetailedproposedtaxonomy
listingallthemethodsdiscussedinthispaper.Notethat,inFigure8,thenamesofthemethods(thefirstletter)are
positionedonthey-axisbasedontheirpublicationdate.Eventhoughsomeconceptsmightbeanteriortothedate
indicatedinFigure8(forinstancetheconceptofk-meanswasintroducedin1967),thedatescorrespondtothefirst
paperdiscussingtheconceptsappliedtoanomalydetection.Therestofthispaperisorganizedasfollows:
• Wefirstpresentdistance-basedmethodsthatperformanomalydetectionusingdistancecomputationand
comparisonsonpointsorsub-sequencesofthetimeseries.
• Nextweenumeratethedensity-basedmethods.Theseapproachesprocesstimeseriesdataontopofarepresen-
tationthataimstomeasurethedensityofthepointsorsub-sequenceswithinthetimeseriesspace.
• Wefurnishwithtwogroupsofprediction-basedmethodsthataimtopredicttheexpectednormalbehaviors
fromatrainingsetoftimeseries.Thesetwogroupsareforecasting-basedmethods(thatusetheforecastingerror
asanomalyscore)andreconstruction-basedmethods(thataretrainedtoreconstructaninputtimeseriesand
usethereconstructionerrorasanomalyscore).
• Wewillalsoincludeatableofallthemethodsineachsectiontorevealtheirothercharacteristics(suchasthe
requirementforsupervision,thecapabilityofhandlingstreamingdata,etc)ascomplementstoourtaxonomy.
ManuscriptsubmittedtoACM

12 Paparrizosetal.
Anomaly Detection Methods
Distance-based Density-based Prediction-based
Proximity- Clustering- Forecasting-
based based based
Distribution-
1980 based
1985
1990
Encoding-
based
1995 Discord-
based
Graph- Reconstruction-
2000 based based
2005 Tree- based
2010
2015
2020
2023
E HSFD DILO
LOF
KnorrSeq2 F F
SSA
CO ILO CI
KNN
LO CBLOF
DBSCAN
MCOD
DBStream
K-Means
Sequence
Miner
Hybrid-KMeans NormA NorM
TARZAN HOT SAX
MP
DAD
SCRI
Matrix Profile
SAND
PIAMD PSTAM STOM
P SCAM MERLIN MAD
+ MERLIN+ DAMP
MCD
Fast-MCD
MC-MCD TwoFinger
Series2Graph DADS
SurpriseEncode
IForest
Eros-SVMs Hybrid-IForest IF-LOF Extended-IForest
OCSVM
MS-SVDD
NetworkSVM
AOSVM
DeepSVM
HMAD
OC-KFD
S-SVM
MGDD MedianMethod SmartSifter
HBOS
H-ESD SH-ESD SH-ESD+ ConInd COPOD
GrammarViz
GeckoFSM
EM-HMM
PST
Lase E r D -D B B N N KDE-EDBN
NoveltySVR
Ensemble-GI
ES DES TES
ARIMA
PCA
deepPCA RobustPCA
ESN
emiT
Torsk HealthESN
MoteESN CoalESN
LSTM-AD PCI
OceanWNN MTAD-GAT AD-LTI
deepLSTM
Telemanon DeepAnT RePAD MultiHTM RADM
AE
DeepNAP
STORN Enc-Dec-AD
LSTM-VAE DONUT BAGEL OmniAnomaly MSCRED VELC CEA
GAN
NumentaHTM MAD-GAN VAR-GAN TAnoGAN LAMP DeepKMean
Fig.8. IllustrationofAnomalyDetectionTaxonomyforallmethods.
• Afterbrieflydescribingallthemethods,wewilldiscussameta-analysisofthetime-seriesanomalydetection
communitybyexaminingtheevolutionandthetrendsofeachcategory(distance-based,density-based,prediction-
based).Wewillalsohaveacloserlookattheevolutionintimeofproposedmethodsthataresemi-supervised,
unsupervised,andabletohandlemultivariatetimeseries.
• Wewillconcludethissurveywiththeevaluationofsuchmethods.Wewillfirstenumerateexistingbenchmarks
proposedintheliterature,aswellasdifferentevaluationmeasuresandtheirlimitationswhenappliedtotime-
seriesanomalydetection.
5 TimeSeriesNotations
Wenowintroducesomeformalnotationsrelatedtotimeseries.Wedefineatimeseries𝑇 ∈ R𝑛 asasequenceof
real-valuednumbers𝑇
𝑖
∈R[𝑇
0
,𝑇
2
,...,𝑇
𝑛−1
],where𝑛=|𝑇|isthelengthof𝑇,and𝑇
𝑖
isthe𝑖𝑡ℎ pointof𝑇.
Amultivariate,or𝐷-dimensionaltimeseriesT∈R(𝐷,𝑛) isasetof𝐷 univariatetimeseriesoflength𝑛.Wenote
T = [𝑇(0),...,𝑇(𝐷−1)] and for 𝑗 ∈ [0,𝐷 −1], we note the univariate time series𝑇(𝑗) = [𝑇(𝑗),𝑇(𝑗),...,𝑇(𝑗) ]. A
0 1 𝑛−1
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 13
subsequence𝑇 ( 𝑗) ∈Rℓ ofthedimension𝑇(𝑗)ofthemultivariatetimeseries𝑇 isasubsetofcontiguousvaluesfrom𝑇(𝑗)
𝑖 ,ℓ
oflengthℓ(usuallyℓ ≪𝑛)startingatposition𝑖;formally,𝑇 ( 𝑗) [𝑇 (𝑗),𝑇 ( 𝑗 ),...,𝑇 ( 𝑗 ) ].Themultivariatesubsequence
|     |     |     |     | 𝑖 ,ℓ = 𝑖 | 𝑖 + 𝑖 + ℓ −1 |     |
| --- | --- | --- | --- | -------- | ------------ | --- |
1
isdefinedas𝑇 [𝑇 ( 0),...,𝑇 ( 𝐷−1) ].Foragivenunivariatetimeseries𝑇,thesetofallsubsequencesin𝑇 oflengthℓis
|            | 𝑖,ℓ = 𝑖 ,ℓ | 𝑖 ,ℓ             |     |     |     |     |
| ---------- | ---------- | ---------------- | --- | --- | --- | --- |
| definedasT | ={𝑇 ,𝑇     | ,...,𝑇 |𝑇|−ℓ,ℓ}. |     |     |     |     |
ℓ 0,ℓ 1,ℓ
6 Distance-basedMethods
Inthissection,variousdistance-basedanomalydetectionmethodsareintroduced.Weenumeratethemethodsinthree
categoriesdescribedinthefollowingsection.WeenumerateallthementionedmethodsinTable1.
Table1. Summaryofthedistance-basedanomalydetectionmethods.
|     |         |     | SecondLevel     | Prototype       | Dim Method | Stream |
| --- | ------- | --- | --------------- | --------------- | ---------- | ------ |
|     | KNN[91] |     | Proximity-based | NearestNeighbor | M U        | ✗      |
✗
|     | KnorrSeq2[177] |     | Proximity-based | NearestNeighbor | M U |     |
| --- | -------------- | --- | --------------- | --------------- | --- | --- |
|     | LOF[34]        |     | Proximity-based | LOF             | M U | ✗   |
|     | COF[236]       |     | Proximity-based | LOF             | M U | ✗   |
✓
|     | LOCI[178] |     | Proximity-based | LOF | M U |     |
| --- | --------- | --- | --------------- | --- | --- | --- |
|     | ILOF[200] |     | Proximity-based | LOF | M U | ✓   |
✓
|     | DILOF[168]  |     | Proximity-based  | LOF     | M U |     |
| --- | ----------- | --- | ---------------- | ------- | --- | --- |
|     | HSDE[131]   |     | Proximity-based  | LOF     | I U | ✗   |
|     | k-means[91] |     | Clustering-based | k-means | M U | ✗   |
✗
|     | Hybrid-k-means[228] |     | Clustering-based | k-means | M U  |     |
| --- | ------------------- | --- | ---------------- | ------- | ---- | --- |
|     | DeepkMeans[163]     |     | Clustering-based | k-means | M Se | ✗   |
✗
|     | DBSCAN[215]  |     | Clustering-based | DBSCAN | M U |     |
| --- | ------------ | --- | ---------------- | ------ | --- | --- |
|     | DBStream[88] |     | Clustering-based | DBSCAN | M U | ✓   |
|     | MCOD[120]    |     | Clustering-based | -      | I U | ✗   |
✗
|     | CBLOF[93]         |     | Clustering-based | LOF | M U |     |
| --- | ----------------- | --- | ---------------- | --- | --- | --- |
|     | sequenceMiner[38] |     | Clustering-based | -   | I U | ✗   |
✗
|     | NorM(SAD)[23] |     | Clustering-based | NormA | I U |     |
| --- | ------------- | --- | ---------------- | ----- | --- | --- |
|     | NormA[25]     |     | Clustering-based | NormA | I U | ✗   |
|     | SAND[31]      |     | Clustering-based | NormA | I U | ✓   |
✗
|     | TARZAN[115] |     | Discord-based | -   | I S |     |
| --- | ----------- | --- | ------------- | --- | --- | --- |
|     | HOTSAX[114] |     | Discord-based | -   | I U | ✗   |
✗
|     | DAD[258]    |     | Discord-based | -             | I U |     |
| --- | ----------- | --- | ------------- | ------------- | --- | --- |
|     | AMD[257]    |     | Discord-based | -             | I U | ✗   |
|     | STAMPI[262] |     | Discord-based | MatrixProfile | M U | ✓   |
✗
|     | STOMP[269]  |     | Discord-based | MatrixProfile | M U |     |
| --- | ----------- | --- | ------------- | ------------- | --- | --- |
|     | MERLIN[169] |     | Discord-based | MatrixProfile | I U | ✗   |
✗
|     | MERLIN++[170] |     | Discord-based | MatrixProfile | I U |     |
| --- | ------------- | --- | ------------- | ------------- | --- | --- |
|     | SCRIMP[268]   |     | Discord-based | MatrixProfile | I U | ✗   |
|     | SCAMP[271]    |     | Discord-based | MatrixProfile | I U | ✗   |
✓
|     | VALMOD[135] |     | Discord-based | MatrixProfile | I U |     |
| --- | ----------- | --- | ------------- | ------------- | --- | --- |
|     | DAMP[146]   |     | Discord-based | MatrixProfile | I U | ✓   |
✓
|     | LAMP[272] |     | Discord-based | MatrixProfile | I Se |     |
| --- | --------- | --- | ------------- | ------------- | ---- | --- |
I:Univariate;M:Multivariate//S:Supervised;Se:Semi-SupervisedU:Unsupervised
6.1 Proximity-basedMethods
Proximity-basedmethodsusedistancetocloseneighborhoodsasthemainsteptodetectanomalies.Wedetailbelow
twomethodtypesofproximity-basedmethods.
6.1.1 KthNearestNeighbor. Oneofthefirstdistance-basedandproximity-basedmethodsintroducedintheliterature
foranomalydetectionisusingK-thNearestNeighbor(KNN)principle[91].KNN-typemethodsutilizeametricamong
neighboringsub-sequencestoinfertheabnormalityscoresofthetimeseries’sub-sequences.Adistancemeasure
𝑑(·,·)(alsocalleddissimilaritymeasure)isusedtofindthenearestneighborsforeachsubsequence.Commondistance
measuresareEuclidean,Manhatten,oringeneral,Minkowskidistances.Thek-anomalyscoreA𝑘 :{𝑇 𝑖,ℓ}𝑖∈I →Rfor
iscalculatedbasedoneachsub-sequences’𝑘𝑡ℎ
thesetoftimeseries’sub-sequences{𝑇 𝑖,ℓ}𝑖∈I nearestneighborsusinga
ManuscriptsubmittedtoACM

14 Paparrizosetal.
variableaggregationfunction𝑎𝑔𝑔:R𝑘 →R:
A𝑘(𝑇 𝑖,ℓ)= inf 𝑎𝑔𝑔 𝑗∈J 𝑑(𝑇 𝑖,ℓ ,𝑇 𝑗,ℓ) (1)
J⊂I,|J|=𝑘+1
Intheaboveequation,ℓisthefixedlengthoftheslidingwindow,and𝑘+1accountsfortrivialmatches.Followingthe
intuitionof[202]thattheanomalyscoreforasubsequence𝑇 𝑖,ℓ isthedistancetoits𝑘𝑡ℎ nearestneighbor,wecanuse
𝑎𝑔𝑔=(cid:205).AlternativeproposalsforA𝑘 mayutilizeotheraggregationmethods,suchasmedian,minimum,orother
functionsthatpoolthedistancesintoscalarscores.Withdifferentaggregationfunctionsanddistancemetricschoices,
onecanproposedifferentKNN-typemodelsthatareappropriateforvariousanomalydetectionproblems.
InadditiontothestandardKNNtechnique[202],wherethemaximumdistancetothe𝑘𝑡ℎ
nearestneighborisusedas
anomalyscore,othervariantsofKNNshavebeensuggestedbyresearchers.Forinstance,KnorrSeqandKnorrSeq2are
alsotwovariantsofKNNsproposedinthelitterature[177].ThefirstalgorithmKnorrSeqisbasedonatumblingwindow
anddiscoversonlyglobaloutliersbymarkingthosesub-sequencesforwhichatleast𝑝%oftheothersubsequence
arefurtherawaythanathreshold𝐷.TheirsecondalgorithmKnorrSeq2isanimplementationofKNNthatdetects
sub-sequencesasoutliersifatleast𝑝%ofthe𝑘 precedingor𝑘 succeedingsub-sequencesarefurtherawaythana
threshold𝐷.Theanomalyscoreiscalculatedusing(cid:205)astheaggregationfunction:
A𝑘(𝑇 𝑖,ℓ)= inf
∑︁ 1, if𝑑(𝑇 𝑖,ℓ ,𝑇 𝑗,ℓ) >𝐷
(2)
J⊂I,|J|=2𝑘+1,∀𝑗∈J,|𝑗−𝑖|≤𝑘 𝑗∈J0, otherwise

Theanomaloussub-sequencesareselectedusingathreshold𝜏 =𝑝𝑘ontheanomalyscores:A𝑘(𝑇 𝑖,ℓ) <=𝜏.
6.1.2 LocalOutlierFactor. Themostcommonlyusedproximity-basedapproachistheLocalOutlierFactor(LOF)[35],
whichmeasuresthedegreeofbeinganoutlierforeachinstance.Unlikethepreviousproximity-basedmodels,which
directlycomputethedistanceofsub-sequences,LOFdependsonhowtheinstanceisisolatedtothesurrounding
neighborhood.Thismethodaimstosolvetheoutlierdetectiontaskwhereanoutlierisconsideredas“anobservation
thatdeviatessomuchfromotherobservationsastoarousesuspicionthatitwasgeneratedbyadifferentmechanism"
(Hawkinsdefinition[91]).Thisdefinitioniscoherentwiththeanomalydetectiontaskintimeserieswherethedifferent
mechanismcanbeeitheranarrhythmiainanelectrocardiogramorafailureinthecomponentsofanindustrialmachine.
First,let’sconsider𝑇 𝑖,ℓ and𝑇 𝑗,ℓ twosub-sequencesofthesametimeseries.Inthefollowingparagraphs,wenotethese
twosub-sequences,AandB,respectively.Given𝑘-𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒(𝐴)thedistancebetween𝐴andits𝑘𝑡ℎ
nearestneighbor
(𝑁 𝑘(𝐴)thesetofthese𝑘neighbors),LOFisbasedonthefollowingreachabilitydistancedefinition:
𝑟𝑑 𝑘(𝐴,𝐵)=𝑚𝑎𝑥(𝑘-𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑒(𝐵),𝑑(𝐴,𝐵)) (3)
AsillustratedinFigure9,themainconceptbehindthisdistancedefinitionistostressoutthehomogeneityof
distancesbetweeninstanceswithinthe𝑘-neighborhood(i.e.,the𝑘-neighborhoodwillhavethesamedistancebetween
eachother).Thusthelocalreachabilitycanbedefinedasfollow:
𝑙𝑟𝑑 𝑘(𝐴)=
(cid:205)
𝐵∈𝑁𝑘
|𝑁
(𝐴
𝑘
)
(
𝑟
𝐴
𝑑
)
𝑘
|
(𝐴,𝐵)
(4)
Givenaninstance,𝐴,𝑙𝑟𝑑 𝑘(𝐴)istheinverseoftheaveragereachabilityofAfromitsneighborhood,i.e.,theaverage
distanceatwhich𝐴canbereachedfromitsneighbors.Therefore,LOFisgivenby:
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 15
rd(A,B)
 B k
 B
rd(A,B)
|     |     | k   | A   |     |
| --- | --- | --- | --- | --- |
 C
A
rd(A,C) k
| rd (A,C) |     |  D  |     |     |
| -------- | --- | --- | --- | --- |
k
 C
| (a) Reachability distance  |     | (b)    Local reachability density  |     |     |
| -------------------------- | --- | ---------------------------------- | --- | --- |
Fig.9. (a)ReachabilitydistancebetweenAandB,AandCfor𝑘=4.(b)Differencebetween𝑟𝑑 𝑘(𝐴,𝑋),𝑋 ∈𝑁 𝑘(𝐴),whenAisan
anomalyandB,C,andDareregularinstances.
|           |                      | (cid:205) | 𝑙𝑟𝑑𝑘(𝐵) |     |
| --------- | -------------------- | --------- | ------- | --- |
|           | (cid:205) 𝑙𝑟𝑑𝑘(𝐵)    | 𝐵∈𝑁𝑘(𝐴)   |         |     |
|           | 𝐵∈𝑁 𝑘( 𝐴 ) 𝑙 𝑟 𝑑𝑘(𝐴) | 𝑁         | 𝐴       |     |
| 𝐿𝑂𝐹 𝑘(𝐴)= |                      | = |       | 𝑘 ( ) | |     |
|           | |𝑁 𝐴                 | 𝑙 𝑟       | 𝑑 𝐴     | (5) |
|           | 𝑘 ( ) |              |           | 𝑘 ( )   |     |
Intuitively,the𝐿𝑂𝐹 ofaninstanceistheaverageofthelocalreachabilitydensityoftheneighborsdividedbyits
𝑘
ownreachabilitydensity.Therefore,ifwesetsub-sequencesoflengthℓasthelengthofthesub-sequence,thisfactor
canbeusedasananomalyscore.
Inthepastdecade,researchersalsosuggestedmanyvariantsoftheLOFmethod[35].COF[236],forexample,is
aconnectivity-basedvariantofLOF.Itindicateshowfarawayapointshiftsfromapattern,adjustingthenotionof
isolationtonotdependonthedensityofdataclouds.LOCI[178]isanotherLOF-likealgorithmthatutilizesdifferent
statistics(correlationintegralandMDEF)toinferindividualpoints’isolation.OtherLOFvariantsaretheILOF[200]
andDILOF[168]method,whichadoptsafasteralgorithmanddetectsanomaliesincrementally.Finally,thehierarchy-
segmentation-baseddataextractionmethod(HSDE)[131]isinspiredbythestrategyofLOFtodetectabnormalpoints
intimeseries.
6.2 Discord-basedMethods
ApracticalmodificationtotheKNN-typemodelistousethediscord,whichevolvesfromcomparingdistancestothe
nearestneighbortocomparingdistancestothe𝑘𝑡ℎ neighbor.Suchadaptationsassistinedgeconditionswhereasmall
numberofanomaliesareclusteredalongwithlimiteddistances,andtheconventionalKNNapproachstrugglesto
recognizethem.Thefollowinggivesthespecificdefinitionsofdiscord:
Definition6.1(Top-k𝑚𝑡ℎ [25,37,70,116,144,147,219,261]Supposethewindowisoflengthℓ.Given
-discord).
acollectionofsub-sequences{𝑇 𝑗,ℓ}𝑗∈I,let𝑓 denote𝑚𝑡ℎ -discordfunctionmeasuringthedistanceto𝑚𝑡ℎ nearest
𝑚
| 𝑚   |     |     | isaTop-k𝑚𝑡ℎ |     |
| --- | --- | --- | ----------- | --- |
neighborhoodsothat𝑓 𝑚(𝑇 𝑗,𝑙) =min 𝑑(𝑇 𝑖,𝑙 ,𝑇 𝑗,𝑙).Asub-sequence𝑇 𝑖,ℓ -discordif𝑓 𝑚(𝑇 𝑖,ℓ)isthe
𝑗∈I\{𝑖}
𝑘𝑡ℎ
maximumamongtheset{𝑇 𝑗,ℓ}𝑗∈I.
Notethatthe𝑚𝑡ℎ -discordisthespecialcaseofTop-k𝑚𝑡ℎ
|     |     | -discordwhen𝑘 | =1,anddiscordisthespecialcaseof |     |
| --- | --- | ------------- | ------------------------------- | --- |
𝑚𝑡ℎ -discordwhen𝑚=1.
ManuscriptsubmittedtoACM

16 Paparrizosetal.
Top-1 1st-discord
1stNN
1stNN
2ndNN
Top-1 2nd-discord Top-2 1st-discord
Fig.10. Adatasetwith16sub-sequences(ofthesamelengthℓ)depictedaspointsin2-dimensionalspace;12sub-sequencesare
normal(hollowpoints),and4areanomalous(solid,redpoints).
Figure10illustratesthesenotionswithanexample,whereforeaseofexposition,werepresenteachsub-sequenceas
apointin2-dimensionalspace.Thefiguredepictstwo1 𝑠𝑡 -discords:thediscordinthetop-right(𝑇𝑜𝑝-1)hasits1-NN
atalargerdistancethanthediscordinthebottom-right(𝑇𝑜𝑝-2).Thefigurealsoshowsagroupoftwoanomalous
sub-sequences:oneofthemisthe𝑇𝑜𝑝-12 𝑛𝑑 -discord,andtheothersub-sequenceisits1-NN(alsoadiscord).
Thereexistseveralstudiesthathaveproposedfastandscalablediscorddiscoveryalgorithmsinvarioussettings[37,
70,116,144,147,219,259,261],includingsimpleand𝑚𝑡ℎ -discords1,in-memoryanddisk-awaretechniques,exactand
approximatealgorithms,usingeithertheirSymbolicAggregateApproximation(SAX)[116,219]orHaarwavelets
[37,70].Inthefollowingsections,wepresentthestate-of-the-artsolutionstothesub-sequenceanomalydetection
problem.Notethatinthisdiscussion,wefocusonthe𝑇𝑜𝑝-𝑘anomalies(usinginsteadathreshold𝜖todetectanomalies
wouldbeastraightforwardmodificationofthesolution).
DiskAwareDiscordDiscoverymethod(DAD)[259]isamethodthatproposesanewexactalgorithmtodiscover
discordrequiringonlytwolinearscansofthediskthoughtformanagingverylargedatasets.Thealgorithmusesthe
rawsequencesdirectly.First,itaddressesthesimplerproblemofdetectingrangediscord,thengeneralizestheproblem
todetectthe𝑇𝑜𝑝-𝑘discord.
OtherthanDAD,severalotherdiscord-likeanomalyidentificationapproacheshavealsobeenproposed.TARZAN[115]
isadiscordmethodviaSAXdiscretizationthroughtheslidingwindow.Theapproachprocessesdatabybuildinga
suffixtreeandcalculatingitsanomalyscorebyapplyinginferencesonthediscord.LikeTARZAN,HOTSAX[114]
alsoadoptsSAXdiscretizationthroughouttheprocessingstep;itthenmeasuresthedistancetothenearestnon-self
matchforsub-sequencestoidentifyabnormalities.AMD[257]furtherimprovesHOTSAX,whichperformsdynamic
segmentationtovarythewindowlength.
Asafinalnote,weobservethatinsituationswithmultiplesimilaranomalies,weshouldeitheruseamethodthat
supports𝑚𝑡ℎ
-discords,oruseasimplediscord(i.e.,1
𝑠𝑡
-discord)methodasfollows.Startingatthebeginningofthe
seriesandproceedingtotheright,weapplythediscordmethodbyonlyconsideringthepointstotheleftofthecurrent
position,andeverytimeananomalyisdetected,wesearchtheentireseriesforsimilaranomalies(thiswillrevealall
occurrencesofthemultiplesimilaranomalies).Asweproceedtotheright,thediscordmethodwilldetectonlythe
firstoccurrenceofeachsetofsimilaranomalies(therestbeingdetectedbythesimilaritysearchoperationmentioned
1Theauthorsofthesepapersdefinetheproblemas𝑘𝑡ℎ-discorddiscovery.
ManuscriptsubmittedtoACM

| DiveintoTime-SeriesAnomalyDetection:ADecadeReview |      |                                          |     |         |     |      |                                         |        |        |     | 17  |
| ------------------------------------------------- | ---- | ---------------------------------------- | --- | ------- | --- | ---- | --------------------------------------- | ------ | ------ | --- | --- |
|                                                   |      |                                          |     | Discord |     |      |                                         | Motifs |        |     |     |
|                                                   | (a1) |                                          |     |         |     | (b1) |                                         |        |        |     |     |
|                                                   | 0    | 100                                      | 200 | 300     | 400 | 0    | 100                                     | 200    | 300    | 400 |     |
|                                                   | (a2) |                                          |     |         |     | (b2) |                                         |        |        |     |     |
|                                                   | 0    | 100                                      | 200 | ! 300   | 400 | 0    | "′100                                   | 200    | "′′300 | 400 |     |
|                                                   |      | (a) Discord finding using matrix profile |     |         |     |      | (b) Motifs finding using matrix profile |        |        |     |     |
Fig.11. (a)Matrixprofile(𝑎 2)appliedontheSED(Nasadiskfailuredatasets)timeseriessnippet(𝑎 1).Thehighestvalueinthematrix
profile(𝑎 1)pointstothediscordoftheSEDtimeseries.(b)Matrixprofile(𝑏 2)appliedonasynthetictimeseries(𝑏 1).Thesmallest
| valuesinthematrixprofile(𝑎 |     | 1)pointtoamotifpairinthetimeseries. |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
above).Notethatthissolutionimpliesthatwehaveaccumulatedenoughdataatthebeginningoftheseriesforthefirst
executionofthediscordmethod.
6.2.1 MatrixProfile. MatrixProfile[261,270]isadiscord-basedmethodthatrepresentstimeseriesasamatrixof
closestneighbordistances.Comparedtoitspredecessor,MatrixProfileproposedanewmetadatatimeseriescomputed
effectively,capableofprovidingvariousvaluabledetailsabouttheexaminedtimeseries,suchasdiscords.Forsimplicity,
wecancallthismetadataseriesmatrixprofile,andwecandefineitasfollows:
|     |     |     | Amatrixprofile𝑀𝑃 |     | ofatimeseries𝑇 |     | oflength𝑛isatimeseriesoflength𝑛−ℓ−1 |     |     |     |     |
| --- | --- | --- | ---------------- | --- | -------------- | --- | ----------------------------------- | --- | --- | --- | --- |
Definition6.2(MatrixProfile).
wherethe𝑖𝑡ℎ elementof𝑀𝑃 containstheEuclideannormalizeddistanceofthesub-sequenceoflengthℓof𝑇 starting
at𝑖toitsnearestneighbor.
However,thelatterdefinitiondoesnottelluswherethatneighborislocated.Thisinformationisrecordedinthe
matrixprofileindex:
Definition6.3(MatrixProfileIndex). Amatrixprofileindex𝐼 isavectoroftheindexwhere𝐼 𝑀𝑃[𝑖] = 𝑗 and𝑗 isthe
𝑀𝑃
indexofthenearestneighborof𝑖.
TwogeneraldefinitionsofJoinmatrixcomputationcanbeinferred.Thefirst,calledSelf-Join,correspondsexactlyto
thematrixprofile.Thesecond,calledJoin,correspondstothesameoperationfortwodifferenttimeseries.Formallywe
havethefollowing:
Definition6.4(TimeSeriesSelf-Join). Givenatimeseries𝑇,theself-joinof𝑇 withsub-sequencelengthℓ,denotedby
𝑇⊲⊳ 𝑇,isametatimeseries,where:|𝑇⊲⊳ 𝑇|=|𝑇|−ℓ+1and∀𝑖.1≤𝑖 |𝑇⊲⊳ 𝑇|,(𝑇⊲⊳ 𝑇)𝑖,1 =𝑑𝑖𝑠𝑡(𝑇 𝑠𝑡𝑁𝑁 of𝑇
| ℓ   |     |     |     | ℓ   |     |     | ≤ ℓ |     | ℓ   | 𝑖,ℓ,1 | 𝑖,ℓ). |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- |
Definition6.5(TimeSeriesJoin). Giventwotimeseries𝐴and𝐵,andasub-sequencelengthℓ,the 𝐽𝑜𝑖𝑛between
| 𝐴 𝐵 |     | (𝐴⊲⊳ | 𝐵), |     |     | |𝐴⊲⊳ | 𝐵|  | |𝐵| −ℓ |     | ∀𝑖.1 𝑖 | |𝐴⊲⊳ 𝐵|, |
| --- | --- | ---- | --- | --- | --- | ---- | --- | ------ | --- | ------ | -------- |
and denoted by ℓ is a meta time series, where: ℓ = +1 and ≤ ≤ ℓ
| (𝐴⊲⊳ 𝐵)𝑖,1 | =𝑚𝑖𝑛(𝑑𝑖𝑠𝑡(𝐵 | ,𝐴  | 1,ℓ),...,𝑑𝑖𝑠𝑡(𝐵 | ,𝐴  | |𝐴|−ℓ+1,ℓ)). |     |     |     |     |     |     |
| ---------- | ----------- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| ℓ          |             | 𝑖,ℓ |                 | 𝑖,ℓ |              |     |     |     |     |     |     |
ThesemetadataarecomputedusingMueen’sultra-fastAlgorithmforSimilaritySearch(MASS)[166]thatrequires
just𝑂(𝑛∗𝑙𝑜𝑔(𝑛))timebyexploitingtheFastFourierTransform(FFT)tocalculatethedotproductsbetweenthequery
andallthesub-sequencesofthetimeseries.Oncethesemetadataaregenerated,retrievingthe𝑇𝑜𝑝-𝑘discordispossible
ManuscriptsubmittedtoACM

18 Paparrizosetal.
byconsideringthemaximumvalueoftheMatrixProfileandorderingit,excludingthetrivialmatches(overlapping
sub-sequences).Retrievingthesub-sequenceswiththeshortestdistancetotheirnearestneighbor(called𝑚𝑜𝑡𝑖𝑓𝑠)is
alsopossible.Thesesub-sequencescorrespondtoarecurrentmotifinthetimeseriesandcanbeusefulintheanomaly
search.
Figure11showsanexampleoftheMatrixProfilemetadata.Ontheonehand,Figure11(a)showsthattheidentified
discordcorrespondstoasub-sequencethatdeviatessignificantlyfromthenormalcycles.Ontheotherhand,Figure11
(b)showsthatthesingularshapesarewell-identifiedasmotifs.
AfamilyofMatrixProfileanomalydetectionmethodshasalsobeenproposedinthelastdecade.STAMP[262]
proposedanalgorithmthatcanprovideanaccurateansweratanytimeduringthefullcomputationwithtimecomplexity
of𝑂(𝑛2𝑙𝑜𝑔(𝑛)).STAMPI[262]notonlyperformsthestandardall-pairs-similarity-joinofsub-sequencesformatrix
profilemethodsbutalsoadaptsthemethodincrementallytoaccommodatestreamingpurposes.STOMP[269],basedon
STAMP,developedafasteralgorithmtakingadvantageofthesub-sequencesorderandachievingthecomputationwith
timecomplexityof𝑂(𝑛2).Moreover,aGPUimplementationofSTOMPhasbeenproposed.LikeSTOMP,SCAMP[271]
alsoadoptsGPUforthematrixprofileanomalydetectionprocess.TheSCRIMPmethod[268]combinestheSTAMP
algorithm(anytime)andSTOMP(ordered)tomakeahybridapproach.Moreover,theLAMPapproach[272]isableto
computeaconstanttimeapproximationoftheMPvaluegivenanewlyarrivingtimeseriessubsequence.Whileevery
aforementionedmethodcanextractdiscordsofapredefinedlength,VALMOD[134]andMAD[136]havebeenproposed
toextractdiscordsofvariablelengthwithinapredefinedlengthinterval.Moreover,MERLIN[169]andMERLIN++[170]
havebeenproposedtoidentifydiscordsofarbitrarylength.Finally,DAMP[146],adiscord-basedmethod,isableto
workononlinesettings,andscaletofast-arrivingstreams.
6.3 Clustering-basedMethods
Approachesbasedonclusteringstrategieshavebeenproposedfortheanomalydetectiontask.Themainideabehind
thesemethodsistopartitionthesub-sequencespaceandthenevaluatehowonesub-sequencefitsintothepartition.
6.3.1 K-meansMethod. Thek-meansclusteringalgorithmisawidelyusedunsupervisedlearningtechniqueindata
miningandmachinelearning.Itsmainobjectiveistopartitionagivendatasetinto𝑘distinctclusters,whereeachdata
pointbelongstotheclusterwiththeclosestmeanvalue.Thealgorithmoperatesiteratively,startingwithaninitial
randomassignmentof𝑘centroids.Forthespecificcaseoftimeseries,theEuclideanortheDTWdistanceiscommonly
used.K-meansalgorithmcanalsobeusedforanomalydetectionintimeseries[91].Thecomputationalstepsarethe
following:
• Allthesub-sequencesofagivenlengthℓ(providedbytheuser)areclusteredusingthek-meansalgorithm.The
Euclideandistanceisused,andthenumberofclustershastobeprovidedbytheuser.
• Oncethepartitionislearned.Wecomputetheanomalyscoresofeachsub-sequencebasedonthedistancetothe
centroidofitsassignedcluster.
• Thelargerthedistance,themoreabnormalthetimeserieswillbeconsidered.
Suchamethodisstraightforwardbuthasbeenshowntobeveryeffectiveforthespecificcaseofmultivariatetime
series[216].Moreover,extensionssuchasHybrid-k-means[228]canbeusedforanomalydetectionaswell.Finally,the
k-meansmethodcanbeusedontopofotherpre-processingandrepresentationsteps.Forinstance,DeepKMeans[163]
usesanAutoencodertolearnalatentrepresentationofthetimeseriesandappliesk-meansontopofthelatentspaceto
identifyanomalies.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 19
6.3.2 DBSCAN. Anothercommonlyusedclustering-basedmethodistheDensity-BasedSpatialClusteringofAppli-
cationwithNoisealgorithm(DBSCAN)[215].Whenidentifyinganomalies,DBSCANmarksdatapointsintothree
categories:(i)corepoints,(ii)borderpoints,and(iii)anomalies.Toclassifythepoints,twonon-parametricparameters
areimportanttodetectthepotentialanomaliesusingDBSCAN:theradius𝜖ofneighborsoftheanalyzedpointandthe
minimumnumber𝜇ofpointsineachnormalcluster.Giventheseparameters,onecanidentifytheanomalousfollowing
thecategorizationofthesub-sequencesasfollows:
• A𝜖−neighborhoodof𝑇 𝑖,ℓ is𝐵 𝜙(𝑇 𝑖,ℓ ,𝜖)∩𝑇,where𝑇 isthetrainingdata{𝑇 𝑖,ℓ}𝑖∈𝐼.And𝐵 𝜙(𝑇 𝑖,ℓ ,𝜖)istheballof
radius𝜖centeredat𝑇
𝑖,ℓ
withrespecttothenorm𝜙(·,·).
• 𝑇 𝑖,ℓ isacorepointifthesizeofthe𝜖−neighborhoodof𝑇 𝑖,ℓ isgreaterthan𝜇.
• 𝑇 𝑖,ℓ isaborderpointif𝑇 𝑖,ℓ containsacorepointinits𝜖−neighborhood.
• 𝑇 𝑖,ℓ isidentifiedasananomaloussub-sequenceif𝑇 𝑖,ℓ isneitherabordernoracorepoint.
DBSCANhasbeenappliedforanomalydetectiononaunivariatetimeseriesthatcontainsobservationswithaverage
dailytemperatureover33years[41].Theprocessingstepistofirstconvertthedatasetintosub-sequencessetwitha
slidingwindow,whicharefurtherz-normalized.Aftertheprocessingstep,DBSCANisappliedtothesub-sequences,
andtheanomaliesaredetectedaccordingly,asthemethodaboveprescribes.Similarclusteringapproachessuchas
DBStream[88]canbeusedforanomalydetection.
6.3.3 OtherClustering-basedMethods. Anotherclustering-basedtime-seriesanomalydetectionmethodistheMCOD[120]
method.MCODmaintainsasetofmicro-clusterscontainingonlynormalobjects(inourcase:sub-sequences)toeffi-
cientlyandrobustlydetectoutliersintheeventstream.MCODdeterminesanobject𝑥 asanoutlierifthereareless
than𝑘clustersatadistanceof𝑅from𝑥.Wecanrepresentthisbinarydecisionusingthefollowingproductfunction:
A𝑘(𝑇 𝑖,ℓ)= inf
(cid:214) 1, if𝑑(𝑇 𝑖,ℓ ,𝑇 𝑗,ℓ) >𝑅
(6)
J⊂I,|J|=𝑘+1𝑗∈J0, otherwise

Thefunctionabovereturnsdiscretevalues1and0only.SoA𝑘 is1ifandonlyifall𝑘 nearestneighborsareat
least𝑅distanceapartfromtheconsideredsubsequence.Moreover,duetoitssimilaritywithKNN-basedmethods,itis
importanttonotethatMCODcanalsobeassociatedwithproximity-basedapproaches.
Anotherclustering-basedapproachisCBLOF[93],aLOF-basedclusteringalgorithm,whichfirstclustersthedata
andthenassignstheCBLOFfactortoeachentrytomeasureboththesizeandrelativeofandamongtheindividual
clusters.
Then,Sequenceminer[38]isanapproachproposedbyNASA.Itclustersthesequencesusingthelongestcommon
sub-sequence(LCS)metricandranksclustermembersbasedonLCS,andselectsthetop𝑝%asanomalies.Theanomalies
areidentifiedbythepartsofthesequencethatdifferthemostandcharacterizesanomalousedit.
Morerecently,NormA[23–25]isaclustering-basedalgorithmthatsummarizesthetimeserieswithaweightedset
ofsub-sequences.Thenormalset(weightedcollectionofsub-sequencestofeaturethetrainingdataset)resultsfroma
clusteringalgorithm(Hierarchical),andtheweightsarederivedfromclusterproperties(cardinality,extra-distance
clustering,timecoverage).AnextensionofNormA,calledSAND[31],hasbeenproposedforstreamingtimeseries.
ThemaindifferencebetweenNormAandSANDliesintheapproachusedtoupdatetheweightinastreamingmanner.
Additionally,theclusteringstepinSANDisperformedusingthek-Shapemethod[183,184,189],whereasNormA
employsahierarchicalclusteringmethod.
ManuscriptsubmittedtoACM

20 Paparrizosetal.
7 Density-basedMethods
Unlikedistance-basedapproaches,thedensity-basedapproachdoesnottreatthetimeseriesassimplenumericalvalues
butimbuesthemwithmorecomplexrepresentations.Thedensity-basedmethodprocessestimeseriesdataontop
ofarepresentationofthetimeseriesthataimstomeasurethedensityofthepointsorsub-sequencespace.Such
representationvariesfromgraphs,trees,andhistogramstoagrammarinductionrule.Thedensity-basedmodelshave
foursecond-levelcategories:distribution-based,graph-based,tree-based,andencoding-based.Weenumerateallthe
mentionedmethodsinTable2.
| Table2. Summaryofthedensity-basedanomalydetectionmethods. |                    |           |            |        |
| --------------------------------------------------------- | ------------------ | --------- | ---------- | ------ |
|                                                           | SecondLevel        | Prototype | Dim Method | Stream |
| FAST-MCD[210]                                             | Distribution-based | MCD       | M Se       | ✗      |
| MC-MCD[89]                                                | Distribution-based | MCD       | M Se       | ✗      |
✗
| OCSVM[150] | Distribution-based | SVM | M Se |     |
| ---------- | ------------------ | --- | ---- | --- |
| AOSVM[81]  | Distribution-based | SVM | M U  | ✓   |
✗
| Eros-SVMs[124] | Distribution-based | SVM | M Se |     |
| -------------- | ------------------ | --- | ---- | --- |
| S-SVM[20]      | Distribution-based | SVM | I Se | ✗   |
| MS-SVDD[253]   | Distribution-based | SVM | M Se | ✗   |
✗
| NetworkSVM[266] | Distribution-based | SVM | M Se |     |
| --------------- | ------------------ | --- | ---- | --- |
| HMAD[87]        | Distribution-based | SVM | I Se | ✗   |
✗
| DeepSVM[250] | Distribution-based | SVM | M U  |     |
| ------------ | ------------------ | --- | ---- | --- |
| HBOS[79]     | Distribution-based | -   | M U  | ✗   |
| COPOD[133]   | Distribution-based | -   | M U  | ✗   |
| ConInd[7]    | Distribution-based | -   | M Se | ✗   |
| MGDD[233]    | Distribution-based | -   | M U  | ✓   |
✗
| OC-KFD[208]      | Distribution-based | -   | M U |     |
| ---------------- | ------------------ | --- | --- | --- |
| SmartSifter[256] | Distribution-based | -   | M U | ✓   |
| MedianMethod[18] | Distribution-based | -   | I U | ✓   |
| S-ESD[97]        | Distribution-based | ESD | I U | ✗   |
| S-H-ESD[97]      | Distribution-based | ESD | I U | ✗   |
✗
| SH-ESD+[244]   | Distribution-based | ESD | I U  |     |
| -------------- | ------------------ | --- | ---- | --- |
| TwoFinger[156] | Graph-based        | -   | I Se | ✗   |
| GeckoFSM[214]  | Graph-based        | -   | M S  | ✗   |
✗
| Series2Graph[26] | Graph-based | Series2Graph | I U |     |
| ---------------- | ----------- | ------------ | --- | --- |
| DADS[217]        | Graph-based | Series2Graph | I U | ✗   |
✗
| IForest[139]        | Tree-based | IForest     | M U |     |
| ------------------- | ---------- | ----------- | --- | --- |
| IF-LOF[53]          | Tree-based | IForest/LOF | M U | ✗   |
| ExtendedIForest[90] | Tree-based | IForest     | M U | ✗   |
✗
| HybridIForest[157] | Tree-based     | IForest | M Se |     |
| ------------------ | -------------- | ------- | ---- | --- |
| SurpriseEncode[42] | Encoding-based | -       | M U  | ✗   |
✗
| GranmmarViz[220] | Encoding-based | -         | I U |     |
| ---------------- | -------------- | --------- | --- | --- |
| EnsembleGI[71]   | Encoding-based | -         | I U | ✗   |
| PST[234]         | Encoding-based | MarkovCh. | M U | ✗   |
✓
| EM-HMM[193]   | Encoding-based | MarkovCh.    | M Se |     |
| ------------- | -------------- | ------------ | ---- | --- |
| LaserDBN[173] | Encoding-based | BayseianNet. | M Se | ✗   |
✗
| EDBN[195]     | Encoding-based | BayseianNet. | M Se |     |
| ------------- | -------------- | ------------ | ---- | --- |
| KDE-EDBN[196] | Encoding-based | BayseianNet. | M Se | ✗   |
| PCA[223]      | Encoding-based | PCA          | M Se | ✗   |
✗
| RobustPCA[174] | Encoding-based | PCA | M U  |     |
| -------------- | -------------- | --- | ---- | --- |
| DeepPCA[44]    | Encoding-based | PCA | M Se | ✗   |
✗
| POLY[260] | Encoding-based | -   | I U |     |
| --------- | -------------- | --- | --- | --- |
| SSA[260]  | Encoding-based | -   | I U | ✗   |
I:Univariate;M:Multivariate//S:Supervised;Se:Semi-SupervisedU:Unsupervised
7.1 Distribution-basedMethods
Thefirstcategoryofdensity-basedapproachesisdistribution-basedanomalydetectionapproaches.Distribution-based
methodsinvolvebuildingadistributionfromstatisticalfeaturesofthepointsorsub-sequencesofthetimeseries.By
examiningthedistributionsoffeaturesofthenormalsub-sequences,thedistribution-basedapproachtriestorecover
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 21
relevantstatisticalmodels.Itusesthemtoinfertheabnormalityofthedata.Inthefollowingsections,wedescribe
importantanomalydetectionmethodsbelongingtothiscategory.
7.1.1 MinimumCovarianceDeterminant. TheMinimumCovarianceDeterminant(MCD)isacommondistribution-
basedstatisticinuse[209].Thealgorithmseekstofindasubset(ofagivensizeℎ)ofallthesequencestoestimate𝜇
(meanofthesubset)and𝑆(covariancematrixofthesubset)withminimaldeterminant.Inotherwords,theobjectiveis
tofindthesubsetthatistheleastlikelytoincludeanomalies.Oncetheestimationisdone,Mahalanobisdistanceis
utilizedtocalculatethedistancefromsub-sequencestothemean,whichisregardedastheanomalyscore.
FAST-MCD[210]isafasterversionoftheMCDalgorithm.Withinsmalldatasets,theresultoftheFAST-MCD
algorithmusuallyalignswiththatoftheexactMCD.Incontrast,fasterandmoreaccurateresultsarederivedthrough
theFAST-MCDratherthantheclassicalMCDforlargetimeseries.Finally,MC-MCD[89],anextensionofMCD,has
beenproposedforthemulti-clustersetting.
7.1.2 One-ClassSVM. One-ClassSupportVectorMachine(OCSVM)isatypicaldistribution-basedexample,which
aimstoseparatetheinstancesfromanoriginandmaximizethedistancefromthehyperplaneseparation[218]or
sphericalseparation[238].Theanomaliesareidentifiedwithpointsofhighdecisionscore,i.e.,farawayfromthe
separationhyper-plane.ThismethodisavariantoftheclassicalSupportVectorMachineforclassificationtasks[94].
Mathematically,givenℓ-dimensionaltrainingdatapoints𝑥 0 ,...𝑥 𝑛 ∈X,a.non-linearfunction𝜙 thatmapthefeature
spaceXtoadotproductspace𝐹,akernel𝑘(𝑥,𝑦)=(𝜙(𝑥),𝜙(𝑦))(usuallysettoaGaussiankernel𝑘(𝑥,𝑦)=𝑒−||𝑥−𝑦||2/𝑐
),
thequadraticprogramtosolveusingahyperplaneisthefollowing:
1 1 ∑︁
min ||𝑤||2+ 𝜉 𝑖 −𝜌
𝜔∈𝐹,𝜉∈R,𝜌∈R2 𝜈ℓ
𝑖
subjectto:(𝜔.𝜙(𝑥 𝑖)) ≥𝜌−𝜉 𝑖 ,
𝜉
𝑖
≥0.
Foragivennewinstance𝑥,byderivingthedualproblem,thedecisionfunctioncanbedefinedasfollow:
∑︁
𝑓(𝑥)=𝑠𝑔𝑛( 𝛼
𝑖
𝑘(𝑥
𝑖
,𝑥)−𝜌)
𝑖
Assumingthattheoptimizationproblemabovecanbesolved,wecanusesuchadecisionfunctionasananomaly
score.Tobeabletodoit,onehastoensuretotraintheOCSVMmodelonanormalsectionofthetimeseriesonly(those
havetobeannotatedbyaknowledgeexpertandthereforerequireextraworktobeused).Figure12illustratesthe
anomalydetectionprocess.ItisalsoimportanttonotethatOCSVMisverysimilartoSupportvectorDataDescription
(SVDD)thathasalsobeenusedforanomalydetection[253].
Inrecentdecades,anarrayofSVMvariantshavebeenappliedinthetimeseriessetting.AOSVM[81]isanefficient
streaminganomalydetectionalgorithmbasedonSVMthataccommodatesSVMtoanonlinedetection.Themodel
isalsoadaptive,i.e.,itforgetsolddata,featuringlowcomputationalandmemoryrequirements.Eros-SVMs[124]is
anothervariantoftheSVMalgorithm.Itadoptsasemi-supervisedapproachtotrainthemodelinthenormaldata.The
algorithmthenmeasurestimewindows’metricsasfeaturesfedintomultipleOCSVMs,whicharefurtherselected
basedontheEROSsimilaritymetric.Moreover,multipleothermethodsbasedonOCSVMhavebeenproposedinthe
literature.ThesemethodseitherproposeprocessingstepsbeforeapplyingOCSVM(suchasNetworkSVM[266]or
ManuscriptsubmittedtoACM

22 Paparrizosetal.
𝑁𝑜𝑟𝑚𝑎𝑙
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒𝑠
𝜌
𝜉
!
𝜔 𝜉
"
𝑂𝑟𝑖𝑔𝑖𝑛𝑂 𝐴𝑏𝑛𝑜𝑟𝑚𝑎𝑙
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒𝑠
Fig.12. OCSVMillustrationinwhichapointcorrespondstoasubsequenceandonlythegreenpointsareprovidedforthetraining
step.
S-SVM[20]thatproposedseasonalitydecompositionorStockwelltransformation)orcombineOCSVMwithother
methods(suchasHMAD[87]thatuseshiddenMarkovchaintorepresentthetimeseriesintoalatentspace,onwhich
OCSVMisapplied).Finally,DeepSVM[250]proposestouseanAutoencoderarchitecturetoextractmeaningfulfeatures
thatuseOCSVMontopofthelearnedlatentspacetodetectanomalies.
7.1.3 Histogram-basedOutlierScore. Histogram-basedOutlierScore(HBOS)[79]isanotherdistribution-basedal-
gorithmforanomalydetection.Foreverysingledimension(i.e.,timestampsofasub-sequenceforunivariatetime
seriesorvaluesacrossmultipledimensionsformultivariatetimeseries),aunivariatehistogramisconstructedwith
𝑘equalwidthbins.Eachhistogramisfurthernormalizedsothattheheightis1.Foragivenmultivariatepoint𝑝(or
univariatesub-sequence𝑇 𝑖,ℓ),wecountthebinthatcontains𝑝foreachdimensionandmultiplytogethertheinverseof
thefrequencyofbinswhere𝑝belongsforalldimensions.ThealgorithmassumesmutualIndependenceamongthe
timeseries’dimensions(orthetimestampsforunivariatesub-sequenceanomalydetection).Moreover,HBOSsuitsthe
particularcaseofhighlyunbalancedtimeseries(i.e.,veryfewanomalies)andunknowndistribution.
7.1.4 ExtremeStudentizedDeviate. Variousstatistics,suchasExtremeStudentizedDeviate(ESD),areusefulforinferring
timeseriesabnormality.Thelattercomputesthestatisticaltestfor𝑘extremevaluesby𝐶
𝑘
=max𝑘|𝑥
𝑘
−𝑥¯|/𝑠,where𝑥¯
and𝑠denotethemeanandthevariance.Thetestisthencomparedwithothercriticalvaluestodetermineifavalueis
abnormal.Ifso,thenthevalueisremoved,andthestatisticaltestisre-calculatediteratively.BuiltonESD,theS-ESD
andSH-ESD[97]methodsremovetheseasonalcomponentusingSeasonal-Trenddecomposition(STL)andsubtractthe
robustmedian.Thepure,normalizeddataisthenappliedwithESDtodetectanomalies.SH-ESD+[244],onafurther
stepthanSH-ESD,appliestheSTLdecompositionusingaLoessregressionandthengeneralizestheESDontheresidual
partofseasonaldecompositiontodetectanomalies.
7.1.5 Other Distribution-based Methods. Besides the distribution-based algorithms presented above, many other
methodsareproposedusingdifferentmodels.First,theMedianMethod[18]isasimpleanomalydetectionmethod
proposedinitiallytofilteroutliers.Themainideaistomeasurethedeviationfromthemedianofthepreviouspoints
andthemedianoftheirsuccessivedifferences.Moreover,SmartSifter[256]aimstobuildahistogramforcategorical
valuesandafinitemixturemodelforcontinuousdata.Theproposedmethodaimstoupdatethosehistograms/density
asnewpointsarriveinanunsupervisedmannerandthencomputeascorethatestimateshowthenewpointupdated
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 23
Fig.13. IllustrationoftheFiniteStateMachine(FSM).
haschangedthehistogram/density.Then,OC-KFD[208]utilizeslinearquantilemodels.Themodelisselectedviacross-
validatedlikelihood,fromwhichalinearquantilemodelisfitted,andoutliersaredetectedbyconsideringconfidence
intervals.Moreover,MGDD[233]utilizeskerneldensityestimationonslidingwindowsoftheoriginaltimeseries.The
estimateddistributionisthenusedtoidentifytheanomalies.Then,COPOD[133]isacopula-basedanomalydetection
methodandanidealchoiceformultivariatedata.Finally,unlikethepreviousmodels,ConInd[7]isanalgorithmbased
ondomainknowledge.Themodelcandetectonlytheknownanomalies,wheremultiplestatisticalanomalyindicators
(conditionindicators)areproposedbasedondifferentdistributionassumptions.
7.2 Graph-basedMethods
Then,graph-basedmethodsareanothercategoryofdensity-basedapproaches.Graph-basedmethodsrepresentthe
timeseriesandthecorrespondingsub-sequencesasagraph.Thenodesandedgesrepresentthedifferenttypesof
sub-sequences(orrepresentativefeatures)andtheirevolutionintime.Inthissection,wedescribethemostimportant
approachesinthiscategory.
7.2.1 FiniteStateMachine. Finally,FiniteStateMachine(FSM)isageneralcategorizationofmachinelearningalgorithms
thatcanbeonlyinexactlyoneofafinitenumberofstatesatanygiventime.Inreactiontoanyinputs,theFSMwill
shiftfromonestatetoanother;suchchangesbetweenstatesarecalledatransition.Inanomalydetection,inputtime
serieswill,uponcertainmachine-learnedrules,changethestateofthealgorithms.Ifthestateturnsintoananomaly,
theinputisidentifiedasanomalous.
Figure13givesanillustrationofsuchaprocess.Inmanyways,FSMissimilartoadynamicBayesiannetwork,which
alsousesDirectedAcyclicGraph(DAG).However,thetransitionrulebetweenFSMstatesisusuallyparametric,and
thustheentireprocessismachinelearningbased.However,FiniteStateMachineisageneralcategorizationwhere
particularmethodsmightbevastlydifferent,eachofwhichisuniquetoitsownspecificrulesofthelearningalgorithm.
TwoFingers[156],forexample,buildsadatabaseofnormalbehaviorbyconstructingasuffixtreeforvariable-length
N-gramsfromthetrainingdata.Thetreesaretransformedwithinthefinitestatemachineandarefurthercompacted
toaDAG.Finally,theFiniteStateMachine,endowedwiththearchitectureofDAG,matchesthenewseriestodetect
anomalies.GeckFSM[214],however,isvastlydifferentfromTwoFingers,despitealsofollowingafinite-statemachine
structure.Theproposedapproach,GeckoFSM,aimstoclusterthepoints(basedontheirslope)intheunivariatetime
seriesandthenextractsomenon-overlappingsub-sequences.Aslope-basedclustermergingoperationthenfindsan
optimalnumberofclusters,wheretransitionhuman-readablerulesofFSMforeachclusterarefurthercomputedusing
theRIPPERalgorithm[55].Anomaliesareidentifiedaspointsthatderivesignificantlyfromtheserules.
7.2.2 GraphRepresentationofSub-sequences. Asecondapproachistoconvertthetimeseriesintoadirectedgraphwith
nodesrepresentingtheusualtypesofsubsequencesandedgesrepresentingthefrequencyofthetransitionsbetween
ManuscriptsubmittedtoACM

24 Paparrizosetal.
Time series
0 1300 2600 3900 5200 6500
Pattern
following a
Pattern recurrent path
following an in the graph
unusual path
in the graph
(possible
anomaly)
Series2Graph representation of the Time series
Fig.14. ExampleofSeries2graphrepresentation.
typesofsubsequences.Series2Graph[26]isbuildingsuchkindsofgraphs.Moreover,anextensionofSeries2Graph
proposedintheliterature,namedDADS[217],proposesadistributedimplementationand,therefore,amuchmore
scalablemethodforlargetimeseries.
Foragivendataseries𝑇,theoverallprocessofSeries2Graphisdividedintothefollowingfourmainsteps.
(1) SubsequenceEmbedding:Projectallthesubsequences(ofagivenlengthℓ)of𝑇 inatwo-dimensionalspace,
whereshapesimilarityispreserved.
(2) NodeCreation:Createanodeforeachoneofthedensestpartsoftheabovetwo-dimensionalspace.These
nodescanbeseenasasummarizationofallthemajorpatternsoflengthℓthatoccurredin𝑇.
(3) EdgeCreation:Retrievealltransitionsbetweenpairsofsubsequencesrepresentedbytwodifferentnodes:each
transitioncorrespondstoapairofsubsequences,whereoneoccursimmediatelyaftertheotherintheinputdata
series𝑇.Werepresenttransitionswithanedgebetweenthecorrespondingnodes.Theweightsoftheedgesare
settothenumberoftimesthecorrespondingpairofsubsequenceswasobservedin𝑇.
(4) SubsequenceScoring:Computethenormality(oranomaly)scoreofasubsequenceoflengthℓ 𝑞 ≥ℓ(withinor
outsideof𝑇),basedonthepreviouslycomputededges/nodesandtheirweights/degrees.
Figure14depictstheresultinggraphreturnedbySeries2Graph.Theunusualpathinthegraph(withedgeswithlow
weightsandnodeswithlowdegrees)correspondstoanomaliesinthetimeseries.
7.3 Tree-basedMethods
Insteadofmodelingthetimeseriesintoagraph,thedifferentpointsorsub-sequencescanalsobeorganizedintreesto
highlightpotentialisolatedinstancesthatcouldcorrespondtoanomalies.IsolationForest(IForest)isdensity-basedand
themostfamoustree-basedapproachforanomalydetection.IForesttriestoisolatetheoutlierfromtherest[140].The
keyidearemainsonthefactthat,inanormaldistribution,anomaliesaremorelikelytobeisolated(i.e.,requiringfewer
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 25
ITree ITree ITree ITree
1 2 3 n
Instance A Instance A Instance A
...
Instance A
Instance N
Instance N Instance N
Instance N
Fig.15. Setofisolationtreesthatrandomlypartitionadataset.Onaverage,instanceNhasalongerpathtotherootthaninstanceA.
Thus,instanceA’sanomalyscorewillbehigher.
randompartitionstobeisolated)thannormalinstances.Ifweassumethelatterstatement,weonlyhavetoproducea
partitioningprocessthatindicateswelltheisolationdegree(i.e.,anomalousdegree)ofinstances.
LetfirstdefinetheconceptofIsolationTreeasstatedin[140].Letbe𝑇𝑟 abinarytreewhereeachnodehaszeroor
twochildrenandatestthatconsistsofanattribute𝑞andasplit𝑝 suchthat𝑝 <𝑞dividesdatapointsintothetwo
children.𝑇𝑟 isbuiltbydividingrecursivelythetrainingdataset𝑇 ={𝑇
𝑖,ℓ
,𝑇
𝑖+1,ℓ
,...,𝑇 |𝑇|−ℓ,ℓ}randomlyselecting𝑝and𝑞
until,themaximaldepthofthetreeisreached,orthenumberofdifferentinstancesisequalto1.Figure15depictsan
exampleofisolationtrees.
Usingthatkindofdatastructure,thepathlengthintothetree𝑇𝑟 toreachaninstance𝑇 𝑖,ℓ isdirectlycorrelatedto
theanomalydegreeofthatinstance.Therefore,wecandefinetheanomalyscoreasfollow:
𝑆(𝑥,𝑛)=2 𝑠𝑠 =
(cid:205)
𝑇𝑟∈T
ℎ(𝑥,𝑇𝑟)
,𝑐(𝑛)=𝐻(𝑛−1)−
2(𝑛−1)
(7)
|T|𝑐(𝑛) 𝑛
Withℎ(𝑥,𝑇𝑟)thelengthofthepathtoreach𝑥 inthetree𝑇𝑟,T asetofdifferentisolationtreesbuilt,𝑛thenumber
ofinstancesinthetrainingset,andHistheharmonicnumber.ItcanbesimplybutsurelyestimatedusingtheEuler
constant.
OtherIForest-basedalgorithmshavealsobeenproposedrecently.ExtendedIForest[90]isanextensionofthe
traditionalIsolationForestalgorithm,whichremovesthebranchingbiasusinghyperplaneswithrandomslopes.The
randomslopinghyperplanesenableanunbiasedselectionoffeaturesfreeofthebranchingstructurewithinthedataset.
HybridIForest[157]isanotherimprovementonIForest,enablingasupervisedsettingandeliminatingthedataset’s
potentialconfoundingduetounbalancedclusters.Finally,IF-LOF[53]combinesIForestandLOFbyapplyingIForest
andthenutilizesLOFtorefinetheresults,whichspeedsuptheprocess.
7.4 Encoding-basedMethods
Encoding-basedmethodsrepresentthesub-sequencesofatimeseriesintoalow-dimensionallatentspaceordata
structure.Theanomalyscoreisdirectlyfromthelatentspacerepresentations.Morespecifically,theanomalyscoresare
attributedtothepointsthatcorrespondtotheencodedsub-sequencesinthelatentspace.
7.4.1 PrincipalComponentAnalysis. Thefirstencoding-basedapproachistoencodeandrepresentthetimeserieswith
itsprincipalcomponents.PrincipalComponentsAnalysis(PCA)investigatesthemajorcomponentsofthetimeseries
thatcontributethemosttothecovariancestructure.Theanomalyscoreismeasuredbythesub-sequencesdistancefrom
0alongtheprincipalcomponentsweightedbytheireigenvalues.Astandardroutineistopick𝑞significantcomponents
ManuscriptsubmittedtoACM

26 Paparrizosetal.
thatcanexplain50%variationsofthetimeseriesand𝑟 minorcomponentsthatexplainlessthan20%variations.A
pointisananomalyifitsvaluesofmajorprinciplescomponents,𝑦
1
,𝑦
2
...,haveaweightedsumexceedingthethreshold
itsminoronehas.So𝑥 (orasub-sequence𝑇 𝑖,ℓ ofagiventimeseries)isananomalyif:
𝑞 𝑝
∑︁𝑦 𝑖 ∑︁ 𝑦 𝑖
𝜆 >𝑐 1or, 𝜆 >𝑐 2 (8)
𝑖 𝑖
1 𝑝−𝑟+1
Intheequationabove,𝑐 1and𝑐 2arepredefinedthresholdvalues,and𝜆saretheeigenvalues.RobustPCA[174]aims
torecovertheprincipalmatrix𝐿 0bydecomposingtheoriginalcovariancematrixinto𝑀 =𝐿 0 +𝑆 0tominimizetherank
of𝐿 0.Theresidualterm𝑆 0helpsseparatetheanomaloussubsetsandmakesthealgorithmapplicabletotimeseries
containingmanyanomalies.Finally,deepPCA[44]issimilartorobustPCAbutwithanautoencoderpreprocessingstep
first.Theautoencodermapsthetimeseriesintoalatentspace,andthenthePCA(describedabove)isusedtoidentify
anomalies.
7.4.2 GrammarandItemsetRepresentations. Anotherapproachistorepresentthetimeseriesintoasetofsymbols
associatedwithrules.GrammarViz[219]adoptsanapproachtofindanomaliesbasedontheconceptofKolmogorov
complexitywheretherandomnessinasequenceisafunctionofitsalgorithmicincompressibility.Themainideaisthat
itispossibletorepresentatimeseriesascontext-freegrammar(asetofsymbolsassociatedwithrules),andthesections
ofthetimeseriesthatmatchafewgrammarrulesareconsideredanomalies.Inaddition,Afeatureofthisalgorithmis
alsocenteredonitsabilitytofindanomaliesofdifferentlengths.
Moreprecisely,thealgorithmcanbedividedintodifferentphases.First,thewholetimeseriesissummarizedusing
SymbolicAggregateApproximation(SAX)tohavediscretevaluesandnotcontinuousones.Next,context-freegrammar
isbuiltusingSequitur,alinearspaceandtimealgorithmabletoderivecontext-freegrammarfromastringincrementally.
Finally,aruledensitycurveisbuilt,whichisthemetadatathatallowsthedetectionofanomalies.Itispossibletoobtain
aruledensitycurvebyiteratingoverallgrammarrulesandincrementingacounterforeachtimeseriesthatpointsto
therulespans.Oncetheruledensitycurveisobtained,itispossibletodiscoveranomaliesbypickingtheminimum
valuesofthecurve.Otherwise,itispossibletodiscovertheleastfrequentsub-sequences(andpossibleanomalies)by
applyingtheRareRuleAnomaly(RRA)algorithm.
Othergrammar-basedmethodshavebeenproposedintheliterature.First,EnsembleGI[71]isanextensionof
theGrammarVizalgorithm,whichfurtherimplementsgrammarinductiononanensembleapproachthatobtains
theanomalydetectionresultbasedontheensembledetectionofmodelswithdifferentparametervalues.Unlikethe
previoustwo,SupriseEncode[42]adoptsadistinctcompression-basedmethodrepresentingtherecordasanitemset.
Thecompressionratioofsegments(code-lengthencoding)derivedfromeachsub-sequenceiscomparedamongthe
trainingdatasettoderivetheanomalyscore.
7.4.3 HiddenMarkovModel. AnothertypeofEncoder-basedmethodisHiddenMarkovModel(HMM).Thelatter
assumestheexistenceofaMarkovprocess𝑋 suchthatthetimeseriesdataobservedisdependentonthat𝑋.Thegoal
istoderive𝑋 byobservingthedata.Theanomaliesaredetectedbymeasuringtheabilityoftheencodingtorepresent
thetimeseries.Forinstance,EM-HMM[193]isatime-seriesanomalydetectionmethodbasedonHMM.
Moreprecisely,PST[234]isanotherdetectionmethodbasedonHMM.Itproposesanefficientalgorithmforcomputing
theProbabilisticSuffixTree(PST),acompactvariable-orderMarkovchain.Inpractice,thealgorithmembedspossible
chainsofvalues(andtheirprobability)intothetreesandinferstheanomalyscorebycomputingtheprobabilitiesofthe
chainsofvalues.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 27
7.4.4 BayesianNetworks. BayesianNetworkbuildsagraphdenotingtherelationshipbetweenrandomvariablesin
termsofDirectedAcyclicGraph(DAG).EachnodeintheDAGstandsforarandomvariable,andtheedgesrepresentthe
probabilisticrelationshipsamongthevariables.DynamicBayesianNetwork,ortemporalBayesianNetwork,generalizes
theBayesianNetworkgraphmodeltothetimeseriessetting.Themodeliscapableofmodelingthetemporalrelationship
fordifferentrandomvariableswithfirst-orderassumption.
Fig.16. IllustrationofDynamicBayesianNetwork(DBN).
AsdisplayedinFigure16,therandomvariablesatdifferenttimestampsareconnectedbyprobabilisticedges,which
arereferencedbythemodeltocharacterizethetemporalchangeoftherandomvariablesinthedataset.Thejoint
probabilitydistributionofagivenDBNvariable𝑋 𝑖 isgivenbythefollowingequation:
(cid:214)
𝑃(𝑋 𝑖:𝑡,1 ,𝑋 𝑖:𝑡,2 ,𝑋 𝑖:𝑡,𝑅−1 ...𝑋 𝑖:𝑡,𝑅)= 𝑃(𝑋 𝑖:𝑡,𝑟|𝑃𝑎𝑟(𝑋 𝑖:𝑡,𝑟)) (9)
𝑡≤𝑇,𝑟≤𝑅
𝑃𝑎𝑟(𝑋 𝑖:𝑡,𝑟)denotestheparentof𝑋 𝑖:𝑡,𝑟,whichareeitherinsidetheprevioustimestampsorjusttheparentinsidethe
sametimestamps,duetothefirstorderassumption.
Varioustime-seriesanomalydetectionmethodshaveimplementedDBNintheiralgorithms.LaserDBN[173]is
amethodproposedforimagetimeseries.Thedataisfirstpreprocessedbyk-meansclusteringtoperformfeature
selection,andthenDynamicBayesianNetworkisimplementedtocomputetheprobabilitiesofindividualsub-sequences.
EDBN[195]proposesanextensionofDBNtosuittheparticularcaseoftextualtime-seriesanomalydetection(specifically
forbusinessprocessesandlogs).Finally,KDE-EDBN[196]isanextensionofEDBNthatusesKernelDensityEstimation
(KDE)tohandlenumericalattributesinlogs.
7.4.5 OtherEncoding-basedMethods. Inadditiontoallthemethodsdescribedabove,severalmoreanomalydetection
methodscouldbegroupedintheencoding-basedcategory,suchaspolynomialapproximationmethodstodetect
anomalies,likePOLY[132]orSSA[260].Thelatteristrainingmultiplepolynomialapproximationmodelsforeachtime
series(orsub-sequenceinthetimeseries).Asimilaritymeasurebetweenthetrainedmodelsisusedtodetectanomalies.
8 Prediction-basedMethods
Prediction-basedmethodsaimtodetectanomaliesbypredictingtheexpectednormalbehaviorsbasedonatrainingsetof
timeseriesorsub-sequences(containinganomaliesornot).Forinstance,somemethodswillbetrainedtopredictthenext
valueorsub-sequencebasedonthepreviousone.Then,thepredictionerrorisusedasananomalyscore.Theunderlying
assumptionofprediction-basedmethodsisthatnormaldataareeasiertopredict,whileanomaliesareunexpected,
leadingtohigherpredictionerror.Suchassumptionsarevalidwhenthetrainingsetcontainsnoorfewtimeserieswith
anomalies.Therefore,prediction-basedmethodsareusuallymoreoptimalundersemi-supervisedsettings.Withinthe
ManuscriptsubmittedtoACM

28 Paparrizosetal.
prediction-basedmethods,therecometwosecond-levelcategories:forecasting-basedandreconstruction-based.We
enumerateallthementionedmethodsinTable3.
Table3. Summaryoftheprediction-basedanomalydetectionmethods.
|            |     | SecondLevel       |     | Prototype | Dim | Method Stream |     |
| ---------- | --- | ----------------- | --- | --------- | --- | ------------- | --- |
| ES[226]    |     | Forecasting-based |     | -         | I   | Se ✗          |     |
| DES[226]   |     | Forecasting-based |     | -         | I   | Se ✗          |     |
| TES[226]   |     | Forecasting-based |     | -         | I   | U ✗           |     |
| ARIMA[211] |     | Forecasting-based |     | ARIMA     | I   | U ✓           |     |
✓
| NoveltySVR[149] |     | Forecasting-based |     | SVM   | I   | U    |     |
| --------------- | --- | ----------------- | --- | ----- | --- | ---- | --- |
| PCI[263]        |     | Forecasting-based |     | ARIMA | I   | U ✓  |     |
| OceanWNN[246]   |     | Forecasting-based |     | -     | I   | Se ✗ |     |
| MTAD-GAT[267]   |     | Forecasting-based |     | GRU   | M   | Se ✓ |     |
| AD-LTI[252]     |     | Forecasting-based |     | GRU   | M   | Se ✓ |     |
✓
| CoalESN[172]  |     | Forecasting-based |     | ESN  | M   | Se   |     |
| ------------- | --- | ----------------- | --- | ---- | --- | ---- | --- |
| MoteESN[49]   |     | Forecasting-based |     | ESN  | I   | Se ✓ |     |
| HealthESN[51] |     | Forecasting-based |     | ESN  | I   | Se ✗ |     |
| Torsk[96]     |     | Forecasting-based |     | ESN  | M   | U ✓  |     |
| LSTM-AD[153]  |     | Forecasting-based |     | LSTM | M   | Se ✗ |     |
✗
| DeepLSTM[50]    |     | Forecasting-based |     | LSTM | I   | Se   |     |
| --------------- | --- | ----------------- | --- | ---- | --- | ---- | --- |
| DeepAnT[167]    |     | Forecasting-based |     | LSTM | M   | Se ✗ |     |
| Telemanom★[103] |     |                   |     |      |     | ✗    |     |
|                 |     | Forecasting-based |     | LSTM | M   | Se   |     |
| RePAD[127]      |     | Forecasting-based |     | LSTM | M   | U ✗  |     |
| NumentaHTM[3]   |     | Forecasting-based |     | HTM  | I   | U ✓  |     |
✓
| MultiHTM[249] |     | Forecasting-based    |     | HTM | M   | U    |     |
| ------------- | --- | -------------------- | --- | --- | --- | ---- | --- |
| RADM[59]      |     | Forecasting-based    |     | HTM | M   | Se ✓ |     |
| MAD-GAN[129]  |     | Reconstruction-based |     | GAN | M   | Se ✓ |     |
| VAE-GAN[171]  |     | Reconstruction-based |     | GAN | M   | Se ✗ |     |
| TAnoGAN[17]   |     | Reconstruction-based |     | GAN | M   | Se ✗ |     |
✗
| USAD[8]        |     | Reconstruction-based |     | GAN | M   | Se   |     |
| -------------- | --- | -------------------- | --- | --- | --- | ---- | --- |
| EncDec-AD[152] |     | Reconstruction-based |     | AE  | M   | Se ✗ |     |
✓
| LSTM-VAE[194] |     | Reconstruction-based |     | AE  | M   | Se   |     |
| ------------- | --- | -------------------- | --- | --- | --- | ---- | --- |
| DONUT[254]    |     | Reconstruction-based |     | AE  | I   | Se ✗ |     |
| BAGEL[130]    |     | Reconstruction-based |     | AE  | I   | Se ✗ |     |
✗
| OmniAnomaly[231] |     | Reconstruction-based |     | AE  | M   | Se  |     |
| ---------------- | --- | -------------------- | --- | --- | --- | --- | --- |
| MSCRED[265]      |     | Reconstruction-based |     | AE  | I   | U ✗ |     |
✗
| VELC[264]    |     | Reconstruction-based |     | AE  | I   | Se   |     |
| ------------ | --- | -------------------- | --- | --- | --- | ---- | --- |
| CAE[72,73]   |     | Reconstruction-based |     | AE  | I   | Se ✗ |     |
| DeepNAP[117] |     | Reconstruction-based |     | AE  | M   | Se ✓ |     |
✓
| STORN[227] |     | Reconstruction-based |     | AE  | M   | Se  |     |
| ---------- | --- | -------------------- | --- | --- | --- | --- | --- |
I:Univariate;M:Multivariate//S:Supervised;Se:Semi-SupervisedU:Unsupervised
8.1 Forecasting-basedMethods
Forecasting-basedmethodsuseamodeltrainedtoforecastseveraltimestepsbasedonpreviouspointsorsequences.
Theforecastingresultsarethusdirectlyconnectedtopreviousobservationsinthetimeseries.Theforecastedpointsor
sequencesarethencomparedtotheoriginalonestodeterminehowanomalousorunusualtheseoriginalpointsare.
8.1.1 ExponentialSmoothing. Oneofthefirstforecasting-basedapproachesproposedintheliteratureistheExponential
Smoothing[226].Thelatterisanon-linearsmoothingtechniquetopredictthetimeseriespointsbytakingtheprevious
timeseriesdataandassigningexponentialweightstothesepreviousindividualobservations.Theanomaliesarethen
detectedbycomparingthepredictedandactualresults.Formally,thepredictionofthecurrentvalue𝑇ˆ isdefinedas
𝑖
follows:
𝑁−1
∑︁
|     | 𝑇ˆ =(1−𝛼) | 𝑁−1𝑇 | +   | 𝛼(1−𝛼) | 𝑗−1𝑇 | 𝛼 ∈ [0,1] | (10) |
| --- | --------- | ---- | --- | ------ | ---- | --------- | ---- |
|     | 𝑖         |      | 𝑖−𝑁 |        | 𝑖−𝑗  |           |      |
𝑗=1
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 29
Thus,theestimatedsub-sequenceisalinearcombinationofthepreviousdatapoints,withtheweightsvarying
exponentially.Theparameter𝛼 standsfortherateofexponentialdecrease.Thesmallerthe𝛼 is,themoretheweightis
assignedtothedistantdatapoints.
Inaddition,severalapproachesbasedonexponentialsmoothinghavebeenproposed.Forexample,DoubleExponential
Smoothing(DES)andTripleExponentialSmoothing(TES)[226]arevariantsoftheexponentialsmoothingtechniques
fornon-stationarytimeseries.InDES,afurtherparameter𝛽isutilizedtosmooththetrendthatatimeseriescanhave.
Forthespecialcaseoftimeseriescontainingseasonality,TESenablesanotherparameter𝛾 tocontrolit.
8.1.2 ARIMA. Anotherearlycategoryofforecasting-basedapproachesproposedintheliteratureisARIMAmod-
els[211].Thelatterassumesalinearcorrelationamongthetimeseriesdata.ThealgorithmfitstheARIMAmodelon
thetimeseriesanddrawsanomaliesbycomparingthepredictionoftheARIMAmodelandrealdata.Formally,An
ARIMA(𝑝′,𝑞)modelisbuiltuponthefollowingiterativeequations:
|       | 𝑝′  |          | 𝑞           |      |
| ----- | --- | -------- | ----------- | ---- |
|       | ∑︁  |          | ∑︁ 𝑝        |      |
| 𝑇 𝑖 = | 𝛼 𝑘 | 𝑇 𝑡−𝑘 +𝜖 | 𝑖 + 𝜃 𝜖 𝑖−𝑗 | (11) |
𝑗
|     | 𝑘=1 |     | 𝑗=1 |     |
| --- | --- | --- | --- | --- |
Overall,usingARIMAmodels,weassumethateverynexttimeseriesvaluescorrespondtoalinearcombinationof
thepreviousvaluesandresiduals.Notethattheresidualsmustbeestimatedinaniteratedmanner.Moreover,Prediction
ConfidenceInterval(PCI)[263]isanextensionoftheARIMAmodel,whichfurthercombinesthenearestneighbor
method.Thepredictionconfidenceintervalallowsdynamicthresholding.Thethresholdcanbeestimatedonthe
historicalnearestneighbors.
8.1.3 LongShort-TermMemory. LongShort-TermMemory(LSTM)[98]networkhasbeendemonstratedtobepar-
ticularlyefficientinlearninginnerfeaturesforsub-sequencesclassificationortimeseriesforecasting.Suchamodel
canalsobeusedforanomalydetectionpurposes[67,154].Thetwolatterpapers’principleisasfollows:Astacked
LSTMmodelistrainedonnormalpartsofthedatathatwecall𝑁.Theobjectiveistopredictthepoint𝑁 𝑖 ∈𝑁 orthe
sub-sequence𝑁 usingthesub-sequence𝑁
𝑖,𝑙 𝑖−𝑙,𝑙.Consequently,themodelwillbetrainedtoforecastahealthystateof
1
thetimeseries,and,therefore,willfailtoforecastwhenitwillencounterananomaly.
LSTMnetworkisaspecialtypeofRecurrentNeuralNetwork(RNN),basedonLSTMunitsasmemorycellstoencode
hiddeninformation.Figure17depictsthecomponentsandinteractionswithinanLSTMcell.Thevariouscomponents
aregivenby:
| 𝑓 =𝜎 𝑔(𝑊    | 𝑥 +𝑈   | ℎ      | +𝑏 𝑓)        |     |
| ----------- | ------ | ------ | ------------ | --- |
| 𝑡           | 𝑓 𝑡    | 𝑓 𝑡−1  |              |     |
| 𝑖 =𝜎 𝑔(𝑊    | 𝑥 +𝑈   | ℎ +𝑏   |              |     |
| 𝑡           | 𝑖 𝑡    | 𝑖 𝑡−1  | 𝑖)           |     |
| 𝑜 𝑡 =𝜎 𝑔(𝑊  | 𝑥 𝑡 +𝑈 | ℎ 𝑡−1  | +𝑏 )         |     |
|             | 0      | 0      | 0            |     |
| 𝑐 =𝑓 ◦𝑐     | +𝑖     | ◦𝜎 𝑐(𝑊 | 𝑥 +𝑈 ℎ +𝑏 𝑐) |     |
| 𝑡 𝑡         | 𝑡−1    | 𝑡      | 𝑐 𝑡 𝑐 𝑡−1    |     |
| ℎ 𝑡 =𝑜 𝑡 ◦𝜎 | ℎ(𝑐 𝑡) |        |              |     |
Bycombiningalargenumberofcell(outlinedinFigure17)andstackingthem[154],onecanfittheweightsto
forecastthetimeseriesintwodifferentwaysdescribedasfollow:(i)Thefirstistotrainthenetworkusingafixedtime
windowlength𝑇 = [𝑇 ,...,𝑇 ]topredict𝑇 𝑡,(ii)orusingthesameinputtopredicttheincomingsequence
𝑡−ℓ−1,ℓ 𝑡−ℓ 𝑡−1
𝑇 𝑡,ℓ′ = [𝑇 𝑡 ,...,𝑇 𝑡+ℓ′].Forthespecificpurposeofanomalydetection,wewillassumethatsuchamodelcanbetrained
ManuscriptsubmittedtoACM

30 Paparrizosetal.
ℎ'
|     |     | *'() | x + |     | *'  |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- |
#$%ℎ
|     |     | ,'  | -' x | .'  |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
x
|     |     | !"   | !" #$%ℎ | !"  |     |     |     |
| --- | --- | ---- | ------- | --- | --- | --- | --- |
|     |     | ℎ'() |         |     | ℎ'  |     |     |
+'
|      |            | ℎ'()   |            | ℎ'   |            | ℎ'/) |      |
| ---- | ---------- | ------ | ---------- | ---- | ---------- | ---- | ---- |
| *'(0 | x          | +      | x +        |      | x +        |      | *'/) |
|      |            | x #$%ℎ |            | #$%ℎ |            | #$%ℎ |      |
|      |            |        | x          |      | x          |      |      |
|      |            | x      |            | x    |            | x    |      |
|      | !" !" #$%ℎ | !"     | !" !" #$%ℎ | !"   | !" !" #$%ℎ | !"   |      |
| ℎ'(0 |            |        |            |      |            |      | ℎ'/) |
|      | +'()       |        | +'         |      | +'/)       |      |      |
Fig.17. LSTMcellarchitecture.
toachievebothofthepreviouslyenumeratedtasks.Then,whathastobedoneistotrainthismodelonthenormal
sectionofthetimeseries(aprioriannotatedbytheknowledgeexpert)andusetheforecastingerrorasananomaly
score.Therefore,onecanexpecttoobtainabiggerforecastingerrorforasub-sequencethatthemodelhasneverseen
(likeananomaly),ratherthanausualsub-sequence.
ThereexistsalargevarietyofmethodsbasedonLSTMneuralnetworksproposedintheliterature.First,DeepLSTM[50]
isastandardimplementationofLSTMnetworks.ThegenerativemodelstackstheLSTMnetworktrainedfromnormal
sectionsofthetimeseries.Then,LSTM-AD[153]adoptsasimilarapproachtoDeepLSTM.Inadditiontotrainingthe
LSTMmodeltopredicttimeseries,LSTM-ADalsoestimatesthetrainingdataset’serrorswithmultivariatenormal
distributionandcalculatestheanomalyscorewiththeMahalanobisdistance.
Moreover,Telemanom[103]isanLSTM-basedapproachthatfocusesonchanneleddata(i.e.,multivariatetimeseries).
AnLSTMnetworkistrainedforeachchannel.Thepredictionerrorisfurthersmoothedovertime,andlowerrorsare
prunedretroactively.Then,RePad[127]isanotherLSTM-basedalgorithmthatconsidersshort-termhistoricaldata
pointstopredictfutureanomaliesinstreamingdata.ThedetectionisbasedontheAverageAbsoluteRelativeError
(AARE)ofLSTM,andRePadalsoimplementsadynamicthresholdadjustmenttovarythethresholdvalueatdifferent
timestamps.
8.1.4 GatedRecurrentUnit. InadditiontoLSTMcellsfrequentlyimplementedintimeseriessettings,otherneural
networkarchitectureshavealsobeeninuse.OneexampleistheGatedRecurrentUnit(GRU)whichisalsoanRNNbut
operatesinadifferentgatedunitthanLSTMtoforecasttimeseriesvalues.Wewillsummarizesomeoftheapproaches
usedinthesedifferentarchitectures.
MTAD-GAT[267]isthefirstexampleofanomalydetectionmethodsbasedonGRUunits.Thelatterusesboththe
predictionerrorandreconstructionerrorforthedetectionofanomalies(Thismethodcouldfitinbothforecasting
andreconstruction-basedcategories).Themodelutilizestwoparallelgraphattentionlayerstopreprocessthetime
seriesdatasetandthenimplementsaGRUnetworktoreconstructandpredictthenextvalues.AD-ITL[252]isanother
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 31
GRU-basedalgorithmwithseasonalandrawfeaturesasinput.Theinputtimeseriesisfirstusedtoextractseasonal
featuresandfurtherfedtotheGRUnetwork.TheGRUthenpredictseachvalueofthewindow,andLocalTrend
Inconsistency(LTI)isusedasameasureoftheerrortoassesstheabnormalitybetweenpredictedandactualvalues.
8.1.5 EchoStateNetworks. ResearchershavealsoproposedmultipleEchoStateNetworksfordetectinganomaliesin
timeseries.AnEchoStateNetwork(ESN)isavariantofRNN,whichhasasparselyconnectedrandomhiddenlayer.
Themodelrandomizestheweightsinhiddenandinputlayersandalsoconnectsneuronsrandomly.Onlythevaluesin
theoutputlayersarelearned,renderingthemethodalinearmodelthatiseasilytrained.Therandomhiddenlayersact
asadynamicreservoirthattransformstheinputintosequencesofnon-linear,complicatedprocesses.Thetrainable
outputlayerorganizestheencodingoftheinputsinthedynamicreservoir,enablingcomplexrepresentationofthedata
despiteitslinearity.Theinitialvaluesofinputandhiddenlayersarealsochosencarefully,usuallytunedwithmultiple
parameters.
First,CoalESN[172]isasimpleimplementationofEchoStatebypredictingtimeseriesvaluesandcomparingthe
estimatedresultswithrealonestodetermineabnormality.MoteESN[49]adoptsasimilarapproachtoCoalESNbutuses
theabsolutedifferencetomeasuretheanomalyscore.Themodelisoptimizedforasensordevice,wherethenetworkis
trainedofflinebeforedeploymentonthesensor.Torsk[96]isanotheradaptationofESN.Likeitsprecursors,Torskuses
thepreviouswindowastrainingdataandthenpredictsthefollowingones.Themodelfurtherimplementsautomatic
thresholding.Finally,HealthESN[51]isanEchoStateNetworkappliedtothemedicalandhealthdomain.Thealgorithm
utilizesthedefaultarchitecturewithtrainingandtestingsteps;afterasequenceofdatapreprocessing,intelligent
thresholdcomputationisusedtoestimatetheadaptivethresholdanddeclareanomaliesbytheESNpredictions.
8.1.6 HierarchicalTemporalMemory. AnotherrecurrentneuralnetworktypeofapproachisHierarchicalTemporal
Memory(HTM).Thelatteristhecorecomponentofmultipleanomalydetectionmethodsproposedintheliterature.
TheHTMmethodisbasedonthetheoryandideasproposedintheThousandBrainsTheoryofIntelligence[92].The
latterproposesthatmanymodelsarelearnedforeachobjectorconcept,ratherthanonlyonesinglemodelperobject,
asmostofthemethodsdescribedintheprevioussectionsusuallyhandle.
In particular, HTM focuses on three main tasks: sequence learning, continual learning, and sparse distributed
representations.EventhoughHTM-basedmethodscanbeseenasRNN-basedmethods(suchasLSTM,GRU,and
ESN-basedapproach),themaindifferenceisbetweentheneurondefinitionandthelearningprocess.ForHTM,the
unsupervisedHebbian-learningrule[95]isappliedtotrainthemodelratherthantheclassicalback-propagationisnot
applied.
Thefirsttime-seriesanomalydetectionmethodusingHTMproposedintheliteratureistheNumentaHTM[3]and
MultiHTM[249]approaches.Moreover,RADM[59]combinesHTMwithNaiveBayesianNetworkstodetectanomalies
inmultivariatetimeseries.
8.1.7 OtherForecasting-basedMethods. Finally,itisimportanttonotethatforecasting-basedapproachesareageneric
conceptthatrequirestohaveamodelthatcanpredicttheincomingvaluefromhistoricaldata.Therefore,anyregression
approachcanbeusedasaforecasting-basedapproach.Intheprevioussections,wedescribedonahigh-levelthemost
popularmethodsusedtoperformanomalydetectionusingforecasting-basedtechniques.Wecancomplementthelist
withmethodsusingmorespecificarchitectureonspecificapplicationssuchasOceanWNN[246]usingWavelet-Neural
Networks,ormoreclassicalregressiontechniquesusedasforecasting-basedcoreunitssuchasNoveltySVR[149]using
Support-Vector-Machine(SVM).
ManuscriptsubmittedtoACM

𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑇(/)𝑇(/89) 𝑇(;)
-,ℓ -,ℓ -,ℓ
…
ℓ 𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝐷(𝑇 ,𝜃 )
-ℓ /
𝐿𝑎𝑡𝑒𝑛𝑡𝑠𝑝𝑎𝑐𝑒𝑍 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
…
𝐺(𝑍,𝜃 )
4
ℓ
𝑇- 6 ,ℓ (/)𝑇 - 6 ,ℓ (/89)𝑇- 6 ,ℓ (;)
𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
32 Paparrizosetal.
𝐴𝑛𝑜𝑚𝑎𝑙𝑦𝑠𝑐𝑜𝑟𝑒
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝑆= ℒ(𝑇 -,@ ,𝑇′ -,@) 𝑅𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑇 - ( ,ℓ /)𝑇 - ( ,ℓ /89) 𝑇 - ( ,ℓ ;) 𝑇- 6 ,ℓ (/)𝑇 - 6 ,ℓ (/89)𝑇- 6 ,ℓ (;)
𝐿𝑎𝑡𝑒𝑛𝑡𝑠𝑝𝑎𝑐𝑒
… …
E(𝑇,𝜃/) D(𝑍,𝜃/)
ℓ ℓ
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑅𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
0 20 40 60 0 20 40 60
𝑁𝑜𝑟𝑚𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝐴𝑛𝑜𝑚𝑎𝑙𝑜𝑢𝑠𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Fig.18. Overviewofautoencodersmethodsfortime-seriesanomalydetection.
8.2 Reconstruction-basedMethods
Reconstruction-basedmethodsrepresentnormalbehaviorbyencodingsub-sequencesofanormaltrainingtimeseries
intoalow-dimensionalspace.Thesub-sequencesarethenreconstructedfromthelow-dimensionalspace,andthe
reconstructedsub-sequencesarethencomparedtotheoriginalsub-sequences.Thedifferencebetweenthereconstruction
andtheoriginalsequenceisusedtodetectanomalies.Ingeneral,theinputstothereconstructionprocessaretraining
sub-sequences.
8.2.1 Autoencoder. Autoencoderisatypeofartificialneuralnetworkusedtolearntoreconstructthedatasetgivenas
inputusingasmallerencodingsizetoavoididentityreconstruction.Asageneralidea,theautoencoderwilltrytolearn
thebestlatentrepresentation(alsocalledencoding)usingareconstructionloss.Therefore,itwilllearntocompressthe
datasetintoashortercodeandthenuncompressitintoadatasetthatcloselymatchestheoriginal.Figure18depictsan
overviewofautoencodersfortimeseries.Formally,giventwotransitionfunctions𝐸and𝐷,respectivelycalledencoder
anddecoder,thetaskofanautoencoderisthefollowingone:
𝜙 :T ℓ →Z (12)
𝜓 :Z→T ℓ (13)
𝜙,𝜓 =𝑎𝑟𝑔minL(𝑇 𝑖,ℓ ,𝜓(𝜙(𝑇 𝑖,ℓ))) (14)
𝜙,𝜓
Lisalossfunctionthatisusuallysettothemeansquareerroroftheinputanditsreconstruction,formallywritten
||𝑋 −𝜓(𝜙(𝑇 𝑖,ℓ))||2.Thislossfitsthetaskwellforthespecificcaseofsub-sequencesinatimeseriessinceitcoincides
withtheEuclidiandistance.
Thereconstructionerrorcanbeusedasananomalousscoreforthespecificanomalydetectiontask.Asthemodelis
trainedonthenon-anomaloussub-sequenceofthetimeseries,itisoptimizedtoreconstructthenormalsub-sequences.
Therefore,allthesub-sequencesfarfromthetrainingsetwillhaveabiggerreconstructionerror.
Asautoencoderhasbeenapopularmethodintherecentdecade,manyanomalydetectionalgorithmsarebasedon
autoencoderalgorithms’implementation.EncDec-AD[152]isthefirstmodelthatimplementsanencoder-decoder
byusingreconstructionerrortoscoreanomalies.LSTM-VAE[194]andMSCRED[265]useLSTMandConvolutional
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 33
𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑇(/)𝑇(/89) 𝑇(;)
-,ℓ -,ℓ -,ℓ
…
ℓ 𝐸𝑥𝑖𝑠𝑡𝑖𝑛𝑔
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝐷(𝑇 ,𝜃 )
-ℓ /
𝐿𝑎𝑡𝑒𝑛𝑡𝑠𝑝𝑎𝑐𝑒𝑍 𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
…
𝐺(𝑍,𝜃 )
4
ℓ
𝑇- 6 ,ℓ (/)𝑇 - 6 ,ℓ (/89)𝑇- 6 ,ℓ (;)
𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Fig.19. OverviewofGANmethodsfortime-seriesanomalydetection.
𝐴𝑛𝑜𝑚𝑎𝑙𝑦𝑠𝑐𝑜𝑟𝑒
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝑆= ℒ(𝑇 -,@ ,𝑇′ -,@) 𝑅𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
LSTMcellsintheautoencoder𝑇a
-
(
,ℓ
/rc)h𝑇
-
(i
,ℓ
/t8e9c)tu𝑇r
-
(
,
e
ℓ
;).Similarly,Omnianomaly[231]isanotherautoe𝑇n
-
6
,
c
ℓ
(o/d)𝑇e
-
6
,
r
ℓ
(/m89e)t𝑇h- 6 ,ℓo(;d)wherethe
autoencoderarchitectureusesGRUandplanarnormalizingfl𝐿𝑎o𝑡w𝑒𝑛.𝑡𝑠𝑝𝑎𝑐𝑒
Then, STORN [227] and DONUT [254] proposed a Varational Autoencoder (VAE) method to detect abnormal
… …
sub-sequences.ForDONUT,itfurtherpreproc E e ( s 𝑇 s , e 𝜃 s/t ) hetimeseriesusi D n ( g 𝑍, t 𝜃 h/e ) MCMC-basedmissingdataimputation
ℓ ℓ
technique[205].ImprovingfromDONUT,BAGEL[130]implementsconditionalVAEinsteadofVAE.VELC[264]sets
upadditionalconstraintstotheVAE.TheDecoderphaseisregularizedduetoanomaliesintrainingdata,whichhelps
𝑂𝑟𝑖𝑔𝑖𝑛𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
𝑟𝑒𝑐𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑒𝑑
fitnormaldataandpreventgeneralizationtomodelabnormalities.
𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Moreover,CAE[72,73]usesaconvolutionalautoencodertoconverttimeseriessub-sequencestoimageencoding.
Thealgorithmalsospeedsupneste
0
d-loo
20
p-sea
4
r
0
chus60ingsub-sequ
0
ence
2
s
0
appr
4
o
0
xima
60
tionwithSAXwordembedding.
𝑁𝑜𝑟𝑚𝑎𝑙𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒 𝐴𝑛𝑜𝑚𝑎𝑙𝑜𝑢𝑠𝑠𝑢𝑏𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒
Finally, DeepNAP [117] is a sequence-to-sequence AE-based model. However, unlike other AE-based models,
DeepNAPdetectsanomaliesbeforetheyoccur.
8.2.2 GenerativeAdversarialNetworks. GenerativeAdversarialNetwork(GAN)isinitiallyproposedforimagegener-
ationpurposes[82]butcanalsobeusedtogeneratetimeseries.GANhastwocomponents:(i)onetogeneratenew
timeseriesand(ii)onetodiscriminatetheexistingtimeseries.Bothofthecomponentsareusefulforthedetectionof
anomalies.Figure19depictstheoverviewofGANmethodsforanomalytimeseries.
Moreprecisely,aGANiscomposedoftwonetworks.Thefirstiscalledthegenerator𝐺(𝑧,𝜃 𝑔)with𝜃 𝑔itsparameters.
Thesecondoneiscalledthediscriminant𝐺(𝑥,𝜃 𝑑)with𝜃 𝑑itsparameters.Theoutputof𝐺isthesameshapeastheinput,
andtheoutputof𝐷isascalar𝐷(𝑥)thatrepresentstheprobabilitythat𝑥 camefromtheoriginaldataset.Therefore
1−𝐷(𝑥)istheprobabilitythat𝐺 hasgenerated𝑥.Formally,𝐺 and𝐷 havetobeoptimized,suchasthetwo-player
optimizationproblemwheretheaccuracyofthediscriminatorhastobemaximizedbutalsominimizedregardingthe
generator.Thevaluetobeminimized,denotedas𝑉(𝐺,𝐷),isdefinedinthefollowingmanner.
m
𝐺
inm
𝐷
ax𝑉(𝐺,𝐷)=E 𝑥∼𝑝𝑑𝑎𝑡𝑎(𝑥) [𝑙𝑜𝑔𝐷(𝑥)]+E 𝑧∼𝑝𝑧(𝑧) [𝑙𝑜𝑔(1−𝐷(𝐺(𝑧)))] (15)
ManuscriptsubmittedtoACM

34 Paparrizosetal.
ForT
ℓ
thesetofsub-sequencestotrainon,andZthecorrespondingsetofsub-sequencesfromthelatentspace
(noisesample),wehavethefollowingstochasticgradientdescend:
1 ∑︁
𝐷𝑖𝑠𝑐𝑟𝑖𝑚𝑖𝑛𝑎𝑛𝑡 :∇𝜃𝑑
|T|
[−𝑙𝑜𝑔𝐷(𝑇)−𝑙𝑜𝑔(1−𝐷(𝐺(𝑍)))] (16)
(𝑇,𝑍)∈(T,Z)
1 ∑︁
𝐺𝑒𝑛𝑒𝑟𝑎𝑡𝑜𝑟 :∇𝜃𝑔|Z| [1−𝑙𝑜𝑔(1−𝐷(𝐺(𝑍)))] (17)
𝑍∈Z
Thisarchitecturehasbeentriedforthespecificcaseoftime-seriesanomalydetection[128].Forthepurposeof
anomalydetection,thegeneratoristrainedtoproducesub-sequenceslabeledasnormal,andthediscriminatoris
trainedtodiscriminatetheanomalies.Thustrainingsuchamodelrequireshavingatrainingdatasetwithnormal
sub-sequences.Onecanusethediscriminatorandthegeneratorsimultaneouslytodetecttheanomaly.First,giventhat
thediscriminatorhasbeentrainedtoseparatereal(i.e.,normal)fromfake(i.e.,anomaly)sub-sequences,itcanbeused
asadirecttoolforanomalydetection.Nevertheless,thegeneratorcanalsobehelpful.Giventhatthegeneratorhas
beentrainedtoproducearealisticsub-sequence,itwillmostprobablyfailtoproducearealisticanomaly.Therefore,the
Euclidiandistancebetweenthesub-sequencetoevaluateandwhatwouldhavegeneratedthegeneratorwiththesame
latentinputcanhavesomesignificanceindiscriminatinganomaly.
SeveralanomalydetectionmethodsbasedonGANhavebeenproposedintheliterature,suchasMAD-GAN[129],
USAD[8]andTAnoGAN[17].TheseapproachestrainGANonthenormalsectionsofthetimeseries.Theanomaly
scoreisbasedonthecombinationofdiscriminatorandreconstructionloss.VAE-GAN[171]isanotherGAN-based
modelthatcombinesGANandVariationalAutoencoder.Morespecifically,thegeneratorisaVAE,whichfurther
competeswiththediscriminator.Theanomalyscoreiscomputedthesameastheprevioustwo.
9 EvolutionofMethodsoverTime:AMeta-Analysis
Atthispoint,wedescribedthemainmethodsproposedintheliteraturetodetectanomaliesintimeseries.Wegrouped
themintothreefirst-levelcategoriesand9second-levelcategories.However,thesefirstorsecond-levelcategoriesdo
notsharethesamedistributionintime.Figure20showsthenumberofmethodsproposedperintervalofyears(left)
andthecumulativenumberovertheyears(right).
Wefirstobservethatthenumberofmethodsproposedyearlywasconstantbetween1990and2016.Thenumberof
methodsproposedintheliteraturesignificantlyincreasedafter2016.Thisfirstconfirmsthegrowingacademicinterest
inthetopicoftime-seriesanomalydetection.
Wecanthendiveintothesecond-levelcategories,andweobservethatthesignificantincreaseinmethodsproposed
iscausedmainlybytheprediction-basedapproachand,morespecifically,byLSTMandautoencoder-basedapproaches.
Between2020and2023,suchmethodsrepresentalmost50%ofthenewlyintroducedanomalydetectionmethods.The
greatsuccessofdeeplearningforcomputervisioncausessuchgrowth.Moreover,thankstotheopen-sourcedeep
learninglibrarysuchasTensorFlowandPyTorch,genericdeeplearningmethodsareeasytoadapttotimeseries.
Wecantheninspecttheevolutionofthenumberofmethodsproposedintheliteraturethatcanhandleunivariateor
multivariatetimeseries.Figure21(right)showsthenumberofmethodsformultivariateandunivariatetimeseriesper
intervalofyearslistedonthex-axis.
Surprisingly,weobservethatmostofthemethodsproposedbetween1990and2016wereproposedformultivariate
timeseries,whereas,inthelastthreeyears,mostoftheproposedmethodsareforunivariatetimeseries.However,
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 35
Numberof methodsproposedper
Numberof methodsproposedper
Second-levelcategories(cumulative)
Second-levelcategories
Reconstruction Reconstruction
|            | noitciderP |          | noitciderP  |
| ---------- | ---------- | -------- | ----------- |
| Encoding   | desab      |          | desab       |
| Graph Tree |            | Encoding | Forecasting |
Forecasting
Graph
| Distribution |               |              | ytisneD    |
| ------------ | ------------- | ------------ | ---------- |
|              | ytisneD desab | Distribution | Tree desab |
Discord
Discord
Clustering
|     | ecnatsiD Clustering |     |          |
| --- | ------------------- | --- | -------- |
|     | desab               |     | ecnatsiD |
desab
Proximity
Proximity
Fig.20. Relativenumberofmethodsproposedovertimepercategory,atdifferenttimes-intervals(left),andcumulative(right).
Numberof methodsproposedthatare  Numberof methodsproposedthatcan
Unsupervisedor Semi-Supervised handleUnivariateor Multivariatetime series
desivrepus-imeS
etairavitluM
sdohtem
Multivariate
Semi-Supervised
|     | desivrepusnU |     | etairavinU |
| --- | ------------ | --- | ---------- |
sdohtem
| Unsupervised | Univariate |     |     |
| ------------ | ---------- | --- | --- |
Fig. 21. Number of methods proposed over time that are Unsupervised/Semi-supervised (left), and that can handle univari-
ate/multivariatetimeseries(right).
afteradeepinspection,mostofthemethodsproposedbefore2016weredesignedforpointanomalydetection(i.e.,
well-definedproblemsformultivariatetimeseries).Therecentinterestinsub-sequenceanomalydetection,joinedby
thefactthatthesubsequenceanomalydetectionproblemformultivariatetimeseriesishardertodefine,leadstoa
significantincreaseinmethodsforunivariatetimeseries.
Finally,wecanmeasuretheevolutionofthenumberofunsupervisedandsemi-supervisedmethodsovertheyears.
ThelatterisillustratedinFigure21(left).Weobservethat65%oftheanomalydetectionmethodsproposedinthe
literaturewereunsupervisedbetween1980and2000,whereas50%ofthemethodsproposedbetween2012and2018
wereunsupervised.
ManuscriptsubmittedtoACM

36 Paparrizosetal.
| Table4.       | Summaryofexistingbenchmarksfortime-seriesanomalydetection. |          |           |               |         |
| ------------- | ---------------------------------------------------------- | -------- | --------- | ------------- | ------- |
|               | #Time                                                      | Average  | Average#  | Average       | Anomaly |
| Benchmark     |                                                            |          |           |               | Dim     |
|               | Series                                                     | Length   | Anomalies | AnomalyLength | Type    |
| NAB[126]      | 58                                                         | 6301.7   | 2         | 287.8         | I P&S   |
| Yahoo[125]    | 367                                                        | 1561.2   | 5.9       | 1.8           | I P&S   |
| Exathlon[108] | 93                                                         | 25115.9  | 1         | 9537.6        | M S     |
| KDD21[113]    | 250                                                        | 77415.1  | 1         | 196.5         | I P&S   |
| TODS[123]     | 54                                                         | 13469.9  | 266.7     | 2.3           | I&M P&S |
| TimeEval[216] | 976                                                        | 30991    | 5.5       | 106.7         | I&M P&S |
| TSB-UAD[185]  | 14046                                                      | 34043.6  | 86.3      | 24.9          | I P&S   |
| TSB-AD[142]   | 1070(Curated)                                              | 105485.2 | 104.2     | 409.5         | I&M P&S |
I:Univariate;M:Multivariate//P:Point;S:Subsequence
Thestatisticsarebasedonthedatasetsdownloadedduringthewritingofthisarticle.
10 EvaluatingAnomalyDetection
Withthecontinuousadvancementoftime-seriesanomalydetectionmethods,itbecomesevidentthatdifferentmethods
possessdistinctpropertiesandmaybemoresuitableforspecificdomains.Moreover,themetricsusedtoevaluate
thesemethodsvarysignificantlyintermsoftheircharacteristics.Consequently,evaluatingandselectingthemost
appropriatemethodforagivenscenariohasemergedasamajorchallengeinthisfield.Inthissection,wewillbegin
bypresentingthebenchmarksthathavebeenproposedintheliteratureforevaluatingtime-seriesanomalydetection
methods.Then,wewilldiscussdifferentevaluationmeasurescommonlyusedinthefieldandexaminetheirlimitations
whenappliedtoanomalydetection.
10.1 ExistingBenchmarks
Inprevioussections,wenotedthatasubstantialnumberoftime-seriesanomalydetectionmethodshavebeendeveloped
overthepastseveraldecades.Multiplesurveysandexperimentalstudieshaveevaluatedtheperformanceofvarious
anomalydetectorsacrossdifferentdatasets[185,216,235].Theseinvestigationshaveconsistentlyhighlightedthe
absenceofaone-size-fits-allanomalydetector.Theemergingconsensusacknowledgesthatamodelperformingwellon
onedatasetisnotsufficienttodeclareananomalydetectionalgorithmuseful.Theeffectivenessofananomalydetector
shouldbedemonstratedacrossawiderangeofdatasetsratherthanseveralcherry-pickingdatasets.Consequently,
therehavebeeneffortsmadetoestablishbenchmarksincorporatingmultipledatasetsfromvariousdomainstoensure
thoroughandcomprehensiveevaluation.
Inthefollowing,wewilloverviewrecentbenchmarksfortime-seriesanomalydetection.Thesebenchmarksare
presentedchronologically,asillustratedinTable4,withbriefdescriptionstodemonstrateadvancementsinthisfield.
NAB[126]provides58labeledreal-worldandartificialtimeseries,primarilyfocusingonreal-timeanomalydetection
forstreamingdata.ItcomprisesdiversedomainssuchasAWSservermetrics,onlineadvertisementclickingrates,
real-timetrafficdata,andacollectionofTwittermentionsoflargepublicly-tradedcompanies.
Yahoo[125]comprisesacollectionofrealandsynthetictimeseriesdatasets,whicharederivedfromtherealproduction
traffictosomeoftheYahooproductionsystems.
Exathlon[108]isproposedforexplainableanomalydetectionoverhigh-dimensionaltimeseriesdata.Itisconstructed
basedonrealdatatracesfromrepeatedexecutionsoflarge-scalestreamprocessingjobsonanApacheSparkcluster.
KDD21(orUCRAnomalyArchive)[113]isacompositedatasetthatcoversvariousdomains,suchasmedicine,sports,
andspacescience.Itwasdesignedtoaddressthepitfallsofpreviousbenchmarks[251].
TODS[123]refinessyntheticcriterionandincludesfiveanomalyscenarioscategorizedbybehavior-driventaxonomy
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 37
aspoint-global,pattern-contextual,pattern-shapelet,pattern-seasonal,andpattern-trend.
TimeEval[216]comprisesacollectionofdatasets(bothrealandsynthetic)fromverydifferentdomains.Thisbenchmark
containsbothunivariateandmultivariatetimeseriesmixingbothpointandsequenceanomalies.Inaddition,this
benchmarkhasbeenfilteredsuchthatthereisnotimeseriesthathaveanormal/abnormalratioabove0.1,andthatat
leastonemethodperformsmorethan0.8AUC-ROCforeachtimeseries.
TSB-UAD[185]isacomprehensiveandunifiedbenchmarkdesignedforevaluatingunivariatetime-seriesanomaly
detectionmethods.Itincludespublicdatasetsthatcontainreal-worldanomalies,aswellassyntheticdatasetsthat
provideeleventransformationmethodstoemulatedifferentanomalytypes.Additionally,thebenchmarkincorporates
artificialdatasetsthataretransformedfromtime-seriesclassificationdatasetswithvaryinglevelsofsimilaritybetween
normalandabnormalsubsequences.ThiscomprehensivecoverageofdifferentanomalyscenariosmakesTSB-UADa
uniformplatformtocomparedifferentmethodsacrossdifferentrealisticscenarios.
Wenotethatthereareongoingdiscussionsregardingthelimitationsofcertaindatasetsusedinexistingbenchmarks.
Wuetal.[251]identifyfourcommonflaws:(i)triviality,(ii)unrealisticanomalydensity,(iii)mislabeledgroundtruth,and
(iv)run-to-failurebias.Suchissuesunderscorethesubstantialchallengesindesigningtrulyrepresentativebenchmarks.
Inresponse,Wuetal.developamanuallycurateddatasetconsistingprimarilyofunivariatetimeseriesfeaturinga
single,oftenartificiallyintroducedanomaly.However,thisdatasetmaynotaccuratelyreflectreal-worldscenarios
(giventhatmostpreviouslypublishedreal-worlddatasetscontainmultipleanomalies)andexcludesotherpotentially
anomalousregions,resultinginanewsetoflabelingambiguities.Toaddresstheseconcerns,TSB-AD[142]introduces
thefirstlarge-scale,heterogeneous,andmeticulouslycurateddataset,combininghumanperceptionwithmodel-driven
interpretationtoofferimprovedreliability.
TSB-AD[142]isthelargestbenchmarktodate,comprising1,000rigorouslycurated,high-qualitytimeseriesdatasets.
Thisbenchmarkincludebothunivariateandmultivariatecases,ensuringcoverageofawiderangeofreal-world
scenariosforanomalydetection.Itestablishesareliableframeworkforevaluatingmethodsandincludescomprehensive
benchmarkingof40anomalydetectionapproaches(continuouslyupdating2).Eachmethodundergoesathorough
hyperparameter tuning to ensure optimal performance. The benchmark also incorporates the latest advances in
foundationmodel-basedmethods,highlightingtheirpotentialfortimeseriesanomalydetection.
10.2 EvaluationMeasures
Inthissection,wepresentanoverviewofevaluationmetricsusedtoassesstheperformanceofanomalydetectors.
Therearevariouswaystocategorizetheevaluationmetrics.Itcanbeclassifiedbasedonwhetherathresholdneedsto
besetoriftheevaluationisconductedonindependenttimepointsorsequences.Inthefollowing,wewillcategorize
theevaluationbasedontherequirementofthresholdsetting.
10.2.1 Threshold-basedEvaluation. Threshold-basedevaluationrequiressettingathresholdtoclassifyeachpoint(time
step)asananomalyornotbasedontheanomalyscore𝑆 𝑇.Generally,ahigheranomalyscorevalueindicatesamore
abnormalpoint.Themoststraightforwardapproachistosetthethresholdto𝜇(𝑆 𝑇)+𝛼∗𝜎(𝑆 𝑇),with𝛼 setto3[15],
where𝜇(𝑆 𝑇)isthemeanand𝜎(𝑆 𝑇)isthestandarddeviationof𝑆 𝑇.However,thisapproachissensitivetoextreme
valuesintheanomalyscoreandcanresultinunfaircomparisonsbetweendifferentmethodsduetovariationsintheir
statisticalproperties.
2https://thedatumorg.github.io/TSB-AD
ManuscriptsubmittedtoACM

| 38  |     |     |     |     |     |     |     |     | Paparrizosetal. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |
𝑠𝑒𝑡𝑜𝑓
| 1   |     | 1   |     |     |     | 1   | 𝑤𝑖𝑛𝑑𝑜𝑤ℓ | 1   | 𝑤𝑖𝑛𝑑𝑜𝑤ℓ |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- |
𝑃𝑜𝑖𝑛𝑡−𝑤𝑖𝑠𝑒𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛
| 𝑙𝑒𝑏𝑎𝑙 |     | 𝑙𝑒𝑏𝑎𝑙 |     |     |     | ℓ𝑙𝑒𝑏𝑎𝑙 | 1/2 | ℓ𝑙𝑒𝑏𝑎𝑙 | 1/2 |     |
| ----- | --- | ----- | --- | --- | --- | ------ | --- | ------ | --- | --- |
𝑃𝑜𝑖𝑛𝑡−𝑎𝑑𝑗𝑢𝑠𝑡𝑒𝑑𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛
| 0   | e   | 0   | s   |     |     | −ℓ/2+𝑠 0 | 𝑠 𝑒 𝑒+ℓ/2 | 0 −ℓ/2+𝑠 𝑠 | 𝑒 𝑒+ℓ/2 |     |
| --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | ------- | --- |
|     | s   |     | e   |     |     |          |           |            |         |     |
𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑆𝑒𝑡𝑜𝑓 𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑆𝑒𝑡𝑜𝑓 𝑒𝑟𝑜𝑐𝑠𝑦𝑙𝑎𝑚𝑜𝑛𝑎 𝑆𝑒𝑡𝑜𝑓
|     |     |     |     | 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇 |     |     | 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇 |     | 𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇 |     |
| --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- | ---------- | --- |
𝑇ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑𝑇
|     | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥      |     | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥 |     |     |     | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥 | 𝑡𝑖𝑚𝑒𝑖𝑛𝑑𝑒𝑥 |     |     |
| --- | -------------- | --- | --------- | --- | --- | --- | --------- | --------- | --- | --- |
|     | 𝑃𝑜𝑖𝑛𝑡−𝑎𝑑𝑗𝑢𝑠𝑡𝑒𝑑 |     |           |     |     | 𝑅𝑃𝑇 |           |           |     |     |
| 𝑅𝑃𝑇 | 𝑃𝑜𝑖𝑛𝑡−𝑤𝑖𝑠𝑒     | 𝑅𝑃𝑇 |           |     |     |     |           |           |     | 𝑅𝑃𝑇 |
ℓ
|     | 𝐹𝑃𝑅                            |                                                                 |           | 𝐹𝑃𝑅 |     |                                      | 𝐹𝑃𝑅             | 𝐹𝑃𝑅                            |     |     |
| --- | ------------------------------ | --------------------------------------------------------------- | --------- | --- | --- | ------------------------------------ | --------------- | ------------------------------ | --- | --- |
|     |                                |                                                                 | (b.1) AUC |     |     |                                      | (b.2) Range-AUC | (b.3) Volume Under the Surface |     |     |
|     | (a) Threshold-based Evaluation |                                                                 |           |     |     | (b) Threshold-independent Evaluation |                 |                                |     |     |
|     | Fig.22.                        | Illustrationofevaluationmeasuresfortime-seriesanomalydetection. |           |     |     |                                      |                 |                                |     |     |
Toaddressthisissue,researchersinthefieldhavedevelopedalternativemethodsforthresholdselectionthatoperate
automatically,eliminatingtheneedforstatisticalassumptionsregardingerrors.Forinstance,[5]introducedanadaptive
thresholdingtechniquethatexploitstheconsistenttimecorrelationstructureobservedinanomalyscoresduring
benignactivityperiods.Thistechniquedynamicallyadjuststhethresholdbasedonpredictedfutureanomalyscores.
Non-parametricdynamicthresholding,proposedin[104],aimstofindathresholdsuchthatremovingallvaluesabove
itresultsinthegreatestpercentagedecreaseinthemeanandstandarddeviationoftheanomalyscores.Another
approach,knownasPeaks-Over-Threshold(POT)[224,232],involvesaninitialthresholdselection,identificationof
extremevaluesinthetailsofaprobabilitydistribution,fittingthetailportionwithageneralizedParetodistribution
withparameters,computinganomalyscoresbasedontheestimateddistribution,andapplyingasecondarythresholdto
identifyanomalies.
Aftersettingthethreshold,wecanclassifythepointsaseithernormalorabnormalbasedonwhethertheyexceed
the threshold. In the subsequent section, we will review common evaluation measures. We begin by presenting
thenecessarydefinitionsandformulationsforintroducingthesemeasures,followedbyabriefexplanationoftheir
∈{0,1}𝑛
distinctions.Formally,thebinarypredictions𝑝𝑟𝑒𝑑 areobtainedbycomparing𝑆 𝑇 withthreshold𝑇ℎas:
|     |     |     |     |     |     | 0, | if:𝑆 <𝑇ℎ |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | -------- | --- | --- | --- |
𝑇𝑖
|     |     |     | ∀𝑖 ∈ [1,|𝑆 | 𝑇|],𝑝𝑟𝑒𝑑 | 𝑖   | =    |             |     |     | (18) |
| --- | --- | --- | ---------- | -------- | --- | ---- | ----------- | --- | --- | ---- |
|     |     |     |            |          |     | 1, | if:𝑆 𝑇𝑖 ≥𝑇ℎ |     |     |      |

| Bycomparing𝑝𝑟𝑒𝑑tothetrue-labeledanomalies𝑙𝑎𝑏𝑒𝑙 |     |     |     |     |     | ∈{0,1}𝑛 |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
,thepointscanfallintooneofthefollowingfour
categories:
• TruePositive(TP):Numberofpointsthathavebeencorrectlyidentifiedasanomalies.
• TrueNegative(TN):Numberofpointsthathavebeencorrectlyidentifiedasnormal.
• FalsePositive(FP):Numberofpointsthathavebeenwronglyidentifiedasanomalies.
• FalseNegative(FN):Numberofpointsthathavebeenwronglyidentifiedasnormal.
Giventhesefourcategories,severalpoint-wiseevaluationmeasureshavebeenproposedtoassesstheaccuracyof
anomalydetectionmethods.
Precision(orpositivepredictivevalue)isthenumberofcorrectlyidentifiedanomaliesoverthetotalnumberofpoints
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 39
𝑇𝑃
detectedasanomaliesbythemethod:𝑇𝑃+𝐹𝑃.
𝑇𝑃
Recall(orTruePositiveRate,TPR)isthenumberofcorrectlyidentifiedanomaliesoverallanomalies:𝑇𝑃+𝐹𝑁.
FalsePositiveRate(orFPR)isthenumberofpointswronglyidentifiedasanomaliesoverthetotalnumberofnormal
𝐹𝑃
points: 𝐹𝑃+𝑇𝑁.ContrarytoRecall,theoptimalscoreisobtainedbypredictingallthepointsasnormal.
F-Scorecombinesprecisionandrecallintoasinglemetricbytakingtheirharmonicmean,withanon-negativereal
valueof𝛽:
(1+𝛽2)∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙
.Usually,𝛽issetto1,balancingtheimportancebetweenPrecisionandRecall.
𝛽2∗𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙
Precision@kistheprecisionofasubsetofanomaliescorrespondingto𝑘highestvalueintheanomalyscore𝑆 𝑇.
Whilemostcurrentmethods[222,232,255]calculatethesemetricsbytreatingtimepointsasindependentsamples,
theyoftenemploypointadjustmenttechniquestoaccountforconsecutiveanomalies.Thismeansthatdetectingany
pointwithinananomaloussegmentisconsideredasifallpointswithinthatsegmentweredetected,asisshownin
Figure22(a).However,theworkof[118]criticizestheuseofpoint-adjustedmetrics,demonstratingthattheyhaveahigh
likelihoodofoverestimatingdetectionperformanceandthatevenarandomanomalyscorecanyieldseeminglygood
results.Inlightofthiscritique,[118]proposePoint-adjustedmetricsat𝐾%,whereinapredeterminedproportion𝐾%
ofanomaliesmustbedetectedbeforetheapplicationofpointadjustment.Otherrefinedpoint-adjustedmetricsinclude
Delaythresholdedpoint-adjustedF-scorein[52,204].Thismetricconsidersananomalytobedetectedonlyifitis
predictedwithinthefirst𝑘timestepsofthetruth-labeledanomaly.
Furthermore, the above-mentioned metrics ignore the sequential nature of time series. A range-based quality
measure[237]wasrecentlyproposedtoaddresstheshortcomingsofpoint-basedmeasures.Thisdefinitionconsiders
severalfactors:(i)whetherasubsequenceisdetectedornot(ExistenceReward);(ii)howmanypointsinthesubsequence
aredetected(OverlapReward);(iii)whichpartofthesubsequenceisdetected(position-dependentweightfunction);
and(iv)howmanyfragmentedregionscorrespondtoonerealsubsequenceoutlier(CardinalityFactor).Inthisway,
point-basedPrecisionandRecallcanbeextendedtocalculatingRange-basedF-score.
OthermetricsincludeNABscore[126],whichpenalizesfalsepositivepointsbyassigninganegativevalueand
providespositivevaluerewardsforaccuratelydetectinganomaloussegments,withtherewardbeinghigherforearly
predictionofthefirstanomalouspoint.ItisnoteworthythattheutilizationoftheNABscoreitselfisnotwidespread;
however,thebenchmarkintroducedinthispaperiswidelyadoptedintheresearchcommunityforevaluationusing
othermetrics.
10.2.2 Threshold-independentEvaluation. Therequirementtoapplyathresholdtotheanomalyscoresignificantly
affectstheaccuracymeasures.Theycanvarysignificantlywhenthethresholdchanges.Accordingtoarecentwork[180],
threshold-basedmeasuresareparticularlysensitivetothenoisyanomalyscore,whichstemfromnoiseintheoriginaltime
series.Asthescorefluctuatesaroundthethreshold,theybecomelessrobusttonoise.Moreover,thenormal/abnormal
ratio,whichexhibitsconsiderablevariabilityacrossdifferenttasks,furtherinfluencesthethreshold.Notably,variations
inthisratiocanleadtovariationsinthethreshold,consequentlyimpactingthevaluesofthreshold-basedaccuracy
measures.Additionally,detectorsmayintroducealagintotheanomalyscore,andtheremaybeinherentlagresulting
from the approximation made during the labeling phase. Even small lags can have a significant impact on these
evaluationmeasures.Therefore,manyworksconsiderthresholdselectionasaproblemorthogonaltomodelevaluation
andusemetricsthatsummarizethemodelperformanceacrossallpossiblethresholds.Wewillintroduceseveral
threshold-independentevaluationmeasuresasfollows.
BestF-Score:MaximumF-Scoreoverallpossiblethresholds.
AUC:TheAreaUndertheReceiverOperatingCharacteristicscurve(AUC-ROC)[66]isawidelyusedevaluation
ManuscriptsubmittedtoACM

40 Paparrizosetal.
metricinanomalydetection,aswellasinbinaryclassificationingeneral.Itquantifiestheperformanceofamodel
bymeasuringtheareaunderthecurvethatrepresentsthetruepositiverate(TPR)onthey-axisagainstthefalse
positiverate(FPR)onthex-axis,asdepictedinFigure22(b.1).AUC-ROCrepresentstheprobabilitythatarandomly
chosenpositiveexamplewillberankedhigherthanarandomlychosennegativeexample.Itiscomputedusingthe
trapezoidalrule.Forthatpurpose,wedefineanorderedsetofthresholds,denotedas𝑇ℎ,rangingfrom0to1,where
𝑇ℎ= [𝑇ℎ
0
,𝑇ℎ
1
,...𝑇ℎ 𝑁]with0=𝑇ℎ
0
<𝑇ℎ
1
<...<𝑇ℎ
𝑁
=1.Therefore,𝐴𝑈𝐶-𝑅𝑂𝐶isdefinedasfollows:
𝑁
𝐴𝑈𝐶-𝑅𝑂𝐶 = 1∑︁ Δ
𝑇
𝑘
𝑃𝑅
∗Δ𝑘
𝐹𝑃𝑅
2
𝑘=1
(19)
 Δ𝑘 𝐹𝑃𝑅 =𝐹𝑃𝑅(𝑇ℎ 𝑘)−𝐹𝑃𝑅(𝑇ℎ 𝑘−1 )
with:
 Δ 𝑇 𝑘 𝑃𝑅 =𝑇𝑃𝑅(𝑇ℎ 𝑘−1 )+𝑇𝑃𝑅(𝑇ℎ 𝑘)

TheAreaUnderthePrecision-Recallcurve(AUC-PR)[58]issimilar,butwiththeRecall(TPR)onthex-axisand
Precisiononthey-axis.ThePrecisionandFPRexhibitdistinctresponsestochangesinfalsepositivesinthecontextof
anomalydetection.Inthisdomain,thenumberoftruenegativestendstobesubstantiallylargerthanthenumberof
falsepositives,resultinginlowFPRvaluesforvariousthresholdchoicesthatarerelevant.Consequently,onlyasmall
portionoftheROCcurveholdsrelevanceundersuchcircumstances.Onepotentialapproachtoaddressthisissueisto
focussolelyonspecificsegmentsofthecurve[10].Alternatively,theuseoftheAUC-PRhasbeenadvocatedasamore
informativealternativetoROCforimbalanceddatasets[145].
Range-AUC:AUC-ROCandAUC-PRareprimarilydesignedforpoint-basedanomalies,treatingeachpointinde-
pendentlyandassigningequalweighttothedetectionofeachpointincalculatingtheoverallAUC.However,these
metricsmaynotbeidealforassessingsubsequenceanomalies.Thereareseveralreasonsforthislimitation,including
theimportanceofdetectingevensmallsegmentswithinsubsequenceoutliers,theabsenceofconsistentlabelingcon-
ventionsacrossdatasets,especiallyforsubsequences,andthesensitivityoftheanomalyscorestotimelagsintroduced
bydetectors.Toaddresstheselimitations,anextensionoftheROCandPRcurvescalledRange-AUC[180]hasbeen
introducedspecificallyforsubsequences.Byaddingabufferregionattheoutliers’boundariesasshowninFigure
22(b.2),itaccountsforthefalsetoleranceoflabelinginthegroundtruthandassignshigheranomalyscoresnearthe
outlierboundaries.Itreplacesbinarylabelswithcontinuousvaluesintherange[0,1].Thisrefinementenablesthe
adaptationofpoint-basedTPR,FPR,andPrecisiontobettersuitsubsequenceanomalycases.
VolumeUndertheSurface(VUS)[180]:ThebufferlengthinRange-AUC,denotedas𝑙,needstobepredefined.Ifnot
properlyset,itcanstronglyinfluencerange-AUCmeasures.Toeliminatethisinfluence,VUScomputesRange-AUC
fordifferentbufferlengthsfrom0tothe𝑙,whichleadstothecreationofathree-dimensionalsurfaceintheROC-PR
spaceasshowninFigure22(b.3).TheVUSfamilyofmeasures,includingVUS-ROCandVUS-PR,areparameter-free
andthreshold-independent,applicableforevaluatingbothpoint-basedandrange-basedanomalies.
Differentevaluationmethodshavedifferentproperties,includingrobustnesstolagandnoise,theseparabilityto
differentiatebetweenaccurateandinaccuratemethods,andtheneedforparameters,etc.Therefore,theselectionof
evaluationmetricsshouldbeapproachedwithcaution,consideringthespecificrequirementsofthetask.Fordetailed
casestudieshighlightingthepropertiesofdifferentmetrics,werecommendreferringtothefollowingpapers[180,229].
Intermsofkeytakeaways,werecommendutilizingthreshold-independentevaluationmeasurestomitigatepotential
biasesintroducedbythresholdselection.AUC-basedmeasureshavebeenwidelyadoptedinthisregard.However,their
limitationslieinthelackofconsiderationfortheconsistencyoftimeseries.Toaddressthis,Range-AUChasrefined
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 41
theAUC-basedmeasures.Amongtherange-basedmeasures,VUS-ROCstandsoutforitsrobustness,separability,
andconsistencyinrankingtheaccuracyofdetectorsacrossdiversedatasets,makingitarecommendedchoiceasthe
evaluationmeasureofpreference.
11 Conclusions
Inthissurvey,weexaminedintotheanomalydetectionproblemintimeseries.Westartedbydefiningataxonomyof
timeseriestypes,anomalytypes,andanomalydetectionmethods.Wegroupedthemethodsintomultipleprocess-centric
categories.Wethendescribedthemostpopularanomalydetectionmethodsforeachcategoryindetail,andprovidedan
extensivelistofotherexistingmethods.Wefinallydiscussedtheproblemofbenchmarkingandevaluationofanomaly
detectionmethodsintimeseries.Weinitiatedthisdiscussionbylistingthetimeseriesdatasetandbenchmarkproposed
intheliterature.Wethenlistedthetraditionalevaluationmeasuresusedtoassessthedetectionquality,discussedtheir
limitations,andintroducedarecentefforttoadaptthesemeasurestothecontextoftimeseries.
Despitethedecades-longworthofresearchinthisarea,time-seriesanomalydetectionremainsachallengingproblem.
Several communities have tackled the problem separately, introducing methods that follow their corresponding
fundamentalconcepts.Sincethesemethodswerenotcomparedonthesamebasis(i.e.,usingthesameevaluation
measuresanddatasets),theprogressofanomalydetectionmethodshasbeenchallengingtoassess.However,therecent
effortsinproposingbenchmarks[113,185]hashelpedtoevaluatetheprogressandidentifyappropriatemethodsfor
specificproblems[185,216].
Nevertheless,multipleresearchdirectionsremainopen.First,thereisnoagreementyetonasinglebenchmark
thattheentirecommunityshoulduse.Eventhoughnumerousbenchmarkshavebeenproposed,theyhavetheirown
limitationsconcerningthediversityoftimeseries,anomalytypes,oruncertainlabels.Thereisaneedtoagreeasa
communityonacommonbasisforcomparingtheanomalydetectionmethods.
Second,encouragedbythecurrentmomentum,manynovelmethodsareproposedeveryyear.However,recent
evaluationssuggested[185,216]thatnosinglebestmethodexists(i.e.,achievingthebestperformanceoneverydataset).
Thisobservationopensanewdirectionofresearchtowardsensembling,modelselection,andAutoML.Arecent
experimentalevaluation[235]concludedthatsimpletimeseriesclassificationbaselinescanbeusedformodelselection
fortime-seriesanomalydetection,leadingtoaccuracyimprovementsbyafactorof2comparedtothebestperforming
individualanomalydetectionmethod.Thisstudysuggeststhatwecanbeoptimisticaboutfurtherimprovementsin
accuracy,bycontinuingtheresearchinthisdirection.
Finally,eventhoughalargenumberofunsupervisedmethodshavebeenproposedforunivariatetime-seriesanomaly
detection,notmuchattentionhasbeenpaidtomultivariatetimeseries,streamingtimeseries,serieswithmissing
values,serieswithnon-continuoustimestamps,heterogeneoustimeseries,oracombinationoftheabove.Suchtimes
seriesareoftenencounteredinpractice,thusweneedrobustandaccuratemethodsforthesecases,aswell.
References
[1] AliAbdul-Aziz,MarkWoike,NikunjOza,BryanMatthews,andGeorgeBaakilini.2010.Propulsionhealthmonitoringofaturbineenginedisk
usingspintestdata.InHealthMonitoringofStructuralandBiologicalSystems2010,TribikramKundu(Ed.),Vol.7650.InternationalSocietyfor
OpticsandPhotonics,SPIE,431–440. https://doi.org/10.1117/12.847574
[2] CharuCAggarwal.2017.Anintroductiontooutlieranalysis.InOutlieranalysis.Springer,1–34.
[3] SubutaiAhmad,AlexanderLavin,ScottPurdy,andZuhaAgha.2017.UnsupervisedReal-TimeAnomalyDetectionforStreamingData.262(2017),
134–147. https://doi.org/10.1016/j.neucom.2017.04.070
[4] ShadabAlam,FrancoDAlbareti,CarlosAllendePrieto,FriedrichAnders,ScottFAnderson,TimothyAnderton,BrettHAndrews,EricArmengaud,
ÉricAubourg,StephenBailey,etal.2015.TheeleventhandtwelfthdatareleasesoftheSloanDigitalSkySurvey:finaldatafromSDSS-III.The
ManuscriptsubmittedtoACM

42 Paparrizosetal.
AstrophysicalJournalSupplementSeries219,1(2015),12.
[5] MuhammadQasimAli,EhabAl-Shaer,HassanKhan,andSyedAliKhayam.2013.Automatedanomalydetectoradaptationusingadaptivethreshold
tuning.ACMTransactionsonInformationandSystemSecurity(TISSEC)15,4(2013),1–30.
[6] FranciscoMartinezAlvarez,AliciaTroncoso,JoseCRiquelme,andJesusSAguilarRuiz.2010.Energytimeseriesforecastingbasedonpattern
sequencesimilarity.IEEETransactionsonKnowledgeandDataEngineering23,8(2010),1230–1243.
[7] JérômeAntoniandPietroBorghesani.2019. AStatisticalMethodologyfortheDesignofConditionIndicators. 114(2019),290–327. https:
//doi.org/10.1016/j.ymssp.2018.05.012
[8] JulienAudibert,PietroMichiardi,FrédéricGuyard,SébastienMarti,andMariaAZuluaga.2020. Usad:Unsupervisedanomalydetectionon
multivariatetimeseries.InSIGKDD.3395–3404.
[9] MartinBach-Andersen,BoRømer-Odgaard,andOleWinther.2017.Flexiblenon-linearpredictivemodelsforlarge-scalewindturbinediagnostics.
WindEnergy20,5(2017),753–764.
[10] StuartGBakerandPaulFPinsky.2001.Aproposeddesignandanalysisforcomparingdigitalandanalogmammography:specialreceiveroperating
characteristicmethodsforcancerscreening.J.Amer.Statist.Assoc.96,454(2001),421–428.
[11] ZivBar-Joseph.2004.Analyzingtimeseriesgeneexpressiondata.Bioinformatics20,16(2004),2493–2503.
[12] ZivBar-Joseph,GeorgKGerber,DavidKGifford,TommiSJaakkola,andItamarSimon.2003.Continuousrepresentationsoftime-seriesgene
expressiondata.JournalofComputationalBiology10,3-4(2003),341–356.
[13] ZivBar-Joseph,AnthonyGitter,andItamarSimon.2012.Studyingandmodellingdynamicbiologicalprocessesusingtime-seriesgeneexpression
data.NatureReviewsGenetics13,8(2012),552.
[14] MohiniBariya,AlexandravonMeier,JohnPaparrizos,andMichaelJFranklin.2021.k-ShapeStream:ProbabilisticStreamingClusteringforElectric
GridEvents.In2021IEEEMadridPowerTech.IEEE,1–6.
[15] V.BarnetandT.Lewis.1994.OutliersinStatisticalData.JohnWileyandSons,Inc.
[16] VicBarnettandTobyLewis.1984. Outliersinstatisticaldata. WileySeriesinProbabilityandMathematicalStatistics.AppliedProbabilityand
Statistics(1984).
[17] MdAbulBasharandRichiNayak.2020.TAnoGAN:Timeseriesanomalydetectionwithgenerativeadversarialnetworks.InSSCI.IEEE,1778–1785.
[18] SabyasachiBasuandMartinMeckesheimer.2007. AutomaticOutlierDetectionforTimeSeries:AnApplicationtoSensorData. 11,2(2007),
137–154. https://doi.org/10.1007/s10115-006-0026-6
[19] DanielBernoulliandCGAllen.1961.Themostprobablechoicebetweenseveraldiscrepantobservationsandtheformationtherefromofthemost
likelyinduction.Biometrika48,1-2(1961),3–18.
[20] ArpitaBhargavaandASRaghuvanshi.2013.AnomalydetectioninwirelesssensornetworksusingS-TransformincombinationwithSVM.In2013
5thInternationalConferenceandComputationalIntelligenceandCommunicationNetworks.IEEE,111–116.
[21] BharatBBiswal,MaartenMennes,Xi-NianZuo,SurilGohel,ClareKelly,SteveMSmith,ChristianFBeckmann,JonathanSAdelstein,RandyL
Buckner,StanColcombe,etal.2010.Towarddiscoveryscienceofhumanbrainfunction.ProceedingsoftheNationalAcademyofSciences107,10
(2010),4734–4739.
[22] AneBlázquez-García,AngelConde,UsueMori,andJoseALozano.2021. Areviewonoutlier/anomalydetectionintimeseriesdata. ACM
ComputingSurveys(CSUR)54,3(2021),1–33.
[23] PaulBoniol,MicheleLinardi,FedericoRoncallo,andThemisPalpanas.2020.AutomatedAnomalyDetectioninLargeSequences.InProceedingsof
theInternationalConferenceonDataEngineering(ICDE).1834–1837. https://doi.org/10.1109/ICDE48307.2020.00182
[24] PaulBoniol,MicheleLinardi,FedericoRoncallo,andThemisPalpanas.2020.SAD:AnUnsupervisedSystemforSubsequenceAnomalyDetection.
InProceedingsoftheInternationalConferenceonDataEngineering(ICDE).1778–1781. https://doi.org/10.1109/ICDE48307.2020.00168
[25] PaulBoniol,MicheleLinardi,FedericoRoncallo,ThemisPalpanas,MohammedMeftah,andEmmanuelRemy.2021.Unsupervisedandscalable
subsequenceanomalydetectioninlargedataseries.TheVLDBJournal(March2021). https://doi.org/10.1007/s00778-021-00655-8
[26] PaulBoniolandThemisPalpanas.2020. Series2Graph:Graph-BasedSubsequenceAnomalyDetectionforTimeSeries. 13,11(2020),14.
https://doi.org/10.14778/3407790.3407792
[27] PaulBoniol,JohnPaparrizos,YuhaoKang,ThemisPalpanas,RueySTsay,AaronJElmore,andMichaelJFranklin.2022.Theseus:navigatingthe
labyrinthoftime-seriesanomalydetection.ProceedingsoftheVLDBEndowment15,12(2022),3702–3705.
[28] PaulBoniol,JohnPaparrizos,andThemisPalpanas.2023.NewTrendsinTimeSeriesAnomalyDetection..InEDBT.847–850.
[29] PaulBoniol,JohnPaparrizos,andThemisPalpanas.2024.AnInteractiveDiveintoTime-SeriesAnomalyDetection.In2024IEEE40thInternational
ConferenceonDataEngineering(ICDE).
[30] PaulBoniol,JohnPaparrizos,ThemisPalpanas,andMichaelJFranklin.2021.Sandinaction:subsequenceanomalydetectionforstreams.Proceedings
oftheVLDBEndowment14,12(2021),2867–2870.
[31] PaulBoniol,JohnPaparrizos,ThemisPalpanas,andMichaelJFranklin.2021.SAND:streamingsubsequenceanomalydetection.PVLDB14,10
(2021),1717–1729.
[32] PaulBoniol,EmmanouilSylligardos,JohnPaparrizos,PanosTrahanias,andThemisPalpanas.2024.ADecimo:ModelSelectionforTimeSeries
AnomalyDetection.In2024IEEE40thInternationalConferenceonDataEngineering(ICDE).
[33] MohammadBraeiandSebastianWagner.2020. Anomalydetectioninunivariatetime-series:Asurveyonthestate-of-the-art. arXivpreprint
arXiv:2004.00433(2020).
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 43
[34] MarkusMBreunig,Hans-PeterKriegel,RaymondTNg,andJörgSander.2000.LOF:identifyingdensity-basedlocaloutliers.InProceedingsofthe
2000ACMSIGMODinternationalconferenceonManagementofdata.93–104.
[35] MarkusM.Breunig,Hans-PeterKriegel,RaymondT.Ng,andJörgSander.2000.LOF:IdentifyingDensity-basedLocalOutliers.InSIGMOD.
[36] PeterJBrockwellandRichardADavis.2016.Introductiontotimeseriesandforecasting.springer.
[37] YingyiBu,OscarTat-WingLeung,AdaWai-CheeFu,EamonnJ.Keogh,JianPei,andSamMeshkin.2007.WAT:FindingTop-KDiscordsinTime
SeriesDatabase.InSIAM.
[38] SuratnaBudalakoti,AshokNSrivastava,andMatthewEricOtey.2008.Anomalydetectionanddiagnosisalgorithmsfordiscretesymbolsequences
withapplicationstoairlinesafety.IEEETransactionsonSystems,Man,andCybernetics,PartC(ApplicationsandReviews)39,1(2008),101–113.
[39] C.Bui,N.Pham,A.Vo,A.Tran,A.Nguyen,andT.Le.2018.TimeSeriesForecastingforHealthcareDiagnosisandPrognosticswiththeFocus
onCardiovascularDiseases.InInternationalConferenceontheDevelopmentofBiomedicalEngineeringinVietnam(BME6).SpringerSingapore,
Singapore,809–818.
[40] AnderCarreño,IñakiInza,andJoseALozano.2020.Analyzingrareevent,anomaly,noveltyandoutlierdetectiontermsunderthesupervised
classificationframework.ArtificialIntelligenceReview53,5(2020),3575–3594.
[41] MeteCelik,FilizDadaser-Celik,andAhmetSakirDokuz.2011.AnomalydetectionintemperaturedatausingDBSCANalgorithm.2011International
SymposiumonInnovationsinIntelligentSystemsandApplications(2011),91–95.
[42] SoumenChakrabarti,SunitaSarawagi,andByronDom.1998.MiningSurprisingPatternsUsingTemporalDescriptionLength.InProceedingsofthe
InternationalConferenceonVeryLargeDatabases(VLDB)(VLDB’98,Vol.24).MorganKaufmannPublishersInc.,606–617. https://dl.acm.org/doi/10.
5555/645924.671328
[43] RaghavendraChalapathyandSanjayChawla.2019.DeepLearningforAnomalyDetection:ASurvey.arXiv:1901.03407[cs,stat] http://arxiv.org/
abs/1901.03407
[44] RaghavendraChalapathy,AdityaKrishnaMenon,andSanjayChawla.2017.Robust,DeepandInductiveAnomalyDetection.InMachineLearning
andKnowledgeDiscoveryinDatabases,MichelangeloCeci,JaakkoHollmén,LjupčoTodorovski,CelineVens,andSašoDžeroski(Eds.).Springer
InternationalPublishing,Cham,36–51.
[45] VarunChandola,ArindamBanerjee,andVipinKumar.2009.Anomalydetection:Asurvey.ACMcomputingsurveys(CSUR)41,3(2009),1–58.
[46] VarunChandola,ArindamBanerjee,andVipinKumar.2009.AnomalyDetection:ASurvey.41,3(2009),1–58. https://doi.org/10.1145/1541880.
1541882
[47] V.Chandola,A.Banerjee,andV.Kumar.2012.AnomalyDetectionforDiscreteSequences:ASurvey.24,5(2012),823–839. https://doi.org/10.
1109/TKDE.2010.235
[48] IhChang,GeorgeCTiao,andChungChen.1988.Estimationoftimeseriesparametersinthepresenceofoutliers.Technometrics30,2(1988),
193–204.
[49] MarcusChang,AndreasTerzis,andPhilippeBonnet.2009.Mote-BasedOnlineAnomalyDetectionUsingEchoStateNetworks.InProceedingsofthe
InternationalConferenceonDistributedComputinginSensorSystems(DCOOS)(LectureNotesinComputerScience,Vol.5516),BhaskarKrishnamachari,
SubhashSuri,WendiHeinzelman,andUrbashiMitra(Eds.).SpringerBerlinHeidelberg,72–86. https://doi.org/10.1007/978-3-642-02085-8_6
[50] S.ChauhanandL.Vig.2015. AnomalyDetectioninECGTimeSignalsviaDeepLongShort-TermMemoryNetworks.InProceedingsofthe
InternationalConferenceonDataScienceandAdvancedAnalytics(DSAA).1–7. https://doi.org/10.1109/DSAA.2015.7344872
[51] QingChen,AnguoZhang,TingwenHuang,QianpingHe,andYongduanSong.2020.ImbalancedDataset-BasedEchoStateNetworksforAnomaly
Detection.32,8(2020),3685–3694. https://doi.org/10.1007/s00521-018-3747-z
[52] Run-QingChen,Guang-HuiShi,Wan-LeiZhao,andChang-HuiLiang.2021.AjointmodelforIToperationseriespredictionandanomalydetection.
Neurocomputing448(2021),130–139.
[53] ZhangyuCheng,ChengmingZou,andJianweiDong.2019.OutlierDetectionUsingIsolationForestandLocalOutlierFactor.InProceedingsofthe
ConferenceonResearchinAdaptiveandConvergentSystems(RACS).ACM,161–168. https://doi.org/10.1145/3338840.3355641
[54] DhruvChoudhary,ArunKejariwal,andFrancoisOrsini.2017.OntheRuntime-EfficacyTrade-offofAnomalyDetectionTechniquesforReal-Time
StreamingData.arXiv:1710.04735[cs,eess,stat] http://arxiv.org/abs/1710.04735
[55] WilliamW.Cohen.1995.FastEffectiveRuleInduction.InMachineLearningProceedings1995,ArmandPrieditisandStuartRussell(Eds.).Morgan
Kaufmann,SanFrancisco(CA),115–123. https://doi.org/10.1016/B978-1-55860-377-6.50023-2
[56] AndrewA.Cook,GokselMisirli,andZhongFan.2020. AnomalyDetectionforIoTTime-SeriesData:ASurvey. 7,7(2020),6481–6494.
https://doi.org/10.1109/JIOT.2019.2958185
[57] MadalenaCosta,AryLGoldberger,andC-KPeng.2002.Multiscaleentropyanalysisofcomplexphysiologictimeseries.Physicalreviewletters89,
6(2002),068102.
[58] JesseDavisandMarkGoadrich.2006.TherelationshipbetweenPrecision-RecallandROCcurves.InICML.233–240.
[59] NanDing,HuanboGao,HongyuBu,HaoxuanMa,andHuaiweiSi.2018.Multivariate-Time-Series-DrivenReal-TimeAnomalyDetectionBasedon
BayesianNetwork.18,10(2018),3367. https://doi.org/10.3390/s18103367
[60] WilfredJDixon.1950.Analysisofextremevalues.TheAnnalsofMathematicalStatistics21,4(1950),488–506.
[61] AdamDziedzic,JohnPaparrizos,SanjayKrishnan,AaronElmore,andMichaelFranklin.2019.Band-limitedtrainingandinferenceforconvolutional
neuralnetworks.InICML.PMLR,1745–1754.
ManuscriptsubmittedtoACM

44 Paparrizosetal.
[62] JensEd’Hondt,OdysseasPapapetrou,andJohnPaparrizos.2024.BeyondtheDimensions:AStructuredEvaluationofMultivariateTimeSeries
DistanceMeasures.In2024IEEE40thInternationalConferenceonDataEngineeringWorkshops(ICDEW).IEEE,107–112.
[63] FrancisYsidroEdgeworth.1887.Xli.ondiscordantobservations.Thelondon,edinburgh,anddublinphilosophicalmagazineandjournalofscience23,
143(1887),364–375.
[64] JasonErnstandZivBar-Joseph.2006.STEM:atoolfortheanalysisofshorttimeseriesgeneexpressiondata.BMCbioinformatics7,1(2006),191.
[65] PhilippeEslingandCarlosAgon.2012.Time-seriesdatamining.ACMComputingSurveys(CSUR)45,1(2012),12.
[66] TomFawcett.2006.AnintroductiontoROCanalysis.PatternRecognitionLetters27,8(2006),861–874. https://doi.org/10.1016/j.patrec.2005.10.010
ROCAnalysisinPatternRecognition.
[67] PavelFilonov,AndreyLavrentyev,andArtemVorontsov.2016.Multivariateindustrialtimeserieswithcyber-attacksimulation:Faultdetection
usinganlstm-basedpredictivedatamodel.arXivpreprintarXiv:1612.06676(2016).
[68] RalphFoorthuis.2020.OntheNatureandTypesofAnomalies:AReview.arXivpreprintarXiv:2007.15634(2020).
[69] AnthonyJFox.1972.Outliersintimeseries.JournaloftheRoyalStatisticalSociety:SeriesB(Methodological)34,3(1972),350–363.
[70] AdaWai-CheeFu,OscarTat-WingLeung,EamonnJ.Keogh,andJessicaLin.2006.FindingTimeSeriesDiscordsBasedonHaarTransform.In
ADMA.
[71] YifengGao,JessicaLin,andConstantinBrif.2020.EnsembleGrammarInductionForDetectingAnomaliesinTimeSeries.InProceedingsofthe
InternationalConferenceonExtendingDatabaseTechnology(EDBT). https://doi.org/10.5441/002/edbt.2020.09
[72] GabrielGarcia,GabrielMichau,MélanieDucoffe,JayantSenGupta,andOlgaFink.2020.TimeSeriestoImages:MonitoringtheConditionof
IndustrialAssetswithDeepLearningImageProcessingAlgorithms.(052020).
[73] GabrielRodriguezGarcia,GabrielMichau,MélanieDucoffe,JayantSenGupta,andOlgaFink.2020.TimeSeriestoImages:MonitoringtheCondition
ofIndustrialAssetswithDeepLearningImageProcessingAlgorithms.arXiv:2005.07031[cs,eess,stat] http://arxiv.org/abs/2005.07031
[74] MartinGavrilov,DragomirAnguelov,PiotrIndyk,andRajeevMotwani.2000.Miningthestockmarket:Whichmeasureisbest.InProc.ofthe6th
ACMSIGKDD.487–496.
[75] SamGeorge.2019.IoTSignalsreport:IoT’spromisewillbeunlockedbyaddressingskillsshortage,complexityandsecurity. https://blogs.microsoft.
com/blog/2019/07/30/.
[76] JWLGlaisher.1873.Ontherejectionofdiscordantobservations.MonthlyNoticesoftheRoyalAstronomicalSociety33(1873),391–402.
[77] SteveGoddard,SherriKHarms,StephenEReichenbach,TsegayeTadesse,andWilliamJWaltman.2003.Geospatialdecisionsupportfordrought
riskmanagement.Commun.ACM46,1(2003),35–37.
[78] RahulGoel,SandeepSoni,NamanGoyal,JohnPaparrizos,HannaWallach,FernandoDiaz,andJacobEisenstein.2016.Thesocialdynamicsof
languagechangeinonlinenetworks.InSocialInformatics:8thInternationalConference,SocInfo2016,Bellevue,WA,USA,November11-14,2016,
Proceedings,PartI8.Springer,41–57.
[79] MarkusGoldsteinandAndreasDengel.2013.Histogram-basedOutlierScore(HBOS):AfastUnsupervisedAnomalyDetectionAlgorithm.
[80] MarkusGoldsteinandSeiichiUchida.2016.Acomparativeevaluationofunsupervisedanomalydetectionalgorithmsformultivariatedata.PloS
one11,4(2016),e0152173.
[81] VanessaGómez-Verdejo,JerónimoArenas-García,MiguelLazaro-Gredilla,andÁngelNavia-Vazquez.2011.Adaptiveone-classsupportvector
machine.IEEETransactionsonSignalProcessing59,6(2011),2975–2981.
[82] IanGoodfellow,JeanPouget-Abadie,MehdiMirza,BingXu,DavidWarde-Farley,SherjilOzair,AaronCourville,andYoshuaBengio.2014.Generative
adversarialnets.NeurIPS27(2014).
[83] BAGould.1855.OnPeirce’sCriterionfortheRejectionofDoubtfulObservations,withtablesforfacilitatingitsapplication.TheAstronomical
Journal4(1855),81–87.
[84] AdityaGrover,AshishKapoor,andEricHorvitz.2015.Adeephybridmodelforweatherforecasting.InProceedingsofthe21thACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining.ACM,379–386.
[85] FrankEGrubbs.1950.Samplecriteriafortestingoutlyingobservations.TheAnnalsofMathematicalStatistics(1950),27–58.
[86] ManishGupta,JingGao,CharuC.Aggarwal,andJiaweiHan.2014. OutlierDetectionforTemporalData:ASurvey. 26,9(2014),2250–2267.
https://doi.org/10.1109/TKDE.2013.184
[87] NicoGörnitz,MikioBraun,andMariusKloft.2015.HiddenMarkovAnomalyDetection.InProceedingsoftheInternationalConferenceonMachine
Learning(ICML)(ICML’15).JMLR.org,1833–1842. https://dl.acm.org/doi/10.5555/3045118.3045313
[88] MichaelHahslerandMatthewBolaos.2016.ClusteringDataStreamsBasedonSharedDensitybetweenMicro-Clusters.IEEETrans.onKnowl.and
DataEng.28,6(jun2016),1449–1461. https://doi.org/10.1109/TKDE.2016.2522412
[89] JohannaHardinandDavidMRocke.2004.Outlierdetectioninthemultipleclustersettingusingtheminimumcovariancedeterminantestimator.
ComputationalStatistics&DataAnalysis44,4(2004),625–638. https://doi.org/10.1016/S0167-9473(02)00280-3
[90] SahandHariri,MatiasCarrascoKind,andRobertJ.Brunner.2019.ExtendedIsolationForest.(2019). https://doi.org/10.1109/TKDE.2019.2947676
arXiv:1811.02141
[91] D.MHawkins.1980.IdentificationofOutliers.SpringerNetherlands,Dordrecht. OCLC:945065134.
[92] JeffHawkinsandRichardDawkins.2021.Athousandbrains:anewtheoryofintelligence.(2021).
[93] ZengyouHe,XiaofeiXu,andShengchunDeng.2003.Discoveringcluster-basedlocaloutliers.Patternrecognitionletters24,9-10(2003),1641–1650.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 45
[94] M.A.Hearst,S.T.Dumais,E.Osuna,J.Platt,andB.Scholkopf.1998.Supportvectormachines.IEEEIntelligentSystemsandtheirApplications13,4
(July1998),18–28. https://doi.org/10.1109/5254.708428
[95] DonaldO.Hebb.1949.Theorganizationofbehavior:Aneuropsychologicaltheory.Wiley,NewYork.
[96] NiklasHeimandJamesE.Avery.2019. AdaptiveAnomalyDetectioninChaoticTimeSerieswithaSpatiallyAwareEchoStateNetwork.
arXiv:1909.01709[cs,stat] http://arxiv.org/abs/1909.01709
[97] Jordan Hochenbaum, Owen S. Vallis, and Arun Kejariwal. 2017. Automatic Anomaly Detection in the Cloud Via Statistical Learning.
arXiv:1704.07706[cs] http://arxiv.org/abs/1704.07706
[98] SeppHochreiterandJürgenSchmidhuber.1997.LongShort-TermMemory.NeuralComput.9,8(Nov.1997),1735–1780. https://doi.org/10.1162/
neco.1997.9.8.1735
[99] VictoriaJ.HodgeandJimAustin.2004.ASurveyofOutlierDetectionMethodologies.22,2(2004),85–126. https://doi.org/10.1007/s10462-004-4304-y
[100] OveHoegh-Guldberg,PeterJMumby,AnthonyJHooten,RobertSSteneck,PaulGreenfield,EdgardoGomez,CDrewHarvell,PeterFSale,
AlasdairJEdwards,KenCaldeira,etal.2007.Coralreefsunderrapidclimatechangeandoceanacidification.science318,5857(2007),1737–1742.
[101] RieHonda,ShuaiWang,TokioKikuchi,andOsamuKonishi.2002.Miningofmovingobjectsfromtime-seriesimagesanditsapplicationtosatellite
weatherimagery.JournalofIntelligentInformationSystems19,1(2002),79–93.
[102] PabloHuijse,PabloAEstevez,PavlosProtopapas,JoseCPrincipe,andPabloZegers.2014.Computationalintelligencechallengesandapplications
onlarge-scaleastronomicaltimeseriesdatabases.IEEEComputationalIntelligenceMagazine9,3(2014),27–39.
[103] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,andTomSoderstrom.2018.DetectingSpacecraftAnomaliesUsing
LSTMsandNonparametricDynamicThresholding.InSIGKDD.ACM,387–395. https://doi.org/10.1145/3219819.3219845
[104] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,andTomSoderstrom.2018.Detectingspacecraftanomaliesusinglstms
andnonparametricdynamicthresholding.InSIGKDD.387–395.
[105] MarkHung.2017.Leadingtheiot,gartnerinsightsonhowtoleadinaconnectedworld.GartnerResearch(2017),1–29.
[106] JOIrwin.1925.Onacriterionfortherejectionofoutlyingobservations.Biometrika(1925),238–250.
[107] AlanJulianIzenman.2008.Modernmultivariatestatisticaltechniques.Regression,classificationandmanifoldlearning10(2008),978–0.
[108] VincentJacob,FeiSong,ArnaudStiegler,BijanRad,YanleiDiao,andNesimeTatbul.2021.Exathlon:abenchmarkforexplainableanomalydetection
overtimeseries.PVLDB14,11(2021),2613–2626.
[109] HoyoungJeung,SofianeSarni,IoannisPaparrizos,SaketSathe,KarlAberer,NicholasDawes,ThanasisGPapaioannou,andMichaelLehning.
2010.Effectivemetadatamanagementinfederatedsensornetworks.In2010IEEEInternationalConferenceonSensorNetworks,Ubiquitous,and
TrustworthyComputing.IEEE,107–114.
[110] HaoJiang,ChunweiLiu,QiJin,JohnPaparrizos,andAaronJElmore.2020.Pids:attributedecompositionforimprovedcompressionandquery
performanceincolumnarstorage.Proc.VLDBEndow13,6(2020),925–938.
[111] HaoJiang,ChunweiLiu,JohnPaparrizos,AndrewAChien,JihongMa,andAaronJElmore.2021.GoodtotheLastBit:Data-DrivenEncoding
withCodecDB.InSIGMOD.843–856.
[112] KunioKashino,GavinSmith,andHiroshiMurase.1999.Time-seriesactivesearchforquickretrievalofaudioandvideo.In1999IEEEInternational
ConferenceonAcoustics,Speech,andSignalProcessing.Proceedings.ICASSP99(Cat.No.99CH36258),Vol.6.IEEE,2993–2996.
[113] E.Keogh,T.DuttaRoy,U.Naik,andAAgrawal.2021.Multi-datasetTime-SeriesAnomalyDetectionCompetition2021,https://compete.hexagon-
ml.com/practice/competition/39/.
[114] EamonnKeogh,JessicaLin,andAdaFu.2005.Hotsax:Efficientlyfindingthemostunusualtimeseriessubsequence.InFifthIEEEInternational
ConferenceonDataMining(ICDM’05).Ieee,8–pp.
[115] EamonnKeogh,StefanoLonardi,andBill’Yuan-chi’Chiu.2002.Findingsurprisingpatternsinatimeseriesdatabaseinlineartimeandspace.In
ProceedingsoftheeighthACMSIGKDDinternationalconferenceonKnowledgediscoveryanddatamining.550–556.
[116] EamonnKeogh,StefanoLonardi,ChotiratAnnRatanamahatana,LiWei,Sang-HeeLee,andJohnHandley.2007.Compression-baseddatamining
ofsequentialdata.DataMiningandKnowledgeDiscovery(2007).
[117] ChunggyeomKim,JinhyukLee,RaehyunKim,YoungbinPark,andJaewooKang.2018. DeepNAP:DeepNeuralAnomalyPre-Detectionina
SemiconductorFab.457-458(2018),1–11. https://doi.org/10.1016/j.ins.2018.05.020
[118] SiwonKim,KukjinChoi,Hyun-SooChoi,ByunghanLee,andSungrohYoon.2022.Towardsarigorousevaluationoftime-seriesanomalydetection.
InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.36.7194–7201.
[119] SKnieling,JNiediek,EKutter,JBostroem,CEElger,andFMormann.2017. Anonlineadaptivescreeningprocedureforselectiveneuronal
responses.Journalofneurosciencemethods291(2017),36–42.
[120] MariaKontaki,AnastasiosGounaris,ApostolosNPapadopoulos,KostasTsichlas,andYannisManolopoulos.2011.Continuousmonitoringof
distance-basedoutliersoverdatastreams.In2011IEEE27thInternationalConferenceonDataEngineering.IEEE,135–146.
[121] PeterKrenskyandJimHare.2018.HypeCycleforDataScienceandMachineLearning,2018.GartnerCompany(2018).
[122] SanjayKrishnan,AaronJElmore,MichaelFranklin,JohnPaparrizos,ZechaoShang,AdamDziedzic,andRuiLiu.2019.Artificialintelligencein
resource-constrainedandsharedenvironments.ACMSIGOPSOperatingSystemsReview53,1(2019),1–6.
[123] Kwei-HerngLai,DaochenZha,JunjieXu,YueZhao,GuanchuWang,andXiaHu.2021.RevisitingTimeSeriesOutlierDetection:Definitionsand
Benchmarks.InNeurIPS.
ManuscriptsubmittedtoACM

46 Paparrizosetal.
[124] BouchraLamrini,AugustinGjini,SimonDaudin,PascalPratmarty,FrançoisArmando,andLouiseTravé-Massuyès.2018.AnomalyDetection
usingSimilarity-basedOne-ClassSVMforNetworkTrafficCharacterization..InDX.
[125] N.Laptev,S.Amizadeh,andY.Billawala.2015.S5-ALabeledAnomalyDetectionDataset,version1.0(16M). https://webscope.sandbox.yahoo.com/
catalog.php?datatype=s&did=70
[126] AlexanderLavinandSubutaiAhmad.2015.Evaluatingreal-timeanomalydetectionalgorithms–theNumentaanomalybenchmark.InICMLA.
IEEE,38–44.
[127] Ming-ChangLee,Jia-ChunLin,andErnstGunnarGran.2020. RePAD:Real-TimeProactiveAnomalyDetectionforTimeSeries.InAINA,
LeonardBarolli,FloraAmato,FrancescoMoscato,TomoyaEnokido,andMakotoTakizawa(Eds.).SpringerInternationalPublishing,1291–1302.
https://doi.org/10.1007/978-3-030-44041-1_110
[128] DanLi,DachengChen,JonathanGoh,andSee-KiongNg.2018.AnomalyDetectionwithGenerativeAdversarialNetworksforMultivariateTime
Series.CoRRabs/1809.04758(2018).arXiv:1809.04758 http://arxiv.org/abs/1809.04758
[129] DanLi,DachengChen,BaihongJin,LeiShi,JonathanGoh,andSee-KiongNg.2019.MAD-GAN:Multivariateanomalydetectionfortimeseries
datawithgenerativeadversarialnetworks.InInternationalconferenceonartificialneuralnetworks.Springer,703–716.
[130] ZeyanLi,WenxiaoChen,andDanPei.2018.RobustandUnsupervisedKPIAnomalyDetectionBasedonConditionalVariationalAutoencoder.In
ProceedingsoftheInternationalPerformanceComputingandCommunicationsConference(IPCCC).IEEE,1–9. https://doi.org/10.1109/PCCC.2018.
8710885
[131] ZhihuaLi,ZiyuanLi,NingYu,StevenWen,etal.2017.Locality-basedvisualoutlierdetectionalgorithmfortimeseries.SecurityandCommunication
Networks2017(2017).
[132] ZhiLi,HongMa,andYongbingMei.2007.AUnifyingMethodforOutlierandChangeDetectionfromDataStreamsBasedonLocalPolynomial
Fitting.InAdvancesinKnowledgeDiscoveryandDataMining,Zhi-HuaZhou,HangLi,andQiangYang(Eds.).SpringerBerlinHeidelberg,Berlin,
Heidelberg,150–161.
[133] ZhengLi,YueZhao,NicolaBotta,CezarIonescu,andXiyangHu.2020.COPOD:Copula-BasedOutlierDetection.InIEEEInternationalConference
onDataMining(ICDM).IEEE.
[134] MicheleLinardi,YanZhu,ThemisPalpanas,andEamonnKeogh.2018. MatrixProfileX:VALMOD-ScalableDiscoveryofVariable-Length
MotifsinDataSeries.InProceedingsoftheInternationalConferenceonManagementofData(SIGMOD)(2018).ACMPress,1053–1066. https:
//doi.org/10.1145/3183713.3183744
[135] MicheleLinardi,YanZhu,ThemisPalpanas,andEamonnKeogh.2020.MatrixprofilegoesMAD:variable-lengthmotifanddiscorddiscoveryin
dataseries.DataMiningandKnowledgeDiscovery34(2020),1022–1071.
[136] MicheleLinardi,YanZhu,ThemisPalpanas,andEamonnJ.Keogh.2020.MatrixProfileGoesMAD:Variable-LengthMotifAndDiscordDiscovery
inDataSeries.InDAMI.
[137] ChunweiLiu,HaoJiang,JohnPaparrizos,andAaronJElmore.2021.Decomposedboundedfloatsforfastcompressionandqueries.Proc.VLDB
Endow14,11(2021),2586–2598.
[138] ChunweiLiu,JohnPaparrizos,andAaronJElmore.2024.Adaedge:Adynamiccompressionselectionframeworkforresourceconstraineddevices.
In2024IEEE40thInternationalConferenceonDataEngineering(ICDE).IEEE,1506–1519.
[139] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.2008.IsolationForest.InProceedingsoftheInternationalConferenceonDataMining(ICDM).IEEE,
413–422. https://doi.org/10.1109/ICDM.2008.17
[140] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.2008.Isolationforest.InICDM.IEEE,413–422.
[141] QinghuaLiu,PaulBoniol,ThemisPalpanas,andJohnPaparrizos.2024.Time-SeriesAnomalyDetection:OverviewandNewTrends.PVLDB17,12
(2024),4229–4232.
[142] QinghuaLiuandJohnPaparrizos.2024.TheElephantintheRoom:TowardsAReliableTime-SeriesAnomalyDetectionBenchmark.InNeurIPS
2024.
[143] ShinanLiu,TarunMangla,TedShaowang,JinjinZhao,JohnPaparrizos,SanjayKrishnan,andNickFeamster.2023.Amir:Activemultimodal
interactionrecognitionfromvideoandnetworktrafficinconnectedenvironments.ProceedingsoftheACMonInteractive,Mobile,Wearableand
UbiquitousTechnologies7,1(2023),1–26.
[144] YubaoLiu,XiuweiChen,andFeiWang.2009.EfficientDetectionofDiscordsforTimeSeriesStream.AdvancesinDataandWebManagement
(2009),629–634. http://www.springerlink.com/index/n546h380446p95r7.pdf
[145] JorgeMLobo,AlbertoJiménez-Valverde,andRaimundoReal.2008.AUC:amisleadingmeasureoftheperformanceofpredictivedistribution
models.GlobalecologyandBiogeography17,2(2008),145–151.
[146] YueLu,RenjieWu,AbdullahMueen,MariaAZuluaga,andEamonnKeogh.2022.MatrixprofileXXIV:scalingtimeseriesanomalydetectionto
trillionsofdatapointsandultra-fastarrivingdatastreams.InSIGKDD.1173–1182.
[147] WeiLuoandMarcusGallagher.2011.FasterandParameter-FreeDiscordSearchinQuasi-PeriodicTimeSeries.InAdvancesinKnowledgeDiscovery
andDataMining,JoshuaZhexueHuang,LongbingCao,andJaideepSrivastava(Eds.).
[148] HelmutLütkepohl,MarkusKrätzig,andPeterCBPhillips.2004.Appliedtimeserieseconometrics.Cambridgeuniversitypress.
[149] JunshuiMaandSimonPerkins.2003.OnlineNoveltyDetectiononTemporalSequences.InProceedingsoftheInternationalConferenceonKnowledge
DiscoveryandDataMining(SIGKDD).ACMPress,613. https://doi.org/10.1145/956750.956828
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 47
[150] JunshuiMaandSimonPerkins.2003.Time-seriesnoveltydetectionusingone-classsupportvectormachines.InProceedingsoftheInternational
JointConferenceonNeuralNetworks,2003.,Vol.3.IEEE,1741–1745.
[151] MohammadSaeidMahdavinejad,MohammadrezaRezvan,MohammadaminBarekatain,PeymanAdibi,PayamBarnaghi,andAmitPSheth.2017.
MachinelearningforInternetofThingsdataanalysis:Asurvey.DigitalCommunicationsandNetworks(2017).
[152] PankajMalhotra,AnushaRamakrishnan,GaurangiAnand,LovekeshVig,PuneetAgarwal,andGautamShroff.2016.LSTM-BasedEncoder-Decoder
forMulti-SensorAnomalyDetection.arXiv:1607.00148[cs,stat] http://arxiv.org/abs/1607.00148
[153] PankajMalhotra,LovekeshVig,GautamShroff,andPuneetAgarwal.2015.LongShortTermMemoryNetworksforAnomalyDetectioninTime
Series.InProceedingsoftheEuropeanSymposiumonArtificialNeuralNetworks,ComputationalIntelligenceandMachineLearning(ESANN),Vol.23.
http://www.elen.ucl.ac.be/Proceedings/esann/esannpdf/es2015-56.pdf
[154] PankajMalhotra,LovekeshVig,GautamShroff,PuneetAgarwal,etal.2015.LongShortTermMemoryNetworksforAnomalyDetectioninTime
Series..InEsann,Vol.2015.89.
[155] RosarioNMantegna.1999.Hierarchicalstructureinfinancialmarkets.TheEuropeanPhysicalJournalB-CondensedMatterandComplexSystems11,
1(1999),193–197.
[156] CarlaMarceau.2000.CharacterizingtheBehaviorofaProgramUsingMultiple-LengthN-Grams.InProceedingsoftheWorkshoponNewSecurity
Paradigms(NSPW).ACMPress,101–110. https://doi.org/10.1145/366173.366197
[157] Pierre-François Marteau, Saeid Soheily-Khah, and Nicolas Béchet. 2017. Hybrid Isolation Forest - Application to Intrusion Detection.
arXiv:1705.03800[cs] http://arxiv.org/abs/1705.03800
[158] FranciscoMartínez-Álvarez,AliciaTroncoso,GualbertoAsencio-Cortés,andJoséRiquelme.2015.Asurveyondataminingtechniquesappliedto
electricity-relatedtimeseriesforecasting.Energies8,11(2015),13162–13193.
[159] RobertLMasonandJohnCYoung.2002.Multivariatestatisticalprocesscontrolwithindustrialapplications.SIAM.
[160] RichardMcCleary,RichardAHay,ErrollEMeidinger,andDavidMcDowall.1980. Appliedtimeseriesanalysisforthesocialsciences. Sage
PublicationsBeverlyHills,CA.
[161] KathyMcKeown,HalDaumeIII,SnigdhaChaturvedi,JohnPaparrizos,KapilThadani,PabloBarrio,OrBiran,SuvarnaBothe,MichaelCollins,
KennethRFleischmann,etal.2016.Predictingtheimpactofscientificconceptsusingfull-textfeatures.JournaloftheAssociationforInformation
ScienceandTechnology67,11(2016),2684–2696.
[162] KatsiarynaMirylenka,VassilisChristophides,ThemisPalpanas,IoannisPefkianakis,andMartinMay.2016.Characterizinghomedeviceusage
fromwirelesstraffictimeseries.
[163] MaziarMoradiFard,ThibautThonet,andEricGaussier.2020.Deepk-Means:Jointlyclusteringwithk-Meansandlearningrepresentations.Pattern
RecognitionLetters138(2020),185–192. https://doi.org/10.1016/j.patrec.2020.07.028
[164] AMorales-Esteban,FranciscoMartínez-Álvarez,ATroncoso,JLJusto,andCristinaRubio-Escudero.2010.Patternrecognitiontoforecastseismic
timeseries.ExpertSystemswithApplications37,12(2010),8333–8342.
[165] CristinaMorariuandTheodorBorangiu.2018.Timeseriesforecastingfordynamicschedulingofmanufacturingprocesses.In2018IEEEInternational
ConferenceonAutomation,QualityandTesting,Robotics(AQTR).1–6. https://doi.org/10.1109/AQTR.2018.8402748
[166] AbdullahMueen,YanZhu,MichaelYeh,KavehKamgar,KrishnamurthyViswanathan,ChetanGupta,andEamonnKeogh.2017. TheFastest
SimilaritySearchAlgorithmforTimeSeriesSubsequencesunderEuclideanDistance.
[167] MohsinMunir,ShoaibAhmedSiddiqui,AndreasDengel,andSherazAhmed.2019. DeepAnT:ADeepLearningApproachforUnsupervised
AnomalyDetectioninTimeSeries.7(2019),1991–2005. https://doi.org/10.1109/ACCESS.2018.2886457
[168] GyoungSNa,DonghyunKim,andHwanjoYu.2018.Dilof:Effectiveandmemoryefficientlocaloutlierdetectionindatastreams.InSIGKDD.
1993–2002.
[169] TakaakiNakamura,MakotoImamura,RyanMercer,andEamonnJ.Keogh.2020.MERLIN:Parameter-FreeDiscoveryofArbitraryLengthAnomalies
inMassiveTimeSeriesArchives.InICDM,ClaudiaPlant,HaixunWang,AlfredoCuzzocrea,CarloZaniolo,andXindongWu(Eds.).IEEE,1190–1195.
https://doi.org/10.1109/ICDM50108.2020.00147
[170] TakaakiNakamura,RyanMercer,MakotoImamura,andEamonnKeogh.2023.MERLIN++:parameter-freediscoveryoftimeseriesanomalies.
DataMiningandKnowledgeDiscovery37,2(2023),670–709. https://doi.org/10.1007/s10618-022-00876-7
[171] ZijianNiu,KeYu,andXiaofeiWu.2020.LSTM-basedVAE-GANfortime-seriesanomalydetection.Sensors20,13(2020),3738.
[172] OliverObst,X.RosalindWang,andMikhailProkopenko.2008.UsingEchoStateNetworksforAnomalyDetectioninUndergroundCoalMines.In
ProceedingsoftheInternationalConferenceonInformationProcessinginSensorNetworks(IPSN).IEEE,219–229. https://doi.org/10.1109/IPSN.2008.35
[173] AlbertoOgbechie,JavierDíaz-Rozo,PedroLarrañaga,andConchaBielza.2017. DynamicBayesianNetwork-BasedAnomalyDetectionfor
In-ProcessVisualInspectionofLaserSurfaceHeatTreatment.InProceedingsoftheInternationalConferenceonMachineLearningforCyberPhysical
Systems(ML4CPS),JürgenBeyerer,OliverNiggemann,andChristianKühnert(Eds.).SpringerBerlinHeidelberg,17–24. https://doi.org/10.1007/978-
3-662-53806-7_3
[174] RandyPaffenroth,KathleenKay,andLesServi.2018. RobustPCAforAnomalyDetectioninCyberNetworks. arXiv:1801.01571[cs] http:
//arxiv.org/abs/1801.01571
[175] ESPage.1957.Onproblemsinwhichachangeinaparameteroccursatanunknownpoint.Biometrika44,1/2(1957),248–252.
[176] ThemisPalpanas.2015.DataSeriesManagement:TheRoadtoBigSequenceAnalytics.SIGMODRec.44,2(2015),47–52.
ManuscriptsubmittedtoACM

48 Paparrizosetal.
[177] GirishKeshavPalshikar.2005. Distance-basedoutliersinsequences.InDistributedComputingandInternetTechnology:SecondInternational
Conference,ICDCIT2005,Bhubaneswar,India,December22-24,2005.Proceedings2.Springer,547–552.
[178] SpirosPapadimitriou,HiroyukiKitagawa,PhillipBGibbons,andChristosFaloutsos.2003.Loci:Fastoutlierdetectionusingthelocalcorrelation
integral.InICDE.IEEE,315–326.
[179] IoannisPaparrizos.2018.Fast,Scalable,andAccurateAlgorithmsforTime-SeriesAnalysis.Ph.D.Dissertation.ColumbiaUniversity.
[180] JohnPaparrizos,PaulBoniol,ThemisPalpanas,RueySTsay,AaronElmore,andMichaelJFranklin.2022.Volumeunderthesurface:anewaccuracy
evaluationmeasurefortime-seriesanomalydetection.PVLDB15,11(2022),2774–2787.
[181] JohnPaparrizos,IkraduyaEdian,ChunweiLiu,AaronJElmore,andMichaelJFranklin.2022.Fastadaptivesimilaritysearchthroughvariance-aware
quantization.InICDE.IEEE,2969–2983.
[182] JohnPaparrizosandMichaelJFranklin.2019.GRAIL:efficienttime-seriesrepresentationlearning.ProceedingsoftheVLDBEndowment12,11
(2019),1762–1777.
[183] JohnPaparrizosandLuisGravano.2016.k-Shape:EfficientandAccurateClusteringofTimeSeries.SIGMOD45,1(June2016),69–76. https:
//doi.org/10.1145/2949741.2949758
[184] JohnPaparrizosandLuisGravano.2017.FastandAccurateTime-SeriesClustering.ACMTransactionsonDatabaseSystems(TODS)42,2(2017),8.
[185] JohnPaparrizos,YuhaoKang,PaulBoniol,RueySTsay,ThemisPalpanas,andMichaelJFranklin.2022.TSB-UAD:anend-to-endbenchmarksuite
forunivariatetime-seriesanomalydetection.PVLDB15,8(2022),1697–1711.
[186] JohnPaparrizos,ChunweiLiu,BrunoBarbarioli,JohnnyHwang,IkraduyaEdian,AaronJElmore,MichaelJFranklin,andSanjayKrishnan.2021.
VergeDB:ADatabaseforIoTAnalyticsonEdgeDevices..InCIDR.
[187] JohnPaparrizos,ChunweiLiu,AaronElmore,andMichaelJ.Franklin.2023.QueryingTime-SeriesData:AComprehensiveComparisonofDistance
Measures.IEEEDataEngineeringBulletin(DEB2023)47(2023),69–88.
[188] JohnPaparrizos,ChunweiLiu,AaronJElmore,andMichaelJFranklin.2020.Debunkingfourlong-standingmisconceptionsoftime-seriesdistance
measures.InSIGMOD.1887–1905.
[189] JohnPaparrizosandSaiPrasannaTejaReddy.2023.Odyssey:Anengineenablingthetime-seriesclusteringjourney.ProceedingsoftheVLDB
Endowment16,12(2023),4066–4069.
[190] JohnPaparrizos,RyenWWhite,andEricHorvitz.2016.Detectingdevastatingdiseasesinsearchlogs.InSIGKDD.559–568.
[191] JohnPaparrizos,RyenWWhite,andEricHorvitz.2016.Screeningforpancreaticadenocarcinomausingsignalsfromwebsearchlogs:Feasibility
studyandresults.Journalofoncologypractice12,8(2016),737–744.
[192] JohnPaparrizos,KaizeWu,AaronElmore,ChristosFaloutsos,andMichaelJFranklin.2023.Acceleratingsimilaritysearchforelasticmeasures:A
studyandnewgeneralizationoflowerboundingdistances.ProceedingsoftheVLDBEndowment16,8(2023),2019–2032.
[193] DaehyungPark,ZackoryErickson,TapomayukhBhattacharjee,andCharlesC.Kemp.2016. MultimodalExecutionMonitoringforAnomaly
DetectionduringRobotManipulation.InProceedingsoftheInternationalConferenceonRoboticsandAutomation(ICRA).IEEE,407–414. https:
//doi.org/10.1109/ICRA.2016.7487160
[194] DaehyungPark,YuunaHoshi,andCharlesC.Kemp.2018.AMultimodalAnomalyDetectorforRobot-AssistedFeedingUsinganLSTM-Based
VariationalAutoencoder.3,3(2018),1544–1551. https://doi.org/10.1109/LRA.2018.2801475
[195] StephenPauwelsandToonCalders.2019. AnAnomalyDetectionTechniqueforBusinessProcessesBasedonExtendedDynamicBayesian
Networks.InProceedingsoftheACM/SIGAPPSymposiumonAppliedComputing(SAC).ACM,494–501. https://doi.org/10.1145/3297280.3297326
[196] StephenPauwelsandToonCalders.2019.DetectingAnomaliesinHybridBusinessProcessLogs.19,2(2019),18–30. https://doi.org/10.1145/
3357385.3357387
[197] ERWINSPearsonandCChandraSekar.1936.Theefficiencyofstatisticaltoolsandacriterionfortherejectionofoutlyingobservations.Biometrika
28,3/4(1936),308–320.
[198] BenjaminPeirce.1852.Criterionfortherejectionofdoubtfulobservations.TheAstronomicalJournal2(1852),161–163.
[199] C-KPeng,ShlomoHavlin,HEugeneStanley,andAryLGoldberger.1995. Quantificationofscalingexponentsandcrossoverphenomenain
nonstationaryheartbeattimeseries.Chaos:AnInterdisciplinaryJournalofNonlinearScience5,1(1995),82–87.
[200] DragoljubPokrajac,AleksandarLazarevic,andLonginJanLatecki.2007. Incrementallocaloutlierdetectionfordatastreams.In2007IEEE
symposiumoncomputationalintelligenceanddatamining.IEEE,504–515.
[201] XiangfeiQiu,JilinHu,LekuiZhou,XingjianWu,JunyangDu,BuangZhang,ChenjuanGuo,AoyingZhou,ChristianS.Jensen,ZhenliSheng,
andBinYang.2024.TFB:TowardsComprehensiveandFairBenchmarkingofTimeSeriesForecastingMethods.Proc.VLDBEndow.17,9(2024),
2363–2377.
[202] SridharRamaswamy,RajeevRastogi,andKyuseokShim.2000.EfficientAlgorithmsforMiningOutliersfromLargeDataSets.SIGMODRec.29,2
(may2000),427–438. https://doi.org/10.1145/335191.335437
[203] UsmanRaza,AlessandroCamerra,AmyLMurphy,ThemisPalpanas,andGianPietroPicco.2015.Practicaldatapredictionforreal-worldwireless
sensornetworks.IEEETransactionsonKnowledgeandDataEngineering27,8(2015),2231–2244.
[204] HanshengRen,BixiongXu,YujingWang,ChaoYi,CongruiHuang,XiaoyuKou,TonyXing,MaoYang,JieTong,andQiZhang.2019.Time-series
anomalydetectionserviceatmicrosoft.InProceedingsofthe25thACMSIGKDDinternationalconferenceonknowledgediscovery&datamining.
3009–3017.
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 49
[205] DaniloJimenezRezende,ShakirMohamed,andDaanWierstra.2014.StochasticBackpropagationandApproximateInferenceinDeepGenerative
Models.InProceedingsofthe31stInternationalConferenceonICML-Volume32(Beijing,China)(ICML’14).JMLR.org,II–1278–II–1286.
[206] JoshuaSRichmanandJRandallMoorman.2000.Physiologicaltime-seriesanalysisusingapproximateentropyandsampleentropy.American
JournalofPhysiology-HeartandCirculatoryPhysiology278,6(2000),H2039–H2049.
[207] KexinRong,ClaraEYoon,KarianneJBergen,HashemElezabi,PeterBailis,PhilipLevis,andGregoryCBeroza.2018.Locality-sensitivehashing
forearthquakedetection:Acasestudyofscalingdata-drivenscience.ProceedingsoftheVLDBEndowment11,11(2018),1674–1687.
[208] VolkerRoth.2006.KernelFisherDiscriminantsforOutlierDetection.18,4(2006),942–960. https://doi.org/10.1162/neco.2006.18.4.942
[209] PeterRousseeuw.1984.LeastMedianofSquaresRegression.JournalofTheAmericanStatisticalAssociation-JAMERSTATISTASSN79(121984),
871–880. https://doi.org/10.1080/01621459.1984.10477105
[210] PeterJ.RousseeuwandKatrienVanDriessen.1999.AFastAlgorithmfortheMinimumCovarianceDeterminantEstimator.Technometrics41,3
(1999),212–223. https://doi.org/10.1080/00401706.1999.10485670arXiv:https://www.tandfonline.com/doi/pdf/10.1080/00401706.1999.10485670
[211] PeterJ.RousseeuwandAnnickM.Leroy.1987.Robustregressionandoutlierdetection.Wiley,NewYork.
[212] PeterJRousseeuwandAnnickMLeroy.2005.Robustregressionandoutlierdetection.Vol.589.Johnwiley&sons.
[213] EduardoJRuiz,VagelisHristidis,CarlosCastillo,AristidesGionis,andAlejandroJaimes.2012.Correlatingfinancialtimeserieswithmicro-blogging
activity.InProceedingsofthefifthACMinternationalconferenceonWebsearchanddatamining.ACM,513–522.
[214] StanSalvadorandPhilipChan.2005. LearningStatesandRulesforDetectingAnomaliesinTimeSeries. 23,3(2005),241–255. https:
//doi.org/10.1007/s10489-005-4610-3
[215] JörgSander,MartinEster,Hans-PeterKriegel,andXiaoweiXu.1998.Density-BasedClusteringinSpatialDatabases:TheAlgorithmGDBSCAN
andItsApplications.DataMiningandKnowledgeDiscovery2,2(01Jun1998),169–194. https://doi.org/10.1023/A:1009745219419
[216] SebastianSchmidl,PhillipWenig,andThorstenPapenbrock.2022.AnomalyDetectioninTimeSeries:AComprehensiveEvaluation.PVLDB15,9
(may2022),1779–1797. https://doi.org/10.14778/3538598.3538602
[217] JohannesSchneider,PhillipWenig,andThorstenPapenbrock.2021.DistributedDetectionofSequentialAnomaliesinUnivariateTimeSeries.The
VLDBJournal30,4(mar2021),579–602. https://doi.org/10.1007/s00778-021-00657-6
[218] BernhardSchölkopf,RobertCWilliamson,AlexSmola,JohnShawe-Taylor,andJohnPlatt.1999.Supportvectormethodfornoveltydetection.
NeurIPS12(1999).
[219] PavelSenin,JessicaLin,XingWang,TimOates,SunilGandhi,ArnoldP.Boedihardjo,CrystalChen,andSusanFrankenstein.2015.Timeseries
anomalydiscoverywithgrammar-basedcompression.InEDBT.
[220] PavelSenin,JessicaLin,XingWang,TimOates,SunilGandhi,ArnoldP.Boedihardjo,CrystalChen,andSusanFrankenstein.2015.TimeSeries
AnomalyDiscoverywithGrammar-BasedCompression.,481–492pages. https://doi.org/10.5441/002/edbt.2015.42
[221] DennisShasha.1999.Tuningtimeseriesqueriesinfinance:Casestudiesandrecommendations.IEEEDataEng.Bull.22,2(1999),40–46.
[222] LifengShen,ZhuocongLi,andJamesKwok.2020.Timeseriesanomalydetectionusingtemporalhierarchicalone-classnetwork.NeurIPS33(2020),
13016–13026.
[223] S-C.ChenK.SarinnapakornShyu,M-L.andLW.Chang.2003.ANovelAnomalyDetectionSchemeBasedonPrincipalComponentClassifier.
(2003).
[224] AlbanSiffer,Pierre-AlainFouque,AlexandreTermier,andChristineLargouet.2017.Anomalydetectioninstreamswithextremevaluetheory.In
Proceedingsofthe23rdACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.1067–1075.
[225] DavidEugeneSmith.2012.Asourcebookinmathematics.CourierCorporation.
[226] RalphD.SnyderandStephenJ.Withers.1983.Exponentialsmoothingwithfinitesamplecorrection.Number1983,1inWorkingpaper.Department
ofEconometricsandOperationsResearch.MonashUniversity.Dept.,Univ,Clayton.
[227] MaximilianSoelch,JustinBayer,MarvinLudersdorfer,andPatrickvanderSmagt.2016.VariationalInferenceforOn-LineAnomalyDetectionin
High-DimensionalTimeSeries.arXiv:1602.07109[cs,stat] http://arxiv.org/abs/1602.07109
[228] HongchaoSong,ZhuqingJiang,AidongMen,andBoYang.2017.AHybridSemi-SupervisedAnomalyDetectionModelforHigh-Dimensional
Data.ComputationalIntelligenceandNeuroscience2017(15Nov2017),8501683. https://doi.org/10.1155/2017/8501683
[229] SondreSørbøandMassimilianoRuocco.2023.NavigatingtheMetricMaze:ATaxonomyofEvaluationMetricsforAnomalyDetectioninTime
Series.arXivpreprintarXiv:2303.01272(2023).
[230] EJStone.1873.Ontherejectionofdiscordantobservations.MonthlyNoticesoftheRoyalAstronomicalSociety34(1873),9.
[231] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019. RobustAnomalyDetectionforMultivariateTimeSeriesthrough
StochasticRecurrentNeuralNetwork.InSIGKDD.ACM,2828–2837. https://doi.org/10.1145/3292500.3330672
[232] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019.Robustanomalydetectionformultivariatetimeseriesthroughstochastic
recurrentneuralnetwork.InSIGKDD.2828–2837.
[233] S.Subramaniam,T.Palpanas,D.Papadopoulos,V.Kalogeraki,andD.Gunopulos.2006. OnlineOutlierDetectioninSensorDataUsingNon-
ParametricModels.InProceedingsoftheInternationalConferenceonVeryLargeDatabases(VLDB)(VLDB’06).VLDBEndowment,187–198.
https://dl.acm.org/doi/10.5555/1182635.1164145
[234] PeiSun,SanjayChawla,andBavaniArunasalam.2006.MiningforOutliersinSequentialDatabases.InProceedingsoftheInternationalConference
onDataMining(ICDM).SocietyforIndustrialandAppliedMathematics,94–105. https://doi.org/10.1137/1.9781611972764.9
ManuscriptsubmittedtoACM

50 Paparrizosetal.
[235] EmmanouilSylligardos,PaulBoniol,JohnPaparrizos,PanosE.Trahanias,andThemisPalpanas.2023.ChooseWisely:AnExtensiveEvaluationof
ModelSelectionforAnomalyDetectioninTimeSeries.Proc.VLDBEndow.16,11(2023),3418–3432. https://doi.org/10.14778/3611479.3611536
[236] JianTang,ZhixiangChen,AdaWai-CheeFu,andDavidWCheung.2002.Enhancingeffectivenessofoutlierdetectionsforlowdensitypatterns.In
PAKDD.535–548.
[237] NesimeTatbul,TaeJunLee,StanZdonik,MejbahAlam,andJustinGottschlich.2018.Precisionandrecallfortimeseries.InNeurIPS.1924–1934.
[238] DavidMJTaxandRobertPWDuin.2004.Supportvectordatadescription.Machinelearning54,1(2004),45–66.
[239] RueySTsay.1988.Outliers,levelshifts,andvariancechangesintimeseries.Journalofforecasting7,1(1988),1–20.
[240] RueySTsay.2014.FinancialTimeSeries.WileyStatsRef:StatisticsReferenceOnline(2014),1–23.
[241] RueySTsay,DanielPena,andAlanEPankratz.2000.Outliersinmultivariatetimeseries.Biometrika87,4(2000),789–804.
[242] JohnWTukeyetal.1977.Exploratorydataanalysis.Vol.2.Reading,Mass.
[243] KuniakiUeharaandMitsuomiShimada.2002.Extractionofprimitivemotionanddiscoveryofassociationrulesfromhumanmotiondata.In
ProgressinDiscoveryScience.Springer,338–348.
[244] RafaelG.Vieira,MarcosA.LeoneFilho,andRobinsonSemolini.2018.AnEnhancedSeasonal-HybridESDTechniqueforRobustAnomalyDetection
onTimeSeries.InSimpósioBrasileirodeRedesdeComputadores(SBRC),Vol.36.
[245] GabrielWachman,RoniKhardon,PavlosProtopapas,andCharlesRAlcock.2009.Kernelsforperiodictimeseriesarisinginastronomy.InJoint
EuropeanConferenceonMachineLearningandKnowledgeDiscoveryinDatabases.Springer,489–505.
[246] YiWang,LinshengHan,WeiLiu,ShujiaYang,andYanboGao.2019. StudyonWaveletNeuralNetworkBasedAnomalyDetectioninOcean
ObservingDataSeries.186(2019),106129. https://doi.org/10.1016/j.oceaneng.2019.106129
[247] PeterJWebster,GregJHolland,JudithACurry,andH-RChang.2005.Changesintropicalcyclonenumber,duration,andintensityinawarming
environment.Science309,5742(2005),1844–1846.
[248] BillyMWilliamsandLesterAHoel.2003.ModelingandforecastingvehiculartrafficflowasaseasonalARIMAprocess:Theoreticalbasisand
empiricalresults.Journaloftransportationengineering129,6(2003),664–672.
[249] JiaWu,WeiruZeng,andFeiYan.2018.HierarchicalTemporalMemoryMethodforTime-Series-BasedAnomalyDetection.273(2018),535–546.
https://doi.org/10.1016/j.neucom.2017.08.026
[250] P.Wu,J.Liu,andF.Shen.2020.ADeepOne-ClassNeuralNetworkforAnomalousEventDetectioninComplexScenes.IEEETransactionson
NeuralNetworksandLearningSystems31,7(2020),2609–2622. https://doi.org/10.1109/TNNLS.2019.2933554
[251] RenjieWuandEamonnJ.Keogh.2023.CurrentTimeSeriesAnomalyDetectionBenchmarksareFlawedandareCreatingtheIllusionofProgress.
IEEETrans.Knowl.DataEng.35,3(2023),2421–2429. https://doi.org/10.1109/TKDE.2021.3112126
[252] WentaiWu,LigangHe,WeiweiLin,YiSu,YuhuaCui,CarstenMaple,andStephenJarvis.2020.DevelopinganUnsupervisedReal-TimeAnomaly
DetectionSchemeforTimeSerieswithMulti-Seasonality.arXiv:1908.01146[cs,eess,stat] http://arxiv.org/abs/1908.01146
[253] YanshanXiao,BoLiu,LongbingCao,XindongWu,ChengqiZhang,ZhifengHao,FengzhaoYang,andJieCao.2009.Multi-spheresupportvector
datadescriptionforoutliersdetectiononmulti-distributiondata.In2009IEEEinternationalconferenceondataminingworkshops.IEEE,82–87.
[254] HaowenXu,WenxiaoChen,NengwenZhao,ZeyanLi,JiahaoBu,ZhihanLi,YingLiu,YoujianZhao,DanPei,YangFeng,etal.2018.Unsupervised
AnomalyDetectionviaVariationalAuto-EncoderforSeasonalKPIsinWebApplications.InProceedingsoftheInternationalConferenceonWorld
WideWeb(WWW).InternationalWorldWideWebConferencesSteeringCommittee,InternationalWorldWideWebConferencesSteering
Committee,187–196. https://doi.org/10.1145/3178876.3185996
[255] HaowenXu,WenxiaoChen,NengwenZhao,ZeyanLi,JiahaoBu,ZhihanLi,YingLiu,YoujianZhao,DanPei,YangFeng,etal.2018.Unsupervised
anomalydetectionviavariationalauto-encoderforseasonalkpisinwebapplications.InProceedingsofthe2018worldwidewebconference.187–196.
[256] KenjiYamanishi,Jun-ichiTakeuchi,GrahamWilliams,andPeterMilne.2004.On-LineUnsupervisedOutlierDetectionUsingFiniteMixtureswith
DiscountingLearningAlgorithms.8,3(2004),275–300. https://doi.org/10.1023/B:DAMI.0000023676.72185.7c
[257] Chao-LungYangandWei-JuLiao.2017.AdjacentMeanDifference(AMD)methodfordynamicsegmentationintimeseriesanomalydetection.In
2017IEEE/SICEInternationalSymposiumonSystemIntegration(SII).IEEE,241–246.
[258] DragomirYankov,EamonnKeogh,andUmaaRebbapragada.2008.Diskawarediscorddiscovery:Findingunusualtimeseriesinterabytesized
datasets.KnowledgeandInformationSystems17(2008),241–262.
[259] DragomirYankov,EamonnJ.Keogh,andUmaaRebbapragada.2007.DiskAwareDiscordDiscovery:FindingUnusualTimeSeriesinTerabyte
SizedDatasets.InICDM.
[260] YuanYao,AbhishekSharma,LeanaGolubchik,andRameshGovindan.2010.OnlineAnomalyDetectionforSensorSystems:ASimpleandEfficient
Approach.Perform.Eval.67,11(nov2010),1059–1075. https://doi.org/10.1016/j.peva.2010.08.018
[261] C.-C.M.Yeh,Y.Zhu,L.Ulanova,N.Begum,Y.Ding,H.A.Dau,D.F.Silva,A.Mueen,andE.J.Keogh.2016.MatrixProfileI:AllPairsSimilarityJoins
forTimeSeries:AUnifyingViewThatIncludesMotifs,DiscordsandShapelets.InICDM.
[262] Chin-ChiaMichaelYeh,YanZhu,LiudmilaUlanova,NurjahanBegum,YifeiDing,HoangAnhDau,DiegoFurtadoSilva,AbdullahMueen,and
EamonnKeogh.2016.MatrixProfileI:AllPairsSimilarityJoinsforTimeSeries:AUnifyingViewThatIncludesMotifs,DiscordsandShapelets.In
ProceedingsoftheInternationalConferenceonDataMining(ICDM).1317–1322. https://doi.org/10.1109/ICDM.2016.0179
[263] YufengYu,YuelongZhu,ShijinLi,andDingshengWan.2014.TimeSeriesOutlierDetectionBasedonSlidingWindowPrediction.2014(2014),
1–14. https://doi.org/10.1155/2014/879736
ManuscriptsubmittedtoACM

DiveintoTime-SeriesAnomalyDetection:ADecadeReview 51
[264] ChunkaiZhang,ShaocongLi,HongyeZhang,andYingyangChen.2020.VELC:ANewVariationalAutoEncoderBasedModelforTimeSeries
AnomalyDetection.arXiv:1907.01702[cs,stat] http://arxiv.org/abs/1907.01702
[265] ChuxuZhang,DongjinSong,YuncongChen,XinyangFeng,CristianLumezanu,WeiCheng,JingchaoNi,BoZong,HaifengChen,andNiteshV.
Chawla.2019.ADeepNeuralNetworkforUnsupervisedAnomalyDetectionandDiagnosisinMultivariateTimeSeriesData.InAAAI,Vol.33.
1409–1416. https://doi.org/10.1609/aaai.v33i01.33011409
[266] RuiZhang,ShaoyanZhang,SethuramanMuthuraman,andJianminJiang.2007.OneClassSupportVectorMachineforAnomalyDetectioninthe
CommunicationNetworkPerformanceData.InProceedingsoftheConferenceonAppliedElectromagnetics,WirelessandOpticalCommunications
(ELECTROSCIENCE)(ELECTROSCIENCE’07).WorldScientificandEngineeringAcademyandSociety(WSEAS),31–37.
[267] HangZhao,YujingWang,JuanyongDuan,CongruiHuang,DefuCao,YunhaiTong,BixiongXu,JingBai,JieTong,andQiZhang.2020.Multivariate
time-seriesanomalydetectionviagraphattentionnetwork.InICDM.IEEE,841–850.
[268] YanZhu,Chin-ChiaMichaelYeh,ZacharyZimmerman,KavehKamgar,andEamonnKeogh.2018.MatrixprofileXI:SCRIMP++:timeseriesmotif
discoveryatinteractivespeeds.In2018IEEEInternationalConferenceonDataMining(ICDM).IEEE,837–846.
[269] YanZhu,ZacharyZimmerman,NaderShakibaySenobari,Chin-ChiaMichaelYeh,GarethFunning,AbdullahMueen,PhilipBrisk,andEamonn
Keogh.2016.Matrixprofileii:Exploitinganovelalgorithmandgpustobreaktheonehundredmillionbarrierfortimeseriesmotifsandjoins.In
2016IEEE16thinternationalconferenceondatamining(ICDM).IEEE,739–748.
[270] YanZhu,ZacharyZimmerman,NaderShakibaySenobari,Chin-ChiaMichaelYeh,GarethFunning,AbdullahMueen,PhilipBrisk,andEamonn
Keogh.2016.Matrixprofileii:Exploitinganovelalgorithmandgpustobreaktheonehundredmillionbarrierfortimeseriesmotifsandjoins.In
2016IEEE16thinternationalconferenceondatamining(ICDM).IEEE,739–748.
[271] ZacharyZimmerman,KavehKamgar,NaderShakibaySenobari,BrianCrites,GarethFunning,PhilipBrisk,andEamonnKeogh.2019.Matrix
profileXIV:scalingtimeseriesmotifdiscoverywithGPUstobreakaquintillionpairwisecomparisonsadayandbeyond.InProceedingsofthe
ACMSymposiumonCloudComputing.74–86.
[272] ZacharyZimmerman,NaderShakibaySenobari,GarethFunning,EvangelosPapalexakis,SametOymak,PhilipBrisk,andEamonnKeogh.2019.
MatrixprofileXVIII:timeseriesmininginthefaceoffastmovingstreamsusingalearnedapproximatematrixprofile.In2019IEEEInternational
ConferenceonDataMining(ICDM).IEEE,936–945.
ManuscriptsubmittedtoACM