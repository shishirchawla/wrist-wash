import os
from config import config
from features import *
import struct
import pandas as pd
import numpy as np
import logging
from collections import defaultdict
from preproc import writeRawDataToHTK, raw_data

log_config = config['logging']
logger = logging.getLogger(__name__)
def main():
  path = config['test_data_dir']
  open(os.path.join(path, "sessionlist.txt"), 'w').close()

  session_dict = defaultdict(list)

  for test_file in config['test_files_withoutnull']:
    print 'processing:', test_file
    test_file_path = os.path.join(config['dataset_dir_withoutnull'], test_file)
    df = loadDataset(test_file_path)

    htk_file_name = config['output_dir']+test_file+"_completesession.mfcc"
    activity_features = compute_features(df, config['num_features'])
    #activity_features = raw_data(df)
    if activity_features.shape[0] != 0:
      writeFeaturesToHTK(activity_features, htk_file_name)
      #writeRawDataToHTK(activity_features, htk_file_name)
      user_id = test_file.split('/')[0]
      user_session = int(test_file.split('_')[1])
      session_dict[(user_id, user_session)].append(htk_file_name)

  writeSessionFiles(session_dict)

def writeSessionFiles(session_dict):
  newline = "\n"

  for user in config['users']:
    path = './user' + user + '-train-data'
    open(os.path.join(path, "sessionlist.txt"), 'w').close()  # for leave one subject out
    for i in range(config['num_session_per_user']):
      open(os.path.join(path, "sessionlist" + str(i + 1) + ".txt"), 'w').close()  # for leave one session out

  for user in config['users']:
    path = './user' + user + '-test-data'
    open(os.path.join(path, "sessionlist.txt"), 'w').close()  # for leave one subject out
    for i in range(config['num_session_per_user']):
      open(os.path.join(path, "sessionlist" + str(i + 1) + ".txt"), 'w').close()  # for leave one session out

  # write leave one session out files
  for segment_key, segment_files in session_dict.iteritems():
    test_user_id = segment_key[0]
    trainpath = './user' + test_user_id + '-train-data'
    testpath = './user' + test_user_id + '-test-data'

    for i in range(config['num_session_per_user']):
      for segment in segment_files:
        test_user_session = segment.split('_')[1]

        if i + 1 != int(test_user_session):
          with open(os.path.join(trainpath, "sessionlist" + str(i + 1) + ".txt"), 'a') as train_file:
              train_file.write(segment + newline)
        else:
          with open(os.path.join(testpath, "sessionlist" + str(i + 1) + ".txt"), 'a') as test_file:
              test_file.write(segment + newline)

  # write leave one subject out files
  for user in config['users']:
    trainpath = './user' + user + '-train-data'
    testpath = './user' + user + '-test-data'

    for segment_key, segment_files in session_dict.iteritems():
      train_user_id = segment_key[0]
      train_user_session = segment_key[1]

      if train_user_id != user:
        with open(os.path.join(trainpath, "sessionlist.txt"), 'a') as train_file:
          for segment in segment_files:
            train_file.write(segment + newline)
      else:
        with open(os.path.join(testpath, "sessionlist.txt"), 'a') as test_file:
          for segment in segment_files:
            test_file.write(segment + newline)
        if train_user_session in config['user_adapt_test_sessions']:
          with open(os.path.join(testpath, "sessionlist-ua.txt"), 'a') as test_file:
            for segment in segment_files:
              test_file.write(segment + newline)

def loadDataset(filepath):
  column_names = ['timestamp', 'id', 'ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mic', 'activity']
  column_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  data = pd.read_csv(filepath, sep=",", names=column_names, usecols=column_indexes)
  data.dropna(axis=0, inplace=True)

  # sub sample data based on config TODO
  selected_index = np.arange(0, len(data.index), config['sub_sampling_factor'])
  data = data.ix[selected_index]

  return data

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
    while start + int(size) < data.count():
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
def compute_features(df, num_features, window_size=int(float(config['sub_window_size'])*config['sampling_freq']/config['sub_sampling_factor'])):
  features = np.empty((0, num_features))

  if df.isnull().values.any():
    return features

  for (start, end) in subwindows(df["timestamp"], window_size):
    window_df = df[start:end]
    window_features = np.array([])

    # Add ecdf
    # convert df to numpy matrix
    window_data = window_df.as_matrix(columns=['ax', 'ay', 'az', 'gx', 'gy', 'gz', 'mic'])
    window_features = np.append(window_features, ecdf(window_data, components=5))
    window_features = np.append(window_features, stddev(window_data))
    window_features = np.append(window_features, skew(window_data))
    window_features = np.append(window_features, kurtosis(window_data))

    features = np.vstack([features, window_features])

  return features


def writeFeaturesToHTK(features, output_file_name):
  byte_array = []

  for x in np.nditer(features):
    byte_array.append(bytearray(struct.pack(">f", x)))

  num_items_per_sample = features.shape[1]
  num_samples = int(len(byte_array)/num_items_per_sample)

  samples_byte = bytearray(struct.pack(">I", num_samples))
  # For sampling frequency of 100 hz (100 * 10^2 * x = 10^9)
  # FIXME make this value dynamic based on config
  samp_period_byte = bytearray(struct.pack(">I", 600000))
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

if __name__ == '__main__':
  main()

