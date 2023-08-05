import random

from akerbp.mlpet import Dataset
from akerbp.mlpet import utilities

# Set a seed to ensure robustability when comparing tests
random.seed(448)

# Instantiate an empty dataset object using the example settings and mappings provided
dataset_name = "shear"
ds = Dataset(
    settings=rf"support/settings_{dataset_name}.yaml",
    mappings=r"support/mappings.yaml",
    folder_path=r"support/",
)

# Populate the dataset with data from a file (support for multiple file formats and direct cdf data collection exists)
ds.load_from_pickle(ds.data_path)

# The original data will be kept in ds.df_original and will remain unchanged
print(ds.df_original.head())

# Split the data into train-validation sets
df_train, df_test = utilities.train_test_split(
    df=ds.df_original,
    target_column=ds.label_column,
    id_column=ds.id_column,
    test_size=0.3,
)

# Preprocess the data for training according to default workflow
# print(ds.default_preprocessing_workflow) <- Uncomment to see what the workflow does
df_preprocessed = ds.preprocess(df_train)

# Preprocessing can also be fully controlled by specifying the workflow manually
# Either by relying on default options already in the dataset class
df_select_default = ds.preprocess(df_train, select_curves={})
# The above will fall back to the defaults for select_curves which is to select
# curves found in the self.curves attribute of the Dataset class instance which in
# turn was set by what was passed in the settings.yaml

# PLEASE NOTE that the order in which kwargs are passed to preprocess will be
# the order in which they are executed in the preprocessing method!

# Or by expliclity overriding the defaults
df_select_manual = ds.preprocess(df_train, select_curves={"curves": ["GR"]})

print(df_preprocessed.head())
print(df_select_default.head())
print(df_select_manual.head())
