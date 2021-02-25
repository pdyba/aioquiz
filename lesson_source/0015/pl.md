# Importowanie bibliotek

Biblioteke dowolną tj. wbudowaną lub zewnętrznie zainstlowaną (pip) można importowac 
na 3 podstawowe sposoby:

Cała biblioteka
```python
import pprint

pprint.pprint({"ala": "ma", "kota": 3, "a": "c"})
```

Wybrana część bibiloteki lub konkretna funkcja
```python
from pprint import pprint

pprint({"ala": "ma", "kota": 3, "a": "c"})
```

Aliasowanie
```python
from pprint import pprint as pp
 
pp({"ala": "ma", "kota": 3, "a": "c"})
```

Python 3.7 uprościł to
```python
from pprint import pp 
 
pp({"ala": "ma", "kota": 3, "a": "c"})
```

## Istotne biblioteki

* pprint
* random
* json
* datetime
* os
* logging
* re
