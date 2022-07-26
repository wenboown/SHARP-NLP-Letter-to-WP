############################################################################################################################################
**SUPPLEMENTARY MATERIAL**: |long-title|
############################################################################################################################################

.. |long-title| replace:: *Are language deficits associated with psychosis risk universal? Automated analyses of*
                            *spoken language in Mandarin-speaking youths at clinical high risk for psychosis,* by Agurto et al.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Carla Agurto, Raquel Norel, Bo Wen, Yanyan Wei, Dan Zhang, Zarina
Bilgrami, Xiaolu His, Tianhong Zhang, Ofer Pasternak, Huijun Li,
Matcheri Keshavan, Larry J. Seidman, Susan Whitfield-Gabrieli, Martha E.
Shenton, Margaret A. Niznikiewicz, Jijun Wang, Guillermo Cecchi, Cheryl
M. Corcoran, William S. stone.

In press, World Psychiatry

============
Subjects
============

Supplementary Table 1. Demographics and clinical variables of the
cohorts.

+-------------+-------------+-------------+-------------+-------------+
|             | Category    | CHR         | Healthy     | Statistics  |
|             |             |             | Controls    |             |
+=============+=============+=============+=============+=============+
| Demographic | Sex         | 20 (11      | 25 (12      | Chi-Square: |
| s           |             | females)    | females)    | 0.22,       |
|             |             |             |             | p=0.64      |
+-------------+-------------+-------------+-------------+-------------+
|             | Age         | 19.6 +/-    | 24.9 +/-    | KS-test:    |
|             |             | 6.4         | 1.9         | 0.75,       |
|             |             |             |             | p=1E-6      |
+-------------+-------------+-------------+-------------+-------------+
|             | Race        | 100%        | 100%        | --          |
|             |             | Chinese     | Chinese     |             |
+-------------+-------------+-------------+-------------+-------------+
|             | Education   | 11.4 +/-    | 16.7 +/-    | KS-test:    |
|             | in years    | 4.0         | 1.4         | 0.7, p=1E-5 |
+-------------+-------------+-------------+-------------+-------------+
| SIPS/SOPS   | Negative    | 10.2 +/-    | --          | --          |
|             | Symptoms    | 5.4         |             |             |
| scores      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
|             | Positive    | 9.1 +/- 4.0 | --          | --          |
|             | Symptoms    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

========================
Supplementary Methods
========================

-----------------
Preprocessing
-----------------

To analyze only the speech of the subjects, we needed to identify and
extract the parts of their voice from the whole interview since only one
channel was used in the recording. Given that manual transcription
contained the timestamps that indicate when the subject is speaking, we
used that information to segment the recording and then join only
subject’s segments to generate a new audio file.

-----------------
Metrics
-----------------

Acoustic features: Based on the literature as well as our previous work
on the characterization of CHR subjects\ :sup:`1,2,3,4`, we extracted
several features that can capture flattened intonation, disturbed flow
of speech (e.g., voice break), changes in speech rate and other
characteristics found in studies that characterize speech in
schizophrenia patients. All these features were extracted in the
pre-processed audio containing only the subject’s speech in Mandarin. We
grouped all the extracted features in 8 categories: pitch variations,
changes in rhythm, voice stability, spectral characterization, vowel
space, MFCCs, chroma features, and noise measurements (see Table 2).
More information about the processing used to compute these features can
be found here\ :sup:`4-6`.

English-based linguistic features: To perform a thorough
characterization of the content of the subject’s speech, we extracted
features at the word, sentence, and paragraph level. To do so, we
prepared the text to be analyzed by tokenizing and lemmatizing it using
the NLTK library\ :sup:`16`. In addition, we only kept the content words
of the text by removing the stop words (e.g., “then”) from our analysis,
using the provided list from natural language toolkit library in python
(NLTK):sup:`7`.

At the word level, we used part of speech (PoS) tagging\ :sup:`8` to
obtain the normalized frequency (percentage) of different parts of
speech such as adjectives, verbs, etc. used by the subject during the
interview (see Table 2). We also quantified content and unique words
normalized by the total number of words uttered by the subject.

In the case of features extracted at the sentence level, we used two
categories: graph-based and speech coherence. For graph-based features,
each word (previously lemmatized) becomes a graph node while consecutive
words (two nodes) are connected using edges. From that graphical
representation of the text, we computed standard mathematical graph
properties listed in\ :sup:`9` and summarized in Table 2. To quantify
speech coherence, we used the Universal Sentence Encoder\ :sup:`10` text
embedding, an algorithm trained by Google with a deep averaging network
encoder, that numerically represents each text (word, sentence,
paragraph) using 512 dimensions. Once each sentence is vectorized,
cosine similarity is used to evaluate the similarity (coherence) between
a question (interviewer) and the answer (subject), as well as
consecutive answers of the subjects. To summarize each of these
coherence metrics, we report 4 statistical descriptors (percentiles 5,
50, 95 and MAD (i.e. mean absolute deviation, which is a robust measure
of variability). Only for English transcripts (to avoid redundancy) did
we also quantify the number of interactions between the interviewer and
the subject by counting the transitions from questions to answers (i.e.,
number of switches).

Finally, for the analysis at a paragraph level, the whole content of the
subject speech was used to perform sentiment analysis using Watson
Natural Language Understanding API\ :sup:`11`. This tool provides the
following metrics: overall sentiment (positive, negative), as well as
scores for specific sentiments (i.e., anger, disgust, fear, joy, and
sadness).

Mandarin-based linguistic features: To be able to compare performance
between the use of Mandarin transcripts and their translated transcripts
in English we extracted the same type of features described above but
with the following variations in the text processing. To perform
tokenization in Mandarin, we need to consider that this language is
written without spacing. Therefore, we used the Electra base version of
NLP features trained on the close-source Chinese corpus via HanLP 2.1
library\ :sup:`12`. By using this library, we obtained the tokenized
words and POS tagging based on the Penn Chinese Treebank (3.0):sup:`13`.
Unlike English, Mandarin does not require lemmatization. Specific to
Mandarin, POS features included other categories besides the ones
reported for English, including localizers, associative/possessive, and
measure words, among others. Also, wh-words are not included among POS
tags in Mandarin.

For coherence features, we used Sentence Transformers\ :sup:`14` to
obtain the sentence embedding. The consequent steps are a bit different
from English. For Q-A coherence, the cosine similarity is computed
between the question and the first sentence in the answer paragraph. For
A-A coherence, cosine similarity is computed on 1\ :sup:`st`,
2\ :sup:`nd`, 3\ :sup:`rd` order within the answer paragraph, i.e.,
between neighboring sentences (1:sup:`st` order), next-neighboring
sentences (2:sup:`nd` order), and skipping 2 sentences in between
(3:sup:`rd` order).

For graph-based features, each tokenized word is a node. After these
pre-processing steps, the feature extraction in Mandarin is equivalent
to the English one. However, for the sentiment analysis, the used
library\ :sup:`20` does not provide specific sentiments (e.g., anger)
for Mandarin. Therefore, we also incorporate local sentiment by
computing overall sentiment score for each answer of the subject and
summarized these values using 5 descriptors (median, interquartile
range, MAD (median absolute deviation), robust minimum and maximum).

Table 2. Summary of the extracted acoustic features for analysis

+-----------------------+-----------------------+-----------------------+
| Type of Feature       | Category              | List of all features  |
+=======================+=======================+=======================+
| Acoustic              | Pitch variations      | Pitch distribution,   |
|                       |                       | mean and std of       |
|                       |                       | glottal pulse period  |
+-----------------------+-----------------------+-----------------------+
|                       | Changes in rhythm     | Pause and syllable    |
|                       |                       | duration              |
|                       |                       | distribution,         |
|                       |                       | articulation and      |
|                       |                       | speech rates, voice   |
|                       |                       | and unvoiced ratio.   |
+-----------------------+-----------------------+-----------------------+
|                       | Voice stability       | Jitter, shimmer,      |
|                       |                       | voice breaks          |
+-----------------------+-----------------------+-----------------------+
|                       | Spectral              | Max dB, max           |
|                       | characterization      | frequency, energy,    |
|                       |                       | slope                 |
+-----------------------+-----------------------+-----------------------+
|                       | Vowel space           | Total area, ‘a-i-u’   |
|                       |                       | area, formants and    |
|                       |                       | bandwidths 1,2,3      |
|                       |                       | distribution          |
+-----------------------+-----------------------+-----------------------+
|                       | Mel-frequency         | Thirteen MFCCs        |
|                       | cepstral coefficients |                       |
|                       | (MFCC)                |                       |
+-----------------------+-----------------------+-----------------------+
|                       | Chroma                | Twelve pitch class    |
|                       |                       | profiles              |
+-----------------------+-----------------------+-----------------------+
|                       | Noise measurements    | Noise to harmonics    |
|                       |                       | ratio, harmonics to   |
|                       |                       | noise ratio, mean     |
|                       |                       | autocorrelation       |
+-----------------------+-----------------------+-----------------------+
|                       | Parts of speech &     |    Nouns, verbs,      |
|                       | Word count            |    adverbs,           |
|                       |                       |    determiners,       |
|                       |                       |    adjectives,        |
|                       |                       |    Wh-words. Content  |
|                       |                       |    and unique words.  |
+-----------------------+-----------------------+-----------------------+
| English-based         | Graph-based           |    Number of nodes,   |
| linguistic            |                       |    edges, parallel    |
|                       |                       |    edges in the       |
|                       |                       |    graph. Number of   |
|                       |                       |    largest strongly   |
|                       |                       |    connected          |
|                       |                       |    components.        |
|                       |                       |    Average and std of |
|                       |                       |    degrees. Number of |
|                       |                       |    words and loops of |
|                       |                       |    1,2,3,4 and 5      |
|                       |                       |    words, Graph       |
|                       |                       |    density.           |
+-----------------------+-----------------------+-----------------------+
|                       | Speech coherence      | Question-Answer       |
|                       |                       | coherence,            |
|                       |                       | Answer-Answer         |
|                       |                       | coherence             |
+-----------------------+-----------------------+-----------------------+
|                       | Sentiment Analysis    | Overall sentiment     |
|                       |                       | (positive and         |
|                       |                       | negative), anger,     |
|                       |                       | fear, sadness, joy,   |
|                       |                       | disgust.              |
+-----------------------+-----------------------+-----------------------+
| Mandarin-based        | Parts of speech &     |    33 POS tags that   |
| linguistic            | Word count            |    include all listed |
|                       |                       |    for English        |
|                       |                       |    (except Wh- words) |
|                       |                       |    plus localizer,    |
|                       |                       |    measure word,      |
|                       |                       |    among others.      |
|                       |                       |    Content and unique |
|                       |                       |    words.             |
+-----------------------+-----------------------+-----------------------+
|                       | Graph-based           | Number of nodes,      |
|                       |                       | edges, parallel edges |
|                       |                       | in the graph. Number  |
|                       |                       | of largest strongly   |
|                       |                       | connected components. |
|                       |                       | Average and std of    |
|                       |                       | degrees. Number of    |
|                       |                       | words and loops of    |
|                       |                       | 1,2,3,4 and 5 words,  |
|                       |                       | Graph density.        |
+-----------------------+-----------------------+-----------------------+
|                       | Speech Coherence      | Question-Answer       |
|                       |                       | coherence,            |
|                       |                       | Answer-Answer         |
|                       |                       | coherence             |
+-----------------------+-----------------------+-----------------------+
|                       | Sentiment Analysis    | Overall sentiment     |
|                       |                       | (positive, negative,  |
|                       |                       | neutral), and         |
|                       |                       | distribution of       |
|                       |                       | answer’s sentiment.   |
+-----------------------+-----------------------+-----------------------+

A total of 341 features were extracted for each subject’s session.
However, there were two issues that we considered before performing any
analysis: 1) Age and education years were not matched in both cohorts
(CHR and HC); and 2) Features can be highly correlated, meaning that we
could have redundant information in the characterization, potentially
decreasing the performance of any machine learning algorithm. For the
first issue, we corrected the features for both age and education years
by regressing the features to these variables in the HC cohort and used
the same parameters to remove possible effects in the CHR cohort. For
the second issue, we measured the correlation between features, and
discarded features that had an associated correlation coefficient of
0.95 or more. After this procedure, we ended with 300 features. After
addressing these issues, we performed two main experiments. The first
experiment was to evaluate if the features can help us distinguish
between spoken language in CHR and HC. The second experiment was to
evaluate if the extracted features can be used to infer SIPS/SOPS
positive and negative symptoms for patients. For both experiments,
features were normalized to have mean=0, variance=1, and performance was
evaluated using 10-fold cross validation. Depending on the experiment
(classification or inference), different machine learning algorithms
were used. For classification, we used random forest and support vector
machines (SVM) with two different kernels, Linear and RBF. These
experiments were performed independently for each of the three types of
features extracted as well as the combination of the three; in all
cases, no significant differences were observed between the classifier
models. In addition, for classification, we repeated the experiments 20
times to identify the mean prediction accuracy. Finally, to complement
these findings, a post-hoc analysis that checked for the most relevant
features in the best models was performed. All statistical measurements
(Spearman correlation, Wilcoxon paired t-test and Kolmogorov Smirnov)
used in this study considered the non-normal distribution of the
analyzed variables.

================================
Supplementary Results
================================

--------------------------------------------------
Classification between CHR v. HC
--------------------------------------------------

High performance results were obtained for the three types of features
used in this analysis (Supplementary Figure 1). Best accuracy values
ranged from 0.88 (only acoustic features) to 0.95 (only English-based
linguistic features), while by using the AUC metric, the performance
values ranged from 0.91 (only acoustic features) to 0.99 (only
English-based linguistic features). All performance values were higher
than chance probability. When we compared the performance between
English and Mandarin-based linguistic features, there is only a
statistically significant difference for one classifier: RBF SVM
(Wilcoxon paired test, p=2E-6) and the difference is marginal. While
performance results using only acoustic features are very high, results
are significantly lower than linguistic features for all classifiers.
There is no improvement with respect to the highest performance model
after joining all the type of features. In fact, results using only
English-based linguistic features are significantly better, especially
for RBF (Wilcoxon paired test, p=2E-6) and linear SVM (Wilcoxon paired
test, p=1E-4).

A post hoc analysis to find the most relevant features in the models was
performed only for Linear SVM, as it assigns a coefficient to each
feature. Supplementary Figure 2 shows the results of the top 5 features
across 20 runs for each fold (200 values). Positive weights indicate
that the value of a feature is higher for the CHR cohort while a
negative weight indicates that the value of the feature is higher for HC
cohort. Among the most relevant acoustic features, we found that
bandwidth of the first formant (robust minimum), voiced only pause
duration and spectral spread are higher for CHR while total duration of
pauses and chroma #11 are higher for HC. Note that the top 5 acoustic
features have similar weights in the model which indicates that their
contribution is similar. We also observed that similar features between
English and Mandarin such as coherence between questions and answer
(robust minimum) have the same orientation in the weight analysis (See
Supplementary Figure 2 ), this feature being more predominant in
Mandarin (KS test for English: p=6E-5, and for Mandarin: p=4.5E-6). An
additional analysis (see Supplementary Figure 3) showed that the
correlation between languages for coherence is r=0.70. We also noticed
that between predicative-adjective (Mandarin) and adjective (English),
there is a correlation of r=0.60. Correlations between other features
are lower (r<0.60) which may indicate that each type of feature is
capturing different aspects of the interviews’ content.

|fig1|

Supplementary Figure 1 Classification performance results. Bars indicate
the mean performance value and error bars indicates the 95% confidence
interval across 20 runs. Accuracy and AUC values are shown in the left
and right side, respectively. Different shades of bars are used to
indicate the type of feature used in the model.

|fig2|

Supplementary Figure 2 Top 5 relevant features of best models for each
type of feature. Features were selected based on the normalized weight
of only Linear SVM models. Bars indicate the mean normalized weight
value and error bars indicates the 95% confidence interval across 20
runs for the Linear SVM models. Positive weights indicate that feature
values are higher for CHR, and negative weights indicate that the
feature values are higher for HC. a) Results of only using acoustic
features in the models, b) Results of only using English-based
linguistic features in the models, and c) Results of only using
Mandarin-based linguistic features in the models, d) Description of each
of the features shown in (a)-(c).

|fig3|

Supplementary Figure 3 Comparison between relevant features of
English-based and Mandarin-based linguistic features. a) Heatmap of the
correlation between both types of features, b) Comparison between both
types of features of coherence Q-A (robust minimum), and c) Comparison
between predicative-adjective and adjective.

---------------------------------------------------------------------------
Inference of SIPS/SOPS positive and negative symptom scores.
---------------------------------------------------------------------------


Only acoustic features were able to infer SIPS/SOPS scores with high
performance (negative symptoms: r= 0.69, p=8E-4, positive symptoms:
r=0.49, p=3E-2). Using linguistic features, the achieved performances
were low (r<0.1) except for Mandarin-based linguistic features. These
features can infer negative symptoms with r=0.36; however, given the
small cohort, the results are not statistically significant (p=1E-1).
When we analyzed the relevant features in the acoustic models, we found
that degree of voice break and standard deviation (std) of the period
are the most relevant features to infer positive symptoms. A statistical
test reveals that these features have correlations of r=0.75 (p=1E-4)
and r=0.60 (p=5E-3). On the other hand, the most relevant features for
negative symptoms are related to MFCC coefficients #1 (r=-0.67, p=1E-3)
and #8 (r=0.61, p=4E-3). Lastly, although the model to infer negative
symptoms using Mandarin-based linguistic features did not achieve
statistical significance, we found that the robust minimum of the second
order coherence among answers, one of the extracted features, has a
correlation of r=0.59, p=7E-3 with these symptoms.

|fig4|

Supplementary Figure 4 Regression results for acoustic features. a)
Performance of the cross-validated models using 3 different machine
learning algorithms. b) Relevant features to infer positive symptoms
score used in the best model (Lasso). Note that features were corrected
by age and education years so values are also shifted to negative
values. c) Top features to infer negative symptoms used in the best
model (Linear Regression).

==============
References:
==============

    1. Bernardini, F. *et al.* Associations of acoustically measured tongue/jaw movements and portion of time
    speaking with negative symptom severity in patients with schizophrenia in Italy and the United States. *Psychiatry
    Res.* **239**, 253–258 (2016).

    2. Covington, M. A. *et al.*
    Phonetic measures of reduced tongue movement correlate with negative
    symptom severity in hospitalized patients with first-episode
    schizophrenia-spectrum disorders. *Schizophr. Res.* **142**, 93–95
    (2012).

3. Zhang, J., Pan Z., Gui, C., Zhu, J. & Cui, D. Clinical
investigation of speech signal features among patients with
schizophrenia. *Shanghai Arch. Psychiatry* **28**, 95–102.4. Agurto, C.
*et al.* Analyzing acoustic and prosodic fluctuations in free speech to
predict psychosis onset in high-risk youths. in *2020 42nd Annual
International Conference of the IEEE Engineering in Medicine & Biology
Society (EMBC)* 5575–5579 (IEEE, 2020).5. Praat Vocal Toolkit: Cut
pauses. http://www.praatvocaltoolkit.com/cut-pauses.html.6.
Giannakopoulos, T. pyAudioAnalysis: An Open-Source Python Library for
Audio Signal Analysis. *PLOS ONE* **10**, e0144610 (2015).7. NLTK::
Natural Language Toolkit. https://www.nltk.org/.8. Santorini, B.
Part-of-Speech Tagging Guidelines for the Penn Treebank Project (3rd
Revision). 37 (1990).9. Mota, N. B. *et al.* Speech graphs provide a
quantitative measure of thought disorder in psychosis. *PloS One* **7**,
e34928 (2012).10. Cer, D. *et al.* Universal Sentence Encoder.
*ArXiv180311175 Cs* (2018).11. IBM Watson Natural Language Understanding
- Features.
https://www.ibm.com/cloud/watson-natural-language-understanding/details
(2021).12. mtl — HanLP Documentation.
https://hanlp.hankcs.com/docs/api/hanlp/pretrained/mtl.html.13. Xia, F.
The Part-Of-Speech Tagging Guidelines for the Penn Chinese Treebank
(3.0). *IRCS Tech. Rep. Ser.* (2000).14. Pretrained Models —
Sentence-Transformers documentation.
https://www.sbert.net/docs/pretrained_models.html#multi-lingual-models.

.. |fig1| image:: figs/fig1.png
   :width: 6.32407in
   :height: 2.13583in
.. |fig2| image:: figs/fig2.png
   :width: 6.40278in
   :height: 4.01389in
.. |fig3| image:: figs/fig3.png
   :width: 6.5in
   :height: 1.67222in
.. |fig4| image:: figs/fig4.png
   :width: 6.5in
   :height: 3.26806in
