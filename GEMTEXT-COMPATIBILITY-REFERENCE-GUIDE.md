# Gemtext Compatibility Reference Guide

This reference guide documents the compatibility of Markdown features with gemtext as an output format of this Hugo theme. It should be assumed that any Markdown features not documented below are unsupported.

The reference guide format is as follows:

```markdown
## <Feature Name>

<Markdown input> => <gemtext output>

Support level: <full, partial, or unsupported>

[Other relevant information]

[Examples]
```

## Nesting

```plaintext
nested element => unchanged
```

Support level: unsupported

Nesting support is not factored into other features' support levels.

## Escape Characters

```plaintext
literal backslash + character => unchanged
```

Support level: unsupported

Escape character support is not factored into other features' support levels.

## Paragraphs

```plaintext
paragraph => text line
```

Support level: full

E.g:

Markdown input:

```markdown
I will become a text line in the gemtext output.
```

Gemtext output:

```gemtext
I will become a text line in the gemtext output.
```

## Blockquotes

```plaintext
blockquote => quote line
```

Support level: full

E.g:

Markdown input:

```markdown
> I will become quote lines
> in the gemtext output.
```

Gemtext output:

```gemtext
> I will become quote lines
> in the gemtext output.
```

## Headings

```plaintext
heading => (flattened) heading
```

Support level: partial

Number signs, equal signs, and dashes can delimit headings. Markdown heading levels greater than level 3 are flattened to level 3 in the gemtext output. The use of heading levels greater than level 3 is strongly discouraged.

E.g:

Markdown input:

```markdown
===
I will become a level 1 heading in the gemtext output


---------
I will become a level 2 heading in the gemtext output


### I will become a level 3 heading in the gemtext output


#### I will become a level 3 heading in the gemtext output


##### I will become a level 3 heading in the gemtext output


###### I will become a level 3 heading in the gemtext output
```

Gemtext output:

```gemtext
# I will become a level 1 heading in the gemtext output


## I will become a level 2 heading in the gemtext output


### I will become a level 3 heading in the gemtext output


### I will become a level 3 heading in the gemtext output


### I will become a level 3 heading in the gemtext output


### I will become a level 3 heading in the gemtext output
```

## Emphasis (Italic)

```plaintext
emphasis (italic) => text with italic delimiters removed
```

Support level: partial

Asterisks delimiting italicized text are removed from the gemtext output. Using italics with other supported Markdown features can cause unexpected behavior.

E.g:

Markdown input:

```markdown
I will become *italicized* in the HTML output.

*##* I will become a level 2 heading in the gemtext output but not in the HTML output
```

Gemtext output:

```gemtext
I will become italicized in the HTML output.

## I will become a level 2 heading in the gemtext output but not in the HTML output
```

## Emphasis (Bold)

```plaintext
emphasis (bold) => text with bold delimiters removed
```

Support level: partial

Asterisks delimiting bolded text are removed from the gemtext output. Using bolding with other supported Markdown features can cause unexpected behavior.

E.g:

Markdown input:

```markdown
I will become **bolded** in the HTML output.

**##** I will become a level 2 heading in the gemtext output but not in the HTML output
```

Gemtext output:

```gemtext
I will become bolded in the HTML output.

## I will become a level 2 heading in the gemtext output but not in the HTML output
```

## Emphasis (Bold and Italic)

```plaintext
emphasis (bold and italic) => text with bold and italic delimiters removed
```

Support level: partial

Asterisks delimiting bolded and italicized text are removed from the gemtext output. Using bolding and italics with other supported Markdown features can cause unexpected behavior.

E.g:

Markdown input:

```markdown
I will become ***bolded and italicized*** in the HTML output.

***##*** I will become a level 2 heading in the gemtext output but not in the HTML output
```

Gemtext output:

```gemtext
I will become bolded and italicized in the HTML output.

## I will become a level 2 heading in the gemtext output but not in the HTML output
```

## Unordered Lists

```plaintext
unordered list item => unordered list item
```

Support level: full

Dashes \(\-\), asterisks \(\*\), and plus signs \(\+\) can delimit unordered list items.

E.g:

Markdown input:

```markdown
* I will become unordered list #1 item #1 in the gemtext output
* I will become unordered list #1 item #2 in the gemtext output

- I will become unordered list #2 item #1 in the gemtext output
- I will become unordered list #2 item #2 in the gemtext output

+ I will become unordered list #3 item #1 in the gemtext output
+ I will become unordered list #3 item #2 in the gemtext output
```

Gemtext output:

```markdown
* I will become unordered list #1 item #1 in the gemtext output
* I will become unordered list #1 item #2 in the gemtext output

* I will become unordered list #2 item #1 in the gemtext output
* I will become unordered list #2 item #2 in the gemtext output

* I will become unordered list #3 item #1 in the gemtext output
* I will become unordered list #3 item #2 in the gemtext output
```

## Ordered Lists

```plaintext
ordered list item => unordered list line
```

Support level: partial

Numbers can delimit unordered list lines.

E.g:

Markdown input:

```markdown
1. I will become an unordered list line in the gemtext output
2. I will also become an unordered list line in the gemtext output
```

Gemtext output:

```gemtext
* I will become an unordered list line in the gemtext output
* I will also become an unordered list line in the gemtext output
```

## Preformatted Text

```plaintext
preformatted text => preformatting toggle lines + preformatted text lines
```

Support level: partial

Only 3 consecutive backticks can delimit preformatted text. Text following the leading "```" on the same line is permitted.

E.g:

Markdown input:

````markdown
```markdown
[this link](https://example.com) will not be rendered in the HTML nor in the gemtext output.
```
````

Gemtext output:

````gemtext
```markdown
[this link](https://example.com) will not be rendered in the HTML nor in the gemtext output.
```
````

## Links

```plaintext
link => superscripted reference numbers + link lines
```

Support level: partial

Hypertext references must be URL-encoded. Angle bracketed URLs, Markdown reference-style links, and linking to heading IDs are unsupported.

If the "makerefs" variable in the frontmatter is set to true (the default), text enclosed in brackets \(e.g. \[Arch Linux\]\) immediately followed by a URL in parenthesis \(e.g. \(https://archlinux.org\)\) and an optional link title \("Arch Linux"\) becomes a reference-style link with a corresponding link line appended to the bottom of the page in the gemtext output. If there is a link title in the Markdown, it becomes the link name in the gemtext.

E.g:

Markdown input:

```markdown
[Debian](https://www.debian.org) is a good OS, but I prefer [arch](https://archlinux.org "Arch Linux").
```
 
Gemtext output:

```gemtext
Debian¹ is a good OS, but I prefer arch².


## References

=> https://www.debian.org 🔗 [1]: Debian
=> https://archlinux.org 🔗 [2]: Arch Linux
```

If the "makerefs" variable in the frontmatter is set to false, reference-style links are not created and only links that occupy the entire line become link lines in the gemtext output.

E.g:

Markdown input:

```markdown
---
<mandatory frontmatter>
makerefs: false
---
[Puppy Linux](https://puppylinux-woof-ce.github.io "a lightweight linux distro")
```

Gemtext output:

```gemtext
=> https://puppylinux-woof-ce.github.io Puppy Linux
```

## Inline Images

```plaintext
inline image => link line
```

Support level: partial

Links with a preceding exclamation mark are treated the same as normal links in the gemtext output.

E.g:

Markdown input:

```markdown
---
<mandatory frontmatter>
makerefs: false
---
Check out my dog:

![Spot](pics/dogs/spot.jpeg "A black, brown, and white hound running in the yard with his tongue out")
```

Gemtext output:

```gemtext
Check out my dog:

=> pics/dogs/spot.jpeg Spot
```

## Whitespace

```plaintext
whitespace => literal whitespace
```

Support level: partial

Whitespace in the Markdown input is copied verbatim into the gemtext output. For maximum compatibility, it is advised to use 2 literal newlines after each element except before headings. Headings require 3 preceding literal newlines except at the start of the document.

E.g:

Markdown input:

```markdown
I will become a text line


## I will become a level 2 heading

* I will become unordered list item #1
* I will become unordered list item #2

> I will become
> quote lines
```

Gemtext output:

```gemtext
I will become a text line


## I will become a level 2 heading

* I will become unordered list item #1
* I will become unordered list item #2

> I will become
> quote lines
```
