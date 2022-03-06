# Changelog

### 0.X.X

### New features

### Maintenance and fixes

### Documentation

### Deprecation

### 0.2.0

### New features

* Add `mva` argument to `flexitext()` which controls the vertical alignment of individual texts within the outer text box (5da272172874fc89e54c4bf112a237dadb37062a).

### Maintenance and fixes

* Improve backgroundcolor behavior. The backgroundcolor of one piece of text does not overlap other pieces of text (32787dfe0e60c57154f99ffe09011c5e7fd6367a).
* Add `pyproject.toml` (#9).
* Numbers like X. are interpreted as X.0 floats (e.g. `1.`). Flexitext attempted to parse them as two numbers, resulting in an error (#9).
* Add `Changelog.md` (#9).
* Improved test coverage (#9).

### 0.1.0

This is the initial release

