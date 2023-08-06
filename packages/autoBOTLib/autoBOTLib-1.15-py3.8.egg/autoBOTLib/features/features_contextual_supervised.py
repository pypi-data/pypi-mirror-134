from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import TrainingArguments
from transformers import Trainer
import numpy as np
import pandas as pd
import torch

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


dfx_train = pd.read_csv("../../data/fake/train.tsv", sep="\t")
dfx_test = pd.read_csv("../../data/fake/train.tsv", sep="\t")
print(dfx_train)

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-multilingual-cased")

inputs = tokenizer(dfx_train.text_a.values.tolist(), padding="max_length", truncation=True)

unique_labels = len(np.unique(dfx_train.label.values))
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-multilingual-cased", num_labels=unique_labels)

training_args = TrainingArguments("test_trainer")
train_dataset = CustomDataset(inputs, dfx_train.label.values.tolist())
trainer = Trainer(
    model=model, args=training_args, train_dataset=train_dataset)
#trainer.train()
