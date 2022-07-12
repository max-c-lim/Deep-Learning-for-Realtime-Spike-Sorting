from custom_ephys_dataloader import EphysDataset
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np


class WaveformDataset(Dataset):
    """Dataset that represents template waveforms that will be pasted into noise for generating data samples"""

    def __init__(self, kilosort_npz_path, transform=None):
        """
        :param kilosort_npz_path: str
            Local path to .npz file containing template waveforms (result of spikesort_matlab4.py)
        :param transform: callable, optional
            Optional transform to be applied on a sample
        """

        npz = np.load(kilosort_npz_path, allow_pickle=True, mmap_mode="r")
        # self.locations = npz["locations"]
        # self.sampling = npz["fs"]
        self.units = npz["units"]

        self.transform = transform

    def __getitem__(self, idx):
        unit = self.units[idx]
        template = torch.from_numpy(unit["template"].T)
        template_max = template[int(unit["max_channel_id"]), :]
        sample = (template_max, unit["peak_ind"])

        if self.transform:
            sample = self.transform(sample)

        return sample

    def __len__(self):
        return len(self.units)


class ExperimentDataset(Dataset):
    """Dataset that represents a single experiment stored on S3"""

    def __init__(self, batch_uuid, experiment_num, sample_size, start, kilosort_npz_path, spike_times_path):
        """
        :param batch_uuid: str
            String indicating which batch to take from
        :param experiment_num: int
            Number of desired experiment
        :param sample_size: int
            This value should be passed in every time; this determines the size of the samples the dataloader
            should be returning. This is NOT the size of the dataset being loaded in by load_data.
        :param start: int
            Start of larger dataset (frame)
        :param kilosort_npz_path: str
            Local path to .npz file containing template waveforms (result of spikesort_matlab4.py)
        :param spike_times_path:
            Local path to .npy file containing a 1d array of spike times (in samples)
        """

        # TODO: Remove kilosort_npz_path and spike_times_path as parameters and have script download files from S3?
        # TOOD: Store maxwell file locally? Not just for current prototype but for future? Download from S3 and store?

        # Get times when there are no spikes

        # Create attr_csv for ephys_dataloader

        # Instantiate and store ephys_dataloader (pass pd.DataFrame for attr_csv instead of file path)

        # Instantiate and store waveform_dataloader

    def __len__(self):
        # TODO: How should length be defined?
        #       Number of data points without spike?
        #       Number of unique waveforms? <--- I think this one and randomly take data point
        #       Product of those two?

        # TODO: Should we store the different DL recordings in the same batch as different experiments?
        #       S3 has a structure that works well for having multiple recordings under same folder

        pass

    def __getitem__(self, idx):
        # TODO: How should the combination of non-spike times and waveforms be retrieved?
        #       There could be n_non_spike_times * n_waveforms unique data points?
        #       Make n_non_spike_times a parameter?

        # TODO: REMEMBER TO USE TORCH'S RANDOM, NOT NUMPY
        pass


class BatchDataset(Dataset):
    """Dataset to represent multiple recordings"""
    # TODO: This is a wrapper of ExperimentDataset


waveform_dataset = WaveformDataset("2953_sorted.npz")
for i in range(len(waveform_dataset)):
    sample = waveform_dataset[i]
    print(type(sample[1]))
    exit()


batch_uuid = "2022-06-30-e-UCSB-200123-2950-control"
experiment_num = "experiment1"  # Says it should be int in docstring, but must be str
sample_size = 300
attr_csv = "dataset_attr.csv"
start = 0

raw_dataset = EphysDataset(batch_uuid, experiment_num, sample_size, attr_csv, start, align="left")

for i in range(len(raw_dataset)):
    sample = raw_dataset[i]
    print(sample.shape)
