# How to Add Your Papers to the Website

## Quick Steps

1. **Create a new folder** in `content/publications/` with a short name (e.g., `my-paper-2024`)
2. **Create an `index.md` file** in that folder with your paper's metadata
3. **Add optional files**:
   - `featured.jpg` or `featured.png` - thumbnail image
   - `paper.pdf` - PDF of your paper
   - `cite.bib` - BibTeX citation

## Folder Structure

```
content/publications/
  └── my-paper-2024/
      ├── index.md          (required)
      ├── featured.jpg       (optional)
      ├── paper.pdf          (optional)
      └── cite.bib           (optional)
```

## Publication Types

Choose the appropriate `publication_types`:
- `["article-journal"]` - Journal articles
- `["paper-conference"]` - Conference papers
- `["article"]` - Preprints, working papers
- `["paper"]` - Other papers

## Example Template

Copy this template and fill in your details:

```yaml
---
title: "Your Paper Title"

# Authors (use 'me' for yourself, or add other authors)
authors:
  - me
  - "Coauthor Name"

# Author notes (optional)
author_notes:
  - "Equal contribution"

# Publication date (ISO format)
date: "2024-01-15T00:00:00Z"

# When to publish on website (can be future date)
publishDate: "2024-01-15T00:00:00Z"

# Publication type
publication_types: ["article-journal"]  # or ["paper-conference"], ["article"], etc.

# Publication venue
publication: "In *Journal Name*"
publication_short: "In *J. Name*"

# Abstract
abstract: |
  Your full abstract goes here. It can span multiple lines.

# Short summary (optional)
summary: A brief one-line summary.

# Tags
tags:
  - Machine Learning
  - Biology

# Display on homepage? (true/false)
featured: true

# Identifiers (optional)
hugoblox:
  ids:
    doi: 10.1234/example
    arxiv: 2401.12345
    pubmed: 12345678

# Links
links:
  - type: pdf
    url: "paper.pdf"  # Relative to folder, or full URL
  - type: code
    url: https://github.com/yourusername/repo
  - type: dataset
    url: https://example.com/dataset
  - type: slides
    url: https://example.com/slides
  - type: video
    url: https://youtube.com/watch?v=...

# Featured image (optional)
# Add featured.jpg/png to the folder
image:
  caption: 'Image credit: [**Your Name**](https://example.com)'
  focal_point: "Center"
  preview_only: false

# Associated projects (optional)
projects: []

# Associated slides (optional)
slides: ""
---

Add any additional content, notes, or supplementary material here using Markdown.
```

## Key Fields Explained

- **`title`**: Full paper title
- **`authors`**: List of author usernames (use `me` for yourself) or full names
- **`date`**: Publication date (when it was published)
- **`publishDate`**: When to show on website (can be future)
- **`publication_types`**: Type of publication (see above)
- **`publication`**: Full venue name
- **`abstract`**: Full abstract
- **`featured`**: `true` to show on homepage, `false` otherwise
- **`links`**: Various links (PDF, code, etc.)

## Tips

1. **Folder naming**: Use lowercase, hyphens, and be descriptive (e.g., `genomic-modeling-2024`)
2. **PDF files**: Place PDF in the same folder and reference as `"paper.pdf"` or use full URL
3. **Featured image**: Add `featured.jpg` or `featured.png` to the folder (recommended size: 1200x600px)
4. **BibTeX**: Create `cite.bib` file for citation export feature
5. **Ordering**: Publications are sorted by date (most recent first)

## Where Papers Appear

- **Homepage**: Papers with `featured: true` appear in the "Publications" section
- **Publications page**: All papers appear at `/publications/`
- **Individual pages**: Each paper has its own page at `/publications/your-paper-name/`

