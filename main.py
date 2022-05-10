import torch
import os
from datasets import make_dataset

if __name__ == '__main__':
    dataset = make_dataset("dataset1")
    print(dataset.__dict__)