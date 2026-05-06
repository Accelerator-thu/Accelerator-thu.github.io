# Blog Writing Tutorial

This site publishes blog posts from `content/blog/`. Each post should live in its own folder with an `index.md` file and any local images or attachments beside it.

## 1. Create a Post Folder

Use a short, lowercase, hyphenated slug:

```bash
content/blog/my-research-note/index.md
```

The folder name becomes the URL path, for example `/blog/my-research-note/`.

## 2. Add Frontmatter

Start `index.md` with YAML frontmatter:

```yaml
---
title: "My Research Note"
subtitle: "Optional short subtitle"
summary: "One sentence shown in blog lists and previews."
date: 2026-05-05
draft: false

authors:
  - me

tags:
  - Machine Learning
  - Biology
---
```

Set `draft: true` while writing. Drafts are not shown on the live site because `buildDrafts: false` is set in `config/_default/hugo.yaml` and the normal build commands do not enable drafts.

## 3. Write the Body

Write the post below the frontmatter using Markdown:

```markdown
{{< toc mobile_only=true is_open=true >}}

## Main Idea

Introduce the argument or result.

## Details

Use paragraphs, lists, links, equations, and images as needed.
```

Keep headings descriptive and use sentence-style paragraphs. Put local images in the post folder and reference them with relative paths, such as `![Model overview](overview.png)`.

## 4. Preview Locally

Run:

```bash
pnpm run dev
```

Open `http://localhost:1313/blog/` and check the post page. To preview drafts locally only, run Hugo manually with drafts enabled:

```bash
hugo server --buildDrafts --disableFastRender
```

Do not use `--buildDrafts` for production builds.

## 5. Publish

When the post is ready, set `draft: false`, confirm the `date`, and run:

```bash
pnpm run build
```

Commit the new folder and any assets together.
