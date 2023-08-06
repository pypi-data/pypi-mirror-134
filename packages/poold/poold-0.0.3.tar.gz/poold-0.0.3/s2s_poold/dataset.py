import os
from poold.data import Dataset
from src.utils.models_util import get_forecast_filename
from datetime import datetime
import pandas as pd

class S2SDataset(Dataset):
    """ S2S data class for online learning """ 
    def __init__(self, targets, models, gt_id, horizon): 
        """ Initialize dataset.

        Args:
            targets (list[datetime]): list of target prediction dates 
            models (list[str]): list of expert model names
            gt_id (str): ground truth id
            horizon (str):  horizon
        """
        # Call base class constructor
        super().__init__(targets, models)

        self.gt_id = gt_id
        self.horizon = horizon

    def get(self, target, model):
        """ Get model prediction for a target time

        Args:
            target: a target represetnation 
            model: a model name representation
        
        Returns: 
        """
        date_str = datetime.strftime(target_date_obj, '%Y%m%d')      

        fname = get_forecast_filename(
                model=model, 
                submodel=None,
                gt_id=gt_id,
                horizon=horizon,
                target_date_str=target)

        if not os.path.exists(fname):
            printf("Warning: no forecast found for model {model} on target {target}.")
            return None

        df = pd.read_hdf(fname).rename(columns={"pred": f"{a}"})

        # If any of expert predictions are NaN
        if df.isna().any(axis=None): 
            printf("Warning: NaNs in forecast for model {model} on target {target}.")
            return None

        # Important to sort in order to ensure lat/lon points are in consistant order 
        df = df.set_index(['start_date', 'lat', 'lon']).squeeze().sort_index()   
        
        return df

    def get_and_merge(self, target):
        """  Get all model predictions and return a 
        merged set of predictions for a target.

        Args:
            target: a target represetnation 
        """
        pass
        # Get names of submodel forecast files using the selected submodel
        # expert_filenames = [(a, m, get_forecast_filename(model=m, 
        #                                         submodel=s,
        #                                         gt_id=gt_id,
        #                                         horizon=horizon,
        #                                         target_date_str=date_str))
        #                     for (a, m, s) in expert_submodels]       
        



