from dataclasses import dataclass, field
from typing import List
from enum import Enum


@dataclass
class Task:
    """
    TODO: add supported_file_types
    """
    name: str
    supported: bool = field(default=False)
    supported_metrics: List[str] = field(default_factory=list)


@dataclass
class TaskCategory:
    name: str
    description: str
    tasks: List[Task]


class TaskType(str, Enum):
    text_classification = "text-classification"
    named_entity_recognition = "named-entity-recognition"
    extractive_qa = "extractive-qa"
    summarization = "summarization"


_task_categories: List[TaskCategory] = [
    TaskCategory("conditional-text-generation",
                 "data-to-text and text transduction tasks such as translation or summarization",
                 [
                     Task("machine-translation"),
                     Task("sentence-splitting-fusion"),
                     Task(TaskType.summarization, True, [
                          "blue", "rouge1", "rouge2", "rougel"])
                 ]),
    TaskCategory("text-classification", "predicting a class index or boolean value",
                 [Task(TaskType.text_classification, True, ["F1score", "Accuracy"])]),
    TaskCategory("structure-prediction", "predicting structural properties of the text, such as syntax",
                 [Task(TaskType.named_entity_recognition, True, ["f1_score_seqeval"])]),
    TaskCategory("question-answering", "question answering tasks",
                 [Task(TaskType.extractive_qa, True, ["f1_score_qa", "exact_match_qa"])])
]


def get_task_categories():
    """getter for task categories data"""
    return _task_categories
