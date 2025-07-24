---
title: "{{ replace .Name "-" " " | title }}"
draft: true
pageinfo: false
makerefs: false
{{ $hugoVersionSlice := split hugo.Version "." -}}
{{ $majorVersion := int (index $hugoVersionSlice 0) -}}
{{ $minorVersion := int (index $hugoVersionSlice 1) -}}
{{ if and (eq $majorVersion 0) (lt $minorVersion 123) }}_{{ end }}build:
  list: never
---

