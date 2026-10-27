---
title: 'Learning Symbolic Models for Graph-Structured Physical Mechanism'

# Authors
authors:
  - Hongzhi Shi
  - Jingtao Ding
  - Yufan Cao
  - Quanming Yao
  - Li Liu
  - Yong Li

date: '2023-05-01T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2023-05-01T00:00:00Z'

# Publication type.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *The Eleventh International Conference on Learning Representations (ICLR 2023)*
publication_short: In *ICLR 2023*

abstract: |
  Graph-structured physical mechanisms are ubiquitous in real-world scenarios, thus revealing underneath formulas is of great importance for scientific discovery. However, classical symbolic regression methods fail on this task since they can only handle input-output pairs that are not graph-structured. In this paper, we propose a new approach that generalizes symbolic regression to graph-structured physical mechanisms. The essence of our method is to model the formula skeleton with a message-passing flow, which helps transform the discovery of the skeleton into the search for the message-passing flow. Such a transformation guarantees that we are able to search a message-passing flow, which is efficient and Pareto-optimal in terms of both accuracy and simplicity. Subsequently, the underneath formulas can be identified by interpreting component functions of the searched message-passing flow, reusing classical symbolic regression methods. We conduct extensive experiments on datasets from different physical domains, including mechanics, electricity, and thermology, and on real-world datasets of pedestrian dynamics without ground-truth formulas. The experimental results not only verify the rationale of our design but also demonstrate that the proposed method can automatically learn precise and interpretable formulas for graph-structured physical mechanisms.

# Summary. An optional shortened abstract.
summary: Generalizes symbolic regression to graph-structured physical mechanisms by modeling the formula skeleton as a searchable message-passing flow.

tags:
  - Symbolic Regression
  - Graph Neural Networks
  - Physics-Informed Learning
  - Machine Learning
  - AI for Physics

# Display this page in the Featured widget?
featured: true
layout: redirect
redirect_url: "/publications/graphsr/1071_learning_symbolic_models_for_g.pdf"

# Standard identifiers for auto-linking
hugoblox:
  ids:
    # OpenReview: f2wN4v_2__W (linked below with an explicit label)

# Custom links
links:
  - type: pdf
    url: "1071_learning_symbolic_models_for_g.pdf"
  - type: preprint
    label: OpenReview
    url: https://openreview.net/forum?id=f2wN4v_2__W
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

