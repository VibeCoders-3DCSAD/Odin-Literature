---
conversion_metadata:
  converted_at: "2026-07-22T13:26:23Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Gomez et al.pdf"
  source_pdf_sha256: "224c00e02e3f67888cd5e59271807b224c320c718f7a7cf0a956b1c92cda3ae2"
  page_count: 9
  markdown_char_count: 103123
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Modeling Personality Traits by Predicting Questionnaire Responses as an
Alternative Approach to Filipino Automatic Personality Recognition

Alessandra Pauleen I. Gomez, Ibrahim D. Kahil,
Shaun Vincent N. Ong, Edward P. Tighe
Department of Software Technology and Center for Language Technologies
De La Salle University, Manila, Philippines
{alessandra_gomez,ibrahim_kahil,shaun_ong,edward.tighe}@dlsu.edu.ph

Abstract

Emerging research in Filipino Automatic Per-
sonality Recognition (APR) often utilizes so-
cial media data for its widespread availability
and natural expression. However, current ap-
proaches focusing on direct personality trait
modeling often yield subpar results, prompting
exploration of alternative methods. Thus, we
explored an APR framework where individual
personality questionnaire item responses are
predicted and then aggregated to estimate trait
scores. Using text data from 2,168 Filipino
X (formerly Twitter) users, we trained models
for each item in the Big Five Inventory (BFI)
related to Extraversion and Conscientiousness.
We also experimented with multiple configu-
rations of logistic regression, SVM, and XG-
Boost models using TF-IDF and term occur-
rence values. Findings highlight the challenges
in predicting trait scores for both Extraversion
and Conscientiousness. While implementing a
hierarchical classification scheme at the item
level showed some improvement, especially
for Conscientiousness, overall trait-level per-
formance remains lacking. Overall, while the
original pipeline as well as the integration of
a hierarchical approach show potential, signifi-
cant improvements are needed before this item-
based framework can be effectively used for
APR.

1

Introduction

The extent of a person’s individuality and identity
encompasses a great number of factors, from their
daily experiences all the way to their hobbies, in-
terests, and way of interacting with others. Such
traits are often considered part of one’s personal-
ity—defined by the American Psychological Asso-
ciation as a collection of “enduring characteristics
and behavior that comprise a person’s unique ad-
justment to life.” Numerous scientific theories and
approaches have been created in order to deepen the
world’s understanding of personality into how it is

today. As part of its evolution, personality psychol-
ogy has been integrated into computational science;
through the use of machine learning and natural
language processing (NLP), personality recogni-
tion was made possible by incorporating data or
signals from human-machine interaction, including
but not limited to social media and telecommunica-
tion (Mushtaq and Kumar, 2022).

Works on text-based APR have branched out
to include attempts to derive personality from so-
cial media posts within a specific regional con-
text. There are a lot of cultural linguistic nuances
that can serve as integral personality indicators, yet
models are not always able to extract information
that properly encapsulates these intricacies brought
about by multilingualism.

With this new aspect of APR, studies on person-
ality recognition on Filipino user data have begun
to take place. From attempts at extraction meth-
ods (Agno et al., 2019; Chua Chiaco et al., 2022)
to modeling Filipino personality traits using super-
vised learning models (Tighe and Cheng, 2018), Fil-
ipino APR studies are slowly breaking ground with
the goal of applying techniques that can capture
the rich linguistic diversity of the nation. However,
since this particular branch of study is relatively
new, there have been unsuccessful ventures as well;
at present, existing studies on the use of higher
complexity models such as neural networks (Tighe
et al., 2020) failed to yield good results, especially
considering that this was attempted when Filipino
user data was scarce.

Given the current state of Filipino APR, it begs
the question of whether it is possible to utilize an-
other approach at modeling personality traits in-
stead of directly generating user personality pro-
files from social media data. One such alterna-
tive is a questionnaire-based approach, wherein
models trained on social media data will then pre-
dict how the user might answer a question from
a personality inventory. By combining APR with

---

<!-- PAGE 2 -->

a questionnaire-based framework, it may reveal a
new angle of extracting, processing, and analyzing
data that will be able to account for the cultural
linguistic cues found in the Filipino language—and
by extension, can also be applied in the context of
general, non-regional APR research.

The general objective of this study is to investi-
gate the effectiveness of a questionnaire item-based
prediction approach to automatic personality recog-
nition on social media text data. The specific ob-
jectives of the study are defined below:

1. To define a list of qualification criteria for
deriving a subset of the PagkataoKo dataset;

2. To extract text-based information from users’

social media posts;

3. To build and train prediction models for each
personality questionnaire item using the gen-
erated user embeddings;

4. To evaluate and analyze the performance of
the item-based prediction models at an indi-
vidual item level and an overall trait score
level; and

5. To compare the item-based prediction ap-
proach to automatic personality recognition
against baseline prediction models

The results of this study represent the output
of a different approach to APR, specifically pre-
dicting users’ Likert scale-type answers to the BFI
questionnaire instead of predicting their personal-
ity trait scores directly. Due to the uniqueness of
the approach, it offers the viability of utilizing the
approach to conduct APR and introduces the idea
of predicting questionnaire items for other models
as well.

2 Methodology

This section provides a step-by-step breakdown of
the individual processes undertaken to achieve the
objectives of this study. As seen in Figure 1 that
shows the overall research pipeline, using the orig-
inal PagkataoKo dataset, a smaller subset of data
was derived by filtering based on a set of defined
qualification criteria. Then, preprocessing and fea-
ture extraction were done on the data of each user
from their X (formerly Twitter) posts. After, feature
reduction was performed to further trim down the
number of features. Machine learning models were

Figure 1: Diagram of the Overall Research Pipeline
Following Our Proposed Item-Based Approach

then built for each questionnaire item under the
Extraversion and Conscientiousness traits, which
were trained and tested. The mentioned traits were
chosen among the Big Five in accordance with
Tighe and Cheng’s (2018) findings about the two
being the easiest to model.

The resulting predictions for each questionnaire
item were then aggregated to estimate the Extraver-
sion and Conscientiousness trait scores of each user.
Evaluation of the machine learning models were
conducted for each individual item, along with a
separate trait-level evaluation to assess the perfor-
mance of the overall approach of utilizing question-
naire item predictions for estimating personality
trait scores.

2.1 Data Source

The dataset used in the study is the PagkataoKo
dataset curated by Tighe et al. (2022). Collected
starting the first week of June 2019 up until the
second week of February 2020, the study was able
to gather a total of 3,128 records and contains infor-
mation about Filipino X (formerly Twitter) and/or
Instagram users such as demographic data, account
metadata, post data, and personality data.

The primary information utilized from the
dataset includes the X (formerly Twitter) post data
such as the actual post text and the data contain-
ing BFI responses and overall score per dimension
which are needed for ground truth comparisons and
evaluation.

To align with the scope of the study, the data was

---

<!-- PAGE 3 -->

filtered according to set qualification criteria. First,
the users must be of Philippine legal age; that is,
they must be at least 18 years old. Second, as the
study is focused on text-based data, the users must
have X (formerly Twitter) with at least 50 posted
tweets.

A simple demographic and summary statistic
analysis was conducted on the original curated
dataset as well as the filtered qualifying dataset.
These statistics are reported on Table 1..

Demographics Universal Set Twitter Subset Qualified Subset

Count

Age

Mean
SD
Age Range
18-20
21-23
24-26
≥ 27

Sex

Male
Female
Intersex
Declined1

Nationality
Filipino
Mixed2

3,128

2,283

21.2
3.9

53.9%
29.3%
9.3%
7.5%

21.0%
76.1%
0.5%
2.4%

99.2%
0.8%

21.0
3.9

55.9%
29.0%
8.5%
6.6%

22.0%
75.0%
0.6%
2.5%

99.1%
0.9%

2,168

21.0
3.6

56.0%
29.2%
8.5%
6.3%

21.5%
75.5%
0.6%
2.4%

99.2%
0.8%

1 Declined to disclose their sex
2 Filipinos with one or more other nationalities

Table 1: Demographic statistics across the universal set
of all participants (U), the subset of participants with
Twitter accounts (T), and the subset of participants with
Twitter accounts that satisfied the qualification criteria
(QT)

2.2 Text Preprocessing

Preprocessing was first performed on the text cor-
pus. The study mainly utilized tokenization and
N-Grams. For tokenization, Marges’s (2019) Pinoy
TweetTokenizer will be used, which is a modified
TweetTokenizer for the Filipino language. The tok-
enizer features are as follows:

1. Replacing usernames with a placeholder (i.e.

USERNAME);

2. Hashtag tokenization;

3. Limiting repeating syllables;

4. Emoticon tokenization;

6. Lowercasing

For N-Grams, the study utilized NLTK’s nltk.lm
package to extract n-grams of different lengths
needed (Bird et al., 2009). It should be noted that
only unigram and bigram features were tested.

2.3 Formulating User Documents

Concurrently, while performing text preprocess-
ing, user documents were constructed wherein all
tweets of a user were combined into one document
for analysis. To do this, the study utilized the tech-
nique of concatenation of strings in each tweet of a
particular user which then forms the user document.
To implement this, tokenization was first performed
on the text at the tweet level, followed by applying
n-grams to the tokens of each tweet, outputting a
group of tokens per tweet. From there, we con-
catenate the arrays of tokens together, formulating
a user document for a particular user where these
tokens are treated as terms.

2.4 Feature Extraction

Feature extraction was performed on the prepro-
cessed text data to extract the necessary informa-
tion from the text. The study utilized TF-IDF and
Term Occurrence as the extraction methods. Due
to the PagkataoKo dataset containing multiple lan-
guages (i.e., English and Filipino), both TF-IDF
and Term Occurrence are among the more viable
methods as these can handle multilingual text and
terms. There are two parameters in the tfidfVector-
izer that were included as experiment parameters,
which are min_df and max_df. Both min_df and
max_df are document frequency filters that remove
features depending on the percentage of documents
they are found in.

2.5 Feature Reduction

In order to retain only the most relevant features
as input for model building, feature reduction tech-
niques were employed on the training set. Note that
this was also treated as an experiment parameter,
testing between the use of the chi-square test and
principal component analysis (PCA). Using the chi-
square (X²) test, we only retained the features that
fall within the top 20% of results and these features
were selected for training the machine learning
models.

2.6 Model Building

5. Replacing URLs with a placeholder (i.e.

URL); and

The study made use of the following supervised
machine learning models that focused on solving

---

<!-- PAGE 4 -->

a classification problem centered around the pre-
diction of BFI item responses based on their social
media data:

• Logistic Regression

• Support Vector Machine with a Non-Linear

Kernel

• XGBoost

These three models were chosen because in the
context of the study, they may perform best given
the amount of data available.

It is worth noting that since the study focuses on
predicting responses to BFI questions, individual
models were created for each of the 17 BFI items
under either Extraversion or Conscientiousness. In
addition to the approach of directly classifying the
specific Likert scale-type responses for each item,
the study also experiments with a two-phase, hi-
erarchical classification scheme. This alternative
method involves training initial models that broadly
classify users’ responses into one of three cate-
gories: (a) 1-2, (b) 3, or (c) 4-5. Then, for the
second phase, a set of binary models is trained for
each item to further distinguish users’ responses
within each category, thus obtaining the specific
item responses.

2.7 Aggregating Item-Level Model Results

Once the individual item-level models were used to
predict the responses of a given user, these results
were then be aggregated to estimate their raw per-
sonality trait scores. This may be accomplished by
following the pseudocode depicted in Algorithm 1,
which is patterned after the actual scoring metric
of the BFI. The algorithm shows how to calculate
each trait score by obtaining the average of the
predicted responses for all question items that fall
under a particular personality trait. In doing so, it
should also be kept in mind that questions tagged
as reversed should have their responses converted
accordingly.

3 Experiment Setup and Evaluation

3.1 Experiment Setup

This study experimented with multiple combina-
tions of feature extraction, feature reduction, and
machine-learning techniques to identify the config-
urations that yield the most optimal results.

A total of 17 item-level models were created for
each configuration or combination of techniques as

Algorithm 1 Aggregating Item-Level Model Re-
sults
Input: Predicted item responses for a given user
Output: List of estimated personality trait scores

initialize empty trait score list
for each personality trait do

sum = 0
for each question item under current trait do

if question item is reversed then

sum += REVERSE(predicted re-

sponse)

else

sum += predicted response

end if

end for
trait score = sum / number of questions under

current trait

append current trait score to trait score list

end for
return trait score list

described above to correspond to each of the items
in the Big Five Inventory that correspond to either
Extraversion or Conscientiousness.

Furthermore, it should also be noted that a train-
validation-test split was applied on the dataset, with
a split ratio of 70%, 15%, and 15%, respectively.
This was implemented by utilizing scikit-learn’s
train_test_split function to ensure objective and
black-boxed splitting.

3.2

Item-Level Evaluation

This phase of the experiments centers on building
models for the 8 items under Extraversion and the
9 items under Conscientiousness.

Experiment parameters came in the form of mul-
tiple combinations of feature extraction and reduc-
tion techniques as well as machine learning algo-
rithms and configurations, all utilized to derive the
best performing model for each item. Taking into
account all of the experiment parameters except for
the two-phase hierarchical classification scheme,
there are a total of 96 configurations generated
for each item (2 feature extraction methods × 2
feature reduction methods × 3 machine learning
algorithms × 2 min_df values × 4 max_df values).
Additionally, the set of 96 experiment configura-
tions is conducted using the two-phase hierarchical
classification approach, resulting in a final total of
192 models per questionnaire item (96 models us-

---

<!-- PAGE 5 -->

ing direct approach + 96 models using two-phase
hierarchical classification approach).

Following model training and hyperparameter
tuning, the primary metric that was used to deter-
mine the best model configuration for each item
was the validation F1 score, as this takes into con-
sideration the class imbalance present in the source
dataset’s distribution of item responses. In the case
of the models created following the two-phase hier-
archical classification approach, the validation F1
score of the initial broad classification models is
the metric used as the basis for determining the best
configurations. These best models then make the
final predictions of the test users’ answers, which
are then compared to their ground-truth responses
for each item.

Baseline models were implemented using ma-
jority class classifiers to serve as benchmarks for
comparing the proposed best item models. These
classifiers were trained using the responses for each
item, identifying the majority class as a constant
predictor.

3.3 Trait-Level Evaluation

This second phase of the experiment focused on
acquiring the predicted item responses for each trait
from the best item models in the previous phase and
computing for the users’ trait-level scores using the
designated formula of the BFI.

Once the personality trait results were aggre-
gated for each user in the test set and compared
against their ground-truth trait scores, evaluation
was performed with the use of root mean squared
error (RMSE) and R2 score.

Similar to the previous phase, baseline models
were employed to have a further comparison and
performance evaluation of the proposed approach.
These baselines included a mean regressor, a sim-
ple linear regression model, and a multi-layer per-
ceptron (MLP) regressor.

The mean regressor was trained using the raw
personality trait scores from the dataset, with the
average score for each trait serving as a constant
predictor. Meanwhile, the pipeline for both the
mean regressor and the MLP regressor follows a
process similar to the proposed approach up until
the feature reduction stage. However, instead of
proceeding to item-specific model-building and ag-
gregation, the pipeline for these baseline models
directly transitions to trait-specific model building
and trait-level evaluation. This divergence stems
from their trait-based approach of training directly

on the raw personality trait scores of each user,
rather than on the individual item responses as in
the proposed approach.

4 Results

4.1 Evaluation of Initial Proposed Approach

Item-Level Evaluation Results

4.1.1
Out of all the item-level models constructed and
tested during experimentation, only the configura-
tions that achieved the best validation results for
each individual questionnaire item are reported.

Table 2 and Table 3 provide overviews of the
best-performing models for each Extraversion item
and each Conscientiousness item, respectively. The
results of these item models are also juxtaposed
with the results of baseline majority class classi-
fiers, as illustrated in Figure 2 and Figure 3.

Across all of the Extraversion and Conscientious-
ness item models, there appears to be a fair amount
of variance in the optimal configurations identified
for almost all of the parameters included in the
experiment. The one exception, it seems, is the fea-
ture type for the Extraversion item models, as most
seem to favor the use of Term Occurrence, possibly
due to its potential to aid in model generalization.
As seen in Table 2, the overall test F1 scores of
the best item models for Extraversion fall between
0.3000 to 0.5000, with Item 31R achieving the high-
est test F1 score at 0.4334. Conversely, the weakest
performing model belongs to Item 36, which has a
test F1 score of approximately 0.3196. A compari-
son of these F1 scores with those obtained on the
train-validation set suggests a possibility that the
models overfitted on the training data.

Item-Level Results for Extraversion

Item

Item 1
Item 6R
Item 11
Item 16
Item 21R
Item 26
Item 31R
Item 36

Min_df Max_df Feature
Reduc-
tion
PCA
CHI
CHI
CHI
PCA
CHI
CHI
PCA

0.1
0.05
0.05
0.1
0.05
0.1
0.05
0.1

0.9
0.7
0.9
0.7
0.6
0.6
0.8
0.9

Algorithm Feature

LR
XGB
LR
LR
LR
XGB
SVM
SVM

TO
TF-IDF
TO
TF-IDF
TO
TO
TO
TO

Train-
Val F1

1.0000
1.0000
1.0000
1.0000
1.0000
1.0000
0.9875
0.9962

Test F1

0.3450
0.3740
0.3311
0.3586
0.3386
0.3785
0.4334
0.3196

Table 2: The performance and configurations of the best
performing classification models per Extraversion item.
Models were selected based on validation F1 score.

Compared to the results produced by the Ex-
traversion item models, the range of values for the
test F1 scores of the best performing Conscientious-
ness item models is generally broader, both on the
lower and higher ends of the scale. Table 3 reveals

---

<!-- PAGE 6 -->

that the best performing item model for Conscien-
tiousness produced a test F1 score of 0.5416, while
the worst performing model had a test F1 score of
0.2426.

Item-Level Results for Conscientiousness

Item

Item 3
Item 8R
Item 13
Item 18R
Item 23R
Item 28
Item 33
Item 38
Item 43R

Min_df Max_df Feature
Reduc-
tion
CHI
CHI
CHI
PCA
PCA
PCA
CHI
PCA
PCA

0.05
0.05
0.1
0.1
0.1
0.05
0.1
0.05
0.1

0.9
0.9
0.6
0.6
0.6
0.7
0.7
0.6
0.9

Algorithm Feature

XGB
XGB
XGB
SVM
LR
LR
LR
LR
XGB

TO
TO
TF-IDF
TO
TO
TF-IDF
TF-IDF
TF-IDF
TF-IDF

Train-
Val F1

0.7207
0.9902
0.2761
0.8959
1.0000
0.9680
1.0000
1.0000
1.0000

Test F1

0.4574
0.5416
0.2426
0.2534
0.4373
0.4152
0.3534
0.2750
0.3921

Table 3: The performance and configurations of the best
performing classification models per Conscientiousness
item. Models were selected based on validation F1
score.

As evidenced by the side-by-side comparisons of
the test F1 scores for the item models of both traits
against the baseline majority classifiers in Figure
2 and Figure 3, it becomes apparent that all of the
proposed item models consistently underperform.
This disparity in classification performance may
potentially be caused in part by the disproportionate
number of samples for the majority class label of
each questionnaire item. The degree to which this
class imbalance exists can be seen from how most
of the majority class classifiers exhibited test F1
scores above 0.5.

Figure 3: A comparison of test F1 scores between base-
line majority class classifiers and the best item models
for Conscientiousness

regressor, a linear regression model, and a multi-
layer perceptron regressor.

For the Extraversion trait, Table 4 shows that the
proposed approach produced the best results, with
the lowest test RMSE of approximately 0.6714, and
the highest R2 score of around 0.1240. However,
when taking these values on their own, the R2 value
can be considered relatively low. This may suggest
that the variance in the Extraversion trait scores is
still not explained very well by the predictor using
the given features.

Model
Mean Regressor
Linear Regression
MLP Regressor
Proposed Approach

Trait-Level Results for Extraversion
Train-Val RMSE Train-Val R2 Test RMSE Test R2
-0.0003
0.1154
0.0000
0.1240

0.0000
0.8751
-0.0004
0.9974

0.7175
0.6747
0.7174
0.6714

0.7499
0.2650
0.7500
0.0382

Table 4: The trait-level results for Extraversion using
the proposed approach as well as baseline models

Compared to Extraversion, the results produced
by all of the models for the Conscientiousness trait
are considerably worse. The proposed approach
performs the worst with a test RMSE of 0.6760
and a test R2 value of -0.2273, while the linear re-
gression model performs the best with a test RMSE
of 0.6010 and a test R2 value of 0.0298. These re-
sults show that the initial item-based approach for
Conscientiousness leaves much to be improved, as
direct trait modeling still works better in predicting
overall trait scores.

Interestingly, despite generally having better test
RMSE scores, the Conscientiousness models ap-
pear to have poorer test R2 scores across the board,
which may suggest that with the given feature set,
Conscientiousness trait scores are more challeng-
ing to predict compared to Extraversion.

Figure 2: A comparison of test F1 scores between base-
line majority class classifiers and the best item models
for Extraversion

4.1.2 Trait-Level Evaluation Results
Table 4 and Table 5 present the trait-level results
comparing the aggregated predictions against the
ground-truth personality trait scores for Extraver-
sion and Conscientiousness, respectively. The re-
sults of the proposed approach are also compared
to that of 3 different baselines, particularly, a mean

---

<!-- PAGE 7 -->

Trait-Level Results for Conscientiousness

Model
Mean Regressor
Linear Regression
MLP Regressor
Proposed Approach

Train-Val RMSE Train-Val R2 Test RMSE Test R2
-0.0010
0.0298
-0.0199
-0.2273

0.0000
0.8326
-0.0120
0.8892

0.6105
0.6010
0.6162
0.6760

0.6108
0.2499
0.6144
0.2033

Table 5: The trait-level results for Conscientiousness
using the proposed approach as well as baseline models

4.2 Evaluation of Proposed Approach with

Hierarchical Classification

Another experiment was done with the proposed
approach, particularly the integration of a hierarchi-
cal classification scheme. As mentioned previously,
hierarchical classification attempts to classify the
data into broader classes (e.g. Class 1-2, Class 4-5)
on the first classification layer, then classifies the
data in a more specific class (e.g. Class 1, Class 2)
on the second layer. This experiment was done to
attempt to classify data points better by grouping
classes that were closer to each other first and then
differentiating them later on.

Train-Val RMSE
Train-Val R²
Item

Val F1
(Broad)

0.5685
Item 1
0.5359
Item 6R
0.5220
Item 11
Item 16
0.5560
Item 21R 0.5567
Item 26
0.4956
Item 31R 0.6579
0.5317
Item 36

Extraversion

0.2097
0.9218

Test RMSE
Test R²

Val F1
(Spe-
cific)

0.3502
0.3990
0.3431
0.3350
0.3643
0.3913
0.4650
0.3236

Val F1
(Bi-
nary
1)
0.6520
0.7825
0.6040
0.7307
0.7508
0.6427
0.6269
0.5018

Val F1
(Bi-
nary
2)
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000

Val F1
(Bi-
nary
3)
0.5399
0.6313
0.5613
0.5815
0.5445
0.7402
0.5986
0.5692

0.7126
0.0131
Train-Val F1 Test F1

0.9519
0.9822
1.0000
0.7085
0.7209
1.0000
0.9412
0.6096

0.3892
0.3138
0.3905
0.3205
0.2999
0.3230
0.4284
0.2848

Table 6: Extraversion Results with Hierarchical Classi-
fication

curacy in the first layer of classes, specifically in
Classes 1-2, 3, and 4-5, respectively. These afore-
mentioned scores for both traits show generally
higher values, meaning that on the broad level of
classification, the models are able to classify more
accurately compared to previous scores.

The validation F1 scores labeled specific, on the
other hand, are not as high as the broad F1 scores.
The specific F1 scores pertains to the accuracy of
classifying the data to the actual response predic-
tion classes (i.e. Class 1, 2, 3, 4, 5).

The validation F1 scores labeled Binary repre-
sent the accuracy of predicting the right binary
class after the first classification layer has been
done (i.e. Binary 1 - Class 1 and 2, Binary 2 -
Class 3, Binary 3 - Class 4 and 5). Although the
F1 scores for each Binary are generally high, this
only deals with classifying the data into one or two
classes.

Trait-Level Results for Extraversion

Version
Original
Hierarchical
Classification

Test RMSE Test R²
0.1240
0.0131

0.6714
0.7126

Table 8: Extraversion Trait-Level Results for Original
and Hierarchical Experiments

Trait-Level Results for Conscientiousness
Test RMSE Test R²
-0.2273
-0.0560

0.6760
0.6270

Version
Original
Hierarchical
Classification

0.6270
-0.0560
Train-Val F1 Test F1

Table 9: Conscientiousness Trait-Level Results for Orig-
inal and Hierarchical Experiments

Train-Val RMSE
Train-Val R²
Item

Val F1
(Broad)

0.6373
Item 3
0.6366
Item 8R
Item 13
0.7167
Item 18R 0.5135
Item 23R 0.7327
0.6344
Item 28
0.5780
Item 33
Item 38
0.5016
Item 43R 0.6583

Conscientiousness

0.2015
0.8911

Test RMSE
Test R²

Val F1
(Spe-
cific)

0.6281
0.5419
0.4909
0.4036
0.4451
0.5052
0.4435
0.4434
0.4156

Val F1
(Bi-
nary
1)
0.8617
0.5513
0.8526
0.4775
0.7957
1.0000
0.9033
0.7528
0.7148

Val F1
(Bi-
nary
2)
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000
1.0000

Val F1
(Bi-
nary
3)
0.5824
0.6123
0.5480
0.5090
0.5514
0.5099
0.6314
0.6323
0.5480

0.8263
0.8297
1.0000
0.9859
0.9712
0.8611
0.9925
0.6317
0.7604

0.5742
0.5078
0.4366
0.3380
0.4388
0.4555
0.3608
0.3406
0.5399

Table 7: Conscientiousness Results with Hierarchical
Classification

Tables 6 and 7 show the results of the item mod-
els with hierarchical classification, along with the
validation F1 scores for each layer for both broad
and binary classification.

The broad F1 scores represent classification ac-

Overall, observing the results found in Table
7, the validation scores look somewhat promising,
with predictions that look more accurate after pass-
ing through two layers as opposed to the original
proposed approach for Conscientiousness. It can
be observed that the approach with hierarchical
classification is a potentially viable method in clas-
sifying as it produced more accurate results at the
item-level. This difference in metric scores may
likely be attributed to the step-by-step process of
classifying the data, where data is classified in a
broader threshold of similar classes and then further
differentiated on the second level. By breaking the
modeling process into two phases, this approach

---

<!-- PAGE 8 -->

They can delve into more experimentations that aim
to determine how the data qualitatively correlates
to model performance, and what can be changed
during preprocessing, extraction, and reduction in
order for models to learn better from them and at-
tain the most optimal performance results. Another
angle of interest is examining trait-level result cor-
relations with feature tokens, as this may help in
identifying trends or patterns in terms of how each
trait’s best performing approach assigns weights
or significance to certain terms or phrases, espe-
cially considering the mix of English and Filipino
linguistic nuances.

At a more general level, future studies may opt to
focus on a wider scope. Recommendations include
exploring multimodal approaches that make use
of images alongside textual data, testing the item-
based approach on a high-resource language like
English to more accurately assess the impact of
data quantity, and investigating methodologies on
how to properly structure social media data.

Future works may also address the identified
issues from the results of the study, mainly data
imbalance leading to model overfitting, hyperpa-
rameter limitations, and data quality or weight as-
signments on features. This can be done by increas-
ing hyperparameter search space and number of
iterations for the models, as well as attempting to
experiment only with the unigram data instead of
including bigrams.

The potential of the hierarchical approach can
also be expounded upon; with proper data balanc-
ing methods and the right set of configurations, this
approach may prove to be integral and beneficial
to the overall pipeline.

Other recommendations include exploring other
feature extraction and reduction techniques, as well
as utilizing the remaining three traits of the Big
Five (Openness, Agreeableness, and Neuroticism)
to determine if the proposed approach could work
equally or better as compared to its Extraversion
and Conscientiousness results. Future works are
also recommended to test the proposed approach
against diverse datasets and different social media
platforms and contexts in order to have a better
benchmark for performance and generalizability.

better accounted for the inherent ordinality of the
data and showed that the models still had potential
for distinguishing between high and low responses,
which was particularly beneficial for the Consci-
entiousness trait. However, despite an improved
item-level performance, the trait-level results still
much to be desired. That said, it is still a step in the
right direction to be able to classify the item-level
data more accurately at least at the broad level.

5 Conclusion

Following initial item-level and trait-level evalua-
tions of the approach, it was inferred that due to
data imbalance, substantial results became hard to
derive because models performed poorly in terms
of item-level prediction, and were even outper-
formed by baseline classifiers and regression mod-
els. In hopes of addressing this issue, a hierarchical
classification approach was integrated, which in-
volved breaking down the modeling process into
two phases. Implementing this method showed a
somewhat distinct advantage, most notably for the
Conscientiousness trait. However, while the hierar-
chical approach worked relatively better for Con-
scientiousness, the original pipeline still reigned
for Extraversion. This difference in model inclina-
tion may be attributed to the difference in feature
significance between the two traits.

It is also worth noting that when compared
against baseline models, the original pipeline still
performed best for Extraversion, whereas the base-
lines performed better for Conscientiousness even
with the slight improvement provided by the hierar-
chical approach. This supports the deduction that
Conscientiousness items responses may be harder
to predict, particularly with the given data.

With these results, it is evident that this particular
field of APR study, especially in a Filipino context,
leaves much room for pondering and experimen-
tation. Some models indeed showed promise, but
even the so-called best performing models have
very low test metric scores. The overall results of
this study signify that more tuning for both data
and models needs to be done for this item-based
approach to manifest improvements and become a
framework that can prove beneficial to APR.

6 Recommendation

Future works that will choose to build up on the re-
sults from this study are encouraged to focus more
on the best performing approaches for each trait.

---

<!-- PAGE 9 -->

References

Alexander H.

II Agno,

Jesah R. Gano,

and
Claude Kristoffer Sedillo. 2019. Instagram vs Twit-
ter: Analyzing the manifestation of personality
through the writing style of Filipino SNS users. Bach-
elor’s thesis, De La Salle University.

American Psychological Association. Personality.

Steven Bird, Edward Loper, and Ewan Klein. 2009.
Natural Language Processing with Python. O’Reilly
Media Inc.

Ronn Christian Chua Chiaco, Howard Montecillo,
Ronell John Roxas, and Bryan Ethan Tio. 2022. Ap-
plication of word embeddings on automatic person-
ality recognition using Filipino Twitter data. Bache-
lor’s thesis, De La Salle University.

Andrew Marges. 2019. pinoy_tweetokenize.

Sumiya Mushtaq and Neerendra Kumar. 2022. Text-
based automatic personality recognition: Recent
In Proceedings of Third Interna-
developments.
tional Conference on Computing, Communications,
and Cyber-Security:
IC4S 2021, pages 537–549.
Springer.

Edward Tighe, Luigi Acorda, Alexander Ii Agno, Jesah
Gano, Timothy Go, Gabriel Santiago, and Claude
Sedillo. 2022. Collection methods and data charac-
teristics of the PagkataoKo dataset. In Proceedings
of the 36th Pacific Asia Conference on Language, In-
formation and Computation, pages 513–524, Manila,
Philippines. Association for Computational Linguis-
tics.

Edward Tighe, Oya Aran, and Charibeth Cheng. 2020.
Exploring neural network approaches in automatic
personality recognition of Filipino Twitter users. In
Proceedings of the 20th Philippine Computing Sci-
ence Congress, pages 137–145.

Edward Tighe and Charibeth Cheng. 2018. Model-
ing personality traits of Filipino Twitter users. In
Proceedings of the Second Workshop on Computa-
tional Modeling of People’s Opinions, Personality,
and Emotions in Social Media, pages 112–122, New
Orleans, Louisiana, USA. Association for Computa-
tional Linguistics.

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Modeling Personality Traits by Predicting Questionnaire Responses as an
Alternative Approach to Filipino Automatic Personality Recognition
AlessandraPauleenI.Gomez,IbrahimD.Kahil,
ShaunVincentN.Ong,EdwardP.Tighe
DepartmentofSoftwareTechnology and CenterforLanguageTechnologies
DeLaSalleUniversity,Manila,Philippines
{alessandra_gomez,ibrahim_kahil,shaun_ong,edward.tighe}@dlsu.edu.ph
|     | Abstract |     |     |     | today. Aspartofitsevolution,personalitypsychol- |     |     |     |     |
| --- | -------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
ogyhasbeenintegratedintocomputationalscience;
EmergingresearchinFilipinoAutomaticPer-
|     |     |     |     |     | through | the use of | machine | learning | and natural |
| --- | --- | --- | --- | --- | ------- | ---------- | ------- | -------- | ----------- |
sonalityRecognition(APR)oftenutilizesso-
|     |     |     |     |     | language | processing | (NLP), | personality | recogni- |
| --- | --- | --- | --- | --- | -------- | ---------- | ------ | ----------- | -------- |
cialmediadataforitswidespreadavailability
|                       |     |          |     |            | tion was | made possible |     | by incorporating | data or |
| --------------------- | --- | -------- | --- | ---------- | -------- | ------------- | --- | ---------------- | ------- |
| andnaturalexpression. |     | However, |     | currentap- |          |               |     |                  |         |
signalsfromhuman-machineinteraction,including
| proaches | focusing | on direct | personality | trait |     |     |     |     |     |
| -------- | -------- | --------- | ----------- | ----- | --- | --- | --- | --- | --- |
modelingoftenyieldsubparresults,prompting butnotlimitedtosocialmediaandtelecommunica-
tion(MushtaqandKumar,2022).
| explorationofalternativemethods. |     |     |     | Thus,we |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
exploredanAPRframeworkwhereindividual Works on text-based APR have branched out
personality questionnaire item responses are toincludeattemptstoderivepersonalityfromso-
predictedandthenaggregatedtoestimatetrait
|               |      |           |       |          | cial media | posts | within | a specific | regional con- |
| ------------- | ---- | --------- | ----- | -------- | ---------- | ----- | ------ | ---------- | ------------- |
| scores. Using | text | data from | 2,168 | Filipino |            |       |        |            |               |
text. Therearealotofculturallinguisticnuances
X(formerlyTwitter)users,wetrainedmodels
thatcanserveasintegralpersonalityindicators,yet
foreachitemintheBigFiveInventory(BFI)
relatedtoExtraversionandConscientiousness. modelsarenotalwaysabletoextractinformation
thatproperlyencapsulatestheseintricaciesbrought
| We also experimented |     | with | multiple | configu- |     |     |     |     |     |
| -------------------- | --- | ---- | -------- | -------- | --- | --- | --- | --- | --- |
rations of logistic regression, SVM, and XG- aboutbymultilingualism.
Boost models using TF-IDF and term occur- WiththisnewaspectofAPR,studiesonperson-
| rencevalues. | Findingshighlightthechallenges |     |     |     |     |     |     |     |     |
| ------------ | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
alityrecognitiononFilipinouserdatahavebegun
inpredictingtraitscoresforbothExtraversion
|                       |     |                    |     |     | to take | place. From | attempts | at extraction | meth- |
| --------------------- | --- | ------------------ | --- | --- | ------- | ----------- | -------- | ------------- | ----- |
| andConscientiousness. |     | Whileimplementinga |     |     |         |             |          |               |       |
ods(Agnoetal.,2019;ChuaChiacoetal.,2022)
hierarchicalclassificationschemeattheitem
tomodelingFilipinopersonalitytraitsusingsuper-
| level showed | some | improvement, |     | especially |     |     |     |     |     |
| ------------ | ---- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
visedlearningmodels(TigheandCheng,2018),Fil-
| for Conscientiousness, |     | overall | trait-level | per- |     |     |     |     |     |
| ---------------------- | --- | ------- | ----------- | ---- | --- | --- | --- | --- | --- |
formanceremainslacking. Overall,whilethe ipinoAPRstudiesareslowlybreakinggroundwith
originalpipelineaswellastheintegrationof the goal of applying techniques that can capture
ahierarchicalapproachshowpotential,signifi- therichlinguisticdiversityofthenation. However,
cantimprovementsareneededbeforethisitem- since this particular branch of study is relatively
| based framework |     | can be effectively |     | used for |     |     |     |     |     |
| --------------- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- |
new,therehavebeenunsuccessfulventuresaswell;
APR.
|     |     |     |     |     | at present, | existing | studies | on the | use of higher |
| --- | --- | --- | --- | --- | ----------- | -------- | ------- | ------ | ------------- |
complexitymodelssuchasneuralnetworks(Tighe
1 Introduction
etal.,2020)failedtoyieldgoodresults,especially
Theextentofaperson’sindividualityandidentity consideringthatthiswasattemptedwhenFilipino
| encompassesagreatnumberoffactors,fromtheir |     |     |     |     | userdatawasscarce. |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
dailyexperiencesallthewaytotheirhobbies,in- GiventhecurrentstateofFilipinoAPR,itbegs
terests, and way of interacting with others. Such thequestionofwhetheritispossibletoutilizean-
traits are often considered part of one’s personal- other approach at modeling personality traits in-
ity—definedbytheAmericanPsychologicalAsso- stead of directly generating user personality pro-
ciationasacollectionof“enduringcharacteristics files from social media data. One such alterna-
and behavior that comprise a person’s unique ad- tive is a questionnaire-based approach, wherein
justmenttolife.”Numerousscientifictheoriesand modelstrainedonsocialmediadatawillthenpre-
approacheshavebeencreatedinordertodeepenthe dict how the user might answer a question from
world’sunderstandingofpersonalityintohowitis apersonalityinventory. BycombiningAPRwith

aquestionnaire-basedframework,itmayreveala
newangleofextracting,processing,andanalyzing
| data that will | be able | to account | for the | cultural |     |     |     |     |     |     |     |
| -------------- | ------- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
linguisticcuesfoundintheFilipinolanguage—and
byextension,canalsobeappliedinthecontextof
general,non-regionalAPRresearch.
Thegeneralobjectiveofthisstudyistoinvesti-
gatetheeffectivenessofaquestionnaireitem-based
predictionapproachtoautomaticpersonalityrecog-
| nition on | social media | text data. | The specific | ob- |     |     |     |     |     |     |     |
| --------- | ------------ | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
jectivesofthestudyaredefinedbelow:
| 1. To define | a list | of qualification | criteria | for |     |     |     |     |     |     |     |
| ------------ | ------ | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
derivingasubsetofthePagkataoKodataset;
2. Toextracttext-basedinformationfromusers’
socialmediaposts;
|     |     |     |     |     | Figure 1: | Diagram | of  | the Overall |     | Research | Pipeline |
| --- | --- | --- | --- | --- | --------- | ------- | --- | ----------- | --- | -------- | -------- |
3. Tobuildandtrainpredictionmodelsforeach FollowingOurProposedItem-BasedApproach
personalityquestionnaireitemusingthegen-
erateduserembeddings;
|     |     |     |     |     | then built | for | each questionnaire |     |     | item | under the |
| --- | --- | --- | --- | --- | ---------- | --- | ------------------ | --- | --- | ---- | --------- |
4. To evaluate and analyze the performance of ExtraversionandConscientiousnesstraits,which
the item-based prediction models at an indi- weretrainedandtested. Thementionedtraitswere
vidual item level and an overall trait score chosen among the Big Five in accordance with
| level;and |     |     |     |     | TigheandCheng’s(2018)findingsaboutthetwo |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
beingtheeasiesttomodel.
5. To compare the item-based prediction ap- Theresultingpredictionsforeachquestionnaire
| proach | to automatic | personality | recognition |     |     |     |     |     |     |     |     |
| ------ | ------------ | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
itemwerethenaggregatedtoestimatetheExtraver-
againstbaselinepredictionmodels
sionandConscientiousnesstraitscoresofeachuser.
|                |          |                 |              |            | Evaluation | of  | the machine |            | learning | models | were   |
| -------------- | -------- | --------------- | ------------ | ---------- | ---------- | --- | ----------- | ---------- | -------- | ------ | ------ |
| The results    | of this  | study represent |              | the output |            |     |             |            |          |        |        |
|                |          |                 |              |            | conducted  | for | each        | individual | item,    | along  | with a |
| of a different | approach | to APR,         | specifically | pre-       |            |     |             |            |          |        |        |
separatetrait-levelevaluationtoassesstheperfor-
dictingusers’Likertscale-typeanswerstotheBFI
manceoftheoverallapproachofutilizingquestion-
questionnaireinsteadofpredictingtheirpersonal-
|                 |           |     |                  |     | naire item | predictions |     | for | estimating | personality |     |
| --------------- | --------- | --- | ---------------- | --- | ---------- | ----------- | --- | --- | ---------- | ----------- | --- |
| ity traitscores | directly. | Due | tothe uniqueness | of  |            |             |     |     |            |             |     |
traitscores.
theapproach,itofferstheviabilityofutilizingthe
| approachtoconductAPRandintroducestheidea |     |     |     |     | 2.1 DataSource |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
ofpredictingquestionnaireitemsforothermodels
|     |     |     |     |     | The dataset | used | in  | the study | is  | the PagkataoKo |     |
| --- | --- | --- | --- | --- | ----------- | ---- | --- | --------- | --- | -------------- | --- |
aswell.
|     |     |     |     |     | dataset  | curated   | by Tighe | et      | al. (2022). |     | Collected |
| --- | --- | --- | --- | --- | -------- | --------- | -------- | ------- | ----------- | --- | --------- |
|     |     |     |     |     | starting | the first | week     | of June | 2019        | up  | until the |
2 Methodology
secondweekofFebruary2020,thestudywasable
Thissectionprovidesastep-by-stepbreakdownof togatheratotalof3,128recordsandcontainsinfor-
theindividualprocessesundertakentoachievethe mationaboutFilipinoX(formerlyTwitter)and/or
objectives of this study. As seen in Figure 1 that Instagramuserssuchasdemographicdata,account
showstheoverallresearchpipeline,usingtheorig- metadata,postdata,andpersonalitydata.
inalPagkataoKodataset,asmallersubsetofdata The primary information utilized from the
wasderivedbyfilteringbasedonasetofdefined datasetincludestheX(formerlyTwitter)postdata
qualificationcriteria. Then,preprocessingandfea- such as the actual post text and the data contain-
tureextractionweredoneonthedataofeachuser ingBFIresponsesandoverallscoreperdimension
fromtheirX(formerlyTwitter)posts. After,feature whichareneededforgroundtruthcomparisonsand
| reductionwasperformedtofurthertrimdownthe |     |     |     |     | evaluation. |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
numberoffeatures. Machinelearningmodelswere Toalignwiththescopeofthestudy,thedatawas

| filteredaccordingtosetqualificationcriteria. |         |               |       | First,        | 6. Lowercasing |     |     |     |     |     |     |
| -------------------------------------------- | ------- | ------------- | ----- | ------------- | -------------- | --- | --- | --- | --- | --- | --- |
| the users                                    | must be | of Philippine | legal | age; that is, |                |     |     |     |     |     |     |
ForN-Grams,thestudyutilizedNLTK’snltk.lm
| theymustbeatleast18yearsold. |     |     | Second,asthe |     |         |            |         |     |              |     |         |
| ---------------------------- | --- | --- | ------------ | --- | ------- | ---------- | ------- | --- | ------------ | --- | ------- |
|                              |     |     |              |     | package | to extract | n-grams |     | of different |     | lengths |
studyisfocusedontext-baseddata,theusersmust
|     |     |     |     |     | needed(Birdetal.,2009). |     |     | Itshouldbenotedthat |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------- | --- | --- | --- |
haveX(formerlyTwitter)withatleast50posted
onlyunigramandbigramfeaturesweretested.
tweets.
A simple demographic and summary statistic 2.3 FormulatingUserDocuments
| analysis was | conducted | on              | the original | curated  |               |     |                  |     |      |             |     |
| ------------ | --------- | --------------- | ------------ | -------- | ------------- | --- | ---------------- | --- | ---- | ----------- | --- |
|              |           |                 |              |          | Concurrently, |     | while performing |     | text | preprocess- |     |
| dataset as   | well      | as the filtered | qualifying   | dataset. |               |     |                  |     |      |             |     |
ing,userdocumentswereconstructedwhereinall
ThesestatisticsarereportedonTable1..
tweetsofauserwerecombinedintoonedocument
|     |     |     |     |     | foranalysis. | Todothis,thestudyutilizedthetech- |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --------------------------------- | --- | --- | --- | --- | --- |
Demographics UniversalSet TwitterSubset QualifiedSubset niqueofconcatenationofstringsineachtweetofa
| Count |     | 3,128 | 2,283 | 2,168 |     |     |     |     |     |     |     |
| ----- | --- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
particularuserwhichthenformstheuserdocument.
Age
Toimplementthis,tokenizationwasfirstperformed
| Mean |     | 21.2 | 21.0 | 21.0 |     |     |     |     |     |     |     |
| ---- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
onthetextatthetweetlevel,followedbyapplying
| SD       |     | 3.9   | 3.9   | 3.6   |                                           |     |     |     |     |     |     |
| -------- | --- | ----- | ----- | ----- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
| AgeRange |     |       |       |       | n-gramstothetokensofeachtweet,outputtinga |     |     |     |     |     |     |
| 18-20    |     | 53.9% | 55.9% | 56.0% |                                           |     |     |     |     |     |     |
21-23 29.3% 29.0% 29.2% group of tokens per tweet. From there, we con-
| 24-26 |     | 9.3% | 8.5% | 8.5% |     |     |     |     |     |     |     |
| ----- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
catenatethearraysoftokenstogether,formulating
| ≥27 |     | 7.5% | 6.6% | 6.3% |     |     |     |     |     |     |     |
| --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
auserdocumentforaparticularuserwherethese
Sex
tokensaretreatedasterms.
| Male   |     | 21.0% | 22.0% | 21.5% |     |     |     |     |     |     |     |
| ------ | --- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Female |     | 76.1% | 75.0% | 75.5% |     |     |     |     |     |     |     |
2.4 FeatureExtraction
| Intersex |     | 0.5% | 0.6% | 0.6% |     |     |     |     |     |     |     |
| -------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
Declined1
|     |     | 2.4% | 2.5% | 2.4% |         |            |     |           |     |        |         |
| --- | --- | ---- | ---- | ---- | ------- | ---------- | --- | --------- | --- | ------ | ------- |
|     |     |      |      |      | Feature | extraction | was | performed |     | on the | prepro- |
Nationality
Filipino 99.2% 99.1% 99.2% cessed text data to extract the necessary informa-
Mixed2 0.8% 0.9% 0.8% tionfromthetext. ThestudyutilizedTF-IDFand
1Declinedtodisclosetheirsex TermOccurrenceastheextractionmethods. Due
2Filipinoswithoneormoreothernationalities
tothePagkataoKodatasetcontainingmultiplelan-
|     |     |     |     |     | guages | (i.e., English |     | and Filipino), |     | both | TF-IDF |
| --- | --- | --- | --- | --- | ------ | -------------- | --- | -------------- | --- | ---- | ------ |
Table1: Demographicstatisticsacrosstheuniversalset
ofallparticipants(U),thesubsetofparticipantswith andTermOccurrenceareamongthemoreviable
Twitteraccounts(T),andthesubsetofparticipantswith methodsasthesecanhandlemultilingualtextand
Twitteraccountsthatsatisfiedthequalificationcriteria
terms. TherearetwoparametersinthetfidfVector-
| (QT) |     |     |     |     | izerthatwereincludedasexperimentparameters, |        |     |         |      |        |     |
| ---- | --- | --- | --- | --- | ------------------------------------------- | ------ | --- | ------- | ---- | ------ | --- |
|      |     |     |     |     | which are                                   | min_df | and | max_df. | Both | min_df | and |
max_df aredocumentfrequencyfiltersthatremove
2.2 TextPreprocessing
featuresdependingonthepercentageofdocuments
| Preprocessingwasfirstperformedonthetextcor- |       |                 |              |     | theyarefoundin. |     |     |     |     |     |     |
| ------------------------------------------- | ----- | --------------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
| pus. The                                    | study | mainly utilized | tokenization | and |                 |     |     |     |     |     |     |
2.5 FeatureReduction
| N-Grams. | Fortokenization,Marges’s(2019)Pinoy |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TweetTokenizerwillbeused,whichisamodified In order to retain only the most relevant features
| TweetTokenizerfortheFilipinolanguage. |     |     |     | Thetok- |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
asinputformodelbuilding,featurereductiontech-
enizerfeaturesareasfollows: niqueswereemployedonthetrainingset. Notethat
|     |     |     |     |     | this was | also treated | as  | an experiment |     | parameter, |     |
| --- | --- | --- | --- | --- | -------- | ------------ | --- | ------------- | --- | ---------- | --- |
1. Replacingusernameswithaplaceholder(i.e.
testingbetweentheuseofthechi-squaretestand
| USERNAME); |     |     |     |     | principalcomponentanalysis(PCA).Usingthechi- |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
square(X²)test,weonlyretainedthefeaturesthat
2. Hashtagtokenization;
fallwithinthetop20%ofresultsandthesefeatures
|     |     |     |     |     | were selected |     | for training |     | the machine | learning |     |
| --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ----------- | -------- | --- |
3. Limitingrepeatingsyllables;
models.
4. Emoticontokenization;
2.6 ModelBuilding
5. Replacing URLs with a placeholder (i.e. The study made use of the following supervised
| URL);and |     |     |     |     | machinelearningmodelsthatfocusedonsolving |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |

a classification problem centered around the pre- Algorithm 1 Aggregating Item-Level Model Re-
| dictionofBFIitemresponsesbasedontheirsocial |     |     |     |     |     |     | sults   |                                       |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------------- | --- | --- | --- |
| mediadata:                                  |     |     |     |     |     |     | Input:  | Predicteditemresponsesforagivenuser   |     |     |     |
|                                             |     |     |     |     |     |     | Output: | Listofestimatedpersonalitytraitscores |     |     |     |
• LogisticRegression
initializeemptytraitscorelist
| • Support | Vector | Machine |     | with | a Non-Linear |     |     |     |     |     |     |
| --------- | ------ | ------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
foreachpersonalitytraitdo
Kernel
sum=0
| • XGBoost |     |     |     |     |     |     | foreachquestionitemundercurrenttraitdo |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
ifquestionitemisreversedthen
| These three | models | were | chosen |     | because | in the |     |     |                      |     |     |
| ----------- | ------ | ---- | ------ | --- | ------- | ------ | --- | --- | -------------------- | --- | --- |
|             |        |      |        |     |         |        |     | sum | += REVERSE(predicted |     | re- |
contextofthestudy,theymayperformbestgiven
sponse)
theamountofdataavailable.
else
Itisworthnotingthatsincethestudyfocuseson
sum+=predictedresponse
predictingresponsestoBFIquestions,individual
endif
modelswerecreatedforeachofthe17BFIitems
endfor
| undereitherExtraversionorConscientiousness. |     |     |     |     |     | In  |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
traitscore=sum/numberofquestionsunder
additiontotheapproachofdirectlyclassifyingthe
currenttrait
specificLikertscale-typeresponsesforeachitem,
appendcurrenttraitscoretotraitscorelist
| the study | also experiments |     | with | a   | two-phase, | hi- |     |     |     |     |     |
| --------- | ---------------- | --- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- |
endfor
| erarchical | classification |     | scheme. | This | alternative |     |     |     |     |     |     |
| ---------- | -------------- | --- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
returntraitscorelist
methodinvolvestraininginitialmodelsthatbroadly
| classify | users’ responses |     | into | one | of three | cate- |     |     |     |     |     |
| -------- | ---------------- | --- | ---- | --- | -------- | ----- | --- | --- | --- | --- | --- |
gories: (a) 1-2, (b) 3, or (c) 4-5. Then, for the describedabovetocorrespondtoeachoftheitems
secondphase,asetofbinarymodelsistrainedfor
intheBigFiveInventorythatcorrespondtoeither
| each item | to further | distinguish |     | users’ | responses |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- |
ExtraversionorConscientiousness.
within each category, thus obtaining the specific Furthermore,itshouldalsobenotedthatatrain-
itemresponses.
validation-testsplitwasappliedonthedataset,with
|     |     |     |     |     |     |     | a split ratio | of 70%, | 15%, and 15%, | respectively. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------------- | ------------- | --- |
2.7 AggregatingItem-LevelModelResults
|     |     |     |     |     |     |     | This was | implemented | by utilizing | scikit-learn’s |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------------ | -------------- | --- |
Oncetheindividualitem-levelmodelswereusedto
|     |     |     |     |     |     |     | train_test_split | function | to ensure | objective | and |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | --------- | --------- | --- |
predicttheresponsesofagivenuser,theseresults
black-boxedsplitting.
werethenbeaggregatedtoestimatetheirrawper-
sonalitytraitscores. Thismaybeaccomplishedby 3.2 Item-LevelEvaluation
followingthepseudocodedepictedinAlgorithm1,
Thisphaseoftheexperimentscentersonbuilding
whichispatternedaftertheactualscoringmetric
modelsforthe8itemsunderExtraversionandthe
oftheBFI.Thealgorithmshowshowtocalculate
9itemsunderConscientiousness.
| each trait | score | by obtaining |     | the | average | of the |     |     |     |     |     |
| ---------- | ----- | ------------ | --- | --- | ------- | ------ | --- | --- | --- | --- | --- |
Experimentparameterscameintheformofmul-
predictedresponsesforallquestionitemsthatfall
tiplecombinationsoffeatureextractionandreduc-
| underaparticularpersonalitytrait. |     |     |     |     | Indoingso,it |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
tiontechniquesaswellasmachinelearningalgo-
shouldalsobekeptinmindthatquestionstagged
rithmsandconfigurations,allutilizedtoderivethe
asreversedshouldhavetheirresponsesconverted
|     |     |     |     |     |     |     | bestperformingmodelforeachitem. |     |     | Takinginto |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ---------- | --- |
accordingly.
accountalloftheexperimentparametersexceptfor
3 ExperimentSetupandEvaluation the two-phase hierarchical classification scheme,
|     |     |     |     |     |     |     | there are | a total of | 96 configurations | generated |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----------------- | --------- | --- |
3.1 ExperimentSetup
|     |     |     |     |     |     |     | for each | item (2 feature | extraction | methods | × 2 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ---------- | ------- | --- |
This study experimented with multiple combina- feature reduction methods × 3 machine learning
tionsoffeatureextraction,featurereduction,and algorithms×2min_dfvalues×4max_dfvalues).
machine-learningtechniquestoidentifytheconfig- Additionally, the set of 96 experiment configura-
urationsthatyieldthemostoptimalresults. tionsisconductedusingthetwo-phasehierarchical
Atotalof17item-levelmodelswerecreatedfor classificationapproach,resultinginafinaltotalof
eachconfigurationorcombinationoftechniquesas 192modelsperquestionnaireitem(96modelsus-

ingdirectapproach+96modelsusingtwo-phase on the raw personality trait scores of each user,
hierarchicalclassificationapproach). ratherthanontheindividualitemresponsesasin
| Following |     | model | training | and | hyperparameter |     | theproposedapproach. |     |     |     |     |     |     |
| --------- | --- | ----- | -------- | --- | -------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
tuning,theprimarymetricthatwasusedtodeter-
|          |      |       |               |     |          |      | 4 Results |     |     |     |     |     |     |
| -------- | ---- | ----- | ------------- | --- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
| mine the | best | model | configuration |     | for each | item |           |     |     |     |     |     |     |
wasthevalidationF1score,asthistakesintocon-
|     |     |     |     |     |     |     | 4.1 EvaluationofInitialProposedApproach |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
siderationtheclassimbalancepresentinthesource
|                                       |     |     |     |     |           |     | 4.1.1 | Item-LevelEvaluationResults |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --------- | --- | ----- | --------------------------- | --- | --- | --- | --- | --- |
| dataset’sdistributionofitemresponses. |     |     |     |     | Inthecase |     |       |                             |     |     |     |     |     |
ofthemodelscreatedfollowingthetwo-phasehier- Out of all the item-level models constructed and
testedduringexperimentation,onlytheconfigura-
archicalclassificationapproach,thevalidationF1
|          |             |     |       |                |        |     | tions that | achieved | the | best validation |     | results | for |
| -------- | ----------- | --- | ----- | -------------- | ------ | --- | ---------- | -------- | --- | --------------- | --- | ------- | --- |
| score of | the initial |     | broad | classification | models | is  |            |          |     |                 |     |         |     |
themetricusedasthebasisfordeterminingthebest eachindividualquestionnaireitemarereported.
configurations. Thesebestmodelsthenmakethe Table 2 and Table 3 provide overviews of the
best-performingmodelsforeachExtraversionitem
finalpredictionsofthetestusers’answers,which
|     |     |     |     |     |     |     | andeachConscientiousnessitem,respectively. |     |     |     |     |     | The |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
arethencomparedtotheirground-truthresponses
foreachitem. results of these item models are also juxtaposed
|          |        |     |      |             |       |     | with the | results | of baseline | majority |     | class | classi- |
| -------- | ------ | --- | ---- | ----------- | ----- | --- | -------- | ------- | ----------- | -------- | --- | ----- | ------- |
| Baseline | models |     | were | implemented | using | ma- |          |         |             |          |     |       |         |
fiers,asillustratedinFigure2andFigure3.
jorityclassclassifierstoserveasbenchmarksfor
comparingtheproposedbestitemmodels. These AcrossalloftheExtraversionandConscientious-
classifiersweretrainedusingtheresponsesforeach nessitemmodels,thereappearstobeafairamount
ofvarianceintheoptimalconfigurationsidentified
| item, identifying |     | the | majority | class | as a constant |     |            |        |     |            |          |     |        |
| ----------------- | --- | --- | -------- | ----- | ------------- | --- | ---------- | ------ | --- | ---------- | -------- | --- | ------ |
|                   |     |     |          |       |               |     | for almost | all of | the | parameters | included |     | in the |
predictor.
|     |     |     |     |     |     |     | experiment. | Theoneexception,itseems,isthefea- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------------- | --- | --- | --- | --- | --- |
3.3 Trait-LevelEvaluation turetypefortheExtraversionitemmodels,asmost
seemtofavortheuseofTermOccurrence,possibly
| This second | phase |     | of the | experiment | focused | on  |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
acquiringthepredicteditemresponsesforeachtrait duetoitspotentialtoaidinmodelgeneralization.
fromthebestitemmodelsinthepreviousphaseand AsseeninTable2,theoveralltestF1scoresof
thebestitemmodelsforExtraversionfallbetween
computingfortheusers’trait-levelscoresusingthe
designatedformulaoftheBFI. 0.3000to0.5000,withItem31Rachievingthehigh-
Once the personality trait results were aggre- esttestF1scoreat0.4334. Conversely,theweakest
performingmodelbelongstoItem36,whichhasa
| gated for | each  | user         | in the | test  | set and compared   |     |                                   |     |     |     |     |           |     |
| --------- | ----- | ------------ | ------ | ----- | ------------------ | --- | --------------------------------- | --- | --- | --- | --- | --------- | --- |
|           |       |              |        |       |                    |     | testF1scoreofapproximately0.3196. |     |     |     |     | Acompari- |     |
| against   | their | ground-truth |        | trait | scores, evaluation |     |                                   |     |     |     |     |           |     |
wasperformedwiththeuseofrootmeansquared sonoftheseF1scoreswiththoseobtainedonthe
error(RMSE)andR2 score. train-validation set suggests a possibility that the
modelsoverfittedonthetrainingdata.
Similartothepreviousphase,baselinemodels
wereemployedtohaveafurthercomparisonand
Item-LevelResultsforExtraversion
performanceevaluationoftheproposedapproach.
|     |     |     |     |     |     |     | Item | Min_df Max_df | Feature | Algorithm | Feature | Train- | TestF1 |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | ------- | --------- | ------- | ------ | ------ |
|     |     |     |     |     |     |     |      |               | Reduc-  |           |         | ValF1  |        |
Thesebaselinesincludedameanregressor,asim-
tion
|     |     |     |     |     |     |     | Item1 | 0.1 | 0.9 PCA | LR  | TO  | 1.0000 | 0.3450 |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | ------ | ------ |
plelinearregressionmodel,andamulti-layerper-
|     |     |     |     |     |     |     | Item6R | 0.05 | 0.7 CHI | XGB | TF-IDF | 1.0000 | 0.3740 |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------- | --- | ------ | ------ | ------ |
ceptron(MLP)regressor. Item11 0.05 0.9 CHI LR TO 1.0000 0.3311
|                                       |      |           |     |         |           |     | Item16  | 0.1  | 0.7 CHI | LR  | TF-IDF | 1.0000 | 0.3586 |
| ------------------------------------- | ---- | --------- | --- | ------- | --------- | --- | ------- | ---- | ------- | --- | ------ | ------ | ------ |
| The                                   | mean | regressor | was | trained | using the | raw |         |      |         |     |        |        |        |
|                                       |      |           |     |         |           |     | Item21R | 0.05 | 0.6 PCA | LR  | TO     | 1.0000 | 0.3386 |
|                                       |      |           |     |         |           |     | Item26  | 0.1  | 0.6 CHI | XGB | TO     | 1.0000 | 0.3785 |
| personalitytraitscoresfromthedataset, |      |           |     |         | withthe   |     |         |      |         |     |        |        |        |
|                                       |      |           |     |         |           |     | Item31R | 0.05 | 0.8 CHI | SVM | TO     | 0.9875 | 0.4334 |
average score for each trait serving as a constant Item36 0.1 0.9 PCA SVM TO 0.9962 0.3196
| predictor. | Meanwhile, |     | the | pipeline | for both | the |         |                                          |     |     |     |     |     |
| ---------- | ---------- | --- | --- | -------- | -------- | --- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- |
|            |            |     |     |          |          |     | Table2: | Theperformanceandconfigurationsofthebest |     |     |     |     |     |
mean regressor and the MLP regressor follows a performingclassificationmodelsperExtraversionitem.
processsimilartotheproposedapproachupuntil ModelswereselectedbasedonvalidationF1score.
| the feature | reduction |     | stage. | However, | instead | of  |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
proceedingtoitem-specificmodel-buildingandag- Compared to the results produced by the Ex-
gregation, the pipeline for these baseline models traversionitemmodels,therangeofvaluesforthe
directlytransitionstotrait-specificmodelbuilding testF1scoresofthebestperformingConscientious-
and trait-level evaluation. This divergence stems nessitemmodelsisgenerallybroader,bothonthe
fromtheirtrait-basedapproachoftrainingdirectly lowerandhigherendsofthescale. Table3reveals

thatthebestperformingitemmodelforConscien-
tiousnessproducedatestF1scoreof0.5416,while
theworstperformingmodelhadatestF1scoreof
0.2426.
Item-LevelResultsforConscientiousness
| Item | Min_df | Max_df Feature | Algorithm | Feature | Train- TestF1 |     |     |     |     |     |     |     |
| ---- | ------ | -------------- | --------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|      |        | Reduc-         |           | ValF1   |               |     |     |     |     |     |     |     |
tion
| Item3   | 0.05 | 0.9 CHI | XGB | TO 0.7207     | 0.4574 |     |     |     |     |     |     |     |
| ------- | ---- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Item8R  | 0.05 | 0.9 CHI | XGB | TO 0.9902     | 0.5416 |     |     |     |     |     |     |     |
| Item13  | 0.1  | 0.6 CHI | XGB | TF-IDF 0.2761 | 0.2426 |     |     |     |     |     |     |     |
| Item18R | 0.1  | 0.6 PCA | SVM | TO 0.8959     | 0.2534 |     |     |     |     |     |     |     |
Item23R
|        | 0.1  | 0.6 PCA | LR  | TO 1.0000     | 0.4373 |     |     |     |     |     |     |     |
| ------ | ---- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Item28 | 0.05 | 0.7 PCA | LR  | TF-IDF 0.9680 | 0.4152 |     |     |     |     |     |     |     |
Item33 0.1 0.7 CHI LR TF-IDF 1.0000 0.3534 Figure3: AcomparisonoftestF1scoresbetweenbase-
| Item38 | 0.05 | 0.6 PCA | LR  | TF-IDF 1.0000 | 0.2750 |     |     |     |     |     |     |     |
| ------ | ---- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
linemajorityclassclassifiersandthebestitemmodels
| Item43R | 0.1 | 0.9 PCA | XGB | TF-IDF 1.0000 | 0.3921 |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
forConscientiousness
Table3: Theperformanceandconfigurationsofthebest
performingclassificationmodelsperConscientiousness
| item. | Models | were selected | based | on validation | F1  |            |          |            |     |        |     |          |
| ----- | ------ | ------------- | ----- | ------------- | --- | ---------- | -------- | ---------- | --- | ------ | --- | -------- |
|       |        |               |       |               |     | regressor, | a linear | regression |     | model, | and | a multi- |
score.
layerperceptronregressor.
FortheExtraversiontrait,Table4showsthatthe
Asevidencedbytheside-by-sidecomparisonsof
proposedapproachproducedthebestresults,with
thetestF1scoresfortheitemmodelsofbothtraits
thelowesttestRMSEofapproximately0.6714,and
againstthebaselinemajorityclassifiersinFigure
|     |     |     |     |     |     | the highest | R2  | score | of around | 0.1240. |     | However, |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --------- | ------- | --- | -------- |
2andFigure3,itbecomesapparentthatallofthe
whentakingthesevaluesontheirown,theR2value
proposeditemmodelsconsistentlyunderperform.
|      |           |                   |     |             |     | canbeconsideredrelativelylow. |     |     |     | Thismaysuggest |     |     |
| ---- | --------- | ----------------- | --- | ----------- | --- | ----------------------------- | --- | --- | --- | -------------- | --- | --- |
| This | disparity | in classification |     | performance | may |                               |     |     |     |                |     |     |
potentiallybecausedinpartbythedisproportionate thatthevarianceintheExtraversiontraitscoresis
stillnotexplainedverywellbythepredictorusing
numberofsamplesforthemajorityclasslabelof
thegivenfeatures.
| eachquestionnaireitem. |     |     | Thedegreetowhichthis |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classimbalanceexistscanbeseenfromhowmost
of the majority class classifiers exhibited test F1 Trait-LevelResultsforExtraversion
|                 |     |     |     |     |     | Model            |                                           | Train-ValRMSE |     | Train-ValR2 | TestRMSE | TestR2  |
| --------------- | --- | --- | --- | --- | --- | ---------------- | ----------------------------------------- | ------------- | --- | ----------- | -------- | ------- |
| scoresabove0.5. |     |     |     |     |     | MeanRegressor    |                                           | 0.7499        |     | 0.0000      | 0.7175   | -0.0003 |
|                 |     |     |     |     |     | LinearRegression |                                           | 0.2650        |     | 0.8751      | 0.6747   | 0.1154  |
|                 |     |     |     |     |     | MLPRegressor     |                                           | 0.7500        |     | -0.0004     | 0.7174   | 0.0000  |
|                 |     |     |     |     |     | ProposedApproach |                                           | 0.0382        |     | 0.9974      | 0.6714   | 0.1240  |
|                 |     |     |     |     |     | Table4:          | Thetrait-levelresultsforExtraversionusing |               |     |             |          |         |
theproposedapproachaswellasbaselinemodels
ComparedtoExtraversion,theresultsproduced
byallofthemodelsfortheConscientiousnesstrait
|     |     |     |     |     |     | are considerably |     | worse. |      | The proposed |     | approach |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ---- | ------------ | --- | -------- |
|     |     |     |     |     |     | performs         | the | worst  | with | a test RMSE  | of  | 0.6760   |
andatestR2
valueof-0.2273,whilethelinearre-
gressionmodelperformsthebestwithatestRMSE
Figure2: AcomparisonoftestF1scoresbetweenbase- of0.6010andatestR2 valueof0.0298. Thesere-
linemajorityclassclassifiersandthebestitemmodels
sultsshowthattheinitialitem-basedapproachfor
forExtraversion
Conscientiousnessleavesmuchtobeimproved,as
directtraitmodelingstillworksbetterinpredicting
| 4.1.2 | Trait-LevelEvaluationResults |     |     |     |     | overalltraitscores. |     |     |     |     |     |     |
| ----- | ---------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Table 4 and Table 5 present the trait-level results Interestingly,despitegenerallyhavingbettertest
comparingtheaggregatedpredictionsagainstthe RMSE scores, the Conscientiousness models ap-
peartohavepoorertestR2
ground-truthpersonalitytraitscoresforExtraver- scoresacrosstheboard,
sionandConscientiousness,respectively. There- whichmaysuggestthatwiththegivenfeatureset,
sultsoftheproposedapproacharealsocompared Conscientiousnesstraitscoresaremorechalleng-
tothatof3differentbaselines,particularly,amean ingtopredictcomparedtoExtraversion.

Trait-LevelResultsforConscientiousness
|                  |       |               |        |             |          |         | curacy                             | in  | the first | layer of classes, | specifically |             | in  |
| ---------------- | ----- | ------------- | ------ | ----------- | -------- | ------- | ---------------------------------- | --- | --------- | ----------------- | ------------ | ----------- | --- |
|                  | Model | Train-ValRMSE |        | Train-ValR2 | TestRMSE | TestR2  |                                    |     |           |                   |              |             |     |
|                  |       |               |        |             |          |         | Classes1-2,3,and4-5,respectively.  |     |           |                   |              | Theseafore- |     |
| MeanRegressor    |       |               | 0.6108 | 0.0000      | 0.6105   | -0.0010 |                                    |     |           |                   |              |             |     |
| LinearRegression |       |               | 0.2499 | 0.8326      | 0.6010   | 0.0298  |                                    |     |           |                   |              |             |     |
|                  |       |               |        |             |          |         | mentioned                          |     | scores    | for both traits   | show         | generally   |     |
| MLPRegressor     |       |               | 0.6144 | -0.0120     | 0.6162   | -0.0199 |                                    |     |           |                   |              |             |     |
| ProposedApproach |       |               | 0.2033 | 0.8892      | 0.6760   | -0.2273 |                                    |     |           |                   |              |             |     |
|                  |       |               |        |             |          |         | highervalues,meaningthatonthebroad |     |           |                   |              | levelof     |     |
classification,themodelsareabletoclassifymore
| Table | 5: The | trait-level |     | results for | Conscientiousness |     |     |     |     |     |     |     |     |
| ----- | ------ | ----------- | --- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
usingtheproposedapproachaswellasbaselinemodels accuratelycomparedtopreviousscores.
ThevalidationF1scoreslabeledspecific,onthe
|     |     |     |     |     |     |     | otherhand,arenotashighasthebroad |     |     |     |     | F1scores. |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --------- | --- |
4.2 EvaluationofProposedApproachwith
ThespecificF1scorespertainstotheaccuracyof
HierarchicalClassification
classifyingthedatatotheactualresponsepredic-
| Another |     | experiment | was | done | with the | proposed |                  |     |                  |     |     |     |     |
| ------- | --- | ---------- | --- | ---- | -------- | -------- | ---------------- | --- | ---------------- | --- | --- | --- | --- |
|         |     |            |     |      |          |          | tionclasses(i.e. |     | Class1,2,3,4,5). |     |     |     |     |
approach,particularlytheintegrationofahierarchi-
|     |     |     |     |     |     |     | The | validation | F1  | scores labeled |     | Binary | repre- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ------ | ------ |
calclassificationscheme. Asmentionedpreviously, sent the accuracy of predicting the right binary
hierarchicalclassificationattemptstoclassifythe class after the first classification layer has been
| dataintobroaderclasses(e.g. |     |     |     | Class1-2,Class4-5) |     |     |      |       |        |             |     |           |     |
| --------------------------- | --- | --- | --- | ------------------ | --- | --- | ---- | ----- | ------ | ----------- | --- | --------- | --- |
|                             |     |     |     |                    |     |     | done | (i.e. | Binary | 1 - Class 1 | and | 2, Binary | 2 - |
onthefirstclassificationlayer,thenclassifiesthe Class 3, Binary 3 - Class 4 and 5). Although the
datainamorespecificclass(e.g. Class1,Class2) F1scoresforeachBinaryaregenerallyhigh,this
| onthesecondlayer. |     |     | Thisexperimentwasdoneto |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
onlydealswithclassifyingthedataintooneortwo
attempttoclassifydatapointsbetterbygrouping
classes.
classesthatwereclosertoeachotherfirstandthen
Trait-LevelResultsforExtraversion
differentiatingthemlateron.
|     |     |     |     |     |     |     |     | Version |     | TestRMSE |     | TestR² |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- | ------ | --- |
Extraversion
|               |         |        |        |             |             |        |     | Original       |     | 0.6714 |     | 0.1240 |     |
| ------------- | ------- | ------ | ------ | ----------- | ----------- | ------ | --- | -------------- | --- | ------ | --- | ------ | --- |
| Train-ValRMSE |         |        | 0.2097 | TestRMSE    |             | 0.7126 |     |                |     |        |     |        |     |
| Train-ValR²   |         |        | 0.9218 | TestR²      |             | 0.0131 |     | Hierarchical   |     | 0.7126 |     | 0.0131 |     |
| Item          | ValF1   | ValF1  | ValF1  | ValF1 ValF1 | Train-ValF1 | TestF1 |     |                |     |        |     |        |     |
|               | (Broad) | (Spe-  | (Bi-   | (Bi- (Bi-   |             |        |     | Classification |     |        |     |        |     |
|               |         | cific) | nary   | nary nary   |             |        |     |                |     |        |     |        |     |
|               |         |        | 1)     | 2)          | 3)          |        |     |                |     |        |     |        |     |
Item1 0.5685 0.3502 0.6520 1.0000 0.5399 0.9519 0.3892 Table8: ExtraversionTrait-LevelResultsforOriginal
| Item6R | 0.5359 | 0.3990 | 0.7825 | 1.0000 0.6313 | 0.9822 | 0.3138 |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
andHierarchicalExperiments
| Item11  | 0.5220 | 0.3431 | 0.6040 | 1.0000 0.5613 | 1.0000 | 0.3905 |     |     |     |     |     |     |     |
| ------- | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| Item16  | 0.5560 | 0.3350 | 0.7307 | 1.0000 0.5815 | 0.7085 | 0.3205 |     |     |     |     |     |     |     |
| Item21R | 0.5567 | 0.3643 | 0.7508 | 1.0000 0.5445 | 0.7209 | 0.2999 |     |     |     |     |     |     |     |
| Item26  | 0.4956 | 0.3913 | 0.6427 | 1.0000 0.7402 | 1.0000 | 0.3230 |     |     |     |     |     |     |     |
| Item31R | 0.6579 | 0.4650 | 0.6269 | 1.0000 0.5986 | 0.9412 | 0.4284 |     |     |     |     |     |     |     |
Trait-LevelResultsforConscientiousness
| Item36 | 0.5317 | 0.3236 | 0.5018 | 1.0000 0.5692 | 0.6096 | 0.2848 |     |         |     |          |     |        |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | ------- | --- | -------- | --- | ------ | --- |
|        |        |        |        |               |        |        |     | Version |     | TestRMSE |     | TestR² |     |
Table6: ExtraversionResultswithHierarchicalClassi-
|     |     |     |     |     |     |     |     | Original |     | 0.6760 |     | -0.2273 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | --- | ------- | --- |
fication
|     |     |     |     |     |     |     |     | Hierarchical |     | 0.6270 |     | -0.0560 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | ------- | --- |
Classification
Conscientiousness
Train-ValRMSE 0.2015 TestRMSE 0.6270 Table9:ConscientiousnessTrait-LevelResultsforOrig-
| Train-ValR² |     |     | 0.8911 | TestR² |     | -0.0560 |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
inalandHierarchicalExperiments
| Item  | ValF1   | ValF1  | ValF1  | ValF1 ValF1   | Train-ValF1 | TestF1 |          |     |           |             |       |     |       |
| ----- | ------- | ------ | ------ | ------------- | ----------- | ------ | -------- | --- | --------- | ----------- | ----- | --- | ----- |
|       | (Broad) | (Spe-  | (Bi-   | (Bi- (Bi-     |             |        |          |     |           |             |       |     |       |
|       |         | cific) | nary   | nary nary     |             |        |          |     |           |             |       |     |       |
|       |         |        | 1)     | 2)            | 3)          |        |          |     |           |             |       |     |       |
|       |         |        |        |               |             |        | Overall, |     | observing | the results | found | in  | Table |
| Item3 | 0.6373  | 0.6281 | 0.8617 | 1.0000 0.5824 | 0.8263      | 0.5742 |          |     |           |             |       |     |       |
Item8R 0.6366 0.5419 0.5513 1.0000 0.6123 0.8297 0.5078 7,thevalidationscoreslooksomewhatpromising,
| Item13 | 0.7167 | 0.4909 | 0.8526 | 1.0000 0.5480 | 1.0000 | 0.4366 |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Item18R 0.5135 0.4036 0.4775 1.0000 0.5090 0.9859 0.3380 withpredictionsthatlookmoreaccurateafterpass-
| Item23R | 0.7327 | 0.4451 | 0.7957 | 1.0000 0.5514 | 0.9712 | 0.4388 |     |     |     |     |     |     |     |
| ------- | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Item28 0.6344 0.5052 1.0000 1.0000 0.5099 0.8611 0.4555 ingthroughtwolayersasopposedtotheoriginal
Item33 0.5780 0.4435 0.9033 1.0000 0.6314 0.9925 0.3608 proposed approach for Conscientiousness. It can
| Item38 | 0.5016 | 0.4434 | 0.7528 | 1.0000 0.6323 | 0.6317 | 0.3406 |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Item43R 0.6583 0.4156 0.7148 1.0000 0.5480 0.7604 0.5399 be observed that the approach with hierarchical
Table7: ConscientiousnessResultswithHierarchical classificationisapotentiallyviablemethodinclas-
| Classification |     |     |     |     |     |     | sifyingasitproducedmoreaccurateresultsatthe |     |                 |     |        |        |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --------------- | --- | ------ | ------ | --- |
|                |     |     |     |     |     |     | item-level.                                 |     | This difference | in  | metric | scores | may |
Tables6and7showtheresultsoftheitemmod- likelybeattributedtothestep-by-stepprocessof
elswithhierarchicalclassification,alongwiththe classifying the data, where data is classified in a
validationF1scoresforeachlayerforbothbroad broaderthresholdofsimilarclassesandthenfurther
andbinaryclassification. differentiatedonthesecondlevel. Bybreakingthe
Thebroad F1scoresrepresentclassificationac- modeling process into two phases, this approach

betteraccountedfortheinherentordinalityofthe Theycandelveintomoreexperimentationsthataim
dataandshowedthatthemodelsstillhadpotential todeterminehowthedataqualitativelycorrelates
fordistinguishingbetweenhighandlowresponses, to model performance, and what can be changed
which was particularly beneficial for the Consci- duringpreprocessing,extraction,andreductionin
entiousness trait. However, despite an improved orderformodelstolearnbetterfromthemandat-
item-levelperformance,thetrait-levelresultsstill tainthemostoptimalperformanceresults. Another
muchtobedesired. Thatsaid,itisstillastepinthe angleofinterestisexaminingtrait-levelresultcor-
rightdirectiontobeabletoclassifytheitem-level relations with feature tokens, as this may help in
datamoreaccuratelyatleastatthebroad level. identifyingtrendsorpatternsintermsofhoweach
|     |     |     |     |     |     | trait’s best | performing |     | approach |     | assigns | weights |     |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | -------- | --- | ------- | ------- | --- |
5 Conclusion
|     |     |     |     |     |     | or significance |     | to  | certain | terms | or phrases, |     | espe- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ------- | ----- | ----------- | --- | ----- |
ciallyconsideringthemixofEnglishandFilipino
Followinginitialitem-levelandtrait-levelevalua-
linguisticnuances.
| tions of | the approach, |     | it was | inferred | that due to |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ------ | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Atamoregenerallevel,futurestudiesmayoptto
dataimbalance,substantialresultsbecamehardto
|     |     |     |     |     |     | focusonawiderscope. |     |     | Recommendationsinclude |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------------------- | --- | --- | --- | --- |
derivebecausemodelsperformedpoorlyinterms
|               |     |             |     |      |              | exploring | multimodal |     | approaches |     | that | make | use |
| ------------- | --- | ----------- | --- | ---- | ------------ | --------- | ---------- | --- | ---------- | --- | ---- | ---- | --- |
| of item-level |     | prediction, | and | were | even outper- |           |            |     |            |     |      |      |     |
ofimagesalongsidetextualdata,testingtheitem-
formedbybaselineclassifiersandregressionmod-
|     |     |     |     |     |     | based approach |     | on  | a high-resource |     |     | language | like |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --------------- | --- | --- | -------- | ---- |
els. Inhopesofaddressingthisissue,ahierarchical
|                |          |     |     |             |           | English | to more | accurately |     | assess |     | the impact | of  |
| -------------- | -------- | --- | --- | ----------- | --------- | ------- | ------- | ---------- | --- | ------ | --- | ---------- | --- |
| classification | approach |     | was | integrated, | which in- |         |         |            |     |        |     |            |     |
dataquantity,andinvestigatingmethodologieson
| volved | breaking | down | the modeling |     | process into |     |     |     |     |     |     |     |     |
| ------ | -------- | ---- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
howtoproperlystructuresocialmediadata.
| twophases. | Implementingthismethodshoweda |     |     |     |     |        |       |     |      |         |     |                |     |
| ---------- | ----------------------------- | --- | --- | --- | --- | ------ | ----- | --- | ---- | ------- | --- | -------------- | --- |
|            |                               |     |     |     |     | Future | works | may | also | address |     | the identified |     |
somewhatdistinctadvantage,mostnotablyforthe
|                         |     |     |                         |     |     | issues from | the     | results | of       | the          | study, | mainly   | data |
| ----------------------- | --- | --- | ----------------------- | --- | --- | ----------- | ------- | ------- | -------- | ------------ | ------ | -------- | ---- |
| Conscientiousnesstrait. |     |     | However,whilethehierar- |     |     |             |         |         |          |              |        |          |      |
|                         |     |     |                         |     |     | imbalance   | leading |         | to model | overfitting, |        | hyperpa- |      |
chicalapproachworkedrelativelybetterforCon-
rameterlimitations,anddataqualityorweightas-
| scientiousness,  |     | the original                  |     | pipeline | still reigned |                      |     |     |                         |       |     |        |     |
| ---------------- | --- | ----------------------------- | --- | -------- | ------------- | -------------------- | --- | --- | ----------------------- | ----- | --- | ------ | --- |
|                  |     |                               |     |          |               | signmentsonfeatures. |     |     | Thiscanbedonebyincreas- |       |     |        |     |
| forExtraversion. |     | Thisdifferenceinmodelinclina- |     |          |               |                      |     |     |                         |       |     |        |     |
|                  |     |                               |     |          |               | ing hyperparameter   |     |     | search                  | space | and | number | of  |
tionmaybeattributedtothedifferenceinfeature
iterationsforthemodels,aswellasattemptingto
significancebetweenthetwotraits.
experimentonlywiththeunigramdatainsteadof
| It is | also worth |     | noting that | when | compared |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
includingbigrams.
againstbaselinemodels,theoriginalpipelinestill
|     |     |     |     |     |     | The | potential | of  | the hierarchical |     |     | approach | can |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------- | --- | --- | -------- | --- |
performedbestforExtraversion,whereasthebase-
alsobeexpoundedupon;withproperdatabalanc-
linesperformedbetterforConscientiousnesseven
ingmethodsandtherightsetofconfigurations,this
withtheslightimprovementprovidedbythehierar-
|                 |     |                              |     |     |     | approach | may | proveto | beintegraland |     |     | beneficial |     |
| --------------- | --- | ---------------------------- | --- | --- | --- | -------- | --- | ------- | ------------- | --- | --- | ---------- | --- |
| chicalapproach. |     | Thissupportsthedeductionthat |     |     |     |          |     |         |               |     |     |            |     |
totheoverallpipeline.
Conscientiousnessitemsresponsesmaybeharder
Otherrecommendationsincludeexploringother
topredict,particularlywiththegivendata.
featureextractionandreductiontechniques,aswell
Withtheseresults,itisevidentthatthisparticular
|     |     |     |     |     |     | as utilizing | the | remaining |     | three | traits | of the | Big |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ----- | ------ | ------ | --- |
fieldofAPRstudy,especiallyinaFilipinocontext,
Five(Openness,Agreeableness,andNeuroticism)
| leaves much | room | for | pondering |     | and experimen- |     |     |     |     |     |     |     |     |
| ----------- | ---- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
todetermineiftheproposedapproachcouldwork
tation. Somemodelsindeedshowedpromise,but
|                          |           |      |                     |        |               | equally               | or better | as  | compared |     | to its   | Extraversion |     |
| ------------------------ | --------- | ---- | ------------------- | ------ | ------------- | --------------------- | --------- | --- | -------- | --- | -------- | ------------ | --- |
| even the                 | so-called | best | performing          |        | models have   |                       |           |     |          |     |          |              |     |
|                          |           |      |                     |        |               | and Conscientiousness |           |     | results. |     | Future   | works        | are |
| verylowtestmetricscores. |           |      | Theoverallresultsof |        |               |                       |           |     |          |     |          |              |     |
|                          |           |      |                     |        |               | also recommended      |           |     | to test  | the | proposed | approach     |     |
| this study               | signify   | that | more                | tuning | for both data |                       |           |     |          |     |          |              |     |
againstdiversedatasetsanddifferentsocialmedia
| and models | needs | to  | be done | for this | item-based |           |     |          |     |          |     |        |        |
| ---------- | ----- | --- | ------- | -------- | ---------- | --------- | --- | -------- | --- | -------- | --- | ------ | ------ |
|            |       |     |         |          |            | platforms | and | contexts |     | in order | to  | have a | better |
approachtomanifestimprovementsandbecomea
benchmarkforperformanceandgeneralizability.
frameworkthatcanprovebeneficialtoAPR.
6 Recommendation
Futureworksthatwillchoosetobuilduponthere-
sultsfromthisstudyareencouragedtofocusmore
| on the best | performing |     | approaches |     | for each trait. |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |

References
Alexander H. II Agno, Jesah R. Gano, and
ClaudeKristofferSedillo.2019. InstagramvsTwit-
ter: Analyzing the manifestation of personality
throughthewritingstyleofFilipinoSNSusers. Bach-
elor’sthesis,DeLaSalleUniversity.
AmericanPsychologicalAssociation. Personality.
Steven Bird, Edward Loper, and Ewan Klein. 2009.
NaturalLanguageProcessingwithPython.O’Reilly
MediaInc.
Ronn Christian Chua Chiaco, Howard Montecillo,
RonellJohnRoxas,andBryanEthanTio.2022. Ap-
plicationofwordembeddingsonautomaticperson-
alityrecognitionusingFilipinoTwitterdata. Bache-
lor’sthesis,DeLaSalleUniversity.
AndrewMarges.2019. pinoy_tweetokenize.
Sumiya Mushtaq and Neerendra Kumar. 2022. Text-
based automatic personality recognition: Recent
developments. In Proceedings of Third Interna-
tionalConferenceonComputing,Communications,
and Cyber-Security: IC4S 2021, pages 537–549.
Springer.
EdwardTighe,LuigiAcorda,AlexanderIiAgno,Jesah
Gano, Timothy Go, Gabriel Santiago, and Claude
Sedillo.2022. Collectionmethodsanddatacharac-
teristicsofthePagkataoKodataset. InProceedings
ofthe36thPacificAsiaConferenceonLanguage,In-
formationandComputation,pages513–524,Manila,
Philippines.AssociationforComputationalLinguis-
tics.
EdwardTighe,OyaAran,andCharibethCheng.2020.
Exploringneuralnetworkapproachesinautomatic
personalityrecognitionofFilipinoTwitterusers. In
Proceedingsofthe20thPhilippineComputingSci-
enceCongress,pages137–145.
Edward Tighe and Charibeth Cheng. 2018. Model-
ing personality traits of Filipino Twitter users. In
Proceedings of the Second Workshop on Computa-
tional Modeling of People’s Opinions, Personality,
andEmotionsinSocialMedia,pages112–122,New
Orleans,Louisiana,USA.AssociationforComputa-
tionalLinguistics.