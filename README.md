# yoheiohto.github.io

Source of the personal website of Yohei Ohto (大戸陽平), published at <https://yoheiohto.github.io>.

The site is built with [Jekyll](https://jekyllrb.com/) on GitHub Pages, based on the [Academic Pages](https://academicpages.github.io/) template.

## Where to edit

See [HOW_TO_EDIT.md](HOW_TO_EDIT.md) for the files to change when adding publications, talks, and other content.

## Local preview

Use Ruby 3.2. The macOS system Ruby (2.6) is too old, and Ruby 4 cannot install the gems pinned by `github-pages`.

```bash
brew install ruby@3.2
export PATH="/opt/homebrew/opt/ruby@3.2/bin:$PATH"
bundle install
bundle exec jekyll serve -l -H localhost
# Open http://localhost:4000
```

With Docker, run `docker compose up` instead.

## License

The template code is released under the MIT License (see [LICENSE](LICENSE)). The site content belongs to Yohei Ohto.
