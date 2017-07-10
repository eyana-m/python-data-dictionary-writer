from pathlib import Path

import os
source = "Data/settlement/tables"

pathlist = Path(source).glob('**/*.html')
for path in pathlist:
    path_in_str = str(path)
    print(path_in_str)
