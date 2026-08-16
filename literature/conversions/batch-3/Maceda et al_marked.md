---
conversion_metadata:
  converted_at: "2026-07-21T14:09:01Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Maceda et al.pdf"
  source_pdf_sha256: "4cba4f1b9fd897fcdb248d961795c82cd0a348568ced80e054c545968e3bcb9f"
  page_count: 6
  markdown_char_count: 67545
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Classifying Sentiments on Social Media Texts: A GPT-4
Preliminary Study

Lany L. MACEDA*
Bicol University, Legazpi City, Philippines

Jennifer L. Llovido
Bicol University, Legazpi City, Philippines

Miles B. Artiaga
Bicol University, Legazpi City, Philippines

Mideth B. Abisado
National University, Manila, Philippines

ABSTRACT
In today’s digital age, social media has become a hub for people
to express their thoughts and feelings. Sentiment classification dis-
cerns public opinions and trends to understand their sentiments
towards a certain topic. Often, achieving accurate sentiment classi-
fications in large datasets necessitate the use of human-annotated
training data which can be costly and time-consuming. Large Lan-
guage Models (LLMs) like the Generative Pre-trained models by
OpenAI have surged in popularity due to its capabilities in under-
standing the given tasks. In this preliminary study, we report the
performance of the latest OpenAI GPT-4 using zero- and one-shot
learning approaches on classifying sentiments when fed with social
media dataset. Notably, the latter approach written in English which
mimics the instructions designed for human annotators, achieved a
substantial agreement (k = 0.77) with human annotations, display-
ing high accuracy, precision, and recall accordingly even without
explicit training data. Meanwhile, the fine-tuned mBERT resulted
to lower evaluation scores than the GPT-4. Our findings provide
foundational insights into the strengths and limitations of GPT-4
for sentiment classification in a social media dataset, setting the
groundwork for broad future research in this field.

CCS CONCEPTS
• Computing methodologies; • Artificial Intelligence; • Natu-
ral Language Processing; • Natural Language Generation;

KEYWORDS
GPT-4, Sentiment Annotation, LLM Prompting, Social Media Data

ACM Reference Format:
Lany L. MACEDA*, Jennifer L. Llovido, Miles B. Artiaga, and Mideth B.
Abisado. 2023. Classifying Sentiments on Social Media Texts: A GPT-4
Preliminary Study. In 2023 7th International Conference on Natural Language
Processing and Information Retrieval (NLPIR 2023), December 15–17, 2023,
Seoul, Republic of Korea. ACM, New York, NY, USA, 6 pages. https://doi.org/
10.1145/3639233.3639353

1 INTRODUCTION
Social media platforms have become virtual hubs where people
share their ideas, sentiments, and opinions on a wide range of topics

Publication rights licensed to ACM. ACM acknowledges that this contribution was
authored or co-authored by an employee, contractor or affiliate of a national govern-
ment. As such, the Government retains a nonexclusive, royalty-free right to publish or
reproduce this article, or to allow others to do so, for Government purposes only.
NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0922-7/23/12. . . $15.00
https://doi.org/10.1145/3639233.3639353

[4, 19], creating a large corpus of unlabeled and unstructured data.
Such data are often unstructured, multilingual, multicultural [1],
and involves the use of slangs, acronyms, or emoticons. In contrast
to newswire and weblogs, there is almost no subsequent editing or
filtering of the incoming textual content [30]. These occurrences
become bottlenecks for many Natural Language Processing (NLP)
tasks including classifying of sentiments [17].

Sentiment analysis is a subfield of NLP that automatically eval-
uates natural language expressions, identifies key assertions or
viewpoints, and categorizes them based on their emotional stance
[34]. The insights produced can be instrumental in making informed
decisions in real life situations [17]. For instance, [18] and [2] rec-
ommended continuous improvement of educational programs in
the Philippines. These studies undergo rigorous manual annotation
of each document performed by field experts to establish a gold
standard set to train a machine or deep learning model.

In 2017, the introduction of Transformers [31], has since become
the foundation of various Large Language Models (LLMs) [3, 6]in
NLP [15]. These models utilize computational techniques and sta-
tistical approaches to produce text resembling human language,
allowing for a deep understanding of context and the expression
of dynamic concepts [25]. LLMs are tasked to perform tasks using
carefully crafted natural language prompts. According to [37], this
paradigm could be valuable because it may enable generation of
high-quality annotations with less demand for human annotators
due to its state-of-the-art performance on various NLP tasks.

The Generative Pre-trained Transformer 4 (GPT-4), launched in
March 2023 by OpenAI [22], is a Transformer-based model that has
undergone pre-training to predict the subsequent token in a doc-
ument. This training utilizes a combination of publicly accessible
data (such as internet content) and data licensed from third-party
providers. Although OpenAI have claimed state-of-the-art results of
GPT-4 on difficult based on the conducted preliminary model eval-
uation, they reported limited information regarding the model’s
architecture (including its size), the hardware used, the compu-
tational resources for training, the dataset creation process, the
training methodology, or related details, due to the competitive
environment and the safety concerns associated with extensive
models like GPT-4 [22].

In this preliminary study, we aim to contribute foundation for
understanding the potential application of an advanced language
model in the field of sentiment analysis, by evaluating GPT-4 on so-
cial media texts and compare its performance to human-annotated
dataset. Specifically, we utilize the human-annotated social media
data related to the implementation of the Philippine Universal Ac-
cess to Quality and Tertiary Education (UAQTE). We emphasize that

---

<!-- PAGE 2 -->

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Lany Maceda et al.

this dataset encompasses the use of slangs, emoticons, and multiple
low-resourced languages within a single sentence such as Filipino,
Bicol, and other native languages in the Philippines, a phenomenon
known as code-mixing. Considering the nature of this dataset, we
further compare the evaluation results to Multilingual Bidirectional
Encoder Representations from Transformers (mBERT) [6] model
and perform manual error analysis to show the capabilities and
limitations of GPT-4 for sentiment analysis task.

2 RELATED WORKS
2.1 Sentiment Classification on Social Media

Texts

Social media platforms provide vast amount of user-generated con-
tent that can be used to gauge public opinion or sentiments on
various topics. However, low-resource languages have received less
attention due to the scarcity of annotated datasets, limited access
to computational resources, and shortage of experts in the field
[36] including the Philippines and its native languages. There are
two most commonly used approaches for sentiment classification:
supervised learning and unsupervised learning [14, 20]. In the su-
pervised learning approach, a machine learning or deep learning
algorithm is usually trained to classify sentiments using a manually
annotated dataset in which human annotators have identified the
sentiment of each document. For instance, [18] used mBERT to
classify large code-mixed texts from various social media platforms
such as Twitter, Facebook, and YouTube, achieving the highest ac-
curacy of 80.21% using a human-annotated training set. Similarly,
[10] used mBERT to classify the sentiments of social media posts
which achieved the F1-scores of 0.603, 0.698, and 0.595 for the Tamil,
Malayalam, and Kannada code-mixed languages, respectively. In the
study of [29], text data underwent comprehensive preprocessing
steps, including emoji, repeated characters, and punctuation re-
moval. Traditional machine learning, deep learning, transfer learn-
ing, and hybrid deep learning models were then compared before
and after these processes. The CNN+BiLSTM hybrid deep learning
model achieved the highest accuracy of 0.66 on preprocessed Tamil
code-mixed data.

Alternatively, unsupervised techniques may incur minimal re-
source costs, but the outcomes they yield can often lack clarity and
interpretability [14], as exemplified by the utilization of lexicon-
based approaches. These existing lexicons are composed of mainly
words that are deemed to carry sentiments but can be quite limited
when applied to new tasks due to numerous out-of-vocabulary
words [30]. According to [35], instead of training task-specific mod-
els, a pre-trained LLM could be used directly for various tasks
without fine-tuning through prompt learning.

In this study, we compare the evaluation results of GPT-4 against
the fine-tuned Multilingual BERT (mBERT), a multilingual version
of BERT trained on 104 languages including English and widely
used local languages in the Philippines such as Tagalog, Waray, and
Cebuano.

2.2 GPT Models
Several studies have assessed the capabilities of LLM like GPT in var-
ious tasks, [7] conducted various annotation task and showed that

ChatGPT, a chatbot that uses GPT model, outperformed Mechani-
cal Turk human annotators. Similarly, [9] reported that ChatGPT
demonstrated great potential as a data annotation tool even with
simple prompt design. In cost-effective scenarios, GPT-3 labeling
can outperform human labeling, and incorporating a combination
of GPT-3 and human labeling can lead to further enhancements in
performance [32]. In [13], emphasized the effectiveness of GPT-3.5
in overcoming the standard linguistic nuances of sentiment analysis,
such as contextualization and sarcasm detection. We also observed
trends in assessing GPT-4 in various licensing examinations[11],
[12] and medical problems [11, 15, 21].

These studies have focused on using monolingual datasets or
publicly available data. It remains uncertain whether these open
datasets are included in the model’s training data or not. In their
technical report, OpenAI acknowledged the possible risk of unin-
tended contamination on their benchmark assessments, where the
model might have inadvertently gain access to the test questions
and their corresponding answers [22]. Further, in the findings of [5],
LLMs like GPT-4 and GPT-3.5 can undergo significant transforma-
tions within a relatively brief period, emphasizing the importance
of ongoing monitoring of the model for possible enhancements. In
utilizing a GPT-4 model to classify social media texts, specifically
Tweets related to the topic of abortion legalization in the United
Stated of America, [16] found that the Few-shot approach method
exhibits a higher degree of similarity to human experts.

To the best of our knowledge, there have been no studies that
have conducted sentiment classification on a social media dataset
using the GPT-4 model, particularly on datasets that are both low-
resourced and code-mixed.

3 METHODOLOGY
3.1 Data
Due to our limited access to GPT-4, we opted to work with a dataset
comprising 200 unprocessed data points for each sentiment cate-
gory: neutral, negative, and positive, sourced from [18]. This se-
lection resulted in a total of 600 samples. These data points were
gathered from Facebook, Twitter, and YouTube, specifically in the
context of UAQTE. Each data sample was manually annotated by
human experts, with a sentiment label denoted by values [0, 1, 2],
which correspond to neutral, negative, and positive sentiments,
respectively, and prepended a number for traceability of results.

As discussed in Section 2, it is worth noting that social media
texts differ from conventional attribute-value data due to their inher-
ently noisy, decentralized, unstructured, and dynamically evolving
nature [8].

3.2 Prompt Template Design
We first experimented two prompt variations written in English.
For this, we employ zero and n-shot learning approaches, where n
specifies the number of examples used in a prompt.

For our zero-shot learning approach, we designed a straight-
forward prompt which follows a prompt structure of [Instruc-
tion/Constraints/n samples]: “Classify the sentiments of the following
texts. For each item, respond only 0, 1, or 2 to indicate whether the
sentiment is neutral, negative, or positive, respectively. In cases of
ambiguity, choose the prevailing sentiment”. For the second prompt,

---

<!-- PAGE 3 -->

Classifying Sentiments on Social Media Texts: A GPT-4 Preliminary Study

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Figure 1: Sentiment Annotation Process using GPT-4 API. (1) Each data sample is prepended with a number; (2) Get n chunk
of data samples; (3) Include the n data samples in the prompt; (4) Access the GPT-4 model through calling its API using the
parameters set; (5) Results are printed and saved in a .csv file; and (5) Loop through the same process until n samples

we mimic the annotation instructions designed for the human an-
notators as our prompt instruction and provided a brief sentiment
description and one example for each sentiment category, hence
referred to as one-shot learning. This approach follows a simi-
lar prompt structure to zero-shot, except that we added identity
modifier or persona “You are the CHED-UniFAST program coordi-
nator in the Philippines” as our System’s prompt which was used
to set the context of the dialogue, followed by the instruction and
examples. The final prompt structure of one-shot learning is [Per-
sona/Instruction/Examples/Constraints/n samples].

In [33] suggested to evaluate different prompt designs such as
use of code-mixed prompt. We selected the successful learning
approach as the basis for our code-mixed prompt. To write the
code-mixed prompt, we engaged with a native Bicolano speaker to
translate the English prompt using their own comprehension and
natural language, free from restrictions regarding usage of symbols
or abbreviations. The final code-mixed prompt consisted the use of
various languages, slang, abbreviation, and misspellings: “Iclassify
mo ung sintemyento netong mga social media texts gamit an mga
minasunod na polarities about sa pag implement ng Philippine RA
10931 UAQTE Act program. . .”. This approach allowed us to capture
the informal and dynamic language style prevalent in our dataset.

3.3 Sentiment Annotation using GPT-4
The original GPT model [23] is composed of 12-layer decoder-
only Transformer with masked self-attention heads. Its primary
capability is fine-tuning for specific downstream tasks.

As of the writing, GPT-4 is by far the most advanced model
released by OpenAI. GPT-4’s text input capability was released
via ChatGPT and the API. In this study, we use the GPT-4 API
with 8,192 tokens context model, comprising of both prompt and
completion which entails corresponding price per token. During our

initial test runs, GPT-4 is costly especially with longer prompts. To
reduce our costs, we employed looping of batch processing, which
means that for each request, it will process 30 and 15 samples from
the dataset for zero- and one-shot prompts respectively, instead of
individually sending each data sample to API. This API allows us to
communicate with the model by specifying a set of parameters that
control its behavior during text generation, such as a temperature
of 0, and a 200 maximum output tokens for every API call. We only
run the experiment once as our final evaluation and save the output
in a .csv file. Figure 1 summarizes our sentiment annotation process
using GPT-4 API.

3.4 Evaluation
Following the evaluation of [28] to analyze the agreement or inter-
rater reliability among annotators, we used Cohen’s Kappa. Table
1 shows the interpretation of the Kappa value obtained. Addition-
ally, we employed commonly used classification metrics such as
accuracy, precision, and recall to evaluate the model’s predictive
accuracy and its ability to correctly classify sentiments. Accuracy
measures the overall correctness of model predictions, while pre-
cision focuses on the proportion of true positives among positive
predictions, and recall quantifies the ability of the model to capture
all positive instances.

Further, we compare the evaluation results against the fine-tuned
Multilingual BERT (mBERT). It is worth noting that the dataset
used for both models underwent no preprocessing. For fine-tuning
mBERT a 70:30 split ratio for training and testing sets, a learning-
rate and batch size of 2e-5 and 16 were employed. Both mBERT and
GPT are Transformer based pre-trained models.

---

<!-- PAGE 4 -->

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Lany Maceda et al.

Table 1: Interpretation of Cohen’s Kappa

Kappa value

Interpretation

<0.20
0.21-0.40
0.41-0.60
0.61-0.80
0.81-1.00

Poor agreement
Fair agreement
Moderate agreement
Substantial agreement
Very good agreement

4 RESULTS AND DISCUSSION
In Table 2, we present the performance of GPT-4 using various
learning approaches in a classification task, each evaluated based
on Cohen’s Kappa value, accuracy, precision, and recall. We run the
experiment once as our final evaluation due to our limited access
to GPT-4 API and increased cost associated with longer prompts.
Compared to the achieved score of the prompt that uses zero-
shot approach, the Kappa values of prompts written in English and
Code-mixed using the one-shot approach achieved 0.77 and 0.73
respectively, which indicate that there is a substantial and statisti-
cally significant level of agreement between the model’s predictions
and the human annotations if context and identity modifier are
given. Accordingly, these prompts achieved an accuracy score of
0.85 and 0.8250 which demonstrates a high proportion of correct
classifications, emphasizing the capability of the model’s predic-
tions even without explicit training data to learn the sentiments
of an unprocessed code-mixed dataset. The matching precision
and recall values signify that the model maintains a balanced ap-
proach, effectively capturing positive instances while minimizing
false positives. Meanwhile, the fine-tuned mBERT resulted to lower
results than the GPT-4. This result is similar to the study of [24],
where the GPT-3 model beats the BERT-base model in Marathi Text
Classification.

As stated by [16], GPT models are highly sensitive to prompts.
Interestingly, the code-mixed prompt achieved scores that were
not significantly different from the prompt written in English. We
initially conclude that the use of words or language in the prompt
may not be the primary issue, as long as the prompt provides
identity modifier (System’s prompt), adequate instructions, and
context.

4.1 Error Analysis
We collected five samples from our annotated dataset to manually
examine instances where the model’s predictions diverged from
or did not match the human-annotated data. Our primary observa-
tion was despite our explicit instruction to respond in numerical

values [0, 1, 2] which corresponds to sentiments: neutral, negative,
and positive, the one-shot prompts received responses in words,
sometimes numerical values, unlike the zero-shot prompt which
responded the correct format for all items. Hence, post-cleaning of
the collected responses was necessary to evaluate GPT-4’s perfor-
mance on various metrics. These inaccuracies and inconsistencies
have been also observed in the study of [27].

In Table 3 we focused on the results of GPT-4 model; the first
sample written in non-English text was annotated correctly by all
prompts; the second and third example, utilizing a one-shot prompt,
correctly identified the text implying an announcement even with
the inclusion of positive phrase like “kayo ang bida!”. This pattern
was consistently observed in other samples, emphasizing the sig-
nificance of incorporating constraints for improved classification
accuracy. While one-shot prompt achieved high evaluation scores,
it still predicted inaccurate sentiments as shown in the fourth and
fifth examples where the latter uses a Filipino slang word “cutie”
which means “to manifest something they want to have/achieve” [26].
We hypothesize that this could be due to potential influence of the
model’s pre-trained knowledge that might introduce interpretative
variations, particularly in a domain-specific contexts. Interestingly,
mBERT correctly classified all data samples despite its low evalua-
tion scores.

5 CONCLUSION
In this preliminary study, we explored the application of GPT-4
for classifying sentiments in social media texts. The results demon-
strated GPT-4’s capability in handling diverse linguistic inputs
without using any training data, provided that the prompt should
contain specific and adequate instructions. However, challenges
were identified in instances involving slang or domain-specific
language.

6 LIMITATIONS AND FUTURE WORKS
Despite the impressive evaluation score obtained by GPT-4 in an-
notating the dataset, inaccuracies were observed on our experi-
ments. We initially suggest employing GPT-4 to participate in the
annotation process, alongside human annotators. The GPT-4’s per-
formance is dependent to the dataset they were trained on and to
the quality of the annotated data used for evaluation. Any biases
from these datasets may directly affect the model’s performance.
Additionally, the model’s effectiveness may vary across different
domains and industries, as it might not be well-suited to highly
specialized subjects or contexts not adequately covered in this ex-
periment.

In this study, code-mixed dataset was used to evaluate the GPT-
4 model capabilities in sentiment classification, since significant

Table 2: Performance of GPT-4 and mBERT model

Learning Approach

GPT-Zero-shot (English)
GPT-One-shot (English)
GPT-One-shot (Code-mixed)
mBERT

Kappa value Accuracy

Precision

0.50
0.77
0.73
-

0.6683
0.85
0.8250
0.8277

0.6870
0.8665
0.8432
0.8381

Recall

0.6683
0.85
0.8250
0.8252

---

<!-- PAGE 5 -->

Classifying Sentiments on Social Media Texts: A GPT-4 Preliminary Study

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Table 3: Examples of Classified Sentiments by GPT-4 and mBERT

No.

Human

mBERT

Zero-shot

One-shot
(EN)

One-shot
(CM)

Examples

1

2

3

4

5

Negative

Negative

Negative

Negative

Negative

Neutral

Neutral

Positive

Neutral

Positive

Neutral

Neutral

Positive

Neutral

Neutral

Negative

Negative

Negative

Neutral

Negative

Positive

Positive

Positive

Neutral

Neutral

Kasuya man kan bank Portal! Subago pa Password expired
dai na nag untok.hahaha.
(EN: The bank portal is frustrating! My password has been
expired for a while now, and it’s not getting any
better.hahaha)
TES Update #85 October pa lang parang Pasko na sa
UniFAST! TES Cuties ng SOCCSKSARGEN, kayo ang bida
ngayong alas otso gabi!
(EN: TES Update #85, it’s only October, but it already feels
like Christmas at UniFAST! TES Cuties of
SOCCSKSARGEN, you’re the stars tonight at eight
o’clock!)
Gawis ay agsapa, PINASkolars! Reminding again our TES
Beneficiaries to answer our #quickpoll and Google Form
that you can locate by clicking this #tesgrant. Iyaman!
Hello po just wanna ask po kung kailan po kaya ang
realese ng TDP? Medyo matagal na din po kasi yunh
sakin di ko pa rin po natatanggap Salamat po
(EN: Hello, I just want to ask when will the TDP be
released? It’s been a while, and I still haven’t received it.
Thank you.)
Ched Unifast Cutie

results were obtained from the experiments, this suggests that
future studies could focus on testing GPT-4 on purely-written native
and less-common languages, promoting inclusivity and broadening
the scope of sentiment analysis.

ACKNOWLEDGMENTS
The researchers would like to thank the Philippine Commission
on Higher Education (CHEd) Leading the Advancement of Knowl-
edge in Agriculture and Science (LAKAS) Project No. 2021-007,
eParticipation 2.1: Harnessing Natural Language Processing (NLP)
for Community Participation, for providing the necessary funds to
make this research possible. The researchers are truly grateful for
their contribution to the research.

REFERENCES
[1] Marvin M. Agüero-Torales, José I. Abreu Salas, and Antonio G. López-Herrera.
2021. Deep learning and multilingual sentiment analysis on social media data:
An overview. Appl Soft Comput 107, (August 2021). https://doi.org/10.1016/j.asoc.
2021.107373

[2] Maria Charmy A Arispe, Joni Neil B Capucao, Floradel S Relucio, and Daniel
E., Jr. Maligat. 2019. Teachers’ sentiments to Bikol MTB-MLE: Using sentiment
analysis and text mining techniques. International Journal of Research Studies in
Education 8, 4 (July 2019). https://doi.org/10.5861/ijrse.2019.4906

[3] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan,
Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter,
Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot Learners.
(May 2020). Retrieved from http://arxiv.org/abs/2005.14165

[4] Mary Joy Canon, Christian Sy, and Lea Austero. 2019. Discovering themes from
online news articles on the 2018 mt. mayon eruption. In Proceedings - 2018

International Symposium on Computer, Consumer and Control, IS3C 2018, February
19, 2019. Institute of Electrical and Electronics Engineers Inc., 242–245. . https:
//doi.org/10.1109/IS3C.2018.00068

[5] Lingjiao Chen, Matei Zaharia, and James Zou. How Is ChatGPT’s Behavior Chang-

ing over Time?

[6] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-
training of Deep Bidirectional Transformers for Language Understanding. (Octo-
ber 2018). Retrieved from https://arxiv.org/pdf/1810.04805v2

[7] Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli. 2023. ChatGPT outperforms
crowd workers for text-annotation tasks. Proceedings of the National Academy of
Sciences 120, 30 (July 2023). https://doi.org/10.1073/pnas.2305016120

[8] Pritam Gundecha and Huan Liu. 2012. Mining Social Media: A Brief Introduction.
In 2012 TutORials in Operations Research. INFORMS, 1–17. https://doi.org/10.1287/
educ.1120.0105

[9] Fan Huang, Haewoon Kwak, and Jisun An. 2023. Is ChatGPT better than Human
Annotators? Potential and Limitations of ChatGPT in Explaining Implicit Hate
Speech. In ACM Web Conference 2023 - Companion of the World Wide Web Con-
ference, WWW 2023, April 30, 2023. Association for Computing Machinery, Inc,
294–297. . https://doi.org/10.1145/3543873.3587368

[10] Adaikkan Kalaivani and Durairaj Thenmozhi. 2021. Multilingual Sentiment Analy-
sis in Tamil, Malayalam, and Kannada code-mixed social media posts using MBERT.
Retrieved from https://ceur-ws.org/Vol-3159/T6-16.pdf

[11] Jungo Kasai, Yuhei Kasai, Keisuke Sakaguchi, Yutaro Yamada, and Dragomir
Radev. 2023. Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing
Examinations. (March 2023). Retrieved from http://arxiv.org/abs/2303.18027
[12] Daniel Martin Katz, Michael James Bommarito, Shang Gao, and Pablo David
Arredondo. GPT-4 Passes the Bar Exam. Retrieved from http://dx.doi.org/10.2139/
ssrn.4389233

[13] Kiana Kheiri and Hamid Karimi. 2023. SentimentGPT: Exploiting GPT for Ad-
vanced Sentiment Analysis and its Departure from Current Machine Learning.
(July 2023). Retrieved from http://arxiv.org/abs/2307.10234

[14] Monica Lee and John Levi Martin. 2015. Coding, counting and cultural cartogra-
phy. Am J Cult Sociol 3, 1 (January 2015), 1–33. https://doi.org/10.1057/ajcs.2014.13
[15] Zhengliang Liu, Xiaowei Yu, Lu Zhang, Zihao Wu, Chao Cao, Haixing Dai, Lin
Zhao, Wei Liu, Dinggang Shen, Quanzheng Li, Tianming Liu, Dajiang Zhu, and
Xiang Li. 2023. DeID-GPT: Zero-shot Medical Text De-Identification by GPT-4.
(March 2023). Retrieved from http://arxiv.org/abs/2303.11032

[16] Chandreen Liyanage, Ravi Gokani, and Vijay Mago. GPT-4 as a Twitter Data
Annotator: Unraveling Its Performance on a Stance Classification Task. https:

---

<!-- PAGE 6 -->

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Lany Maceda et al.

//doi.org/10.36227/techrxiv.24143706.v1

[17] Ismini Lourentzou, Kabir Manghnani, and Chengxiang Zhai. Adapting Sequence
to Sequence Models for Text Normalization in Social Media. Retrieved from https:
//arxiv.org/abs/1904.06100

[18] Lany L Maceda, Arlene A Satuito, and Mideth B Abisado. Sentiment Analy-
sis of Code-mixed Social Media Data on Philippine UAQTE using Fine-tuned
mBERT Model. IJACSA) International Journal of Advanced Computer Science and
Applications 14, 7 , 2023

[19] Lany MacEda, Jennifer Llovido, and Arlene Satuito. 2019. Categorization of
earthquake-related tweets using machine learning approaches. In Proceedings
- 2018 International Symposium on Computer, Consumer and Control, IS3C 2018,
February 19, 2019. Institute of Electrical and Electronics Engineers Inc., 229–232.
. https://doi.org/10.1109/IS3C.2018.00065

[20] Laura K. Nelson, Derek Burk, Marcel Knudsen, and Leslie McCall. 2021. The
Future of Coding: A Comparison of Hand-Coding and Three Types of Computer-
Assisted Text Analysis Methods. Sociol Methods Res 50, 1 (February 2021), 202–237.
https://doi.org/10.1177/0049124118769114

[21] Harsha Nori, Nicholas King, Scott Mayer McKinney, Dean Carignan, and Eric
Horvitz. 2023. Capabilities of GPT-4 on Medical Challenge Problems. (March
2023). Retrieved from http://arxiv.org/abs/2303.13375

[22] OpenAI. 2023. GPT-4 Technical Report. (March 2023). Retrieved from http://arxiv.

org/abs/2303.08774

[23] Alec Radford Openai, Karthik Narasimhan Openai, Tim Salimans Openai, and Ilya
Sutskever Openai. Improving Language Understanding by Generative Pre-Training.
Retrieved from https://api.semanticscholar.org/CorpusID:49313245

[24] Chandrashekhar S. Pawar and Ashwin Makwana. 2022. Comparison of BERT-Base
and GPT-3 for Marathi Text Classification. Lecture Notes in Electrical Engineering
936, (2022), 563–574. https://doi.org/10.1007/978-981-19-5037-7_40/COVER
[25] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya
Sutskever. Language Models are Unsupervised Multitask Learners. Retrieved from
https://api.semanticscholar.org/CorpusID:160025533

[26] John Patrick Ranara. 2023. From “Arjo Cutie” to “I will marry you, cutie”: A

timeline of Maine Mendoza and Arjo Atayde’s romance. Philstar Life.

[27] Jaromir Savelka, Arav Agarwal, Marshall An, Chris Bogart, and Majd Sakr. 2023.
Thrilled by Your Progress! Large Language Models (GPT-4) No Longer Struggle
to Pass Assessments in Higher Education Programming Courses. August 07, 2023.
Association for Computing Machinery (ACM), 78–92. .https://doi.org/10.1145/
3568813.3600142

[28] Thomas Schmidt, Manuel Burghardt, Katrin Dennerlein, and Christian Wolff.
Sentiment Annotation for Lessing’s Plays: Towards a Language Resource for

Sentiment Analysis on German Literary Texts. Conference on Language, Data
and Knowledge (LDK 2019), 2019, pp. 45–50. [Online]. Available: http://ceur-
ws.org/Vol-2402/paper9.pdf

[29] Kogilavani Shanmugavadivel, Sai Haritha Sampath, Pramod Nandhakumar,
Prasath Mahalingam, Malliga Subramanian, Prasanna Kumar Kumaresan, and
Ruba Priyadharshini. 2022. An analysis of machine learning models for sentiment
analysis of Tamil code-mixed data. Comput Speech Lang 76, (November 2022),
101407. https://doi.org/10.1016/J.CSL.2022.101407

[30] Olga Uryupina, Barbara Plank, Aliaksei Severyn, Agata Rotondi, and Alessandro
Moschitti. SenTube: A Corpus for Sentiment Analysis on YouTube Social Media.
In Proceedings of the Ninth International Conference on Language Resources and
Evaluation (LREC’14). Retrieved from http://www.lrec-conf.org/proceedings/
lrec2014/pdf/180_Paper.pdf

[31] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan
N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention Is All You Need.
(June 2017). Retrieved from http://arxiv.org/abs/1706.03762

[32] Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu, and Michael Zeng.
2021. Want To Reduce Labeling Cost? GPT-3 Can Help. (August 2021). Retrieved
from http://arxiv.org/abs/2108.13487

[33] Zengzhi Wang, Qiming Xie, Zixiang Ding, Yi Feng, and Rui Xia. 2023. Is ChatGPT
a Good Sentiment Analyzer? A Preliminary Study. (April 2023). Retrieved from
http://arxiv.org/abs/2304.04339

[34] Mayur Wankhade, Annavarapu Chandra Sekhara Rao, and Chaitanya Kulkarni.
2022. A survey on sentiment analysis methods, applications, and challenges. Artif
Intell Rev 55, 7 (October 2022), 5731–5780. https://doi.org/10.1007/s10462-022-
10144-1

[35] Ziang Xiao, Xingdi Yuan, Q. Vera Liao, Rania Abdelghani, and Pierre Yves Oudeyer.
2023. Supporting Qualitative Analysis with Large Language Models: Combining
Codebook with GPT-3 for Deductive Coding. In International Conference on Intel-
ligent User Interfaces, Proceedings IUI, March 27, 2023. Association for Computing
Machinery, 75–78. https://doi.org/10.1145/3581754.3584136

[36] Seid Muhie Yimam, Hizkiel Mitiku Alemayehu, Abinew Ali Ayele, and Chris
Biemann. Exploring Amharic Sentiment Analysis from Social Media Texts: Building
Annotation Tools and Classification Models. In Proceedings of the 28th International
Conference on Computational Linguistics, Jan. 2020, doi: 10.18653/v1/2020.coling-
main.91.

[37] Yiming Zhu, Peixian Zhang, Ehsan-Ul Haq, Pan Hui, and Gareth Tyson. 2023. Can
ChatGPT Reproduce Human-Generated Labels? A Study of Social Computing
Tasks. (April 2023). Retrieved from http://arxiv.org/abs/2304.10145

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Classifying Sentiments on Social Media Texts: A GPT-4
Preliminary Study

Lany L. MACEDA*
Bicol University, Legazpi City, Philippines

Jennifer L. Llovido
Bicol University, Legazpi City, Philippines

Miles B. Artiaga
Bicol University, Legazpi City, Philippines

Mideth B. Abisado
National University, Manila, Philippines

ABSTRACT
In today’s digital age, social media has become a hub for people
to express their thoughts and feelings. Sentiment classification dis-
cerns public opinions and trends to understand their sentiments
towards a certain topic. Often, achieving accurate sentiment classi-
fications in large datasets necessitate the use of human-annotated
training data which can be costly and time-consuming. Large Lan-
guage Models (LLMs) like the Generative Pre-trained models by
OpenAI have surged in popularity due to its capabilities in under-
standing the given tasks. In this preliminary study, we report the
performance of the latest OpenAI GPT-4 using zero- and one-shot
learning approaches on classifying sentiments when fed with social
media dataset. Notably, the latter approach written in English which
mimics the instructions designed for human annotators, achieved a
substantial agreement (k = 0.77) with human annotations, display-
ing high accuracy, precision, and recall accordingly even without
explicit training data. Meanwhile, the fine-tuned mBERT resulted
to lower evaluation scores than the GPT-4. Our findings provide
foundational insights into the strengths and limitations of GPT-4
for sentiment classification in a social media dataset, setting the
groundwork for broad future research in this field.

CCS CONCEPTS
• Computing methodologies; • Artificial Intelligence; • Natu-
ral Language Processing; • Natural Language Generation;

KEYWORDS
GPT-4, Sentiment Annotation, LLM Prompting, Social Media Data

ACM Reference Format:
Lany L. MACEDA*, Jennifer L. Llovido, Miles B. Artiaga, and Mideth B.
Abisado. 2023. Classifying Sentiments on Social Media Texts: A GPT-4
Preliminary Study. In 2023 7th International Conference on Natural Language
Processing and Information Retrieval (NLPIR 2023), December 15–17, 2023,
Seoul, Republic of Korea. ACM, New York, NY, USA, 6 pages. https://doi.org/
10.1145/3639233.3639353

1 INTRODUCTION
Social media platforms have become virtual hubs where people
share their ideas, sentiments, and opinions on a wide range of topics

Publication rights licensed to ACM. ACM acknowledges that this contribution was
authored or co-authored by an employee, contractor or affiliate of a national govern-
ment. As such, the Government retains a nonexclusive, royalty-free right to publish or
reproduce this article, or to allow others to do so, for Government purposes only.
NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 979-8-4007-0922-7/23/12. . . $15.00
https://doi.org/10.1145/3639233.3639353

[4, 19], creating a large corpus of unlabeled and unstructured data.
Such data are often unstructured, multilingual, multicultural [1],
and involves the use of slangs, acronyms, or emoticons. In contrast
to newswire and weblogs, there is almost no subsequent editing or
filtering of the incoming textual content [30]. These occurrences
become bottlenecks for many Natural Language Processing (NLP)
tasks including classifying of sentiments [17].

Sentiment analysis is a subfield of NLP that automatically eval-
uates natural language expressions, identifies key assertions or
viewpoints, and categorizes them based on their emotional stance
[34]. The insights produced can be instrumental in making informed
decisions in real life situations [17]. For instance, [18] and [2] rec-
ommended continuous improvement of educational programs in
the Philippines. These studies undergo rigorous manual annotation
of each document performed by field experts to establish a gold
standard set to train a machine or deep learning model.

In 2017, the introduction of Transformers [31], has since become
the foundation of various Large Language Models (LLMs) [3, 6]in
NLP [15]. These models utilize computational techniques and sta-
tistical approaches to produce text resembling human language,
allowing for a deep understanding of context and the expression
of dynamic concepts [25]. LLMs are tasked to perform tasks using
carefully crafted natural language prompts. According to [37], this
paradigm could be valuable because it may enable generation of
high-quality annotations with less demand for human annotators
due to its state-of-the-art performance on various NLP tasks.

The Generative Pre-trained Transformer 4 (GPT-4), launched in
March 2023 by OpenAI [22], is a Transformer-based model that has
undergone pre-training to predict the subsequent token in a doc-
ument. This training utilizes a combination of publicly accessible
data (such as internet content) and data licensed from third-party
providers. Although OpenAI have claimed state-of-the-art results of
GPT-4 on difficult based on the conducted preliminary model eval-
uation, they reported limited information regarding the model’s
architecture (including its size), the hardware used, the compu-
tational resources for training, the dataset creation process, the
training methodology, or related details, due to the competitive
environment and the safety concerns associated with extensive
models like GPT-4 [22].

In this preliminary study, we aim to contribute foundation for
understanding the potential application of an advanced language
model in the field of sentiment analysis, by evaluating GPT-4 on so-
cial media texts and compare its performance to human-annotated
dataset. Specifically, we utilize the human-annotated social media
data related to the implementation of the Philippine Universal Ac-
cess to Quality and Tertiary Education (UAQTE). We emphasize that

19NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Lany Maceda et al.

this dataset encompasses the use of slangs, emoticons, and multiple
low-resourced languages within a single sentence such as Filipino,
Bicol, and other native languages in the Philippines, a phenomenon
known as code-mixing. Considering the nature of this dataset, we
further compare the evaluation results to Multilingual Bidirectional
Encoder Representations from Transformers (mBERT) [6] model
and perform manual error analysis to show the capabilities and
limitations of GPT-4 for sentiment analysis task.

2 RELATED WORKS
2.1 Sentiment Classification on Social Media

Texts

Social media platforms provide vast amount of user-generated con-
tent that can be used to gauge public opinion or sentiments on
various topics. However, low-resource languages have received less
attention due to the scarcity of annotated datasets, limited access
to computational resources, and shortage of experts in the field
[36] including the Philippines and its native languages. There are
two most commonly used approaches for sentiment classification:
supervised learning and unsupervised learning [14, 20]. In the su-
pervised learning approach, a machine learning or deep learning
algorithm is usually trained to classify sentiments using a manually
annotated dataset in which human annotators have identified the
sentiment of each document. For instance, [18] used mBERT to
classify large code-mixed texts from various social media platforms
such as Twitter, Facebook, and YouTube, achieving the highest ac-
curacy of 80.21% using a human-annotated training set. Similarly,
[10] used mBERT to classify the sentiments of social media posts
which achieved the F1-scores of 0.603, 0.698, and 0.595 for the Tamil,
Malayalam, and Kannada code-mixed languages, respectively. In the
study of [29], text data underwent comprehensive preprocessing
steps, including emoji, repeated characters, and punctuation re-
moval. Traditional machine learning, deep learning, transfer learn-
ing, and hybrid deep learning models were then compared before
and after these processes. The CNN+BiLSTM hybrid deep learning
model achieved the highest accuracy of 0.66 on preprocessed Tamil
code-mixed data.

Alternatively, unsupervised techniques may incur minimal re-
source costs, but the outcomes they yield can often lack clarity and
interpretability [14], as exemplified by the utilization of lexicon-
based approaches. These existing lexicons are composed of mainly
words that are deemed to carry sentiments but can be quite limited
when applied to new tasks due to numerous out-of-vocabulary
words [30]. According to [35], instead of training task-specific mod-
els, a pre-trained LLM could be used directly for various tasks
without fine-tuning through prompt learning.

In this study, we compare the evaluation results of GPT-4 against
the fine-tuned Multilingual BERT (mBERT), a multilingual version
of BERT trained on 104 languages including English and widely
used local languages in the Philippines such as Tagalog, Waray, and
Cebuano.

2.2 GPT Models
Several studies have assessed the capabilities of LLM like GPT in var-
ious tasks, [7] conducted various annotation task and showed that

ChatGPT, a chatbot that uses GPT model, outperformed Mechani-
cal Turk human annotators. Similarly, [9] reported that ChatGPT
demonstrated great potential as a data annotation tool even with
simple prompt design. In cost-effective scenarios, GPT-3 labeling
can outperform human labeling, and incorporating a combination
of GPT-3 and human labeling can lead to further enhancements in
performance [32]. In [13], emphasized the effectiveness of GPT-3.5
in overcoming the standard linguistic nuances of sentiment analysis,
such as contextualization and sarcasm detection. We also observed
trends in assessing GPT-4 in various licensing examinations[11],
[12] and medical problems [11, 15, 21].

These studies have focused on using monolingual datasets or
publicly available data. It remains uncertain whether these open
datasets are included in the model’s training data or not. In their
technical report, OpenAI acknowledged the possible risk of unin-
tended contamination on their benchmark assessments, where the
model might have inadvertently gain access to the test questions
and their corresponding answers [22]. Further, in the findings of [5],
LLMs like GPT-4 and GPT-3.5 can undergo significant transforma-
tions within a relatively brief period, emphasizing the importance
of ongoing monitoring of the model for possible enhancements. In
utilizing a GPT-4 model to classify social media texts, specifically
Tweets related to the topic of abortion legalization in the United
Stated of America, [16] found that the Few-shot approach method
exhibits a higher degree of similarity to human experts.

To the best of our knowledge, there have been no studies that
have conducted sentiment classification on a social media dataset
using the GPT-4 model, particularly on datasets that are both low-
resourced and code-mixed.

3 METHODOLOGY
3.1 Data
Due to our limited access to GPT-4, we opted to work with a dataset
comprising 200 unprocessed data points for each sentiment cate-
gory: neutral, negative, and positive, sourced from [18]. This se-
lection resulted in a total of 600 samples. These data points were
gathered from Facebook, Twitter, and YouTube, specifically in the
context of UAQTE. Each data sample was manually annotated by
human experts, with a sentiment label denoted by values [0, 1, 2],
which correspond to neutral, negative, and positive sentiments,
respectively, and prepended a number for traceability of results.

As discussed in Section 2, it is worth noting that social media
texts differ from conventional attribute-value data due to their inher-
ently noisy, decentralized, unstructured, and dynamically evolving
nature [8].

3.2 Prompt Template Design
We first experimented two prompt variations written in English.
For this, we employ zero and n-shot learning approaches, where n
specifies the number of examples used in a prompt.

For our zero-shot learning approach, we designed a straight-
forward prompt which follows a prompt structure of [Instruc-
tion/Constraints/n samples]: “Classify the sentiments of the following
texts. For each item, respond only 0, 1, or 2 to indicate whether the
sentiment is neutral, negative, or positive, respectively. In cases of
ambiguity, choose the prevailing sentiment”. For the second prompt,

20Classifying Sentiments on Social Media Texts: A GPT-4 Preliminary Study

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Figure 1: Sentiment Annotation Process using GPT-4 API. (1) Each data sample is prepended with a number; (2) Get n chunk
of data samples; (3) Include the n data samples in the prompt; (4) Access the GPT-4 model through calling its API using the
parameters set; (5) Results are printed and saved in a .csv file; and (5) Loop through the same process until n samples

we mimic the annotation instructions designed for the human an-
notators as our prompt instruction and provided a brief sentiment
description and one example for each sentiment category, hence
referred to as one-shot learning. This approach follows a simi-
lar prompt structure to zero-shot, except that we added identity
modifier or persona “You are the CHED-UniFAST program coordi-
nator in the Philippines” as our System’s prompt which was used
to set the context of the dialogue, followed by the instruction and
examples. The final prompt structure of one-shot learning is [Per-
sona/Instruction/Examples/Constraints/n samples].

In [33] suggested to evaluate different prompt designs such as
use of code-mixed prompt. We selected the successful learning
approach as the basis for our code-mixed prompt. To write the
code-mixed prompt, we engaged with a native Bicolano speaker to
translate the English prompt using their own comprehension and
natural language, free from restrictions regarding usage of symbols
or abbreviations. The final code-mixed prompt consisted the use of
various languages, slang, abbreviation, and misspellings: “Iclassify
mo ung sintemyento netong mga social media texts gamit an mga
minasunod na polarities about sa pag implement ng Philippine RA
10931 UAQTE Act program. . .”. This approach allowed us to capture
the informal and dynamic language style prevalent in our dataset.

3.3 Sentiment Annotation using GPT-4
The original GPT model [23] is composed of 12-layer decoder-
only Transformer with masked self-attention heads. Its primary
capability is fine-tuning for specific downstream tasks.

As of the writing, GPT-4 is by far the most advanced model
released by OpenAI. GPT-4’s text input capability was released
via ChatGPT and the API. In this study, we use the GPT-4 API
with 8,192 tokens context model, comprising of both prompt and
completion which entails corresponding price per token. During our

initial test runs, GPT-4 is costly especially with longer prompts. To
reduce our costs, we employed looping of batch processing, which
means that for each request, it will process 30 and 15 samples from
the dataset for zero- and one-shot prompts respectively, instead of
individually sending each data sample to API. This API allows us to
communicate with the model by specifying a set of parameters that
control its behavior during text generation, such as a temperature
of 0, and a 200 maximum output tokens for every API call. We only
run the experiment once as our final evaluation and save the output
in a .csv file. Figure 1 summarizes our sentiment annotation process
using GPT-4 API.

3.4 Evaluation
Following the evaluation of [28] to analyze the agreement or inter-
rater reliability among annotators, we used Cohen’s Kappa. Table
1 shows the interpretation of the Kappa value obtained. Addition-
ally, we employed commonly used classification metrics such as
accuracy, precision, and recall to evaluate the model’s predictive
accuracy and its ability to correctly classify sentiments. Accuracy
measures the overall correctness of model predictions, while pre-
cision focuses on the proportion of true positives among positive
predictions, and recall quantifies the ability of the model to capture
all positive instances.

Further, we compare the evaluation results against the fine-tuned
Multilingual BERT (mBERT). It is worth noting that the dataset
used for both models underwent no preprocessing. For fine-tuning
mBERT a 70:30 split ratio for training and testing sets, a learning-
rate and batch size of 2e-5 and 16 were employed. Both mBERT and
GPT are Transformer based pre-trained models.

21NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Lany Maceda et al.

Table 1: Interpretation of Cohen’s Kappa

Kappa value

Interpretation

<0.20
0.21-0.40
0.41-0.60
0.61-0.80
0.81-1.00

Poor agreement
Fair agreement
Moderate agreement
Substantial agreement
Very good agreement

4 RESULTS AND DISCUSSION
In Table 2, we present the performance of GPT-4 using various
learning approaches in a classification task, each evaluated based
on Cohen’s Kappa value, accuracy, precision, and recall. We run the
experiment once as our final evaluation due to our limited access
to GPT-4 API and increased cost associated with longer prompts.
Compared to the achieved score of the prompt that uses zero-
shot approach, the Kappa values of prompts written in English and
Code-mixed using the one-shot approach achieved 0.77 and 0.73
respectively, which indicate that there is a substantial and statisti-
cally significant level of agreement between the model’s predictions
and the human annotations if context and identity modifier are
given. Accordingly, these prompts achieved an accuracy score of
0.85 and 0.8250 which demonstrates a high proportion of correct
classifications, emphasizing the capability of the model’s predic-
tions even without explicit training data to learn the sentiments
of an unprocessed code-mixed dataset. The matching precision
and recall values signify that the model maintains a balanced ap-
proach, effectively capturing positive instances while minimizing
false positives. Meanwhile, the fine-tuned mBERT resulted to lower
results than the GPT-4. This result is similar to the study of [24],
where the GPT-3 model beats the BERT-base model in Marathi Text
Classification.

As stated by [16], GPT models are highly sensitive to prompts.
Interestingly, the code-mixed prompt achieved scores that were
not significantly different from the prompt written in English. We
initially conclude that the use of words or language in the prompt
may not be the primary issue, as long as the prompt provides
identity modifier (System’s prompt), adequate instructions, and
context.

4.1 Error Analysis
We collected five samples from our annotated dataset to manually
examine instances where the model’s predictions diverged from
or did not match the human-annotated data. Our primary observa-
tion was despite our explicit instruction to respond in numerical

values [0, 1, 2] which corresponds to sentiments: neutral, negative,
and positive, the one-shot prompts received responses in words,
sometimes numerical values, unlike the zero-shot prompt which
responded the correct format for all items. Hence, post-cleaning of
the collected responses was necessary to evaluate GPT-4’s perfor-
mance on various metrics. These inaccuracies and inconsistencies
have been also observed in the study of [27].

In Table 3 we focused on the results of GPT-4 model; the first
sample written in non-English text was annotated correctly by all
prompts; the second and third example, utilizing a one-shot prompt,
correctly identified the text implying an announcement even with
the inclusion of positive phrase like “kayo ang bida!”. This pattern
was consistently observed in other samples, emphasizing the sig-
nificance of incorporating constraints for improved classification
accuracy. While one-shot prompt achieved high evaluation scores,
it still predicted inaccurate sentiments as shown in the fourth and
fifth examples where the latter uses a Filipino slang word “cutie”
which means “to manifest something they want to have/achieve” [26].
We hypothesize that this could be due to potential influence of the
model’s pre-trained knowledge that might introduce interpretative
variations, particularly in a domain-specific contexts. Interestingly,
mBERT correctly classified all data samples despite its low evalua-
tion scores.

5 CONCLUSION
In this preliminary study, we explored the application of GPT-4
for classifying sentiments in social media texts. The results demon-
strated GPT-4’s capability in handling diverse linguistic inputs
without using any training data, provided that the prompt should
contain specific and adequate instructions. However, challenges
were identified in instances involving slang or domain-specific
language.

6 LIMITATIONS AND FUTURE WORKS
Despite the impressive evaluation score obtained by GPT-4 in an-
notating the dataset, inaccuracies were observed on our experi-
ments. We initially suggest employing GPT-4 to participate in the
annotation process, alongside human annotators. The GPT-4’s per-
formance is dependent to the dataset they were trained on and to
the quality of the annotated data used for evaluation. Any biases
from these datasets may directly affect the model’s performance.
Additionally, the model’s effectiveness may vary across different
domains and industries, as it might not be well-suited to highly
specialized subjects or contexts not adequately covered in this ex-
periment.

In this study, code-mixed dataset was used to evaluate the GPT-
4 model capabilities in sentiment classification, since significant

Table 2: Performance of GPT-4 and mBERT model

Learning Approach

GPT-Zero-shot (English)
GPT-One-shot (English)
GPT-One-shot (Code-mixed)
mBERT

Kappa value Accuracy

Precision

0.50
0.77
0.73
-

0.6683
0.85
0.8250
0.8277

0.6870
0.8665
0.8432
0.8381

Recall

0.6683
0.85
0.8250
0.8252

22Classifying Sentiments on Social Media Texts: A GPT-4 Preliminary Study

NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Table 3: Examples of Classified Sentiments by GPT-4 and mBERT

No.

Human

mBERT

Zero-shot

One-shot
(EN)

One-shot
(CM)

Examples

1

2

3

4

5

Negative

Negative

Negative

Negative

Negative

Neutral

Neutral

Positive

Neutral

Positive

Neutral

Neutral

Positive

Neutral

Neutral

Negative

Negative

Negative

Neutral

Negative

Positive

Positive

Positive

Neutral

Neutral

Kasuya man kan bank Portal! Subago pa Password expired
dai na nag untok.hahaha.
(EN: The bank portal is frustrating! My password has been
expired for a while now, and it’s not getting any
better.hahaha)
TES Update #85 October pa lang parang Pasko na sa
UniFAST! TES Cuties ng SOCCSKSARGEN, kayo ang bida
ngayong alas otso gabi!
(EN: TES Update #85, it’s only October, but it already feels
like Christmas at UniFAST! TES Cuties of
SOCCSKSARGEN, you’re the stars tonight at eight
o’clock!)
Gawis ay agsapa, PINASkolars! Reminding again our TES
Beneficiaries to answer our #quickpoll and Google Form
that you can locate by clicking this #tesgrant. Iyaman!
Hello po just wanna ask po kung kailan po kaya ang
realese ng TDP? Medyo matagal na din po kasi yunh
sakin di ko pa rin po natatanggap Salamat po
(EN: Hello, I just want to ask when will the TDP be
released? It’s been a while, and I still haven’t received it.
Thank you.)
Ched Unifast Cutie

results were obtained from the experiments, this suggests that
future studies could focus on testing GPT-4 on purely-written native
and less-common languages, promoting inclusivity and broadening
the scope of sentiment analysis.

ACKNOWLEDGMENTS
The researchers would like to thank the Philippine Commission
on Higher Education (CHEd) Leading the Advancement of Knowl-
edge in Agriculture and Science (LAKAS) Project No. 2021-007,
eParticipation 2.1: Harnessing Natural Language Processing (NLP)
for Community Participation, for providing the necessary funds to
make this research possible. The researchers are truly grateful for
their contribution to the research.

REFERENCES
[1] Marvin M. Agüero-Torales, José I. Abreu Salas, and Antonio G. López-Herrera.
2021. Deep learning and multilingual sentiment analysis on social media data:
An overview. Appl Soft Comput 107, (August 2021). https://doi.org/10.1016/j.asoc.
2021.107373

[2] Maria Charmy A Arispe, Joni Neil B Capucao, Floradel S Relucio, and Daniel
E., Jr. Maligat. 2019. Teachers’ sentiments to Bikol MTB-MLE: Using sentiment
analysis and text mining techniques. International Journal of Research Studies in
Education 8, 4 (July 2019). https://doi.org/10.5861/ijrse.2019.4906

[3] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan,
Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter,
Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. 2020. Language Models are Few-Shot Learners.
(May 2020). Retrieved from http://arxiv.org/abs/2005.14165

[4] Mary Joy Canon, Christian Sy, and Lea Austero. 2019. Discovering themes from
online news articles on the 2018 mt. mayon eruption. In Proceedings - 2018

International Symposium on Computer, Consumer and Control, IS3C 2018, February
19, 2019. Institute of Electrical and Electronics Engineers Inc., 242–245. . https:
//doi.org/10.1109/IS3C.2018.00068

[5] Lingjiao Chen, Matei Zaharia, and James Zou. How Is ChatGPT’s Behavior Chang-

ing over Time?

[6] Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. BERT: Pre-
training of Deep Bidirectional Transformers for Language Understanding. (Octo-
ber 2018). Retrieved from https://arxiv.org/pdf/1810.04805v2

[7] Fabrizio Gilardi, Meysam Alizadeh, and Maël Kubli. 2023. ChatGPT outperforms
crowd workers for text-annotation tasks. Proceedings of the National Academy of
Sciences 120, 30 (July 2023). https://doi.org/10.1073/pnas.2305016120

[8] Pritam Gundecha and Huan Liu. 2012. Mining Social Media: A Brief Introduction.
In 2012 TutORials in Operations Research. INFORMS, 1–17. https://doi.org/10.1287/
educ.1120.0105

[9] Fan Huang, Haewoon Kwak, and Jisun An. 2023. Is ChatGPT better than Human
Annotators? Potential and Limitations of ChatGPT in Explaining Implicit Hate
Speech. In ACM Web Conference 2023 - Companion of the World Wide Web Con-
ference, WWW 2023, April 30, 2023. Association for Computing Machinery, Inc,
294–297. . https://doi.org/10.1145/3543873.3587368

[10] Adaikkan Kalaivani and Durairaj Thenmozhi. 2021. Multilingual Sentiment Analy-
sis in Tamil, Malayalam, and Kannada code-mixed social media posts using MBERT.
Retrieved from https://ceur-ws.org/Vol-3159/T6-16.pdf

[11] Jungo Kasai, Yuhei Kasai, Keisuke Sakaguchi, Yutaro Yamada, and Dragomir
Radev. 2023. Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing
Examinations. (March 2023). Retrieved from http://arxiv.org/abs/2303.18027
[12] Daniel Martin Katz, Michael James Bommarito, Shang Gao, and Pablo David
Arredondo. GPT-4 Passes the Bar Exam. Retrieved from http://dx.doi.org/10.2139/
ssrn.4389233

[13] Kiana Kheiri and Hamid Karimi. 2023. SentimentGPT: Exploiting GPT for Ad-
vanced Sentiment Analysis and its Departure from Current Machine Learning.
(July 2023). Retrieved from http://arxiv.org/abs/2307.10234

[14] Monica Lee and John Levi Martin. 2015. Coding, counting and cultural cartogra-
phy. Am J Cult Sociol 3, 1 (January 2015), 1–33. https://doi.org/10.1057/ajcs.2014.13
[15] Zhengliang Liu, Xiaowei Yu, Lu Zhang, Zihao Wu, Chao Cao, Haixing Dai, Lin
Zhao, Wei Liu, Dinggang Shen, Quanzheng Li, Tianming Liu, Dajiang Zhu, and
Xiang Li. 2023. DeID-GPT: Zero-shot Medical Text De-Identification by GPT-4.
(March 2023). Retrieved from http://arxiv.org/abs/2303.11032

[16] Chandreen Liyanage, Ravi Gokani, and Vijay Mago. GPT-4 as a Twitter Data
Annotator: Unraveling Its Performance on a Stance Classification Task. https:

23NLPIR 2023, December 15–17, 2023, Seoul, Republic of Korea

Lany Maceda et al.

//doi.org/10.36227/techrxiv.24143706.v1

[17] Ismini Lourentzou, Kabir Manghnani, and Chengxiang Zhai. Adapting Sequence
to Sequence Models for Text Normalization in Social Media. Retrieved from https:
//arxiv.org/abs/1904.06100

[18] Lany L Maceda, Arlene A Satuito, and Mideth B Abisado. Sentiment Analy-
sis of Code-mixed Social Media Data on Philippine UAQTE using Fine-tuned
mBERT Model. IJACSA) International Journal of Advanced Computer Science and
Applications 14, 7 , 2023

[19] Lany MacEda, Jennifer Llovido, and Arlene Satuito. 2019. Categorization of
earthquake-related tweets using machine learning approaches. In Proceedings
- 2018 International Symposium on Computer, Consumer and Control, IS3C 2018,
February 19, 2019. Institute of Electrical and Electronics Engineers Inc., 229–232.
. https://doi.org/10.1109/IS3C.2018.00065

[20] Laura K. Nelson, Derek Burk, Marcel Knudsen, and Leslie McCall. 2021. The
Future of Coding: A Comparison of Hand-Coding and Three Types of Computer-
Assisted Text Analysis Methods. Sociol Methods Res 50, 1 (February 2021), 202–237.
https://doi.org/10.1177/0049124118769114

[21] Harsha Nori, Nicholas King, Scott Mayer McKinney, Dean Carignan, and Eric
Horvitz. 2023. Capabilities of GPT-4 on Medical Challenge Problems. (March
2023). Retrieved from http://arxiv.org/abs/2303.13375

[22] OpenAI. 2023. GPT-4 Technical Report. (March 2023). Retrieved from http://arxiv.

org/abs/2303.08774

[23] Alec Radford Openai, Karthik Narasimhan Openai, Tim Salimans Openai, and Ilya
Sutskever Openai. Improving Language Understanding by Generative Pre-Training.
Retrieved from https://api.semanticscholar.org/CorpusID:49313245

[24] Chandrashekhar S. Pawar and Ashwin Makwana. 2022. Comparison of BERT-Base
and GPT-3 for Marathi Text Classification. Lecture Notes in Electrical Engineering
936, (2022), 563–574. https://doi.org/10.1007/978-981-19-5037-7_40/COVER
[25] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya
Sutskever. Language Models are Unsupervised Multitask Learners. Retrieved from
https://api.semanticscholar.org/CorpusID:160025533

[26] John Patrick Ranara. 2023. From “Arjo Cutie” to “I will marry you, cutie”: A

timeline of Maine Mendoza and Arjo Atayde’s romance. Philstar Life.

[27] Jaromir Savelka, Arav Agarwal, Marshall An, Chris Bogart, and Majd Sakr. 2023.
Thrilled by Your Progress! Large Language Models (GPT-4) No Longer Struggle
to Pass Assessments in Higher Education Programming Courses. August 07, 2023.
Association for Computing Machinery (ACM), 78–92. .https://doi.org/10.1145/
3568813.3600142

[28] Thomas Schmidt, Manuel Burghardt, Katrin Dennerlein, and Christian Wolff.
Sentiment Annotation for Lessing’s Plays: Towards a Language Resource for

Sentiment Analysis on German Literary Texts. Conference on Language, Data
and Knowledge (LDK 2019), 2019, pp. 45–50. [Online]. Available: http://ceur-
ws.org/Vol-2402/paper9.pdf

[29] Kogilavani Shanmugavadivel, Sai Haritha Sampath, Pramod Nandhakumar,
Prasath Mahalingam, Malliga Subramanian, Prasanna Kumar Kumaresan, and
Ruba Priyadharshini. 2022. An analysis of machine learning models for sentiment
analysis of Tamil code-mixed data. Comput Speech Lang 76, (November 2022),
101407. https://doi.org/10.1016/J.CSL.2022.101407

[30] Olga Uryupina, Barbara Plank, Aliaksei Severyn, Agata Rotondi, and Alessandro
Moschitti. SenTube: A Corpus for Sentiment Analysis on YouTube Social Media.
In Proceedings of the Ninth International Conference on Language Resources and
Evaluation (LREC’14). Retrieved from http://www.lrec-conf.org/proceedings/
lrec2014/pdf/180_Paper.pdf

[31] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan
N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention Is All You Need.
(June 2017). Retrieved from http://arxiv.org/abs/1706.03762

[32] Shuohang Wang, Yang Liu, Yichong Xu, Chenguang Zhu, and Michael Zeng.
2021. Want To Reduce Labeling Cost? GPT-3 Can Help. (August 2021). Retrieved
from http://arxiv.org/abs/2108.13487

[33] Zengzhi Wang, Qiming Xie, Zixiang Ding, Yi Feng, and Rui Xia. 2023. Is ChatGPT
a Good Sentiment Analyzer? A Preliminary Study. (April 2023). Retrieved from
http://arxiv.org/abs/2304.04339

[34] Mayur Wankhade, Annavarapu Chandra Sekhara Rao, and Chaitanya Kulkarni.
2022. A survey on sentiment analysis methods, applications, and challenges. Artif
Intell Rev 55, 7 (October 2022), 5731–5780. https://doi.org/10.1007/s10462-022-
10144-1

[35] Ziang Xiao, Xingdi Yuan, Q. Vera Liao, Rania Abdelghani, and Pierre Yves Oudeyer.
2023. Supporting Qualitative Analysis with Large Language Models: Combining
Codebook with GPT-3 for Deductive Coding. In International Conference on Intel-
ligent User Interfaces, Proceedings IUI, March 27, 2023. Association for Computing
Machinery, 75–78. https://doi.org/10.1145/3581754.3584136

[36] Seid Muhie Yimam, Hizkiel Mitiku Alemayehu, Abinew Ali Ayele, and Chris
Biemann. Exploring Amharic Sentiment Analysis from Social Media Texts: Building
Annotation Tools and Classification Models. In Proceedings of the 28th International
Conference on Computational Linguistics, Jan. 2020, doi: 10.18653/v1/2020.coling-
main.91.

[37] Yiming Zhu, Peixian Zhang, Ehsan-Ul Haq, Pan Hui, and Gareth Tyson. 2023. Can
ChatGPT Reproduce Human-Generated Labels? A Study of Social Computing
Tasks. (April 2023). Retrieved from http://arxiv.org/abs/2304.10145

24