import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data
train_sample = pd.read_csv('data/train_sample.csv')

# Set data types
train_sample['ip'] = train_sample['ip'].astype('category')
train_sample['app'] = train_sample['app'].astype('category')
train_sample['device'] = train_sample['device'].astype('category')
train_sample['os'] = train_sample['os'].astype('category')
train_sample['channel'] = train_sample['channel'].astype('category')
train_sample['click_time'] = train_sample['click_time'].astype('datetime64[ns]')
train_sample['attributed_time'] = train_sample['attributed_time'].astype('datetime64[ns]', errors='ignore')
train_sample['is_attributed'] = train_sample['is_attributed'].astype('category')

# Basic counts
total_clicks = len(train_sample)
total_downloads = (len(train_sample[train_sample['is_attributed'] == 1]))

print('Total clicks:', total_clicks)
print('Total downloads:', total_downloads)
print('Download percentage:', total_downloads / total_clicks)

# Preview data
print(train_sample.describe())
print(train_sample.head(5))

# Unique values per feature
print(train_sample.agg(['nunique']))