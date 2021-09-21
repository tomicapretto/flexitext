# Overview

Flexitext provides two interfaces to draw text with a variety of styles in Matplotlib plots.

- **Functional:** Takes a formatted string and draws the formatted text. This parses the formatted string and then uses classes from the OOP interface under the hood.
- **Object-Oriented:** This does not involve any parsing step, but requires you to create the text objects either by hand or programatically. This is useful if you want to re-use styles without having to manipulate Python strings.
