from typing import Dict, List, Any, Optional
from .aggregating import Aggregating, aggregating
from typing import Callable, Mapping, Iterator
import numpy as np
from tqdm import tqdm
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from operation import DatasetOperation, dataset_operation
from featurize import *
from data import TextData

class TextClassificationAggregating(Aggregating, DatasetOperation):


    def __init__(self,
                 name:str = None,
                 func:Callable[...,Any] = None,
                 resources: Optional[Mapping[str, Any]] = None,
                 contributor: str = None,
                 processed_fields: List = ["text"],
                 generated_field: str = None,
                 task = "text-classification",
                 description = None,
                 ):
        super().__init__(name = name, func = func, resources = resources, contributor = contributor,
                         task = task,description=description)
        self._type = 'TextClassificationAggregating'
        self.processed_fields = ["text"]
        if isinstance(processed_fields,str):
            self.processed_fields[0] = processed_fields
        else:
            self.processed_fields = processed_fields
        self.generated_field = generated_field
        self._data_type = "Dataset"




class text_classification_aggregating(aggregating, dataset_operation):
    def __init__(self,
                 name: Optional[str] = None,
                 resources: Optional[Mapping[str, Any]] = None,
                 contributor: str = None,
                 processed_fields: List = ["text"],
                 generated_field:str = None,
                 task = "text-classification",
                 description = None,
                 ):
        super().__init__(name = name, resources = resources, contributor = contributor, description=description)
        self.processed_fields = processed_fields
        self.generated_field = generated_field
        self.task = task


    def __call__(self, *param_arg):
        if callable(self.name):
            tf_class = TextClassificationAggregating(name = self.name.__name__, func=self.name)
            return tf_class(*param_arg)
        else:
            f = param_arg[0]
            name = self.name or f.__name__
            tf_cls = TextClassificationAggregating(name=name, func = f,
                                   resources = self.resources,
                                   contributor = self.contributor,
                                    processed_fields = self.processed_fields,
                                    generated_field = self.generated_field,
                                    task = self.task,
                                    description=self.description,)
            return tf_cls



@text_classification_aggregating(name = "get_label_distribution", contributor= "datalab", processed_fields= "text",
                                 task="text-classification", description="this function is used to calculate the text length")
def get_label_distribution(samples:Iterator):
    """
    Input:
    samples: [{
     "text":
     "label":
    }]
    Output:
        dict:
        "label":n_samples
    """
    labels_to_number = {}
    for sample in samples:
        text, label = sample["text"], sample["label"]




        if label in labels_to_number.keys():
            labels_to_number[label] += 1
        else:
            labels_to_number[label] = 1

    res = {
        "imbalance_ratio": min(labels_to_number.values())*1.0/max(labels_to_number.values()),
        "label_distribution":labels_to_number
    }

    return res


@text_classification_aggregating(name="get_statistics", contributor="datalab", processed_fields="text",
                                 task="text-classification",
                                 description="this function is used to calculate the text length")
def get_statistics(samples: Iterator):
    """
    Input:
    samples: [{
     "text":
     "label":
    }]
    Output:
        dict:
        "label":n_samples

    usage:
    you can test it with following code:

    from datalabs import load_dataset
    from aggregate import *
    dataset = load_dataset('mr')
    res = dataset['test'].apply(get_statistics)
    print(next(res))

    """
    labels_to_number = {}
    lengths = []
    for sample in tqdm(samples):
        text, label = sample["text"], sample["label"]

        # gender bias
        results = get_gender_bias.func(text)

        # average length
        text_length = get_length.func(text)
        lengths.append(text_length)

        # label imbalance
        if label in labels_to_number.keys():
            labels_to_number[label] += 1
        else:
            labels_to_number[label] = 1

    res = {
        "imbalance_ratio": min(labels_to_number.values()) * 1.0 / max(labels_to_number.values()),
        "average_text_length":np.average(lengths),
    }

    return res