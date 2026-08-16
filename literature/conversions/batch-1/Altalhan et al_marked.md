---
conversion_metadata:
  converted_at: "2026-07-22T11:55:23Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Altalhan et al.pdf"
  source_pdf_sha256: "02751206a9c5c75f816d3b52572879022ad828dff2c209da99ecca1f220a7e09"
  page_count: 14
  markdown_char_count: 171626
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 24 December 2024, accepted 10 January 2025, date of publication 20 January 2025, date of current version 23 January 2025.

Digital Object Identifier 10.1109/ACCESS.2025.3531662

Imbalanced Data Problem in Machine Learning:
A Review

MANAHEL ALTALHAN , ABDULMOHSEN ALGARNI
AND MONIA TURKI-HADJ ALOUANE , (Member, IEEE)
Department of Computer Science, King Khalid University, Abha 61421, Saudi Arabia

,

Corresponding author: Manahel Altalhan (445816339@kku.edu.sa)

This work was supported by the Deanship of Research and Graduate Studies, King Khalid University, through Small Group Research
under Grant RGP1/71/45.

ABSTRACT One of the prominent challenges encountered in real-world data is an imbalance, characterized
by unequal distribution of observations across different target classes, which complicates achieving accurate
model classifications. This survey delves into various machine learning techniques developed to address
the difficulties posed by imbalanced data. It discusses data-level methods such as oversampling and
undersampling, algorithm-level solutions including ensemble learning and specific algorithm adjustments,
cost-sensitive algorithms, and hybrid strategies that combine multiple approaches. Moreover, this paper
emphasizes the crucial role of evaluation methods like Precision, F1 Score, Recall, G-mean, and AUC in
measuring the effectiveness of these strategies under imbalanced conditions. A detailed review of recent
research articles helps pinpoint persistent gaps in generalizability, scalability, and robustness across these
methods, underscoring the necessity for ongoing improvements. The survey seeks to offer an extensive
overview of current approaches that improve the efficiency and effectiveness of machine learning models
dealing with imbalanced datasets, thus equipping researchers with the insights needed to develop robust and
effective models ready for real-world application.

INDEX TERMS Imbalanced data, machine learning, balance techniques, evaluation methods.

I. INTRODUCTION
Imbalanced data poses a major challenge in machine learning.
This occurs when the class distribution within a dataset is
uneven, resulting in what is referred to as imbalance [1].
It means that one data class is significantly larger than
the others. Most instances are part of the dominant class
(the negative or majority class), with only a small number
represented in the other classes (the positive or minority
class) [2]. It causes a fundamental problem in machine
learning, as when classifiers are trained on this type of
data in which the distribution is unbalanced, the classifier’s
conduct becomes biased in favor of the dominant class,
often overlooking the lesser class [3]. This results in
misclassifying instances within the minority class, which is
usually exceedingly critical due to the affected part they want

The associate editor coordinating the review of this manuscript and

approving it for publication was Sawyer Duane Campbell

.

to discover constantly occurring in a few examples compared
to all examples [2]. Imbalanced datasets present four key
challenges: bias, overlap, feature vector size, and dataset
size [4]. This scenario is prevalent across various domains
such as healthcare like diabetes diagnosis [5] and skin lesion
classification [6], Finance like credit fraud detection [7],
Engineering like fault detection in wind turbines [8], and
recognition rotting or dead tree [9], [10] and others.

The consequences of imbalanced data are far-reaching.
In situations such as medical diagnosis, where accurately
identifying rare diseases is vital, models that favor the major-
ity class may lead to overlooked diagnoses and compromised
patient care [11]. Similarly, in fraud detection, the machine
learning model tends to exhibit bias towards the predominant
class, causing a decrease in True Positives (TP) and an
increase in False Positives (FP) [12], allowing fraudulent
activities to go undetected. Thus, addressing imbalanced data
is imperative for building reliable and effective ML systems.

13686

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

VOLUME 13, 2025

---

<!-- PAGE 2 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

Now, the importance and seriousness of this problem have
become clear to us.

Over the years, researchers have developed numerous
methods to counteract the effects of class imbalance, encom-
passing three primary classifications: data-level techniques,
algorithm-level
techniques, and integrated methods [7],
[13]. Data-level techniques involve modifying the dataset
before the classifier is trained, including under-sampling the
dominant class, over-sampling the minor class, or creating
synthetic data [7], [14]. Conversely, algorithm-level tech-
niques modify the learning algorithms to manage imbalanced
data more efficiently without compromising the data itself,
often through cost-sensitive learning, ensemble methods,
or algorithm-specific adjustments [13].

While data-level and algorithm-level techniques offer valu-
able strategies for addressing imbalanced data, they each have
limitations. Data-level techniques may discard potentially
useful information or introduce noise through synthetic data
generation [15]. Algorithm-level techniques, while effective,
may not fully exploit the available data or may require
complex adjustments for different algorithms [13].

Data-level and algorithm-level techniques [7], these hybrid
approaches aim to leverage each category’s strengths while
mitigating their weaknesses. Examples include combined
sampling techniques, algorithmic resampling strategies, and
ensembles of resampled datasets. Evaluation metrics like
accuracy and precision may not adequately capture model
performance in imbalanced datasets. Hence, metrics such
as AUC (area under the precision-recall (PR) curve) and
AUC (area under the receiver operating characteristic (ROC)
curve), and the F1-score have been proposed and shown to
be effective in classifying tasks with imbalanced data [16].
Additionally, researchers have introduced class-weighted
evaluation frameworks that accommodate arbitrary skews
in class cardinalities and importance, effectively addressing
challenges presented by imbalanced datasets.

The subsequent sections of the paper will follow this
structure. Section II outlines the review strategy, including
the research questions that guide the survey. Next, Section III
delves into the foundational techniques of oversampling
and undersampling, providing an overview of their role in
addressing data imbalance. Section IV explores a broad
spectrum of balance strategies, categorized into data-
level, algorithm-level, and hybrid approaches, with each
subsection detailing methods to enhance model performance
when dealing with imbalanced datasets. In Section V, the
limitations of each technique are discussed, along with
justifications for their inclusion. Following this, Section VI
examines various evaluation methods essential for assessing
the effectiveness of models handling imbalanced data,
highlighting metrics like F1 Score, AUC, and others to
provide a nuanced understanding of model efficacy. Finally,
Section VII synthesizes these insights to offer a conclusive
summary of the current techniques for managing imbalanced
data in machine learning, pinpointing existing gaps in each
approach.

including Google Scholar,

II. REVIEW STRATEGY
This survey investigates the imbalanced data problem
in machine learning by reviewing studies from various
IEEE, Springer,
databases,
is placed on
Elsevier, MDPI, and others. Emphasis
recent advancements, with most reviewed studies published
between 2020 and 2024, ensuring the latest methodologies
and insights are included. The search process utilized
specific keywords such as ‘‘imbalanced data,’’
‘‘class
imbalance,’’ ‘‘machine learning,’’ ‘‘data-level techniques,’’
‘‘algorithm-level solutions,’’ ‘‘oversampling,’’ ‘‘undersam-
pling,’’ ‘‘SMOTE,’’ ‘‘cost-sensitive learning,’’ ‘‘Ensemble
methods,’’ and ‘‘hybrid approaches.’’ This review has inves-
tigated 40 studies, and most of the papers are from journals
ranked in Q1 and Q2 categories, ensuring high-quality and
impactful contributions. The selected references encompass
foundational approaches, innovative techniques, and domain-
specific solutions, providing a comprehensive analysis of the
field. This strategy offers a deep understanding of current
approaches to addressing data imbalance challenges while
identifying research gaps that indirectly illuminate potential
future directions.

This review aims to address key questions that encompass
all aspects of the imbalanced data problem in machine
learning:

1- Q1: How effective are fundamental approaches, such
as oversampling and undersampling, in addressing class
imbalance across applications?

2- Q2: What are the findings and limitations of data-level,
algorithm-level, and hybrid techniques in achieving
class balance?

3- Q3: How do these limitations limit the overall perfor-

mance of the balancing techniques?

4- Q4: Which evaluation metrics best assess the success of

balancing techniques in ML and DL tasks?
The first section of the review focuses on answering the
first question, providing a foundational understanding.
The second section elaborates on the second ques-
tion, offering detailed insights. The third question is
addressed by analyzing the limitations and shortcomings
of various techniques, as discussed in the third section
of the review. Finally, the fourth part provides a concise
and clear response to the fourth question, wrapping up
the review comprehensively.

III. FUNDAMENTAL APPROACHES TO CLASS
DISTRIBUTION BALANCING
This section delves into the fundamental methods to mitigate
class imbalance in ML: oversampling and undersampling,
which the figure 1 shows. Class imbalance is critical
in predictive modeling, often resulting in biased model
outcomes that favor the majority class disproportionately.
Addressing this imbalance is essential to foster fair and
precise models. Over/Under sampling are two key techniques
that adjust the arrangement of classes in training datasets

VOLUME 13, 2025

13687

---

<!-- PAGE 3 -->

to create a more balanced environment for model training.
A thorough exploration of these foundational techniques
prepares the groundwork for the advanced balancing methods
detailed in subsequent sections of this survey.

FIGURE 1. Basic approaches to class distribution balance.

A. OVERSAMPLING
Oversampling targets enhancing the minority class’s rep-
resentation within a dataset, bringing its frequency up
to parity with the majority class. This adjustment can
be realized by simply duplicating existing instances or
creating new, synthetic ones through methodologies like
SMOTE (Synthetic Minority Oversampling Technique) [17].
SMOTE and its derivatives, such as Borderline-SMOTE and
ADASYN, synthesize new samples by interpolating between
minority class instances that connect via line segments to their
nearest neighbors within the same class. These approaches
operate primarily in the feature space, thereby injecting a
higher degree of diversity into the lesser class and supporting
the model’s capability to generalize from limited data [18].

Advantages:
• Increases the model’s generalization abilities by intro-
ducing a more comprehensive range of variability within
the minority class, thus preparing the model for broader
scenarios.

• Safeguards against the loss of essential information in
minority class instances, which is particularly vital in
datasets where each example holds significant value.

Disadvantages:
• There is a risk of overfitting, as models might begin
to memorize the noise inherent in the synthetically
generated samples rather than learn to generalize from
the actual data.

• Elevates the computational burden, especially when
employing sophisticated synthetic instance generation
techniques, which can be resource-intensive.

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

Centroids, Tomek Links, or Near Miss are utilized to maintain
the statistical integrity of the majority class while minimizing
its quantity [19]. These methods enhance model performance
by eliminating instances that are either redundant or less
informative, thereby creating a more balanced dataset that
stops the model from being dominated by the traits of the
predominant class.
Advantages:
• Significantly reduces the time required for model
training by decreasing the dataset size, simplifying the
learning process.

• Reduces the likelihood of model bias toward the
majority class, promoting more fair and balanced
decision-making.

Disadvantages:
• There is a danger of losing essential data, as the removal
process may inadvertently discard crucial instances to
understand the predominant class comprehensively.

• May lead to underfitting, especially if

the diver-
sity within the majority class is not fully captured,
potentially impairing the model’s ability to generalize
effectively.

C. STRATEGIC CONSIDERATIONS FOR CHOOSING
BETWEEN OVERSAMPLING AND UNDERSAMPLING
Choosing between oversampling and undersampling requires
careful consideration of multiple aspects, such as dataset
size, data characteristics, available computing resources,
and the significance of minority class instances. Typically,
oversampling is preferred in scenarios where the minority
class includes critical, rare events that are essential
to
capture accurately, such as in fraud detection or diagnosing
rare medical conditions. Conversely, undersampling is often
more advantageous for extremely large datasets, where
reducing the volume of data can significantly enhance
computational efficiency and where there is enough data
redundancy to minimize the risk of
losing important
information [20].

To achieve the best of both worlds, hybrid approaches that
merge elements of both oversampling and undersampling
are becoming more prevalent. Methods like SMOTEEN,
combining SMOTE with Edited Nearest Neighbors, or var-
ious ensemble techniques incorporating different resampling
strategies within a single classifier framework can provide
a more balanced dataset [21]. These hybrid methods help
ensure that models are not only efficient but also retain the
integrity and diversity of data, thus enhancing overall model
performance without sacrificing detail or computational
speed.

B. UNDERSAMPLING
In contrast to oversampling, undersampling aims to balance
class allocation by reducing the size of
the majority
class, often achieved through the random deletion of its
instances [17]. More refined techniques such as Cluster

IV. BALANCE TECHNIQUES
Many dataset characteristics determine the most suitable
techniques for addressing imbalance (data-level, algorithm-
level, or hybrid). One key factor is the percentage of
imbalance, which varies from dataset to dataset. Knowing

13688

VOLUME 13, 2025

---

<!-- PAGE 4 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

it gives a clear understanding of the distribution of classes
in the dataset, whether high or moderate. The percentage
of imbalance is critical for effectively handling imbalanced
datasets and building reliable ML models.

A. DATA-LEVEL TECHNIQUES
Data level techniques focus on aligning class distributions
by adjusting the size of training datasets through resampling,
have become widely adopted [22], which aims to equalize
the class distribution through two methods: Undersampling
and Oversampling [23]. Although resampling directly bal-
ances the training set, it introduces two main challenges:
oversampling may lead to overfitting and reduced gen-
eralization on the test set, whereas undersampling may
result in a significant loss of knowledge from the majority
class [13]. Standard undersampling methods include Random
Undersampling, Tomek Links, and Cluster Centroids [24].
Typically, to prevent the substantial depletion of instances
from the predominant class, oversampling techniques are
often preferred [4]. Prominent oversampling methods include
SMOTE, ADASYN (Adaptive Synthetic Sampling), and
Borderline-SMOTE [24].

SMOTE represents a commonly adopted oversampling
method [25]. It identifies instances near within the feature
space, establishes connections between them, and generates
new samples along those connections. Nonetheless, generat-
ing synthetic examples without accounting for the majority
class can create ambiguous instances, especially when there
is significant overlap between classes, which is a notable
drawback of this approach [13].

Many hybrid-sampling methods and SMOTE variants
shown in table 1 have been proposed to address these
challenges. Modify SMOTE-N (Synthetic Minority Over-
sampling Technique for nominal data) to suit the nominal
attributes of the data [25]. SMOTEENN (combining SMOTE-
N with Edited Nearest Neighbors) aims to rectify class
imbalance by oversampling the minority class and enhancing
dataset quality through the elimination of noisy samples, and
SMOTE-Tomek (combining SMOTE-N with Tomek links) to
simultaneously create synthetic samples for the lesser class
and undersample the greater class, effectively rebalancing
the dataset and improving classification outcomes [26].
Distance-based SMOTE (D-SMOTE) regulates class overlap
through a distance parameter, creating synthetic samples that
better represent the minority class. Bi-phasic SMOTE (BP-
SMOTE), on the other hand, overcomes traditional SMOTE’s
shortcomings by enhancing the oversampling procedure
through instance selection, guaranteeing the inclusion of
only pertinent instances in the resultant training dataset [4].
CDSMOTE combines (class decomposition and synthetic
minority oversampling); it starts by dividing the majority
class into subclasses and then using SMOTE to increase the
sample size of the minority class. This approach strives to
attain a balanced data distribution while retaining crucial
information [27]. Radius Synthetic Minority Oversampling

Technique (RSMOTE) is unlike traditional SMOTE, which
connects minority samples to create synthetic instances along
line segments; it identifies the nearest samples from the
majority class within a specified radius to generate synthetic
data points, aiding in the creation of more diverse and realistic
synthetic samples [28]. The SASMOTE (a self-inspected
adaptive SMOTE approach) overcomes traditional SMOTE
limitations by prioritizing visible neighbors and eliminating
low-quality samples. Integrating adaptive nearest neighbor-
hood selection and self-inspection for uncertainty evaluation
elevates the quality of resampled data, particularly beneficial
for highly imbalanced healthcare classification tasks [29].
Borderline-SMOTE is a sampling technique employed in
managing imbalanced datasets, particularly in situations such
as fraud detection in credit card transactions. It generates
synthetic samples for the underrepresented class by targeting
instances close to the decision boundary between classes,
often known as borderline instances [30]. The Oriented
Oversampling with Spatial Information Method (OOSI)
tackles challenges in imbalanced and noisy datasets through
a robust and adaptive approach that includes three critical
phases: Oriented Information Sampling, Spatial Information
Quantification, and Adaptive Data Space Partitioning [31].
The Synthetic and Dependent Wild Bootstrapped Oversam-
pling Method (SDWBOTE) helps overcome the challenges
of skewed data in fault detection and localization tasks within
wind turbine systems. It considers temporal dependencies and
relationships among samples [8].

GAN-based methods, leveraging Generative Adversarial
Networks (GANs) composed of a generator and a discrimina-
tor, are gaining traction. These techniques generate synthetic
samples by understanding the inherent data distribution and
producing new samples that closely resemble actual data.
For instance, the GAN-based Data Augmentation Method
introduced by [6] seeks to improve the classification accuracy
of imbalanced skin lesion datasets. Another study explores
the (GANs) to address challenges associated with imbalanced
datasets in machine learning. Focusing on three real-world
datasets—Car Evaluation, Human Activity Recognition, and
Bank datasets—the research aims to enhance minority class
representation through data augmentation. The GAN-based
approach generates synthetic data to balance the dataset,
improving classification accuracy and model performance.
This study underscores the potential of GANs as an
effective tool for data augmentation and boosting model
robustness across diverse applications [33]. An innovative
Active Balancing Mechanism (ABM) is proposed to tackle
the challenges of imbalanced medical data, focusing on
myocardial infarction (MI) detection using electrocardiogram
(ECG) signals. The ABM incorporates Gaussian naïve Bayes
and entropy to enhance classification accuracy and reliabil-
ity. Additionally, a modified convolutional neural network
(MCNN) is developed to further optimize performance,
showcasing the method’s potential for real-time monitoring
and decision-making in clinical settings [32].

VOLUME 13, 2025

13689

---

<!-- PAGE 5 -->

TABLE 1. Effectiveness and limitations of Hybrid-sampling techniques.

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

B. ALGORITHM-LEVEL TECHNIQUES
Algorithmic strategies enhance learning in the minority class
by immediately altering the training process of the classifier
or modifying algorithms to address challenges associated
with imbalanced data effectively [34]. Common strategies
encompass:

1) COST SENSITIVE LEARNING
Cost-sensitive learning entails allocating varying weights or
costs to classes during the training process, prioritizing the
penalization of misclassifications of the minority class [35].
MetaCost is a cost-sensitive classification algorithm that

creates multiple classification models from the original
dataset and computes the class probability for each sample.
It
then applies a conditional risk formula to assign a
cost to each sample, subsequently re-labeling the training
set based on these costs. Still,
is less suitable for
handling imbalanced data in multi-class scenarios [36]. The
adaptive cost-sensitive learning (ACL) method, effective
under large imbalance ratios, dynamically adapts the sample
cost throughout the entire training process. The model is
trained using weighted losses in a manner that harmonizes
the contribution of each class to the model parameter
updates, preventing the dominance of majority classes in
imbalanced data during training. Calculating the costs for

it

13690

VOLUME 13, 2025

---

<!-- PAGE 6 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

the
samples considers the sample number distribution,
convergence trend of classes, and the convergence trend
of samples [37]. Another study employs cost-sensitive
learning to dynamically adjust class-specific costs within
deep neural networks, thereby improving the recognition
of minority classes. This approach is particularly useful in
applications such as medical diagnosis and fraud detection,
where accurately identifying underrepresented classes is
critical [35]. An innovative adaptive cost-sensitive learning
method is proposed to tackle the challenges of imbalanced
data in industrial fault diagnosis. This approach dynamically
calculates sample costs based on sample distribution and
convergence trends, effectively reducing the dominance
of majority classes during training. By ensuring adequate
representation of minority classes, the method significantly
enhances the performance of intelligent diagnostic models,
particularly in scenarios with high imbalance ratios [37].

2) ALGORITHM-SPECIFIC ADJUSTMENTS
Adjustments specific to algorithms entail customizing meth-
ods like decision trees, random forests, and SVMs to
handle imbalanced data more effectively, as demonstrated
in adaptive cost-sensitive learning, which enhances the
performance of intelligent diagnosis models in such con-
ditions. A Support Vector Machine (SVM) equipped with
Multiple Kernel Learning (MKL) allows the SVM to inte-
grate different kernel functions and fine-tune their weights,
thus improving its ability to classify imbalanced datasets
more accurately [38]. The Stratified Sampling-Based Deep
Neural Network (SSDNN) approach tackles imbalanced data
challenges by employing a stratified sampling technique,
enhancing prediction accuracy. Partitioning the dataset into
non-duplicated groups with balanced class representation
increases computational complexity due to the stratified
sampling method [9]. GENDA (Generative Neighborhood-
based Deep Autoencoder) is a novel generative model to
address the imbalance, particularly for image and time-
representations of
series data [13]. By learning latent
the data and generating synthetic samples for minority
classes,
its flexibility allows for application in various
domains where original data usage is restricted. It provides
advantages over algorithm-level techniques by incorporating
data augmentation and addressing imbalance classification
without making distribution assumptions. A novel deep-
learning-based model is introduced to address data imbalance
in medical image classification. Acknowledging the under-
representation of many medical conditions in datasets, the
authors propose an innovative approach that utilizes effective
perturbation operations to extract relevant features from
single-class samples [39]. Another study conducts an in-
depth exploration of adapting class-balanced loss functions
for Gradient Boosting Decision Trees (GBDT) across diverse
tabular classification tasks, including binary, multi-class,
and multi-label classifications. The research highlights the
effectiveness of these loss functions in addressing class

imbalance challenges common in real-world applications.
Additionally, the study introduces a Python package that
simplifies the integration of these loss functions into GBDT
workflows, making advanced techniques more accessible to
researchers and practitioners [40].

3) ENSEMBLE METHODS
Ensemble methods entail merging multiple base classifiers
or models to forge a more robust learner to address the
imbalance problem [41]. Table 2 mentions some ensem-
ble methods, their findings, and their limitations. These
approaches leverage various algorithms or versions of the
same algorithm to bolster predictive performance on imbal-
anced datasets. It mitigates the impact of class imbalance by
blending predictions from multiple models, thus enhancing
the classifier’s overall performance. Boosting refers to a
group of machine learning techniques that successively
train a sequence of weak learners. Each learner aims to
rectify the errors of its predecessors by assigning higher
importance to misclassified cases. This iterative process
enables boosting to construct a resilient ensemble model
capable of making accurate predictions, which is particularly
beneficial in scenarios with class imbalance or noisy data.
AdaBoost, a renowned boosting algorithm, continuously
adjusts the weights of misclassified instances to improve
the model’s overall performance [42]. Bagging, or Bootstrap
Aggregating, generates multiple training dataset instances
via bootstrap sampling, training individual base learners
on each sample. The predictions of these base learners
are subsequently aggregated, usually through averaging,
to generate the final prediction. This process aims to
enhance machine learning models’ overall performance and
stability by mitigating variance and overfitting. Concur-
indirectly aids in addressing imbalanced data
rently,
issues [43]. Random forests, a widely favored ensemble
learning technique, amalgamate numerous decision trees to
enhance predictive accuracy. Every tree in the forest is
constructed from a randomized subset of features in the
training data, and the ultimate prediction is formed by
aggregating the predictions from all the trees [44]. Gradient
Boosting optimizes weak learners, typically decision trees,
to improve predictive accuracy. This algorithm functions
through iteratively constructing decision trees to rectify
the errors made by preceding trees. It achieves this by
assigning greater weights to misclassified samples in each
iteration [45]. A stacked deep learning algorithm leverages
ensemble methods to manage imbalanced data adeptly.
It integrates techniques such as Stacked CNN (Convolutional
Neural Networks) and Stacked RNN (Recurrent Neural
Networks), employing both to identify intricate patterns and
temporal interdependencies [4].

it

C. HYBRID APPROACHES
Hybrid approaches amalgamate various strategies, frequently
blending data-level and algorithm-level techniques as shown

VOLUME 13, 2025

13691

---

<!-- PAGE 7 -->

TABLE 2. Effectiveness and limitations of ensemble methods.

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

Adversarial Network (E-GAN)
technique amalgamates
features from both (GANs) and (CNNs), which are short-
cuts to generative adversarial networks and convolutional
neural networks, respectively. This fusion leverages the
data generation prowess of GANs and the classification
capabilities of CNNs [11]. A recent study that tackles the
challenge of imbalanced spectral data in materials science
through a Generative Adversarial Network (GAN)-based data
augmentation method. This approach uses joint optimization
between the GAN’s generator and a classifier, allowing
for the creation of synthetic samples that are both realistic
and effectively distinguishable across material phases [46].
By employing transfer learning and domain adaptation
techniques, explicitly using Maximum Mean Discrepancy
(MMD), this approach addresses the issue of imbalanced data
in detecting Return-Oriented Programming (ROP) attacks.
It leverages balanced data from a source domain to train a
model while minimizing the MMD to align the distributions
of the source and target domains [47]. The integration
of Genetic Algorithm (GA) with Support Vector Machine
(SVM) seeks to optimize SVM parameters while using
targeted sampling techniques to manage class imbalance
effectively [48].

2) ALGORITHMIC ENSEMBLE WITH DATA-LEVEL
TECHNIQUES
Integrating algorithmic ensemble with data-level techniques
involves generating multiple models by employing diverse
resampled dataset versions and consolidating their pre-
dictions. SMOTEBoost and RUSBoost exemplify these
techniques, with SMOTEBoost combining the SMOTE
algorithm with boosting to enhance predictions in imbalanced

FIGURE 2. Approaches to handle imbalanced data problem.

in figure 2. These methodologies provide a comprehensive
solution to tackle class imbalance challenges, enhancing
machine learning models’
resilience, effectiveness, and
reliability. By integrating multiple methods, they aim to
alleviate issues like overfitting, information loss, and poor
performance in minority classes, thus enhancing the overall
effectiveness of machine learning models in managing class
disproportionality. Table 3 highlights the hybrid techniques
employed in recent years. Common hybrid approaches
include:

1) DATA-PRE-PROCESSING WITH
ALGORITHM-ADJUSTMENTS
Data preprocessing incorporating algorithm adjustments:
involves using techniques
like over-sampling, under-
sampling, or SMOTE to prepare the data before applying
algorithm-level adjustments. The Enhanced Generative

13692

VOLUME 13, 2025

---

<!-- PAGE 8 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

TABLE 3. Effectiveness and limitations of hybrid approaches to handle imbalanced data.

datasets. It overcomes the constraints of traditional boosting
algorithms such as AdaBoost, boosts learning by creating
synthetic examples for the minority class and adjusting the
training distribution to focus on these instances [49], and
RUSBoost combines Random UnderSampling (RUS) with
boosting entails undersampling the majority class and subse-
quently boosting the classifier on the balanced dataset [50].
Integrating (DB-SLSMOTE) with (Random Forest) tackles
class imbalance by augmenting the minority class through
oversampling by synthetic samples generated from density

distribution. Subsequently, Random Forest harnesses this
balanced dataset to construct a resilient ensemble model,
enhancing classification effectiveness [51]. Before applying
the MCNN-LSTM model, the Tomek-Links technique is
utilized as an undersampling method to manage imbalanced
data.

The MCNN-LSTM model is a hybrid framework where
Convolutional Neural Networks (CNN) are effective in text
data when capturing local features and patterns. In contrast,
Long Short-Term Memory (LSTM) networks are tailored for

VOLUME 13, 2025

13693

---

<!-- PAGE 9 -->

text classification tasks, instrumental in situations with imbal-
anced data. This integration addresses the inherent challenges
of imbalanced data in text classification endeavors [52]. Inte-
grating oversampling techniques with ensemble deep learn-
ing models involves merging modified oversampling methods
like (D-SMOTE) Distance-based SMOTE and (BP-SMOTE)
Bi-phasic SMOTE with Stacked CNN and Stacked RNN.
It enhances predictive accuracy and robustness in handling
imbalanced datasets [4]. In [53], authors combined Deep
Convolutional Generative Adversarial Networks(DCGAN)
for generating synthetic samples and Convolutional Neural
Networks (CNN) for classification and feature extraction.
The research by [54] integrates resampling techniques like
SMOTE and US to rebalance class distributions. Moreover,
it employs Particle Swarm Optimization (PSO) for attribute
selection to improve sensitivity and reduce data dimension-
ality. At the same time, MetaCost is utilized as an algorithm-
level approach to address class imbalances effectively.
Another investigation employs a blend of undersampling
using Tomek Links, clustering via BIRCH, and oversampling
through Borderline SMOTE to address the imbalance in
credit card transaction datasets and by removing noise with
Tomek Links, clustering the data with BIRCH and generating
synthetic instances for the underrepresented class through
Borderline SMOTE, this approach seeks to equalize the
dataset effectively [7]. The ATOMIC approach represents an
automated machine-learning method explicitly designed for
imbalanced classification tasks. It addresses the challenges
posed by imbalanced datasets through a combination of
the algorithmic ensemble, which optimizes the selection
of learning algorithms, and data-level techniques, which
optimize resampling strategies and hyperparameters [55].
A study examines the challenges of classifying minority
classes in imbalanced datasets, with a focus on cerebral
stroke prediction and bankruptcy risk in financial data.
By evaluating the performance of various machine learning
algorithms,
the research underscores the limitations of
traditional resampling methods like SMOTE in clinical
contexts. It highlights the critical role of understanding
dataset characteristics, as these factors greatly impact the
effectiveness of predictive models [56].

3) REAL-WORLD APPLICATIONS OF HYBRID APPROACHES
Hybrid approaches have effectively addressed class imbal-
ance across various real-world domains. Enhancing model
performance and reliability has become essential in critical
fields such as healthcare, fraud detection, cybersecurity,
materials science,
telecommunications, and others. Each
application utilizes hybrid techniques to tackle the unique
challenges posed by imbalanced datasets, improving pre-
dictive accuracy and decision-making capabilities. Table 4
shows the applications and datasets used in each study
discussed.

In healthcare, techniques such as D-SMOTE and BP-
SMOTE with Stacked CNN and RNN enhance predictive
analytics for the early diagnosis of critical conditions like

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

cardiovascular diseases and breast cancer [4]. Similarly, E-
GAN improves disease detection accuracy for conditions
such as breast cancer, diabetes, and chronic kidney disease
by addressing imbalanced datasets effectively [11]. The DB-
SLSMOTE with Random Forest method proves particularly
valuable in detecting rare diseases by enhancing classification
accuracy in datasets with limited positive cases [51]. DCGAN
and CNN generate synthetic samples for medical imaging to
mitigate class imbalances, supporting the accurate diagnosis
of diseases like malaria [53]. Additionally, the integrated
approach of SMOTE, Undersampling, PSO, and MetaCost
optimizes the classification of underrepresented medical data,
aiding healthcare professionals in making more informed
decisions [54].

Fraud detection leverages methods like DB-SLSMOTE
with Random Forest, enhancing models’ reliability for
identifying fraudulent financial transactions [51]. The Tomek
Links + BIRCH Clustering + Borderline SMOTE technique
further improves fraud detection accuracy by addressing
imbalances in transaction datasets [7]. Additionally,
the
ATOMIC Method automates the creation of machine learning
solutions designed for imbalanced data, facilitating the
detection of fraudulent activities in financial systems [55].

In cybersecurity, Transfer Learning with Domain Adap-
tation using MMD is utilized to enhance the detection of
Return-Oriented Programming (ROP) attacks, a complex
exploit
technique [47]. This approach leverages transfer
learning to address dataset imbalances, improving the accu-
racy and reliability of deep learning models for identifying
such attacks.

In materials science, the GAN-Based Data Augmentation
Method tackles the classification of material phases in
imbalanced spectral datasets. Generating synthetic samples
supports experimental design and materials characterization,
as demonstrated in case studies involving hydrogels such as
Pluronic F-127 and Alpha-Cyclodextrin [46].

In automated text classification, the Tomek Links Before
MCNN-LSTM method categorizes news articles into diverse
topics such as Politics, Sports, and Lifestyle [52]. This
approach enhances content organization and retrieval for
media organizations, ensuring improved representation and
handling of underrepresented categories.

For telecommunications,

the Genetic Algorithm with
SVM improves user classification in systems such as
Non-Orthogonal Multiple Access
(NOMA) networks.
By addressing class imbalances,
this method ensures
efficient resource allocation and optimized communication
management [48].

The ATOMIC Method is applicable across various
domains, such as anomaly detection, healthcare diagnostics,
fraud detection, and credit scoring. Automating model opti-
mization for imbalanced data simplifies analytical processes,
enhancing decision-making and resource allocation in these
critical areas [55].

The study presenting a Hybrid Ensemble focuses on
cerebral stroke prediction by enhancing the reliability of

13694

VOLUME 13, 2025

---

<!-- PAGE 10 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

machine learning models and assessing the effectiveness of
SMOTE in clinical datasets [56].

V. DISCUSSION OF THE LIMITATIONS
This section provides a justification for the limitations of each
technique. Data-level, the (SMOTE-Tomek and SMOTE-
ENN)
these techniques face difficulties with datasets
featuring high-class overlap or noise. SMOTE-generated
synthetic samples may resemble the majority of instances,
causing classifier confusion. Additionally, cleaning methods
can unintentionally remove valuable minority samples or
miss noisy majority instances, reducing effectiveness [26].
Distance-based SMOTE (D-SMOTE) requires high computa-
tional resources for distance calculations in high-dimensional
spaces, leading to longer processing times. The ‘‘curse of
dimensionality’’ in such datasets can diminish the relevance
of distance metrics, affecting synthetic sample quality and
efficiency [4]. Bi-Phasic SMOTE (BP-SMOTE), its iterative
process, with multiple SMOTE applications and instance
selection phases, can be resource-intensive. As dataset size
grows, processing time and resource demands increase,
reducing scalability for real-world applications [4]. Class-
decomposition SMOTE (CD-SMOTE) effectiveness relies on
accurately decomposing the majority class into subclasses.
Inaccurate decomposition can produce poorly defined sub-
classes, diminishing the impact of oversampling and poten-
tially biasing the model toward the majority class [27].
Radius-SMOTE (R-SMOTE) performance depends heavily
on correctly tuning parameters like radius distance for
defining boundaries in synthetic sample generation. Poor
tuning can cause excessive overlap with majority samples
or inadequate minority sample generation. Additionally,
dataset size and complexity increase computational costs,
limiting scalability [28]. Self-Inspected Adaptive SMOTE
(SASMOTE) requires precise hyperparameter tuning for
optimal results. Its design for specific case studies limits
generalizability across healthcare applications, suggesting a
need for adaptation to broader contexts [29]. (Borderline-
SMOTE) generates synthetic samples near decision bound-
aries, which may overlap with the majority class, creating
ambiguous regions. This overlap can confuse the classifier
and reduce generalization performance, particularly with
poorly separated classes [30]. Oriented Oversampling with
Spatial Information (OOSI) may face runtime challenges on
complex datasets due to high dimensionality and intricate
distributions. Adaptive spatial partitioning requires intensive
computation, affecting scalability and efficiency, especially
with noisy datasets [31]. SMOTE with Tomek Links +
Borderline SMOTE (SDWBOTE) If temporal dependencies
between samples aren’t accurately captured, SDWBOTE may
carry over noise and bias from the original dataset, potentially
resulting in poor real-world classifier performance and
misrepresentation of minority classes [8]. (GAN-Based Data
Augmentation) demands substantial computational resources
for training due to the complexity of adversarial optimization
between the generator and discriminator. Additionally, GANs

are susceptible to mode collapse, where the generator fails
to cover the entire data space, limiting sample diversity and
quality of augmentation [6]. The limitations of (ABM) are
summarized in the risk of traditional under-sampling leading
to the loss of valuable minority class information and the
reliance on validation with a single dataset, which restricts
its generalizability to diverse clinical scenarios [32].

Algorithm-level, in (SVM with Multiple Kernel Learning
(MKL)) optimizing multiple kernel
functions increases
computational demands, potentially limiting scalability in
real-time applications. Extensive parameter tuning is also
needed for optimal results, which can be time-consuming
and may reduce model interpretability—a key factor in fields
like healthcare [38]. (AdaBoost) emphasis on misclassified
instances can make it highly sensitive to noisy data, increas-
ing the risk of overfitting. The algorithm may over-focus on
these points in the presence of outliers or noise, reducing its
ability to generalize effectively to unseen data [42]. (Bagging)
is computationally intensive, as it trains multiple models for
each bootstrap sample. Additionally, it may not adequately
address class imbalance on its own, as bootstrap sampling
imbalance, resulting in poor
can maintain the original
performance on minority classes [43]. (Random Forests) may
show bias toward the majority class in imbalanced datasets,
as training often prioritizes majority class accuracy. The
model also requires careful hyperparameter tuning to prevent
increased bias or overfitting, making balanced performance
across classes challenging to achieve [44]. In (Gradient
Boosting) Decision Trees (GBDT) with additional trees,
GBDT can become overly fitted to the training data, capturing
noise and outliers instead of actual patterns, which leads
to overfitting. Effective regularization is crucial to prevent
performance loss on unseen data [45]. (Stacked Deep
Learning) models are complex due to the integration of
multiple architectures, raising the risk of overfitting. This
complexity may lead the model to capture noise instead of
general patterns, resulting in poor generalization, particularly
with smaller or less diverse datasets [4].

Hybrid-level,

in (D-SMOTE and BP-SMOTE with
Stacked CNN and RNN),
the complexity of combining
multiple deep learning architectures increases the risk of
overfitting, complicating generalization. Additionally, inter-
pretability is reduced, making it challenging to understand
model decisions, especially in sensitive fields like health-
care [4]. (E-GAN with CNN) combined GAN and CNN
model demands substantial computational resources and
time, particularly for large datasets. Additionally, synthetic
samples may lead to overfitting if they do not accurately
reflect the minority class distribution [11]. (DB-SLSMOTE
with Random Forest) generating synthetic samples can add
to training complexity and the risk of overfitting, with
Random Forest training being especially resource-intensive
for large datasets [51]. (Tomek-Links Before MCNN-LSTM)
the model’s dependence on a specific dataset (Indonesian
news) limits its generalizability, and the lack of transfer
learning prevents it from utilizing larger datasets to enhance

VOLUME 13, 2025

13695

---

<!-- PAGE 11 -->

TABLE 4. Applications of hybrid approaches.

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

performance [52]. (DCGAN and CNN) requires substantial
computational resources for adversarial training, and syn-
thetic samples may lead to overfitting, affecting the model’s
generalization on unseen data [53]. (SMOTE + US + PSO +
MetaCost) concentrating on specific methods may restrict
broader insights into alternative approaches. Furthermore,
conclusions may lack generalizability if datasets do not
include diverse medical characteristics [54]. (Tomek Links +
BIRCH Clustering + Borderline SMOTE) the approach’s
complexity and parameter sensitivity necessitates careful
tuning, and its sensitivity to noise may leave residual noise,
impacting model accuracy [7]. ATOMIC Method (Meta-
Learning) ATOMIC’s handling of imbalanced data could
be enhanced by a broader exploration of hyperparameters
and algorithms, improving its performance and adaptability
across different datasets [55]. (Genetic Algorithm with
SVM) the iterative nature of Genetic Algorithms results
in high computational costs and a risk of overfitting if
hyperparameters, such as population size and mutation rate,
are not carefully optimized [48]. (Transfer Learning and
MMD) the high-quality source data is crucial for transfer
learning, and limited validation data can reduce detection
effectiveness. Careful model selection is essential to ensure
consistent results [47]. (GAN-based Data Augmentation with
Joint Optimization) is computationally intensive due to the
dual optimization between the generator and classifier, and
it struggles with high phase similarity, which limits distinct
sample generation and effective class separation [46]. In the
(Hybrid Ensemble) approach, classifiers face challenges in
accurately predicting minority classes in medical datasets,
and SMOTE’s theoretical validation may fail to align with
real-world clinical applications [56].

VI. EVALUATION METHODS
When handling imbalanced datasets in machine learning,
choosing the appropriate evaluation metrics is crucial for
precisely assessing model performance. This section explores
various evaluation techniques particularly beneficial for
addressing imbalanced data. It highlights the advantages of
each method and its effectiveness in evaluating the model’s
performance, particularly concerning accurately predicting
outcomes for the minority class.

Accuracy is a fundamental assessment criterion utilized in
machine learning and data mining. However, accuracy can
result in misaddressing if used with an unbalanced dataset.
A model may still achieve high overall accuracy even if its
classification performance for minority categories is poor
as long as it performs well in the majority categories. For
example, if 99% of the testing data are negative samples,
we can get a 99% accuracy by simply classifying all the
testing data as a negative sample. So, the accuracy cannot
be chosen as an evaluation index in imbalanced learning.
The evaluation indicators relating to imbalanced learning are
shown in Table 5.

In Table 5, most evaluation metrics are derived from the
confusion matrix (CM), a critical tool for visually represent-
ing an algorithm’s performance. It’s particularly critical when
dealing with imbalanced datasets as it delineates the count
of accurate and inaccurate predictions for each class. This
detailed breakdown is crucial for understanding the model’s
effectiveness across the predominant and underrepresented
classes. The main components of the confusion matrix
are:

• (TP) True Positives: Accurately identified positive

observation.

13696

VOLUME 13, 2025

---

<!-- PAGE 12 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

TABLE 5. Evaluation metrics for imbalance classification.

• (TN)True Negatives: Accurately identified negative

observation.

• (FP) False Positives: Incorrectly identified as positive.
• (FN) False Negatives: Incorrectly identified as negative.
Metrics like AUC and G-mean are commonly used because
they remain unaffected by class distribution imbalances. AUC
is based on the entire ROC curve, while G-mean incorporates
different parts of the confusion matrix, ensuring a more
balanced model performance evaluation. This makes them
suitable for dealing with situations where there are large
differences in the number of positive and negative class
samples. The Receiver Operating Characteristic curve and
the Area Under the Curve are valuable for assessing the
quality of classifier outputs. These metrics are particularly
adept at evaluating performance across different threshold
settings, offering robustness against class imbalance. The
AUC condenses the ROC curve’s insights into a single value,
expressing the likelihood that a classifier will prioritize a
randomly chosen positive instance over a negative one. The
ROC curve graphs TPR (TruePositive Rate) against FPR
(False Positive Rate) across different threshold configura-
tions. AUC is the area under the ROC curve. The Geometric
Mean computed by extracting the square root of (Recall
and Specificity) product guarantees that enhancements in
one class’s efficiency do not adversely impact the other.
This balance is crucial for effectively evaluating models

where it is essential not to overlook the minority class,
which is often of higher interest in imbalanced datasets.
For multiclass imbalance problems, the G-mean evaluation
metric is often preferred as it offers a unified measurement
approach, eliminating the need to assess each class separately.
And for highly imbalanced Big Data, the Area under the
Precision-Recall Curve (AUPRC) is a more effective metric
for evaluating the performance of classifiers. In highly
imbalanced Big Data,
the AUC metric fails to capture
information about precision scores and false positive counts
that the AUPRC metric reveals. The F1 Score denotes the
harmonic mean of precision and recall, which is valuable
in situations requiring a balance between the two and is
common in datasets with imbalanced class distributions. The
F1 Score provides more context than accuracy in situations
with uneven class distribution. In the formulas for AUC and
F1-score, Precision denotes accuracy [57], [58].

Considering these evaluation methods ensures a thorough
understanding of a model’s performance on imbalanced
datasets, guiding the development of efficient and equitable
models.

VII. CONCLUSION
This paper highlights the crucial importance of addressing
class imbalance in machine learning initiatives. It begins by
discussing basic strategies for balancing class distribution,

VOLUME 13, 2025

13697

---

<!-- PAGE 13 -->

which paves the way for a comprehensive exploration
of techniques categorized into data-level, algorithm-level,
or hybrid strategies. Additionally, this work examines the
limitations inherent
in each technique, providing justifi-
cations for their shortcomings, to offer a nuanced under-
standing of their practical challenges and opportunities for
improvement.Subsequently, it underscores the importance
of evaluation methods in assessing the efficacy of these
strategies under imbalanced data conditions, examining
metrics like F1 Score, AUC, and G-mean, among others.
These metrics are vital for evaluating how various techniques
fare, especially in accurately predicting outcomes for the
minority class.

Recent studies have identified several gaps in address-
ing imbalanced data across data-centric, algorithmic, and
blended approaches. At the data level, there is a pressing need
for scalable techniques that can manage large imbalanced
datasets and maintain their effectiveness across differ-
ent domains. Algorithm-level challenges revolve around
strengthening the resilience of methods against the evolving
threats inherent in imbalanced data scenarios. Meanwhile,
hybrid approaches face scalability, generalizability, and
robustness issues, highlighting the necessity for methods that
can effectively scale, function across diverse settings, and
resist evolving threats in imbalanced data contexts.

These challenges underline the continuous push to develop
more effective and flexible imbalanced data classification
methods. Moreover, the balance between model complexity
and generalization remains a significant hurdle, emphasizing
the need for ongoing research. Understanding the strengths
and limitations of each approach, including essential evalua-
tion methods, equips researchers to develop machine-learning
models that are effective, robust, and ready for real-world
application. These models are purposefully crafted to manage
the intricacies linked with data imbalance adeptly.

REFERENCES
[1] S. Haykin, Neural Networks: A Comprehensive Foundation.

Upper Saddle River, NJ, USA: Prentice-Hall, 1998.

[2] S.-M. Chen, Data Science and Big Data: An Environment of Computa-

tional Intelligence. Cham, Switzerland: Springer, 2017.

[3] J. L. Leevy, T. M. Khoshgoftaar, R. A. Bauder, and N. Seliya, ‘‘A survey
on addressing high-class imbalance in big data,’’ J. Big Data, vol. 5, no. 1,
pp. 1–30, Dec. 2018.

[4] A. M. Sowjanya and O. Mrudula, ‘‘Effective treatment of imbalanced
datasets in health care using modified SMOTE coupled with stacked deep
learning algorithms,’’ Appl. Nanoscience, vol. 13, no. 3, pp. 1829–1840,
Feb. 2022.

[5] M. M. Chowdhury, R. S. Ayon, and M. S. Hossain, ‘‘An investigation
of machine learning algorithms and data augmentation techniques for
diabetes diagnosis using class imbalanced BRFSS dataset,’’ Healthcare
Anal., vol. 5, Jun. 2024, Art. no. 100297.

[6] Q. Su, H. N. A. Hamed, M. A. Isa, X. Hao, and X. Dai, ‘‘A GAN-
based data augmentation method for imbalanced multi-class skin lesion
classification,’’ IEEE Access, vol. 12, pp. 16498–16513, 2024.

[7] M. Alamri and M. Ykhlef, ‘‘Hybrid undersampling and oversampling
for handling imbalanced credit card data,’’ IEEE Access, vol. 12,
pp. 14050–14060, 2024.

[8] N. Jiang and N. Li, ‘‘A wind turbine frequent principal fault detection and
localization approach with imbalanced data using an improved synthetic
oversampling technique,’’ Int. J. Electr. Power Energy Syst., vol. 126,
Mar. 2021, Art. no. 106595.

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

[9] J. Sadaiyandi, P. Arumugam, A. K. Sangaiah, and C. Zhang, ‘‘Strat-
ified sampling-based deep learning approach to increase prediction
accuracy of unbalanced dataset,’’ Electronics, vol. 12, no. 21, p. 4423,
Oct. 2023.

[10] S. Briechle, P. Krzystek, and G. Vosselman, ‘‘Silvi-net—A dual-CNN
approach for combined classification of tree species and standing dead
trees from remote sensing data,’’ Int. J. Appl. Earth Observ. Geoinf.,
vol. 98, Jun. 2021, Art. no. 102292.

[11] T. Suresh, Z. Brijet, and T. D. Subha, ‘‘Imbalanced medical disease dataset
classification using enhanced generative adversarial network,’’ Comput.
Methods Biomechanics Biomed. Eng., vol. 26, no. 14, pp. 1702–1718,
Oct. 2023.

[12] G. Y. Wong, F. H. F. Leung, and S.-H. Ling, ‘‘A novel evolutionary
preprocessing method based on over-sampling and under-sampling for
imbalanced datasets,’’ in Proc. 39th Annu. Conf. IEEE Ind. Electron. Soc.
(IECON), Nov. 2013, pp. 2354–2359.

[13] E. Troullinou, G. Tsagkatakis, A. Losonczy, P. Poirazi, and P. Tsakalides,
‘‘A generative neighborhood-based deep autoencoder for robust imbal-
anced classification,’’ IEEE Trans. Artif. Intell., vol. 5, no. 1, pp. 80–91,
Jan. 2024.

[14] M. Koziarski, M. Woźniak, and B. Krawczyk, ‘‘Combined cleaning and
resampling algorithm for multi-class imbalanced data with label noise,’’
Knowl.-Based Syst., vol. 204, Sep. 2020, Art. no. 106223.

[15] A. Singh, R. K. Ranjan, and A. Tiwari, ‘‘Credit card fraud detection
under extreme imbalanced data: A comparative study of data-level
algorithms,’’ J. Exp. Theor. Artif. Intell., vol. 34, no. 4, pp. 571–598,
Jul. 2022.

[16] H. Wasswa, T. Lynar, and H. Abbass, ‘‘Enhancing IoT-botnet detection
using variational auto-encoder and cost-sensitive learning: A deep learning
approach for imbalanced datasets,’’ in Proc. IEEE Region 10 Symp.
(TENSYMP), Sep. 2023, pp. 1–6.

[17] P. Kaur and A. Gosain, ‘‘Comparing the behavior of oversampling and
undersampling approach of class imbalance learning by combining class
imbalance problem with noise,’’ in Proc. ICT Based Innov. CSI. Cham,
Switzerland: Springer, Sep. 2017, pp. 23–30.

[18] D. Elreedy, A. F. Atiya, and F. Kamalov, ‘‘A theoretical distribution
analysis of synthetic minority oversampling technique (SMOTE) for
imbalanced learning,’’ Mach. Learn., vol. 113, no. 7, pp. 4903–4923,
Jul. 2024.

[19] S. Mundra, S. Vijay, A. Mundra, P. Gupta, M. K. Goyal, M. Kaur,
S. Khaitan, and A. K. Rajpoot, ‘‘Classification of imbalanced medical data:
An empirical study of machine learning approaches,’’ J. Intell. Fuzzy Syst.,
vol. 43, no. 2, pp. 1933–1946, Jun. 2022.

[20] T. Wongvorachan, S. He, and O. Bulut, ‘‘A comparison of undersampling,
oversampling, and SMOTE methods for dealing with imbalanced classi-
fication in educational data mining,’’ Information, vol. 14, no. 1, p. 54,
Jan. 2023.

[21] R. Malhotra and K. Lata, ‘‘An empirical study on predictability of software
maintainability using imbalanced data,’’ Softw. Quality J., vol. 28, no. 4,
pp. 1581–1614, Dec. 2020.

[22] M. Khushi, K. Shaukat, T. M. Alam, I. A. Hameed, S. Uddin, S. Luo,
X. Yang, and M. C. Reyes, ‘‘A comparative performance analysis of data
resampling methods on imbalance medical data,’’ IEEE Access, vol. 9,
pp. 109960–109975, 2021.

[23] K. M. Hasib, M. S. Iqbal, F. M. Shah, J. A. Mahmud, M. H. Popel,
M. I. H. Showrov, S. Ahmed, and O. Rahman, ‘‘A survey of methods
for managing the classification and solution of data imbalance problem,’’
2020, arXiv:2012.11870.

J. A. S. Aranda, R. dos Santos Costa,
[24] V. W. de Vargas,
P. R. da Silva Pereira,
‘‘Imbalanced data
and J. L. V. Barbosa,
preprocessing techniques for machine learning: A systematic mapping
study,’’ Knowl. Inf. Syst., vol. 65, no. 1, pp. 31–57, Jan. 2023.

[25] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer, ‘‘SMOTE:
Synthetic minority over-sampling technique,’’ J. Artif. Intell. Res., vol. 16,
pp. 321–357, Jun. 2002.

[26] G. E. A. P. A. Batista, R. C. Prati, and M. C. Monard, ‘‘A study of
the behavior of several methods for balancing machine learning training
data,’’ ACM SIGKDD Explorations Newslett., vol. 6, no. 1, pp. 20–29,
Jun. 2004.

[27] E. Elyan, C. F. Moreno-Garcia, and C. Jayne, ‘‘CDSMOTE: Class
decomposition and synthetic minority class oversampling technique for
imbalanced-data classification,’’ Neural Comput. Appl., vol. 33, no. 7,
pp. 2839–2851, Apr. 2021.

13698

VOLUME 13, 2025

---

<!-- PAGE 14 -->

M. Altalhan et al.: Imbalanced Data Problem in Machine Learning: A Review

[28] G. A. Pradipta, R. Wardoyo, A. Musdholifah, and I. N. H. Sanjaya,
‘‘Radius-SMOTE: A new oversampling technique of minority samples
based on radius distance for learning from imbalanced data,’’ IEEE Access,
vol. 9, pp. 74763–74777, 2021.

[29] T. Kosolwattana, C. Liu, R. Hu, S. Han, H. Chen, and Y. Lin, ‘‘A self-
inspected adaptive SMOTE algorithm (SASMOTE) for highly imbalanced
data classification in healthcare,’’ BioData Mining, vol. 16, no. 1, p. 15,
Apr. 2023.

[30] F. de la Bourdonnaye and F. Daniel, ‘‘Evaluating resampling methods on
a real-life highly imbalanced online credit card payments dataset,’’ 2022,
arXiv:2206.13152.

[31] Y. Deng and M. Li, ‘‘An adaptive and robust method for oriented
oversampling with spatial information for imbalanced noisy datasets,’’
IEEE Access, vol. 11, pp. 122610–122624, 2023.

[32] H. Zhang, H. Zhang, S. Pirbhulal, W. Wu, and V. H. C. D. Albuquerque,
‘‘Active balancing mechanism for imbalanced medical data in deep
learning–based classification models,’’ ACM Trans. Multimedia Comput.,
Commun., Appl., vol. 16, no. 1s, pp. 1–15, Jan. 2020.

[33] S. Ayoub, Y. Gulzar, J. Rustamov, A. Jabbari, F. A. Reegu, and S. Turaev,
‘‘Adversarial approaches to tackle imbalanced data in machine learning,’’
Sustainability, vol. 15, no. 9, p. 7097, Apr. 2023.

[34] J. Zheng, X. Wang, D. Wei, B. Chen, and Y. Shao, ‘‘A novel imbalanced
ensemble learning in software defect predication,’’ IEEE Access, vol. 9,
pp. 86855–86868, 2021.

[35] S. H. Khan, M. Hayat, M. Bennamoun, F. A. Sohel, and R. Togneri, ‘‘Cost-
sensitive learning of deep feature representations from imbalanced data,’’
IEEE Trans. Neural Netw. Learn. Syst., vol. 29, no. 8, pp. 3573–3587,
Aug. 2018.

[36] P. Domingos, ‘‘MetaCost: A general method for making classifiers cost-
sensitive,’’ in Proc. 5th ACM SIGKDD Int. Conf. Knowl. Discovery Data
Mining, Aug. 1999, pp. 155–164.

[37] Z. Ren, Y. Zhu, W. Kang, H. Fu, Q. Niu, D. Gao, K. Yan, and
J. Hong, ‘‘Adaptive cost-sensitive learning: Improving the convergence of
intelligent diagnosis models under imbalanced data,’’ Knowl.-Based Syst.,
vol. 241, Apr. 2022, Art. no. 108296.

[38] S. Saeed and H. C. Ong, ‘‘Performance of SVM with multiple kernel
learning for classification tasks of imbalanced datasets,’’ Pertanika J. Sci.
Technol., vol. 27, no. 1, pp. 527–545, 2019.

[39] L. Gao, L. Zhang, C. Liu, and S. Wu, ‘‘Handling imbalanced medical
image data: A deep-learning-based one-class classification approach,’’
Artif. Intell. Med., vol. 108, Aug. 2020, Art. no. 101935.

[40] J. Luo, Y. Yuan, and S. Xu, ‘‘Improving GBDT performance on imbalanced
datasets: An empirical study of class-balanced loss functions,’’ 2024,
arXiv:2407.14381.

[41] R. Mary Mathew and R. Gunasundari, ‘‘A review on handling multiclass
imbalanced data classification in education domain,’’ in Proc. Int.
Conf. Advance Comput. Innov. Technol. Eng. (ICACITE), Mar. 2021,
pp. 752–755.

[42] R. E. Schapire, ‘‘A brief introduction to boosting,’’ IJCAI, vol. 99, no. 999,

pp. 1401–1406, 1999.

[43] L. Breiman,

‘‘Bagging predictors,’’ Mach. Learn., vol. 24, no. 2,

pp. 123–140, Aug. 1996.

[44] L. Breiman, ‘‘Random forests,’’ Mach. Learn., vol. 45, pp. 5–32, Jan. 2001.
[45] P. Sheng, L. Chen, and J. Tian, ‘‘Learning-based road crack detection using
gradient boost decision tree,’’ in Proc. 13th IEEE Conf. Ind. Electron. Appl.
(ICIEA), May 2018, pp. 1228–1232.

[46] J. Chung, J. Zhang, A. I. Saimon, Y. Liu, B. N. Johnson, and Z. Kong,
‘‘Imbalanced spectral data analysis using data augmentation based on
the generative adversarial network,’’ Sci. Rep., vol. 14, no. 1, p. 13230,
Jun. 2024.

[47] H. Wang, A. Singhal, and P. Liu,

‘‘Tackling imbalanced data in
cybersecurity with transfer learning: A case with ROP payload detection,’’
Cybersecurity, vol. 6, no. 1, p. 2, Jan. 2023.

[48] H. Shamsudin, U. K. Yusof, Y. Haijie, and I. S. Isa, ‘‘An optimized support
vector machine with genetic algorithm for imbalanced data classification,’’
Jurnal Teknologi, vol. 85, no. 4, pp. 67–74, Jun. 2023.

[49] N. V. Chawla, A. Lazarević, L. Hall, and K. W. Bowyer, ‘‘SMOTEBoost:
Improving prediction of the minority class in boosting,’’ in Proc. 7th Eur.
Conf. Knowl. Discovery Databases, Cavtat-Dubrovnik, Croatia. Cham,
Switzerland: Springer, Jan. 2003, pp. 107–119.

[50] C. Seiffert, T. M. Khoshgoftaar, J. Van Hulse, and A. Napolitano,
‘‘RUSBoost: A hybrid approach to alleviating class imbalance,’’ IEEE
Trans. Syst., Man, Cybern., A, Syst. Hum., vol. 40, no. 1, pp. 185–197,
Jan. 2010.

[51] Q. Han, R. Yang, Z. Wan, S. Chen, M. Huang, and H. Wen, ‘‘Imbalanced
data classification based on DB-SLSMOTE and random forest,’’ in Proc.
Chin. Autom. Congr. (CAC), Nov. 2020, pp. 6271–6276.

[52] K. M. Hasib, S. Azam, A. Karim, A. A. Marouf, F. M. J. M. Shamrat,
S. Montaha, K. C. Yeo, M. Jonkman, R. Alhajj, and J. G. Rokne,
‘‘MCNN-LSTM: Combining CNN and LSTM to classify multi-class text
in imbalanced news data,’’ IEEE Access, vol. 11, pp. 93048–93063, 2023.
[53] L. M. Shoohi and J. H. Saud, ‘‘DCGAN for handling imbalanced malaria
dataset based on over-sampling technique and using CNN,’’ Medico-Legal
Update, vol. 20, no. 1, pp. 1079–1085, Apr. 2020.

[54] Y.-C. Wang and C.-H. Cheng, ‘‘A multiple combined method for
rebalancing medical data with class imbalances,’’ Comput. Biol. Med.,
vol. 134, Jul. 2021, Art. no. 104527.

[55] N. Moniz and V. Cerqueira, ‘‘Automated imbalanced classification via
meta-learning,’’ Expert Syst. Appl., vol. 178, Sep. 2021, Art. no. 115011.
[56] S. Gholampour, ‘‘Impact of nature of medical data on machine and
deep learning for imbalanced datasets: Clinical validity of SMOTE is
questionable,’’ Mach. Learn. Knowl. Extraction, vol. 6, no. 2, pp. 827–841,
Apr. 2024.

[57] S. Riyanto, I. S. Sitanggang, T. Djatna, and T. D. Atikah, ‘‘Comparative
analysis using various performance metrics in imbalanced data for multi-
class text classification,’’ Int. J. Adv. Comput. Sci. Appl., vol. 14, no. 6,
pp. 1–9, 2023.

[58] J. T. Hancock, T. M. Khoshgoftaar, and J. M. Johnson, ‘‘Evaluating
classifier performance with highly imbalanced big data,’’ J. Big Data,
vol. 10, no. 1, p. 42, Apr. 2023.

MANAHEL ALTALHAN received the bachelor’s degree from King Khalid
University (KKU), Abha, Saudi Arabia, in 2022, where she is currently
pursuing the master’s degree in computer science. She was a Cooperator
with the KKU Computer Science Department,
in 2023. Her research
interests include artificial intelligence, data mining, and machine learning,
particularly focusing on handling imbalanced data.

ABDULMOHSEN ALGARNI received the Ph.D.
degree from Queensland University of Technol-
ogy, Australia, in 2012. He was a Research Asso-
ciate with the School of Electrical Engineering
and Computer Science, Queensland University of
Technology, in 2012. He is currently an Associate
Professor with the College of Computer Science,
King Khalid University. His research interests
include artificial intelligence, data mining, text
mining, machine learning, information retrieval,
and information filtering.

MONIA TURKI-HADJ ALOUANE (Member,
IEEE) received the Ph.D. (Diploma) degree in
electrical engineering and the National Tenure
Diploma degree in telecommunications from the
National Engineering School of Tunis (ENIT),
in 1997 and June 2007, respectively. She is
currently a Professor with the College of Computer
Science, King Khalid University, Saudi Arabia.
In September 1997, she was recruited as an Assis-
tant Professor of electrical engineering with ENIT,
where she was promoted to an Associate Professor of telecommunications,
in December 2007. From 2010 to 2012, she was a Visiting Associate
Professor with the Electricity Department, Polytechnic School of Tunisia
(EPT). Since 2012, she has been a Full Professor of telecommunications
with the Information and Communication Technologies (ICT) Department,
ENIT. She has coordinated internationally sponsored research projects. Since
1997, she has been leading more than 20 research master’s theses and eight
Ph.D. theses. She has published more than 70 papers in impacted journals and
conferences. Her research interests include signal processing (speech, image,
and video), machine learning, deep learning, and evolutionary algorithms.

VOLUME 13, 2025

13699

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received24December2024,accepted10January2025,dateofpublication20January2025,dateofcurrentversion23January2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3531662
Imbalanced Data Problem in Machine Learning:
A Review
MANAHELALTALHAN ,ABDULMOHSENALGARNI ,
ANDMONIATURKI-HADJALOUANE ,(Member,IEEE)
DepartmentofComputerScience,KingKhalidUniversity,Abha61421,SaudiArabia
Correspondingauthor:ManahelAltalhan(445816339@kku.edu.sa)
ThisworkwassupportedbytheDeanshipofResearchandGraduateStudies,KingKhalidUniversity,throughSmallGroupResearch
underGrantRGP1/71/45.
ABSTRACT Oneoftheprominentchallengesencounteredinreal-worlddataisanimbalance,characterized
byunequaldistributionofobservationsacrossdifferenttargetclasses,whichcomplicatesachievingaccurate
model classifications. This survey delves into various machine learning techniques developed to address
the difficulties posed by imbalanced data. It discusses data-level methods such as oversampling and
undersampling,algorithm-levelsolutionsincludingensemblelearningandspecificalgorithmadjustments,
cost-sensitive algorithms, and hybrid strategies that combine multiple approaches. Moreover, this paper
emphasizes the crucial role of evaluation methods like Precision, F1 Score, Recall, G-mean, and AUC in
measuring the effectiveness of these strategies under imbalanced conditions. A detailed review of recent
research articles helps pinpoint persistent gaps in generalizability, scalability, and robustness across these
methods, underscoring the necessity for ongoing improvements. The survey seeks to offer an extensive
overview of current approaches that improve the efficiency and effectiveness of machine learning models
dealingwithimbalanceddatasets,thusequippingresearcherswiththeinsightsneededtodeveloprobustand
effectivemodelsreadyforreal-worldapplication.
INDEXTERMS Imbalanceddata,machinelearning,balancetechniques,evaluationmethods.
I. INTRODUCTION todiscoverconstantlyoccurringinafewexamplescompared
Imbalanceddataposesamajorchallengeinmachinelearning. to all examples [2]. Imbalanced datasets present four key
This occurs when the class distribution within a dataset is challenges: bias, overlap, feature vector size, and dataset
uneven, resulting in what is referred to as imbalance [1]. size [4]. This scenario is prevalent across various domains
It means that one data class is significantly larger than suchashealthcarelikediabetesdiagnosis[5]andskinlesion
the others. Most instances are part of the dominant class classification [6], Finance like credit fraud detection [7],
(the negative or majority class), with only a small number Engineering like fault detection in wind turbines [8], and
represented in the other classes (the positive or minority recognitionrottingordeadtree[9],[10]andothers.
class) [2]. It causes a fundamental problem in machine The consequences of imbalanced data are far-reaching.
learning, as when classifiers are trained on this type of In situations such as medical diagnosis, where accurately
data in which the distribution is unbalanced, the classifier’s identifyingrarediseasesisvital,modelsthatfavorthemajor-
conduct becomes biased in favor of the dominant class, ityclassmayleadtooverlookeddiagnosesandcompromised
often overlooking the lesser class [3]. This results in patient care [11]. Similarly, in fraud detection, the machine
misclassifying instances within the minority class, which is learningmodeltendstoexhibitbiastowardsthepredominant
usuallyexceedinglycriticalduetotheaffectedparttheywant class, causing a decrease in True Positives (TP) and an
increase in False Positives (FP) [12], allowing fraudulent
The associate editor coordinating the review of this manuscript and activitiestogoundetected.Thus,addressingimbalanceddata
approvingitforpublicationwasSawyerDuaneCampbell . isimperativeforbuildingreliableandeffectiveMLsystems.
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
13686 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
Now, the importance and seriousness of this problem have II. REVIEWSTRATEGY
becomecleartous. This survey investigates the imbalanced data problem
Over the years, researchers have developed numerous in machine learning by reviewing studies from various
methodstocounteracttheeffectsofclassimbalance,encom- databases, including Google Scholar, IEEE, Springer,
passing three primary classifications: data-level techniques, Elsevier, MDPI, and others. Emphasis is placed on
algorithm-level techniques, and integrated methods [7], recent advancements, with most reviewed studies published
[13]. Data-level techniques involve modifying the dataset between 2020 and 2024, ensuring the latest methodologies
beforetheclassifieristrained,includingunder-samplingthe and insights are included. The search process utilized
dominant class, over-sampling the minor class, or creating specific keywords such as ‘‘imbalanced data,’’ ‘‘class
synthetic data [7], [14]. Conversely, algorithm-level tech- imbalance,’’ ‘‘machine learning,’’ ‘‘data-level techniques,’’
niquesmodifythelearningalgorithmstomanageimbalanced ‘‘algorithm-level solutions,’’ ‘‘oversampling,’’ ‘‘undersam-
data more efficiently without compromising the data itself, pling,’’ ‘‘SMOTE,’’ ‘‘cost-sensitive learning,’’ ‘‘Ensemble
often through cost-sensitive learning, ensemble methods, methods,’’and‘‘hybridapproaches.’’Thisreviewhasinves-
oralgorithm-specificadjustments[13]. tigated 40 studies, and most of the papers are from journals
Whiledata-levelandalgorithm-leveltechniquesoffervalu- ranked in Q1 and Q2 categories, ensuring high-quality and
ablestrategiesforaddressingimbalanceddata,theyeachhave impactful contributions. The selected references encompass
limitations. Data-level techniques may discard potentially foundationalapproaches,innovativetechniques,anddomain-
usefulinformationorintroducenoisethroughsyntheticdata specificsolutions,providingacomprehensiveanalysisofthe
generation[15].Algorithm-leveltechniques,whileeffective, field. This strategy offers a deep understanding of current
|         |       |         |               |     |         |     |         | approaches | to addressing |     | data | imbalance | challenges |     | while |
| ------- | ----- | ------- | ------------- | --- | ------- | --- | ------- | ---------- | ------------- | --- | ---- | --------- | ---------- | --- | ----- |
| may not | fully | exploit | the available |     | data or | may | require |            |               |     |      |           |            |     |       |
complexadjustmentsfordifferentalgorithms[13]. identifyingresearchgapsthatindirectlyilluminatepotential
Data-levelandalgorithm-leveltechniques[7],thesehybrid futuredirections.
approaches aim to leverage each category’s strengths while Thisreviewaimstoaddresskeyquestionsthatencompass
mitigating their weaknesses. Examples include combined all aspects of the imbalanced data problem in machine
learning:
| samplingtechniques, |               | algorithmicresamplingstrategies,and |           |                |     |         |       |            |           |     |                 |     |             |     |      |
| ------------------- | ------------- | ----------------------------------- | --------- | -------------- | --- | ------- | ----- | ---------- | --------- | --- | --------------- | --- | ----------- | --- | ---- |
| ensembles           | of resampled  |                                     | datasets. | Evaluation     |     | metrics | like  |            |           |     |                 |     |             |     |      |
|                     |               |                                     |           |                |     |         |       | 1- Q1: How | effective |     | are fundamental |     | approaches, |     | such |
| accuracy            | and precision |                                     | may       | not adequately |     | capture | model |            |           |     |                 |     |             |     |      |
asoversamplingandundersampling,inaddressingclass
| performance | in  | imbalanced |     | datasets. | Hence, | metrics | such |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --------- | ------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
imbalanceacrossapplications?
| as AUC | (area | under | the precision-recall |     | (PR) | curve) | and |     |     |     |     |     |     |     |     |
| ------ | ----- | ----- | -------------------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2- Q2:Whatarethefindingsandlimitationsofdata-level,
AUC(areaunderthereceiveroperatingcharacteristic(ROC)
|         |         |          |      |               |     |           |     | algorithm-level, |     | and | hybrid | techniques |     | in achieving |     |
| ------- | ------- | -------- | ---- | ------------- | --- | --------- | --- | ---------------- | --- | --- | ------ | ---------- | --- | ------------ | --- |
| curve), | and the | F1-score | have | been proposed |     | and shown | to  |                  |     |     |        |            |     |              |     |
classbalance?
| be effective  | in          | classifying | tasks | with imbalanced |     | data           | [16]. |            |     |       |             |       |     |         |         |
| ------------- | ----------- | ----------- | ----- | --------------- | --- | -------------- | ----- | ---------- | --- | ----- | ----------- | ----- | --- | ------- | ------- |
|               |             |             |       |                 |     |                |       | 3- Q3: How | do  | these | limitations | limit | the | overall | perfor- |
| Additionally, | researchers |             | have  | introduced      |     | class-weighted |       |            |     |       |             |       |     |         |         |
manceofthebalancingtechniques?
| evaluation | frameworks |     | that | accommodate | arbitrary |     | skews |     |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ---- | ----------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
4- Q4:Whichevaluationmetricsbestassessthesuccessof
| in class | cardinalities | and | importance, |     | effectively | addressing |     |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ----------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
balancingtechniquesinMLandDLtasks?
challengespresentedbyimbalanceddatasets.
Thefirstsectionofthereviewfocusesonansweringthe
| The        | subsequent | sections    |     | of the paper | will      | follow    | this |                 |        |           |            |              |                |        |       |
| ---------- | ---------- | ----------- | --- | ------------ | --------- | --------- | ---- | --------------- | ------ | --------- | ---------- | ------------ | -------------- | ------ | ----- |
|            |            |             |     |              |           |           |      | first question, |        | providing | a          | foundational | understanding. |        |       |
| structure. | Section    | II outlines |     | the review   | strategy, | including |      |                 |        |           |            |              |                |        |       |
|            |            |             |     |              |           |           |      | The             | second | section   | elaborates |              | on the         | second | ques- |
theresearchquestionsthatguidethesurvey.Next,SectionIII
|        |          |              |     |            |     |              |     | tion, | offering | detailed | insights. |     | The third | question | is  |
| ------ | -------- | ------------ | --- | ---------- | --- | ------------ | --- | ----- | -------- | -------- | --------- | --- | --------- | -------- | --- |
| delves | into the | foundational |     | techniques | of  | oversampling |     |       |          |          |           |     |           |          |     |
addressedbyanalyzingthelimitationsandshortcomings
| and undersampling, |      | providing  |     | an overview |             | of their | role in |            |             |     |     |           |        |       |         |
| ------------------ | ---- | ---------- | --- | ----------- | ----------- | -------- | ------- | ---------- | ----------- | --- | --- | --------- | ------ | ----- | ------- |
|                    |      |            |     |             |             |          |         | of various | techniques, |     | as  | discussed | in the | third | section |
| addressing         | data | imbalance. |     | Section     | IV explores |          | a broad |            |             |     |     |           |        |       |         |
ofthereview.Finally,thefourthpartprovidesaconcise
| spectrum                | of balance |     | strategies, | categorized |     | into | data- |           |          |     |        |                  |     |          |     |
| ----------------------- | ---------- | --- | ----------- | ----------- | --- | ---- | ----- | --------- | -------- | --- | ------ | ---------------- | --- | -------- | --- |
|                         |            |     |             |             |     |      |       | and clear | response |     | to the | fourth question, |     | wrapping | up  |
| level, algorithm-level, |            |     | and hybrid  | approaches, |     | with | each  |           |          |     |        |                  |     |          |     |
thereviewcomprehensively.
subsectiondetailingmethodstoenhancemodelperformance
| when dealing | with | imbalanced |     | datasets. | In  | Section | V, the |     |     |     |     |     |     |     |     |
| ------------ | ---- | ---------- | --- | --------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
limitations of each technique are discussed, along with III. FUNDAMENTALAPPROACHESTOCLASS
justifications for their inclusion. Following this, Section VI DISTRIBUTIONBALANCING
examinesvariousevaluationmethodsessentialforassessing Thissectiondelvesintothefundamentalmethodstomitigate
the effectiveness of models handling imbalanced data, class imbalance in ML: oversampling and undersampling,
highlighting metrics like F1 Score, AUC, and others to which the figure 1 shows. Class imbalance is critical
provideanuancedunderstandingofmodelefficacy.Finally, in predictive modeling, often resulting in biased model
|         |                 |     |       |          |          |              |     | outcomes | that favor | the | majority | class | disproportionately. |     |     |
| ------- | --------------- | --- | ----- | -------- | -------- | ------------ | --- | -------- | ---------- | --- | -------- | ----- | ------------------- | --- | --- |
| Section | VII synthesizes |     | these | insights | to offer | a conclusive |     |          |            |     |          |       |                     |     |     |
summaryofthecurrenttechniquesformanagingimbalanced Addressing this imbalance is essential to foster fair and
data in machine learning, pinpointing existing gaps in each precisemodels.Over/Undersamplingaretwokeytechniques
approach. that adjust the arrangement of classes in training datasets
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 13687 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
to create a more balanced environment for model training. Centroids,TomekLinks,orNearMissareutilizedtomaintain
A thorough exploration of these foundational techniques thestatisticalintegrityofthemajorityclasswhileminimizing
preparesthegroundworkfortheadvancedbalancingmethods itsquantity[19].Thesemethodsenhancemodelperformance
detailedinsubsequentsectionsofthissurvey. by eliminating instances that are either redundant or less
|     |     |     |     |     |     | informative, | thereby | creating |                 | a more balanced |        | dataset that  |
| --- | --- | --- | --- | --- | --- | ------------ | ------- | -------- | --------------- | --------------- | ------ | ------------- |
|     |     |     |     |     |     | stops the    | model   | from     | being dominated |                 | by the | traits of the |
predominantclass.
Advantages:
|     |     |     |     |     |     | • Significantly |     | reduces    | the | time required |             | for model |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --- | ------------- | ----------- | --------- |
|     |     |     |     |     |     | training        | by  | decreasing | the | dataset size, | simplifying | the       |
learningprocess.
|     |     |     |     |     |     | Reduces |     | the likelihood |     | of model | bias | toward the |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------------- | --- | -------- | ---- | ---------- |
•
|     |     |     |     |     |     | majority |     | class, promoting |     | more | fair and | balanced |
| --- | --- | --- | --- | --- | --- | -------- | --- | ---------------- | --- | ---- | -------- | -------- |
decision-making.
Disadvantages:
• Thereisadangeroflosingessentialdata,astheremoval
|     |     |     |     |     |     | process | may | inadvertently |     | discard | crucial | instances to |
| --- | --- | --- | --- | --- | --- | ------- | --- | ------------- | --- | ------- | ------- | ------------ |
FIGURE1. Basicapproachestoclassdistributionbalance.
understandthepredominantclasscomprehensively.
|     |     |     |     |     |     | • May | lead   | to underfitting, |     | especially | if        | the diver- |
| --- | --- | --- | --- | --- | --- | ----- | ------ | ---------------- | --- | ---------- | --------- | ---------- |
|     |     |     |     |     |     | sity  | within | the majority     |     | class is   | not fully | captured,  |
A. OVERSAMPLING
Oversampling targets enhancing the minority class’s rep- potentially impairing the model’s ability to generalize
resentation within a dataset, bringing its frequency up effectively.
| to parity with | the majority | class. | This | adjustment | can |     |     |     |     |     |     |     |
| -------------- | ------------ | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
be realized by simply duplicating existing instances or C. STRATEGICCONSIDERATIONSFORCHOOSING
creating new, synthetic ones through methodologies like BETWEENOVERSAMPLINGANDUNDERSAMPLING
SMOTE(SyntheticMinorityOversamplingTechnique)[17]. Choosingbetweenoversamplingandundersamplingrequires
SMOTEanditsderivatives,suchasBorderline-SMOTEand careful consideration of multiple aspects, such as dataset
ADASYN,synthesizenewsamplesbyinterpolatingbetween size, data characteristics, available computing resources,
minorityclassinstancesthatconnectvialinesegmentstotheir and the significance of minority class instances. Typically,
nearest neighbors within the same class. These approaches oversampling is preferred in scenarios where the minority
operate primarily in the feature space, thereby injecting a class includes critical, rare events that are essential to
higherdegreeofdiversityintothelesserclassandsupporting capture accurately, such as in fraud detection or diagnosing
themodel’scapabilitytogeneralizefromlimiteddata[18]. raremedicalconditions.Conversely,undersamplingisoften
Advantages: more advantageous for extremely large datasets, where
|             |             |                |     |           |           | reducing | the | volume | of data | can significantly |     | enhance |
| ----------- | ----------- | -------------- | --- | --------- | --------- | -------- | --- | ------ | ------- | ----------------- | --- | ------- |
| • Increases | the model’s | generalization |     | abilities | by intro- |          |     |        |         |                   |     |         |
ducingamorecomprehensiverangeofvariabilitywithin computational efficiency and where there is enough data
theminorityclass,thuspreparingthemodelforbroader redundancy to minimize the risk of losing important
| scenarios. |     |     |     |     |     | information[20]. |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
• Safeguards against the loss of essential information in Toachievethebestofbothworlds,hybridapproachesthat
|          |                  |       |     |              |          | merge elements |     | of both | oversampling |     | and undersampling |     |
| -------- | ---------------- | ----- | --- | ------------ | -------- | -------------- | --- | ------- | ------------ | --- | ----------------- | --- |
| minority | class instances, | which | is  | particularly | vital in |                |     |         |              |     |                   |     |
datasetswhereeachexampleholdssignificantvalue. are becoming more prevalent. Methods like SMOTEEN,
Disadvantages: combining SMOTE with Edited Nearest Neighbors, or var-
• There is a risk of overfitting, as models might begin iousensembletechniquesincorporatingdifferentresampling
to memorize the noise inherent in the synthetically strategies within a single classifier framework can provide
generated samples rather than learn to generalize from a more balanced dataset [21]. These hybrid methods help
theactualdata. ensure that models are not only efficient but also retain the
• Elevates the computational burden, especially when integrityanddiversityofdata,thusenhancingoverallmodel
employing sophisticated synthetic instance generation performance without sacrificing detail or computational
| techniques,whichcanberesource-intensive. |     |     |     |     |     | speed.                |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| B. UNDERSAMPLING                         |     |     |     |     |     | IV. BALANCETECHNIQUES |     |     |     |     |     |     |
Incontrasttooversampling,undersamplingaimstobalance Many dataset characteristics determine the most suitable
class allocation by reducing the size of the majority techniques for addressing imbalance (data-level, algorithm-
class, often achieved through the random deletion of its level, or hybrid). One key factor is the percentage of
|                 |              |            |     |      |            | imbalance, | which | varies | from | dataset to | dataset. | Knowing       |
| --------------- | ------------ | ---------- | --- | ---- | ---------- | ---------- | ----- | ------ | ---- | ---------- | -------- | ------------- |
| instances [17]. | More refined | techniques |     | such | as Cluster |            |       |        |      |            |          |               |
| 13688           |              |            |     |      |            |            |       |        |      |            |          | VOLUME13,2025 |

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
it gives a clear understanding of the distribution of classes Technique (RSMOTE) is unlike traditional SMOTE, which
in the dataset, whether high or moderate. The percentage connectsminoritysamplestocreatesyntheticinstancesalong
of imbalance is critical for effectively handling imbalanced line segments; it identifies the nearest samples from the
datasetsandbuildingreliableMLmodels. majorityclasswithinaspecifiedradiustogeneratesynthetic
datapoints,aidinginthecreationofmorediverseandrealistic
A. DATA-LEVELTECHNIQUES synthetic samples [28]. The SASMOTE (a self-inspected
Data level techniques focus on aligning class distributions adaptive SMOTE approach) overcomes traditional SMOTE
byadjustingthesizeoftrainingdatasetsthroughresampling, limitations by prioritizing visible neighbors and eliminating
have become widely adopted [22], which aims to equalize low-quality samples. Integrating adaptive nearest neighbor-
the class distribution through two methods: Undersampling hoodselectionandself-inspectionforuncertaintyevaluation
and Oversampling [23]. Although resampling directly bal- elevatesthequalityofresampleddata,particularlybeneficial
ances the training set, it introduces two main challenges: for highly imbalanced healthcare classification tasks [29].
oversampling may lead to overfitting and reduced gen- Borderline-SMOTE is a sampling technique employed in
eralization on the test set, whereas undersampling may managingimbalanceddatasets,particularlyinsituationssuch
result in a significant loss of knowledge from the majority as fraud detection in credit card transactions. It generates
class[13].StandardundersamplingmethodsincludeRandom syntheticsamplesfortheunderrepresentedclassbytargeting
Undersampling, Tomek Links, and Cluster Centroids [24]. instances close to the decision boundary between classes,
Typically, to prevent the substantial depletion of instances often known as borderline instances [30]. The Oriented
from the predominant class, oversampling techniques are Oversampling with Spatial Information Method (OOSI)
oftenpreferred[4].Prominentoversamplingmethodsinclude tackleschallengesinimbalancedandnoisydatasetsthrough
SMOTE, ADASYN (Adaptive Synthetic Sampling), and a robust and adaptive approach that includes three critical
Borderline-SMOTE[24]. phases:OrientedInformationSampling,SpatialInformation
SMOTE represents a commonly adopted oversampling Quantification, and Adaptive Data Space Partitioning [31].
method [25]. It identifies instances near within the feature The Synthetic and Dependent Wild Bootstrapped Oversam-
space, establishes connections between them, and generates pling Method (SDWBOTE) helps overcome the challenges
newsamplesalongthoseconnections.Nonetheless,generat- ofskeweddatainfaultdetectionandlocalizationtaskswithin
ing synthetic examples without accounting for the majority windturbinesystems.Itconsiderstemporaldependenciesand
classcancreateambiguousinstances,especiallywhenthere relationshipsamongsamples[8].
is significant overlap between classes, which is a notable GAN-based methods, leveraging Generative Adversarial
drawbackofthisapproach[13]. Networks(GANs)composedofageneratorandadiscrimina-
Many hybrid-sampling methods and SMOTE variants tor,aregainingtraction.Thesetechniquesgeneratesynthetic
shown in table 1 have been proposed to address these samples by understanding the inherent data distribution and
challenges. Modify SMOTE-N (Synthetic Minority Over- producing new samples that closely resemble actual data.
sampling Technique for nominal data) to suit the nominal For instance, the GAN-based Data Augmentation Method
attributesofthedata[25].SMOTEENN(combiningSMOTE- introducedby[6]seekstoimprovetheclassificationaccuracy
N with Edited Nearest Neighbors) aims to rectify class of imbalanced skin lesion datasets. Another study explores
imbalancebyoversamplingtheminorityclassandenhancing the(GANs)toaddresschallengesassociatedwithimbalanced
datasetqualitythroughtheeliminationofnoisysamples,and datasets in machine learning. Focusing on three real-world
SMOTE-Tomek(combiningSMOTE-NwithTomeklinks)to datasets—CarEvaluation,HumanActivityRecognition,and
simultaneously create synthetic samples for the lesser class Bankdatasets—theresearchaimstoenhanceminorityclass
and undersample the greater class, effectively rebalancing representation through data augmentation. The GAN-based
the dataset and improving classification outcomes [26]. approach generates synthetic data to balance the dataset,
Distance-basedSMOTE(D-SMOTE)regulatesclassoverlap improving classification accuracy and model performance.
throughadistanceparameter,creatingsyntheticsamplesthat This study underscores the potential of GANs as an
better represent the minority class. Bi-phasic SMOTE (BP- effective tool for data augmentation and boosting model
SMOTE),ontheotherhand,overcomestraditionalSMOTE’s robustness across diverse applications [33]. An innovative
shortcomings by enhancing the oversampling procedure Active Balancing Mechanism (ABM) is proposed to tackle
through instance selection, guaranteeing the inclusion of the challenges of imbalanced medical data, focusing on
only pertinent instances in the resultant training dataset [4]. myocardialinfarction(MI)detectionusingelectrocardiogram
CDSMOTE combines (class decomposition and synthetic (ECG)signals.TheABMincorporatesGaussiannaïveBayes
minority oversampling); it starts by dividing the majority and entropy to enhance classification accuracy and reliabil-
classintosubclassesandthenusingSMOTEtoincreasethe ity. Additionally, a modified convolutional neural network
sample size of the minority class. This approach strives to (MCNN) is developed to further optimize performance,
attain a balanced data distribution while retaining crucial showcasing the method’s potential for real-time monitoring
information [27]. Radius Synthetic Minority Oversampling anddecision-makinginclinicalsettings[32].
VOLUME13,2025 13689

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
TABLE1. EffectivenessandlimitationsofHybrid-samplingtechniques.
B. ALGORITHM-LEVELTECHNIQUES creates multiple classification models from the original
Algorithmicstrategiesenhancelearningintheminorityclass dataset and computes the class probability for each sample.
byimmediatelyalteringthetrainingprocessoftheclassifier It then applies a conditional risk formula to assign a
or modifying algorithms to address challenges associated cost to each sample, subsequently re-labeling the training
with imbalanced data effectively [34]. Common strategies set based on these costs. Still, it is less suitable for
encompass: handlingimbalanceddatainmulti-classscenarios[36].The
adaptive cost-sensitive learning (ACL) method, effective
underlargeimbalanceratios,dynamicallyadaptsthesample
1) COSTSENSITIVELEARNING cost throughout the entire training process. The model is
Cost-sensitivelearningentailsallocatingvaryingweightsor trained using weighted losses in a manner that harmonizes
costs to classes during the training process, prioritizing the the contribution of each class to the model parameter
penalizationofmisclassificationsoftheminorityclass[35]. updates, preventing the dominance of majority classes in
MetaCost is a cost-sensitive classification algorithm that imbalanced data during training. Calculating the costs for
13690 VOLUME13,2025

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
samples considers the sample number distribution, the imbalance challenges common in real-world applications.
convergence trend of classes, and the convergence trend Additionally, the study introduces a Python package that
of samples [37]. Another study employs cost-sensitive simplifiestheintegrationoftheselossfunctionsintoGBDT
learning to dynamically adjust class-specific costs within workflows,makingadvancedtechniquesmoreaccessibleto
deep neural networks, thereby improving the recognition researchersandpractitioners[40].
| of minority  | classes.    | This        | approach |                  | is particularly |                  | useful in |                    |          |        |         |            |      |             |        |
| ------------ | ----------- | ----------- | -------- | ---------------- | --------------- | ---------------- | --------- | ------------------ | -------- | ------ | ------- | ---------- | ---- | ----------- | ------ |
| applications | such        | as medical  |          | diagnosis        | and             | fraud detection, |           |                    |          |        |         |            |      |             |        |
|              |             |             |          |                  |                 |                  |           | 3) ENSEMBLEMETHODS |          |        |         |            |      |             |        |
| where        | accurately  | identifying |          | underrepresented |                 | classes          | is        |                    |          |        |         |            |      |             |        |
|              |             |             |          |                  |                 |                  |           | Ensemble           | methods  | entail | merging | multiple   | base | classifiers |        |
| critical     | [35]. An    | innovative  | adaptive |                  | cost-sensitive  |                  | learning  |                    |          |        |         |            |      |             |        |
|              |             |             |          |                  |                 |                  |           | or models          | to forge | a more | robust  | learner    |      | to address  | the    |
| method       | is proposed | to          | tackle   | the challenges   |                 | of imbalanced    |           |                    |          |        |         |            |      |             |        |
|              |             |             |          |                  |                 |                  |           | imbalance          | problem  | [41].  | Table   | 2 mentions |      | some        | ensem- |
datainindustrialfaultdiagnosis.Thisapproachdynamically
|             |         |             |           |           |             |               |          | ble methods,   | their    | findings,  | and        | their       | limitations. |     | These  |
| ----------- | ------- | ----------- | --------- | --------- | ----------- | ------------- | -------- | -------------- | -------- | ---------- | ---------- | ----------- | ------------ | --- | ------ |
| calculates  | sample  | costs       | based     | on sample |             | distribution  | and      |                |          |            |            |             |              |     |        |
|             |         |             |           |           |             |               |          | approaches     | leverage | various    | algorithms |             | or versions  |     | of the |
| convergence | trends, | effectively |           | reducing  |             | the dominance |          |                |          |            |            |             |              |     |        |
|             |         |             |           |           |             |               |          | same algorithm |          | to bolster | predictive | performance |              | on  | imbal- |
| of majority | classes | during      | training. |           | By ensuring |               | adequate |                |          |            |            |             |              |     |        |
anceddatasets.Itmitigatestheimpactofclassimbalanceby
| representation |                 | of minority | classes, | the         | method     | significantly |         |                  |             |         |              |         |          |           |      |
| -------------- | --------------- | ----------- | -------- | ----------- | ---------- | ------------- | ------- | ---------------- | ----------- | ------- | ------------ | ------- | -------- | --------- | ---- |
|                |                 |             |          |             |            |               |         | blending         | predictions | from    | multiple     | models, | thus     | enhancing |      |
| enhances       | the performance |             | of       | intelligent | diagnostic |               | models, |                  |             |         |              |         |          |           |      |
|                |                 |             |          |             |            |               |         | the classifier’s |             | overall | performance. |         | Boosting | refers    | to a |
particularlyinscenarioswithhighimbalanceratios[37].
|     |     |     |     |     |     |     |     | group of | machine    | learning | techniques   |      | that         | successively |         |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | ------------ | ---- | ------------ | ------------ | ------- |
|     |     |     |     |     |     |     |     | train a  | sequence   | of weak  | learners.    | Each | learner      |              | aims to |
|     |     |     |     |     |     |     |     | rectify  | the errors | of its   | predecessors |      | by assigning |              | higher  |
2) ALGORITHM-SPECIFICADJUSTMENTS
|     |     |     |     |     |     |     |     | importance | to  | misclassified | cases. | This | iterative |     | process |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------- | ------ | ---- | --------- | --- | ------- |
Adjustmentsspecifictoalgorithmsentailcustomizingmeth-
|          |          |        |        |     |          |          |     | enables | boosting | to construct |     | a resilient | ensemble |     | model |
| -------- | -------- | ------ | ------ | --- | -------- | -------- | --- | ------- | -------- | ------------ | --- | ----------- | -------- | --- | ----- |
| ods like | decision | trees, | random |     | forests, | and SVMs | to  |         |          |              |     |             |          |     |       |
capableofmakingaccuratepredictions,whichisparticularly
| handle      | imbalanced     | data        | more      | effectively, | as     | demonstrated |      |            |              |      |               |            |           |              |       |
| ----------- | -------------- | ----------- | --------- | ------------ | ------ | ------------ | ---- | ---------- | ------------ | ---- | ------------- | ---------- | --------- | ------------ | ----- |
|             |                |             |           |              |        |              |      | beneficial | in scenarios | with | class         | imbalance  |           | or noisy     | data. |
| in adaptive | cost-sensitive |             | learning, |              | which  | enhances     | the  |            |              |      |               |            |           |              |       |
|             |                |             |           |              |        |              |      | AdaBoost,  | a renowned   |      | boosting      | algorithm, |           | continuously |       |
| performance | of             | intelligent | diagnosis |              | models | in such      | con- |            |              |      |               |            |           |              |       |
|             |                |             |           |              |        |              |      | adjusts    | the weights  | of   | misclassified |            | instances | to improve   |       |
| ditions.    | A Support      | Vector      | Machine   |              | (SVM)  | equipped     | with |            |              |      |               |            |           |              |       |
themodel’soverallperformance[42].Bagging,orBootstrap
| Multiple        | Kernel | Learning         | (MKL)          | allows   | the            | SVM   | to inte- |                  |           |                 |          |            |         |            |          |
| --------------- | ------ | ---------------- | -------------- | -------- | -------------- | ----- | -------- | ---------------- | --------- | --------------- | -------- | ---------- | ------- | ---------- | -------- |
|                 |        |                  |                |          |                |       |          | Aggregating,     | generates |                 | multiple | training   | dataset | instances  |          |
| grate different |        | kernel functions |                | and      | fine-tune      | their | weights, |                  |           |                 |          |            |         |            |          |
|                 |        |                  |                |          |                |       |          | via bootstrap    | sampling, |                 | training | individual |         | base       | learners |
| thus improving  |        | its ability      | to             | classify | imbalanced     |       | datasets |                  |           |                 |          |            |         |            |          |
|                 |        |                  |                |          |                |       |          | on each          | sample.   | The predictions |          | of         | these   | base       | learners |
| more accurately |        | [38].            | The Stratified |          | Sampling-Based |       | Deep     |                  |           |                 |          |            |         |            |          |
|                 |        |                  |                |          |                |       |          | are subsequently |           | aggregated,     |          | usually    | through | averaging, |          |
NeuralNetwork(SSDNN)approachtacklesimbalanceddata
|            |     |           |     |            |          |            |     | to generate | the | final | prediction. | This | process | aims | to  |
| ---------- | --- | --------- | --- | ---------- | -------- | ---------- | --- | ----------- | --- | ----- | ----------- | ---- | ------- | ---- | --- |
| challenges | by  | employing | a   | stratified | sampling | technique, |     |             |     |       |             |      |         |      |     |
enhancemachinelearningmodels’overallperformanceand
| enhancing      | prediction     | accuracy.  |              | Partitioning |                 | the dataset    | into       |              |               |              |               |            |              |            |          |
| -------------- | -------------- | ---------- | ------------ | ------------ | --------------- | -------------- | ---------- | ------------ | ------------- | ------------ | ------------- | ---------- | ------------ | ---------- | -------- |
|                |                |            |              |              |                 |                |            | stability    | by mitigating |              | variance      | and        | overfitting. | Concur-    |          |
| non-duplicated |                | groups     | with         | balanced     | class           | representation |            |              |               |              |               |            |              |            |          |
|                |                |            |              |              |                 |                |            | rently,      | it indirectly | aids         | in addressing |            | imbalanced   |            | data     |
| increases      | computational  |            | complexity   |              | due to          | the            | stratified |              |               |              |               |            |              |            |          |
|                |                |            |              |              |                 |                |            | issues [43]. | Random        | forests,     |               | a widely   | favored      | ensemble   |          |
| sampling       | method         | [9].       | GENDA        | (Generative  |                 | Neighborhood-  |            |              |               |              |               |            |              |            |          |
|                |                |            |              |              |                 |                |            | learning     | technique,    | amalgamate   |               | numerous   | decision     |            | trees to |
| based Deep     | Autoencoder)   |            | is           | a novel      | generative      |                | model to   |              |               |              |               |            |              |            |          |
|                |                |            |              |              |                 |                |            | enhance      | predictive    | accuracy.    |               | Every      | tree in      | the forest | is       |
| address        | the imbalance, |            | particularly |              | for image       | and            | time-      |              |               |              |               |            |              |            |          |
|                |                |            |              |              |                 |                |            | constructed  | from          | a randomized |               | subset     | of features  |            | in the   |
| series data    | [13].          | By         | learning     | latent       | representations |                | of         |              |               |              |               |            |              |            |          |
|                |                |            |              |              |                 |                |            | training     | data,         | and the      | ultimate      | prediction |              | is formed  | by       |
| the data       | and            | generating | synthetic    |              | samples         | for            | minority   |              |               |              |               |            |              |            |          |
aggregatingthepredictionsfromallthetrees[44].Gradient
| classes, | its flexibility |          | allows | for      | application | in  | various  |            |            |           |           |           |           |           |        |
| -------- | --------------- | -------- | ------ | -------- | ----------- | --- | -------- | ---------- | ---------- | --------- | --------- | --------- | --------- | --------- | ------ |
|          |                 |          |        |          |             |     |          | Boosting   | optimizes  | weak      | learners, | typically |           | decision  | trees, |
| domains  | where           | original | data   | usage is | restricted. | It  | provides |            |            |           |           |           |           |           |        |
|          |                 |          |        |          |             |     |          | to improve | predictive | accuracy. |           | This      | algorithm | functions |        |
advantagesoveralgorithm-leveltechniquesbyincorporating
|                   |        |              |            |              |     |                |       | through    | iteratively | constructing |                  | decision | trees       | to  | rectify |
| ----------------- | ------ | ------------ | ---------- | ------------ | --- | -------------- | ----- | ---------- | ----------- | ------------ | ---------------- | -------- | ----------- | --- | ------- |
| data augmentation |        | and          | addressing | imbalance    |     | classification |       |            |             |              |                  |          |             |     |         |
|                   |        |              |            |              |     |                |       | the errors | made        | by preceding |                  | trees.   | It achieves |     | this by |
| without           | making | distribution |            | assumptions. |     | A novel        | deep- |            |             |              |                  |          |             |     |         |
|                   |        |              |            |              |     |                |       | assigning  | greater     | weights      | to misclassified |          | samples     |     | in each |
learning-basedmodelisintroducedtoaddressdataimbalance
|                |       |                 |         |               |     |              |        | iteration | [45]. A | stacked | deep   | learning   | algorithm | leverages |          |
| -------------- | ----- | --------------- | ------- | ------------- | --- | ------------ | ------ | --------- | ------- | ------- | ------ | ---------- | --------- | --------- | -------- |
| in medical     | image | classification. |         | Acknowledging |     | the          | under- |           |         |         |        |            |           |           |          |
|                |       |                 |         |               |     |              |        | ensemble  | methods | to      | manage | imbalanced |           | data      | adeptly. |
| representation |       | of many         | medical | conditions    |     | in datasets, | the    |           |         |         |        |            |           |           |          |
ItintegratestechniquessuchasStackedCNN(Convolutional
authorsproposeaninnovativeapproachthatutilizeseffective
|              |            |     |            |     |          |          |      | Neural | Networks) | and | Stacked | RNN | (Recurrent |     | Neural |
| ------------ | ---------- | --- | ---------- | --- | -------- | -------- | ---- | ------ | --------- | --- | ------- | --- | ---------- | --- | ------ |
| perturbation | operations |     | to extract |     | relevant | features | from |        |           |     |         |     |            |     |        |
Networks),employingbothtoidentifyintricatepatternsand
| single-class | samples | [39]. | Another |     | study | conducts | an in- |     |     |     |     |     |     |     |     |
| ------------ | ------- | ----- | ------- | --- | ----- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
temporalinterdependencies[4].
| depth exploration |     | of adapting |     | class-balanced |     | loss | functions |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --- | -------------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
forGradientBoostingDecisionTrees(GBDT)acrossdiverse
tabular classification tasks, including binary, multi-class, C. HYBRIDAPPROACHES
and multi-label classifications. The research highlights the Hybridapproachesamalgamatevariousstrategies,frequently
effectiveness of these loss functions in addressing class blendingdata-levelandalgorithm-leveltechniquesasshown
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 13691 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
TABLE2. Effectivenessandlimitationsofensemblemethods.
|     |     |     |     |     |     |     |     | Adversarial     | Network       |               | (E-GAN)  | technique |              | amalgamates    |         |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ------------- | -------- | --------- | ------------ | -------------- | ------- |
|     |     |     |     |     |     |     |     | features        | from          | both (GANs)   | and      | (CNNs),   |              | which are      | short-  |
|     |     |     |     |     |     |     |     | cuts to         | generative    | adversarial   |          | networks  | and          | convolutional  |         |
|     |     |     |     |     |     |     |     | neural          | networks,     | respectively. |          | This      | fusion       | leverages      | the     |
|     |     |     |     |     |     |     |     | data generation |               | prowess       | of       | GANs      | and the      | classification |         |
|     |     |     |     |     |     |     |     | capabilities    | of            | CNNs          | [11]. A  | recent    | study        | that tackles   | the     |
|     |     |     |     |     |     |     |     | challenge       | of imbalanced |               | spectral | data      | in materials |                | science |
throughaGenerativeAdversarialNetwork(GAN)-baseddata
augmentationmethod.Thisapproachusesjointoptimization
|     |     |     |     |     |     |     |     | between         | the      | GAN’s           | generator | and    | a classifier, | allowing   |           |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | --------------- | --------- | ------ | ------------- | ---------- | --------- |
|     |     |     |     |     |     |     |     | for the         | creation | of synthetic    | samples   |        | that          | are both   | realistic |
|     |     |     |     |     |     |     |     | and effectively |          | distinguishable |           | across | material      | phases     | [46].     |
|     |     |     |     |     |     |     |     | By employing    |          | transfer        | learning  | and    | domain        | adaptation |           |
FIGURE2. Approachestohandleimbalanceddataproblem.
|     |     |     |     |     |     |     |     | techniques, | explicitly |     | using Maximum |     | Mean | Discrepancy |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------------- | --- | ---- | ----------- | --- |
(MMD),thisapproachaddressestheissueofimbalanceddata
|           |           |               |           |         |             |               |     | in detecting | Return-Oriented |      |      | Programming |        | (ROP) | attacks. |
| --------- | --------- | ------------- | --------- | ------- | ----------- | ------------- | --- | ------------ | --------------- | ---- | ---- | ----------- | ------ | ----- | -------- |
| in figure | 2. These  | methodologies |           | provide | a           | comprehensive |     |              |                 |      |      |             |        |       |          |
|           |           |               |           |         |             |               |     | It leverages | balanced        | data | from | a source    | domain | to    | train a  |
| solution  | to tackle | class         | imbalance |         | challenges, | enhancing     |     |              |                 |      |      |             |        |       |          |
modelwhileminimizingtheMMDtoalignthedistributions
| machine      | learning | models’           |          | resilience, | effectiveness, |           | and     |            |           |             |           |            |       |                 |       |
| ------------ | -------- | ----------------- | -------- | ----------- | -------------- | --------- | ------- | ---------- | --------- | ----------- | --------- | ---------- | ----- | --------------- | ----- |
|              |          |                   |          |             |                |           |         | of the     | source    | and target  | domains   |            | [47]. | The integration |       |
| reliability. | By       | integrating       | multiple |             | methods,       | they      | aim to  |            |           |             |           |            |       |                 |       |
|              |          |                   |          |             |                |           |         | of Genetic | Algorithm |             | (GA) with | Support    |       | Vector Machine  |       |
| alleviate    | issues   | like overfitting, |          | information |                | loss, and | poor    |            |           |             |           |            |       |                 |       |
|              |          |                   |          |             |                |           |         | (SVM)      | seeks     | to optimize | SVM       | parameters |       | while           | using |
| performance  | in       | minority          | classes, | thus        | enhancing      | the       | overall |            |           |             |           |            |       |                 |       |
|              |          |                   |          |             |                |           |         | targeted   | sampling  | techniques  |           | to manage  |       | class imbalance |       |
effectivenessofmachinelearningmodelsinmanagingclass
effectively[48].
| disproportionality. |     | Table  | 3 highlights |        | the hybrid | techniques |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------ | ------------ | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| employed            | in  | recent | years.       | Common | hybrid     | approaches |     |     |     |     |     |     |     |     |     |
include:
|     |     |     |     |     |     |     |     | 2) ALGORITHMICENSEMBLEWITHDATA-LEVEL |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
TECHNIQUES
1) DATA-PRE-PROCESSINGWITH Integratingalgorithmicensemblewithdata-leveltechniques
ALGORITHM-ADJUSTMENTS involves generating multiple models by employing diverse
Data preprocessing incorporating algorithm adjustments: resampled dataset versions and consolidating their pre-
involves using techniques like over-sampling, under- dictions. SMOTEBoost and RUSBoost exemplify these
sampling, or SMOTE to prepare the data before applying techniques, with SMOTEBoost combining the SMOTE
algorithm-level adjustments. The Enhanced Generative algorithmwithboostingtoenhancepredictionsinimbalanced
| 13692 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
TABLE3. Effectivenessandlimitationsofhybridapproachestohandleimbalanceddata.
datasets.Itovercomestheconstraintsoftraditionalboosting distribution. Subsequently, Random Forest harnesses this
algorithms such as AdaBoost, boosts learning by creating balanced dataset to construct a resilient ensemble model,
synthetic examples for the minority class and adjusting the enhancing classification effectiveness [51]. Before applying
training distribution to focus on these instances [49], and the MCNN-LSTM model, the Tomek-Links technique is
RUSBoost combines Random UnderSampling (RUS) with utilizedasanundersamplingmethodtomanageimbalanced
boostingentailsundersamplingthemajorityclassandsubse- data.
quently boosting the classifier on the balanced dataset [50]. The MCNN-LSTM model is a hybrid framework where
Integrating (DB-SLSMOTE) with (Random Forest) tackles Convolutional Neural Networks (CNN) are effective in text
class imbalance by augmenting the minority class through datawhencapturinglocalfeaturesandpatterns.Incontrast,
oversampling by synthetic samples generated from density LongShort-TermMemory(LSTM)networksaretailoredfor
VOLUME13,2025 13693

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
textclassificationtasks,instrumentalinsituationswithimbal- cardiovascular diseases and breast cancer [4]. Similarly, E-
anceddata.Thisintegrationaddressestheinherentchallenges GAN improves disease detection accuracy for conditions
ofimbalanceddataintextclassificationendeavors[52].Inte- such as breast cancer, diabetes, and chronic kidney disease
grating oversampling techniques with ensemble deep learn- byaddressingimbalanceddatasetseffectively[11].TheDB-
ingmodelsinvolvesmergingmodifiedoversamplingmethods SLSMOTEwithRandomForestmethodprovesparticularly
like(D-SMOTE)Distance-basedSMOTEand(BP-SMOTE) valuableindetectingrarediseasesbyenhancingclassification
Bi-phasic SMOTE with Stacked CNN and Stacked RNN. accuracyindatasetswithlimitedpositivecases[51].DCGAN
It enhances predictive accuracy and robustness in handling andCNNgeneratesyntheticsamplesformedicalimagingto
imbalanced datasets [4]. In [53], authors combined Deep mitigateclassimbalances,supportingtheaccuratediagnosis
Convolutional Generative Adversarial Networks(DCGAN) of diseases like malaria [53]. Additionally, the integrated
for generating synthetic samples and Convolutional Neural approach of SMOTE, Undersampling, PSO, and MetaCost
Networks (CNN) for classification and feature extraction. optimizestheclassificationofunderrepresentedmedicaldata,
The research by [54] integrates resampling techniques like aiding healthcare professionals in making more informed
SMOTE and US to rebalance class distributions. Moreover, decisions[54].
it employs Particle Swarm Optimization (PSO) for attribute Fraud detection leverages methods like DB-SLSMOTE
selection to improve sensitivity and reduce data dimension- with Random Forest, enhancing models’ reliability for
ality.Atthesametime,MetaCostisutilizedasanalgorithm- identifyingfraudulentfinancialtransactions[51].TheTomek
level approach to address class imbalances effectively. Links+BIRCHClustering+BorderlineSMOTEtechnique
Another investigation employs a blend of undersampling further improves fraud detection accuracy by addressing
usingTomekLinks,clusteringviaBIRCH,andoversampling imbalances in transaction datasets [7]. Additionally, the
through Borderline SMOTE to address the imbalance in ATOMICMethodautomatesthecreationofmachinelearning
credit card transaction datasets and by removing noise with solutions designed for imbalanced data, facilitating the
TomekLinks,clusteringthedatawithBIRCHandgenerating detectionoffraudulentactivitiesinfinancialsystems[55].
synthetic instances for the underrepresented class through In cybersecurity, Transfer Learning with Domain Adap-
Borderline SMOTE, this approach seeks to equalize the tation using MMD is utilized to enhance the detection of
dataseteffectively[7].TheATOMICapproachrepresentsan Return-Oriented Programming (ROP) attacks, a complex
automated machine-learning method explicitly designed for exploit technique [47]. This approach leverages transfer
imbalanced classification tasks. It addresses the challenges learningtoaddressdatasetimbalances,improvingtheaccu-
posed by imbalanced datasets through a combination of racy and reliability of deep learning models for identifying
the algorithmic ensemble, which optimizes the selection suchattacks.
of learning algorithms, and data-level techniques, which Inmaterialsscience,theGAN-BasedDataAugmentation
optimize resampling strategies and hyperparameters [55]. Method tackles the classification of material phases in
A study examines the challenges of classifying minority imbalanced spectral datasets. Generating synthetic samples
classes in imbalanced datasets, with a focus on cerebral supportsexperimentaldesignandmaterialscharacterization,
stroke prediction and bankruptcy risk in financial data. asdemonstratedincasestudiesinvolvinghydrogelssuchas
By evaluating the performance of various machine learning PluronicF-127andAlpha-Cyclodextrin[46].
algorithms, the research underscores the limitations of In automated text classification, the Tomek Links Before
traditional resampling methods like SMOTE in clinical MCNN-LSTMmethodcategorizesnewsarticlesintodiverse
contexts. It highlights the critical role of understanding topics such as Politics, Sports, and Lifestyle [52]. This
dataset characteristics, as these factors greatly impact the approach enhances content organization and retrieval for
effectivenessofpredictivemodels[56]. media organizations, ensuring improved representation and
handlingofunderrepresentedcategories.
3) REAL-WORLDAPPLICATIONSOFHYBRIDAPPROACHES For telecommunications, the Genetic Algorithm with
Hybrid approaches have effectively addressed class imbal- SVM improves user classification in systems such as
ance across various real-world domains. Enhancing model Non-Orthogonal Multiple Access (NOMA) networks.
performance and reliability has become essential in critical By addressing class imbalances, this method ensures
fields such as healthcare, fraud detection, cybersecurity, efficient resource allocation and optimized communication
materials science, telecommunications, and others. Each management[48].
application utilizes hybrid techniques to tackle the unique The ATOMIC Method is applicable across various
challenges posed by imbalanced datasets, improving pre- domains,suchasanomalydetection,healthcarediagnostics,
dictive accuracy and decision-making capabilities. Table 4 frauddetection,andcreditscoring.Automatingmodelopti-
shows the applications and datasets used in each study mizationforimbalanceddatasimplifiesanalyticalprocesses,
discussed. enhancing decision-making and resource allocation in these
In healthcare, techniques such as D-SMOTE and BP- criticalareas[55].
SMOTE with Stacked CNN and RNN enhance predictive The study presenting a Hybrid Ensemble focuses on
analytics for the early diagnosis of critical conditions like cerebral stroke prediction by enhancing the reliability of
13694 VOLUME13,2025

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
machine learning models and assessing the effectiveness of are susceptible to mode collapse, where the generator fails
SMOTEinclinicaldatasets[56]. tocovertheentiredataspace,limitingsamplediversityand
quality of augmentation [6]. The limitations of (ABM) are
V. DISCUSSIONOFTHELIMITATIONS summarizedintheriskoftraditionalunder-samplingleading
Thissectionprovidesajustificationforthelimitationsofeach to the loss of valuable minority class information and the
technique. Data-level, the (SMOTE-Tomek and SMOTE- reliance on validation with a single dataset, which restricts
ENN) these techniques face difficulties with datasets itsgeneralizabilitytodiverseclinicalscenarios[32].
featuring high-class overlap or noise. SMOTE-generated Algorithm-level,in(SVMwithMultipleKernelLearning
synthetic samples may resemble the majority of instances, (MKL)) optimizing multiple kernel functions increases
causingclassifierconfusion.Additionally,cleaningmethods computational demands, potentially limiting scalability in
can unintentionally remove valuable minority samples or real-time applications. Extensive parameter tuning is also
miss noisy majority instances, reducing effectiveness [26]. needed for optimal results, which can be time-consuming
Distance-basedSMOTE(D-SMOTE)requireshighcomputa- andmayreducemodelinterpretability—akeyfactorinfields
tionalresourcesfordistancecalculationsinhigh-dimensional like healthcare [38]. (AdaBoost) emphasis on misclassified
spaces, leading to longer processing times. The ‘‘curse of instancescanmakeithighlysensitivetonoisydata,increas-
dimensionality’’insuchdatasetscandiminishtherelevance ingtheriskofoverfitting.Thealgorithmmayover-focuson
of distance metrics, affecting synthetic sample quality and thesepointsinthepresenceofoutliersornoise,reducingits
efficiency[4].Bi-PhasicSMOTE(BP-SMOTE),itsiterative abilitytogeneralizeeffectivelytounseendata[42].(Bagging)
process, with multiple SMOTE applications and instance iscomputationallyintensive,asittrainsmultiplemodelsfor
selection phases, can be resource-intensive. As dataset size each bootstrap sample. Additionally, it may not adequately
grows, processing time and resource demands increase, address class imbalance on its own, as bootstrap sampling
reducing scalability for real-world applications [4]. Class- can maintain the original imbalance, resulting in poor
decompositionSMOTE(CD-SMOTE)effectivenessrelieson performanceonminorityclasses[43].(RandomForests)may
accurately decomposing the majority class into subclasses. show biastoward the majorityclass in imbalanceddatasets,
Inaccurate decomposition can produce poorly defined sub- as training often prioritizes majority class accuracy. The
classes, diminishing the impact of oversampling and poten- modelalsorequirescarefulhyperparametertuningtoprevent
tially biasing the model toward the majority class [27]. increased bias or overfitting, making balanced performance
Radius-SMOTE (R-SMOTE) performance depends heavily across classes challenging to achieve [44]. In (Gradient
on correctly tuning parameters like radius distance for Boosting) Decision Trees (GBDT) with additional trees,
defining boundaries in synthetic sample generation. Poor GBDTcanbecomeoverlyfittedtothetrainingdata,capturing
tuning can cause excessive overlap with majority samples noise and outliers instead of actual patterns, which leads
or inadequate minority sample generation. Additionally, to overfitting. Effective regularization is crucial to prevent
dataset size and complexity increase computational costs, performance loss on unseen data [45]. (Stacked Deep
limiting scalability [28]. Self-Inspected Adaptive SMOTE Learning) models are complex due to the integration of
(SASMOTE) requires precise hyperparameter tuning for multiple architectures, raising the risk of overfitting. This
optimal results. Its design for specific case studies limits complexity may lead the model to capture noise instead of
generalizability across healthcare applications, suggesting a generalpatterns,resultinginpoorgeneralization,particularly
need for adaptation to broader contexts [29]. (Borderline- withsmallerorlessdiversedatasets[4].
SMOTE) generates synthetic samples near decision bound- Hybrid-level, in (D-SMOTE and BP-SMOTE with
aries, which may overlap with the majority class, creating Stacked CNN and RNN), the complexity of combining
ambiguous regions. This overlap can confuse the classifier multiple deep learning architectures increases the risk of
and reduce generalization performance, particularly with overfitting, complicating generalization. Additionally, inter-
poorly separated classes [30]. Oriented Oversampling with pretability is reduced, making it challenging to understand
SpatialInformation(OOSI)mayfaceruntimechallengeson model decisions, especially in sensitive fields like health-
complex datasets due to high dimensionality and intricate care [4]. (E-GAN with CNN) combined GAN and CNN
distributions.Adaptivespatialpartitioningrequiresintensive model demands substantial computational resources and
computation, affecting scalability and efficiency, especially time, particularly for large datasets. Additionally, synthetic
with noisy datasets [31]. SMOTE with Tomek Links + samples may lead to overfitting if they do not accurately
Borderline SMOTE (SDWBOTE) If temporal dependencies reflect the minority class distribution [11]. (DB-SLSMOTE
betweensamplesaren’taccuratelycaptured,SDWBOTEmay with Random Forest) generating synthetic samples can add
carryovernoiseandbiasfromtheoriginaldataset,potentially to training complexity and the risk of overfitting, with
resulting in poor real-world classifier performance and Random Forest training being especially resource-intensive
misrepresentationofminorityclasses[8].(GAN-BasedData forlargedatasets[51].(Tomek-LinksBeforeMCNN-LSTM)
Augmentation)demandssubstantialcomputationalresources the model’s dependence on a specific dataset (Indonesian
fortrainingduetothecomplexityofadversarialoptimization news) limits its generalizability, and the lack of transfer
betweenthegeneratoranddiscriminator.Additionally,GANs learningpreventsitfromutilizinglargerdatasetstoenhance
VOLUME13,2025 13695

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
TABLE4. Applicationsofhybridapproaches.
performance [52]. (DCGAN and CNN) requires substantial VI. EVALUATIONMETHODS
computational resources for adversarial training, and syn- When handling imbalanced datasets in machine learning,
theticsamplesmayleadtooverfitting,affectingthemodel’s choosing the appropriate evaluation metrics is crucial for
generalizationonunseendata[53].(SMOTE+US+PSO+ preciselyassessingmodelperformance.Thissectionexplores
MetaCost) concentrating on specific methods may restrict various evaluation techniques particularly beneficial for
broader insights into alternative approaches. Furthermore, addressing imbalanced data. It highlights the advantages of
conclusions may lack generalizability if datasets do not each method and its effectiveness in evaluating the model’s
includediversemedicalcharacteristics[54].(TomekLinks+ performance, particularly concerning accurately predicting
BIRCH Clustering + Borderline SMOTE) the approach’s outcomesfortheminorityclass.
complexity and parameter sensitivity necessitates careful Accuracyisafundamentalassessmentcriterionutilizedin
tuning,anditssensitivitytonoisemayleaveresidualnoise, machine learning and data mining. However, accuracy can
impacting model accuracy [7]. ATOMIC Method (Meta- result in misaddressing if used with an unbalanced dataset.
Learning) ATOMIC’s handling of imbalanced data could A model may still achieve high overall accuracy even if its
be enhanced by a broader exploration of hyperparameters classification performance for minority categories is poor
and algorithms, improving its performance and adaptability as long as it performs well in the majority categories. For
across different datasets [55]. (Genetic Algorithm with example, if 99% of the testing data are negative samples,
SVM) the iterative nature of Genetic Algorithms results we can get a 99% accuracy by simply classifying all the
in high computational costs and a risk of overfitting if testing data as a negative sample. So, the accuracy cannot
hyperparameters,suchaspopulationsizeandmutationrate, be chosen as an evaluation index in imbalanced learning.
are not carefully optimized [48]. (Transfer Learning and Theevaluationindicatorsrelatingtoimbalancedlearningare
MMD) the high-quality source data is crucial for transfer showninTable5.
learning, and limited validation data can reduce detection In Table 5, most evaluation metrics are derived from the
effectiveness. Careful model selection is essential to ensure confusionmatrix(CM),acriticaltoolforvisuallyrepresent-
consistentresults[47].(GAN-basedDataAugmentationwith inganalgorithm’sperformance.It’sparticularlycriticalwhen
Joint Optimization) is computationally intensive due to the dealing with imbalanced datasets as it delineates the count
dual optimization between the generator and classifier, and of accurate and inaccurate predictions for each class. This
it struggles with high phase similarity, which limits distinct detailedbreakdowniscrucialforunderstandingthemodel’s
samplegenerationandeffectiveclassseparation[46].Inthe effectiveness across the predominant and underrepresented
(Hybrid Ensemble) approach, classifiers face challenges in classes. The main components of the confusion matrix
accurately predicting minority classes in medical datasets, are:
and SMOTE’s theoretical validation may fail to align with • (TP) True Positives: Accurately identified positive
real-worldclinicalapplications[56]. observation.
13696 VOLUME13,2025

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
TABLE5. Evaluationmetricsforimbalanceclassification.
• (TN)True Negatives: Accurately identified negative where it is essential not to overlook the minority class,
observation. which is often of higher interest in imbalanced datasets.
• (FP)FalsePositives:Incorrectlyidentifiedaspositive. For multiclass imbalance problems, the G-mean evaluation
• (FN)FalseNegatives:Incorrectlyidentifiedasnegative. metric is often preferred as it offers a unified measurement
approach,eliminatingtheneedtoassesseachclassseparately.
MetricslikeAUCandG-meanarecommonlyusedbecause
theyremainunaffectedbyclassdistributionimbalances.AUC And for highly imbalanced Big Data, the Area under the
Precision-RecallCurve(AUPRC)isamoreeffectivemetric
isbasedontheentireROCcurve,whileG-meanincorporates
different parts of the confusion matrix, ensuring a more for evaluating the performance of classifiers. In highly
balanced model performance evaluation. This makes them imbalanced Big Data, the AUC metric fails to capture
informationaboutprecisionscoresandfalsepositivecounts
| suitable | for dealing | with | situations | where | there are large |     |     |     |     |
| -------- | ----------- | ---- | ---------- | ----- | --------------- | --- | --- | --- | --- |
differences in the number of positive and negative class that the AUPRC metric reveals. The F1 Score denotes the
samples. The Receiver Operating Characteristic curve and harmonic mean of precision and recall, which is valuable
the Area Under the Curve are valuable for assessing the in situations requiring a balance between the two and is
quality of classifier outputs. These metrics are particularly commonindatasetswithimbalancedclassdistributions.The
|          |            |             |        |           |           | F1 Score provides | more context | than accuracy | in situations |
| -------- | ---------- | ----------- | ------ | --------- | --------- | ----------------- | ------------ | ------------- | ------------- |
| adept at | evaluating | performance | across | different | threshold |                   |              |               |               |
settings, offering robustness against class imbalance. The withunevenclassdistribution.IntheformulasforAUCand
AUCcondensestheROCcurve’sinsightsintoasinglevalue, F1-score,Precisiondenotesaccuracy[57],[58].
expressing the likelihood that a classifier will prioritize a Consideringtheseevaluationmethodsensuresathorough
randomly chosen positive instance over a negative one. The understanding of a model’s performance on imbalanced
|                 |        |              |               |           |             | datasets, guiding | the development | of efficient | and equitable |
| --------------- | ------ | ------------ | ------------- | --------- | ----------- | ----------------- | --------------- | ------------ | ------------- |
| ROC curve       | graphs | TPR          | (TruePositive | Rate)     | against FPR |                   |                 |              |               |
| (False Positive |        | Rate) across | different     | threshold | configura-  | models.           |                 |              |               |
tions.AUCistheareaundertheROCcurve.TheGeometric
Mean computed by extracting the square root of (Recall VII. CONCLUSION
and Specificity) product guarantees that enhancements in This paper highlights the crucial importance of addressing
one class’s efficiency do not adversely impact the other. classimbalanceinmachinelearninginitiatives.Itbeginsby
This balance is crucial for effectively evaluating models discussing basic strategies for balancing class distribution,
| VOLUME13,2025 |     |     |     |     |     |     |     |     | 13697 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
which paves the way for a comprehensive exploration [9] J. Sadaiyandi, P. Arumugam, A. K. Sangaiah, and C. Zhang, ‘‘Strat-
of techniques categorized into data-level, algorithm-level, ified sampling-based deep learning approach to increase prediction
|           |             |               |     |      |      |              | accuracy | of unbalanced |     | dataset,’’ | Electronics, | vol. 12, | no. 21, p.4423, |
| --------- | ----------- | ------------- | --- | ---- | ---- | ------------ | -------- | ------------- | --- | ---------- | ------------ | -------- | --------------- |
| or hybrid | strategies. | Additionally, |     | this | work | examines the |          |               |     |            |              |          |                 |
Oct.2023.
| limitations | inherent | in  | each technique, |     | providing | justifi- |                   |     |           |        |            |               |          |
| ----------- | -------- | --- | --------------- | --- | --------- | -------- | ----------------- | --- | --------- | ------ | ---------- | ------------- | -------- |
|             |          |     |                 |     |           |          | [10] S. Briechle, | P.  | Krzystek, | and G. | Vosselman, | ‘‘Silvi-net—A | dual-CNN |
cations for their shortcomings, to offer a nuanced under- approachforcombinedclassificationoftreespeciesandstandingdead
|          |          |           |            |     |                   |     | trees | from remote | sensing | data,’’ | Int. J. Appl. | Earth | Observ. Geoinf., |
| -------- | -------- | --------- | ---------- | --- | ----------------- | --- | ----- | ----------- | ------- | ------- | ------------- | ----- | ---------------- |
| standing | of their | practical | challenges |     | and opportunities | for |       |             |         |         |               |       |                  |
vol.98,Jun.2021,Art.no.102292.
| improvement.Subsequently, |     |     | it  | underscores | the | importance |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[11] T.Suresh,Z.Brijet,andT.D.Subha,‘‘Imbalancedmedicaldiseasedataset
of evaluation methods in assessing the efficacy of these classificationusingenhancedgenerativeadversarialnetwork,’’Comput.
strategies under imbalanced data conditions, examining Methods Biomechanics Biomed. Eng., vol. 26, no. 14, pp.1702–1718,
Oct.2023.
metrics like F1 Score, AUC, and G-mean, among others. [12] G. Y. Wong, F. H. F. Leung, and S.-H. Ling, ‘‘A novel evolutionary
Thesemetricsarevitalforevaluatinghowvarioustechniques preprocessing method based on over-sampling and under-sampling for
fare, especially in accurately predicting outcomes for the imbalanceddatasets,’’inProc.39thAnnu.Conf.IEEEInd.Electron.Soc.
(IECON),Nov.2013,pp.2354–2359.
minorityclass.
[13] E.Troullinou,G.Tsagkatakis,A.Losonczy,P.Poirazi,andP.Tsakalides,
Recent studies have identified several gaps in address- ‘‘A generative neighborhood-based deep autoencoder for robust imbal-
ancedclassification,’’IEEETrans.Artif.Intell.,vol.5,no.1,pp.80–91,
| ing imbalanced |     | data across | data-centric, |     | algorithmic, | and |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Jan.2024.
blendedapproaches.Atthedatalevel,thereisapressingneed
[14] M.Koziarski,M.Woźniak,andB.Krawczyk,‘‘Combinedcleaningand
| for scalable | techniques |     | that can | manage | large | imbalanced |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | -------- | ------ | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
resamplingalgorithmformulti-classimbalanceddatawithlabelnoise,’’
Knowl.-BasedSyst.,vol.204,Sep.2020,Art.no.106223.
| datasets     | and maintain    |     | their | effectiveness | across  | differ- |                |         |            |        |                  |       |                 |
| ------------ | --------------- | --- | ----- | ------------- | ------- | ------- | -------------- | ------- | ---------- | ------ | ---------------- | ----- | --------------- |
|              |                 |     |       |               |         |         | [15] A. Singh, | R.      | K. Ranjan, | and A. | Tiwari, ‘‘Credit | card  | fraud detection |
| ent domains. | Algorithm-level |     |       | challenges    | revolve | around  |                |         |            |        |                  |       |                 |
|              |                 |     |       |               |         |         | under          | extreme | imbalanced | data:  | A comparative    | study | of data-level   |
strengtheningtheresilienceofmethodsagainsttheevolving
|                  |     |               |     |                 |     |            | algorithms,’’ |     | J. Exp. Theor. | Artif. | Intell., | vol. 34, no. | 4, pp.571–598, |
| ---------------- | --- | ------------- | --- | --------------- | --- | ---------- | ------------- | --- | -------------- | ------ | -------- | ------------ | -------------- |
| threats inherent |     | in imbalanced |     | data scenarios. |     | Meanwhile, | Jul.2022.     |     |                |        |          |              |                |
hybrid approaches face scalability, generalizability, and [16] H.Wasswa,T.Lynar,andH.Abbass,‘‘EnhancingIoT-botnetdetection
usingvariationalauto-encoderandcost-sensitivelearning:Adeeplearning
robustnessissues,highlightingthenecessityformethodsthat approach for imbalanced datasets,’’ in Proc. IEEE Region 10 Symp.
can effectively scale, function across diverse settings, and (TENSYMP),Sep.2023,pp.1–6.
resistevolvingthreatsinimbalanceddatacontexts. [17] P.KaurandA.Gosain,‘‘Comparingthebehaviorofoversamplingand
undersamplingapproachofclassimbalancelearningbycombiningclass
Thesechallengesunderlinethecontinuouspushtodevelop
imbalanceproblemwithnoise,’’inProc.ICTBasedInnov.CSI.Cham,
more effective and flexible imbalanced data classification Switzerland:Springer,Sep.2017,pp.23–30.
|          |           |     |         |         |       |            | [18] D. Elreedy, | A.           | F. Atiya, | and F.       | Kamalov, | ‘‘A theoretical | distribution |
| -------- | --------- | --- | ------- | ------- | ----- | ---------- | ---------------- | ------------ | --------- | ------------ | -------- | --------------- | ------------ |
| methods. | Moreover, | the | balance | between | model | complexity |                  |              |           |              |          |                 |              |
|          |           |     |         |         |       |            | analysis         | of synthetic | minority  | oversampling |          | technique       | (SMOTE) for  |
andgeneralizationremainsasignificanthurdle,emphasizing
|          |             |           |     |               |     |               | imbalanced | learning,’’ | Mach. | Learn., | vol. | 113, no. 7, | pp.4903–4923, |
| -------- | ----------- | --------- | --- | ------------- | --- | ------------- | ---------- | ----------- | ----- | ------- | ---- | ----------- | ------------- |
| the need | for ongoing | research. |     | Understanding |     | the strengths |            |             |       |         |      |             |               |
Jul.2024.
andlimitationsofeachapproach,includingessentialevalua- [19] S. Mundra, S. Vijay, A. Mundra, P. Gupta, M. K. Goyal, M. Kaur,
tionmethods,equipsresearcherstodevelopmachine-learning S.Khaitan,andA.K.Rajpoot,‘‘Classificationofimbalancedmedicaldata:
Anempiricalstudyofmachinelearningapproaches,’’J.Intell.FuzzySyst.,
models that are effective, robust, and ready for real-world vol.43,no.2,pp.1933–1946,Jun.2022.
application.Thesemodelsarepurposefullycraftedtomanage [20] T.Wongvorachan,S.He,andO.Bulut,‘‘Acomparisonofundersampling,
theintricacieslinkedwithdataimbalanceadeptly. oversampling,andSMOTEmethodsfordealingwithimbalancedclassi-
ficationineducationaldatamining,’’Information,vol.14,no.1,p.54,
Jan.2023.
REFERENCES [21] R.MalhotraandK.Lata,‘‘Anempiricalstudyonpredictabilityofsoftware
maintainabilityusingimbalanceddata,’’Softw.QualityJ.,vol.28,no.4,
| [1] S. | Haykin, | Neural Networks: |     | A Comprehensive |     | Foundation. |     |     |     |     |     |     |     |
| ------ | ------- | ---------------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
UpperSaddleRiver,NJ,USA:Prentice-Hall,1998. pp.1581–1614,Dec.2020.
[2] S.-M.Chen,DataScienceandBigData:AnEnvironmentofComputa- [22] M.Khushi,K.Shaukat,T.M.Alam,I.A.Hameed,S.Uddin,S.Luo,
tionalIntelligence.Cham,Switzerland:Springer,2017. X.Yang,andM.C.Reyes,‘‘Acomparativeperformanceanalysisofdata
resamplingmethodsonimbalancemedicaldata,’’IEEEAccess,vol.9,
[3] J.L.Leevy,T.M.Khoshgoftaar,R.A.Bauder,andN.Seliya,‘‘Asurvey
pp.109960–109975,2021.
onaddressinghigh-classimbalanceinbigdata,’’J.BigData,vol.5,no.1,
pp.1–30,Dec.2018. [23] K. M. Hasib, M. S. Iqbal, F. M. Shah, J. A. Mahmud, M. H. Popel,
[4] A. M. Sowjanya and O. Mrudula, ‘‘Effective treatment of imbalanced M. I. H. Showrov, S. Ahmed, and O. Rahman, ‘‘A survey of methods
datasetsinhealthcareusingmodifiedSMOTEcoupledwithstackeddeep formanagingtheclassificationandsolutionofdataimbalanceproblem,’’
learningalgorithms,’’Appl.Nanoscience,vol.13,no.3,pp.1829–1840, 2020,arXiv:2012.11870.
Feb.2022. [24] V. W. de Vargas, J. A. S. Aranda, R. dos Santos Costa,
|           |            |       |           |       |          |                    | P.R.daSilvaPereira, |     | and | J. L. | V. Barbosa, | ‘‘Imbalanced | data |
| --------- | ---------- | ----- | --------- | ----- | -------- | ------------------ | ------------------- | --- | --- | ----- | ----------- | ------------ | ---- |
| [5] M. M. | Chowdhury, | R. S. | Ayon, and | M. S. | Hossain, | ‘‘An investigation |                     |     |     |       |             |              |      |
of machine learning algorithms and data augmentation techniques for preprocessing techniques for machine learning: A systematic mapping
diabetesdiagnosisusingclassimbalancedBRFSSdataset,’’Healthcare study,’’Knowl.Inf.Syst.,vol.65,no.1,pp.31–57,Jan.2023.
Anal.,vol.5,Jun.2024,Art.no.100297. [25] N.V.Chawla,K.W.Bowyer,L.O.Hall,andW.P.Kegelmeyer,‘‘SMOTE:
[6] Q. Su, H. N. A. Hamed, M. A. Isa, X. Hao, and X. Dai, ‘‘A GAN- Syntheticminorityover-samplingtechnique,’’J.Artif.Intell.Res.,vol.16,
baseddataaugmentationmethodforimbalancedmulti-classskinlesion pp.321–357,Jun.2002.
classification,’’IEEEAccess,vol.12,pp.16498–16513,2024. [26] G. E. A. P. A. Batista, R. C. Prati, and M. C. Monard, ‘‘A study of
[7] M. Alamri and M. Ykhlef, ‘‘Hybrid undersampling and oversampling thebehaviorofseveralmethodsforbalancingmachinelearningtraining
for handling imbalanced credit card data,’’ IEEE Access, vol. 12, data,’’ ACM SIGKDD Explorations Newslett., vol. 6, no. 1, pp.20–29,
| pp.14050–14060,2024. |     |     |     |     |     |     | Jun.2004. |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
[8] N.JiangandN.Li,‘‘Awindturbinefrequentprincipalfaultdetectionand [27] E. Elyan, C. F. Moreno-Garcia, and C. Jayne, ‘‘CDSMOTE: Class
localizationapproachwithimbalanceddatausinganimprovedsynthetic decompositionandsyntheticminorityclassoversamplingtechniquefor
oversampling technique,’’ Int. J. Electr. Power Energy Syst., vol. 126, imbalanced-data classification,’’ Neural Comput. Appl., vol. 33, no. 7,
| Mar.2021,Art.no.106595. |     |     |     |     |     |     | pp.2839–2851,Apr.2021. |     |     |     |     |     |               |
| ----------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | ------------- |
| 13698                   |     |     |     |     |     |     |                        |     |     |     |     |     | VOLUME13,2025 |

M.Altalhanetal.:ImbalancedDataProbleminMachineLearning:AReview
[28] G. A. Pradipta, R. Wardoyo, A. Musdholifah, and I. N. H. Sanjaya, [51] Q.Han,R.Yang,Z.Wan,S.Chen,M.Huang,andH.Wen,‘‘Imbalanced
‘‘Radius-SMOTE: A new oversampling technique of minority samples dataclassificationbasedonDB-SLSMOTEandrandomforest,’’inProc.
basedonradiusdistanceforlearningfromimbalanceddata,’’IEEEAccess, Chin.Autom.Congr.(CAC),Nov.2020,pp.6271–6276.
vol.9,pp.74763–74777,2021. [52] K.M.Hasib,S.Azam,A.Karim,A.A.Marouf,F.M.J.M.Shamrat,
[29] T.Kosolwattana,C.Liu,R.Hu,S.Han,H.Chen,andY.Lin,‘‘Aself- S. Montaha, K. C. Yeo, M. Jonkman, R. Alhajj, and J. G. Rokne,
inspectedadaptiveSMOTEalgorithm(SASMOTE)forhighlyimbalanced ‘‘MCNN-LSTM:CombiningCNNandLSTMtoclassifymulti-classtext
dataclassificationinhealthcare,’’BioDataMining,vol.16,no.1,p.15, inimbalancednewsdata,’’IEEEAccess,vol.11,pp.93048–93063,2023.
Apr.2023. [53] L.M.ShoohiandJ.H.Saud,‘‘DCGANforhandlingimbalancedmalaria
[30] F.delaBourdonnayeandF.Daniel,‘‘Evaluatingresamplingmethodson datasetbasedonover-samplingtechniqueandusingCNN,’’Medico-Legal
areal-lifehighlyimbalancedonlinecreditcardpaymentsdataset,’’2022, Update,vol.20,no.1,pp.1079–1085,Apr.2020.
arXiv:2206.13152. [54] Y.-C. Wang and C.-H. Cheng, ‘‘A multiple combined method for
[31] Y. Deng and M. Li, ‘‘An adaptive and robust method for oriented rebalancing medical data with class imbalances,’’ Comput. Biol. Med.,
oversampling with spatial information for imbalanced noisy datasets,’’ vol.134,Jul.2021,Art.no.104527.
IEEEAccess,vol.11,pp.122610–122624,2023. [55] N. Moniz and V. Cerqueira, ‘‘Automated imbalanced classification via
[32] H.Zhang,H.Zhang,S.Pirbhulal,W.Wu,andV.H.C.D.Albuquerque, meta-learning,’’ExpertSyst.Appl.,vol.178,Sep.2021,Art.no.115011.
‘‘Active balancing mechanism for imbalanced medical data in deep [56] S. Gholampour, ‘‘Impact of nature of medical data on machine and
learning–basedclassificationmodels,’’ACMTrans.MultimediaComput., deep learning for imbalanced datasets: Clinical validity of SMOTE is
Commun.,Appl.,vol.16,no.1s,pp.1–15,Jan.2020. questionable,’’Mach.Learn.Knowl.Extraction,vol.6,no.2,pp.827–841,
| [33] S.Ayoub,Y.Gulzar,J.Rustamov,A.Jabbari,F.A.Reegu,andS.Turaev, |     |     |     |     |     |     | Apr.2024. |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
‘‘Adversarialapproachestotackleimbalanceddatainmachinelearning,’’ [57] S.Riyanto,I.S.Sitanggang,T.Djatna,andT.D.Atikah,‘‘Comparative
Sustainability,vol.15,no.9,p.7097,Apr.2023. analysisusingvariousperformancemetricsinimbalanceddataformulti-
[34] J.Zheng,X.Wang,D.Wei,B.Chen,andY.Shao,‘‘Anovelimbalanced classtextclassification,’’Int.J.Adv.Comput.Sci.Appl.,vol.14,no.6,
| ensemblelearninginsoftwaredefectpredication,’’IEEEAccess,vol.9, |     |     |     |     |     |     | pp.1–9,2023. |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
pp.86855–86868,2021. [58] J. T. Hancock, T. M. Khoshgoftaar, and J. M. Johnson, ‘‘Evaluating
[35] S.H.Khan,M.Hayat,M.Bennamoun,F.A.Sohel,andR.Togneri,‘‘Cost- classifier performance with highly imbalanced big data,’’ J. Big Data,
sensitivelearningofdeepfeaturerepresentationsfromimbalanceddata,’’ vol.10,no.1,p.42,Apr.2023.
| IEEE | Trans. Neural | Netw. | Learn. | Syst., vol. | 29, no. 8, | pp.3573–3587, |     |     |     |     |     |     |
| ---- | ------------- | ----- | ------ | ----------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- |
Aug.2018.
[36] P.Domingos,‘‘MetaCost:Ageneralmethodformakingclassifierscost-
sensitive,’’inProc.5thACMSIGKDDInt.Conf.Knowl.DiscoveryData MANAHELALTALHANreceivedthebachelor’sdegreefromKingKhalid
Mining,Aug.1999,pp.155–164. University (KKU), Abha, Saudi Arabia, in 2022, where she is currently
|              |         |          |     |        |              |             | pursuing | the master’s | degree in | computer    | science. She | was a Cooperator |
| ------------ | ------- | -------- | --- | ------ | ------------ | ----------- | -------- | ------------ | --------- | ----------- | ------------ | ---------------- |
| [37] Z. Ren, | Y. Zhu, | W. Kang, | H.  | Fu, Q. | Niu, D. Gao, | K. Yan, and |          |              |           |             |              |                  |
|              |         |          |     |        |              |             | with the | KKU Computer | Science   | Department, | in 2023.     | Her research     |
J.Hong,‘‘Adaptivecost-sensitivelearning:Improvingtheconvergenceof
intelligentdiagnosismodelsunderimbalanceddata,’’Knowl.-BasedSyst., interestsincludeartificialintelligence,datamining,andmachinelearning,
vol.241,Apr.2022,Art.no.108296. particularlyfocusingonhandlingimbalanceddata.
| [38] S. Saeed | and H. | C. Ong, | ‘‘Performance | of  | SVM with | multiple kernel |     |     |     |     |     |     |
| ------------- | ------ | ------- | ------------- | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- |
learningforclassificationtasksofimbalanceddatasets,’’PertanikaJ.Sci.
Technol.,vol.27,no.1,pp.527–545,2019. ABDULMOHSENALGARNIreceivedthePh.D.
| [39] L. Gao, | L. Zhang, | C. Liu,             | and S. | Wu, ‘‘Handling | imbalanced     | medical     |     |     |        |                 |            |             |
| ------------ | --------- | ------------------- | ------ | -------------- | -------------- | ----------- | --- | --- | ------ | --------------- | ---------- | ----------- |
|              |           |                     |        |                |                |             |     |     | degree | from Queensland | University | of Technol- |
| image        | data: A   | deep-learning-based |        | one-class      | classification | approach,’’ |     |     |        |                 |            |             |
ogy,Australia,in2012.HewasaResearchAsso-
Artif.Intell.Med.,vol.108,Aug.2020,Art.no.101935.
|     |     |     |     |     |     |     |     |     | ciate | with the School | of Electrical | Engineering |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | ------------- | ----------- |
[40] J.Luo,Y.Yuan,andS.Xu,‘‘ImprovingGBDTperformanceonimbalanced
andComputerScience,QueenslandUniversityof
| datasets:         | An empirical | study | of  | class-balanced | loss functions,’’ | 2024, |     |     |                                            |     |     |     |
| ----------------- | ------------ | ----- | --- | -------------- | ----------------- | ----- | --- | --- | ------------------------------------------ | --- | --- | --- |
| arXiv:2407.14381. |              |       |     |                |                   |       |     |     | Technology,in2012.HeiscurrentlyanAssociate |     |     |     |
[41] R.MaryMathewandR.Gunasundari,‘‘Areviewonhandlingmulticlass ProfessorwiththeCollegeofComputerScience,
imbalanced data classification in education domain,’’ in Proc. Int. King Khalid University. His research interests
Conf. Advance Comput. Innov. Technol. Eng. (ICACITE), Mar. 2021, include artificial intelligence, data mining, text
| pp.752–755. |     |     |     |     |     |     |     |     | mining, | machine | learning, information | retrieval, |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --------------------- | ---------- |
[42] R.E.Schapire,‘‘Abriefintroductiontoboosting,’’IJCAI,vol.99,no.999, andinformationfiltering.
pp.1401–1406,1999.
| [43] L. Breiman, | ‘‘Bagging |     | predictors,’’ | Mach. | Learn., | vol. 24, no. 2, |     |     |     |     |     |     |
| ---------------- | --------- | --- | ------------- | ----- | ------- | --------------- | --- | --- | --- | --- | --- | --- |
pp.123–140,Aug.1996.
[44] L.Breiman,‘‘Randomforests,’’Mach.Learn.,vol.45,pp.5–32,Jan.2001. MONIA TURKI-HADJ ALOUANE (Member,
[45] P.Sheng,L.Chen,andJ.Tian,‘‘Learning-basedroadcrackdetectionusing IEEE) received the Ph.D. (Diploma) degree in
|     |     |     |     |     |     |     |     |     | electrical | engineering | and the | National Tenure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------- | --------------- |
gradientboostdecisiontree,’’inProc.13thIEEEConf.Ind.Electron.Appl.
Diplomadegreeintelecommunicationsfromthe
(ICIEA),May2018,pp.1228–1232.
|     |     |     |     |     |     |     |     |     | National | Engineering | School | of Tunis (ENIT), |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ---------------- |
[46] J.Chung,J.Zhang,A.I.Saimon,Y.Liu,B.N.Johnson,andZ.Kong,
‘‘Imbalanced spectral data analysis using data augmentation based on in 1997 and June 2007, respectively. She is
thegenerativeadversarialnetwork,’’Sci.Rep.,vol.14,no.1,p.13230, currentlyaProfessorwiththeCollegeofComputer
| Jun.2024. |     |     |     |     |     |     |     |     | Science, | King Khalid | University, | Saudi Arabia. |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ----------- | ------------- |
[47] H. Wang, A. Singhal, and P. Liu, ‘‘Tackling imbalanced data in InSeptember1997,shewasrecruitedasanAssis-
cybersecuritywithtransferlearning:AcasewithROPpayloaddetection,’’ tantProfessorofelectricalengineeringwithENIT,
Cybersecurity,vol.6,no.1,p.2,Jan.2023.
whereshewaspromotedtoanAssociateProfessoroftelecommunications,
[48] H.Shamsudin,U.K.Yusof,Y.Haijie,andI.S.Isa,‘‘Anoptimizedsupport
|     |     |     |     |     |     |     | in December | 2007. | From 2010 | to 2012, | she was a | Visiting Associate |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------- | -------- | --------- | ------------------ |
vectormachinewithgeneticalgorithmforimbalanceddataclassification,’’
|     |     |     |     |     |     |     | Professor | with the | Electricity Department, |     | Polytechnic | School of Tunisia |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ----------------------- | --- | ----------- | ----------------- |
JurnalTeknologi,vol.85,no.4,pp.67–74,Jun.2023. (EPT). Since 2012, she has been a Full Professor of telecommunications
[49] N.V.Chawla,A.Lazarević,L.Hall,andK.W.Bowyer,‘‘SMOTEBoost:
withtheInformationandCommunicationTechnologies(ICT)Department,
Improvingpredictionoftheminorityclassinboosting,’’inProc.7thEur.
ENIT.Shehascoordinatedinternationallysponsoredresearchprojects.Since
| Conf. | Knowl. Discovery |     | Databases, | Cavtat-Dubrovnik, |     | Croatia. Cham, |     |     |     |     |     |     |
| ----- | ---------------- | --- | ---------- | ----------------- | --- | -------------- | --- | --- | --- | --- | --- | --- |
1997,shehasbeenleadingmorethan20researchmaster’sthesesandeight
Switzerland:Springer,Jan.2003,pp.107–119.
Ph.D.theses.Shehaspublishedmorethan70papersinimpactedjournalsand
| [50] C. Seiffert, | T.  | M. Khoshgoftaar, |     | J. Van | Hulse, and | A. Napolitano, |     |     |     |     |     |     |
| ----------------- | --- | ---------------- | --- | ------ | ---------- | -------------- | --- | --- | --- | --- | --- | --- |
‘‘RUSBoost: A hybrid approach to alleviating class imbalance,’’ IEEE conferences.Herresearchinterestsincludesignalprocessing(speech,image,
Trans.Syst.,Man,Cybern.,A,Syst.Hum.,vol.40,no.1,pp.185–197, andvideo),machinelearning,deeplearning,andevolutionaryalgorithms.
Jan.2010.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 13699 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |