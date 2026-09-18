---
title: "Writing Entries"
date: 2026-02-20T14:30:00+0000
draft: false
tags: ["journal"]
---

Create an entry with the "entry" archetype:

```sh
hugo new --kind entry entry/my-first-entry.md
```

Entries are Markdown. Headings, lists, blockquotes and preformatted
blocks all survive into gemtext:

> Gemtext has no nesting and no inline emphasis, so the theme flattens
> what it can and drops the rest.

Emphasis is a good example. *Italics* and **bold** are rendered on the
web, and their asterisks are removed from the gemtext, so write in a way
that still reads without them.

## Adding An Audio Version

Make the entry a page bundle and put the audio file beside it:

```plaintext
content/entry/my-first-entry/
├── index.md
└── my-first-entry.opus
```

The website gets an audio player and the capsule gets a download link.
Include more than one encoding and browsers pick the format they
support, while the capsule only links the most preferred one.
