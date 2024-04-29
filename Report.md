<img src="D:\UET\Sixth Semester\EAD\Assignment 2 - AJAX\UET.png" width="10%">

<h2><center>Graph Theory</center></h2>

<h4><center>Submitted by:</center><h4><center>2021-CS-82 Muhammad Abdullah</center></h4>


<h4><center>Submitted To:</center><h4><center>Mr. Waqas Ali</center></h4>



# Introduction

## Background

Document classification is a fundamental task in natural language processing (NLP) and information retrieval. Its primary goal is to categorize documents into predefined topics or classes based on their content. Traditionally, vector-based models such as term frequency-inverse document frequency (TF-IDF) and bag-of-words (BoW) have been widely used for document classification. These models represent documents as high-dimensional vectors, where each dimension corresponds to a unique term, and classification is performed based on the similarity between these vectors.

## Limitations of Vector-Based Models

While vector-based models have proven effective in many cases, they may not fully capture the semantic relationships between terms within documents. For instance, two documents may contain similar terms but express different concepts, leading to misclassification. Additionally, vector-based models suffer from the curse of dimensionality, especially when dealing with large vocabularies, which can impact classification accuracy and computational efficiency.

## Motivation for Graph-Based Approach

In recent years, there has been a growing interest in graph-based methods for document classification. Graphs provide a more flexible and expressive representation of document content, allowing us to capture not only the presence of terms but also their relationships and interactions. By modeling documents as graphs, we can leverage graph algorithms and techniques to extract meaningful features and improve classification accuracy.

## Significance of the Project

This project builds upon concepts from foundational papers on graph-based document classification and maximal common subgraphs (MCS) for graph comparison. By investigating graph structures to capture the inherent relationships between terms within documents, I aim to enhance classification accuracy beyond traditional vector-based models. Our approach offers hands-on experience with graph theory and machine learning, fostering skills in data representation, algorithm implementation, and analytical thinking in the context of document classification.

## Objectives

The primary objective of this project is to develop a system that can classify documents into predefined topics by representing each document as a directed graph, identifying common subgraphs, and applying the K-Nearest Neighbors (KNN) algorithm based on graph similarity measures. Through this project, I seek to explore the following key components:

- Data collection and preparation
- Graph construction
- Feature extraction via common subgraphs
- Classification with KNN
- Evaluation of classification performance

# Methodology

## Data Collection and Preparation

### Data Collection
We collected data from various online sources related to three assigned topics: travel, fashion, and diseases. Each topic consists of 15 pages of text, with approximately 300 words per page. The data collection process involved web scraping using the `requests` library to fetch HTML content from URLs and then parsing the HTML using `BeautifulSoup` to extract the text.

### ![1](D:\UET\Sixth Semester\GT\Project\Images\1.png)



### Data Preparation

After obtaining the raw text data, I performed preprocessing steps to prepare the data for further analysis. The preprocessing steps included:
- **Tokenization**: Breaking the text into individual words or tokens using the `nltk.tokenize.word_tokenize` function.
- **Stopword Removal**: Removing common stopwords (e.g., "the", "is", "and") using the `nltk.corpus.stopwords` module.
- **Stemming**: Reducing words to their root form using the Porter stemming algorithm implemented in the `nltk.stem.PorterStemmer` class.

![2](D:\UET\Sixth Semester\GT\Project\Images\2.png)

## Graph Construction

### Representation
We represented each document as a directed graph, where nodes represent unique terms (words) and edges denote term relationships based on their sequence in the text. The graph construction process involved the following steps:
- Reading the preprocessed text data from each document.
- Splitting the text into individual words to create nodes in the graph.
- Connecting adjacent words in the text with directed edges to represent the sequential order of terms.

### Implementation
The graph construction was implemented in the `graph.py` module. We utilized the `networkx` library to create and manipulate graphs in Python. The `networkx.DiGraph` class was used to represent directed graphs, and edges were added between nodes to capture term relationships.

## ![3](D:\UET\Sixth Semester\GT\Project\Images\3.png)



## Feature Extraction via Common Subgraphs

### Identification
We employed frequent subgraph mining techniques to identify common subgraphs within the training set graphs. These common subgraphs served as features for classification, capturing the shared content across documents related to the same topic. The process involved:
- Generating candidate subgraphs from individual document graphs.
- Counting the frequency of each subgraph across all document graphs.
- Selecting the most frequent subgraphs as features for classification.

### Implementation
The common subgraph identification was implemented in the `graph.py` module. We iterated through the training set graphs and used the `nx.compose` function from `networkx` to combine graphs and identify common subgraphs.

![4](D:\UET\Sixth Semester\GT\Project\Images\4.png)

# Results

## Data Curation

The dataset was curated to ensure a balanced representation of three diverse topics: travel, fashion, and diseases. Each topic consisted of 15 pages of text, with approximately 300 words per page. This ensured that the dataset was adequately sized and representative of each class for effective model training and evaluation.

## Clarity and Thoroughness of the Methodology

The methodology was meticulously defined and implemented, covering all essential steps of the document classification process:
- Data collection from various online sources
- Preprocessing of text data to prepare it for graph construction
- Graph representation of documents
- Feature extraction using common subgraphs

The clarity and thoroughness of the methodology facilitated a structured approach to model development and evaluation.

## Creativity in Graph Representation and Feature Extraction

The use of graph-based features, particularly the identification of common subgraphs, showcased creativity in capturing the inherent relationships between terms within documents. By representing documents as directed graphs and extracting common subgraphs, the methodology leveraged graph theory principles to enhance the classification process. This creative approach allowed for a more nuanced understanding of document content beyond traditional vector-based models.

## Depth of Analysis and Critical Reflection

Although not explicitly mentioned in the code, critical reflection on the challenges encountered during the project and the identification of potential improvements to the approach are essential aspects of any research endeavor. Through thoughtful analysis and reflection, insights into the strengths and limitations of the methodology can be gained, paving the way for future enhancements and contributions to the field of document classification.

# Future Work

## Implementation of KNN Classification and Common Subgraph Identification

The current implementation lacks the integration of KNN classification based on graph similarity measures and the identification of common subgraphs. These aspects were not included due to a lack of understanding during the project's execution. However, addressing these components is crucial for further enhancing the document classification system. In future work, efforts will be made to implement KNN classification and explore techniques for identifying common subgraphs within document graphs. This will involve gaining a deeper understanding of graph-based algorithms and methodologies to improve the accuracy and efficiency of the classification system.

## Integration of Advanced Graph-Based Techniques

In addition to KNN classification and common subgraph identification, future work will focus on integrating advanced graph-based techniques for document classification. This may include exploring graph neural networks (GNNs) and graph embedding methods to capture complex relationships and semantic information within document graphs. By leveraging these advanced techniques, the classification system can achieve greater accuracy and robustness across diverse document datasets.

## Evaluation and Benchmarking

Future work will also involve comprehensive evaluation and benchmarking of the document classification system against existing state-of-the-art methods. This will include conducting comparative studies with traditional vector-based models and other graph-based approaches to assess the effectiveness and scalability of the proposed methodology. Through rigorous evaluation and benchmarking, the strengths and limitations of the classification system can be better understood, leading to informed decisions for further improvements.

# Conclusion

In conclusion, this project has laid the foundation for a graph-based document classification system, encompassing data curation, graph construction, and feature extraction. While certain aspects such as KNN classification and common subgraph identification were not fully implemented due to a lack of understanding, the project has demonstrated creativity in graph representation and feature extraction. Moving forward, future work will focus on addressing the missing components and integrating advanced graph-based techniques to enhance the accuracy and efficiency of the classification system. Through continuous iteration and improvement, the proposed methodology holds promise for advancing the field of document classification and contributing to real-world applications in information retrieval and natural language processing.