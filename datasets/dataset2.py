import torch
from torch.utils.data import Dataset
from .datasets import register_dataset

@register_dataset("dataset2")
class Dataset2(Dataset):
    def __init__(self) -> None:
        super(Dataset, self).__init__()
    
    def __getitem__(self, index):
        return super().__getitem__(index)
    
    def __len__(self):
        pass
    