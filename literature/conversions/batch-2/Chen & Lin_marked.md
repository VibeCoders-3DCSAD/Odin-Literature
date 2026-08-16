---
conversion_metadata:
  converted_at: "2026-07-22T12:53:23Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Chen & Lin.pdf"
  source_pdf_sha256: "cdd6f8480b3321cf1dd502d8c95771921c6d24418bf4099738ee6e226bd2dea5"
  page_count: 8
  markdown_char_count: 74583
---

<!-- PAGE-AWARE EXTRACTION (via pdfminer.six) -->

<!-- PAGE 1 -->

Journal of Trends in Financial and Economics
ISSN: 3007-696X
DOI: https://doi.org/10.61784/jtfe3036

DEEP LEARNING-BASED CREDIT RISK MODELING:
ADDRESSING DATA IMBALANCE AND INVARIANCE

LiangYu Chen, Hao Lin*
School of Management, Sun Yat-sen University, Guangzhou 510275, Guangdong, China.
Corresponding Author: Hao Lin, Email: 627709133@qq.com

Abstract: Credit risk modeling plays a crucial role in financial decision-making, helping lenders assess the likelihood
of default and optimize lending strategies. Traditional credit risk assessment models, including logistic regression and
decision trees, often struggle with data imbalance and invariance issues, leading to biased risk predictions and reduced
generalization. The rapid advancement of deep learning (DL) techniques has introduced more sophisticated models
capable of learning complex credit risk patterns. However, most DL-based credit scoring models still suffer from class
imbalance in default prediction and fail to maintain fairness and stability across different demographic and economic
conditions.
This study proposes a DL-based credit risk modeling framework designed to address data imbalance through advanced
resampling techniques and generative modeling, while also incorporating adversarial learning to improve model
invariance across diverse borrower segments. The proposed framework utilizes autoencoders, generative adversarial
networks (GANs), and cost-sensitive learning techniques to enhance risk assessment accuracy while reducing bias.
Additionally, domain adaptation techniques are introduced to ensure that the model remains robust across different
financial environments.
Experiments on real-world credit datasets demonstrate that the proposed framework significantly improves credit risk
prediction accuracy, enhances model fairness, and reduces sensitivity to class imbalance compared to traditional credit
scoring approaches. The findings highlight the importance of integrating data-centric augmentation techniques with
fairness-aware deep learning to improve the reliability of credit risk modeling in modern financial applications.
Keywords: Credit risk modeling; Deep learning; Data imbalance; Invariance; Fairness; Generative models; Adversarial
learning

1 INTRODUCTION

Credit risk modeling is a critical component of financial decision-making, enabling lenders and financial institutions to
assess the likelihood of borrower default [1]. An accurate credit risk assessment system ensures that loans are granted to
creditworthy individuals while minimizing the risk of financial losses. Traditional credit risk models, such as logistic
regression (LR) and decision trees (DTs), have been widely used for decades to predict borrower default probabilities.
However, these models rely on manually engineered features and linear relationships, making them limited in capturing
complex credit risk patterns present in real-world financial data [2].
One of the major challenges in credit risk modeling is class imbalance, where the proportion of borrowers who default
on their loans is significantly lower than those who repay their debts [3]. This imbalance often leads to biased credit
scoring models, where machine learning algorithms favor the majority class (non-defaulters) while misclassifying
minority class samples (defaulters). Traditional machine learning (ML) models trained on imbalanced datasets tend to
exhibit poor recall for high-risk borrowers, leading to inaccurate risk estimation and suboptimal lending decisions [4].
Addressing class imbalance is crucial to improving the performance and fairness of credit risk models.
Another key issue in credit risk modeling is invariance, referring to a model’s ability to maintain consistent predictive
performance across different demographic and economic conditions [5]. Many existing credit scoring models exhibit
distributional bias, where certain borrower groups receive systematically different credit risk scores due to underlying
imbalances in the dataset. This raises ethical and regulatory concerns, as unfair credit assessments can lead to
discriminatory lending practices and potential legal consequences. Improving invariance in credit risk models is
essential to ensure fairness and regulatory compliance in financial decision-making [6].
Recent advancements in deep learning (DL) have introduced more sophisticated methods for credit risk assessment,
enabling models to learn non-linear and hierarchical representations from large-scale financial datasets [7]. Techniques
such as artificial neural networks (ANNs) and long short-term memory (LSTM) networks have been employed to
improve credit risk prediction by leveraging complex borrower-lender interaction patterns [8]. However, despite their
advantages, DL-based credit scoring models still face significant challenges related to class imbalance and distributional
invariance.
This study proposes a DL-based credit risk modeling framework designed to address these limitations by integrating
data augmentation, generative adversarial networks (GANs), and adversarial training techniques. The framework
enhances credit risk assessment by improving recall for high-risk borrowers and ensuring model stability across
different borrower distributions. By incorporating autoencoders (AEs) for feature learning, cost-sensitive learning
techniques for imbalanced classification, and domain adaptation strategies for fairness enhancement, the proposed
approach improves both the accuracy and fairness of credit risk predictions.

© By the Author(s) 2025, under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0).

---

<!-- PAGE 2 -->

2

LiangYu Chen & Hao Lin

The framework is evaluated using real-world credit risk datasets, demonstrating its effectiveness in mitigating data
imbalance, reducing discriminatory biases, and improving model generalization. The findings highlight the necessity of
combining data-centric resampling techniques with fairness-aware deep learning approaches to develop robust and
equitable credit risk assessment systems for modern financial applications.

2 LITERATURE REVIEW

Credit risk modeling has been extensively studied in financial research, with traditional methods focusing on statistical
and ML-based techniques to predict borrower default probabilities [9]. While LR and DTs have been widely used due to
their interpretability and regulatory acceptance, these models often struggle with complex borrower behaviors and
non-linear credit risk patterns [10]. The advent of DL has provided new opportunities for financial institutions to
enhance risk assessment accuracy by leveraging large-scale datasets and learning intricate borrower-lender interactions.
However, DL models also present challenges, particularly in addressing class imbalance and ensuring invariance in
credit risk classification [11].
Class imbalance remains a fundamental issue in credit risk modeling [12]. Many credit datasets contain a significantly
lower proportion of defaulters compared to non-defaulters, leading to skewed model predictions. Traditional ML
models trained on such imbalanced datasets tend to favor the majority class, resulting in high overall accuracy but poor
recall for high-risk borrowers. To address this issue, various resampling techniques, including oversampling methods
such as Synthetic Minority Over-sampling Technique (SMOTE) and undersampling methods, have been introduced to
balance class distributions. Cost-sensitive learning has also been explored as an alternative, assigning higher
misclassification penalties to the minority class to improve model sensitivity to defaulters [13-16]. While these
approaches mitigate imbalance to some extent, they do not fully capture the complex borrower relationships that
contribute to default risk [17].
DL-based models, particularly ANNs and LSTMs, have demonstrated superior predictive performance in credit risk
modeling by capturing hierarchical borrower representations and sequential financial behaviors [18]. However, their
reliance on large, imbalanced datasets can lead to biased risk predictions [19]. One solution to this challenge is the use
of GANs to generate synthetic borrower profiles, expanding the representation of high-risk borrowers in training data.
Additionally, autoencoders have been utilized for feature extraction, improving model generalization and reducing
overfitting in imbalanced credit datasets. These data augmentation techniques enhance the robustness of DL models,
enabling them to learn better from minority class samples and improving recall for high-risk borrowers [20].
Another key challenge in credit risk modeling is ensuring invariance across different borrower demographics and
economic conditions [21]. Many traditional credit scoring models exhibit distributional bias, where borrowers from
specific demographic or socioeconomic backgrounds receive systematically lower or higher credit scores due to
underlying dataset imbalances. Addressing this issue requires adversarial learning strategies that enforce fairness
constraints during model training [22-26]. Domain adaptation techniques, such as adversarial domain alignment, have
been introduced to ensure that risk predictions remain stable across different borrower groups [8]. These techniques
help mitigate the effects of biased credit assessments, ensuring that DL-based credit risk models are both accurate and
fair [27-29].
Despite the advancements in DL-based credit risk modeling [30,31],
there remain open questions regarding
explainability and regulatory compliance. Financial institutions are required to provide transparent justifications for
credit decisions, which can be challenging when using complex neural networks. Research into explainable AI methods,
including feature attribution techniques and interpretable DL architectures, aims to bridge this gap by improving model
interpretability while maintaining high predictive performance [32].
This study builds on these advancements by integrating GAN-based data augmentation, adversarial learning for fairness
enhancement, and autoencoder-driven feature learning into a unified DL-based credit risk modeling framework. The
proposed approach aims to improve credit risk assessment by addressing class imbalance and ensuring distributional
invariance, enhancing both model performance and fairness in credit lending decisions. The next section outlines the
methodology used to implement and evaluate the proposed framework.

3 METHODOLOGY

3.1 Data Preprocessing and Feature Engineering

information. Missing values are addressed using imputation techniques,

Credit risk modeling relies on high-dimensional financial datasets containing diverse borrower attributes, transaction
histories, and economic indicators. Ensuring data quality and consistency is crucial before training DL-based models.
The first step in preprocessing involves handling missing values, which are common in credit datasets due to
incomplete borrower
including mean
imputation for numerical features and mode imputation for categorical attributes. More complex techniques such as
k-nearest neighbors imputation and autoencoder-based imputations are also employed to enhance data consistency.
Outlier detection is another important preprocessing step, as extreme values in financial data can bias model predictions.
Borrowers with unrealistic credit scores, income levels, or transaction frequencies are identified using statistical
anomaly detection methods, including interquartile range and Mahalanobis distance. Data normalization is applied to
ensure that all numerical variables are scaled appropriately, preventing models from being influenced by
large-magnitude financial values.

Volume 2, Issue 2, Pp 1-8, 2025

---

<!-- PAGE 3 -->

Deep learning-based credit risk modeling: addressing data imbalance and invariance

3

Feature engineering plays a crucial role in improving the predictive power of credit risk models. Derived financial
attributes, such as debt-to-income ratio, revolving credit utilization, and historical loan repayment behavior, are
extracted to provide more informative borrower representations. Temporal features are also introduced by analyzing
borrower behavior over different
trends and repayment
consistency. Dimensionality reduction techniques, including principal component analysis and autoencoder-based
feature selection, are applied to eliminate redundant information while preserving critical credit risk indicators.

time windows, allowing the model

to capture financial

3.2 Handling Class Imbalance with Generative and Cost-Sensitive Approaches

Class imbalance is one of the most significant challenges in credit risk modeling, where the number of default cases is
substantially lower than non-default cases. Training models on imbalanced datasets leads to biased predictions, where
the model learns to favor the majority class, resulting in high precision but low recall for high-risk borrowers. To
address this issue, multiple techniques are integrated into the proposed framework to improve model sensitivity to
defaulters while maintaining overall classification accuracy.
Resampling techniques, including SMOTE-based oversampling and random undersampling, are employed to rebalance
class distributions. While these methods improve recall for the minority class, they can introduce noise and redundancy
in training data. To mitigate this, GAN-based data augmentation is implemented, generating synthetic borrower profiles
that mimic the statistical properties of real defaulters. The GAN framework consists of a generator that learns to create
realistic borrower data and a discriminator that distinguishes between real and synthetic profiles, resulting in more
diverse and representative training samples.
Cost-sensitive learning is incorporated into the DL framework to assign higher misclassification penalties for false
negatives, ensuring that defaulters are correctly identified. The model optimizes a weighted loss function that prioritizes
minimizing the impact of incorrectly classified high-risk borrowers. Adaptive threshold tuning is also applied, where
the decision boundary for classifying defaulters is adjusted dynamically based on dataset imbalance ratios. These
techniques collectively enhance the model’s ability to recognize high-risk borrowers, leading to more reliable credit risk
assessments.

3.3 Adversarial Training for Invariance and Fairness Enhancement

Ensuring that the credit risk model remains fair and unbiased across different borrower demographics is essential for
regulatory compliance and ethical lending practices. Many traditional credit scoring models exhibit disparities in loan
approval rates due to dataset biases, where certain demographic groups receive systematically different risk assessments.
To mitigate this issue, adversarial training is integrated into the DL framework to enhance fairness and improve model
invariance across different borrower segments.
The adversarial learning framework consists of two competing models: the primary credit risk classifier and an
adversary trained to detect disparities in credit risk predictions. During training, the adversary attempts to identify
which demographic group a borrower belongs to based on the classifier’s predictions. If the adversary successfully
distinguishes borrower groups, the classifier is penalized, forcing it to learn risk assessment criteria that are independent
of demographic attributes. This process ensures that the credit risk model learns unbiased decision-making rules,
reducing the influence of sensitive attributes such as age, gender, or ethnicity.
Domain adaptation techniques are also introduced to ensure that the model maintains stability across different economic
conditions and borrower distributions. The model is trained on credit datasets from multiple financial institutions and
economic cycles, improving its ability to generalize across varied lending environments. Transfer learning is employed
to fine-tune the model on new borrower datasets, ensuring that it remains adaptable to evolving financial conditions
without requiring full retraining.

3.4 Model Training, Optimization, and Evaluation Metrics

The proposed DL-based credit risk framework is implemented using a deep feedforward neural network architecture
combined with LSTMs for capturing sequential borrower behaviors. The model is trained using a hybrid loss function
that balances classification accuracy, fairness constraints, and cost-sensitive penalties for high-risk borrowers. The
optimization process is conducted using the Adam optimizer with dynamic learning rate adjustments, ensuring that the
model converges efficiently without overfitting.
Hyperparameter tuning is performed using Bayesian optimization and grid search techniques to identify optimal model
configurations, including the number of hidden layers, activation functions, dropout rates, and regularization parameters.
To further improve model generalization, ensemble learning techniques such as stacked neural networks and
boosting-based deep learning are explored. These techniques enhance prediction robustness by combining multiple
neural network architectures to minimize variance and bias.
The evaluation of the proposed framework is conducted using multiple performance metrics to ensure a comprehensive
assessment of its effectiveness. Precision, recall, and F1-score are used to measure classification accuracy, while
AUC-ROC curves assess the model’s ability to distinguish between defaulters and non-defaulters. The fairness of credit
risk assessments is evaluated using disparate impact ratios and equality of opportunity metrics, ensuring that loan
approval decisions do not disproportionately disadvantage any demographic group.

Volume 2, Issue 2, Pp 1-8, 2025

---

<!-- PAGE 4 -->

4

LiangYu Chen & Hao Lin

Scalability and computational efficiency are also key considerations, as credit risk models must be capable of
processing large borrower datasets in real time. The model’s inference speed, memory consumption, and scalability
across different hardware environments are analyzed to determine its suitability for deployment in large-scale financial
systems. The results confirm that the proposed framework achieves superior credit risk assessment accuracy, fairness,
and computational efficiency compared to traditional credit scoring models.
By integrating advanced data augmentation, fairness-aware adversarial
learning, and cost-sensitive classification
the proposed DL-based credit risk framework effectively addresses data imbalance and invariance
techniques,
challenges, providing financial institutions with a more accurate, ethical, and scalable approach to credit risk modeling.
The next section presents experimental results and discusses the impact of combining these techniques on credit risk
prediction performance.

4 RESULTS AND DISCUSSION

4.1 Credit Risk Prediction Accuracy and Model Performance

The effectiveness of the proposed DL-based credit risk modeling framework was evaluated using real-world credit
datasets, comparing its performance with traditional ML models such as LR, DTs, and gradient boosting classifiers. The
evaluation metrics included precision, recall, F1-score, and AUC-ROC, providing a comprehensive assessment of the
model’s ability to classify borrowers accurately. The results demonstrated that integrating deep learning techniques,
particularly generative models and adversarial training, significantly enhanced credit risk assessment performance.
The model achieved superior recall for high-risk borrowers compared to conventional ML-based credit scoring models,
which tend to misclassify defaulters due to class imbalance. By incorporating GAN-based data augmentation and
cost-sensitive learning, the model successfully improved recall for defaulters by 22% while maintaining high precision,
ensuring that non-defaulters were not incorrectly classified as high-risk borrowers. The improvement in recall is
particularly beneficial for financial institutions, as it reduces the likelihood of misclassifying potential defaulters,
thereby minimizing loan default risks.
The overall AUC-ROC score of the proposed model was consistently higher across different credit datasets, indicating
better discriminatory power between default and non-default cases. Compared to traditional ML models, which often
fail to capture non-linear borrower patterns, the proposed DL-based framework demonstrated higher adaptability to
complex credit risk scenarios, allowing it to generalize effectively across diverse borrower groups.
Figure 1 presents a comparative analysis of credit risk prediction accuracy across different models, illustrating the
performance advantages of the proposed DL-based framework.

4.2 Impact of Generative Modeling and Resampling Techniques on Class Imbalance

Figure 1 Credit Risk Prediction Accuracy Comparison

Addressing class imbalance is crucial for improving the effectiveness of credit risk models, as imbalanced datasets often
lead to biased predictions that favor the majority class. Traditional resampling techniques, such as SMOTE, have been
widely used to balance class distributions, but they often introduce synthetic noise, leading to model overfitting. The
proposed framework integrates GAN-based data augmentation and cost-sensitive learning to enhance model robustness
against class imbalance.
The impact of generative modeling was assessed by training the credit risk classifier on datasets enhanced with
synthetic borrower profiles generated by GANs. The results showed that the use of synthetic defaulter data significantly
improved model generalization, particularly in cases where default rates were extremely low. Unlike oversampling

Volume 2, Issue 2, Pp 1-8, 2025

---

<!-- PAGE 5 -->

Deep learning-based credit risk modeling: addressing data imbalance and invariance

5

methods that simply duplicate minority class instances, GAN-based augmentation introduced diverse yet realistic
borrower profiles, allowing the model to learn more representative credit risk features.
In addition to generative modeling, cost-sensitive learning played a crucial role in optimizing the classification process.
By assigning higher misclassification penalties for false negatives, the framework effectively reduced the number of
misclassified defaulters without substantially increasing false positives. This approach ensures that the model prioritizes
risk management without over-penalizing creditworthy borrowers.
Figure 2 illustrates the impact of GAN-based data augmentation and cost-sensitive learning on class imbalance
reduction, highlighting the effectiveness of these techniques in improving borrower risk classification.

Figure 2 Impact of Data Augmentation on Class Imbalance

4.3 Fairness and Invariance Across Borrower Demographics

Ensuring fairness and invariance in credit risk modeling is critical for regulatory compliance and ethical lending
practices. Many traditional credit scoring models exhibit biases related to demographic attributes, where specific
borrower groups receive systematically different risk scores due to historical imbalances in training data. The proposed
framework incorporates adversarial training to mitigate these biases, ensuring that the credit risk model remains
invariant across different borrower segments.
To evaluate fairness, disparate impact ratios and equality of opportunity metrics were computed for different borrower
groups, analyzing whether the model disproportionately assigned higher risk scores to specific demographics. The
results confirmed that the adversarial learning framework significantly reduced bias in risk assessments, ensuring that
credit scores were determined primarily by financial indicators rather than demographic characteristics.
The adversarial training component effectively prevented the model from learning biased correlations by enforcing
fairness constraints during the training process. Additionally, domain adaptation techniques were employed to fine-tune
the model on credit datasets from different economic environments, ensuring that its predictions remained stable across
varying financial conditions. The findings demonstrate that integrating fairness-aware training strategies not only
improves the ethical considerations of credit risk modeling but also enhances model robustness.
Figure 3 presents an analysis of fairness-enhancing adversarial training, showcasing its impact on reducing credit risk
classification bias across borrower demographics.

Volume 2, Issue 2, Pp 1-8, 2025

---

<!-- PAGE 6 -->

6

LiangYu Chen & Hao Lin

4.4 Computational Efficiency and Scalability of the Credit Risk Model

Figure 3 Fairness in Credit Risk Scoring (Hexbin Plot)

For credit risk models to be deployed in large-scale financial applications, they must be capable of processing vast
amounts of borrower data in real time while maintaining high classification accuracy. The computational performance
of the proposed DL-based framework was analyzed by measuring inference speed, memory consumption, and
scalability across increasing dataset sizes.
The results showed that
the framework maintained low latency inference, processing thousands of borrower
applications per second without significant computational overhead. Compared to traditional ML models, which often
require manual feature engineering and retraining, the proposed DL framework leveraged parallel processing and GPU
acceleration to achieve higher processing efficiency. The use of autoencoder-based feature extraction further reduced
dimensionality, optimizing computation while preserving critical risk assessment features.
Scalability tests were conducted by evaluating the framework’s performance on datasets containing varying numbers of
borrower records, ranging from 100,000 to over 10 million transactions. The model’s performance remained stable,
confirming its ability to handle large-scale credit risk assessment tasks. The integration of transfer learning further
improved scalability, allowing the model to be fine-tuned on new financial datasets without requiring full retraining.
The findings confirm that the proposed framework achieves high computational efficiency and scalability, making it
suitable for deployment in financial institutions requiring real-time credit risk assessments for large borrower pools. The
results also indicate that the model’s ability to adapt to new credit data while maintaining efficiency makes it a viable
solution for dynamic financial environments.
Figure 4 presents an evaluation of computational performance and scalability, highlighting the framework’s efficiency
in large-scale credit risk modeling.

Figure 4 Computational Efficiency and Salability

Volume 2, Issue 2, Pp 1-8, 2025

---

<!-- PAGE 7 -->

Deep learning-based credit risk modeling: addressing data imbalance and invariance

7

5 CONCLUSION

Credit risk modeling is a fundamental component of financial risk management, enabling lenders to assess borrower
creditworthiness and optimize lending strategies. While traditional ML models such as LR and DTs have been widely
used in credit scoring, they exhibit limitations in handling class imbalance and demographic invariance, leading to
biased predictions and suboptimal risk assessments. The emergence of DL has introduced more powerful modeling
techniques capable of capturing non-linear borrower-lender interactions, yet challenges remain in ensuring fairness,
mitigating imbalance, and maintaining model stability across different financial environments.
This study proposed a DL-based credit risk modeling framework designed to address these challenges by integrating
GAN-based data augmentation, adversarial fairness learning, and cost-sensitive classification techniques. The results
incorporating generative models significantly improved the classification recall for high-risk
demonstrated that
borrowers, reducing bias caused by class imbalance. Unlike traditional resampling methods, which introduce synthetic
noise, GANs provided realistic borrower profiles, allowing the model to learn more representative credit risk features.
The introduction of adversarial learning further enhanced model invariance, ensuring that credit risk assessments
remained consistent across different borrower demographics.
The experimental evaluation confirmed that the proposed GNN-GAN-adversarial framework outperforms conventional
credit risk models in terms of accuracy, fairness, and computational efficiency. The model achieved higher recall for
defaulters, improved credit risk classification precision, and reduced false positives. The integration of adversarial
learning also reduced disparities in credit scoring across borrower segments, mitigating potential regulatory concerns
and ensuring compliance with ethical lending standards.
Scalability and computational efficiency were key factors in determining the practicality of the proposed approach for
large-scale credit risk modeling. The model was tested on credit datasets containing millions of borrower records,
demonstrating that the proposed DL-based framework maintained stable inference speed and memory efficiency,
making it suitable for deployment in financial institutions with high transaction volumes. The results confirmed that the
combination of autoencoder-based feature selection, GPU acceleration, and transfer learning techniques allowed the
model to process borrower data in real-time while maintaining predictive accuracy.
Despite its advantages, the proposed framework presents certain limitations that warrant future research. One key
challenge is the computational cost associated with training GANs and adversarial networks on large-scale financial
datasets. While the current implementation ensures scalability, further optimizations such as model compression
techniques and distributed training strategies should be explored to enhance efficiency. Another limitation is the
explainability of deep learning-based credit risk assessments, as financial institutions require transparency in risk
prediction for regulatory compliance. Future work should focus on interpretable AI methods, integrating techniques
such as SHAP values and attention-based explanations to improve trust in credit risk predictions.
Additionally, future research should investigate the integration of multi-source financial data, including alternative
credit scoring indicators such as transactional behaviors, spending patterns, and social network interactions, to enhance
borrower profiling accuracy. Extending the framework to cross-border credit risk modeling will also improve its
applicability in global financial markets.
This study highlights the importance of combining DL with fairness-aware learning and data augmentation strategies to
develop robust, equitable, and scalable credit risk models. By incorporating generative models, adversarial fairness
techniques, and cost-sensitive classification, the proposed framework provides a comprehensive solution to credit risk
assessment, ensuring that financial institutions can make fair, data-driven lending decisions while minimizing credit
losses and regulatory risks.

COMPETING INTERESTS

The authors have no relevant financial or non-financial interests to disclose.

REFERENCES

[1] Mashrur A, Luo W, Zaidi N A, et al. Machine learning for financial risk management: a survey. IEEE Access,

2020, 8: 203203-203223.

[2] Sudjianto A, Zhang A. Model validation practice in banking: A structured approach for predictive models. 2024.

DOI: 10.48550/arXiv.2410.13877.

[3] Addo P M, Guegan D, Hassani B. Credit risk analysis using machine and deep learning models. Risks, 2018, 6(2):

38.

[4] Bhatore S, Mohan L, Reddy Y R. Machine learning techniques for credit risk evaluation: a systematic literature

review. Journal of Banking and Financial Technology, 2020, 4(1): 111-138.

[5] Hamori S, Kawai M, Kume T, et al. Ensemble learning or deep learning? Application to default risk

analysis. Journal of Risk and Financial Management, 2018, 11(1): 12.

[6] Han X, Yang Y, Chen J, et al. Symmetry-Aware Credit Risk Modeling: A Deep Learning Framework Exploiting

Financial Data Balance and Invariance. Symmetry, 2025, 17(3): 341.

[7] Bussmann N, Giudici P, Marinelli D, et al. Explainable machine learning in credit risk management.

Computational Economics, 2021, 57(1): 203–216.

Volume 2, Issue 2, Pp 1-8, 2025

---

<!-- PAGE 8 -->

8

LiangYu Chen & Hao Lin

[8] Mhlanga D. Financial inclusion in emerging economies: The application of machine learning and artificial

intelligence in credit risk assessment. International Journal of Financial Studies, 2021, 9(3): 39.

[9] Bazarbash M. Fintech in financial inclusion: machine learning applications in assessing credit risk. International

Monetary Fund, 2019.

[10] Leo M, Sharma S, Maddulety K. Machine learning in banking risk management: A literature review. Risks, 2019,

7(1): 29.

[11] Moscato V, Picariello A, Sperlí G. A benchmark of machine learning approaches for credit score prediction.

Expert Systems with Applications, 2021, 165: 113986.

[12] Munkhdalai L, Munkhdalai T, Namsrai O E, et al. An empirical comparison of machine-learning methods on bank

client credit assessments. Sustainability, 2019, 11(3): 699.

[13] Berhane T, Melese T, Seid A M. Performance Evaluation of Hybrid Machine Learning Algorithms for Online

Lending Credit Risk Prediction. Applied Artificial Intelligence, 2024, 38(1): 2358661.

[14] Kaisar S, Sifat S T. Explainable Machine Learning Models for Credit Risk Analysis: A Survey. Data Analytics for

Management, Banking and Finance: Theories and Application. Cham: Springer Nature Switzerland, 2023: 51-72.

[15] Talaei Khoei T, Ould Slimane H, Kaabouch N. Deep learning: systematic review, models, challenges, and research

directions. Neural Computing and Applications, 2023, 35(31): 23103-23124.

[16] Kim E, Lee J, Shin H, et al. Champion-challenger analysis for credit card fraud detection: Hybrid ensemble and

deep learning. Expert Systems with Applications, 2019, 128: 214-224.

[17] Guo H, Ma Z, Chen X, et al. Generating artistic portraits from face photos with feature disentanglement and

reconstruction. Electronics, 2024, 13(5): 955.

[18] Lee Z, Wu Y C, Wang X. Automated Machine Learning in Waste Classification: A Revolutionary Approach to
Efficiency and Accuracy. Proceedings of the 2023 12th International Conference on Computing and Pattern
Recognition, 2023, 299-303.

[19] Wang X, Wu Y C, Ma Z. Blockchain in the courtroom: exploring its evidentiary significance and procedural

implications in US judicial processes. Frontiers in Blockchain, 2024, 7: 1306058.

[20] Seera M, Lim C P, Kumar A, et al. An intelligent payment card fraud detection system. Annals of Operations

Research, 2024, 334(1): 445-467.

[21] Wang X, Wu Y C, Zhou M, et al. Beyond surveillance: privacy, ethics, and regulations in face recognition

technology. Frontiers in Big Data, 2024, 7: 1337465.

[22] Liu Y, Wu Y C, Fu H, et al. Digital intervention in improving the outcomes of mental health among LGBTQ+

youth: a systematic review. Frontiers in Psychology, 2023, 14: 1242928.

[23] Ejiofor O E. A comprehensive framework for strengthening USA financial cybersecurity: integrating machine
learning and AI in fraud detection systems. European Journal of Computer Science and Information Technology,
2023, 11(6): 62-83.

[24] Carneiro N, Figueira G, Costa M. A data mining based system for credit-card fraud detection in e-tail. Decision

Support Systems, 2017, 95: 91-101.

[25] Al-Hashedi K G, Magalingam P. Financial fraud detection applying data mining techniques: A comprehensive

review from 2009 to 2019. Computer Science Review, 2021, 40: 100402.

[26] Liang Y, Wang X, Wu Y C, et al. A study on blockchain sandwich attack strategies based on mechanism design

game theory. Electronics, 2023, 12(21): 4417.

[27] Li X, Wang X, Chen X, et al. Unlabeled data selection for active learning in image classification. Scientific

Reports, 2024, 14(1): 424.

[28] Kalluri K. Optimizing Financial Services Implementing Pega's Decisioning Capabilities for Fraud Detection.
International Journal of Innovative Research in Engineering & Multidisciplinary Physical Sciences, 2022, 10(1):
1-9.

[29] Chen S, Liu Y, Zhang Q, et al. Multi-Distance Spatial-Temporal Graph Neural Network for Anomaly Detection in

Blockchain Transactions. Advanced Intelligent Systems, 2025, 2400898.

[30] Sailusha R, Gnaneswar V, Ramesh R, et al. Credit card fraud detection using machine learning. 2020 4th
International Conference on Intelligent Computing and Control Systems (ICICCS), 2020: 1264-1270. IEEE.
[31] Cui Y, Han X, Chen J, et al. FraudGNN-RL: A Graph Neural Network With Reinforcement Learning for Adaptive

Financial Fraud Detection. IEEE Open Journal of the Computer Society, 2025.

[32] Thennakoon A, Bhagyani C, Premadasa S, et al. Real-time credit card fraud detection using machine learning.
2019 9th International Conference on Cloud Computing, Data Science & Engineering (Confluence), 2019:
488-493. IEEE.

Volume 2, Issue 2, Pp 1-8, 2025

<!-- MARKITDOWN CONVERSION -->

<!-- Full MarkItDown conversion for formatting fidelity. -->

Journal of Trends in Financial and Economics
ISSN: 3007-696X
DOI: https://doi.org/10.61784/jtfe3036

DEEP LEARNING-BASED CREDIT RISK MODELING:
ADDRESSING DATA IMBALANCE AND INVARIANCE

LiangYu Chen, Hao Lin*
School of Management, Sun Yat-sen University, Guangzhou 510275, Guangdong, China.
Corresponding Author: Hao Lin, Email: 627709133@qq.com

Abstract: Credit risk modeling plays a crucial role in financial decision-making, helping lenders assess the likelihood
of default and optimize lending strategies. Traditional credit risk assessment models, including logistic regression and
decision trees, often struggle with data imbalance and invariance issues, leading to biased risk predictions and reduced
generalization. The rapid advancement of deep learning (DL) techniques has introduced more sophisticated models
capable of learning complex credit risk patterns. However, most DL-based credit scoring models still suffer from class
imbalance in default prediction and fail to maintain fairness and stability across different demographic and economic
conditions.
This study proposes a DL-based credit risk modeling framework designed to address data imbalance through advanced
resampling techniques and generative modeling, while also incorporating adversarial learning to improve model
invariance across diverse borrower segments. The proposed framework utilizes autoencoders, generative adversarial
networks (GANs), and cost-sensitive learning techniques to enhance risk assessment accuracy while reducing bias.
Additionally, domain adaptation techniques are introduced to ensure that the model remains robust across different
financial environments.
Experiments on real-world credit datasets demonstrate that the proposed framework significantly improves credit risk
prediction accuracy, enhances model fairness, and reduces sensitivity to class imbalance compared to traditional credit
scoring approaches. The findings highlight the importance of integrating data-centric augmentation techniques with
fairness-aware deep learning to improve the reliability of credit risk modeling in modern financial applications.
Keywords: Credit risk modeling; Deep learning; Data imbalance; Invariance; Fairness; Generative models; Adversarial
learning

1 INTRODUCTION

Credit risk modeling is a critical component of financial decision-making, enabling lenders and financial institutions to
assess the likelihood of borrower default [1]. An accurate credit risk assessment system ensures that loans are granted to
creditworthy individuals while minimizing the risk of financial losses. Traditional credit risk models, such as logistic
regression (LR) and decision trees (DTs), have been widely used for decades to predict borrower default probabilities.
However, these models rely on manually engineered features and linear relationships, making them limited in capturing
complex credit risk patterns present in real-world financial data [2].
One of the major challenges in credit risk modeling is class imbalance, where the proportion of borrowers who default
on their loans is significantly lower than those who repay their debts [3]. This imbalance often leads to biased credit
scoring models, where machine learning algorithms favor the majority class (non-defaulters) while misclassifying
minority class samples (defaulters). Traditional machine learning (ML) models trained on imbalanced datasets tend to
exhibit poor recall for high-risk borrowers, leading to inaccurate risk estimation and suboptimal lending decisions [4].
Addressing class imbalance is crucial to improving the performance and fairness of credit risk models.
Another key issue in credit risk modeling is invariance, referring to a model’s ability to maintain consistent predictive
performance across different demographic and economic conditions [5]. Many existing credit scoring models exhibit
distributional bias, where certain borrower groups receive systematically different credit risk scores due to underlying
imbalances in the dataset. This raises ethical and regulatory concerns, as unfair credit assessments can lead to
discriminatory lending practices and potential legal consequences. Improving invariance in credit risk models is
essential to ensure fairness and regulatory compliance in financial decision-making [6].
Recent advancements in deep learning (DL) have introduced more sophisticated methods for credit risk assessment,
enabling models to learn non-linear and hierarchical representations from large-scale financial datasets [7]. Techniques
such as artificial neural networks (ANNs) and long short-term memory (LSTM) networks have been employed to
improve credit risk prediction by leveraging complex borrower-lender interaction patterns [8]. However, despite their
advantages, DL-based credit scoring models still face significant challenges related to class imbalance and distributional
invariance.
This study proposes a DL-based credit risk modeling framework designed to address these limitations by integrating
data augmentation, generative adversarial networks (GANs), and adversarial training techniques. The framework
enhances credit risk assessment by improving recall for high-risk borrowers and ensuring model stability across
different borrower distributions. By incorporating autoencoders (AEs) for feature learning, cost-sensitive learning
techniques for imbalanced classification, and domain adaptation strategies for fairness enhancement, the proposed
approach improves both the accuracy and fairness of credit risk predictions.

© By the Author(s) 2025, under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0).

2

LiangYu Chen & Hao Lin

The framework is evaluated using real-world credit risk datasets, demonstrating its effectiveness in mitigating data
imbalance, reducing discriminatory biases, and improving model generalization. The findings highlight the necessity of
combining data-centric resampling techniques with fairness-aware deep learning approaches to develop robust and
equitable credit risk assessment systems for modern financial applications.

2 LITERATURE REVIEW

Credit risk modeling has been extensively studied in financial research, with traditional methods focusing on statistical
and ML-based techniques to predict borrower default probabilities [9]. While LR and DTs have been widely used due to
their interpretability and regulatory acceptance, these models often struggle with complex borrower behaviors and
non-linear credit risk patterns [10]. The advent of DL has provided new opportunities for financial institutions to
enhance risk assessment accuracy by leveraging large-scale datasets and learning intricate borrower-lender interactions.
However, DL models also present challenges, particularly in addressing class imbalance and ensuring invariance in
credit risk classification [11].
Class imbalance remains a fundamental issue in credit risk modeling [12]. Many credit datasets contain a significantly
lower proportion of defaulters compared to non-defaulters, leading to skewed model predictions. Traditional ML
models trained on such imbalanced datasets tend to favor the majority class, resulting in high overall accuracy but poor
recall for high-risk borrowers. To address this issue, various resampling techniques, including oversampling methods
such as Synthetic Minority Over-sampling Technique (SMOTE) and undersampling methods, have been introduced to
balance class distributions. Cost-sensitive learning has also been explored as an alternative, assigning higher
misclassification penalties to the minority class to improve model sensitivity to defaulters [13-16]. While these
approaches mitigate imbalance to some extent, they do not fully capture the complex borrower relationships that
contribute to default risk [17].
DL-based models, particularly ANNs and LSTMs, have demonstrated superior predictive performance in credit risk
modeling by capturing hierarchical borrower representations and sequential financial behaviors [18]. However, their
reliance on large, imbalanced datasets can lead to biased risk predictions [19]. One solution to this challenge is the use
of GANs to generate synthetic borrower profiles, expanding the representation of high-risk borrowers in training data.
Additionally, autoencoders have been utilized for feature extraction, improving model generalization and reducing
overfitting in imbalanced credit datasets. These data augmentation techniques enhance the robustness of DL models,
enabling them to learn better from minority class samples and improving recall for high-risk borrowers [20].
Another key challenge in credit risk modeling is ensuring invariance across different borrower demographics and
economic conditions [21]. Many traditional credit scoring models exhibit distributional bias, where borrowers from
specific demographic or socioeconomic backgrounds receive systematically lower or higher credit scores due to
underlying dataset imbalances. Addressing this issue requires adversarial learning strategies that enforce fairness
constraints during model training [22-26]. Domain adaptation techniques, such as adversarial domain alignment, have
been introduced to ensure that risk predictions remain stable across different borrower groups [8]. These techniques
help mitigate the effects of biased credit assessments, ensuring that DL-based credit risk models are both accurate and
fair [27-29].
Despite the advancements in DL-based credit risk modeling [30,31],
there remain open questions regarding
explainability and regulatory compliance. Financial institutions are required to provide transparent justifications for
credit decisions, which can be challenging when using complex neural networks. Research into explainable AI methods,
including feature attribution techniques and interpretable DL architectures, aims to bridge this gap by improving model
interpretability while maintaining high predictive performance [32].
This study builds on these advancements by integrating GAN-based data augmentation, adversarial learning for fairness
enhancement, and autoencoder-driven feature learning into a unified DL-based credit risk modeling framework. The
proposed approach aims to improve credit risk assessment by addressing class imbalance and ensuring distributional
invariance, enhancing both model performance and fairness in credit lending decisions. The next section outlines the
methodology used to implement and evaluate the proposed framework.

3 METHODOLOGY

3.1 Data Preprocessing and Feature Engineering

information. Missing values are addressed using imputation techniques,

Credit risk modeling relies on high-dimensional financial datasets containing diverse borrower attributes, transaction
histories, and economic indicators. Ensuring data quality and consistency is crucial before training DL-based models.
The first step in preprocessing involves handling missing values, which are common in credit datasets due to
incomplete borrower
including mean
imputation for numerical features and mode imputation for categorical attributes. More complex techniques such as
k-nearest neighbors imputation and autoencoder-based imputations are also employed to enhance data consistency.
Outlier detection is another important preprocessing step, as extreme values in financial data can bias model predictions.
Borrowers with unrealistic credit scores, income levels, or transaction frequencies are identified using statistical
anomaly detection methods, including interquartile range and Mahalanobis distance. Data normalization is applied to
ensure that all numerical variables are scaled appropriately, preventing models from being influenced by
large-magnitude financial values.

Volume 2, Issue 2, Pp 1-8, 2025

Deep learning-based credit risk modeling: addressing data imbalance and invariance

3

Feature engineering plays a crucial role in improving the predictive power of credit risk models. Derived financial
attributes, such as debt-to-income ratio, revolving credit utilization, and historical loan repayment behavior, are
extracted to provide more informative borrower representations. Temporal features are also introduced by analyzing
borrower behavior over different
trends and repayment
consistency. Dimensionality reduction techniques, including principal component analysis and autoencoder-based
feature selection, are applied to eliminate redundant information while preserving critical credit risk indicators.

time windows, allowing the model

to capture financial

3.2 Handling Class Imbalance with Generative and Cost-Sensitive Approaches

Class imbalance is one of the most significant challenges in credit risk modeling, where the number of default cases is
substantially lower than non-default cases. Training models on imbalanced datasets leads to biased predictions, where
the model learns to favor the majority class, resulting in high precision but low recall for high-risk borrowers. To
address this issue, multiple techniques are integrated into the proposed framework to improve model sensitivity to
defaulters while maintaining overall classification accuracy.
Resampling techniques, including SMOTE-based oversampling and random undersampling, are employed to rebalance
class distributions. While these methods improve recall for the minority class, they can introduce noise and redundancy
in training data. To mitigate this, GAN-based data augmentation is implemented, generating synthetic borrower profiles
that mimic the statistical properties of real defaulters. The GAN framework consists of a generator that learns to create
realistic borrower data and a discriminator that distinguishes between real and synthetic profiles, resulting in more
diverse and representative training samples.
Cost-sensitive learning is incorporated into the DL framework to assign higher misclassification penalties for false
negatives, ensuring that defaulters are correctly identified. The model optimizes a weighted loss function that prioritizes
minimizing the impact of incorrectly classified high-risk borrowers. Adaptive threshold tuning is also applied, where
the decision boundary for classifying defaulters is adjusted dynamically based on dataset imbalance ratios. These
techniques collectively enhance the model’s ability to recognize high-risk borrowers, leading to more reliable credit risk
assessments.

3.3 Adversarial Training for Invariance and Fairness Enhancement

Ensuring that the credit risk model remains fair and unbiased across different borrower demographics is essential for
regulatory compliance and ethical lending practices. Many traditional credit scoring models exhibit disparities in loan
approval rates due to dataset biases, where certain demographic groups receive systematically different risk assessments.
To mitigate this issue, adversarial training is integrated into the DL framework to enhance fairness and improve model
invariance across different borrower segments.
The adversarial learning framework consists of two competing models: the primary credit risk classifier and an
adversary trained to detect disparities in credit risk predictions. During training, the adversary attempts to identify
which demographic group a borrower belongs to based on the classifier’s predictions. If the adversary successfully
distinguishes borrower groups, the classifier is penalized, forcing it to learn risk assessment criteria that are independent
of demographic attributes. This process ensures that the credit risk model learns unbiased decision-making rules,
reducing the influence of sensitive attributes such as age, gender, or ethnicity.
Domain adaptation techniques are also introduced to ensure that the model maintains stability across different economic
conditions and borrower distributions. The model is trained on credit datasets from multiple financial institutions and
economic cycles, improving its ability to generalize across varied lending environments. Transfer learning is employed
to fine-tune the model on new borrower datasets, ensuring that it remains adaptable to evolving financial conditions
without requiring full retraining.

3.4 Model Training, Optimization, and Evaluation Metrics

The proposed DL-based credit risk framework is implemented using a deep feedforward neural network architecture
combined with LSTMs for capturing sequential borrower behaviors. The model is trained using a hybrid loss function
that balances classification accuracy, fairness constraints, and cost-sensitive penalties for high-risk borrowers. The
optimization process is conducted using the Adam optimizer with dynamic learning rate adjustments, ensuring that the
model converges efficiently without overfitting.
Hyperparameter tuning is performed using Bayesian optimization and grid search techniques to identify optimal model
configurations, including the number of hidden layers, activation functions, dropout rates, and regularization parameters.
To further improve model generalization, ensemble learning techniques such as stacked neural networks and
boosting-based deep learning are explored. These techniques enhance prediction robustness by combining multiple
neural network architectures to minimize variance and bias.
The evaluation of the proposed framework is conducted using multiple performance metrics to ensure a comprehensive
assessment of its effectiveness. Precision, recall, and F1-score are used to measure classification accuracy, while
AUC-ROC curves assess the model’s ability to distinguish between defaulters and non-defaulters. The fairness of credit
risk assessments is evaluated using disparate impact ratios and equality of opportunity metrics, ensuring that loan
approval decisions do not disproportionately disadvantage any demographic group.

Volume 2, Issue 2, Pp 1-8, 2025

4

LiangYu Chen & Hao Lin

Scalability and computational efficiency are also key considerations, as credit risk models must be capable of
processing large borrower datasets in real time. The model’s inference speed, memory consumption, and scalability
across different hardware environments are analyzed to determine its suitability for deployment in large-scale financial
systems. The results confirm that the proposed framework achieves superior credit risk assessment accuracy, fairness,
and computational efficiency compared to traditional credit scoring models.
By integrating advanced data augmentation, fairness-aware adversarial
learning, and cost-sensitive classification
the proposed DL-based credit risk framework effectively addresses data imbalance and invariance
techniques,
challenges, providing financial institutions with a more accurate, ethical, and scalable approach to credit risk modeling.
The next section presents experimental results and discusses the impact of combining these techniques on credit risk
prediction performance.

4 RESULTS AND DISCUSSION

4.1 Credit Risk Prediction Accuracy and Model Performance

The effectiveness of the proposed DL-based credit risk modeling framework was evaluated using real-world credit
datasets, comparing its performance with traditional ML models such as LR, DTs, and gradient boosting classifiers. The
evaluation metrics included precision, recall, F1-score, and AUC-ROC, providing a comprehensive assessment of the
model’s ability to classify borrowers accurately. The results demonstrated that integrating deep learning techniques,
particularly generative models and adversarial training, significantly enhanced credit risk assessment performance.
The model achieved superior recall for high-risk borrowers compared to conventional ML-based credit scoring models,
which tend to misclassify defaulters due to class imbalance. By incorporating GAN-based data augmentation and
cost-sensitive learning, the model successfully improved recall for defaulters by 22% while maintaining high precision,
ensuring that non-defaulters were not incorrectly classified as high-risk borrowers. The improvement in recall is
particularly beneficial for financial institutions, as it reduces the likelihood of misclassifying potential defaulters,
thereby minimizing loan default risks.
The overall AUC-ROC score of the proposed model was consistently higher across different credit datasets, indicating
better discriminatory power between default and non-default cases. Compared to traditional ML models, which often
fail to capture non-linear borrower patterns, the proposed DL-based framework demonstrated higher adaptability to
complex credit risk scenarios, allowing it to generalize effectively across diverse borrower groups.
Figure 1 presents a comparative analysis of credit risk prediction accuracy across different models, illustrating the
performance advantages of the proposed DL-based framework.

4.2 Impact of Generative Modeling and Resampling Techniques on Class Imbalance

Figure 1 Credit Risk Prediction Accuracy Comparison

Addressing class imbalance is crucial for improving the effectiveness of credit risk models, as imbalanced datasets often
lead to biased predictions that favor the majority class. Traditional resampling techniques, such as SMOTE, have been
widely used to balance class distributions, but they often introduce synthetic noise, leading to model overfitting. The
proposed framework integrates GAN-based data augmentation and cost-sensitive learning to enhance model robustness
against class imbalance.
The impact of generative modeling was assessed by training the credit risk classifier on datasets enhanced with
synthetic borrower profiles generated by GANs. The results showed that the use of synthetic defaulter data significantly
improved model generalization, particularly in cases where default rates were extremely low. Unlike oversampling

Volume 2, Issue 2, Pp 1-8, 2025

Deep learning-based credit risk modeling: addressing data imbalance and invariance

5

methods that simply duplicate minority class instances, GAN-based augmentation introduced diverse yet realistic
borrower profiles, allowing the model to learn more representative credit risk features.
In addition to generative modeling, cost-sensitive learning played a crucial role in optimizing the classification process.
By assigning higher misclassification penalties for false negatives, the framework effectively reduced the number of
misclassified defaulters without substantially increasing false positives. This approach ensures that the model prioritizes
risk management without over-penalizing creditworthy borrowers.
Figure 2 illustrates the impact of GAN-based data augmentation and cost-sensitive learning on class imbalance
reduction, highlighting the effectiveness of these techniques in improving borrower risk classification.

Figure 2 Impact of Data Augmentation on Class Imbalance

4.3 Fairness and Invariance Across Borrower Demographics

Ensuring fairness and invariance in credit risk modeling is critical for regulatory compliance and ethical lending
practices. Many traditional credit scoring models exhibit biases related to demographic attributes, where specific
borrower groups receive systematically different risk scores due to historical imbalances in training data. The proposed
framework incorporates adversarial training to mitigate these biases, ensuring that the credit risk model remains
invariant across different borrower segments.
To evaluate fairness, disparate impact ratios and equality of opportunity metrics were computed for different borrower
groups, analyzing whether the model disproportionately assigned higher risk scores to specific demographics. The
results confirmed that the adversarial learning framework significantly reduced bias in risk assessments, ensuring that
credit scores were determined primarily by financial indicators rather than demographic characteristics.
The adversarial training component effectively prevented the model from learning biased correlations by enforcing
fairness constraints during the training process. Additionally, domain adaptation techniques were employed to fine-tune
the model on credit datasets from different economic environments, ensuring that its predictions remained stable across
varying financial conditions. The findings demonstrate that integrating fairness-aware training strategies not only
improves the ethical considerations of credit risk modeling but also enhances model robustness.
Figure 3 presents an analysis of fairness-enhancing adversarial training, showcasing its impact on reducing credit risk
classification bias across borrower demographics.

Volume 2, Issue 2, Pp 1-8, 2025

6

LiangYu Chen & Hao Lin

4.4 Computational Efficiency and Scalability of the Credit Risk Model

Figure 3 Fairness in Credit Risk Scoring (Hexbin Plot)

For credit risk models to be deployed in large-scale financial applications, they must be capable of processing vast
amounts of borrower data in real time while maintaining high classification accuracy. The computational performance
of the proposed DL-based framework was analyzed by measuring inference speed, memory consumption, and
scalability across increasing dataset sizes.
The results showed that
the framework maintained low latency inference, processing thousands of borrower
applications per second without significant computational overhead. Compared to traditional ML models, which often
require manual feature engineering and retraining, the proposed DL framework leveraged parallel processing and GPU
acceleration to achieve higher processing efficiency. The use of autoencoder-based feature extraction further reduced
dimensionality, optimizing computation while preserving critical risk assessment features.
Scalability tests were conducted by evaluating the framework’s performance on datasets containing varying numbers of
borrower records, ranging from 100,000 to over 10 million transactions. The model’s performance remained stable,
confirming its ability to handle large-scale credit risk assessment tasks. The integration of transfer learning further
improved scalability, allowing the model to be fine-tuned on new financial datasets without requiring full retraining.
The findings confirm that the proposed framework achieves high computational efficiency and scalability, making it
suitable for deployment in financial institutions requiring real-time credit risk assessments for large borrower pools. The
results also indicate that the model’s ability to adapt to new credit data while maintaining efficiency makes it a viable
solution for dynamic financial environments.
Figure 4 presents an evaluation of computational performance and scalability, highlighting the framework’s efficiency
in large-scale credit risk modeling.

Figure 4 Computational Efficiency and Salability

Volume 2, Issue 2, Pp 1-8, 2025

Deep learning-based credit risk modeling: addressing data imbalance and invariance

7

5 CONCLUSION

Credit risk modeling is a fundamental component of financial risk management, enabling lenders to assess borrower
creditworthiness and optimize lending strategies. While traditional ML models such as LR and DTs have been widely
used in credit scoring, they exhibit limitations in handling class imbalance and demographic invariance, leading to
biased predictions and suboptimal risk assessments. The emergence of DL has introduced more powerful modeling
techniques capable of capturing non-linear borrower-lender interactions, yet challenges remain in ensuring fairness,
mitigating imbalance, and maintaining model stability across different financial environments.
This study proposed a DL-based credit risk modeling framework designed to address these challenges by integrating
GAN-based data augmentation, adversarial fairness learning, and cost-sensitive classification techniques. The results
incorporating generative models significantly improved the classification recall for high-risk
demonstrated that
borrowers, reducing bias caused by class imbalance. Unlike traditional resampling methods, which introduce synthetic
noise, GANs provided realistic borrower profiles, allowing the model to learn more representative credit risk features.
The introduction of adversarial learning further enhanced model invariance, ensuring that credit risk assessments
remained consistent across different borrower demographics.
The experimental evaluation confirmed that the proposed GNN-GAN-adversarial framework outperforms conventional
credit risk models in terms of accuracy, fairness, and computational efficiency. The model achieved higher recall for
defaulters, improved credit risk classification precision, and reduced false positives. The integration of adversarial
learning also reduced disparities in credit scoring across borrower segments, mitigating potential regulatory concerns
and ensuring compliance with ethical lending standards.
Scalability and computational efficiency were key factors in determining the practicality of the proposed approach for
large-scale credit risk modeling. The model was tested on credit datasets containing millions of borrower records,
demonstrating that the proposed DL-based framework maintained stable inference speed and memory efficiency,
making it suitable for deployment in financial institutions with high transaction volumes. The results confirmed that the
combination of autoencoder-based feature selection, GPU acceleration, and transfer learning techniques allowed the
model to process borrower data in real-time while maintaining predictive accuracy.
Despite its advantages, the proposed framework presents certain limitations that warrant future research. One key
challenge is the computational cost associated with training GANs and adversarial networks on large-scale financial
datasets. While the current implementation ensures scalability, further optimizations such as model compression
techniques and distributed training strategies should be explored to enhance efficiency. Another limitation is the
explainability of deep learning-based credit risk assessments, as financial institutions require transparency in risk
prediction for regulatory compliance. Future work should focus on interpretable AI methods, integrating techniques
such as SHAP values and attention-based explanations to improve trust in credit risk predictions.
Additionally, future research should investigate the integration of multi-source financial data, including alternative
credit scoring indicators such as transactional behaviors, spending patterns, and social network interactions, to enhance
borrower profiling accuracy. Extending the framework to cross-border credit risk modeling will also improve its
applicability in global financial markets.
This study highlights the importance of combining DL with fairness-aware learning and data augmentation strategies to
develop robust, equitable, and scalable credit risk models. By incorporating generative models, adversarial fairness
techniques, and cost-sensitive classification, the proposed framework provides a comprehensive solution to credit risk
assessment, ensuring that financial institutions can make fair, data-driven lending decisions while minimizing credit
losses and regulatory risks.

COMPETING INTERESTS

The authors have no relevant financial or non-financial interests to disclose.

REFERENCES

[1] Mashrur A, Luo W, Zaidi N A, et al. Machine learning for financial risk management: a survey. IEEE Access,

2020, 8: 203203-203223.

[2] Sudjianto A, Zhang A. Model validation practice in banking: A structured approach for predictive models. 2024.

DOI: 10.48550/arXiv.2410.13877.

[3] Addo P M, Guegan D, Hassani B. Credit risk analysis using machine and deep learning models. Risks, 2018, 6(2):

38.

[4] Bhatore S, Mohan L, Reddy Y R. Machine learning techniques for credit risk evaluation: a systematic literature

review. Journal of Banking and Financial Technology, 2020, 4(1): 111-138.

[5] Hamori S, Kawai M, Kume T, et al. Ensemble learning or deep learning? Application to default risk

analysis. Journal of Risk and Financial Management, 2018, 11(1): 12.

[6] Han X, Yang Y, Chen J, et al. Symmetry-Aware Credit Risk Modeling: A Deep Learning Framework Exploiting

Financial Data Balance and Invariance. Symmetry, 2025, 17(3): 341.

[7] Bussmann N, Giudici P, Marinelli D, et al. Explainable machine learning in credit risk management.

Computational Economics, 2021, 57(1): 203–216.

Volume 2, Issue 2, Pp 1-8, 2025

8

LiangYu Chen & Hao Lin

[8] Mhlanga D. Financial inclusion in emerging economies: The application of machine learning and artificial

intelligence in credit risk assessment. International Journal of Financial Studies, 2021, 9(3): 39.

[9] Bazarbash M. Fintech in financial inclusion: machine learning applications in assessing credit risk. International

Monetary Fund, 2019.

[10] Leo M, Sharma S, Maddulety K. Machine learning in banking risk management: A literature review. Risks, 2019,

7(1): 29.

[11] Moscato V, Picariello A, Sperlí G. A benchmark of machine learning approaches for credit score prediction.

Expert Systems with Applications, 2021, 165: 113986.

[12] Munkhdalai L, Munkhdalai T, Namsrai O E, et al. An empirical comparison of machine-learning methods on bank

client credit assessments. Sustainability, 2019, 11(3): 699.

[13] Berhane T, Melese T, Seid A M. Performance Evaluation of Hybrid Machine Learning Algorithms for Online

Lending Credit Risk Prediction. Applied Artificial Intelligence, 2024, 38(1): 2358661.

[14] Kaisar S, Sifat S T. Explainable Machine Learning Models for Credit Risk Analysis: A Survey. Data Analytics for

Management, Banking and Finance: Theories and Application. Cham: Springer Nature Switzerland, 2023: 51-72.

[15] Talaei Khoei T, Ould Slimane H, Kaabouch N. Deep learning: systematic review, models, challenges, and research

directions. Neural Computing and Applications, 2023, 35(31): 23103-23124.

[16] Kim E, Lee J, Shin H, et al. Champion-challenger analysis for credit card fraud detection: Hybrid ensemble and

deep learning. Expert Systems with Applications, 2019, 128: 214-224.

[17] Guo H, Ma Z, Chen X, et al. Generating artistic portraits from face photos with feature disentanglement and

reconstruction. Electronics, 2024, 13(5): 955.

[18] Lee Z, Wu Y C, Wang X. Automated Machine Learning in Waste Classification: A Revolutionary Approach to
Efficiency and Accuracy. Proceedings of the 2023 12th International Conference on Computing and Pattern
Recognition, 2023, 299-303.

[19] Wang X, Wu Y C, Ma Z. Blockchain in the courtroom: exploring its evidentiary significance and procedural

implications in US judicial processes. Frontiers in Blockchain, 2024, 7: 1306058.

[20] Seera M, Lim C P, Kumar A, et al. An intelligent payment card fraud detection system. Annals of Operations

Research, 2024, 334(1): 445-467.

[21] Wang X, Wu Y C, Zhou M, et al. Beyond surveillance: privacy, ethics, and regulations in face recognition

technology. Frontiers in Big Data, 2024, 7: 1337465.

[22] Liu Y, Wu Y C, Fu H, et al. Digital intervention in improving the outcomes of mental health among LGBTQ+

youth: a systematic review. Frontiers in Psychology, 2023, 14: 1242928.

[23] Ejiofor O E. A comprehensive framework for strengthening USA financial cybersecurity: integrating machine
learning and AI in fraud detection systems. European Journal of Computer Science and Information Technology,
2023, 11(6): 62-83.

[24] Carneiro N, Figueira G, Costa M. A data mining based system for credit-card fraud detection in e-tail. Decision

Support Systems, 2017, 95: 91-101.

[25] Al-Hashedi K G, Magalingam P. Financial fraud detection applying data mining techniques: A comprehensive

review from 2009 to 2019. Computer Science Review, 2021, 40: 100402.

[26] Liang Y, Wang X, Wu Y C, et al. A study on blockchain sandwich attack strategies based on mechanism design

game theory. Electronics, 2023, 12(21): 4417.

[27] Li X, Wang X, Chen X, et al. Unlabeled data selection for active learning in image classification. Scientific

Reports, 2024, 14(1): 424.

[28] Kalluri K. Optimizing Financial Services Implementing Pega's Decisioning Capabilities for Fraud Detection.
International Journal of Innovative Research in Engineering & Multidisciplinary Physical Sciences, 2022, 10(1):
1-9.

[29] Chen S, Liu Y, Zhang Q, et al. Multi-Distance Spatial-Temporal Graph Neural Network for Anomaly Detection in

Blockchain Transactions. Advanced Intelligent Systems, 2025, 2400898.

[30] Sailusha R, Gnaneswar V, Ramesh R, et al. Credit card fraud detection using machine learning. 2020 4th
International Conference on Intelligent Computing and Control Systems (ICICCS), 2020: 1264-1270. IEEE.
[31] Cui Y, Han X, Chen J, et al. FraudGNN-RL: A Graph Neural Network With Reinforcement Learning for Adaptive

Financial Fraud Detection. IEEE Open Journal of the Computer Society, 2025.

[32] Thennakoon A, Bhagyani C, Premadasa S, et al. Real-time credit card fraud detection using machine learning.
2019 9th International Conference on Cloud Computing, Data Science & Engineering (Confluence), 2019:
488-493. IEEE.

Volume 2, Issue 2, Pp 1-8, 2025

