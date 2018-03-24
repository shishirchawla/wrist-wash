# Specify all config such as train data path, test data path, etc in this file.

config = {
  'dataset_dir'   : '/Users/schawla/dev/wrist-wash/dataset/3.10',
  'users'         : ['1', '2'],
  'num_session_per_user' : 4,
  'train_files'   : ['1/session_1_labels.txt', '1/session_2_labels.txt', '1/session_3_labels.txt', '1/session_4_labels.txt',
                     '2/session_1_labels.txt', '2/session_2_labels.txt', '2/session_3_labels.txt', '2/session_4_labels.txt'],
  'test_files'    : [] ,

  # HTK train and test dirs
  'train_data_dir': './train-data',
  'test_data_dir' : './test-data',
  # HTK data
  'output_dir'    : './htkdata/',

  # Data properties
  'sampling_freq'               : 50,   # in hz
  'activity_types'              : [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15],
  'null_class_label'            : 0,
  'num_samples_per_sub_window'  : 10,
  'sliding_window_overlap'      : 1.0,  # 1 means no overlap

  # null class config
  'ignore_null_class'           : 1,

  # number of features
  #'num_features'  : ((3*7)+7), # ecdf with 3 components + mean
  'num_features'  : (7*4)+(3*7),

  'write_train_files' : 1,
  'write_test_files' : 1,

  # Normalize
  'normalize'     : 0,
  # PCA
  'pca'           : 0,

  # Debugging properties
  'logging'       : 1,

  # HMM properties
  'window_size'       : 1.0,    # in seconds
  'sub_window_size'   : 0.04,    # in seconds

  'loso'              : 1,      # leave on subject out (loso)

  # log file properties
  'log_file_name'     : 'wrist-wash.log'

}

