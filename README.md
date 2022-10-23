# hugo-theme-journal
An accessible, no-JS, minimalist, high-contrast Hugo theme that outputs Gemtext and HTML. Suitable for blogs.

## Clone to Your Theme Directory
```bash
$ git clone <repository-url> themes/hugo-theme-journal
```

## Generate The Blog
Since Hugo can't separate the Gemtext and HTML output by itself, this theme uses two scripts to handle the output:

* `python3 themes/hugo-theme-journal/scripts/generate.py` outputs the site and the capsule
* `python3 themes/hugo-theme-journal/scripts/clean.py` removes previously generated output

If the correct media types, output formats, markup settings, and outputs are not specified in config.toml, the above scripts may fail or the blog may render correctly.

## License
GPLv3 or later
