---
title: 'Misc'
date: 2025-02-22
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    id: toys
    content:
      title: '🧩 Toy Projects'
      subtitle: ''
      text: |
        {{< misc-cards group="toys" title="Browser games" >}}
    design:
      columns: '1'
      spacing:
        padding: ['4rem', '0', '1rem', '0']
  # - block: markdown
  #   content:
  #     title: "Things I've Driven"
  #     subtitle: ''
  #     text: |
  #       - **[Open gallery](/driven/)** — Cars, carts, robots, and one very persuasive U-Haul.
  #   design:
  #     columns: '1'
  - block: markdown
    id: gallery
    content:
      title: '📷 Gallery'
      subtitle: ''
      text: |
        {{< misc-cards group="gallery" title="Albums" >}}
    design:
      columns: '1'
      spacing:
        padding: ['1rem', '0', '2rem', '0']
---
