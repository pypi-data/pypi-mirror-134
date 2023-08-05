# Pyaliner

Library for aligning and visually comparing sequential data in the terminal.

## paired 2-way ground-truth vs other comparison

### compact

![Compact paired target vs output](/images/paired-2way.png)

### classic

![Classic paired target vs output](/images/classic-paired-2way.png)

## inlined ground-truth vs other 2-way comparison 

### compact

![Compact inlined target vs output](/images/inlined-2way.png)

### classic

![Classic inlined target vs output](/images/classic-inlined-2way.png)

## paired 3-way ground-truth vs other comparison

### compact

![Compact paired input vs target vs output](/images/paired-3way.png)

### classic

![Classic paired input vs target vs output](/images/classic-paired-3way.png)

## alignment

```python

>>> from pyaliner import align, COMPACT

>>> align('Example invalid invalid sentence'.split(), 'Example sentence'.split())
(('Example', 'invalid', 'invalid', 'sentence'), ('Example', '⎵', '⎵', 'sentence'))

>>> align('Example invalid invalid sentence'.split(), 'Example sentence'.split(), kind=COMPACT)
(('Example', 'invalid∙invalid', 'sentence'), ('Example', '⎵', 'sentence'))

```

# Limitations

*  Three-way alignment uses a slow heuristic.
*  Wide characters, e.g., East Asian scripts,  are not properly aligned with narrow ones

# Installing

Install with pip:

```shell
pip install pyaliner
```

# Testing

Unit tests are written with [pytest](https://docs.pytest.org/en/stable) and [hypothesis](https://hypothesis.works/). 
Run with:

```shell
pip install pytest hypothesis

pytest
```

# Changelog

Check the [Changelog](https://github.com/JoseLlarena/pyaliner/blob/master/CHANGELOG.md) for fixes and enhancements of each version.

# License

Copyright Jose Llarena 2022

Distributed under the terms of the [MIT](https://github.com/JoseLlarena/pyaliner/blob/master/LICENSE) license, Pyaliner is free 
and open source software.