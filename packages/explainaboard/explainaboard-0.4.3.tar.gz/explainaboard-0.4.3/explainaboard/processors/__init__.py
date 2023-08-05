# when a new processor is implemented, remember to import it here so it gets registered
from . import text_classification
from . import named_entity_recognition
from . import extractive_qa
from . import summarization
from .processor_registry import get_processor