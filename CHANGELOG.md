# Changelog

## 2025.09.07 - 2025-09-07

### Fixed

- Fix link in README

## 2025.07.27.2 - 2025-07-27

### Changed

- Make content area's background color always fill viewport height
- Make footer always stick to bottom of page

## 2025.07.27.1 - 2025-07-27

### Changed

- Add gray background to website

## 2025.07.27 - 2025-07-27

### Changed

- Change minimum supported Hugo version to 0.146.0
- Migrate to new template system in Hugo v0.146.0

### Fixed

- Fix rendering of term pages

## 2025.07.24.1 - 2025-07-24

### Changed

- Switch from semantic versioning to calendar versioning

### Added

- Support Hugo versions 0.146.0 and later

## 2025.07.24 - 2025-07-24

### Changed

- Utilize front matter key "build", retain compatibility with deprecated key "_build"

### Added

- Document maximum supported Hugo version in README.md

## 2025.02.06.1 - 2025-02-06

### Changed

* Add non-breaking spaces within entry tag names

## 2025.02.06 - 2025-02-06

### Changed

* Add non-breaking spaces after emojis and within entry dates and read times
* Remove commas from entry tag list in html output format

### Fixed

* Move taxonomy and term feeds' link emojis to outside link text in html output format

## 2025.02.05 - 2025-02-05

### Fixed

- Add missing hyphen to compound modifier in pageinfo partial for English translation

## 2025.01.28 - 2025-01-28

### Added

- Add Gemini capsule demo URL to README.md

## 2024.11.25 - 2024-11-25

### Changed

- Move css stylesheet to subdirectory

## 2024.11.23 - 2024-11-23

### Changed

- Improve conversion of ref numbers to superscripts

## 2024.11.08.1 - 2024-11-08

### Fixed

- Fix typo in README.md

## 2024.11.08 - 2024-11-08

### Changed

- Make hover/non-hover link colors equivalent
- Improve code readability

### Added

- Add distinct CSS styling to external links

### Fixed

- Disable html renderer in gemtext output format
- Disable html-specific features in gemtext output format
- Stop treating link titles as safe html

## 2024.11.07 - 2024-11-07

### Changed

- Transition to new config file naming convention
- Convert tabs to spaces

### Added

- Add time element to entry date and duration in HTML output format

### Removed

- Remove niche timestamp obfuscation privacy feature

## 2024.08.16 - 2024-08-16

### Changed

- Make author element optional in Atom feeds
- Make email subelement optional in author element

### Added

- Add support for site.Params.author, retain compatibility with site.Author

### Fixed

- Remove erroneous "index.gmi" suffix in gemtext Atom feeds
- Fix incorrect greedy italics/bold parsing in gemtext renderer

## 2024.07.04 - 2024-07-04

### Fixed

- Remove extra whitespace accidentally introduced in v1.3.5

## 2024.06.30 - 2024-06-30

### Added

- Add this changelog

### Fixed

- Fix incorrect file path truncation in gemtext renderer

## 2024.06.28 - 2024-06-28

### Fixed

- Add back missing `rel="noreferrer"` attribute to relative links for privacy

## 2024.06.18 - 2024-06-18

### Fixed

- Correct reference-style link index counting

## 2024.06.11 - 2024-06-11

### Added

- Make theme compatible with Hugo v0.114.0 or newer

## 2024.05.27 - 2024-05-27

### Fixed

- Add missing trailing forward slashes on links in html output format

## 2024.05.26 - 2024-05-26

### Changed

- Flatten CSS directory structure

## 2024.05.20 - 2024-05-20

### Added

- Create custom 404 page for html output format

### Fixed

- Fix incorrect (un)ordered list parsing in gemtext renderer

## 2024.05.02.1 - 2024-05-02

### Added

- Document unexpected behavior related to bolding and italics in gemtext renderer

## 2024.05.02 - 2024-05-02

### Changed

- Improve documentation
- Improve gemtext renderer

### Fixed

- Correct English i18n string

## 2024.02.19 - 2024-02-19

### Removed

- Remove Google Lighthouse score from README.md

## 2024.02.04 - 2024-02-04

### Added

- Document maximum supported Hugo version in README.md

### Fixed

- Fix some gemtext rendering rules not being applied
- Fix incorrect parsing of unordered lists in gemtext renderer again

## 2024.01.01.1 - 2024-01-01

### Fixed

- Fix incorrect parsing of unordered lists in gemtext renderer

## 2024.01.01 - 2024-01-01

### Added

- Write new documentation conforming to Diátaxis

## 2023.12.31 - 2023-12-31

### Added

- Support Markdown's ordered lists in gemtext renderer

## 2023.12.29 - 2023-12-29

### Added

- Support Markdown's alternative heading syntax in gemtext renderer

## 2023.12.02 - 2023-12-02

### Changed

- Improve documentation

### Added

- Lazy load inline images
- Add `referrerpolicy="noreferrer"` attribute to images
- Support Markdown's link titles in gemtext renderer

### Removed

- Remove `rel="noreferrer"` from non-web links

## 2023.11.30 - 2023-11-30

### Changed

- Improve documentation

## 2023.11.03 - 2023-11-03

### Changed

- Replace link reference numbers with their superscripts

## 2023.10.15 - 2023-10-15

### Changed

- Convert all dates in output to UTC for privacy

## 2023.10.08 - 2023-10-08

### Changed

- Improve documentation

## 2023.09.28 - 2023-09-28

### Added

- Make browsers not request absent favicon

## 2023.09.16 - 2023-09-16

### Added

- Add link underlines for accessibility

## 2023.09.10 - 2023-09-10

### Changed

- Shorten logo line-height so logos look better

### Added

- Add brackets around reference-style link indexes

## 2023.09.02 - 2023-09-02

### Added

- Add back CSS rule removed in previous version

## 2023.08.30 - 2023-08-30

### Fixed

- Fix whitespace around logos

### Removed

- Remove redundant CSS rule

## 2023.08.25 - 2023-08-25

### Changed

- Mandate having a title, intro, logo, and copyright notice in gemtext output format

### Fixed

- Fix capsule and website whitespace
- Fix crashing with absent page elements (entries, navlinks, etc.)

## 2023.08.10 - 2023-08-10

### Fixed

- Fix inline image scaling

## 2023.08.06 - 2023-08-06

### Fixed

- Fix incorrect printing of `pageinfo` tags in gemtext renderer

## 2023.08.02 - 2023-08-02

### Changed

- Update README.md

### Added

- Add multilingual support
- Add Spanish language support

### Fixed

- Correct minimum Hugo version

## 2023.07.04 - 2023-07-04

### Fixed

- Fix scrollbar covering preformatted text

## 2023.06.27.1 - 2023-06-27

### Changed

- Revert justifying text

## 2023.06.27 - 2023-06-27

### Changed

- Justify text

## 2023.06.01 - 2023-06-01

### Changed

- Improve CSS styling
- Update documentation

## 2023.05.16 - 2023-05-16

### Fixed

- Fix whitespace bug in gemtext renderer

## 2023.05.11 - 2023-05-11

### Changed

- Mandate having a title for html output format

## 2023.05.09.2 - 2023-05-09

### Changed

- Replace hardcoded language `en` with `$.Site.Language` for html output format

## 2023.05.09.1 - 2023-05-09

### Added

- Add support for overriding the default CSS

## 2023.05.09 - 2023-05-09

### Changed

- Make non-critical page elements optional
- Improve preformatted text parsing in gemtext renderer

### Added

- Document gemtext renderer

## 2023.05.08 - 2023-05-08

### Changed

- Improve documentation

### Fixed

- Fix demo links being rendered as real links in documentation

## 2023.05.05 - 2023-05-05

### Changed

- Improve README.md
- Improve link parsing in gemtext renderer
- Improve CSS

### Added

- Add inline image support to gemtext renderer
- Add link title support to gemtext renderer
- Add support of `+` symbol as unordered list syntax in gemtext renderer
- Document theme compatibility with gemtext

## 2023.04.09 - 2023-04-09

### Changed

- Improve page titles for html output format

## 2023.03.26 - 2023-03-26

### Changed

- Improve page style with non-breakable spaces in `pageinfo` for html output format

## 2023.03.16 - 2023-03-16

### Fixed

- Fix link parsing in gemtext renderer

## 2023.03.15 - 2023-03-15

### Fixed

- Fix blockquote paragraph margins in html output format

## 2023.03.12 - 2023-03-12

### Fixed

- Fix entry indexing logic in gemtext renderer

## 2023.02.25 - 2023-02-25

### Changed

- Remove trailing `index.gmi` from links
- Reorganize layouts

## 2023.02.24 - 2023-02-24

### Changes

- Move link emojis outside the link text
- Declare `safeHTML` where possible to avoid unneeded html rendering
- Simplify relative URLs in gemtext metadata partial

### Added

- Add tag list to metadata partial
- Implement taxonomies
- Implement terms
- Implement Atom feeds for taxonomies
- Implement Atom feeds for terms

## 2023.02.15 - 2023-02-15

### Fixed

- Remove extra space above unordered lists in html output format

## 2023.02.05 - 2023-02-05

### Changed

- Improve bold and italics parsing in gemtext renderer again

## 2023.01.28 - 2023-01-28

### Changed

- Always render the link emoji in reference-style links for html output format

### Fixed

- Stop rendering the link emoji in inline links for html output format

## 2023.01.25 - 2023-01-25

### Changed

- Improve preformatted text parsing in gemtext renderer

## 2023.01.24 - 2023-01-24

### Fixed

- Rewrite chunking algorithm to prevent content overwriting bug in gemtext renderer

## 2023.01.23 - 2023-01-23

### Fixed

- Improve bold and italics parsing in gemtext renderer again

## 2023.01.22 - 2023-01-22

### Changed

- Improve bold and italics parsing in gemtext renderer

### Fixed

- Implement chunking algorithm to avoid parsing preformatted text in gemtext renderer
- Fix rendering of links, headings, and unordered lists at beginning of document in gemtext renderer

## 2023.01.21.1 - 2023-01-21

### Changed

- Improve link style with non-breakable spaces for html output format
- Improve link parsing in gemtext renderer

### Fixed

- Fix whitespace after links in html output format

## 2023.01.21 - 2023-01-21

_First release._
