# wildcard_matcher

A simple wildcard string matcher widget for python 3.x.

# Installation

```shell
python -m pip install wildcard_matcher
```

# Usage

```
>>> import wildcard_matcher
>>> wildcard_matcher.match("hello world", "hello*")
True
>>> wildcard_matcher.match("hello world", "he*lo*world")
True
>>> wildcard_matcher.match("hello world", "he*lo*rld")
True
```

# Contributing

Please feel free to [log an issue](issues/new) with examples of what you tried and didn't work. PRs are most welcome.

