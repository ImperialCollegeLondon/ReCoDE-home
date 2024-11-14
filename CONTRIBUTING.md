# ReCoDE Home

Home to the ReCoDE project that is a collection of high-quality research computing and data science exemplars.

## About

ReCoDE is a Vice-Provost for Education [funded project](https://www.imperial.ac.uk/about/education/get-involved/funding-opportunities-for-learning-and-teaching-innovation/funded-projects-funding-opportunities-for-learning-and-teaching-innovation/) for Learning & Teaching Innovation.

## Mkdocs Material

This site is being powered by [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/).
The [documentation](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/) is
excellent and should provide a good starting point for contributing to these pages.

## Development

After cloning this repository, you can pull all the necessary dependencies into your environment
(preferably a virtual one) and serve the site locally at 127.0.0.1:8000 with these two commands:

```bash
pip install -r requirements.txt
mkdocs serve
```

## Continuous Delivery

When a commit is pushed to the repository, a [GitHub Action](.github/workflows/publish.yml) will
automatically deploy the site to the `gh-pages` branch, and a GitHub bot will publish the GitHub Pages.