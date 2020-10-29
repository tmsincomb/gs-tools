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
