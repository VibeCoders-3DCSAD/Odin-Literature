---
conversion_metadata:
  converted_at: "2026-07-21T13:49:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Kim K. et al.pdf"
  source_pdf_sha256: "bf7eb1903c110c2015fdca10f3c1c4d6e6d3ab87d20d42e06e2c150c97261660"
  page_count: 15
  markdown_char_count: 131052
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Received 18 December 2024, accepted 6 January 2025, date of publication 13 January 2025, date of current version 23 January 2025.

Digital Object Identifier 10.1109/ACCESS.2025.3529023

RFMVDA: An Enhanced Deep Learning Approach
for Customer Behavior Classification in
E-Commerce Environments

KWANHEE KIM 1, MINGYU JO 1, (Graduate Student Member, IEEE),
ILKYEUN RA 2, (Member, IEEE), AND SANGOH PARK 1, (Member, IEEE)
1School of Computer Science and Engineering, Chung-Ang University, Seoul 06974, South Korea
2Department of Computer Science and Engineering, University of Colorado Denver, Denver, CO 80204, USA

Corresponding author: Sangoh Park (sopark@cau.ac.kr)

This work was supported in part by the Korea Institute for Advancement of Technology (KIAT), Korean Government [Ministry of Trade,
Industry and Energy (MOTIE)] (Human Resource Development (HRD) Program for Industrial Innovation) under Grant P0020632; and in
part by the Chung-Ang University Research Scholarship Grants in 2023.

ABSTRACT Customer Relationship Management (CRM) systems, widely used in enterprises, have
evolved into Software-as-a-Service (SaaS) platforms. With the advent of Customer Data Platforms (CDP),
these systems continuously store customer behavior data for purposes such as creating single customer
profiles, analyzing, tracking, and managing customer interactions from various perspectives. With the global
expansion of the e-commerce market, research on customer analysis and classification optimized for the
e-commerce environment has been actively conducted. The RFM (Recency, Frequency, Monetary) model
is a straightforward method for classifying customers and is applied across various industries. However,
in the e-commerce environment, where customers can access services at any time, there are limitations in
collecting, storing, and reflecting customer behavior data for classification. To resolve these limitations,
this paper proposes the RFMVDA (Recency, Frequency, Monetary, Visits, Durations, Actions) model. This
model is designed to capture customer data, sessions, and behavior units suitable for the e-commerce
environment. By utilizing the RFMVDA model for customer behavior-based segmentation and classification,
we constructed a Deep Neural Network (DNN) to predict customer behavior-based classifications. As a
result, the proposed model demonstrated a segmentation prediction accuracy of 92.98% for customers in the
e-commerce environment.

INDEX TERMS Customer segmentation, customer classification, machine learning, deep neural network
(DNN), customer data platform (CDP), customer relationship management (CRM).

I. INTRODUCTION
As computing power has increased, big data and Artificial
Intelligence (AI) have become integral to our daily lives.
With advancements in big data processing technologies,
various industries have increasingly adopted methods for
data storage and management. According to global market
research firm IDC, the volume of data is expected to grow
from 33ZB in 2018 to 172ZB by 2025, with an annual
growth rate of 61% [1]. Many companies have seen an
accelerated growth in digital business and data complexity,

The associate editor coordinating the review of this manuscript and

approving it for publication was Yiqi Liu

.

leading to a high demand for data ETL (Extract, Transform,
Load) processes across various industries. This has resulted
in the widespread use of big data platforms for storing
and managing domain-specific data [2]. Companies use
Customer Relationship Management (CRM) software to
handle complex and diverse data. CRM systems perform
ETL on customer data and maintain this information over
long periods for business management purposes. CRM is
crucial for managing customer interactions, enhancing sales,
creating value, and personalizing products and services [3],
[4], [5], [6], [7]. Recently, companies have begun using
Customer Data Platforms (CDP)
to continuously store
information about customers who access their services and

VOLUME 13, 2025

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
For more information, see https://creativecommons.org/licenses/by/4.0/

12527

---

<!-- PAGE 2 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

websites. These platforms allow for the creation, tracking,
and management of single customer profiles, analyzing
customer behavior from various perspectives [8]. Various
studies on customer segmentation have been conducted using
the collected customer data. A representative method for
customer segmentation is the RFM (Recency, Frequency,
Monetary) model [9], [10], [11]. Companies use the RFM
model
thereby enabling
targeted marketing and promotions to encourage repeat visits
or purchases. The RFM model categorizes customers based
on recency, frequency, and monetary value of purchases [12].
However, the traditional RFM model has significant lim-
itations, especially in the context of modern e-commerce
environments.

to classify existing customers,

Firstly, the traditional RFM model is only capable of
classifying customers who have made a purchase. It does
not account for customers who visit a store or platform
without making a purchase, thereby overlooking a significant
segment of customer interactions. Secondly, the RFM model
is traditionally applied in offline retail environments where
customer interactions are bound by store hours, and the
data collected is limited to those specific timeframes. This
approach is inadequate for e-commerce, where customer
interactions are continuous and can occur at any time. Thirdly,
the RFM model is not optimized for online e-commerce
platforms. In e-commerce, customers engage in various
activities beyond just purchasing, such as browsing, adding
items to carts, and spending time on specific product pages.
These activities form a crucial part of the customer journey,
which the RFM model fails to capture.

To address these challenges,

this paper proposes the
RFMVDA (Recency, Frequency, Monetary, Visits, Dura-
tions, Actions) model, which extends the traditional RFM
model by incorporating additional dimensions that are
crucial for capturing customer behavior in e-commerce
environments. The RFMVDA model introduces three new
attributes—Visits, Durations, and Actions—allowing for
a more comprehensive analysis of customer interactions.
By integrating these additional behavioral dimensions,
the RFMVDA model not only enhances the granularity
of customer segmentation but also makes it possible to
classify customers based on their entire journey on an
e-commerce site, including those who do not complete a
purchase. This approach ensures that businesses can gain a
deeper understanding of both purchasing and non-purchasing
behaviors, enabling more effective and targeted marketing
strategies.

Furthermore, we have chosen to implement a Deep Neural
Network (DNN) model
to process the high complexity
and volume of data associated with e-commerce platforms.
DNNs are particularly well-suited for this task due to their
ability to model complex patterns and interactions within
large datasets, making them ideal for customer classification
tasks that
involve multiple behavioral dimensions. The
contributions of this research lie in the development of the
RFMVDA model and the application of DNN for enhanced

customer classification, both of which significantly improve
upon traditional methods.

The structure of this paper is as follows: Section II
introduces concepts for customer segmentation and related
studies on customer behavior and purchase prediction
in the e-commerce environment. Section III proposes
for customer behavior data in
the RFMVDA model
e-commerce,
including segmentation for non-purchasing
customers. Section IV evaluates and analyzes the learning
accuracy and prediction accuracy for customer behavior clas-
sification using the proposed DNN model. Finally, Section V
provides conclusions and future research directions.

II. RELATED WORK
The RFM (Recency, Frequency, Monetary) model is one of
the most widely used methods for customer segmentation
and analysis in marketing. It simplifies the classification of
customers based on three criteria, making it an effective
tool for marketing applications. The RFM model has been
employed in industries for over 30 years as a direct marketing
approach and remains widely used due to its ease of
implementation. Companies use the RFM model to classify
customers into categories such as loyal customers, potential
customers, and lost customers,
thereby gaining insights
into consumer loyalty and relationships with the company’s
products [11]. The RFM model ranks customers based on the
recency, frequency, and monetary value of their purchases,
converting this information into a two-dimensional data
format. Subsequent clustering algorithms like K-means and
fuzzy inference are then applied to segment customers [13],
[14], [15]. The LRFM model extends the RFM model by
adding a Length factor, representing the time span between
the first and last purchases [10]. This model measures the
purchase cycle of customers, enabling further segmentation
into core customers, potential customers, lost customers, and
new customers based on the Length attribute.

In the e-commerce environment, customer segmentation
and purchase prediction research often utilize Recurrent
Neural Networks (RNN) and Long Short-Term Memory
(LSTM) networks to learn customer behavior and predict
purchase likelihood [16], [17]. Studies combining LSTM
with Random Forest (RF) algorithms analyze customers’
time to
purchasing activities and access patterns over
predict consumer behavior. These models input customer
behavior and purchase history into an LSTM-RF model,
producing purchase probability outputs through a Fully
Connected Layer [18]. Although LSTM-RF models have
shown high performance in predicting customer purchases
in e-commerce, they mainly focus on customers who have
made purchases,
thus limiting their ability to classify
non-purchasing user behaviors.

The Self-Organizing Neural Network (SONN) employs
deep learning for customer segmentation in digital marketing
within the e-commerce environment [19]. This unsupervised
learning model clusters customer data using the RFM
model, SOM (Self-Organizing Map), and DNN (Deep Neural

12528

VOLUME 13, 2025

---

<!-- PAGE 3 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

FIGURE 1. Flow diagram of customer information, session, and behavior unit data modeling.

Network). The SONN model classified 4,372 customers
into five segmented groups with an accuracy of 98%.
SONN’s ability to generate two-dimensional data clusters
allows for easy identification of relationships and patterns
the results can vary depending
in the data. However,
on the similarity and distance functions used, increasing
model complexity. Moreover, SONN primarily considers
purchase data for customer classification, excluding factors
like access environment, behavior data, dwell time, and
purchased products, which are essential for behavior-based
segmentation in the e-commerce environment.

Recent studies have further explored the application
of machine learning techniques for client segmentation
in e-commerce settings. For instance, Banerjee and col-
leagues [20] examined AI-driven approaches for cus-
tomer profiling, segmentation, and sales prediction in
direct marketing. Their research highlights how integrat-
ing AI
techniques can improve segmentation accuracy
and predict sales trends, thereby significantly enhancing
personalized marketing strategies. Similarly, Sriprasadh and
co-authors [21] investigated the use of various machine learn-
ing algorithms for client segmentation and customization
within e-commerce environments. Their approach included
data preprocessing using Python’s TensorFlow and Pandas
libraries, followed by the application of clustering models
such as K-means, DBSCAN, and Agglomerative Clustering.

The study achieved an accuracy of approximately 93%
in identifying target customer segments, underscoring the
potential of these techniques to enhance customer segmen-
tation strategies and enable more effective personalized
marketing. Additionally, Vijai et al. [22] applied a range
of machine learning algorithms, including clustering and
predictive modeling techniques, for customer segmentation
in e-commerce management. Their study emphasizes the
critical role of personalized marketing strategies tailored to
distinct customer segments.

These advancements highlight the ongoing evolution of
customer segmentation techniques, particularly in adapting
traditional models to the complexities of the e-commerce
environment.

III. ECBC (EFFICIENT CUSTOMER BEHAVIOR
CLASSIFICATION)
A. CUSTOMER DATA MODELING
This paper collects various customer behavior data (such
as access information, webpage visits, dwell
time, and
device usage) in the e-commerce environment and uses it
to segment customers through machine learning techniques.
Customer data is modeled into three main components:
customer information, sessions, and behaviors. Based on this
model, the data is transformed into attributes necessary for
customer segmentation in the proposed RFMVDA (Recency,

VOLUME 13, 2025

12529

---

<!-- PAGE 4 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 1. Definition of RFMVDA attributes.

TABLE 2. Definition of VDAR attributes.

Frequency, Monetary, Visits, Durations, Actions) model. This
transformed data is used to classify and segment customers
using machine learning models and Deep Neural Networks
(DNNs) designed for the e-commerce environment. When
a customer accesses a specific e-commerce platform or
website, information such as the entry channel (various
search engines, advertisements, etc.), device, region, country,
and time is transmitted to and stored on the server. This
information is contained in web access information headers,
which are standardized by web protocols. All information
about customer behaviors and transaction histories from
the moment they enter the e-commerce environment until
they leave is stored on the server. The stored customer
information is categorized into three data models: customer
information model, session model, and behavior unit model,
as shown in Figure 1. The customer information model
records basic identification data of the customer accessing
the e-commerce platform, including device, region, browser,
and operating system data. This model is updated each
time the customer accesses the website, storing changes
in the user’s access environment in real-time. The session
model comprehensively records customer behavior during
their stay on the website. It includes information about each
session generated when the customer visits the site, such
as start time, end time, and page sequence, to store data
on the customer’s e-commerce site activities. This data is
used to analyze detailed information such as which products
the visitor showed interest in and which pages they spent
more time on. The behavior unit model stores specific
behavior information during the customer’s journey on the
site. It segments and stores actions such as each page view,
number of clicks, cart additions, and purchase activities,
which are essential for subsequent customer segmentation.
The unique ID assigned to the customer links the session
model and individual behavior units, storing interactions
related to customer preferences, interests, and purchasing
tendencies. This model integrates with the session model,
connecting all behavior units occurring in each session into a
single session.

B. RFMVDA SEGMENTATION MODEL (PURCHASING
CUSTOMER SEGMENTATION)
Customers generally access various pages when they visit
an e-commerce platform. In the case of a shopping mall’s
e-commerce site, customers tend to browse detailed informa-
tion about products and contemplate making purchases.

Consequently, they spend time on the product detail pages,
increasing their dwell time on the e-commerce website.
To classify customers in the e-commerce environment, the
RFMVDA (Recency, Frequency, Monetary, Visits, Durations,
Actions) model adds three attributes—visits, durations, and
actions—to the traditional RFM model, resulting in a total of
six attributes, as shown in Table 1. Customers tend to spend
time on product detail pages while comparing products of
interest. When customers view or purchase products on an
e-commerce platform, the number of visits to the shopping
mall’s e-commerce site increases. Additionally, if customers
are satisfied with the purchased products, they will continue
to access the e-commerce site to browse or purchase other
products. Therefore, the number of visits is a crucial attribute
for classifying customers in the e-commerce environment.
If a customer decides that the content of the shopping mall’s
e-commerce website is unnecessary, the time they spend
viewing the detail pages will decrease. For instance, if a
customer accesses the e-commerce site via a search engine
using the keyword ‘‘60-inch TV,’’ it is highly likely that the
customer is interested in purchasing a product related to the
keyword. The customer will browse the products of interest or
comparable products on the e-commerce site and spend time
on the detail pages. Hence, the total dwell time is an essential
indicator of the customer’s decision to purchase a product.
Lastly, the action attribute reflects customer behavior such as
repetitive page views and adding products to the cart. These
actions indicate satisfaction with the purchased products,
leading to continuous access to the site to browse or purchase
other products. Therefore, the total number of visits, total
dwell time, and total purchase actions are critical indicators
for customer classification in the e-commerce environment.

C. VDAR SEGMENTATION MODEL (NON-PURCHASING
CUSTOMER SEGMENTATION)
Traditional RFM models are limited in that they primar-
ily focus on segmenting customers based on purchasing
leaving non-purchasing customers unanalyzed.
behavior,
However, in e-commerce environments, customers can freely
access the site at any time to browse products without
necessarily making a purchase. Unlike physical stores, where
it is difficult to track non-purchasing customers’ activities,
e-commerce platforms can capture and model a wide range
of behavioral data, regardless of whether the customer makes
a purchase.

To address the gap in customer segmentation for non-
purchasing customers, this study proposes the VDAR (Visits,

12530

VOLUME 13, 2025

---

<!-- PAGE 5 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

FIGURE 2. DNN Configuration for customer classification.

Durations, Actions, Referral Keyword) model. The VDAR
model classifies customers based on four key attributes:
Visits, Durations, Actions, and Referral Keyword, as sum-
marized in Table 2. These attributes enable the model to
assess customer engagement by analyzing their site visit
frequency, session duration, behavioral patterns, and their
referral sources before landing on the e-commerce site.

For instance, consider a customer who accessed the
e-commerce site after searching for ‘‘60-inch TV’’ on a
search engine. This customer is likely to have a high interest
in purchasing a television or gathering information about
similar products. The customer may browse various product
models, read reviews, and compare prices, leading to an
increase in their total session duration and page views. If the
product details and pricing meet their expectations, they may
revisit the site more frequently, and their visit count and
page view count would naturally increase. Additionally, the
referral keyword attribute provides insight into the customer’s
intent based on the search terms they used before landing on
the e-commerce site.

The VDAR model’s classification of non-purchasing
customers, based on their behavioral attributes, is crucial

for companies aiming to derive actionable insights from
customer activities beyond purchase behavior. This model
helps marketers and decision-makers identify customers who
are in the consideration phase, allowing them to tailor targeted
marketing strategies that could lead to future purchases.
For example,
if a promotion generates high site traffic
but low engagement in terms of page views and session
durations, it could indicate that the products or content may
not be resonating with the audience, providing valuable
feedback for future optimizations. Therefore, the VDAR
model enables the segmentation of non-purchasing customers
based on their behavioral data and serves as a key tool for
improving overall marketing efficiency and driving data-
driven decision-making in e-commerce businesses.

Furthermore, by applying the VDAR model, businesses
can better understand and respond to the entire customer
journey on e-commerce platforms. This model not only
captures purchase-related behavior but also provides insights
into the broader context of user interactions,
including
those that do not result in immediate transactions. This
comprehensive approach allows companies to tailor their
strategies to engage potential customers more effectively

VOLUME 13, 2025

12531

---

<!-- PAGE 6 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 3. Definition of input layer parameters.

throughout their online journey, from initial site visits to
eventual purchases.

D. DNN CONFIGURATION FOR CUSTOMER
CLASSIFICATION
The customer data accessed in the e-commerce environment
is processed and normalized according to the RFMVDA
model, and a neural network is constructed to classify
customers. The configuration of the DNN is shown in
Figure 2. The input layer consists of N data points from
the customer’s session model. The hidden layer is composed
of
two layers, each connected by neurons. The input
data is passed to the hidden layers, with the first hidden
layer consisting of 128 neurons activated by the ReLU
activation function. The second hidden layer also consists of
128 neurons, connected by the sigmoid activation function.
Finally, the output layer receives the final result.

We selected a Deep Neural Network (DNN) for this task
due to its ability to model complex relationships within large
datasets, which are common in e-commerce environments.
DNNs excel at capturing intricate patterns and dependencies
in data, making them particularly suitable for tasks such as

customer classification, where numerous behavioral factors
must be considered simultaneously. Furthermore, DNNs can
efficiently handle the high dimensionality and volume of data
associated with the RFMVDA model, ensuring robust and
accurate predictions.

The deep learning model is trained to predict values as
close as possible to the actual values by calculating the error
loss when the predicted value differs from the actual value
during forward propagation. Various loss functions exist, with
binary cross-entropy used when the output values are 0 or
1. However, this is not suitable for multi-class classification
where there are more than two classes.

L = −

1
N

N
X

C
X

i=1

j=1

tij log(yij)

(1)

Categorical cross-entropy is used for multi-class clas-
sification problems, as indicated by Equation (1), where
C represents the number of classes. Therefore, this paper
employs categorical cross-entropy as the loss function
since the classification model is trained on data consisting
of 15 different categories for purchasing customers and
9 different categories for non-purchasing customers. Finally,

12532

VOLUME 13, 2025

---

<!-- PAGE 7 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 4. Composition of the performance evaluation dataset.

TABLE 5. Customer segmentation results using LRFM model.

a DNN is constructed, as shown in Figure 2, to standardize
and train the RFMVDA data model.

E. INPUT LAYER PARAMETERS FOR DNN
The parameters of the data model used in the input layer of the
DNN are configured as shown in Table 3. These parameters
include 14 customer data points and 15 session data points,
totaling 29. These parameters serve as essential input data
for customer classification and behavior prediction through
the DNN. Each time a customer accesses the e-commerce
website, a unique session identifier is created. During the
session, if the customer browses various product pages and
makes purchases, data such as the session’s dwell time, total
number of actions, total purchase quantity, and total purchase
amount is stored. When the customer exits the e-commerce
website, the session information in the customer data model
is updated with the final actions taken by the customer. This
process of storing and compiling customer actions from the
moment they access the website until they exit provides the
29 parameters, which are then used to train the DNN.

IV. PERFORMANCE EVALUATION
A. DATASET
The dataset used in this study is based on real customer
data collected from an e-commerce website in South Korea.
This dataset spans a 3-month period from January 1, 2022,
to March 31, 2022, and includes information on a total of
9,416 registered customers. Among these, 5,041 customers
visited the website, and 299 completed a purchase. The
dataset includes various data such as customer registration
details, website visit logs, session information from each
there are
visit, and customer activity records. In total,

37,698 customer sessions and 405,280 customer activity data
points. The dataset primarily contains variables for analyzing
customer behavior, including visit time, page views, cart
additions, and product purchases, as summarized in Table 4.
These behaviors were the focus of analysis and were used
to evaluate the proposed RFMVDA model, as well as to
compare it against the LRFM model.

The raw data collected from the e-commerce environment
contains unstructured data that requires refinement and
preprocessing for analysis. Initially, irrelevant features and
missing data were removed, followed by normalization of
the data into a suitable format for analysis. Given the diverse
distribution of customer behavior data, each variable’s values
were scaled between 0 and 1 to facilitate input into the model.
Throughout this process, the RFMVDA model was con-
structed to analyze each customer’s behavior pattern in detail.
This model includes six key variables: Recency, Frequency,
Monetary, Visits, Durations, and Actions. For the purposes
of model training and testing, the dataset was split into two
sets: 70% was used for training, while the remaining 30% was
reserved for testing.

B. CUSTOMER SEGMENTATION BASED ON LRFM MODEL
The LRFM model was applied to analyze purchasing
customer behavior patterns and to categorize customers into
four segments. This model assigns scores to each customer
based on four factors: Length (the time between the first
and most recent purchase), Recency (the time since the most
recent purchase), Frequency (the number of purchases), and
Monetary (the total amount spent). Using these four elements,
the customers were classified into specific segments.

VOLUME 13, 2025

12533

---

<!-- PAGE 8 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 6. Final customer segmentation applied using the RFMVDA model.

Table 5 shows the customer segmentation after applying
the LRFM model. A total of 299 customers were classified
into four primary segments: VIP Customers, Potential
Loyal Customers, Regular Customers, and Lost Customers.
Each segment was determined by factors such as purchase
frequency, the recency of purchases, total monetary value,
and the length of time from the first visit to the purchase.

The VIP customers account for 30% of the total 299 cus-
tomers. These customers recently made frequent purchases
with high monetary value and are considered very important.
On the other hand, the Lost Customers group comprises
47% of the total customers. This group requires further
customer relationship management strategies to either retain
or reactivate them. The VIP Customers group maintains
recent and frequent purchases with high spending, placing
the top of the LRFM model’s scoring. These
them at
customers represent a loyal base for the business, and
offering special promotions or benefits can maximize reten-
tion and engagement. Potential Loyal Customers, although
having lower purchase frequency and spending than VIP
customers, have still made recent purchases and hold the
potential to be converted into VIP Customers. They are
a key target for additional marketing strategies aimed at
customer conversion. Regular Customers are those with lower
purchase frequency but consistent business engagement.
Custom marketing strategies can be applied to reinforce their
buying patterns and encourage more frequent purchases. Lost
Customers are those who have not made recent purchases and
exhibit low frequency and spending patterns. This segment
requires targeted remarketing campaigns or incentives to
encourage repurchases and re-engagement with the business.
Although the LRFM model successfully segmented cus-
tomers based on their purchasing behavior, it has certain
limitations, particularly in the e-commerce environment. This
model fails to account for the activities of customers who
have not made any purchases. For instance, even if customers
visit the site and engage in various activities, if they do not

make a purchase, the LRFM model does not capture this
behavior. Thus, a more comprehensive model that includes
non-purchasing customers is needed.

Additionally, the model does not fully reflect all customer
access activities in the e-commerce environment. Since
customers can engage in a variety of actions at any time, it is
critical to evaluate the potential likelihood of these actions
leading to purchases. To overcome these limitations, it is
necessary to develop an expanded model that can analyze
a broader range of customer access patterns and behavioral
data.

C. CUSTOMER SEGMENTATION BASED ON THE RFMVDA
MODEL
The RFMVDA model extends the traditional LRFM frame-
work to enhance the granularity of customer behavior
analysis and segmentation in the e-commerce environment.
In addition to the standard Recency (R), Frequency (F), and
Monetary (M) dimensions, the RFMVDA model introduces
three additional variables—Visits (V), Durations (D), and
Actions (A). These supplementary dimensions enable a
more comprehensive and detailed analysis of customer
behavior across a broader spectrum of interactions within the
e-commerce platform.

Unlike traditional models that focus primarily on purchase
history,
the RFMVDA model provides a more holistic
view by incorporating various online activities. This allows
for a richer segmentation of customers based on their
engagement with the platform,
taking into account not
only their purchasing behavior but also metrics such as
visit frequency, time spent on pages, and specific actions
performed on the site. To ensure that each behavioral
dimension contributes equally to the analysis,
the data
for each variable is normalized using Min-Max scaling
to map the values between 0 and 5. This standardization
enables the model to treat all behavioral attributes with

12534

VOLUME 13, 2025

---

<!-- PAGE 9 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 7. Detailed customer segmentation transition from LRFM to RFMVDA model.

equal importance, thereby providing a balanced evaluation of
customer engagement.

Through the application of the RFMVDA model, cus-
tomers were classified into 14 distinct segments, as shown
in Table 6. This segmentation approach offers a significantly
more nuanced classification compared to the traditional
LRFM model, as it accounts for a wider range of customer
behaviors. The RFMVDA model not only considers purchas-
ing habits but also integrates data on overall site interactions,
providing a more detailed and accurate reflection of customer
behavior patterns.

This refined segmentation captures the complexity of
customer interactions within the e-commerce environment.
The RFMVDA model offers a more precise categorization
by considering both purchase history and diverse behavioral
metrics, thereby allowing businesses to better tailor their
marketing strategies and customer relationship management
efforts.

D. COMPARATIVE ANALYSIS OF LRFM AND RFMVDA
MODELS
The segmentation results of 299 customers who made
purchases in the e-commerce environment were compared
using both the LRFM and RFMVDA models. The LRFM
model classifies customers into four simple segments: VIP
Customers, Potential Loyal Customers, Regular Customers,
and Lost Customers. In contrast,
the RFMVDA model
is designed to account for various customer behaviors in
the e-commerce environment by incorporating not only

purchasing behavior but also variables such as Visits,
Durations, and Actions,
leading to the segmentation of
customers into 14 detailed categories.

1) COMPARISON OF CUSTOMER SEGMENTATION RESULTS
The LRFM model, based on relatively simple metrics, is use-
ful for identifying key customer groups but has limitations in
fully reflecting the complex user behavior patterns found in
dynamic online environments like e-commerce. For example,
in the LRFM model, 140 customers were classified as Lost
Customers due to a significant decrease in their purchase
frequency or length attributes, even though they may have
completed purchases during other periods. In the LRFM
model, ‘lost customers’ specifically refer to those whose
purchasing activity has declined significantly within the
defined analysis period, rather than customers who have
never made a purchase at any point.

In contrast, the RFMVDA model considers additional
variables such as visit frequency, session duration, and action
counts to further segment these customers into categories
such as About to Sleep Customers, At Risk Customers, and
About to Leave Customers. This approach allows for a more
detailed classification of customers, identifying early signs of
churn that the LRFM model may overlook.

2) MODEL COMPARISON ANALYSIS
The LRFM model is useful for providing a simple customer
classification based on purchasing data. However, it falls
short of reflecting comprehensive online behavior data.

VOLUME 13, 2025

12535

---

<!-- PAGE 10 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 8. Detailed customer segmentation based on VDAR model.

In contrast, the RFMVDA model provides the ability to seg-
ment customers by incorporating multidimensional behav-
ioral data from the e-commerce environment. By including
non-purchase activities, such as visit frequency, duration,
and action counts,
the RFMVDA model offers a more
complete evaluation of customer engagement, allowing for
more accurate predictions of potential customer churn.

For example, as shown in Table 7, 16 of the 140 customers
categorized as Lost Customers in the LRFM model were
reclassified as Potential Loyal Customers in the RFMVDA
model due to the inclusion of visit frequency and site activity
data. This highlights the ability of the RFMVDA model to
create more precise and effective customer segmentation,
allowing businesses to implement more detailed CRM
strategies. By identifying customers who show early signs of
churn, targeted marketing and reactivation campaigns can be
launched to improve customer retention.

In conclusion, the RFMVDA model is better suited for the
e-commerce environment as it incorporates a broader range
of behavioral data, making it a powerful tool for preventing
customer churn and developing effective marketing strategies
that target various customer segments based on their detailed
behavior profiles.

E. BEHAVIORAL SEGMENTATION OF NON-PURCHASING
CUSTOMERS USING THE VDAR MODEL
As shown in Table 8, the VDAR model was applied to seg-
ment non-purchasing customers who visited the e-commerce
platform during the study period from January to March
2022. Of the 5,041 total visitors, 4,742 customers did not
complete a purchase. The VDAR model enabled a detailed
segmentation of these non-purchasing customers, taking into
account their behavioral data such as total visits (Visits),
total dwell time (Durations), total actions (Actions), and the
presence of referral keywords (Referrer).

The analysis revealed that approximately 36% (1,711
customers) of the non-purchasing customers fell into the
top four segments most
to purchasing
customers. These segments include customers who are likely
to purchase soon and customers showing high engagement
with the content on the site, such as viewing multiple

likely to convert

FIGURE 3. Repeated stratified K-Fold cross validation results.

products or spending significant time on product detail pages.
Additionally, 1,097 customers (22%) demonstrated a keen
interest in various products, indicating strong potential for
future purchases. However, 1,902 customers (40%) were
classified in the lower engagement segments, indicating a
higher risk of disengagement or abandonment.

Marketers and decision-makers can utilize this segmenta-
tion to develop personalized promotional strategies aimed at
converting the top segments into first-time buyers. By target-
ing the 1,711 customers in the higher engagement segments
the e-commerce
with tailored promotions and coupons,
platform can potentially increase its conversion rate and
revenue.

In summary,

the VDAR model successfully segments
non-purchasing customers into distinct groups, helping
e-commerce businesses identify potential first-time buyers
and customers who may need further engagement. This
segmentation is particularly valuable for targeting promo-
tional efforts and optimizing marketing strategies based on
customer behavior insights.

F. PREDICTION OF CUSTOMER SEGMENTATION USING
NEURAL NETWORKS
1) MODEL VALIDATION USING REPEATED STRATIFIED
K-FOLD CROSS VALIDATION
To ensure the robustness and reliability of the proposed
RFMVDA model, we employed the Repeated Stratified
K-Fold Cross Validation method, which is particularly

12536

VOLUME 13, 2025

---

<!-- PAGE 11 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

suitable for classification tasks. This technique involves per-
forming multiple iterations of cross-validation with different
shuffles of the data, which helps in assessing the model’s
performance more comprehensively.

For this validation, the RepeatedStratifiedKFold
function from the sklearn library was used, as it
is
designed for classification models. This method allowed for
a detailed evaluation of how well the model generalizes to
unseen data, beyond the initial training set.

As shown in Figure 3, the cross-validation results indicate
an average accuracy of 96.9%, which confirms the model’s
strong generalization capability across different data folds.

2) EXPLORATION OF DIFFERENT DNN ARCHITECTURES AND
HYPERPARAMETERS
In order to optimize the model’s performance and address
potential overfitting risks, we explored various DNN archi-
tectures and hyperparameters. The experiments involved
tuning different configurations, such as the number of
layers, the number of neurons per layer, activation functions,
learning rates, batch sizes, and dropout rates.

To systematically evaluate these configurations, we uti-
lized a hyperparameter grid search in combination with
repeated stratified K-fold cross-validation. The grid search
was configured as follows:

param_grid = {

’layers’: [[128], [64, 64], [128, 128]], #

Layer configurations

’activation’: [’relu’, ’sigmoid’],

Activation functions
’optimizer’: [’adam’, ’sgd’],

Optimizers

’dropout_rate’: [0.0, 0.2, 0.5],

Dropout rates

’batch_size’: [32, 64],

Batch sizes

’epochs’: [50, 100, 200]
Number of epochs

}

#

#

#

#

#

# Repeated Stratified \text{K-Fold} Cross

Validation setup

rskf = RepeatedStratifiedKFold(n_splits=3,

n_repeats=1, random_state=42)

# GridSearchCV setup and model training
grid = GridSearchCV(estimator=model, param_grid=

param_grid, n_jobs=-1, cv=rskf)

grid_result = grid.fit(x_data, y_data_encoded)

# Output the best score and corresponding

parameters

print(‘‘Best Score: {grid_result.best_score_}’’)
print(‘‘Best Params: {grid_result.best_params_}’’)

This approach allowed us to identify the optimal combi-
nation of hyperparameters, which resulted in a best score
of 0.9725614984830221 with the following configuration:
activation function ‘relu’, batch size 32, dropout rate 0.2,
200 epochs, layers [128, 128], and optimizer ‘adam’.

The experimental results provided valuable insights into
the impact of various hyperparameters on the model’s

FIGURE 4. Performance by optimizer.

FIGURE 5. Performance Heatmap: Dropout Rate vs Batch Size.

FIGURE 6. Performance vs. Epochs.

performance. The following figures illustrate the perfor-
mance comparison between different optimizers and dropout
rates:

As shown in Figure 4, the Adam optimizer provided better
average accuracy compared to SGD, making it the preferable
choice for this model.

The heatmap in Figure 5 illustrates the interaction between
dropout rates and batch sizes, with a dropout rate of 0.0 and
a batch size of 32 achieving the highest accuracy.

Finally, Figure 6 depicts the relationship between the
number of epochs and performance, indicating that increasing
the epochs generally improves accuracy, particularly for
deeper networks with more layers.

VOLUME 13, 2025

12537

---

<!-- PAGE 12 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

TABLE 9. Performance metrics for RFMVDA model.

FIGURE 7. Training and Validation Loss: Training (yellow) and validation (blue) loss over 200 epochs using optimal hyperparameters. The
validation loss shows minimal fluctuation, indicating good generalization.

FIGURE 8. Training and Validation Accuracy: Accuracy trends over 200 epochs for training datasets, showing predicted values
closely matching actual values, indicating high performance and minimal overfitting.

3) EVALUATION OF OPTIMAL HYPERPARAMETERS AND
MODEL PERFORMANCE
In the previous sections, we explored various DNN architec-
tures and hyperparameters to determine the optimal settings
for customer segmentation in the e-commerce environment.
After extensive experiments using Repeated Stratified K-Fold
Cross Validation, the optimal configuration was identified as
follows:

• Optimizer: Adam
• Dropout Rate: 0.2
• Batch Size: 32
• Number of Epochs: 200
• Network Architecture: Two hidden layers, each with

128 neurons, using ReLU activation

Using these optimal hyperparameters,

the model was
retrained on 80% of the dataset and tested on the remaining

12538

VOLUME 13, 2025

---

<!-- PAGE 13 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

FIGURE 9. SHAP Feature Importance for Customer Segmentation in DNN Model: (a) Segmentation Distribution by Customer Type,
(b) Overall Feature Impact on Purchasing Customers.

FIGURE 10. Confusion matrix for different training and prediction splits.

20%. As summarized in Table 9, the model achieved a
training accuracy of 99.54% and a prediction accuracy of
92.98%. The trend of training and prediction accuracy over
epochs is depicted in Figure 7, showing consistent accuracy
improvements and demonstrating the model’s robust learning

capacity. Further validation of the model’s performance is
provided in Figure 8, which displays loss and accuracy
metrics during training and testing. These results confirm
minimal overfitting, suggesting that the selected model is
well-suited for this classification task. To understand each

VOLUME 13, 2025

12539

---

<!-- PAGE 14 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

feature’s contribution to the model’s predictions, we analyzed
the importance of individual input features using SHAP
(SHapley Additive exPlanations) values. Figure 9 displays
the average impact of each feature on customer segmentation
outcomes, with session duration, first action time, and the
number of desktop visits identified as the most influential
factors in determining segmentation results.

Additional performance metrics were calculated to offer
a more comprehensive evaluation. Specifically, the RMSE
(Root Mean Squared Error), Macro F1 Score, and Micro
F1 Score were included to provide further insights into
the model’s accuracy and robustness. The RMSE values of
1.6251 for the 70%-30% split and 1.1778 for the 80%-20%
split indicate a low average error magnitude, reflecting high
prediction precision. The Macro F1 Score values (0.877 for
70%-30% and 0.7923 for 80%-20%) demonstrate balanced
performance across classes, while the Micro F1 Score
(0.8870 for 70%-30% and 0.9390 for 80%-20%) underscores
the model’s effectiveness in accurately classifying individual
instances. These metrics are detailed in Table 9.

To further assess the model’s robustness and generalization
capabilities across different data splits, confusion matrices
for the 70%-30% and 80%-20% splits were generated,
as illustrated in Figure 10. The confusion matrix for the
70%-30% split in Figure 10(a) illustrates the distribution
of correct and incorrect classifications across all classes,
identifying areas for potential misclassification. The matrix
for the 80%-20% split in Figure 10(b) shows improved
accuracy with the larger training dataset, resulting in a
more balanced prediction distribution across classes. This
comparison provides valuable insights into the model’s
consistency and robustness under varying data conditions.

In conclusion, the selected DNN architecture and hyper-
parameters have proven effective for accurate customer
segmentation in e-commerce environments. These findings
have practical implications, as they can contribute to refining
marketing strategies and enhancing personalized customer
experiences.

V. CONCLUSION
With the rapid growth of the e-commerce market, traditional
customer classification methods, such as the RFM model,
face limitations in capturing diverse and continuous customer
behaviors. These methods primarily focus on purchasing
customers and fail to analyze visitors who interact with
platforms but do not make purchases. To address these
shortcomings, this paper introduced the RFMVDA (Recency,
Frequency, Monetary, Visits, Durations, Actions) model,
which extends the RFM framework by incorporating behav-
ioral dimensions such as visit frequency, session duration, and
action counts. The RFMVDA model enables a more detailed
and comprehensive understanding of purchasing customer
interactions in dynamic e-commerce environments.

Recognizing the need to analyze non-purchasing cus-
tomers as well,
this study proposed the VDAR (Visits,
Durations, Actions, Referral Keyword) model. Unlike the

RFM-based models that focus solely on transactional data,
the VDAR framework provides valuable insights into
the engagement levels of visitors who do not complete
purchases. By identifying patterns in non-purchasing behav-
iors, such as visit frequency and referral keywords, the
VDAR model enables businesses to uncover opportunities
for re-engagement strategies and better understand early
indicators of potential future conversions.

The performance of the RFMVDA model was validated
using a Deep Neural Network (DNN), achieving a segmenta-
tion prediction accuracy of 92.98% and a training accuracy of
99.54%, as shown in Table 9. Additional metrics, including
RMSE, Macro F1 Score, and Micro F1 Score, further
demonstrated its robustness. SHAP analysis in Figure 9
highlighted the importance of session duration, first action
time, and desktop visits as key features. The confusion
matrices in Figure 10 confirmed the model’s consistency
across varying data splits.

Although the results are promising, this study recognizes
several limitations. The current analysis relies on historical
data collected over a three-month period, which may
not fully capture seasonal or long-term behavioral trends.
To address this constraint, future research will incorporate
data from longer observation windows and multiple e-
commerce platforms, allowing the RFMVDA and VDAR
models to be evaluated under broader and more diverse
conditions.
In addition, direct comparisons with other
machine learning algorithms, such as Random Forests and
Gradient Boosting, were not performed in this study but will
be systematically pursued in future work. By conducting
benchmark experiments under standardized conditions, these
comparative analyses will not only highlight the unique
advantages of the RFMVDA framework but also pinpoint
areas for further refinement, ultimately enhancing its real-
world applicability.

Future research will also investigate how refined segmenta-
tion models like RFMVDA can be quantitatively linked to key
financial metrics, including customer lifetime value, revenue
growth, and retention rates. By examining these relationships
in practical e-commerce environments, we aim to clarify
how enhanced segmentation strategies can drive long-term
profitability and support evidence-based decision-making.
This approach will help businesses allocate resources more
effectively and prioritize customer-centric programs based on
a clear understanding of potential returns.

In conclusion, the RFMVDA and VDAR models, com-
bined with a DNN architecture, represent a significant
advancement
in customer behavior classification for e-
commerce environments. These frameworks address the
limitations of traditional approaches while providing action-
able insights to enhance customer engagement, improve
retention strategies, and support sustainable business growth.
By capturing both purchasing and non-purchasing user
patterns,
interventions
more precisely, ultimately unlocking new opportunities for
personalized marketing and data-driven decision-making.

they enable businesses to tailor

12540

VOLUME 13, 2025

---

<!-- PAGE 15 -->

K. Kim et al.: RFMVDA: An Enhanced Deep Learning Approach for Customer Behavior Classification

REFERENCES
[1] Big Data, Ministry SMEs Startups of the Republic of Korea, Sejong-si,

South Korea, 2022.

[2] J.-G. Lee and M. Kang, ‘‘Geospatial big data: Challenges and opportuni-

ties,’’ Big Data Res., vol. 2, no. 2, pp. 74–81, Jun. 2015.

[3] C. Bull, ‘‘Strategic issues in customer relationship management (CRM)
implementation,’’ Bus. Process Manage. J., vol. 9, no. 5, pp. 592–602,
Oct. 2003.

[4] Z. Soltani and N. J. Navimipour, ‘‘Customer relationship management
mechanisms: A systematic review of the state of the art literature and
recommendations for future research,’’ Comput. Hum. Behav., vol. 61,
pp. 667–688, Aug. 2016.

[5] S.-Y. Kim, T.-S. Jung, E.-H. Suh, and H.-S. Hwang,

‘‘Customer
segmentation and strategy development based on customer lifetime value:
A case study,’’ Expert Syst. Appl., vol. 31, no. 1, pp. 101–107, Jul. 2006.

[6] H. Wilson, E. Daniel, and M. McDonald, ‘‘Factors for success in customer
relationship management (CRM) systems,’’ J. Marketing Manage., vol. 18,
nos. 1–2, pp. 193–219, Feb. 2002.

[7] I. J. Chen and K. Popovich, ‘‘Understanding customer relationship
management (CRM): People, process and technology,’’ Bus. Process
Manage. J., vol. 9, no. 5, pp. 672–688, Oct. 2003.

[8] M. Kihn and C. B. O’Hara, Customer Data Platforms: Use People Data To
Transf. Future Marketing Engagement. Hoboken, NJ, USA: Wiley, 2020.
[9] J. T. Wei, S. Y. Lin, and H. H. Wu, ‘‘A review of the application of RFM

model,’’ Afr. J. Bus. Manage., vol. 4, no. 19, p. 4199, 2010.

[10] H.-H. Wu, S.-Y. Lin, and C.-W. Liu, ‘‘Analyzing patients’ values by
applying cluster analysis and LRFM model in a pediatric dental clinic in
Taiwan,’’ Scientific World J., vol. 2014, pp. 1–7, Jun. 2014.

[11] R. Mahfuza, R. S. Uddin, Y. Rahman, and Md. A. Hai, ‘‘A comprehensive
framework for superstore bus. With employing effective clustering
techniques,’’ in Proc. 24th Int. Conf. Comput. Inf. Technol. (ICCIT),
Dec. 2021, pp. 1–6.

[12] Y.-L. Chen, M.-H. Kuo, S.-Y. Wu, and K. Tang, ‘‘Discovering recency,
frequency, and monetary (RFM) sequential patterns from customers’ pur-
chasing data,’’ Electron. Commerce Res. Appl., vol. 8, no. 5, pp. 241–251,
Oct. 2009.

[13] A. A. Zoeram and A. K. Mazidi,

‘‘New approach for customer
clustering by integrating the LRFM model and fuzzy inference system,’’
Iranian J. Manage. Stud., vol. 11, no. 2, pp. 351–378, Apr. 2018.

[14] A. J. Christy, A. Umamakeswari, L. Priyatharsini, and A. Neyaa, ‘‘RFM
ranking—An effective approach to customer segmentation,’’ J. King Saud
Univ.-Comput. Inf. Sci., vol. 33, no. 10, pp. 1251–1257, Dec. 2021.
[15] X. He and C. Li, ‘‘The research and application of customer segmentation
on e-commerce websites,’’ in Proc. 6th Int. Conf. Digit. Home (ICDH),
Dec. 2016, pp. 203–208.

[16] C. O. Sakar, S. O. Polat, M. Katircioglu, and Y. Kastro, ‘‘Real-time
prediction of online shoppers’ purchasing intention using multilayer
perceptron and LSTM recurrent neural networks,’’ Neural Comput. Appl.,
vol. 31, no. 10, pp. 6893–6908, Oct. 2019.

[17] Y.-S. Shih and M.-H. Lin, ‘‘A lstm approach for sales forecasting of goods
with short-term demands in e-commerce,’’ in Proc. Asian Conf. Intell. Inf.
Database Syst., 2019, pp. 244–256.

[18] Y. Issaoui, A. Khiat, A. Bahnasse, and H. Ouajji, ‘‘An advanced LSTM
model for optimal scheduling in smart logistic environment: E-commerce
case,’’ IEEE Access, vol. 9, pp. 126337–126356, 2021.

[19] C. Wang, ‘‘Efficient customer segmentation in digital marketing using
deep learning with swarm intelligence approach,’’ Inf. Process. Manage.,
vol. 59, no. 6, Nov. 2022, Art. no. 103085.

[20] M. S. Kasem, M. Hamada, and I. Taj-Eddin, ‘‘Customer profiling,
segmentation, and sales prediction using AI in direct marketing,’’ Neural
Comput. Appl., vol. 36, no. 9, pp. 4995–5005, Mar. 2024.

[21] K. Sriprasadh, S. Palit, B. Pravallika, Manjunatha, R. Lenka, and A. Singla,
‘‘Client segmentation and customization in e-commerce: Applications of
machine learning from a management perspective,’’ in Proc. Int. Conf.
Commun., Comput. Sci. Eng. (IC3SE), May 2024, pp. 1423–1427.
[22] M. Rajyalaxmi, C. Vijai, K. Srivastava, N. Kalyan, B. Pravallika, and
A. Dutt, ‘‘Application of machine learning algorithms for customer
segmentation in e-commerce management,’’ in Proc. Int. Conf. Sci.
Technol. Eng. Manage. (ICSTEM), Apr. 2024, pp. 1–5.

KWANHEE KIM received the M.S. and Ph.D.
degrees from the School of Computer Science and
Engineering, Chung-Ang University, in 2013 and
2023, respectively.

He has been working with CreativeSoft Devel-
opment Company, since 2013. Since 2013, he is
currently working as the CEO with Software
Development Operating Company. He has been
involved in various developments including sys-
tem integration (SI), mobile applications, and
solution development. Currently, his company develops customer data
platform (CDP) solutions and provides services to enterprises. His research
interests include mobile app development, CDP, machine learning, and data-
driven decision-making through big data analysis.

MINGYU JO (Graduate Student Member, IEEE)
received the B.S. and M.S. degrees in com-
puter engineering from the School of Computer
Science and Engineering, Chung-Ang Univer-
sity, Seoul, South Korea,
in 2021 and 2023,
respectively, where he is currently pursuing the
Ph.D. degree in software engineering. His research
interests include distributed systems, high perfor-
mance computing, operating systems, and mobile
systems.

ILKYEUN RA (Member, IEEE) received the
combined B.S. and M.S. degree in computer sci-
ence from Sogang University, the M.S. degree in
computer science from the University of Colorado
Boulder, and the Ph.D. degree in computer and
information science from Syracuse University,
in 2001. He was a Research Staff Member at the
LG Information and Communications (currently
LG Telecom) Research Center. He joined the
Department of Computer Science and Engineer-
ing, University of Colorado Denver, in 2001. His research interests include
computer networks, developing adaptive distributed system software, and
high speed communication system software to support high performance
distributed computing applications.

SANGOH PARK (Member, IEEE) received the
B.S., M.S., and Ph.D. degrees from the School of
Computer Science and Engineering, Chung-Ang
University, in 2005, 2007, and 2010, respectively.
He worked as a Senior Researcher with Global
Science Experimental Data Hub Center, Korea
Institute of Science and Technology Information,
from 2012 to 2017, and a Research Professor at
the School of Computer Science and Engineering.
He has been working as an Assistant Professor
with the School of Computer Science and Engineering, Chung-Ang
University, since 2017. His research interests include embedded systems, big
data systems, cyber physical systems, and Linux systems.

VOLUME 13, 2025

12541

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Received18December2024,accepted6January2025,dateofpublication13January2025,dateofcurrentversion23January2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3529023
RFMVDA: An Enhanced Deep Learning Approach
for Customer Behavior Classification in
E-Commerce Environments
KWANHEEKIM 1,MINGYUJO 1,(GraduateStudentMember,IEEE),
ILKYEUNRA 2,(Member,IEEE),ANDSANGOHPARK 1,(Member,IEEE)
1SchoolofComputerScienceandEngineering,Chung-AngUniversity,Seoul06974,SouthKorea
2DepartmentofComputerScienceandEngineering,UniversityofColoradoDenver,Denver,CO80204,USA
Correspondingauthor:SangohPark(sopark@cau.ac.kr)
ThisworkwassupportedinpartbytheKoreaInstituteforAdvancementofTechnology(KIAT),KoreanGovernment[MinistryofTrade,
IndustryandEnergy(MOTIE)](HumanResourceDevelopment(HRD)ProgramforIndustrialInnovation)underGrantP0020632;andin
partbytheChung-AngUniversityResearchScholarshipGrantsin2023.
ABSTRACT Customer Relationship Management (CRM) systems, widely used in enterprises, have
evolvedintoSoftware-as-a-Service(SaaS)platforms.WiththeadventofCustomerDataPlatforms(CDP),
these systems continuously store customer behavior data for purposes such as creating single customer
profiles,analyzing,tracking,andmanagingcustomerinteractionsfromvariousperspectives.Withtheglobal
expansion of the e-commerce market, research on customer analysis and classification optimized for the
e-commerce environment has been actively conducted. The RFM (Recency, Frequency, Monetary) model
is a straightforward method for classifying customers and is applied across various industries. However,
inthee-commerceenvironment,wherecustomerscanaccessservicesatanytime,therearelimitationsin
collecting, storing, and reflecting customer behavior data for classification. To resolve these limitations,
thispaperproposestheRFMVDA(Recency,Frequency,Monetary,Visits,Durations,Actions)model.This
model is designed to capture customer data, sessions, and behavior units suitable for the e-commerce
environment.ByutilizingtheRFMVDAmodelforcustomerbehavior-basedsegmentationandclassification,
we constructed a Deep Neural Network (DNN) to predict customer behavior-based classifications. As a
result,theproposedmodeldemonstratedasegmentationpredictionaccuracyof92.98%forcustomersinthe
e-commerceenvironment.
INDEX TERMS Customersegmentation,customerclassification,machinelearning,deepneuralnetwork
(DNN),customerdataplatform(CDP),customerrelationshipmanagement(CRM).
I. INTRODUCTION leadingtoahighdemandfordataETL(Extract,Transform,
As computing power has increased, big data and Artificial Load) processes across various industries. This has resulted
Intelligence (AI) have become integral to our daily lives. in the widespread use of big data platforms for storing
With advancements in big data processing technologies, and managing domain-specific data [2]. Companies use
various industries have increasingly adopted methods for Customer Relationship Management (CRM) software to
data storage and management. According to global market handle complex and diverse data. CRM systems perform
research firm IDC, the volume of data is expected to grow ETL on customer data and maintain this information over
from 33ZB in 2018 to 172ZB by 2025, with an annual long periods for business management purposes. CRM is
growth rate of 61% [1]. Many companies have seen an crucialformanagingcustomerinteractions,enhancingsales,
accelerated growth in digital business and data complexity, creating value, and personalizing products and services [3],
[4], [5], [6], [7]. Recently, companies have begun using
The associate editor coordinating the review of this manuscript and Customer Data Platforms (CDP) to continuously store
approvingitforpublicationwasYiqiLiu . information about customers who access their services and
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 12527

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
websites. These platforms allow for the creation, tracking, customerclassification,bothofwhichsignificantlyimprove
and management of single customer profiles, analyzing upontraditionalmethods.
customer behavior from various perspectives [8]. Various The structure of this paper is as follows: Section II
studiesoncustomersegmentationhavebeenconductedusing introduces concepts for customer segmentation and related
the collected customer data. A representative method for studies on customer behavior and purchase prediction
customer segmentation is the RFM (Recency, Frequency, in the e-commerce environment. Section III proposes
Monetary) model [9], [10], [11]. Companies use the RFM the RFMVDA model for customer behavior data in
model to classify existing customers, thereby enabling e-commerce, including segmentation for non-purchasing
targetedmarketingandpromotionstoencouragerepeatvisits customers. Section IV evaluates and analyzes the learning
or purchases. The RFM model categorizes customers based accuracyandpredictionaccuracyforcustomerbehaviorclas-
onrecency,frequency,andmonetaryvalueofpurchases[12]. sificationusingtheproposedDNNmodel.Finally,SectionV
However, the traditional RFM model has significant lim- providesconclusionsandfutureresearchdirections.
| itations,     | especially      | in the | context | of    | modern e-commerce |            |                 |           |            |     |           |       |           |
| ------------- | --------------- | ------ | ------- | ----- | ----------------- | ---------- | --------------- | --------- | ---------- | --- | --------- | ----- | --------- |
| environments. |                 |        |         |       |                   |            | II. RELATEDWORK |           |            |     |           |       |           |
|               |                 |        |         |       |                   |            | The RFM         | (Recency, | Frequency, |     | Monetary) | model | is one of |
| Firstly,      | the traditional |        | RFM     | model | is only           | capable of |                 |           |            |     |           |       |           |
classifying customers who have made a purchase. It does the most widely used methods for customer segmentation
not account for customers who visit a store or platform and analysis in marketing. It simplifies the classification of
withoutmakingapurchase,therebyoverlookingasignificant customers based on three criteria, making it an effective
segmentofcustomerinteractions.Secondly,theRFMmodel tool for marketing applications. The RFM model has been
employedinindustriesforover30yearsasadirectmarketing
| is traditionally |     | applied in | offline | retail | environments | where |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ------- | ------ | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
customer interactions are bound by store hours, and the approach and remains widely used due to its ease of
data collected is limited to those specific timeframes. This implementation. Companies use the RFM model to classify
customersintocategoriessuchasloyalcustomers,potential
| approach | is inadequate |     | for e-commerce, |     | where | customer |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
interactionsarecontinuousandcanoccuratanytime.Thirdly, customers, and lost customers, thereby gaining insights
|         |       |        |           |     |                   |     | into consumer | loyalty | and | relationships |     | with the company’s |     |
| ------- | ----- | ------ | --------- | --- | ----------------- | --- | ------------- | ------- | --- | ------------- | --- | ------------------ | --- |
| the RFM | model | is not | optimized | for | online e-commerce |     |               |         |     |               |     |                    |     |
platforms. In e-commerce, customers engage in various products[11].TheRFMmodelrankscustomersbasedonthe
activities beyond just purchasing, such as browsing, adding recency, frequency, and monetary value of their purchases,
|     |     |     |     |     |     |     | converting | this | information | into | a two-dimensional |     | data |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | ---- | ----------------- | --- | ---- |
itemstocarts,andspendingtimeonspecificproductpages.
Theseactivitiesformacrucialpartofthecustomerjourney, format. Subsequent clustering algorithms like K-means and
whichtheRFMmodelfailstocapture. fuzzyinferencearethenappliedtosegmentcustomers[13],
To address these challenges, this paper proposes the [14], [15]. The LRFM model extends the RFM model by
RFMVDA (Recency, Frequency, Monetary, Visits, Dura- adding a Length factor, representing the time span between
|                 |     |              |     |         |                 |     | the first | and last | purchases | [10]. | This | model measures | the |
| --------------- | --- | ------------ | --- | ------- | --------------- | --- | --------- | -------- | --------- | ----- | ---- | -------------- | --- |
| tions, Actions) |     | model, which |     | extends | the traditional | RFM |           |          |           |       |      |                |     |
model by incorporating additional dimensions that are purchase cycle of customers, enabling further segmentation
crucial for capturing customer behavior in e-commerce intocorecustomers,potentialcustomers,lostcustomers,and
environments. The RFMVDA model introduces three new newcustomersbasedontheLengthattribute.
attributes—Visits, Durations, and Actions—allowing for In the e-commerce environment, customer segmentation
|        |               |     |          |             |               |     | and purchase | prediction |     | research | often | utilize Recurrent |     |
| ------ | ------------- | --- | -------- | ----------- | ------------- | --- | ------------ | ---------- | --- | -------- | ----- | ----------------- | --- |
| a more | comprehensive |     | analysis | of customer | interactions. |     |              |            |     |          |       |                   |     |
By integrating these additional behavioral dimensions, Neural Networks (RNN) and Long Short-Term Memory
the RFMVDA model not only enhances the granularity (LSTM) networks to learn customer behavior and predict
of customer segmentation but also makes it possible to purchase likelihood [16], [17]. Studies combining LSTM
classify customers based on their entire journey on an with Random Forest (RF) algorithms analyze customers’
|            |       |           |       |     |                 |     | purchasing | activities | and | access | patterns | over | time to |
| ---------- | ----- | --------- | ----- | --- | --------------- | --- | ---------- | ---------- | --- | ------ | -------- | ---- | ------- |
| e-commerce | site, | including | those | who | do not complete | a   |            |            |     |        |          |      |         |
purchase. This approach ensures that businesses can gain a predict consumer behavior. These models input customer
deeperunderstandingofbothpurchasingandnon-purchasing behavior and purchase history into an LSTM-RF model,
behaviors, enabling more effective and targeted marketing producing purchase probability outputs through a Fully
strategies. Connected Layer [18]. Although LSTM-RF models have
|     |     |     |     |     |     |     | shown high | performance |     | in predicting |     | customer purchases |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------- | --- | ------------------ | --- |
Furthermore,wehavechosentoimplementaDeepNeural
Network (DNN) model to process the high complexity in e-commerce, they mainly focus on customers who have
and volume of data associated with e-commerce platforms. made purchases, thus limiting their ability to classify
DNNs are particularly well-suited for this task due to their non-purchasinguserbehaviors.
ability to model complex patterns and interactions within The Self-Organizing Neural Network (SONN) employs
largedatasets,makingthemidealforcustomerclassification deeplearningforcustomersegmentationindigitalmarketing
tasks that involve multiple behavioral dimensions. The withinthee-commerceenvironment[19].Thisunsupervised
contributions of this research lie in the development of the learning model clusters customer data using the RFM
RFMVDA model and the application of DNN for enhanced model,SOM(Self-OrganizingMap),andDNN(DeepNeural
| 12528 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
FIGURE1. Flowdiagramofcustomerinformation,session,andbehaviorunitdatamodeling.
Network). The SONN model classified 4,372 customers The study achieved an accuracy of approximately 93%
into five segmented groups with an accuracy of 98%. in identifying target customer segments, underscoring the
SONN’s ability to generate two-dimensional data clusters potential of these techniques to enhance customer segmen-
allows for easy identification of relationships and patterns tation strategies and enable more effective personalized
in the data. However, the results can vary depending marketing. Additionally, Vijai et al. [22] applied a range
on the similarity and distance functions used, increasing of machine learning algorithms, including clustering and
model complexity. Moreover, SONN primarily considers predictive modeling techniques, for customer segmentation
purchase data for customer classification, excluding factors in e-commerce management. Their study emphasizes the
| like access | environment, |     | behavior | data, | dwell | time, | and |               |                 |           |            |             |
| ----------- | ------------ | --- | -------- | ----- | ----- | ----- | --- | ------------- | --------------- | --------- | ---------- | ----------- |
|             |              |     |          |       |       |       |     | critical role | of personalized | marketing | strategies | tailored to |
purchased products, which are essential for behavior-based distinctcustomersegments.
segmentationinthee-commerceenvironment. These advancements highlight the ongoing evolution of
Recent studies have further explored the application customer segmentation techniques, particularly in adapting
of machine learning techniques for client segmentation traditional models to the complexities of the e-commerce
| in e-commerce    |      | settings.     | For       | instance,  | Banerjee | and        | col- | environment.                        |     |     |     |     |
| ---------------- | ---- | ------------- | --------- | ---------- | -------- | ---------- | ---- | ----------------------------------- | --- | --- | --- | --- |
| leagues          | [20] | examined      | AI-driven | approaches |          | for        | cus- |                                     |     |     |     |     |
| tomer profiling, |      | segmentation, |           | and        | sales    | prediction | in   |                                     |     |     |     |     |
|                  |      |               |           |            |          |            |      | III. ECBC(EFFICIENTCUSTOMERBEHAVIOR |     |     |     |     |
direct marketing. Their research highlights how integrat- CLASSIFICATION)
ing AI techniques can improve segmentation accuracy A. CUSTOMERDATAMODELING
| and predict | sales | trends, | thereby | significantly |     | enhancing |     |            |                  |          |          |            |
| ----------- | ----- | ------- | ------- | ------------- | --- | --------- | --- | ---------- | ---------------- | -------- | -------- | ---------- |
|             |       |         |         |               |     |           |     | This paper | collects various | customer | behavior | data (such |
personalizedmarketingstrategies.Similarly,Sriprasadhand as access information, webpage visits, dwell time, and
co-authors[21]investigatedtheuseofvariousmachinelearn-
|     |     |     |     |     |     |     |     | device usage) | in the e-commerce |     | environment | and uses it |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------- | --- | ----------- | ----------- |
ing algorithms for client segmentation and customization tosegmentcustomersthroughmachinelearningtechniques.
within e-commerce environments. Their approach included Customer data is modeled into three main components:
| data preprocessing |     | using | Python’s | TensorFlow |     | and | Pandas |     |     |     |     |     |
| ------------------ | --- | ----- | -------- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- |
customerinformation,sessions,andbehaviors.Basedonthis
libraries, followed by the application of clustering models model, the data is transformed into attributes necessary for
suchasK-means,DBSCAN,andAgglomerativeClustering.
customersegmentationintheproposedRFMVDA(Recency,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 12529 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE1. DefinitionofRFMVDAattributes. TABLE2. DefinitionofVDARattributes.
Consequently,theyspendtimeontheproductdetailpages,
|     |     |     |     |     |     |     |     | increasing | their dwell | time on the | e-commerce |     | website. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | ---------- | --- | -------- |
Frequency,Monetary,Visits,Durations,Actions)model.This
transformed data is used to classify and segment customers To classify customers in the e-commerce environment, the
using machine learning models and Deep Neural Networks RFMVDA(Recency,Frequency,Monetary,Visits,Durations,
|        |          |     |                |     |              |     |      | Actions) | model adds | three attributes—visits, |     | durations, | and |
| ------ | -------- | --- | -------------- | --- | ------------ | --- | ---- | -------- | ---------- | ------------------------ | --- | ---------- | --- |
| (DNNs) | designed | for | the e-commerce |     | environment. |     | When |          |            |                          |     |            |     |
a customer accesses a specific e-commerce platform or actions—tothetraditionalRFMmodel,resultinginatotalof
website, information such as the entry channel (various sixattributes,asshowninTable1.Customerstendtospend
searchengines,advertisements,etc.),device,region,country, time on product detail pages while comparing products of
and time is transmitted to and stored on the server. This interest. When customers view or purchase products on an
|     |     |     |     |     |     |     |     | e-commerce | platform, | the number of | visits to | the shopping |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------- | --------- | ------------ | --- |
informationiscontainedinwebaccessinformationheaders,
which are standardized by web protocols. All information mall’se-commercesiteincreases.Additionally,ifcustomers
about customer behaviors and transaction histories from aresatisfiedwiththepurchasedproducts,theywillcontinue
the moment they enter the e-commerce environment until to access the e-commerce site to browse or purchase other
they leave is stored on the server. The stored customer products.Therefore,thenumberofvisitsisacrucialattribute
|             |     |             |      |       |              |     |          | for classifying | customers | in the e-commerce |     | environment. |     |
| ----------- | --- | ----------- | ---- | ----- | ------------ | --- | -------- | --------------- | --------- | ----------------- | --- | ------------ | --- |
| information | is  | categorized | into | three | data models: |     | customer |                 |           |                   |     |              |     |
informationmodel,sessionmodel,andbehaviorunitmodel, Ifacustomerdecidesthatthecontentoftheshoppingmall’s
as shown in Figure 1. The customer information model e-commerce website is unnecessary, the time they spend
|         |       |                |      |        |          |     |           | viewing | the detail pages | will decrease. | For | instance, | if a |
| ------- | ----- | -------------- | ---- | ------ | -------- | --- | --------- | ------- | ---------------- | -------------- | --- | --------- | ---- |
| records | basic | identification | data | of the | customer |     | accessing |         |                  |                |     |           |      |
thee-commerceplatform,includingdevice,region,browser, customer accesses the e-commerce site via a search engine
usingthekeyword‘‘60-inchTV,’’itishighlylikelythatthe
| and operating |     | system | data. | This model | is  | updated | each |     |     |     |     |     |     |
| ------------- | --- | ------ | ----- | ---------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- |
time the customer accesses the website, storing changes customerisinterestedinpurchasingaproductrelatedtothe
in the user’s access environment in real-time. The session keyword.Thecustomerwillbrowsetheproductsofinterestor
comparableproductsonthee-commercesiteandspendtime
| model comprehensively |     |     | records | customer | behavior |     | during |     |     |     |     |     |     |
| --------------------- | --- | --- | ------- | -------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- |
theirstayonthewebsite.Itincludesinformationabouteach onthedetailpages.Hence,thetotaldwelltimeisanessential
|         |           |      |     |          |        |           |      | indicator | of the customer’s | decision | to purchase | a   | product. |
| ------- | --------- | ---- | --- | -------- | ------ | --------- | ---- | --------- | ----------------- | -------- | ----------- | --- | -------- |
| session | generated | when | the | customer | visits | the site, | such |           |                   |          |             |     |          |
as start time, end time, and page sequence, to store data Lastly,theactionattributereflectscustomerbehaviorsuchas
on the customer’s e-commerce site activities. This data is repetitivepageviewsandaddingproductstothecart.These
|     |     |     |     |     |     |     |     | actions | indicate satisfaction | with the | purchased | products, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------------- | -------- | --------- | --------- | --- |
usedtoanalyzedetailedinformationsuchaswhichproducts
the visitor showed interest in and which pages they spent leadingtocontinuousaccesstothesitetobrowseorpurchase
more time on. The behavior unit model stores specific other products. Therefore, the total number of visits, total
behavior information during the customer’s journey on the dwelltime, andtotalpurchaseactions arecriticalindicators
site. It segments and stores actions such as each page view, forcustomerclassificationinthee-commerceenvironment.
| number | of clicks, | cart | additions, | and | purchase |     | activities, |     |     |     |     |     |     |
| ------ | ---------- | ---- | ---------- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
which are essential for subsequent customer segmentation. C. VDARSEGMENTATIONMODEL(NON-PURCHASING
| The unique | ID  | assigned | to the | customer | links | the | session |     |     |     |     |     |     |
| ---------- | --- | -------- | ------ | -------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
CUSTOMERSEGMENTATION)
model and individual behavior units, storing interactions Traditional RFM models are limited in that they primar-
| related | to customer |     | preferences, | interests, |     | and purchasing |     |           |               |           |       |               |     |
| ------- | ----------- | --- | ------------ | ---------- | --- | -------------- | --- | --------- | ------------- | --------- | ----- | ------------- | --- |
|         |             |     |              |            |     |                |     | ily focus | on segmenting | customers | based | on purchasing |     |
tendencies. This model integrates with the session model, behavior, leaving non-purchasing customers unanalyzed.
connectingallbehaviorunitsoccurringineachsessionintoa However,ine-commerceenvironments,customerscanfreely
singlesession.
|     |     |     |     |     |     |     |     | access | the site at any | time to browse | products |     | without |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | -------------- | -------- | --- | ------- |
necessarilymakingapurchase.Unlikephysicalstores,where
B. RFMVDASEGMENTATIONMODEL(PURCHASING it is difficult to track non-purchasing customers’ activities,
CUSTOMERSEGMENTATION) e-commerce platforms can capture and model a wide range
Customers generally access various pages when they visit ofbehavioraldata,regardlessofwhetherthecustomermakes
| an e-commerce |     | platform. | In  | the case | of a shopping |     | mall’s | apurchase. |     |     |     |     |     |
| ------------- | --- | --------- | --- | -------- | ------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- |
e-commercesite,customerstendtobrowsedetailedinforma- To address the gap in customer segmentation for non-
tionaboutproductsandcontemplatemakingpurchases. purchasingcustomers,thisstudyproposestheVDAR(Visits,
| 12530 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
FIGURE2. DNNConfigurationforcustomerclassification.
Durations, Actions, Referral Keyword) model. The VDAR for companies aiming to derive actionable insights from
model classifies customers based on four key attributes: customer activities beyond purchase behavior. This model
Visits, Durations, Actions, and Referral Keyword, as sum- helpsmarketersanddecision-makersidentifycustomerswho
marized in Table 2. These attributes enable the model to areintheconsiderationphase,allowingthemtotailortargeted
assess customer engagement by analyzing their site visit marketing strategies that could lead to future purchases.
frequency, session duration, behavioral patterns, and their For example, if a promotion generates high site traffic
referralsourcesbeforelandingonthee-commercesite. but low engagement in terms of page views and session
For instance, consider a customer who accessed the durations,itcouldindicatethattheproductsorcontentmay
e-commerce site after searching for ‘‘60-inch TV’’ on a not be resonating with the audience, providing valuable
searchengine.Thiscustomerislikelytohaveahighinterest feedback for future optimizations. Therefore, the VDAR
in purchasing a television or gathering information about modelenablesthesegmentationofnon-purchasingcustomers
similarproducts.Thecustomermaybrowsevariousproduct based on their behavioral data and serves as a key tool for
models, read reviews, and compare prices, leading to an improving overall marketing efficiency and driving data-
increaseintheirtotalsessiondurationandpageviews.Ifthe drivendecision-makingine-commercebusinesses.
productdetailsandpricingmeettheirexpectations,theymay Furthermore, by applying the VDAR model, businesses
revisit the site more frequently, and their visit count and can better understand and respond to the entire customer
page view count would naturally increase. Additionally, the journey on e-commerce platforms. This model not only
referralkeywordattributeprovidesinsightintothecustomer’s capturespurchase-relatedbehaviorbutalsoprovidesinsights
intentbasedonthesearchtermstheyusedbeforelandingon into the broader context of user interactions, including
thee-commercesite. those that do not result in immediate transactions. This
The VDAR model’s classification of non-purchasing comprehensive approach allows companies to tailor their
customers, based on their behavioral attributes, is crucial strategies to engage potential customers more effectively
VOLUME13,2025 12531

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE3. Definitionofinputlayerparameters.
throughout their online journey, from initial site visits to customer classification, where numerous behavioral factors
eventualpurchases. mustbeconsideredsimultaneously.Furthermore,DNNscan
efficientlyhandlethehighdimensionalityandvolumeofdata
|                                |     |     |     | associated with      | the RFMVDA | model, ensuring | robust and |
| ------------------------------ | --- | --- | --- | -------------------- | ---------- | --------------- | ---------- |
| D. DNNCONFIGURATIONFORCUSTOMER |     |     |     | accuratepredictions. |            |                 |            |
CLASSIFICATION The deep learning model is trained to predict values as
Thecustomerdataaccessedinthee-commerceenvironment closeaspossibletotheactualvaluesbycalculatingtheerror
is processed and normalized according to the RFMVDA loss when the predicted value differs from the actual value
model, and a neural network is constructed to classify duringforwardpropagation.Variouslossfunctionsexist,with
| customers. The | configuration | of the DNN | is shown in |                      |      |                 |                 |
| -------------- | ------------- | ---------- | ----------- | -------------------- | ---- | --------------- | --------------- |
|                |               |            |             | binary cross-entropy | used | when the output | values are 0 or |
Figure 2. The input layer consists of N data points from 1.However,thisisnotsuitableformulti-classclassification
thecustomer’ssessionmodel.Thehiddenlayeriscomposed wheretherearemorethantwoclasses.
| of two layers, | each connected | by neurons. | The input |     |     |     |     |
| -------------- | -------------- | ----------- | --------- | --- | --- | --- | --- |
N C
data is passed to the hidden layers, with the first hidden 1 XX
|     |     |     |     |     | L =− | t log(y ) | (1) |
| --- | --- | --- | --- | --- | ---- | --------- | --- |
layer consisting of 128 neurons activated by the ReLU N ij ij
i=1 j=1
activationfunction.Thesecondhiddenlayeralsoconsistsof
128 neurons, connected by the sigmoid activation function. Categorical cross-entropy is used for multi-class clas-
Finally,theoutputlayerreceivesthefinalresult. sification problems, as indicated by Equation (1), where
We selected a Deep Neural Network (DNN) for this task C represents the number of classes. Therefore, this paper
duetoitsabilitytomodelcomplexrelationshipswithinlarge employs categorical cross-entropy as the loss function
datasets, which are common in e-commerce environments. since the classification model is trained on data consisting
DNNsexcelatcapturingintricatepatternsanddependencies of 15 different categories for purchasing customers and
in data, making them particularly suitable for tasks such as 9differentcategoriesfornon-purchasingcustomers.Finally,
| 12532 |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | ------------- |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE4. Compositionoftheperformanceevaluationdataset.
TABLE5. CustomersegmentationresultsusingLRFMmodel.
a DNN is constructed, as shown in Figure 2, to standardize 37,698customersessionsand405,280customeractivitydata
andtraintheRFMVDAdatamodel. points.Thedatasetprimarilycontainsvariablesforanalyzing
customer behavior, including visit time, page views, cart
E. INPUTLAYERPARAMETERSFORDNN additions,andproductpurchases,assummarizedinTable4.
Theparametersofthedatamodelusedintheinputlayerofthe These behaviors were the focus of analysis and were used
DNNareconfiguredasshowninTable3.Theseparameters to evaluate the proposed RFMVDA model, as well as to
include 14 customer data points and 15 session data points, compareitagainsttheLRFMmodel.
totaling 29. These parameters serve as essential input data Therawdatacollectedfromthee-commerceenvironment
for customer classification and behavior prediction through contains unstructured data that requires refinement and
the DNN. Each time a customer accesses the e-commerce preprocessing for analysis. Initially, irrelevant features and
website, a unique session identifier is created. During the missing data were removed, followed by normalization of
session, if the customer browses various product pages and thedataintoasuitableformatforanalysis.Giventhediverse
makespurchases,datasuchasthesession’sdwelltime,total distributionofcustomerbehaviordata,eachvariable’svalues
numberofactions,totalpurchasequantity,andtotalpurchase werescaledbetween0and1tofacilitateinputintothemodel.
amount is stored. When the customer exits the e-commerce Throughout this process, the RFMVDA model was con-
website,thesessioninformationinthecustomerdatamodel structedtoanalyzeeachcustomer’sbehaviorpatternindetail.
isupdatedwiththefinalactionstakenbythecustomer.This This model includes six key variables: Recency, Frequency,
process of storing and compiling customer actions from the Monetary, Visits, Durations, and Actions. For the purposes
moment they access the website until they exit provides the of model training and testing, the dataset was split into two
29parameters,whicharethenusedtotraintheDNN. sets:70%wasusedfortraining,whiletheremaining30%was
reservedfortesting.
IV. PERFORMANCEEVALUATION
A. DATASET
The dataset used in this study is based on real customer B. CUSTOMERSEGMENTATIONBASEDONLRFMMODEL
datacollectedfromane-commercewebsiteinSouthKorea. The LRFM model was applied to analyze purchasing
This dataset spans a 3-month period from January 1, 2022, customerbehaviorpatternsandtocategorizecustomersinto
to March 31, 2022, and includes information on a total of four segments. This model assigns scores to each customer
9,416 registered customers. Among these, 5,041 customers based on four factors: Length (the time between the first
visited the website, and 299 completed a purchase. The andmostrecentpurchase),Recency(thetimesincethemost
dataset includes various data such as customer registration recentpurchase),Frequency(thenumberofpurchases),and
details, website visit logs, session information from each Monetary(thetotalamountspent).Usingthesefourelements,
visit, and customer activity records. In total, there are thecustomerswereclassifiedintospecificsegments.
VOLUME13,2025 12533

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE6. FinalcustomersegmentationappliedusingtheRFMVDAmodel.
Table 5 shows the customer segmentation after applying make a purchase, the LRFM model does not capture this
the LRFM model. A total of 299 customers were classified behavior. Thus, a more comprehensive model that includes
into four primary segments: VIP Customers, Potential non-purchasingcustomersisneeded.
Loyal Customers, Regular Customers, and Lost Customers. Additionally,themodeldoesnotfullyreflectallcustomer
Each segment was determined by factors such as purchase access activities in the e-commerce environment. Since
frequency, the recency of purchases, total monetary value, customerscanengageinavarietyofactionsatanytime,itis
andthelengthoftimefromthefirstvisittothepurchase. critical to evaluate the potential likelihood of these actions
TheVIPcustomersaccountfor30%ofthetotal299cus- leading to purchases. To overcome these limitations, it is
tomers. These customers recently made frequent purchases necessary to develop an expanded model that can analyze
withhighmonetaryvalueandareconsideredveryimportant. a broader range of customer access patterns and behavioral
| On the | other hand, | the Lost   | Customers | group          | comprises | data. |     |     |     |
| ------ | ----------- | ---------- | --------- | -------------- | --------- | ----- | --- | --- | --- |
| 47% of | the total   | customers. | This      | group requires | further   |       |     |     |     |
customerrelationshipmanagementstrategiestoeitherretain
| or reactivate | them. | The VIP | Customers | group | maintains |     |     |     |     |
| ------------- | ----- | ------- | --------- | ----- | --------- | --- | --- | --- | --- |
C. CUSTOMERSEGMENTATIONBASEDONTHERFMVDA
| recent and | frequent | purchases | with | high spending, | placing | MODEL |     |     |     |
| ---------- | -------- | --------- | ---- | -------------- | ------- | ----- | --- | --- | --- |
them at the top of the LRFM model’s scoring. These The RFMVDA model extends the traditional LRFM frame-
customers represent a loyal base for the business, and work to enhance the granularity of customer behavior
offeringspecialpromotionsorbenefitscanmaximizereten- analysis and segmentation in the e-commerce environment.
| tion and | engagement. | Potential | Loyal | Customers, | although |     |     |     |     |
| -------- | ----------- | --------- | ----- | ---------- | -------- | --- | --- | --- | --- |
InadditiontothestandardRecency(R),Frequency(F),and
having lower purchase frequency and spending than VIP Monetary (M) dimensions, the RFMVDA model introduces
customers, have still made recent purchases and hold the three additional variables—Visits (V), Durations (D), and
potential to be converted into VIP Customers. They are Actions (A). These supplementary dimensions enable a
a key target for additional marketing strategies aimed at more comprehensive and detailed analysis of customer
customerconversion.RegularCustomersarethosewithlower behavioracrossabroaderspectrumofinteractionswithinthe
purchase frequency but consistent business engagement. e-commerceplatform.
Custommarketingstrategiescanbeappliedtoreinforcetheir Unliketraditionalmodelsthatfocusprimarilyonpurchase
buyingpatternsandencouragemorefrequentpurchases.Lost history, the RFMVDA model provides a more holistic
Customersarethosewhohavenotmaderecentpurchasesand view by incorporating various online activities. This allows
exhibit low frequency and spending patterns. This segment for a richer segmentation of customers based on their
requires targeted remarketing campaigns or incentives to engagement with the platform, taking into account not
encouragerepurchasesandre-engagementwiththebusiness. only their purchasing behavior but also metrics such as
| Although | the LRFM | model | successfully | segmented | cus- |                  |            |               |                  |
| -------- | -------- | ----- | ------------ | --------- | ---- | ---------------- | ---------- | ------------- | ---------------- |
|          |          |       |              |           |      | visit frequency, | time spent | on pages, and | specific actions |
tomers based on their purchasing behavior, it has certain performed on the site. To ensure that each behavioral
limitations,particularlyinthee-commerceenvironment.This dimension contributes equally to the analysis, the data
model fails to account for the activities of customers who for each variable is normalized using Min-Max scaling
havenotmadeanypurchases.Forinstance,evenifcustomers to map the values between 0 and 5. This standardization
| visit the | site and engage | in  | various | activities, | if they do not |         |                    |                |                 |
| --------- | --------------- | --- | ------- | ----------- | -------------- | ------- | ------------------ | -------------- | --------------- |
|           |                 |     |         |             |                | enables | the model to treat | all behavioral | attributes with |
| 12534     |                 |     |         |             |                |         |                    |                | VOLUME13,2025   |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE7. DetailedcustomersegmentationtransitionfromLRFMtoRFMVDAmodel.
equalimportance,therebyprovidingabalancedevaluationof purchasing behavior but also variables such as Visits,
customerengagement. Durations, and Actions, leading to the segmentation of
Through the application of the RFMVDA model, cus- customersinto14detailedcategories.
| tomers were | classified |     | into 14 distinct | segments, |     | as shown |     |     |     |     |     |
| ----------- | ---------- | --- | ---------------- | --------- | --- | -------- | --- | --- | --- | --- | --- |
inTable6.Thissegmentationapproachoffersasignificantly
1) COMPARISONOFCUSTOMERSEGMENTATIONRESULTS
more nuanced classification compared to the traditional TheLRFMmodel,basedonrelativelysimplemetrics,isuse-
| LRFM model, | as  | it accounts | for | a wider | range of | customer |     |     |     |     |     |
| ----------- | --- | ----------- | --- | ------- | -------- | -------- | --- | --- | --- | --- | --- |
fulforidentifyingkeycustomergroupsbuthaslimitationsin
behaviors.TheRFMVDAmodelnotonlyconsiderspurchas-
fullyreflectingthecomplexuserbehaviorpatternsfoundin
inghabitsbutalsointegratesdataonoverallsiteinteractions, dynamiconlineenvironmentslikee-commerce.Forexample,
providingamoredetailedandaccuratereflectionofcustomer
|     |     |     |     |     |     |     | in the LRFM | model, | 140 customers | were classified | as Lost |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------- | --------------- | ------- |
behaviorpatterns. Customers due to a significant decrease in their purchase
This refined segmentation captures the complexity of frequency or length attributes, even though they may have
| customer | interactions | within | the | e-commerce | environment. |     |           |           |        |                |             |
| -------- | ------------ | ------ | --- | ---------- | ------------ | --- | --------- | --------- | ------ | -------------- | ----------- |
|          |              |        |     |            |              |     | completed | purchases | during | other periods. | In the LRFM |
The RFMVDA model offers a more precise categorization model, ‘lost customers’ specifically refer to those whose
byconsideringbothpurchasehistoryanddiversebehavioral
|     |     |     |     |     |     |     | purchasing | activity | has declined | significantly | within the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------ | ------------- | ---------- |
metrics, thereby allowing businesses to better tailor their defined analysis period, rather than customers who have
marketingstrategiesandcustomerrelationshipmanagement nevermadeapurchaseatanypoint.
efforts.
|     |     |     |     |     |     |     | In contrast, | the | RFMVDA | model considers | additional |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --------------- | ---------- |
variablessuchasvisitfrequency,sessionduration,andaction
D. COMPARATIVEANALYSISOFLRFMANDRFMVDA counts to further segment these customers into categories
| MODELS |     |     |     |     |     |     | suchas AbouttoSleepCustomers, |     |     | AtRiskCustomers,and |     |
| ------ | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | ------------------- | --- |
AbouttoLeaveCustomers.Thisapproachallowsforamore
| The segmentation |     | results | of 299 | customers |     | who made |     |     |     |     |     |
| ---------------- | --- | ------- | ------ | --------- | --- | -------- | --- | --- | --- | --- | --- |
purchases in the e-commerce environment were compared detailedclassificationofcustomers,identifyingearlysignsof
churnthattheLRFMmodelmayoverlook.
| using both       | the | LRFM      | and RFMVDA | models.     |           | The LRFM |     |     |     |     |     |
| ---------------- | --- | --------- | ---------- | ----------- | --------- | -------- | --- | --- | --- | --- | --- |
| model classifies |     | customers | into       | four simple | segments: | VIP      |     |     |     |     |     |
Customers, Potential Loyal Customers, Regular Customers, 2) MODELCOMPARISONANALYSIS
and Lost Customers. In contrast, the RFMVDA model TheLRFMmodelisusefulforprovidingasimplecustomer
is designed to account for various customer behaviors in classification based on purchasing data. However, it falls
the e-commerce environment by incorporating not only short of reflecting comprehensive online behavior data.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     | 12535 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE8. DetailedcustomersegmentationbasedonVDARmodel.
Incontrast,theRFMVDAmodelprovidestheabilitytoseg-
| ment customers |             | by incorporating |              | multidimensional |          | behav-    |     |     |     |     |     |
| -------------- | ----------- | ---------------- | ------------ | ---------------- | -------- | --------- | --- | --- | --- | --- | --- |
| ioral data     | from the    | e-commerce       | environment. |                  | By       | including |     |     |     |     |     |
| non-purchase   | activities, | such             | as           | visit frequency, |          | duration, |     |     |     |     |     |
| and action     | counts,     | the RFMVDA       |              | model            | offers   | a more    |     |     |     |     |     |
| complete       | evaluation  | of customer      |              | engagement,      | allowing | for       |     |     |     |     |     |
moreaccuratepredictionsofpotentialcustomerchurn.
Forexample,asshowninTable7,16ofthe140customers
| categorized  | as Lost      | Customers | in        | the LRFM | model  | were   |     |     |     |     |     |
| ------------ | ------------ | --------- | --------- | -------- | ------ | ------ | --- | --- | --- | --- | --- |
| reclassified | as Potential | Loyal     | Customers |          | in the | RFMVDA |     |     |     |     |     |
modelduetotheinclusionofvisitfrequencyandsiteactivity FIGURE3. RepeatedstratifiedK-Foldcrossvalidationresults.
| data. This  | highlights | the ability | of        | the RFMVDA |               | model to |     |     |     |     |     |
| ----------- | ---------- | ----------- | --------- | ---------- | ------------- | -------- | --- | --- | --- | --- | --- |
| create more | precise    | and         | effective | customer   | segmentation, |          |     |     |     |     |     |
productsorspendingsignificanttimeonproductdetailpages.
| allowing | businesses | to implement |     | more | detailed | CRM |     |     |     |     |     |
| -------- | ---------- | ------------ | --- | ---- | -------- | --- | --- | --- | --- | --- | --- |
strategies.Byidentifyingcustomerswhoshowearlysignsof Additionally, 1,097 customers (22%) demonstrated a keen
|     |     |     |     |     |     |     | interest in | various products, | indicating | strong potential | for |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | ---------- | ---------------- | --- |
churn,targetedmarketingandreactivationcampaignscanbe
launchedtoimprovecustomerretention. future purchases. However, 1,902 customers (40%) were
Inconclusion,theRFMVDAmodelisbettersuitedforthe classified in the lower engagement segments, indicating a
higherriskofdisengagementorabandonment.
| e-commerce | environment |     | as it incorporates |     | a broader | range |     |     |     |     |     |
| ---------- | ----------- | --- | ------------------ | --- | --------- | ----- | --- | --- | --- | --- | --- |
ofbehavioraldata,makingitapowerfultoolforpreventing Marketersanddecision-makerscanutilizethissegmenta-
tiontodeveloppersonalizedpromotionalstrategiesaimedat
customerchurnanddevelopingeffectivemarketingstrategies
thattargetvariouscustomersegmentsbasedontheirdetailed convertingthetopsegmentsintofirst-timebuyers.Bytarget-
behaviorprofiles. ingthe1,711customersinthehigherengagementsegments
|     |     |     |     |     |     |     | with tailored | promotions | and coupons, | the e-commerce |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ------------ | -------------- | --- |
E. BEHAVIORALSEGMENTATIONOFNON-PURCHASING platform can potentially increase its conversion rate and
revenue.
CUSTOMERSUSINGTHEVDARMODEL
As shown in Table 8, the VDAR model was applied to seg- In summary, the VDAR model successfully segments
mentnon-purchasingcustomerswhovisitedthee-commerce non-purchasing customers into distinct groups, helping
|          |        |           |        |      |         |          | e-commerce | businesses | identify potential | first-time | buyers |
| -------- | ------ | --------- | ------ | ---- | ------- | -------- | ---------- | ---------- | ------------------ | ---------- | ------ |
| platform | during | the study | period | from | January | to March |            |            |                    |            |        |
2022. Of the 5,041 total visitors, 4,742 customers did not and customers who may need further engagement. This
|          |             |     |      |       |         |            | segmentation | is particularly | valuable | for targeting | promo- |
| -------- | ----------- | --- | ---- | ----- | ------- | ---------- | ------------ | --------------- | -------- | ------------- | ------ |
| complete | a purchase. | The | VDAR | model | enabled | a detailed |              |                 |          |               |        |
segmentationofthesenon-purchasingcustomers,takinginto tional efforts and optimizing marketing strategies based on
account their behavioral data such as total visits (Visits), customerbehaviorinsights.
totaldwelltime(Durations),totalactions(Actions),andthe
presenceofreferralkeywords(Referrer). F. PREDICTIONOFCUSTOMERSEGMENTATIONUSING
NEURALNETWORKS
| The | analysis | revealed | that approximately |     | 36% | (1,711 |     |     |     |     |     |
| --- | -------- | -------- | ------------------ | --- | --- | ------ | --- | --- | --- | --- | --- |
customers) of the non-purchasing customers fell into the 1) MODELVALIDATIONUSINGREPEATEDSTRATIFIED
top four segments most likely to convert to purchasing K-FOLDCROSSVALIDATION
customers.Thesesegmentsincludecustomerswhoarelikely To ensure the robustness and reliability of the proposed
to purchase soon and customers showing high engagement RFMVDA model, we employed the Repeated Stratified
with the content on the site, such as viewing multiple K-Fold Cross Validation method, which is particularly
| 12536 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
suitableforclassificationtasks.Thistechniqueinvolvesper-
formingmultipleiterationsofcross-validationwithdifferent
shuffles of the data, which helps in assessing the model’s
performancemorecomprehensively.
Forthisvalidation,theRepeatedStratifiedKFold
function from the sklearn library was used, as it is
designedforclassificationmodels.Thismethodallowedfor
a detailed evaluation of how well the model generalizes to
unseendata,beyondtheinitialtrainingset.
AsshowninFigure3,thecross-validationresultsindicate
an average accuracy of 96.9%, which confirms the model’s
stronggeneralizationcapabilityacrossdifferentdatafolds.
FIGURE4. Performancebyoptimizer.
2) EXPLORATIONOFDIFFERENTDNNARCHITECTURESAND
HYPERPARAMETERS
In order to optimize the model’s performance and address
potential overfitting risks, we explored various DNN archi-
tectures and hyperparameters. The experiments involved
tuning different configurations, such as the number of
layers,thenumberofneuronsperlayer,activationfunctions,
learningrates,batchsizes,anddropoutrates.
To systematically evaluate these configurations, we uti-
lized a hyperparameter grid search in combination with
repeated stratified K-fold cross-validation. The grid search
wasconfiguredasfollows:
FIGURE5. PerformanceHeatmap:DropoutRatevsBatchSize.
param_grid = {
’layers’: [[128], [64, 64], [128, 128]], #
Layer configurations
’activation’: [’relu’, ’sigmoid’], #
Activation functions
’optimizer’: [’adam’, ’sgd’], #
Optimizers
’dropout_rate’: [0.0, 0.2, 0.5], #
Dropout rates
’batch_size’: [32, 64], #
Batch sizes
’epochs’: [50, 100, 200] #
Number of epochs
}
# Repeated Stratified \text{K-Fold} Cross
Validation setup
rskf = RepeatedStratifiedKFold(n_splits=3,
n_repeats=1, random_state=42)
FIGURE6. Performancevs.Epochs.
# GridSearchCV setup and model training
grid = GridSearchCV(estimator=model, param_grid=
param_grid, n_jobs=-1, cv=rskf)
grid_result = grid.fit(x_data, y_data_encoded) performance. The following figures illustrate the perfor-
mancecomparisonbetweendifferentoptimizersanddropout
# Output the best score and corresponding
parameters rates:
print(‘‘Best Score: {grid_result.best_score_}’’) AsshowninFigure4,theAdamoptimizerprovidedbetter
print(‘‘Best Params: {grid_result.best_params_}’’)
averageaccuracycomparedtoSGD,makingitthepreferable
choiceforthismodel.
This approach allowed us to identify the optimal combi- TheheatmapinFigure5illustratestheinteractionbetween
nation of hyperparameters, which resulted in a best score dropoutratesandbatchsizes,withadropoutrateof0.0and
of 0.9725614984830221 with the following configuration: abatchsizeof32achievingthehighestaccuracy.
activation function ‘relu’, batch size 32, dropout rate 0.2, Finally, Figure 6 depicts the relationship between the
200epochs,layers[128,128],andoptimizer‘adam’. numberofepochsandperformance,indicatingthatincreasing
The experimental results provided valuable insights into the epochs generally improves accuracy, particularly for
the impact of various hyperparameters on the model’s deepernetworkswithmorelayers.
VOLUME13,2025 12537

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
TABLE9. PerformancemetricsforRFMVDAmodel.
FIGURE7. TrainingandValidationLoss:Training(yellow)andvalidation(blue)lossover200epochsusingoptimalhyperparameters.The
validationlossshowsminimalfluctuation,indicatinggoodgeneralization.
FIGURE8. TrainingandValidationAccuracy:Accuracytrendsover200epochsfortrainingdatasets,showingpredictedvalues
closelymatchingactualvalues,indicatinghighperformanceandminimaloverfitting.
3) EVALUATIONOFOPTIMALHYPERPARAMETERSAND • Optimizer:Adam
MODELPERFORMANCE • DropoutRate:0.2
Intheprevioussections,weexploredvariousDNNarchitec- • BatchSize:32
turesandhyperparameterstodeterminetheoptimalsettings • NumberofEpochs:200
for customer segmentation in the e-commerce environment. • Network Architecture: Two hidden layers, each with
AfterextensiveexperimentsusingRepeatedStratifiedK-Fold 128neurons,usingReLUactivation
CrossValidation,theoptimalconfigurationwasidentifiedas
Using these optimal hyperparameters, the model was
follows:
retrainedon80%ofthedatasetandtestedontheremaining
12538 VOLUME13,2025

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
FIGURE9. SHAPFeatureImportanceforCustomerSegmentationinDNNModel:(a)SegmentationDistributionbyCustomerType,
(b)OverallFeatureImpactonPurchasingCustomers.
FIGURE10. Confusionmatrixfordifferenttrainingandpredictionsplits.
20%. As summarized in Table 9, the model achieved a capacity. Further validation of the model’s performance is
training accuracy of 99.54% and a prediction accuracy of provided in Figure 8, which displays loss and accuracy
92.98%. The trend of training and prediction accuracy over metrics during training and testing. These results confirm
epochsisdepictedinFigure7,showingconsistentaccuracy minimal overfitting, suggesting that the selected model is
improvementsanddemonstratingthemodel’srobustlearning well-suited for this classification task. To understand each
VOLUME13,2025 12539

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
feature’scontributiontothemodel’spredictions,weanalyzed RFM-based models that focus solely on transactional data,
the importance of individual input features using SHAP the VDAR framework provides valuable insights into
(SHapley Additive exPlanations) values. Figure 9 displays the engagement levels of visitors who do not complete
theaverageimpactofeachfeatureoncustomersegmentation purchases.Byidentifyingpatternsinnon-purchasingbehav-
outcomes, with session duration, first action time, and the iors, such as visit frequency and referral keywords, the
number of desktop visits identified as the most influential VDAR model enables businesses to uncover opportunities
factorsindeterminingsegmentationresults. for re-engagement strategies and better understand early
Additional performance metrics were calculated to offer indicatorsofpotentialfutureconversions.
a more comprehensive evaluation. Specifically, the RMSE The performance of the RFMVDA model was validated
(Root Mean Squared Error), Macro F1 Score, and Micro usingaDeepNeuralNetwork(DNN),achievingasegmenta-
F1 Score were included to provide further insights into tionpredictionaccuracyof92.98%andatrainingaccuracyof
the model’s accuracy and robustness. The RMSE values of 99.54%, as shown in Table 9. Additional metrics, including
1.6251 for the 70%-30% split and 1.1778 for the 80%-20% RMSE, Macro F1 Score, and Micro F1 Score, further
splitindicatealowaverageerrormagnitude,reflectinghigh demonstrated its robustness. SHAP analysis in Figure 9
prediction precision. The Macro F1 Score values (0.877 for highlighted the importance of session duration, first action
70%-30% and 0.7923 for 80%-20%) demonstrate balanced time, and desktop visits as key features. The confusion
performance across classes, while the Micro F1 Score matrices in Figure 10 confirmed the model’s consistency
(0.8870for70%-30%and0.9390for80%-20%)underscores acrossvaryingdatasplits.
themodel’seffectivenessinaccuratelyclassifyingindividual Although the results are promising, this study recognizes
instances.ThesemetricsaredetailedinTable9. several limitations. The current analysis relies on historical
Tofurtherassessthemodel’srobustnessandgeneralization data collected over a three-month period, which may
capabilities across different data splits, confusion matrices not fully capture seasonal or long-term behavioral trends.
for the 70%-30% and 80%-20% splits were generated, To address this constraint, future research will incorporate
as illustrated in Figure 10. The confusion matrix for the data from longer observation windows and multiple e-
70%-30% split in Figure 10(a) illustrates the distribution commerce platforms, allowing the RFMVDA and VDAR
of correct and incorrect classifications across all classes, models to be evaluated under broader and more diverse
identifying areas for potential misclassification. The matrix conditions. In addition, direct comparisons with other
for the 80%-20% split in Figure 10(b) shows improved machine learning algorithms, such as Random Forests and
accuracy with the larger training dataset, resulting in a GradientBoosting,werenotperformedinthisstudybutwill
more balanced prediction distribution across classes. This be systematically pursued in future work. By conducting
comparison provides valuable insights into the model’s benchmarkexperimentsunderstandardizedconditions,these
consistencyandrobustnessundervaryingdataconditions. comparative analyses will not only highlight the unique
In conclusion, the selected DNN architecture and hyper- advantages of the RFMVDA framework but also pinpoint
parameters have proven effective for accurate customer areas for further refinement, ultimately enhancing its real-
segmentation in e-commerce environments. These findings worldapplicability.
havepracticalimplications,astheycancontributetorefining Futureresearchwillalsoinvestigatehowrefinedsegmenta-
marketing strategies and enhancing personalized customer tionmodelslikeRFMVDAcanbequantitativelylinkedtokey
experiences. financialmetrics,includingcustomerlifetimevalue,revenue
growth,andretentionrates.Byexaminingtheserelationships
V. CONCLUSION in practical e-commerce environments, we aim to clarify
Withtherapidgrowthofthee-commercemarket,traditional how enhanced segmentation strategies can drive long-term
customer classification methods, such as the RFM model, profitability and support evidence-based decision-making.
facelimitationsincapturingdiverseandcontinuouscustomer This approach will help businesses allocate resources more
behaviors. These methods primarily focus on purchasing effectivelyandprioritizecustomer-centricprogramsbasedon
customers and fail to analyze visitors who interact with aclearunderstandingofpotentialreturns.
platforms but do not make purchases. To address these In conclusion, the RFMVDA and VDAR models, com-
shortcomings,thispaperintroducedtheRFMVDA(Recency, bined with a DNN architecture, represent a significant
Frequency, Monetary, Visits, Durations, Actions) model, advancement in customer behavior classification for e-
whichextendstheRFMframeworkbyincorporatingbehav- commerce environments. These frameworks address the
ioraldimensionssuchasvisitfrequency,sessionduration,and limitationsoftraditionalapproacheswhileprovidingaction-
actioncounts.TheRFMVDAmodelenablesamoredetailed able insights to enhance customer engagement, improve
and comprehensive understanding of purchasing customer retentionstrategies,andsupportsustainablebusinessgrowth.
interactionsindynamice-commerceenvironments. By capturing both purchasing and non-purchasing user
Recognizing the need to analyze non-purchasing cus- patterns, they enable businesses to tailor interventions
tomers as well, this study proposed the VDAR (Visits, more precisely, ultimately unlocking new opportunities for
Durations, Actions, Referral Keyword) model. Unlike the personalizedmarketinganddata-drivendecision-making.
12540 VOLUME13,2025

K.Kimetal.:RFMVDA:AnEnhancedDeepLearningApproachforCustomerBehaviorClassification
| REFERENCES |     |     |     |     |     |     |     |     | KWANHEE | KIM | received the | M.S. | and Ph.D. |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | ---- | --------- |
degreesfromtheSchoolofComputerScienceand
[1] BigData,MinistrySMEsStartupsoftheRepublicofKorea,Sejong-si,
Engineering,Chung-AngUniversity,in2013and
SouthKorea,2022.
[2] J.-G.LeeandM.Kang,‘‘Geospatialbigdata:Challengesandopportuni- 2023,respectively.
ties,’’BigDataRes.,vol.2,no.2,pp.74–81,Jun.2015. HehasbeenworkingwithCreativeSoftDevel-
[3] C.Bull,‘‘Strategicissuesincustomerrelationshipmanagement(CRM) opmentCompany,since2013.Since2013,heis
implementation,’’ Bus. Process Manage. J., vol. 9, no. 5, pp.592–602, currently working as the CEO with Software
| Oct.2003.      |        |                |        |            |              |                |     |     | Development     | Operating | Company.     | He            | has been |
| -------------- | ------ | -------------- | ------ | ---------- | ------------ | -------------- | --- | --- | --------------- | --------- | ------------ | ------------- | -------- |
| [4] Z. Soltani | and N. | J. Navimipour, |        | ‘‘Customer | relationship | management     |     |     |                 |           |              |               |          |
|                |        |                |        |            |              |                |     |     | involved in     | various   | developments | including     | sys-     |
| mechanisms:    | A      | systematic     | review | of the     | state of the | art literature | and |     |                 |           |              |               |          |
|                |        |                |        |            |              |                |     |     | tem integration | (SI),     | mobile       | applications, | and      |
recommendations for future research,’’ Comput. Hum. Behav., vol. 61, solution development. Currently, his company develops customer data
pp.667–688,Aug.2016. platform(CDP)solutionsandprovidesservicestoenterprises.Hisresearch
[5] S.-Y. Kim, T.-S. Jung, E.-H. Suh, and H.-S. Hwang, ‘‘Customer interestsincludemobileappdevelopment,CDP,machinelearning,anddata-
segmentationandstrategydevelopmentbasedoncustomerlifetimevalue:
drivendecision-makingthroughbigdataanalysis.
Acasestudy,’’ExpertSyst.Appl.,vol.31,no.1,pp.101–107,Jul.2006.
[6] H.Wilson,E.Daniel,andM.McDonald,‘‘Factorsforsuccessincustomer
relationshipmanagement(CRM)systems,’’J.MarketingManage.,vol.18,
nos.1–2,pp.193–219,Feb.2002.
| [7] I. J.  | Chen and | K. Popovich, | ‘‘Understanding |     | customer      |      | relationship |     |        |                                 |     |     |     |
| ---------- | -------- | ------------ | --------------- | --- | ------------- | ---- | ------------ | --- | ------ | ------------------------------- | --- | --- | --- |
| management | (CRM):   | People,      | process         | and | technology,’’ | Bus. | Process      |     |        |                                 |     |     |     |
|            |          |              |                 |     |               |      |              |     | MINGYU | JO (GraduateStudentMember,IEEE) |     |     |     |
Manage.J.,vol.9,no.5,pp.672–688,Oct.2003.
|     |     |     |     |     |     |     |     |     | received | the B.S. | and M.S. | degrees | in com- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ------- | ------- |
[8] M.KihnandC.B.O’Hara,CustomerDataPlatforms:UsePeopleDataTo
|     |     |     |     |     |     |     |     |     | puter engineering | from | the School | of  | Computer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---- | ---------- | --- | -------- |
Transf.FutureMarketingEngagement.Hoboken,NJ,USA:Wiley,2020. Science and Engineering, Chung-Ang Univer-
[9] J.T.Wei,S.Y.Lin,andH.H.Wu,‘‘AreviewoftheapplicationofRFM sity, Seoul, South Korea, in 2021 and 2023,
model,’’Afr.J.Bus.Manage.,vol.4,no.19,p.4199,2010.
|            |           |          |       |                  |     |           |           |     | respectively, | where | he is currently | pursuing | the |
| ---------- | --------- | -------- | ----- | ---------------- | --- | --------- | --------- | --- | ------------- | ----- | --------------- | -------- | --- |
| [10] H.-H. | Wu, S.-Y. | Lin, and | C.-W. | Liu, ‘‘Analyzing |     | patients’ | values by |     |               |       |                 |          |     |
Ph.D.degreeinsoftwareengineering.Hisresearch
applyingclusteranalysisandLRFMmodelinapediatricdentalclinicin
interestsincludedistributedsystems,highperfor-
Taiwan,’’ScientificWorldJ.,vol.2014,pp.1–7,Jun.2014.
mancecomputing,operatingsystems,andmobile
[11] R.Mahfuza,R.S.Uddin,Y.Rahman,andMd.A.Hai,‘‘Acomprehensive
framework for superstore bus. With employing effective clustering systems.
| techniques,’’ | in  | Proc. 24th | Int. Conf. | Comput. | Inf. | Technol. | (ICCIT), |     |     |     |     |     |     |
| ------------- | --- | ---------- | ---------- | ------- | ---- | -------- | -------- | --- | --- | --- | --- | --- | --- |
Dec.2021,pp.1–6.
[12] Y.-L.Chen,M.-H.Kuo,S.-Y.Wu,andK.Tang,‘‘Discoveringrecency,
frequency,andmonetary(RFM)sequentialpatternsfromcustomers’pur-
chasingdata,’’Electron.CommerceRes.Appl.,vol.8,no.5,pp.241–251,
|           |     |     |     |     |     |     |     |     |         | (Member, | IEEE) | received | the |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ----- | -------- | --- |
| Oct.2009. |     |     |     |     |     |     |     |     | ILKYEUN | RA       |       |          |     |
combinedB.S.andM.S.degreeincomputersci-
| [13] A. A. | Zoeram | and A. | K. Mazidi, | ‘‘New | approach | for | customer |     |     |     |     |     |     |
| ---------- | ------ | ------ | ---------- | ----- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- |
encefromSogangUniversity,theM.S.degreein
clusteringbyintegratingtheLRFMmodelandfuzzyinferencesystem,’’
computersciencefromtheUniversityofColorado
IranianJ.Manage.Stud.,vol.11,no.2,pp.351–378,Apr.2018.
[14] A.J.Christy,A.Umamakeswari,L.Priyatharsini,andA.Neyaa,‘‘RFM Boulder, and the Ph.D. degree in computer and
ranking—Aneffectiveapproachtocustomersegmentation,’’J.KingSaud information science from Syracuse University,
Univ.-Comput.Inf.Sci.,vol.33,no.10,pp.1251–1257,Dec.2021. in2001.HewasaResearchStaffMemberatthe
[15] X.HeandC.Li,‘‘Theresearchandapplicationofcustomersegmentation LG Information and Communications (currently
one-commercewebsites,’’inProc.6thInt.Conf.Digit.Home(ICDH), LG Telecom) Research Center. He joined the
Dec.2016,pp.203–208.
|            |           |           |                 |     |        |         |             |     | Department | of Computer | Science | and | Engineer- |
| ---------- | --------- | --------- | --------------- | --- | ------ | ------- | ----------- | --- | ---------- | ----------- | ------- | --- | --------- |
| [16] C. O. | Sakar, S. | O. Polat, | M. Katircioglu, |     | and Y. | Kastro, | ‘‘Real-time |     |            |             |         |     |           |
ing,UniversityofColoradoDenver,in2001.Hisresearchinterestsinclude
| prediction | of online | shoppers’ | purchasing |     | intention | using | multilayer |                    |                     |             |        |           |     |
| ---------- | --------- | --------- | ---------- | --- | --------- | ----- | ---------- | ------------------ | ------------------- | ----------- | ------ | --------- | --- |
|            |           |           |            |     |           |       |            | computer networks, | developing adaptive | distributed | system | software, | and |
perceptronandLSTMrecurrentneuralnetworks,’’NeuralComput.Appl., high speed communication system software to support high performance
vol.31,no.10,pp.6893–6908,Oct.2019. distributedcomputingapplications.
[17] Y.-S.ShihandM.-H.Lin,‘‘Alstmapproachforsalesforecastingofgoods
withshort-termdemandsine-commerce,’’inProc.AsianConf.Intell.Inf.
DatabaseSyst.,2019,pp.244–256.
[18] Y.Issaoui,A.Khiat,A.Bahnasse,andH.Ouajji,‘‘AnadvancedLSTM
modelforoptimalschedulinginsmartlogisticenvironment:E-commerce
case,’’IEEEAccess,vol.9,pp.126337–126356,2021. SANGOH PARK (Member, IEEE) received the
| [19] C. Wang, | ‘‘Efficient | customer | segmentation |     | in digital | marketing | using |     |     |     |     |     |     |
| ------------- | ----------- | -------- | ------------ | --- | ---------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
B.S.,M.S.,andPh.D.degreesfromtheSchoolof
deeplearningwithswarmintelligenceapproach,’’Inf.Process.Manage.,
|     |     |     |     |     |     |     |     |     | Computer | Science | and Engineering, | Chung-Ang |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---------------- | --------- | --- |
vol.59,no.6,Nov.2022,Art.no.103085.
University,in2005,2007,and2010,respectively.
| [20] M. | S. Kasem, | M. Hamada, | and | I. Taj-Eddin, | ‘‘Customer |     | profiling, |     |     |     |     |     |     |
| ------- | --------- | ---------- | --- | ------------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
HeworkedasaSeniorResearcherwithGlobal
segmentation,andsalespredictionusingAIindirectmarketing,’’Neural Science Experimental Data Hub Center, Korea
Comput.Appl.,vol.36,no.9,pp.4995–5005,Mar.2024.
InstituteofScienceandTechnologyInformation,
[21] K.Sriprasadh,S.Palit,B.Pravallika,Manjunatha,R.Lenka,andA.Singla,
from2012to2017,andaResearchProfessorat
‘‘Clientsegmentationandcustomizationine-commerce:Applicationsof
theSchoolofComputerScienceandEngineering.
| machine | learning | from a | management | perspective,’’ |     | in Proc. | Int. Conf. |     |             |         |       |           |           |
| ------- | -------- | ------ | ---------- | -------------- | --- | -------- | ---------- | --- | ----------- | ------- | ----- | --------- | --------- |
|         |          |        |            |                |     |          |            |     | He has been | working | as an | Assistant | Professor |
Commun.,Comput.Sci.Eng.(IC3SE),May2024,pp.1423–1427.
[22] M. Rajyalaxmi, C. Vijai, K. Srivastava, N. Kalyan, B. Pravallika, and with the School of Computer Science and Engineering, Chung-Ang
A.Dutt, ‘‘Application of machine learning algorithms for customer University,since2017.Hisresearchinterestsincludeembeddedsystems,big
segmentation in e-commerce management,’’ in Proc. Int. Conf. Sci. datasystems,cyberphysicalsystems,andLinuxsystems.
Technol.Eng.Manage.(ICSTEM),Apr.2024,pp.1–5.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 12541 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |