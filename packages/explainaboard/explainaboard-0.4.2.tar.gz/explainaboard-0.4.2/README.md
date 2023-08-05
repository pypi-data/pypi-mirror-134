# ExplainaBoard SDK
Reconstruct ExplainaBoard into OOP Version

## Installation
- for SDK users: `pip install explainaboard`
- for SDK developers: clone repo and run `pip install .` inside the repo 
  - use `pip install -e .`for developer install. This is only useful in certain situations. Please see python documentation for this option.

## How to use SDK

```python
from explainaboard import TaskType, get_loader, get_processor

path_data = "./explainaboard/tests/artifacts/test-summ.tsv"
loader = get_loader(TaskType.summarization, data = path_data)
data = loader.load()
processor = get_processor(TaskType.summarization, data = data)
analysis = processor.process()
analysis.write_to_directory("./")
```

### Existing Support [More](https://github.com/ExpressAI/ExplainaBoard/blob/main/docs/existing_supports.md)
* `TaskType.text_classification`
  * `FileType.tsv`
* `TaskType.named_entity_recognition`
  * `FileType.conll`
* `TaskType.summarization`
  * `FileType.tsv`
* `TaskType.extractive_qa`
  * `FileType.json` (same format with squad)



