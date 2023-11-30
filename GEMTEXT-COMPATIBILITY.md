# Gemtext Compatibility

Gemtext output format support for Hugo is a hack. Since Hugo's theme API does not expose the Markdown parser, the Markdown is rendered into gemtext using regex. The lack of a proper Markdown parser coupled with the limitations of the [Gemini protocol](https://gemini.circumlunar.space/docs/specification.gmi)'s document format gemtext means only a limited subset of Markdown can be converted to gemtext. That subset is documented below. Any Markdown features not explicitly mentioned below should be assumed incompatible.

## Paragraphs

Markdown paragraphs are supported.

Explanation:

Markdown paragraphs map directly onto gemtext text lines. They are left unmodified.

## Blockquotes

Blockquotes are partially supported.

Explanation:

Markdown blockquotes map onto gemtext quote lines. Gemtext only supports flat (non-nested) quote lines that do not contain other elements like lists or headings. For compatibility, use only flat blockquotes containing no other elements.

E.g:

```markdown
> I am a multi-line
> quote for demo purposes.
> I do not contain any
> other elements.
```

## Headings

Markdown headings are partially supported.

Explanation:

Markdown supports 6 headings while gemtext only supports 3. Markdown headings 1-3 \(\#, \#\#, \#\#\#\) map to their respective gemtext heading. Markdown headings 4-6 \(\#\#\#\#, \#\#\#\#\#, \#\#\#\#\#\#\) map to the level 3 \(\#\#\#\) gemtext heading. This flattening is also reflected in the HTML through the CSS styling.

Alternate syntax for Markdown headings including == and -- is not supported. Only number signs \(\#\) may be used.

The goldmark Markdown renderer requires whitespace between the number signs and the heading name whereas the gemtext specification does not. For compatibility, do not use Markdown headings 4-6 and always put a space after the number signs.

## Whitespace

Newlines are partially supported. Line breaks are unsupported.

Explanation:

The gemtext renderer and HTML renderer handle whitespace differently. While whitespace has special meaning in Markdown, the gemtext renderer simply copies it unmodified into the output. It is possible to achieve consecutive newlines in the HTML, but the gemtext won't render it correctly. For compatibility, use two literal newlines after each new element except before headings. Headings must be preceded by three literal newlines.

E.g:

````markdown
I am a paragraph.

* unordered list item 1
* unordered list item 2

1. ordered list item 1
2. ordered list item 2


## I am a Heading

```
I am preformatted text.
```

> I am
> a quote
````

## Emphasis

Bold and italics are partially supported.

Explanation:

Since gemtext does not support bold nor italics, bold and italic text in Markdown map onto gemtext text lines with the asterisks removed. The gemtext renderer only understands asterisks as representing bold or italics, not underscores. For compatibility, use asterisks and write text that doesn't strictly depend on the display of the bold or italics.

E.g:

Markdown input:

```markdown
*I am italic text!*
**I am bold text!**
***I am bold and italic text!***

_I am italic text!_
__I am bold text!__
___I am bold and italic text!___
```

Gemtext output:

```gemtext
I am italic text!
I am bold text!
I am bold and italic text!

_I am italic text!_
__I am bold text!__
___I am bold and italic text!___
```

## Lists

Unordered lists are partially supported. Ordered lists are unsupported.

Explanation:

Since gemtext does not support ordered lists, ordered lists in Markdown map onto text lines in Gemini.

Unordered list items in Markdown map onto unordered list items in gemtext. Gemtext does not support adding elements in lists nor nested lists. Dashes \(\-\), asterisks \(\*\), and plus signs \(\+\) can all be used to represent line items. For compatibility, use only flat lists containing no other elements.

E.g:

```
* this is
* a list

- this is
- a list

+ this is
+ a list
```

## Preformatted Text

Preformatted text is partially supported.

Explanation:

Preformatted text in Markdown maps to preformatting toggle lines and preformatted text lines in gemtext. Gemtext only supports using 3 backticks to represent preformatting toggle lines. For best compatibility, always use exactly 3 backticks.

E.g:

````
```plaintext
I love Gemini!
```
````

## Links

Links are partially supported.

Explanation:

Links in Markdown map to link lines in gemtext. The gemtext renderer does not recognize angle bracketed URLs nor reference-style links. It only recognizes links that have link text enclosed in brackets \(e.g. \[Arch Linux\]\), immediately followed by the URL in parenthesis \(e.g. \(archlinux.org\)\).

```markdown
[Arch Linux](https://archlinux.org)
```

Gemtext does not support inline links. To circumvent this limitation, the default behavior is to create link references and append them to the bottom of the page.

E.g:

Markdown input:

```markdown
Do you like the [Arch Linux](https://archlinux.org) distro?

What about the [Gentoo](https://www.gentoo.org/) distro?
```

Gemtext output:

```gemtext
Do you like the Arch Linux¹ distro?

What about the Gentoo² distro?


=> https://archlinux.org 🔗 1: Arch Linux 
=> https://www.gentoo.org 🔗 2: Gentoo
```

To disable the link references at the bottom, set "makerefs" to false in the frontmatter. This changes the behavior of the gemtext renderer so that it only renders non-inline Markdown links.

E.g:

Markdown input with "makerefs" set to false:

```markdown
[Arch Linux](https://archlinux.org)

any text before [Arch Linux](https://archlinux.org) or after
```

Gemtext output:

```gemtext
=> https://archlinux.org 🔗 Arch Linux

any text before [Arch Linux](https://archlinux.org) or after
```

Inline images in Markdown can be added by putting an exclamation mark immediately before the link brackets. Gemtext does not support inline images, so they are rendered as normal links. They only show up inline in the HTML.

E.g:

Markdown input:

```markdown
![Cute cat photo](cat.png)
```

Gemtext output:

```gemtext
Cute cat photo¹


=> cat.png 🔗 1: Cute cat photo
```

If a Markdown link has a title and the "makerefs" variable is set to true (the default), the link reference at the bottom of the page uses the link title instead of the link text.

E.g:

Markdown input:

```markdown
Do you like the [Arch Linux](https://archlinux.org "Arch") distro?
```

Gemtext output:

```gemtext
Do you like the Arch Linux¹ distro?


=> https://archlinux.org 🔗 1: Arch
```

For compatibility, only use links with brackets and parenthesis. Always URL encode links. Do not use inline links with the "makerefs" page variable disabled.
