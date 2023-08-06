EnvBert is an easy-to-use Python library built on top of Bert models to organise environmental data in environmental site assessments.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EnvBert

```bash
pip install EnvBert
```

## Usage

```python
# returns the predicted class along with the probability 
from EnvBert.due_diligence import *

doc = """
	weathered shale was encountered below the surface area with fluvial deposits. 
	Sediments in the coastal plain region are found above and below the bedrock 
	with sandstones and shales that form the basement rock"
      """

predict(doc)

```

## About
This Package is part of the Research topic "AI for Environment Due-Diligence" conducted by Afreen Aman, Deepak John Reji, Shaina Raza. If you use this work (code, model or dataset),

Please star at: AI for Environment Due-Diligence, (2022), GitHub repository, https://github.com/dreji18/environmental-due-diligence

## License
[MIT](https://choosealicense.com/licenses/mit/)
