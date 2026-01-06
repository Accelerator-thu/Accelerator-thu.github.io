# Yufan Cao - Personal Academic Website

This repository contains the source code for my personal academic website, hosted at [accelerator-thu.github.io](https://accelerator-thu.github.io).

## About

I'm a Ph.D. student in EECS at UC Berkeley (BAIR), working on computational biology, genomic sequence modeling, and ML-based generative & evolutionary models. This website showcases my research, publications, and academic activities.

## Website

🌐 **Live Site**: [https://accelerator-thu.github.io](https://accelerator-thu.github.io)

## Local Development

To run this site locally:

1. **Install Hugo** (Extended version):
   ```bash
   # macOS
   brew install hugo
   
   # Or download from https://gohugo.io/installation/
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Accelerator-thu/Accelerator-thu.github.io.git
   cd Accelerator-thu.github.io
   ```

3. **Install dependencies**:
   ```bash
   hugo mod download
   ```

4. **Run the development server**:
   ```bash
   hugo server
   ```

5. **View the site**: Open [http://localhost:1313](http://localhost:1313) in your browser

## Project Structure

- `content/` - Website content (publications, blog posts, etc.)
- `data/authors/` - Author profile information
- `config/` - Hugo configuration files
- `static/` - Static assets (images, PDFs, etc.)
- `assets/` - Processed assets (media files)

## Building

To build the site for production:

```bash
hugo --minify
```

The generated site will be in the `public/` directory.

## Deployment

This site is automatically deployed to GitHub Pages via GitHub Actions. Simply push changes to the `main` branch and the site will rebuild automatically.

## Credits

This website is built using [HugoBlox](https://hugoblox.com/) and the Academic CV template.

## License

Content on this website is © Yufan Cao. All rights reserved.

---

**Contact**: [yufan.cao@berkeley.edu](mailto:yufan.cao@berkeley.edu) | [Website](https://accelerator-thu.github.io)
