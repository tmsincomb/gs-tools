# gs-tools

Google Sheet general tools using gspread

## Usage

```python
from gs_tools.pandas_from_gs import df_from_gs

name = 'Summary of experimental techniques - BICCN flagship'
sheet_name = 'Glossary of terms'

df = df_from_gs(name, sheet_name)
df.head()
```

## Installation

```bash
git clone git@github.com:tmsincomb/gs-tools.git
pip install -e gs-tools
```
