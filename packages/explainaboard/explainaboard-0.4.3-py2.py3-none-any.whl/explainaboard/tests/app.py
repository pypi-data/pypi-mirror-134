from explainaboard import TaskType, get_loader, FileType, get_processor

# path_data = "./artifacts/test-summ.tsv"
# loader = get_loader(TaskType.summarization, data = path_data)
# data = loader.load()
# processor = get_processor(TaskType.summarization, data = data)
# analysis = processor.process()
# analysis.write_to_directory("./")
#
#
#
# path_data = "./artifacts/test-ner.tsv"
# loader = get_loader(TaskType.named_entity_recognition, data = path_data)
# data = loader.load()
# processor = get_processor(TaskType.named_entity_recognition, data = data)
# analysis = processor.process()
# analysis.write_to_directory("./")
#
#
#
path_data = "./artifacts/test-classification.tsv"
loader = get_loader(TaskType.text_classification, data = path_data)
data = loader.load()
processor = get_processor(TaskType.text_classification, data = data)
analysis = processor.process()
analysis.write_to_directory("./")


path_data = "./artifacts/test-classification.tsv"
loader = get_loader(TaskType.text_classification, file_type= FileType.tsv, data = path_data)
data = loader.load()
processor = get_processor(TaskType.text_classification, data = data)
analysis = processor.process()
analysis.write_to_directory("./")


# path_data = "./artifacts/test-qa-squad.json"
# loader = get_loader(TaskType.extractive_qa, data = path_data)
# data = loader.load()
# processor = get_processor(TaskType.extractive_qa, data = data)
# analysis = processor.process()
# analysis.write_to_directory("./")
