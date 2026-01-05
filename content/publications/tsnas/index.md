---
title: 'Farthest Greedy Path Sampling for Two-shot Recommender Search'

# Authors
authors:
  - Yufan Cao
  - Tunhou Zhang
  - Wei Wen
  - Feng Yan
  - Hai Li
  - Yiran Chen

date: '2023-10-31T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2023-10-31T00:00:00Z'

# Publication type.
publication_types: ['article']

# Publication name and optional abbreviated publication name.
publication: ''
publication_short: ''

abstract: |
  Weight-sharing Neural Architecture Search (WS-NAS) provides an efficient mechanism for developing end-to-end deep recommender models. However, in complex search spaces, distinguishing between superior and inferior architectures (or paths) is challenging. This challenge is compounded by the limited coverage of the supernet and the co-adaptation of subnet weights, which restricts the exploration and exploitation capabilities inherent to weight-sharing mechanisms. To address these challenges, we introduce Farthest Greedy Path Sampling (FGPS), a new path sampling strategy that balances path quality and diversity. FGPS enhances path diversity to facilitate more comprehensive supernet exploration, while emphasizing path quality to ensure the effective identification and utilization of promising architectures. By incorporating FGPS into a Two-shot NAS (TS-NAS) framework, we derive high-performance architectures. Evaluations on three Click-Through Rate (CTR) prediction benchmarks demonstrate that our approach consistently achieves superior results, outperforming both manually designed and most NAS-based models.

# Summary. An optional shortened abstract.
summary: We introduce Farthest Greedy Path Sampling (FGPS) for Two-shot Neural Architecture Search (TS-NAS) in recommender systems, achieving state-of-the-art performance on CTR prediction benchmarks.

tags:
  - Recommender Systems
  - Neural Architecture Search
  - Weight Sharing
  - Path Sampling
  - Deep Learning

featured: true

# Standard identifiers for auto-linking
hugoblox:
  ids:
    arxiv: 2310.20705v1

# Custom links
links:
  - type: preprint
    provider: arxiv
    id: 2310.20705v1
  - type: pdf
    url: "2310.20705v1.pdf"
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

