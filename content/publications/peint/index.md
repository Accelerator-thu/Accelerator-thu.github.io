---
title: 'Deep Models of Protein Evolution in Time Generate Realistic Evolutionary Trajectories and Functional Proteins'

# Authors
authors:
  - Antoine Koehl
  - Sebastian Prillo
  - Yufan Cao
  - Matthew Liu
  - Junhao Xiong
  - Lillian Weng
  - David F. Savage
  - Yun S. Song

date: '2026-02-20T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2026-02-20T00:00:00Z'

# Publication type.
publication_types: ['article']

# Publication name and optional abbreviated publication name.
publication: '*bioRxiv*'
publication_short: '*bioRxiv*'

abstract: |
  Models of protein evolution are foundational to biology, underpinning essential techniques such as phylogenetic tree inference, ancestral sequence reconstruction, multiple sequence alignment, variant effect prediction, and protein design. Historically, for computational tractability, these models have relied on the simplifying - but biologically unrealistic - assumption that sites in a given protein evolve independently of each other. A crucial test of any evolutionary model is its ability to simulate realistic evolutionary trajectories, but the independent-sites assumption leads to simulations that poorly reflect the complexity of natural protein evolution. Here we introduce PEINT (Protein Evolution IN Time), a flexible and generalizable deep learning framework for modeling how the entire protein sequence evolves over time while incorporating complex interactions between sites. This framework enables learning realistic patterns of constrained evolutionary transitions directly from millions of protein sequences spanning diverse fold families. Furthermore, unlike classical models that require pre-aligned sequences, PEINT learns indel dynamics directly from raw, unaligned sequences, thereby eliminating potential biases from alignment errors that can lead to incorrect inference of evolutionary patterns. By capturing higher-order epistatic interactions and modeling insertion-deletion processes that classical models typically ignore, PEINT accurately reproduces key signatures of natural evolution, including conservation patterns and family-specific dynamics. When simulating evolution along phylogenetic trees, PEINT generates highly novel sequences that preserve protein function, which we validate through experimental characterization of simulated carbonic anhydrase variants that retain enzymatic activity. PEINT thus enables realistic simulation of protein evolution that explores new sequence space while respecting structural and functional constraints. This evolution-informed generative modeling framework offers a powerful new tool for advancing both phylogenetic inference and protein engineering.

# Summary. An optional shortened abstract.
summary: PEINT, a deep model of whole-sequence protein evolution over time that captures epistasis and indels, generates realistic trajectories and functional proteins.

tags:
  - Protein Evolution
  - Generative Models
  - Phylogenetics
  - Protein Language Models
  - Evolution & Sequence Modeling

featured: true
layout: redirect
redirect_url: "https://www.biorxiv.org/content/10.64898/2026.02.19.706898v1"

hugoblox:
  ids:
    doi: 10.64898/2026.02.19.706898

links:
  - type: preprint
    url: "https://www.biorxiv.org/content/10.64898/2026.02.19.706898v1"
  - type: dataset
    url: "https://zenodo.org/records/23315010"

image:
  caption: ''
  focal_point: ''
  preview_only: false

projects: []
slides: ""
---
