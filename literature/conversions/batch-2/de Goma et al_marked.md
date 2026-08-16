---
conversion_metadata:
  converted_at: "2026-07-22T13:35:59Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "de Goma et al.pdf"
  source_pdf_sha256: "83ad812f369e3c3bc9e2b820e03b0bf87f93355efe7ff44a73dbfdc7812cc76d"
  page_count: 7
  markdown_char_count: 70520
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Using Item Personality-Based Profiling in Music Recommender
Systems

Joel de Goma
SCHOOL OF INFORMATION
TECHNOLOGY
Mapua University
Makati, Metro Manila, Philippines
jcdegoma@mapua.edu.ph

Jan Nielsen Anonuevo
SCHOOL OF INFORMATION
TECHNOLOGY
Mapua University
Makati, Metro Manila, Philippines
jndanonuevo@mymail.mapua.edu.ph

Gian Nicole Pangan
SCHOOL OF INFORMATION
TECHNOLOGY
Mapua University
Makati, Metro Manila, Philippines
gnlpangan@mymail.mapua.edu.ph

John Jovaniel Deang
Department of Physical Education
and Athletics
Mapua University
Makati, Metro Manila, Philippines
jjcdeang@mapua.edu.ph

Alberto Villaluz
SCHOOL OF INFORMATION
TECHNOLOGY
Mapua University
Makati, Metro Manila, Philippines
acvillaluz@mapua.edu.ph

Abstract
Music recommender systems play an essential role in giving music
suggestions in accordance to a user’s liking. However, there are two
common problems with regards to recommendation algorithms,
namely user variability and the cold start problem. With this, the
researchers aim to address the said problems by incorporating
personality profiles to aid in giving music recommendations in
accordance to a user’s interests. The study made use of the LightFM
Model to incorporate the user’s top five favorite genres and big
five personality scores, hence using a hybrid approach. The hybrid
model is then compared with the traditional collaborative filtering
model with certain metrics to determine its performance. According
to the results, the hybrid model outperforms the traditional CF
model, proving that incorporating personality profiles can improve
the accuracy of the model in giving music suggestions to a user.

CCS Concepts
• Computing Methodologies; • Machine learning; • Machine
learning approaches; • Neural networks;

Keywords
Recommender Systems, Collaborative Filtering, LightFM

ACM Reference Format:
Joel de Goma, Jan Nielsen Anonuevo, Gian Nicole Pangan, John Jovaniel
Deang, and Alberto Villaluz. 2025. Using Item Personality-Based Profiling
in Music Recommender Systems.
In 2025 The 7th World Symposium on
Software Engineering (WSSE 2025), October 24–26, 2025, Okayama, Japan.
ACM, New York, NY, USA, 7 pages. https://doi.org/10.1145/3779657.3779698

Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
WSSE 2025, Okayama, Japan
© 2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-1577-8/2025/10
https://doi.org/10.1145/3779657.3779698

1 Introduction
With the increasing adoption of music subscription services within
the community, recommender systems play a crucial role in suggest-
ing songs that align with the user’s interests. However, addressing
user variability and overcoming the cold-start problem presents
significant challenges for traditional recommendation algorithms.
Users’ music preferences can be diverse and multifaceted, making it
difficult for these algorithms to accurately capture their preferences
[1].

The researchers will focus on the effectiveness of proportion-
based IPPs towards personality-based music recommender systems.
The current study by Alharthi focuses on the use of the recom-
mender systems in general, and with this, the researchers intend
to apply the said approach to music recommender systems [2]. [3]
suggests that item-based recommender systems perform better in
terms of rating-based CF recommender systems. Referencing the
said study, the researchers intend to explore more on item-based
recommender systems.

As the study will revolve around the use of personality-based
music recommendation systems, certain gaps are intended to be
addressed. Only a few studies have explored the use of personality-
based music recommender systems as most research would focus
on mood and emotion. Li suggests that personality is one of the
factors that determines one’s musical preferences, besides mood
and emotion [3]. With this, the researchers intend to address the
gaps presented by the personality-based recommender system and
that is its issues with its accuracy. Researchers tend to address
this problem by integrating the system with current collaborative
filtering methods. [1] found that having a Big Five personality-
based music recommendation system had certain personality biases
that made the results irrelevant. With this, the researchers intend to
propose a new approach regarding personality-based recommender
systems that use the Big Five model. As Alharthi’s study produces
promising results, the researchers believe that the said study can
be incorporated with music recommender systems using the Big
Five personality model which could lessen errors posed using the
Big Five model.

---

<!-- PAGE 2 -->

WSSE 2025, October 24–26, 2025, Okayama, Japan

Joel de Goma et al.

2 Review of Related Literature
Many recent studies in sentiment analysis gave significant rise to
Machine Learning algorithms. While there has been much research
on Traditional Machine Learning models specifically on the Online
Learning dataset, only a few studies have taken into consideration
Deep Learning models. This has been attributed to the exceptional
accuracy of traditional models.

Lu & Tintarev’s study focuses on addressing the cold-start prob-
lem amongst recommender systems. With this, their paper focuses
on giving better recommendations by re-ranking the suggestions
by the recommender and improving the accuracy of the model by
integration of personality traits. Their results suggested that the
said focus points of the paper have been met, wherein personalized
recommendation lists are higher in diversity and lead to an increase
in user satisfaction [4].

Klec et al’s studied how personality traits can have an influence
on music recommendation error. The study collected responses
from 279 participants to gather their listening traits and their per-
sonality profiles. With this data, the combination between the
personality traits and the audio features from the songs were stud-
ied to arrive at a conclusion with regards to music recommendation
error. Findings suggested that some personality facets had yielded
the lowest recommendation error for BFI-2, compared to the higher
order of the big five personality traits. The researchers had con-
cluded that this discovery can help other researchers to filter the
personality questionnaire down to only the essential questions to
be used in gathering the personality profiles of the users to predict
their listening habits [1].

Garg & et. al. [5] focuses on developing a music mood-based
recommendation system using machine learning and deep learning
techniques, with a particular emphasis on addressing the common
struggle people face in finding music that matches their mood or
emotions. The research utilizes the FERPlus dataset and Spotipy,
a Python library for Spotify, for web scraping and data manipula-
tion. The Valence-Arousal theory is employed to classify the song
database into mood quadrants, and K-Means clustering is used for
further categorization. Features such as valence, energy, danceabil-
ity, loudness, tempo, speechiness, instrumentalness, and popularity
are considered. A Deep Convolutional Neural Network (CNN) is
employed for classification, with varying accuracies reported for
different models and emotions. The model aims to provide real time
playlist recommendations based on mood, contributing to mood
enhancement through AI-driven song selection. The study sug-
gests that this method surpasses genre classification in accuracy,
with potential applications in improving social networking and
customer satisfaction. The reported accuracy percentages include
below 65% for a Simple CNN with six emotions, above 70% for a
Simple CNN with four emotions, below 72% for a Deep CNN with
six emotions, and about 80% for a Deep CNN with four emotions.
Loss percentages, based on 60% training data and 50% validation
data, decrease to 30% or below as the number of epochs increases
for both training and validation data.

Joy & et. al. [6] is rooted in the Big Five Model, leverages
data obtained from Twitter, encompassing 395,056 listening events,
18,310 users with personality values, and 15,753 unique tracks. The
research investigates how users’ personality traits influence the

accuracy scores of state-of-the-art recommendation algorithms and
explores user bias related to personality traits. The methodology in-
volves data cleaning, personality estimation, and data segmentation
for track and artist information extraction. Sparse Linear Meth-
ods, Embarrassingly Shallow Autoencoders (EASE), and Variational
Autoencoders (Mult-VAE) are utilized for analysis. The reported
recall values at different positions (5, 10, and 15) provide insights
into algorithm performance based on users’ personality traits. For
instance, at Recall@5, EASE achieved 0.0366, SLIM achieved 0.0334,
and Mult-VAE achieved 0.0433. These rates indicate the propor-
tion of relevant items retrieved by the algorithms at the specified
positions. The study recognizes its limitations, such as generaliz-
ability and data completeness issues, and outlines future research
directions to better understand the causes of biases and explore
additional aspects of recommendation quality beyond accuracy.

Delando & et. al. [7] is centered around the MBTI, utilizing the
MARSYAS Dataset along with the Extended and S Datasets, the
study aims to predict personality traits, specifically extraversion
and introversion, based on individuals’ music preferences. The
methodology involves data collection, dimensionality reduction,
normalization, and segmentation based on ”Personality Type.” Au-
dio frames are segmented, and features are extracted using MIRtool-
box and a variational autoencoder. Support Vector Machine (SVM),
Random Forest, K-Nearest Neighbors (KNN), and Naive Bayes clas-
sifiers are employed for analysis. The SVM classifier achieves a
performance rate of 71%, showcasing its effectiveness in predicting
personality traits based on music preferences. Furthermore, the
study explores the correlation between music genres and person-
ality types, revealing a scoring distribution of 53% for extraverts
and 47% for introverts, shedding light on the nuanced relationship
between music preferences and personality traits.

Dorochowicz [8] is focused on exploring emotions and physiolog-
ical signals, utilized the DEAM and PMEmo datasets to investigate
the intricate relationship between music and human emotions. The
research aimed to quantify this connection and develop a machine
learning model capable of predicting both music mood based on
audio signals and human emotion based on physiological signals.
The methodology involved downscaling, format conversion, reg-
ularization, and shrinkage, with feature extraction encompassing
zero-crossing rate, energy, entropy of energy, and various spectral
features. Machine learning models, such as SVM, Random Forest,
Decision Tree, Extra Tree, k-NN, MLP, AdaBoost, ElasticNet, Ridge,
Lasso, and Adaptive Boost, were employed for analysis. ANOVA
results indicated significant variance between people and items,
emphasizing individualized emotional responses to music. The Ran-
dom Forest model demonstrated notable performance in terms of
action call count and training time. The arousal and valence analy-
sis revealed distinct emotional responses associated with different
music moods. The research achieved an accuracy rate of 81%, un-
derscoring the practical potential of the developed model, including
personalized playlist generation. However, the study acknowledged
the need for further research and refinement to enhance accuracy
and broaden the scope of emotion recognition.

Liu & et. al. [9] utilizes a dataset from the myPersonality web-
site, aimed to develop an algorithm to determine individuals’ music
tastes based on their personality traits. The approach involved con-
verting Facebook status updates into vector representation. Various

---

<!-- PAGE 3 -->

Using Item Personality-Based Profiling in Music Recommender Systems

WSSE 2025, October 24–26, 2025, Okayama, Japan

Figure 1: Proposed Model Workflow

recommendation models, including Naive Bayes Classifier and col-
laborative filtering methods, were employed. The recommendation
model’s performance was assessed using Root Mean Squared Error
(RMSE), with Matrix Factorization achieving the lowest RMSE at
0.88. F-Measures for Big Five Personality Classes, including Open-
ness (0.2308), Conscientiousness (0.4865), Extraversion (0.6349),
Agreeableness (0.5000), and Neuroticism (0.6154), were also cal-
culated. The recommendation model outperformed user-to-user
collaborative filtering with a rating matrix, although matrix fac-
torization remained superior. The study provided insights into the
relationship between personality traits and music preferences, em-
phasizing the potential of personalized recommendation systems.
Lu & et. al. [10] utilizes the myPersonality dataset and the
PsychoFlickr dataset, focused on developing an emotional recom-
mender system that predicts music taste based on personality traits.
The user recognition problems were categorized into five binary
classifications and further divided into classes (low, medium, high).
Forward Features Selection with 10-fold cross-validation was em-
ployed, and various classifiers, including Naive Bayes, Logistic
Regression, SVM, Random Forest, and GBT with deep networks,
were used. The accuracy results for the myPersonality dataset using
the proposed approach were O - 0.71, C - 0.72, E - 0.75, A - 0.73,
N - 0.71. The self-assessed accuracy results for the myPersonality
dataset were lower (O - 0.54, C - 0.55, E - 0.54, A - 0.54, N - 0.54). For
the PsychoFlickr dataset, the proposed approach achieved accura-
cies of O - 0.61, C - 0.59, E - 0.56, A - 0.60, N - 0.61. The self-assessed
accuracy results were again O - 0.54, C - 0.55, E - 0.54, A - 0.54,
N - 0.54. The experiments demonstrated the success of using user
personality for mood recognition in predicting music taste, urging
further exploration in this field.

3 Methodology
As shown in figure 1 the procedure in developing and evaluating
the model.

3.1 Data Collection
The data collection process will be conducted in the form of a survey.
The survey will be used for the explicit gathering of the information
required for building the three matrices (user, item, interaction) that
will be used for the LightFM Hybrid Model. The questionnaire will
have a combined total of 111 questions consisting of the 10-item
BFI Questionnaire (Likert Scale of 1 – 5), 100-item Song Rating (1 as
like, 0 as dislike), and Preferred Genre Checklist (10 genre options,
choosing a maximum of 5).

3.2 DATA PRE-PROCESSING
3.2.1 User Personality Profile. The respondents’ answers to the
Big Five Inventory (BFI) will then undergo a multi-step process
with only the resulting T-score being stored in the dataset. First,
raw scores are calculated for each of the five core dimensions (Ex-
traversion, Neuroticism, Agreeableness, Conscientiousness, and
Openness) by summing an individual’s responses to the relevant
questionnaire items. These raw scores are then transformed into
the variable “user BF dimension mean” which is used to control
for potential discrepancies in question difficulty and establishes a
standardized baseline for comparison. This is computed by dividing
the item scores by the number of questions associated with each
dimension. Following the calculation of user BF dimension means,
the BFI employs standardization procedures to facilitate meaning-
ful comparisons across individuals and populations. Z-scores are
derived to represent the deviation of an individual’s score from the
average population score for a specific trait, expressed in terms of
standard deviations. Finally, for enhanced interpretability, Z-scores
are converted into T-scores with a mean of 50 and a standard devi-
ation of 10. This will result in 5 T-scores, which will be converted
into degrees to categorically represent the user’s personality profile.
A BF score is stored as “high” if it is greater than 55, “low” if it is
lower than 45, or average otherwise as demonstrated in Table 1.
This will be represented in the appropriate format shown in Table
2 to make it compatible as a user-feature embedding.

---

<!-- PAGE 4 -->

WSSE 2025, October 24–26, 2025, Okayama, Japan

Joel de Goma et al.

Item Features. The researchers will

3.2.2
incorporate the
proportion-based IPP method used in [2] where the item personal-
ity profile is represented in vector form, consisting of 15 features.
Each dimension is represented by three features that correspond
to degrees (low, average, and high) The value of one feature is
the proportion of users who like an item in the degree of one BF
dimension which is calculated based on the following formula:

Proportion=(total Number of Users who liked the Item and has
the same BF degree)/(total Number of Users who Liked the Item).
Spotify API will be used to extract content-based features to be
used alongside the item personality profile as item feature weights.
Instead of the musical and the standard features (bpm, tempo, re-
lease date, volume) that are commonly covered in existing studies,
the study will focus on extracting the following sonical components
or features that quantitatively describe aspects that contribute to
the overall sound and mood of the song, which are Acousticness,
Danceability, Energy, Instrumentalness, Liveness, and Valence.

3.2.3
Interaction Matrix. The interactions matrix will store
recorded interactions for all users. This will comprise three columns,
two of which are foreign keys that link to both the user features
matrix (User ID) and song features matrix (song ID). The isLiked
column is used to represent interactions as either 1 or 0. To account
for the differences between the way interactions are stored in the
survey dataset and the Million Song Dataset (MDS), an additional
column Weight will be used as an additional feature for model
training, assigning different levels of importance depending on the
value of a specific interaction. All interactions from the Mapuan
students will automatically be assigned the highest value (5) since
these represent explicitly liked songs from the provided song list.
MDS user interactions on the other hand are in the form of
play counts instead of likes which require a different approach. The
researchers employed a min-max scaling transform to normalize the
data between a range of 0-1. The scaled values are then multiplied
by 4 and rounded to the nearest integer to map to 5 weight levels.
This will allow the model to prioritize learning the correlated song
features in songs with higher play counts when used as weights
during model training.

3.3 Model Development
A hybrid recommender system will be developed utilizing the
LightFM library which integrates elements of both collaborative
filtering and content-based filtering. In this model, users and songs
are represented by latent factors and biases, derived from user at-
tributes, item attributes, and historical interactions. Specifically,
users are described through features such as genre preferences and
user personality profiles (Big Five) while songs are characterized
by their sonic features and the computed Item Personality Profiles
(IPPs). With the described preprocessing and feature extraction
steps, personality features are more deeply integrated into both the
user and item feature matrix, particularly in situations with limited
explicit user-item interactions. This will be combined with the subs
For all models, researchers will use LightFM’s cross-validation
feature to randomly split the interaction set into two disjoint train-
ing and test sets with an 80-20 split. The model will then be fitted
for 30 epochs and a 0.02 learning rate. The researchers will also test

which of the two loss functions (BPR and WARP) will perform bet-
ter on offline evaluation before finalizing the model to be evaluated
by new users. These two loss functions were chosen for evaluation
since both are particularly useful in cases where only positive inter-
actions(likes) are recorded but with different optimizations. WARP
is suited for optimizing the top recommendation list, while BPR is
more suited for optimizing the AUC score. For model evaluation,
the k value is set to 10 to evaluate its performance when generating
the top 10 recommendations.

3.4 Model Validation and Evaluation
The researchers will use the built-in evaluation metrics provided
by the LightFM library. These metrics can be collectively used to
assess the model’s performance by computing these for the training
and test split of the interaction’s matrix. The metrics to be used will
be the ROC AUC Score, Precision, Recall, and F1-score. ROC AUC
Score quantifies the probability that a randomly selected positive
example will have a higher score than a randomly chosen negative
example. It measures the model’s ability to rank positive examples
higher than negative examples. A perfect score is 1.0, indicating op-
timal performance in distinguishing between positive and negative
examples. Precision at k measures the fraction of relevant items
among the top k items recommended by the system. It evaluates the
precision of the recommendations by considering how many of the
top recommendations are relevant to the user. A perfect score is 1.0,
indicating that all top k recommendations are relevant to the user’s
preferences. Recall at k evaluates the system’s ability to retrieve
all relevant items among the top k recommendations. It measures
the proportion of relevant items that are successfully retrieved by
the system compared to all relevant items in the dataset. A perfect
score is 1.0, indicating that all relevant items are retrieved among
the top k recommendations.

The proposed hybrid model as shown in Procedure C will also be
evaluated against a pure collaborative filtering (CF) model (based
only on interactions without incorporating personality IPP and
UPP features) that is trained on the same combined dataset and
parameters.

3.5 Online Evaluation
In addition to these metrics, researchers will also employ online
evaluation methods to conduct model comparisons from the per-
spective of new users whose personality and preference counts
weren’t included in model training. This will be conducted in the
form of a web app, which will require 20 new users to take the
personality test and input their top 5 genre preferences. This will be
used to test the efficacy of generating real-time recommendations
before acquiring a list of their liked/disliked songs. The users will
then be presented with the generated top 10 recommendations from
the two trained models which they will evaluate in the form of a
post-feedback questionnaire which is adapted from a study evalu-
ating their personality-based recommender system (Lu et.al, 2018).
Moreover, users will also be able to individually rate each song in
the generated list as like/dislike. These measures will be precision
and recall (like the dataset evaluation), and user feedback. For
user feedback, the system is evaluated qualitatively by prompting
users to express their opinions on all lists based on the three main

---

<!-- PAGE 5 -->

Using Item Personality-Based Profiling in Music Recommender Systems

WSSE 2025, October 24–26, 2025, Okayama, Japan

Metrics

Precision
Recall
AUC Score
F1 Score

Metrics

Precision
Recall
AUC Score
F1 Score

Table 1: Model Metrics Comparison (Train)

Collaborative Filtering(CF) Hybrid BPR

Hybrid WARP

0.24
0.86
1.00
0.38

0.16
0.02
0.67
0.04

0.23
0.75
0.82
0.35

Table 2: Model Metrics Comparison (Validation)

Collaborative Filtering(CF) Hybrid BPR

Hybrid WARP

0.48
0.74
0.56
0.58

0.42
0.22
0.53
0.29

0.46
0.64
0.57
0.54

aspects based on Pu, Chen, and Hu’s (2011) ResQue User-Centric
Evaluation Framework. These questions are in the form of a 5-point
Likert scale (1 being strongly disagree and 5 being strongly agree),
with one question each for both models being evaluated which will
assess Recommendation Quality, Recommendation Diversity and
User Satisfaction. Respondents will also be asked which model
is more suited for them in terms of recommendation quality and
diversity.

4 Result and Discussion
The researchers collected data from 208 students and used said data
to feed information into the model, generating recommendations
tailored according to their personality scores and genre preferences
for model A (hybrid model), and popularity-based recommenda-
tions for model B (pure CF model). The precision, recall, AUC, and
F1 scores are then computed to evaluate the metrics of the models,
for both offline and online evaluation methods. A two-tailed t-test
and chi-squared test were also conducted for the survey results from
the online evaluation method to verify how statistically significant
the results are, with p < 0.05.

4.1 Offline Evaluation
As shown in table 1 and table 2, pure collaborative filtering model
has the overall best performance metrics when it comes to the
training set particularly for recall and AUC. The higher discrepancy
between recall and precision score for this model (also referred to
as Model B) is indicative of the limitations of this kind of recom-
mender since it prioritizes breadth/diversity of recommendations
as opposed to actual relevance(precision) with an emphasis on
prioritizing songs with more interactions. The drastic drop in per-
formance when comparing the training and validation/test set for
this model also indicates that model’s design has issues with over-
fitting and is less capable of adapting to unseen data compared to
both variants of the hybrid model. Overall, the hybrid models are
observed to have good metrics with no large discrepancy between
validation and training set, which indicates that it can identify pat-
terns and tailor recommendations accordingly even on data with
no recorded interactions. Between the two loss functions tested by

researchers, the hybrid model that uses WARP has the best perfor-
mance on all metrics. The improved performance of WARP over
BPR may be due to the limitation of pairwise loss function when
used on relatively sparse and imbalanced data, with the dataset hav-
ing complete user personality information for less than 20% of the
overall userbase. Moreover, it is especially suitable for improving a
recommender’s ability to rank items, which is why it was chosen
as the final model to represent the Hybrid Personality IPP Model
(Model A)

4.2 Online Evaluation
The online evaluation method involves the use of a survey that takes
the user features of a user as inputs and then through those inputs,
the model generates a list of song recommendations. With this,
users are tasked to compare the song recommendations for model
A(Hybrid) and model B (Pure CF) by marking the songs in the list
that they like. Then, they are tasked to answer a second survey
related to the recommendation quality (Q1), diversity (Q2), and user
satisfaction (Q3) of the two lists, and compare which list has better
recommendations and/or is more diverse. Respondents were also
asked to like songs that were recommended to them by the two
models. After this, another survey was conducted to determine the
quality and diversity of the recommendations of the two models. In
response to this, a t-test was conducted to determine the significant
difference between each question. The result is shown in Table 3.
Results show that Model A performs better than Model B in terms
of Recommendation Quality and User Satisfaction. In contrast to
this, Model B outperforms Model A in terms of Recommendation
diversity. Looking at the results, users think that model A has
better recommendation quality and is more satisfied with its rec-
ommendations, whilst the users would prefer model B in terms of
diversity. Together with this, a chi-test is conducted for the last
two questions, wherein the respondents are asked which of the two
lists have better recommendation quality, and which list is more
diverse. Shown below is the table for Observed and Expected values.
Observed values are the data collected from the respondents whilst
Expected values are the calculated values. The result is shown in
table 5.

---

<!-- PAGE 6 -->

WSSE 2025, October 24–26, 2025, Okayama, Japan

Joel de Goma et al.

Table 3: Model Metrics Comparison (Train)

Recommendation Quality

Recommendation Diversity

User Satisfaction

Mean
P(T<=t) two-tail

AQ1
3.7
0.428290293

BQ1
3.4

AQ2
3.75

BQ2
3.95

AQ3
4.15
0.518979715

BQ3
3.55

Table 4: Chi-Test Result (Observed)

LCQ1
LCQ2
TOTAL

A

14
3
17

B

4
12
16

Hard to Tell

TOTAL

2
5
7

20
20
40

4.3 Precision and Recall
Both models initially produced recommendations with no varia-
tion due to the limited song dataset, this also has the benefit of
making it easier to identify how the incorporation of personality
and other genre features influence the quality and diversity of the
recommendations. Pure collaborative systems such as Model B,
which solely relies on interaction counts, generated the same set
of recommendations based on its overall popularity among the
users included in the dataset. The recommendation list is therefore
shown to favor older tracks due to inherent popularity bias and
does not adjust based on the provided information such as genre
and sonic features. In contrast, Model A has personality-based IPPs
alongside sonic metadata and genre preferences, which enables it
to tailor recommendations even with the limited dataset. Despite
the number of users increasing (Dataset A vs Dataset B), Model
A was still not able to create more variations. This may be due to
the limited number of songs that the user must choose from (100
songs) in the creation of the dataset. For instance, newer songs
like Vampire (absent from the 2011 MSD dataset due to zero prior
interactions) appeared in the Top 10 by leveraging feature similari-
ties to other tracks already popular among Mapuan students. This
has an unintended effect of making it appear less ”diverse” to users
since the recommended songs are likely to be more specific and
like each other as which explains the discrepancy between opinion
and metrics-based diversity.

Based on the individual songs feedback for the models’ recom-
mendations, the computed precision and recall values also indicate
that Model A outperforms Model B in terms of recommendation
quality and diversity which is even more apparent when there is
more information available in the dataset. Model A has an average
precision value that is 0.13 higher than Model B, which indicates
that even with no variation, it has greater accuracy in adjusting
the ranking to prioritize items users liked based on the provided
IPP features. While in the survey itself, the new respondents seem
to perceive Model B as more diverse and have more quality, the
computed average recall metrics suggest that Model A also per-
forms better in generating lists that represent a wider coverage to
represent variations in user preferences. As a result, Model A is
also consistently shown to have higher F1 scores, especially with an
increase in dataset size, which is a good indicator that the perceived

recommendation quality is consistent with the actual quality of the
recommender which is based on the user’s explicit likes.

5 Conclusion and Recommendation
Overall, the researchers accomplished the primary objective of this
study which is to develop a personality-based IPP recommender
system as well as effectively demonstrate its potential compared to
traditionally pure collaborative filtering recommenders even with
the limitations of dataset skewness and sparsity. In both offline
and online evaluation, hybrid models outperform pure CF models
in both computed metrics (Precision, Recall, AUC, and F1 Score)
as well as user-prompted feedback (for Recommendation Quality
and Diversity). The output recommendations also suggest that the
hybrid model achieved a better balance between relevance and
diversity by leveraging personality alongside genre and sonic fea-
tures to find emergent patterns when combining user, song, and
interaction features. To explore the idea more effectively, the re-
searchers recommend acquiring even more samples for the model
to learn from and fix the issues that arise from overfitting, specif-
ically more songs for the user to evaluate in creating the dataset
and increasing the number of respondents for the dataset. Feature
engineering could also be amended to achieve a more reasonable
balance between popular and diverse items with the incorpora-
tion of personality-based IPPs. Future research can also explore
alternative methods for incorporating personality data, such as us-
ing other recommender libraries such as scikit instead of LightFM
which would have a different method for handling the user-item in-
formation matrix and could potentially lead to better performance.

References
[1] M. Kleć, A. Wieczorkowska, K. Szklanny, and W. Strus. 2023. Beyond the Big Five
personality traits for music recommendation systems. EURASIP Journal on Audio,
Speech, and Music Processing 2023, 1 (2023). DOI:https://doi.org/10.1186/s13636-
022-00269-0.

[2] H. Alharthi. 2015. The Use of Items Personality Profiles in Recommender Sys-
tems. Retrieved February 2, 2024 from https://ruor.uottawa.ca/server/api/core/
bitstreams/59170a9c-2a13-4ad6-baa5-.

[3] H. Li. 2023. Music depth recommendation algorithm based on user data mining.
In Proceedings of the 2023 International Conference on Electronics and Devices,
Computational Science (ICEDCS) (Marseille, France), 630–634. DOI:https://doi.
org/10.1109/ICEDCS60513.2023.00121.

[4] F. Lu and N. Tintarev. 2018. A Diversity Adjusting Strategy with Personality for

Music Recommendation, 7–14.

---

<!-- PAGE 7 -->

Using Item Personality-Based Profiling in Music Recommender Systems

WSSE 2025, October 24–26, 2025, Okayama, Japan

Table 5: Matrix Comparison

Model A
Model B

Precision

0.57
0.41

Recall

0.62
0.46

F1 Score

0.58
0.40

[5] A. Garg, V. Chaturvedi, A. B. Dhindsa, V. Varshney, and A. Parashar. 2022. Ma-
chine learning model for mapping of music mood and human emotion based on
physiological signals. Multimedia Tools and Applications 81. Advance online
publication. DOI:https://doi.org/10.1007/s11042-021-11650-0.

[6] R. P. Joy, M. R. Thanka, J. P. M. Dhas, and E. B. Edwin. 2023. Music Mood Based
Recognition System Based on Machine Learning and Deep Learning. International
Journal of Intelligent Systems and Applications in Engineering 11, 2 (2023),
904–911.

[7] L. Delando, S. Moreira Júnior, G. Ribeiro, E. Cabral, and G. Ribeiro. n.d. Correlating
Big Five Primary Personality Dimensions with Musical Preferences. Retrieved

February 3, 2024 from https://sol.sbc.org.br/index.php/sbcm/article/download/
19433/19261/.

[8] A. Dorochowicz, A. Kurowski, and B. Kostek. 2020. Employing subjective tests
and deep learning for discovering the relationship between personality types
and preferred music genres. Electronics 9, 12 (2020), Article 2016.

[9] R. Liu and X. Hu. 2020. A Multimodal Music Recommendation System with
Listeners’ Personality and Physiological Signals. DOI:https://doi.org/10.1145/
3383583.3398623.

[10] F. Lu and N. Tintarev. 2018. A Diversity Adjusting Strategy with Personality for

Music Recommendation, 7–14.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

| Using | Item | Personality-Based |     | Profiling | in Music | Recommender |
| ----- | ---- | ----------------- | --- | --------- | -------- | ----------- |
Systems
|                     | JoeldeGoma      |     | JanNielsenAnonuevo  |            |     | GianNicolePangan    |
| ------------------- | --------------- | --- | ------------------- | ---------- | --- | ------------------- |
| SCHOOLOFINFORMATION |                 |     | SCHOOLOFINFORMATION |            |     | SCHOOLOFINFORMATION |
|                     | TECHNOLOGY      |     |                     | TECHNOLOGY |     | TECHNOLOGY          |
|                     | MapuaUniversity |     | MapuaUniversity     |            |     | MapuaUniversity     |
Makati,MetroManila,Philippines Makati,MetroManila,Philippines Makati,MetroManila,Philippines
jcdegoma@mapua.edu.ph jndanonuevo@mymail.mapua.edu.ph gnlpangan@mymail.mapua.edu.ph
|     |     | JohnJovanielDeang             |     |                     | AlbertoVillaluz |     |
| --- | --- | ----------------------------- | --- | ------------------- | --------------- | --- |
|     |     | DepartmentofPhysicalEducation |     | SCHOOLOFINFORMATION |                 |     |
andAthletics TECHNOLOGY
|          |     | MapuaUniversity                |     |                                | MapuaUniversity |     |
| -------- | --- | ------------------------------ | --- | ------------------------------ | --------------- | --- |
|          |     | Makati,MetroManila,Philippines |     | Makati,MetroManila,Philippines |                 |     |
|          |     | jjcdeang@mapua.edu.ph          |     | acvillaluz@mapua.edu.ph        |                 |     |
| Abstract |     |                                |     | 1 Introduction                 |                 |     |
Musicrecommendersystemsplayanessentialroleingivingmusic Withtheincreasingadoptionofmusicsubscriptionserviceswithin
suggestionsinaccordancetoauser’sliking.However,therearetwo thecommunity,recommendersystemsplayacrucialroleinsuggest-
commonproblemswithregardstorecommendationalgorithms, ingsongsthatalignwiththeuser’sinterests. However,addressing
namelyuservariabilityandthecoldstartproblem. Withthis,the uservariabilityandovercomingthecold-startproblempresents
researchers aim to address the said problems by incorporating significantchallengesfortraditionalrecommendationalgorithms.
personality profiles to aid in giving music recommendations in Users’musicpreferencescanbediverseandmultifaceted,makingit
accordancetoauser’sinterests.ThestudymadeuseoftheLightFM difficultforthesealgorithmstoaccuratelycapturetheirpreferences
| Modeltoincorporatetheuser’stopfivefavoritegenresandbig |     |     |     | [1]. |     |     |
| ------------------------------------------------------ | --- | --- | --- | ---- | --- | --- |
fivepersonalityscores,henceusingahybridapproach.Thehybrid Theresearcherswillfocusontheeffectivenessofproportion-
modelisthencomparedwiththetraditionalcollaborativefiltering basedIPPstowardspersonality-basedmusicrecommendersystems.
modelwithcertainmetricstodetermineitsperformance.According ThecurrentstudybyAlharthifocusesontheuseoftherecom-
totheresults, thehybridmodeloutperformsthetraditionalCF mendersystemsingeneral,andwiththis,theresearchersintend
model,provingthatincorporatingpersonalityprofilescanimprove toapplythesaidapproachtomusicrecommendersystems[2].[3]
theaccuracyofthemodelingivingmusicsuggestionstoauser. suggeststhatitem-basedrecommendersystemsperformbetterin
termsofrating-basedCFrecommendersystems.Referencingthe
CCSConcepts saidstudy,theresearchersintendtoexploremoreonitem-based
recommendersystems.
•ComputingMethodologies;•Machinelearning;•Machine
Asthestudywillrevolvearoundtheuseofpersonality-based
learningapproaches;•Neuralnetworks;
musicrecommendationsystems,certaingapsareintendedtobe
addressed.Onlyafewstudieshaveexploredtheuseofpersonality-
Keywords
basedmusicrecommendersystemsasmostresearchwouldfocus
RecommenderSystems,CollaborativeFiltering,LightFM
|     |     |     |     | onmoodandemotion. |     | Lisuggeststhatpersonalityisoneofthe |
| --- | --- | --- | --- | ----------------- | --- | ----------------------------------- |
factorsthatdeterminesone’smusicalpreferences,besidesmood
ACMReferenceFormat:
andemotion[3].Withthis,theresearchersintendtoaddressthe
JoeldeGoma,JanNielsenAnonuevo,GianNicolePangan,JohnJovaniel
gapspresentedbythepersonality-basedrecommendersystemand
Deang,andAlbertoVillaluz.2025.UsingItemPersonality-BasedProfiling
inMusicRecommenderSystems. In2025The7thWorldSymposiumon thatisitsissueswithitsaccuracy. Researcherstendtoaddress
SoftwareEngineering(WSSE2025),October24–26,2025,Okayama,Japan. thisproblembyintegratingthesystemwithcurrentcollaborative
ACM,NewYork,NY,USA,7pages.https://doi.org/10.1145/3779657.3779698 filteringmethods. [1]foundthathavingaBigFivepersonality-
basedmusicrecommendationsystemhadcertainpersonalitybiases
thatmadetheresultsirrelevant.Withthis,theresearchersintendto
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor proposeanewapproachregardingpersonality-basedrecommender
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
systemsthatusetheBigFivemodel.AsAlharthi’sstudyproduces
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.Copyrightsforthird-partycomponentsofthisworkmustbehonored. promisingresults,theresearchersbelievethatthesaidstudycan
Forallotheruses,contacttheowner/author(s). beincorporatedwithmusicrecommendersystemsusingtheBig
WSSE2025,Okayama,Japan
Fivepersonalitymodelwhichcouldlessenerrorsposedusingthe
©2025Copyrightheldbytheowner/author(s).
BigFivemodel.
ACMISBN979-8-4007-1577-8/2025/10
https://doi.org/10.1145/3779657.3779698
271

WSSE2025,October24–26,2025,Okayama,Japan JoeldeGomaetal.
2 ReviewofRelatedLiterature accuracyscoresofstate-of-the-artrecommendationalgorithmsand
Manyrecentstudiesinsentimentanalysisgavesignificantriseto exploresuserbiasrelatedtopersonalitytraits.Themethodologyin-
MachineLearningalgorithms.Whiletherehasbeenmuchresearch volvesdatacleaning,personalityestimation,anddatasegmentation
onTraditionalMachineLearningmodelsspecificallyontheOnline fortrackandartistinformationextraction. SparseLinearMeth-
Learningdataset,onlyafewstudieshavetakenintoconsideration ods,EmbarrassinglyShallowAutoencoders(EASE),andVariational
DeepLearningmodels.Thishasbeenattributedtotheexceptional Autoencoders(Mult-VAE)areutilizedforanalysis. Thereported
accuracyoftraditionalmodels. recallvaluesatdifferentpositions(5,10,and15)provideinsights
Lu&Tintarev’sstudyfocusesonaddressingthecold-startprob- intoalgorithmperformancebasedonusers’personalitytraits.For
lemamongstrecommendersystems.Withthis,theirpaperfocuses instance,atRecall@5,EASEachieved0.0366,SLIMachieved0.0334,
ongivingbetterrecommendationsbyre-rankingthesuggestions andMult-VAEachieved0.0433. Theseratesindicatethepropor-
bytherecommenderandimprovingtheaccuracyofthemodelby tionofrelevantitemsretrievedbythealgorithmsatthespecified
integrationofpersonalitytraits. Theirresultssuggestedthatthe positions.Thestudyrecognizesitslimitations,suchasgeneraliz-
saidfocuspointsofthepaperhavebeenmet,whereinpersonalized abilityanddatacompletenessissues,andoutlinesfutureresearch
recommendationlistsarehigherindiversityandleadtoanincrease directionstobetterunderstandthecausesofbiasesandexplore
inusersatisfaction[4]. additionalaspectsofrecommendationqualitybeyondaccuracy.
Klecetal’sstudiedhowpersonalitytraitscanhaveaninfluence Delando&et.al.[7]iscenteredaroundtheMBTI,utilizingthe
onmusicrecommendationerror. Thestudycollectedresponses MARSYASDatasetalongwiththeExtendedandSDatasets,the
from279participantstogathertheirlisteningtraitsandtheirper- studyaimstopredictpersonalitytraits,specificallyextraversion
sonality profiles. With this data, the combination between the and introversion, based on individuals’ music preferences. The
personalitytraitsandtheaudiofeaturesfromthesongswerestud- methodologyinvolvesdatacollection,dimensionalityreduction,
iedtoarriveataconclusionwithregardstomusicrecommendation normalization,andsegmentationbasedon”PersonalityType.”Au-
error.Findingssuggestedthatsomepersonalityfacetshadyielded dioframesaresegmented,andfeaturesareextractedusingMIRtool-
thelowestrecommendationerrorforBFI-2,comparedtothehigher boxandavariationalautoencoder.SupportVectorMachine(SVM),
orderofthebigfivepersonalitytraits. Theresearchershadcon- RandomForest,K-NearestNeighbors(KNN),andNaiveBayesclas-
cludedthatthisdiscoverycanhelpotherresearcherstofilterthe sifiersareemployedforanalysis. TheSVMclassifierachievesa
personalityquestionnairedowntoonlytheessentialquestionsto performancerateof71%,showcasingitseffectivenessinpredicting
beusedingatheringthepersonalityprofilesoftheuserstopredict personalitytraitsbasedonmusicpreferences. Furthermore,the
theirlisteninghabits[1]. studyexploresthecorrelationbetweenmusicgenresandperson-
Garg&et. al. [5]focusesondevelopingamusicmood-based alitytypes,revealingascoringdistributionof53%forextraverts
recommendationsystemusingmachinelearninganddeeplearning and47%forintroverts,sheddinglightonthenuancedrelationship
techniques,withaparticularemphasisonaddressingthecommon betweenmusicpreferencesandpersonalitytraits.
strugglepeoplefaceinfindingmusicthatmatchestheirmoodor Dorochowicz[8]isfocusedonexploringemotionsandphysiolog-
emotions. TheresearchutilizestheFERPlusdatasetandSpotipy, icalsignals,utilizedtheDEAMandPMEmodatasetstoinvestigate
aPythonlibraryforSpotify,forwebscrapinganddatamanipula- theintricaterelationshipbetweenmusicandhumanemotions.The
tion.TheValence-Arousaltheoryisemployedtoclassifythesong researchaimedtoquantifythisconnectionanddevelopamachine
databaseintomoodquadrants,andK-Meansclusteringisusedfor learningmodelcapableofpredictingbothmusicmoodbasedon
furthercategorization.Featuressuchasvalence,energy,danceabil- audiosignalsandhumanemotionbasedonphysiologicalsignals.
ity,loudness,tempo,speechiness,instrumentalness,andpopularity Themethodologyinvolveddownscaling,formatconversion,reg-
areconsidered. ADeepConvolutionalNeuralNetwork(CNN)is ularization,andshrinkage,withfeatureextractionencompassing
employedforclassification,withvaryingaccuraciesreportedfor zero-crossingrate,energy,entropyofenergy,andvariousspectral
differentmodelsandemotions.Themodelaimstoproviderealtime features.Machinelearningmodels,suchasSVM,RandomForest,
playlistrecommendationsbasedonmood,contributingtomood DecisionTree,ExtraTree,k-NN,MLP,AdaBoost,ElasticNet,Ridge,
enhancementthroughAI-drivensongselection. Thestudysug- Lasso,andAdaptiveBoost,wereemployedforanalysis. ANOVA
geststhatthismethodsurpassesgenreclassificationinaccuracy, resultsindicatedsignificantvariancebetweenpeopleanditems,
withpotentialapplicationsinimprovingsocialnetworkingand emphasizingindividualizedemotionalresponsestomusic.TheRan-
customersatisfaction. Thereportedaccuracypercentagesinclude domForestmodeldemonstratednotableperformanceintermsof
below65%foraSimpleCNNwithsixemotions,above70%fora actioncallcountandtrainingtime.Thearousalandvalenceanaly-
SimpleCNNwithfouremotions,below72%foraDeepCNNwith sisrevealeddistinctemotionalresponsesassociatedwithdifferent
sixemotions,andabout80%foraDeepCNNwithfouremotions. musicmoods.Theresearchachievedanaccuracyrateof81%,un-
Losspercentages,basedon60%trainingdataand50%validation derscoringthepracticalpotentialofthedevelopedmodel,including
data,decreaseto30%orbelowasthenumberofepochsincreases personalizedplaylistgeneration.However,thestudyacknowledged
forbothtrainingandvalidationdata. theneedforfurtherresearchandrefinementtoenhanceaccuracy
Joy & et. al. [6] is rooted in the Big Five Model, leverages andbroadenthescopeofemotionrecognition.
dataobtainedfromTwitter,encompassing395,056listeningevents, Liu&et.al.[9]utilizesadatasetfromthemyPersonalityweb-
18,310userswithpersonalityvalues,and15,753uniquetracks.The site,aimedtodevelopanalgorithmtodetermineindividuals’music
researchinvestigateshowusers’personalitytraitsinfluencethe tastesbasedontheirpersonalitytraits.Theapproachinvolvedcon-
vertingFacebookstatusupdatesintovectorrepresentation.Various
272

UsingItemPersonality-BasedProfilinginMusicRecommenderSystems WSSE2025,October24–26,2025,Okayama,Japan
Figure1:ProposedModelWorkflow
recommendationmodels,includingNaiveBayesClassifierandcol- 3.1 DataCollection
laborativefilteringmethods,wereemployed.Therecommendation Thedatacollectionprocesswillbeconductedintheformofasurvey.
model’sperformancewasassessedusingRootMeanSquaredError Thesurveywillbeusedfortheexplicitgatheringoftheinformation
(RMSE),withMatrixFactorizationachievingthelowestRMSEat requiredforbuildingthethreematrices(user,item,interaction)that
0.88. F-MeasuresforBigFivePersonalityClasses,includingOpen- willbeusedfortheLightFMHybridModel.Thequestionnairewill
ness (0.2308), Conscientiousness (0.4865), Extraversion (0.6349), haveacombinedtotalof111questionsconsistingofthe10-item
Agreeableness(0.5000), andNeuroticism(0.6154), werealsocal- BFIQuestionnaire(LikertScaleof1–5),100-itemSongRating(1as
culated. Therecommendationmodeloutperformeduser-to-user like,0asdislike),andPreferredGenreChecklist(10genreoptions,
collaborativefilteringwitharatingmatrix,althoughmatrixfac- choosingamaximumof5).
torizationremainedsuperior. Thestudyprovidedinsightsintothe
relationshipbetweenpersonalitytraitsandmusicpreferences,em-
phasizingthepotentialofpersonalizedrecommendationsystems.
Lu & et. al. [10] utilizes the myPersonality dataset and the
3.2 DATAPRE-PROCESSING
PsychoFlickrdataset,focusedondevelopinganemotionalrecom-
mendersystemthatpredictsmusictastebasedonpersonalitytraits. 3.2.1 UserPersonalityProfile. Therespondents’answerstothe
Theuserrecognitionproblemswerecategorizedintofivebinary BigFiveInventory(BFI)willthenundergoamulti-stepprocess
classificationsandfurtherdividedintoclasses(low,medium,high). withonlytheresultingT-scorebeingstoredinthedataset. First,
ForwardFeaturesSelectionwith10-foldcross-validationwasem- rawscoresarecalculatedforeachofthefivecoredimensions(Ex-
ployed, and various classifiers, including Naive Bayes, Logistic traversion,Neuroticism,Agreeableness,Conscientiousness,and
Regression,SVM,RandomForest,andGBTwithdeepnetworks, Openness)bysumminganindividual’sresponsestotherelevant
wereused.TheaccuracyresultsforthemyPersonalitydatasetusing questionnaireitems. Theserawscoresarethentransformedinto
theproposedapproachwereO-0.71,C-0.72,E-0.75,A-0.73, thevariable“userBFdimensionmean”whichisusedtocontrol
N-0.71.Theself-assessedaccuracyresultsforthemyPersonality forpotentialdiscrepanciesinquestiondifficultyandestablishesa
datasetwerelower(O-0.54,C-0.55,E-0.54,A-0.54,N-0.54).For standardizedbaselineforcomparison.Thisiscomputedbydividing
thePsychoFlickrdataset,theproposedapproachachievedaccura- theitemscoresbythenumberofquestionsassociatedwitheach
ciesofO-0.61,C-0.59,E-0.56,A-0.60,N-0.61.Theself-assessed dimension.FollowingthecalculationofuserBFdimensionmeans,
accuracyresultswereagainO-0.54,C-0.55,E-0.54,A-0.54, theBFIemploysstandardizationprocedurestofacilitatemeaning-
N-0.54.Theexperimentsdemonstratedthesuccessofusinguser fulcomparisonsacrossindividualsandpopulations.Z-scoresare
personalityformoodrecognitioninpredictingmusictaste,urging derivedtorepresentthedeviationofanindividual’sscorefromthe
furtherexplorationinthisfield. averagepopulationscoreforaspecifictrait,expressedintermsof
standarddeviations.Finally,forenhancedinterpretability,Z-scores
areconvertedintoT-scoreswithameanof50andastandarddevi-
ationof10.Thiswillresultin5T-scores,whichwillbeconverted
intodegreestocategoricallyrepresenttheuser’spersonalityprofile.
ABFscoreisstoredas“high”ifitisgreaterthan55,“low”ifitis
3 Methodology
lowerthan45,oraverageotherwiseasdemonstratedinTable1.
Asshowninfigure1theprocedureindevelopingandevaluating ThiswillberepresentedintheappropriateformatshowninTable
themodel. 2tomakeitcompatibleasauser-featureembedding.
273

WSSE2025,October24–26,2025,Okayama,Japan JoeldeGomaetal.
3.2.2 Item Features. The researchers will incorporate the whichofthetwolossfunctions(BPRandWARP)willperformbet-
proportion-basedIPPmethodusedin[2]wheretheitempersonal- teronofflineevaluationbeforefinalizingthemodeltobeevaluated
ityprofileisrepresentedinvectorform,consistingof15features. bynewusers. Thesetwolossfunctionswerechosenforevaluation
Eachdimensionisrepresentedbythreefeaturesthatcorrespond sincebothareparticularlyusefulincaseswhereonlypositiveinter-
to degrees (low, average, and high) The value of one feature is actions(likes)arerecordedbutwithdifferentoptimizations.WARP
theproportionofuserswholikeaniteminthedegreeofoneBF issuitedforoptimizingthetoprecommendationlist,whileBPRis
dimensionwhichiscalculatedbasedonthefollowingformula: moresuitedforoptimizingtheAUCscore.Formodelevaluation,
Proportion=(totalNumberofUserswholikedtheItemandhas thekvalueissetto10toevaluateitsperformancewhengenerating
thesameBFdegree)/(totalNumberofUserswhoLikedtheItem). thetop10recommendations.
SpotifyAPIwillbeusedtoextractcontent-basedfeaturestobe
usedalongsidetheitempersonalityprofileasitemfeatureweights. 3.4 ModelValidationandEvaluation
Insteadofthemusicalandthestandardfeatures(bpm,tempo,re-
Theresearcherswillusethebuilt-inevaluationmetricsprovided
leasedate,volume)thatarecommonlycoveredinexistingstudies,
bytheLightFMlibrary. Thesemetricscanbecollectivelyusedto
thestudywillfocusonextractingthefollowingsonicalcomponents
assessthemodel’sperformancebycomputingtheseforthetraining
orfeaturesthatquantitativelydescribeaspectsthatcontributeto
andtestsplitoftheinteraction’smatrix.Themetricstobeusedwill
theoverallsoundandmoodofthesong,whichareAcousticness,
betheROCAUCScore,Precision,Recall,andF1-score.ROCAUC
Danceability,Energy,Instrumentalness,Liveness,andValence.
Scorequantifiestheprobabilitythatarandomlyselectedpositive
examplewillhaveahigherscorethanarandomlychosennegative
3.2.3 Interaction Matrix. The interactions matrix will store
example. Itmeasuresthemodel’sabilitytorankpositiveexamples
recordedinteractionsforallusers.Thiswillcomprisethreecolumns,
higherthannegativeexamples.Aperfectscoreis1.0,indicatingop-
twoofwhichareforeignkeysthatlinktoboththeuserfeatures
timalperformanceindistinguishingbetweenpositiveandnegative
matrix(UserID)andsongfeaturesmatrix(songID).TheisLiked
examples. Precisionatkmeasuresthefractionofrelevantitems
columnisusedtorepresentinteractionsaseither1or0.Toaccount
amongthetopkitemsrecommendedbythesystem.Itevaluatesthe
forthedifferencesbetweenthewayinteractionsarestoredinthe
precisionoftherecommendationsbyconsideringhowmanyofthe
surveydatasetandtheMillionSongDataset(MDS),anadditional
toprecommendationsarerelevanttotheuser.Aperfectscoreis1.0,
column Weight will be used as an additional feature for model
indicatingthatalltopkrecommendationsarerelevanttotheuser’s
training,assigningdifferentlevelsofimportancedependingonthe
preferences. Recallatkevaluatesthesystem’sabilitytoretrieve
valueofaspecificinteraction. AllinteractionsfromtheMapuan
allrelevantitemsamongthetopkrecommendations. Itmeasures
studentswillautomaticallybeassignedthehighestvalue(5)since
theproportionofrelevantitemsthataresuccessfullyretrievedby
theserepresentexplicitlylikedsongsfromtheprovidedsonglist.
thesystemcomparedtoallrelevantitemsinthedataset.Aperfect
MDS user interactions on the other hand are in the form of
scoreis1.0,indicatingthatallrelevantitemsareretrievedamong
playcountsinsteadoflikeswhichrequireadifferentapproach.The
thetopkrecommendations.
researchersemployedamin-maxscalingtransformtonormalizethe
TheproposedhybridmodelasshowninProcedureCwillalsobe
databetweenarangeof0-1.Thescaledvaluesarethenmultiplied
evaluatedagainstapurecollaborativefiltering(CF)model(based
by4androundedtothenearestintegertomapto5weightlevels.
onlyoninteractionswithoutincorporatingpersonalityIPPand
Thiswillallowthemodeltoprioritizelearningthecorrelatedsong
UPPfeatures)thatistrainedonthesamecombineddatasetand
featuresinsongswithhigherplaycountswhenusedasweights
parameters.
duringmodeltraining.
3.5 OnlineEvaluation
3.3 ModelDevelopment
Inadditiontothesemetrics,researcherswillalsoemployonline
A hybrid recommender system will be developed utilizing the evaluationmethodstoconductmodelcomparisonsfromtheper-
LightFMlibrarywhichintegrateselementsofbothcollaborative spectiveofnewuserswhosepersonalityandpreferencecounts
filteringandcontent-basedfiltering.Inthismodel,usersandsongs weren’tincludedinmodeltraining.Thiswillbeconductedinthe
arerepresentedbylatentfactorsandbiases,derivedfromuserat- formofawebapp,whichwillrequire20newuserstotakethe
tributes,itemattributes,andhistoricalinteractions. Specifically, personalitytestandinputtheirtop5genrepreferences.Thiswillbe
usersaredescribedthroughfeaturessuchasgenrepreferencesand usedtotesttheefficacyofgeneratingreal-timerecommendations
userpersonalityprofiles(BigFive)whilesongsarecharacterized beforeacquiringalistoftheirliked/dislikedsongs. Theuserswill
bytheirsonicfeaturesandthecomputedItemPersonalityProfiles thenbepresentedwiththegeneratedtop10recommendationsfrom
(IPPs). Withthedescribedpreprocessingandfeatureextraction thetwotrainedmodelswhichtheywillevaluateintheformofa
steps,personalityfeaturesaremoredeeplyintegratedintoboththe post-feedbackquestionnairewhichisadaptedfromastudyevalu-
useranditemfeaturematrix,particularlyinsituationswithlimited atingtheirpersonality-basedrecommendersystem(Luet.al,2018).
explicituser-iteminteractions.Thiswillbecombinedwiththesubs Moreover,userswillalsobeabletoindividuallyrateeachsongin
Forallmodels,researcherswilluseLightFM’scross-validation thegeneratedlistaslike/dislike.Thesemeasureswillbeprecision
featuretorandomlysplittheinteractionsetintotwodisjointtrain- and recall (like the dataset evaluation), and user feedback. For
ingandtestsetswithan80-20split.Themodelwillthenbefitted userfeedback,thesystemisevaluatedqualitativelybyprompting
for30epochsanda0.02learningrate.Theresearcherswillalsotest userstoexpresstheiropinionsonalllistsbasedonthethreemain
274

UsingItemPersonality-BasedProfilinginMusicRecommenderSystems WSSE2025,October24–26,2025,Okayama,Japan
Table1:ModelMetricsComparison(Train)
Metrics CollaborativeFiltering(CF) HybridBPR HybridWARP
Precision 0.24 0.16 0.23
Recall 0.86 0.02 0.75
AUCScore 1.00 0.67 0.82
F1Score 0.38 0.04 0.35
Table2:ModelMetricsComparison(Validation)
Metrics CollaborativeFiltering(CF) HybridBPR HybridWARP
Precision 0.48 0.42 0.46
Recall 0.74 0.22 0.64
AUCScore 0.56 0.53 0.57
F1Score 0.58 0.29 0.54
aspectsbasedonPu,Chen,andHu’s(2011)ResQueUser-Centric researchers,thehybridmodelthatusesWARPhasthebestperfor-
EvaluationFramework.Thesequestionsareintheformofa5-point manceonallmetrics. TheimprovedperformanceofWARPover
Likertscale(1beingstronglydisagreeand5beingstronglyagree), BPRmaybeduetothelimitationofpairwiselossfunctionwhen
withonequestioneachforbothmodelsbeingevaluatedwhichwill usedonrelativelysparseandimbalanceddata,withthedatasethav-
assessRecommendationQuality,RecommendationDiversityand ingcompleteuserpersonalityinformationforlessthan20%ofthe
UserSatisfaction. Respondentswillalsobeaskedwhichmodel overalluserbase.Moreover,itisespeciallysuitableforimprovinga
ismoresuitedforthemintermsofrecommendationqualityand recommender’sabilitytorankitems,whichiswhyitwaschosen
diversity. asthefinalmodeltorepresenttheHybridPersonalityIPPModel
(ModelA)
4 ResultandDiscussion
Theresearcherscollecteddatafrom208studentsandusedsaiddata 4.2 OnlineEvaluation
tofeedinformationintothemodel,generatingrecommendations Theonlineevaluationmethodinvolvestheuseofasurveythattakes
tailoredaccordingtotheirpersonalityscoresandgenrepreferences theuserfeaturesofauserasinputsandthenthroughthoseinputs,
formodelA(hybridmodel),andpopularity-basedrecommenda- themodelgeneratesalistofsongrecommendations. Withthis,
tionsformodelB(pureCFmodel).Theprecision,recall,AUC,and usersaretaskedtocomparethesongrecommendationsformodel
F1scoresarethencomputedtoevaluatethemetricsofthemodels, A(Hybrid)andmodelB(PureCF)bymarkingthesongsinthelist
forbothofflineandonlineevaluationmethods.Atwo-tailedt-test thattheylike. Then,theyaretaskedtoanswerasecondsurvey
andchi-squaredtestwerealsoconductedforthesurveyresultsfrom relatedtotherecommendationquality(Q1),diversity(Q2),anduser
theonlineevaluationmethodtoverifyhowstatisticallysignificant satisfaction(Q3)ofthetwolists,andcomparewhichlisthasbetter
theresultsare,withp<0.05. recommendationsand/orismorediverse.Respondentswerealso
askedtolikesongsthatwererecommendedtothembythetwo
4.1 OfflineEvaluation
models.Afterthis,anothersurveywasconductedtodeterminethe
Asshownintable1andtable2,purecollaborativefilteringmodel qualityanddiversityoftherecommendationsofthetwomodels.In
has the overall best performance metrics when it comes to the responsetothis,at-testwasconductedtodeterminethesignificant
trainingsetparticularlyforrecallandAUC.Thehigherdiscrepancy differencebetweeneachquestion.TheresultisshowninTable3.
betweenrecallandprecisionscoreforthismodel(alsoreferredto ResultsshowthatModelAperformsbetterthanModelBinterms
asModelB)isindicativeofthelimitationsofthiskindofrecom- ofRecommendationQualityandUserSatisfaction.Incontrastto
mendersinceitprioritizesbreadth/diversityofrecommendations this,ModelBoutperformsModelAintermsofRecommendation
as opposed to actual relevance(precision) with an emphasis on diversity. Looking at the results, users think that model A has
prioritizingsongswithmoreinteractions.Thedrasticdropinper- betterrecommendationqualityandismoresatisfiedwithitsrec-
formancewhencomparingthetrainingandvalidation/testsetfor ommendations,whilsttheuserswouldprefermodelBintermsof
thismodelalsoindicatesthatmodel’sdesignhasissueswithover- diversity. Togetherwiththis,achi-testisconductedforthelast
fittingandislesscapableofadaptingtounseendatacomparedto twoquestions,whereintherespondentsareaskedwhichofthetwo
bothvariantsofthehybridmodel. Overall,thehybridmodelsare listshavebetterrecommendationquality,andwhichlistismore
observedtohavegoodmetricswithnolargediscrepancybetween diverse.ShownbelowisthetableforObservedandExpectedvalues.
validationandtrainingset,whichindicatesthatitcanidentifypat- Observedvaluesarethedatacollectedfromtherespondentswhilst
ternsandtailorrecommendationsaccordinglyevenondatawith Expectedvaluesarethecalculatedvalues.Theresultisshownin
norecordedinteractions.Betweenthetwolossfunctionstestedby table5.
275

| WSSE2025,October24–26,2025,Okayama,Japan |     |     |     |     |     |     |     | JoeldeGomaetal. |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- |
Table3:ModelMetricsComparison(Train)
RecommendationQuality RecommendationDiversity UserSatisfaction
|                 | AQ1         |     | BQ1 | AQ2  |     | BQ2  | AQ3         | BQ3  |
| --------------- | ----------- | --- | --- | ---- | --- | ---- | ----------- | ---- |
| Mean            | 3.7         |     | 3.4 | 3.75 |     | 3.95 | 4.15        | 3.55 |
| P(T<=t)two-tail | 0.428290293 |     |     |      |     |      | 0.518979715 |      |
Table4:Chi-TestResult(Observed)
|       |     | A   |     | B   |     | HardtoTell | TOTAL |     |
| ----- | --- | --- | --- | --- | --- | ---------- | ----- | --- |
| LCQ1  |     | 14  |     | 4   |     | 2          | 20    |     |
| LCQ2  |     | 3   |     | 12  |     | 5          | 20    |     |
| TOTAL |     | 17  |     | 16  |     | 7          | 40    |     |
4.3 PrecisionandRecall recommendationqualityisconsistentwiththeactualqualityofthe
Bothmodelsinitiallyproducedrecommendationswithnovaria- recommenderwhichisbasedontheuser’sexplicitlikes.
tionduetothelimitedsongdataset,thisalsohasthebenefitof
5 ConclusionandRecommendation
makingiteasiertoidentifyhowtheincorporationofpersonality
andothergenrefeaturesinfluencethequalityanddiversityofthe Overall,theresearchersaccomplishedtheprimaryobjectiveofthis
| recommendations. | PurecollaborativesystemssuchasModelB, |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
studywhichistodevelopapersonality-basedIPPrecommender
whichsolelyreliesoninteractioncounts,generatedthesameset
systemaswellaseffectivelydemonstrateitspotentialcomparedto
| of recommendations | based | on its overall | popularity | among the |     |     |     |     |
| ------------------ | ----- | -------------- | ---------- | --------- | --- | --- | --- | --- |
traditionallypurecollaborativefilteringrecommendersevenwith
usersincludedinthedataset. Therecommendationlististherefore thelimitationsofdatasetskewnessandsparsity. Inbothoffline
showntofavoroldertracksduetoinherentpopularitybiasand andonlineevaluation,hybridmodelsoutperformpureCFmodels
doesnotadjustbasedontheprovidedinformationsuchasgenre
inbothcomputedmetrics(Precision,Recall,AUC,andF1Score)
andsonicfeatures.Incontrast,ModelAhaspersonality-basedIPPs
aswellasuser-promptedfeedback(forRecommendationQuality
alongsidesonicmetadataandgenrepreferences,whichenablesit
andDiversity).Theoutputrecommendationsalsosuggestthatthe
totailorrecommendationsevenwiththelimiteddataset.Despite
|     |     |     |     |     | hybrid | model achieved a | better balance between | relevance and |
| --- | --- | --- | --- | --- | ------ | ---------------- | ---------------------- | ------------- |
thenumberofusersincreasing(DatasetAvsDatasetB),Model diversitybyleveragingpersonalityalongsidegenreandsonicfea-
Awasstillnotabletocreatemorevariations.Thismaybedueto
turestofindemergentpatternswhencombininguser,song,and
thelimitednumberofsongsthattheusermustchoosefrom(100
|                                  |     |     |                        |     | interactionfeatures. | Toexploretheideamoreeffectively,there- |     |     |
| -------------------------------- | --- | --- | ---------------------- | --- | -------------------- | -------------------------------------- | --- | --- |
| songs)inthecreationofthedataset. |     |     | Forinstance,newersongs |     |                      |                                        |     |     |
searchersrecommendacquiringevenmoresamplesforthemodel
likeVampire(absentfromthe2011MSDdatasetduetozeroprior
tolearnfromandfixtheissuesthatarisefromoverfitting,specif-
interactions)appearedintheTop10byleveragingfeaturesimilari- icallymoresongsfortheusertoevaluateincreatingthedataset
tiestoothertracksalreadypopularamongMapuanstudents.This andincreasingthenumberofrespondentsforthedataset.Feature
hasanunintendedeffectofmakingitappearless”diverse”tousers
engineeringcouldalsobeamendedtoachieveamorereasonable
sincetherecommendedsongsarelikelytobemorespecificand
balancebetweenpopularanddiverseitemswiththeincorpora-
likeeachotheraswhichexplainsthediscrepancybetweenopinion
|     |     |     |     |     | tionofpersonality-basedIPPs. |     | Futureresearchcanalsoexplore |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | ---------------------------- | --- |
andmetrics-baseddiversity. alternativemethodsforincorporatingpersonalitydata,suchasus-
Basedontheindividualsongsfeedbackforthemodels’recom- ingotherrecommenderlibrariessuchasscikitinsteadofLightFM
mendations,thecomputedprecisionandrecallvaluesalsoindicate
whichwouldhaveadifferentmethodforhandlingtheuser-itemin-
thatModelAoutperformsModelBintermsofrecommendation
formationmatrixandcouldpotentiallyleadtobetterperformance.
qualityanddiversitywhichisevenmoreapparentwhenthereis
moreinformationavailableinthedataset.ModelAhasanaverage
References
precisionvaluethatis0.13higherthanModelB,whichindicates
[1] M.Kleć,A.Wieczorkowska,K.Szklanny,andW.Strus.2023.BeyondtheBigFive
thatevenwithnovariation,ithasgreateraccuracyinadjusting
personalitytraitsformusicrecommendationsystems.EURASIPJournalonAudio,
therankingtoprioritizeitemsuserslikedbasedontheprovided Speech,andMusicProcessing2023,1(2023).DOI:https://doi.org/10.1186/s13636-
| IPPfeatures.Whileinthesurveyitself,thenewrespondentsseem |     |     |     |     |     | 022-00269-0. |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- |
[2] H.Alharthi.2015.TheUseofItemsPersonalityProfilesinRecommenderSys-
toperceiveModelBasmorediverseandhavemorequality,the tems.RetrievedFebruary2,2024fromhttps://ruor.uottawa.ca/server/api/core/
computedaveragerecallmetricssuggestthatModelAalsoper- bitstreams/59170a9c-2a13-4ad6-baa5-.
[3] H.Li.2023.Musicdepthrecommendationalgorithmbasedonuserdatamining.
formsbetteringeneratingliststhatrepresentawidercoverageto
InProceedingsofthe2023InternationalConferenceonElectronicsandDevices,
| representvariationsinuserpreferences. |     |     | Asaresult,ModelAis |     |     |     |     |     |
| ------------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ComputationalScience(ICEDCS)(Marseille,France),630–634.DOI:https://doi.
alsoconsistentlyshowntohavehigherF1scores,especiallywithan org/10.1109/ICEDCS60513.2023.00121.
increaseindatasetsize,whichisagoodindicatorthattheperceived [4] F.LuandN.Tintarev.2018.ADiversityAdjustingStrategywithPersonalityfor
MusicRecommendation,7–14.
276

UsingItemPersonality-BasedProfilinginMusicRecommenderSystems WSSE2025,October24–26,2025,Okayama,Japan
Table5:MatrixComparison
|        | Precision | Recall | F1Score |
| ------ | --------- | ------ | ------- |
| ModelA | 0.57      | 0.62   | 0.58    |
| ModelB | 0.41      | 0.46   | 0.40    |
[5] A.Garg,V.Chaturvedi,A.B.Dhindsa,V.Varshney,andA.Parashar.2022.Ma- February3,2024fromhttps://sol.sbc.org.br/index.php/sbcm/article/download/
| chinelearningmodelformappingofmusicmoodandhumanemotionbasedon |     | 19433/19261/. |     |
| ------------------------------------------------------------- | --- | ------------- | --- |
physiologicalsignals.MultimediaToolsandApplications81.Advanceonline [8] A.Dorochowicz,A.Kurowski,andB.Kostek.2020.Employingsubjectivetests
publication.DOI:https://doi.org/10.1007/s11042-021-11650-0. anddeeplearningfordiscoveringtherelationshipbetweenpersonalitytypes
[6] R.P.Joy,M.R.Thanka,J.P.M.Dhas,andE.B.Edwin.2023.MusicMoodBased andpreferredmusicgenres.Electronics9,12(2020),Article2016.
RecognitionSystemBasedonMachineLearningandDeepLearning.International [9] R.LiuandX.Hu.2020.AMultimodalMusicRecommendationSystemwith
JournalofIntelligentSystemsandApplicationsinEngineering11,2(2023), Listeners’PersonalityandPhysiologicalSignals.DOI:https://doi.org/10.1145/
| 904–911. |     | 3383583.3398623. |     |
| -------- | --- | ---------------- | --- |
[7] L.Delando,S.MoreiraJúnior,G.Ribeiro,E.Cabral,andG.Ribeiro.n.d.Correlating [10] F.LuandN.Tintarev.2018.ADiversityAdjustingStrategywithPersonalityfor
BigFivePrimaryPersonalityDimensionswithMusicalPreferences.Retrieved MusicRecommendation,7–14.
277