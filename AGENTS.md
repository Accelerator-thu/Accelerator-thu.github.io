# Repository Guidelines

## Project Structure & Module Organization

This is a static academic website built with Hugo and Hugo Blox. Main site content lives in `content/`: homepage blocks in `content/_index.md`, CV content in `content/experience.md`, blog posts in `content/blog/`, and publications in `content/publications/<paper-slug>/index.md`. Author profile data is in `data/authors/me.yaml`. Hugo configuration is split across `config/_default/`, including menus, theme parameters, language settings, and module imports. Custom template hooks and partials live in `layouts/`. Static files that should be copied directly, such as PDFs, belong in `static/`; processed media belongs in `assets/`.

## Build, Test, and Development Commands

- `hugo mod download`: fetch Hugo module dependencies.
- `pnpm install`: install Node dependencies such as Tailwind CSS and Pagefind.
- `pnpm run dev`: start the local Hugo server with fast render disabled at `http://localhost:1313`.
- `pnpm run build`: run `hugo --minify` and then generate the Pagefind search index under `public/`.
- `pnpm run pagefind`: rebuild only the search index from the existing `public/` output.

Use Hugo Extended; the expected version is documented in `CLAUDE.md`, `netlify.toml`, and `hugoblox.yaml`.

## Coding Style & Naming Conventions

Use Markdown with YAML frontmatter for content files. Keep frontmatter keys consistent with existing Hugo Blox examples. Use lowercase, hyphenated slugs for folders and URLs, for example `content/publications/genomic-modeling-2026/`. Prefer two-space indentation in YAML lists and nested fields. Keep custom HTML partials small and scoped to `layouts/`; avoid broad template changes when a content or config update is sufficient.

## Testing Guidelines

There is no separate unit test suite. Validate changes by running `pnpm run build` before submitting. For content edits, also run `pnpm run dev` and check the affected page locally. Publication additions should include a valid `index.md` and, when available, local assets such as `featured.png`, `paper.pdf`, and `cite.bib`. See `ADDING_PAPERS.md` for the publication schema.

## Commit & Pull Request Guidelines

Recent history uses short Conventional Commit-style messages, mainly `feat:` and `fix:`. Follow that pattern, for example `feat: add graph modeling publication` or `fix: adjust publication section spacing`. Pull requests should describe the visible site change, list affected pages or content folders, link any related issue, and include screenshots for layout or visual updates. Mention whether `pnpm run build` passed.

## Agent-Specific Instructions

Do not edit generated output in `public/` or cached files in `resources/` unless the task explicitly requires it. Make source changes in `content/`, `config/`, `data/`, `layouts/`, `assets/`, or `static/` instead.
