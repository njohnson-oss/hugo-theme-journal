# Journal Theme For Hugo

Hugo Journal Theme is an accessible, no-JS, minimalist, high-contrast Hugo theme that outputs Gemtext and HTML. It's suitable for blogs.

## Features

* Outputs Gemtext for the [Gemini protocol](https://gemini.circumlunar.space/docs/specification.gmi)
* Multilingual support
* Audio versions of entries
* Works well on all screen sizes
* No bloated Javascript
* Absolutely no analytics

## Supported Languages

* English
* Spanish

## Documentation

The [gemtext compatibility reference guide](GEMTEXT-COMPATIBILITY-REFERENCE-GUIDE.md) documents the compatibility of Markdown features with gemtext as an output format of this Hugo theme. The [gemtext compatibility explanation document](GEMTEXT-COMPATIBILITY-EXPLANATION.md) explains the rationale behind the design decisions for the gemtext output format.

## Get The Theme

This theme requires Hugo 0.146.0 or later.

Run from the root of your Hugo site:

```sh
$ git clone <repository-url> themes/journal
```

Alternatively, if your Hugo site is version controlled, clone this theme as a git submodule:

```sh
$ git submodule add <repository-url> themes/journal
```

## Configure The Site

The [example site](exampleSite) is a working site with both configuration files annotated. Copy them as a starting point. The settings below are the ones the theme itself reads.

### Required

| Setting | Purpose |
| --- | --- |
| `title` | Site title. Used in page titles and as the feed title. |
| `params.author` | Feed author, as a string or a table with `name` and `email`. |
| `params.indexTitle` | Heading of the homepage. |
| `params.indexIntro` | Opening paragraph of the homepage. |
| `outputs` | Output formats per page kind. See below. |

Every page kind that the site renders must list its output formats, because Hugo's defaults include formats this theme has no templates for. For the website:

```toml
[outputs]
  home = ["HTML", "Atom"]
  section = ["HTML"]
  taxonomy = ["HTML", "Atom"]
  term = ["HTML", "Atom"]
  page = ["HTML"]
```

And for the capsule:

```toml
[outputs]
  home = ["Gemini", "Gemini_Atom"]
  section = ["Gemini"]
  taxonomy = ["Gemini", "Gemini_Atom"]
  term = ["Gemini", "Gemini_Atom"]
  page = ["Gemini"]
```

### Optional

| Setting | Default | Purpose |
| --- | --- | --- |
| `copyright` | none | Footer text and feed rights. `{currentYear}` is replaced with the build year. |
| `params.description` | none | Description meta element and feed subtitle. |
| `params.keywords` | none | Keywords meta element. |
| `params.dateFormat` | `:date_long` | Any layout `time.Format` accepts. |
| `params.custom_css` | theme stylesheet | List of stylesheets, resolved from `assets`. Replaces the theme's own. |
| `taxonomies` | none | Define `tag = "tags"` to use tags. |
| `services.rss.limit` | unlimited | Maximum entries per feed. |
| `menu.main` | none | Navigation links listed on the homepage. |

Two site files are optional. `templates/logo.txt` is rendered as preformatted text at the top of every page; without it no logo is shown. `static/favicon.ico` is picked up by browsers as the icon if present; when it is absent the theme links an empty icon so that browsers do not request one.

### Front Matter

| Key | Default | Purpose |
| --- | --- | --- |
| `pageinfo` | `true` | Show the date, reading time, tags and audio marker. |
| `makerefs` | `true` | Collect links into a reference section at the foot of the gemtext, rather than rendering them in place. |
| `showlinkemoji` | `true` | Prefix gemtext link lines with a link emoji. Only applies when `makerefs` is false. |
| `tags` | none | Tags for the entry. |

Entries live in the `entry` section. Pages elsewhere are treated as standalone pages and are kept out of the homepage entry list and its feed, though they still appear on the pages and feeds of any tag they carry.

### Audio Versions

Make the entry a page bundle and place the audio beside it:

```plaintext
content/entry/my-entry/
├── index.md
└── my-entry.opus
```

The website renders an audio player and the capsule a download link. More than one encoding may be supplied, in which case browsers choose the format they support and the capsule only links the most preferred one.

## Generate The Site

To render the blog for Gemini and the Web, use separate configuration files, since the two differ in their base URL and output formats. For guidance, look at the [example site](exampleSite).

```sh
$ hugo --config hugo.toml --destination public/web
$ hugo --config hugo.gemini.toml --destination public/gemini
```

To build the example site from a checkout of this theme:

```sh
$ hugo --source exampleSite --themesDir ../.. --theme "$(basename "${PWD}")"
```

## License

Hugo Journal Theme is licensed under [GPLv3 or later](LICENSE).
