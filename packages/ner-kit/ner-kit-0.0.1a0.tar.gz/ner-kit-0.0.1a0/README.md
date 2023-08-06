## Named Entity Recognition Toolkit

Provide a toolkit for rapidly extracting useful entities from text using various Python packages. 

### Installation
```pip
pip install ner-kit
```

### Examples
Example 1: Stanford CoreNLP
```python
from nerkit.stanza import *
# First, set environment variable CORENLP_HOME to the CoreNLP folder
corenlp_root_path=r"{}\stanford-corenlp-4.3.2"
text="我喜欢游览广东孙中山故居景点！"
list_token=get_entity_list(text,corenlp_root_path=corenlp_root_path,language="chinese")
for token in list_token:
    print(f"{token['value']}\t{token['pos']}\t{token['ner']}")
```

Example 2: HanLP
```python
from nerkit.HanLP import *
text = "我喜欢游览广东孙中山故居景点！"
res=get_entity_list_by_hanlp(text,recognize='place')
print(res)
for s in res:
    st=str(s)
    ws=st.split("/")
    if ws[1]=="nr":
        print(ws[0],ws[1])
```

Example 3: Stanford CoreNLP (Not official version)
```python
import os
from nerkit.StanfordCoreNLP import get_entity_list
text="我喜欢游览广东孙中山故居景点！"
current_path = os.path.dirname(os.path.realpath(__file__))
res=get_entity_list(text,resource_path=f"{current_path}/stanfordcorenlp/stanford-corenlp-latest/stanford-corenlp-4.3.2")
print(res)
for w,tag in res:
    if tag in ['PERSON','ORGANIZATION','LOCATION']:
        print(w,tag)
```

### License
The `ner-kit` project is provided by [Donghua Chen](https://github.com/dhchenx). 

