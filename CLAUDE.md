# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal academic website for Yufan Cao (Ph.D. student in EECS at UC Berkeley), built with Hugo + HugoBlox Academic CV template. Deployed to GitHub Pages via GitHub Actions.

## Commands

```bash
# Install dependencies
hugo mod download       # Hugo modules
pnpm install            # Node dependencies (Tailwind, Pagefind, Preact)

# Development
pnpm run dev            # hugo server --disableFastRender → http://localhost:1313

# Production build
pnpm run build          # hugo --minify && pagefind --site public

# Search index only
pnpm run pagefind       # Regenerate static search index from public/
```

Hugo Extended v0.154.2 is required (specified in netlify.toml and hugoblox.yaml).

## Architecture

Content is authored in Markdown with YAML frontmatter, rendered by Hugo using HugoBlox block components. No custom backend — purely static.

### Content layer (`content/`)
Pages use HugoBlox "blocks" declared in frontmatter. Key pages:
- `content/_index.md` — Homepage (biography, research interests, publications blocks)
- `content/experience.md` — CV page (experience, awards, languages blocks)
- `content/misc.md` — Miscellaneous projects
- `content/publications/*/index.md` — Individual paper pages (see `ADDING_PAPERS.md` for the full schema)

### Data layer (`data/authors/me.yaml`)
Structured YAML containing education, work experience, awards, skills, social links, and ORCID/Google Scholar IDs. CV blocks reference this file directly.

### Configuration (`config/_default/`)
| File | Purpose |
|------|---------|
| `hugo.yaml` | Core Hugo settings, markdown rendering, taxonomies |
| `params.yaml` | Site identity, theme colors (#003262 Berkeley blue, #6FA3A8), typography |
| `module.yaml` | HugoBlox module imports and asset mount points |
| `menus.yaml` | Top navigation (Bio, Papers, Experience, Misc) |

### Custom templates (`layouts/`)
- `layouts/_partials/hooks/` — Injected into page lifecycle (e.g., ClustrMaps globe, GitHub CV button)

### Asset pipeline
Tailwind CSS v4 processes styles; Pagefind indexes the built `public/` directory for client-side search.

## Adding Publications

See `ADDING_PAPERS.md` for the complete guide. Each paper lives in its own folder under `content/publications/` with an `index.md` file. Publication type is set via the `publication_types` frontmatter field (numeric codes map to preprint, journal, conference, etc.).
