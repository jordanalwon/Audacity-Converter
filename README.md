# Audacity-Converter
*Audacity-Converter* extracts the data of an Audacity project file (.aup3) and makes it available for further processing or saves the data in more accessible file formats.

Audacity-Converter is MIT licensed
(c) 2024, Jordan Alwon

## Installation
*Audacity-Converter* has following dependencies:
```
git clone git@github.com:jordanalwon/Audacity-Converter.git
cd Audacity-Converter
```
```
uv sync
```

## Extract Data
```python
from convert import Converter
converter = Converter(path)
converter.extract_audio('data.wav')
converter.exptract_label("data.txt")
```

## Roadmap to v1.0
- [ ] Add Testframework
- [ ] Integrate Tests to Github CI
- [ ] Complete Docstring
- [ ] Generate Documentation from docstring
- [ ] Create C/C++ file reader to speed up the process