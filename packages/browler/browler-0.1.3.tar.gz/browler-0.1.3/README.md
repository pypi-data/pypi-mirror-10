# Selenium Based Web Crawler

ReadTheDocs - http://browler.readthedocs.org/en/latest/

## Requirements

* redis `brew install redis`

## Install

```
pip install browler
```

## Uninstall

```
pip uninstall browler
```

## Configuration

### With Selenium Hub
```python
config = {
            "browser": 'remote',
            "remote": {
                "url": 'http://localhost:49044/wd/hub',
                'browser': 'firefox'
            },
            "url": "https://en.wikipedia.org/wiki/Main_Page",
            "limit": 10,
            "processes": 2
         }
```

### Local Firefox

```python
config = {
            "browser": 'firefox',
            "url": "https://en.wikipedia.org/wiki/Main_Page",
            "limit": 10,
            "processes": 2
         }
```
