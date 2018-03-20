import os
from config import config
from collections import defaultdict
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from scipy import io
import struct
import logging
from features import *
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import Pipeline

log_config = config['logging']
logger = logging.getLogger(__name__)
def process_data(train_dir, train_files):
  if config['loso']:
    session_dict = defaultdict(list)
  else:
    activity_trainfile_dict = defaultdict(list)
    activity_testfile_dict = defaultdict(list)

  for train_file in train_files:
    print 'processing:', train_file

    file_path = os.path.join(train_dir, train_file)

    # Read data
    readings_df = loadDataset(file_path)

    # DEBUG: see what acceleroemter data looks like (the following line will
    # plot data of the first 15 seconds)
    #plot_activity('activity '+str(24), readings_df[readings_df["activity"] == 24][:1500])

    # assign block numbers to contiguous activities so they can be grouped
    readings_df['block'] = (readings_df.activity.shift(1) != readings_df.activity).astype(int).cumsum()
    for activity, df in readings_df.groupby(['activity', 'block']):
      activity_type = activity[0]
      activity_group_no = activity[1]

      # null class check
      if config['ignore_null_class'] and activity_type == config['null_class_label']:
          continue

      htk_file_name = config['output_dir']+train_file+"_act_"+str(activity_type)+"_instance_"+str(activity_group_no)+".mfcc"
      activity_features = compute_features(df, config['num_features'])
      if activity_features.shape[0] != 0:
        writeFeaturesToHTK(activity_features, htk_file_name)
        if config['loso']:
          session_dict[(train_file, activity_type)].append(htk_file_name)
        else:
          if train_file in config["train_files"]:
            activity_trainfile_dict[activity_type].append(htk_file_name);
          else:
            activity_testfile_dict[activity_type].append(htk_file_name);

  if config['loso']:
    writeLosoFiles(session_dict)
  else:
    if config['write_train_files']:
      writeTrainFiles(activity_trainfile_dict)
    if config['write_test_files']:
      writeTestFiles(activity_testfile_dict)

def writeLosoFiles(session_dict):
  newline = "\n"

  for user in config['users']:
    path = './user' + user + '-train-data'
    for i in range(config['num_session_per_user']):
      for activity_type in config['activity_types']:
        open(os.path.join(path, "trainlist"+str(i+1)+"_act_"+str(activity_type)+".txt"), 'w').close()

  for user in config['users']:
    path = './user' + user + '-test-data'
    for i in range(config['num_session_per_user']):
      open(os.path.join(path, "testlist"+str(i+1)+".txt"), 'w').close()

  for segment_key, segment_files in session_dict.iteritems():
    test_user_id = segment_key[0].split('/')[0]
    test_user_session = segment_key[0].split('_')[1]
    activity_type = segment_key[1]

    path = './user'+test_user_id+'-train-data'

    for i in range(config['num_session_per_user']):
      if i+1 != int(test_user_session):
        with open(os.path.join(path, "trainlist"+str(i+1)+"_act_"+str(activity_type)+".txt"), 'a') as train_file:
          for segment in segment_files:
            train_file.write(segment + newline)
      else:
        with open(os.path.join(path, "testlist"+str(i+1)+".txt"), 'a') as test_file:
          for segment in segment_files:
            test_file.write(segment + newline)

def writeTrainFiles(activity_trainfile_dict):
  newline = "\n"

  path = config['train_data_dir']
  open(os.path.join(path, "trainlist.txt"), 'w').close()
  for activity_type in config['activity_types']:
    open(os.path.join(path, "trainlist"+"_act_"+activity_type+".txt"), 'w').close()

  # train files
  with open(os.path.join(path, "trainlist.txt"), 'a') as trainlist_file:
    for activity_type, train_files in activity_trainfile_dict.iteritems():
        with open(os.path.join(path, "trainlist"+"_act_"+str(activity_type)+".txt"), 'a') as train_activity_file:
          for train_file in train_files:
            trainlist_file.write(train_file + newline)
            train_activity_file.write(train_file + newline)

def writeTestFiles(activity_testfile_dict):
  newline = "\n"

  path = config['test_data_dir']
  open(os.path.join(path, "testlist.txt"), 'w').close()
  open(os.path.join(path, "classifylist.txt"), 'w').close()

  # test files
  with open(os.path.join(path, "testlist.txt"), 'a') as trainlist_file, open(os.path.join(path, "classifylist.txt"), 'a') as classifylist_file:
    for activity_type, train_files in activity_testfile_dict.iteritems():
      for train_file in train_files:
        trainlist_file.write(train_file + newline)
        classifylist_file.write(train_file + newline)

def loadDataset(filepath):
  column_names = ['timestamp', 'id', 'ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mic', 'activity']
  column_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  data = pd.read_csv(filepath, sep=",", names=column_names, usecols=column_indexes)
  data.dropna(axis=0, inplace=True)
  return data

# The following code has been adapted from
# http://blog.jamesrossiter.co.uk/2008/11/16/converting-csv-and-vector-data-to-native-htk-format-using-c/
def writeFeaturesToHTK(features, output_file_name):
  byte_array = []

  for x in np.nditer(features):
    byte_array.append(bytearray(struct.pack(">f", x)))

  num_items_per_sample = features.shape[1]
  num_samples = int(len(byte_array)/num_items_per_sample)

  samples_byte = bytearray(struct.pack(">I", num_samples))
  # For sampling frequency of 100 hz (100 * 10^2 * x = 10^9)
  # FIXME make this value dynamic based on config
  samp_period_byte = bytearray(struct.pack(">I", 1000000))
  # 4 bytes for each entry
  samp_size_byte = bytearray(struct.pack(">h", num_items_per_sample*4))
  # Typecode for MFCC
  parm_kind_byte = bytearray(struct.pack(">h", 6))

  with open(output_file_name, "wb") as binFile:
    binFile.write(samples_byte)
    binFile.write(samp_period_byte)
    binFile.write(samp_size_byte)
    binFile.write(parm_kind_byte)
    for eachbyte in byte_array:
        binFile.write(eachbyte)


########################################################
# Utility functions for creating and processing        #
# windows.                                             #
########################################################
def windows(data, size):
    start = 0
    size_with_buffer = size + config['num_samples_per_sub_window'] - 1
    while start < data.count():
        yield start, start + size_with_buffer
        start += int(size*config['sliding_window_overlap'])

def subwindows(data, size):
    start = 0
    #while start + config['num_samples_per_sub_window'] < data.count():
    while start + (int(size)*2) < data.count():
        yield start, start + config['num_samples_per_sub_window']
        start += int(size)

def segment_signal(data, window_size=int(config['window_size'])*config['sampling_freq']):
  segments = []
  for (start, end) in windows(data["timestamp"], window_size):
    window_df = data[start:end]
    logger.info('Activity type: ' + str(data["activity"].iloc[0]) + ' start: ' + str(start) + ' end: ' + str(end))
    window_size_with_buffer = window_size + config['num_samples_per_sub_window'] - 1
    if(len(data["timestamp"][start:end]) == window_size_with_buffer):
      segments.append(window_df)
    else:
      logger.info('Activity type: ' + str(data["activity"].iloc[0]))
      logger.info('# complete segments: ' + str(len(segments)))
      logger.info('- not enough samples ' + str(len(data["timestamp"][start:end])))

  return segments


########################################################
# Feature extraction related functions.                #
########################################################
def compute_features(df, num_features, window_size=int(float(config['sub_window_size'])*config['sampling_freq'])):
  features = np.empty((0, num_features))

  if df.isnull().values.any():
    return features

  for (start, end) in subwindows(df["timestamp"], window_size):
    window_df = df[start:end]
    window_features = np.array([])

    # Add ecdf
    # convert df to numpy matrix
    window_data = window_df.as_matrix(columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mic'])
    window_features = np.append(window_features, ecdf(window_data))

    features = np.vstack([features, window_features])

  return features


########################################################
# Utility functions for visualizing accelerometer data.#
########################################################
def feature_normalize(dataset):
  mu = dataset.mean(axis=0)
  sigma = dataset.std(axis=0)
  return (dataset - mu)/sigma

def plot_axis(ax, x, y, title):
  ax.plot(x, y)
  ax.set_title(title)
  ax.xaxis.set_visible(False)
  ax.set_ylim([min(y) - y.std(axis=0), max(y) + y.std(axis=0)])
  ax.set_xlim([min(x), max(x)])
  ax.grid(True)

def plot_activity(activity,data):
  fig, (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize = (15, 10), sharex = True)
  plot_axis(ax0, data['timestamp'], data['x-axis'], 'x-axis')
  plot_axis(ax1, data['timestamp'], data['y-axis'], 'y-axis')
  plot_axis(ax2, data['timestamp'], data['z-axis'], 'z-axis')
  plt.subplots_adjust(hspace=0.2)
  fig.suptitle(activity)
  plt.subplots_adjust(top=0.90)
  plt.show()

