# Gemtext Compatibility Explanation Document

This explanation document details the rationale behind the design decisions for the gemtext output format. Its structure mirrors that of the [gemtext compatibility reference guide](GEMTEXT-COMPATIBILITY-REFERENCE-GUIDE.md).

The explanation document format is as follows:

````markdown
## <Feature Name>

<Rationale>
````

## Nesting

Gemtext does not support nesting elements, so it is impossible for the gemtext output format to fully support nesting.

The gemtext renderer may be able to flatten nested elements to allow other output formats to use nested elements without harming the gemtext output format, but adding even partial support for it would probably make the regex unmaintainable and lose too much semantic meaning anyway.

## Escape Characters

Gemtext does not support escape characters, so it is impossible for the gemtext output format to fully support escape characters.

The gemtext renderer may be able to remove backslashes to allow other output formats to use escape characters without harming the gemtext output format, but adding even partial support for it would probably make the regex unmaintainable and invoke so many corner cases that much of the documentation would need to be devoted just to escape characters.

## Paragraphs

Markdown paragraphs are the same as gemtext text lines.

## Blockquotes

Markdown blockquotes are the same as gemtext quote lines.

## Headings

Markdown headings delimited with number signs are the same as gemtext headings, except that gemtext does not support heading levels 4-6. Markdown heading levels 4-6 are flattened to heading level 3 in the gemtext output format. Flattening Markdown heading levels 4-6 results in a significant loss of semantic meaning, so using those levels is strongly discouraged. Flattening Markdown headings is supported because it does not lose as much semantic meaning as flattening element nesting would and, unlike element nesting, implementing it does not overcomplicate the regex.

Alternate Markdown syntax for delimiting headings (equal signs and dashes) is supported since implementing it does not overcomplicate the regex.

## Emphasis (Italics and/or Bolding)

Gemtext does not support italicized and/or bolded text, so it is impossible for the gemtext output format to fully support italicized and/or bolded text.

In order to allow other output formats to use italic and/or bold syntax without harming the gemtext output format, asterisks delimiting italicized and/or bolded text are removed from the gemtext output. Loss of significant semantic meaning can be avoided by using italics and/or bolding in such a way that the text remains comprehensible even with the italics and/or bolding removed.

## Unordered Lists

Markdown unordered list items delimited with asterisks are the same as gemtext unordered list items.

Alternate Markdown syntax for delimiting unordered list items (dashes and plus signs) is supported since implementing it does not overcomplicate the regex.

## Ordered Lists

Gemtext does not support ordered lists, so it is impossible for the gemtext output format to fully support ordered lists.

In order to allow other output formats to use ordered list syntax without harming the gemtext output format and in order to make ordered lists useful in the gemtext output format, ordered list items are converted to unordered list items in the gemtext output. This is supported since implementing it does not overcomplicate the regex. Loss of significant semantic meaning can be avoided by using ordered lists in such a way that the list remains comprehensible even with the ordering removed.

## Preformatted Text

Markdown preformatted text delimited with 3 backticks is the same as gemtext preformatted text.

Gemtext does not support preformatted text delimited with more than 3 backticks. This is not supported because it is not possible in the regex. This is not considered a deficiency since preformatted text with more than 3 backticks is only used for nesting or escaping, features that have already been documented as unsupported.

Alternate Markdown syntax for delimiting preformatted text (4+ spaces or a tab) is unsupported because the regex for supporting it has not been implemented.

## Links

Gemtext does not support inline links, so it is impossible for the gemtext output format to fully support inline links.

In order to allow other output formats to use inline link syntax without harming the gemtext output format and in order to make inline links useful in the gemtext output format, all links are optionally converted to reference-style links in the gemtext output. The conversion is optional because reference-style links may not be appropriate on all pages.

Only basic link syntax is supported: brackets containing link text followed by parenthesis containing a URL optionally followed by quotes containing a link title. Alternate link syntax is unsupported because it has not been implemented.

## Inline Images

Gemtext does not support inline images, so it is impossible for the gemtext output format to fully support inline images.

In order to allow other output formats to use inline image syntax without harming the gemtext output format and in order to make inline images useful in the gemtext output format, inline images are treated the same as regular links.

## Whitespace

Whitespace has no special meaning in gemtext. Gemini clients simply display whitespace verbatim. This can lead to discrepancies between the gemtext output format and other output formats if the guidelines in the [gemtext compatibility reference guide](GEMTEXT-COMPATIBILITY-REFERENCE-GUIDE.md) are not followed.

The gemtext renderer can "autocorrect" whitespace to avoid the need to manually format it. This feature was implemented, but later scrapped since it made the regex unmaintainable and introduced too many new edge cases.
