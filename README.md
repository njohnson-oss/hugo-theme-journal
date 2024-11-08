# Journal Theme For Hugo

Hugo Journal Theme is an accessible, no-JS, minimalist, high-contrast Hugo theme that outputs Gemtext and HTML. It's suitable for blogs.

## Features

* Outputs Gemtext for the [Gemini protocol](https://gemini.circumlunar.space/docs/specification.gmi)
* Multilingual support
* Works well on all screen sizes
* No bloated Javascript
* Absolutely no analytics

## Supported Languages

* English
* Spanish

## Documentation

The [gemtext compatibility reference guide](GEMTEXT-COMPATIBILITY-REFERENCE-GUIDE.md) documents the compatibility of Markdown features with gemtext as an output format of this Hugo theme. The [gemtext compatibility rationale document](GEMTEXT-COMPATIBILITY-RATIONALE.md) explains the rationale behind the design decisions for the gemtext output format.

## Get The Theme

Run from the root of your Hugo site:

```sh
$ git clone <repository-url> themes/journal
```

Alternatively, if your Hugo site is version controlled, clone this theme as a git submodule:

```sh
$ git submodule add <repository-url> themes/journal
```

## Generate The Site

To render the blog for Gemini and the Web, use separate configuration files.

## Versioning

This Hugo theme uses [Semantic Versioning 2.0.0](https://semver.org/).

## License

Hugo Journal Theme is licensed under [GPLv3 or later](LICENSE).
