# CocktailDB

[![](https://img.shields.io/github/v/tag/thexxiv/cocktaildb-py?label=version)](https://github.com/thexxiv/cocktaildb-py/releases/latest) [![](https://img.shields.io/github/license/thexxiv/cocktaildb-py)](https://github.com/thexxiv/cocktaildb-py/blob/main/LICENSE)

TheCocktailDB API client for **Python**.

### Download
[PyPI](https://pypi.org/project/cocktaildb/)

```
pip install cocktaildb
```

### Example

```py
from cocktaildb import search

for cocktail in search("beer"):
    print(cocktail.strDrink)
```

### Documentation

* [pdoc](https://thexxiv.github.io/cocktaildb-py)

### License

CocktailDB is released under the [Apache License 2.0](https://github.com/thexxiv/cocktaildb-py/blob/main/LICENSE).

```
 Copyright 2022 XXIV

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
```