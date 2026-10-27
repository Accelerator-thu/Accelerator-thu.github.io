---
title: 'Towards Automated Model Design on Recommender Systems'

# Authors
authors:
  - Tunhou Zhang
  - Dehua Cheng
  - Yuchen He
  - Zhengxing Chen
  - Xiaoliang Dai
  - Liang Xiong
  - Yudong Liu
  - Feng Cheng
  - Yufan Cao
  - Feng Yan
  - Hai Li
  - Yiran Chen
  - Wei Wen

date: '2025-03-24T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2025-03-24T00:00:00Z'

# Publication type.
publication_types: ['article-journal']

# Publication name and optional abbreviated publication name.
publication: '*ACM Transactions on Recommender Systems*, 3(3), Article 41'
publication_short: '*ACM TORS*, 3(3)'

abstract: |
  The increasing popularity of deep learning models has created new opportunities for developing artificial intelligence–based recommender systems. Designing recommender systems using deep neural networks (DNNs) requires careful architecture design, and further optimization demands extensive co-design efforts on jointly optimizing model architecture and hardware. Design automation, such as Automated Machine Learning (AutoML), is necessary to fully exploit the potential of recommender model design, including model choices and model–hardware co-design strategies. We introduce a novel paradigm that utilizes weight sharing to explore abundant solution spaces. Our paradigm creates a large supernet to search for optimal architectures and co-design strategies to address the challenges of data multimodality and heterogeneity in the recommendation domain. From a model perspective, the supernet includes a variety of operators, dense connectivity, and dimension search options. From a co-design perspective, it encompasses versatile Processing-In-Memory (PIM) configurations to produce hardware-efficient models. Our solution space's scale, heterogeneity, and complexity pose several challenges, which we address by proposing various techniques for training and evaluating the supernet. Our crafted models show promising results on three Click-Through Rate (CTR) prediction benchmarks, outperforming both manually designed and AutoML-crafted models with state-of-the-art performance when focusing solely on architecture search. From a co-design perspective, we achieve 2× floating-point operations efficiency, 1.8× energy efficiency, and 1.5× performance improvements in recommender models.

# Summary. An optional shortened abstract.
summary: A weight-sharing supernet paradigm for joint architecture search and Processing-In-Memory hardware co-design of deep recommender models.

tags:
  - Recommender Systems
  - Neural Architecture Search
  - Automated Machine Learning
  - Deep Learning
  - AutoML for RecSys

# Display this page in the Featured widget?
featured: true
layout: redirect
redirect_url: "/publications/autorec/3706124.pdf"

# Standard identifiers for auto-linking
hugoblox:
  ids:
    doi: 10.1145/3706124
    arxiv: 2411.07569

# Custom links
links:
  - type: pdf
    url: "3706124.pdf"
  # - type: code
  #   url: https://github.com/yourusername/repo
  # - type: dataset
  #   url: ""
  # - type: slides
  #   url: ""
  # - type: video
  #   url: ""

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
projects: []

# Slides (optional).
slides: ""
---

