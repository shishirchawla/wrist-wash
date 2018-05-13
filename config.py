# Specify all config such as train data path, test data path, etc in this file.

config = {
  'dataset_dir'   : '/Users/schawla/dev/wrist-wash/dataset/3.11',
  'dataset_dir_withoutnull'   : '/Users/schawla/dev/wrist-wash/dataset/3.11-withoutnull',
  'users'         : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '11', '10', '12'],
  'num_session_per_user' : 9,
  'user_adapt_test_sessions' : [7, 8, 9],
  'train_files'   : ['1/session_1_labels.csv', '1/session_2_labels.csv', '1/session_3_labels.csv', '1/session_4_labels.csv', '1/session_5_labels.csv', '1/session_6_labels.csv', '1/session_7_labels.csv', '1/session_8_labels.csv', '1/session_9_labels.csv',
                     '2/session_1_labels.csv', '2/session_2_labels.csv', '2/session_3_labels.csv', '2/session_4_labels.csv', '2/session_5_labels.csv', '2/session_6_labels.csv', '2/session_7_labels.csv', '2/session_8_labels.csv', '2/session_9_labels.csv',
                     '3/session_1_labels.csv', '3/session_2_labels.csv', '3/session_3_labels.csv', '3/session_4_labels.csv', '3/session_5_labels.csv', '3/session_6_labels.csv', '3/session_7_labels.csv', '3/session_8_labels.csv', '3/session_9_labels.csv',
                     '4/session_1_labels.csv', '4/session_2_labels.csv', '4/session_3_labels.csv', '4/session_4_labels.csv', '4/session_5_labels.csv', '4/session_6_labels.csv', '4/session_7_labels.csv', '4/session_8_labels.csv', '4/session_9_labels.csv',
                     '5/session_1_labels.csv', '5/session_2_labels.csv', '5/session_3_labels.csv', '5/session_4_labels.csv', '5/session_5_labels.csv', '5/session_6_labels.csv', '5/session_7_labels.csv', '5/session_8_labels.csv', '5/session_9_labels.csv',
                     '6/session_1_labels.csv', '6/session_2_labels.csv', '6/session_3_labels.csv', '6/session_4_labels.csv', '6/session_5_labels.csv', '6/session_6_labels.csv', '6/session_7_labels.csv', '6/session_8_labels.csv', '6/session_9_labels.csv',
                     '7/session_1_labels.csv', '7/session_2_labels.csv', '7/session_3_labels.csv', '7/session_4_labels.csv', '7/session_5_labels.csv', '7/session_6_labels.csv', '7/session_7_labels.csv', '7/session_8_labels.csv', '7/session_9_labels.csv',
                     '8/session_1_labels.csv', '8/session_2_labels.csv', '8/session_3_labels.csv', '8/session_4_labels.csv', '8/session_5_labels.csv', '8/session_6_labels.csv', '8/session_7_labels.csv', '8/session_8_labels.csv', '8/session_9_labels.csv',
                     '9/session_1_labels.csv', '9/session_2_labels.csv', '9/session_3_labels.csv', '9/session_4_labels.csv', '9/session_5_labels.csv', '9/session_6_labels.csv', '9/session_7_labels.csv', '9/session_8_labels.csv', '9/session_9_labels.csv',
                     '11/session_1_labels.csv', '11/session_2_labels.csv', '11/session_3_labels.csv', '11/session_4_labels.csv', '11/session_5_labels.csv', '11/session_6_labels.csv', '11/session_7_labels.csv', '11/session_8_labels.csv', '11/session_9_labels.csv'],
  'test_files'    : [],
  'test_files_withoutnull'  : ['1/session_1_labels_withoutnull.csv', '1/session_2_labels_withoutnull.csv', '1/session_3_labels_withoutnull.csv', '1/session_4_labels_withoutnull.csv', '1/session_5_labels_withoutnull.csv', '1/session_6_labels_withoutnull.csv', '1/session_7_labels_withoutnull.csv', '1/session_8_labels_withoutnull.csv', '1/session_9_labels_withoutnull.csv',
                              '2/session_1_labels_withoutnull.csv', '2/session_2_labels_withoutnull.csv', '2/session_3_labels_withoutnull.csv', '2/session_4_labels_withoutnull.csv', '2/session_5_labels_withoutnull.csv', '2/session_6_labels_withoutnull.csv', '2/session_7_labels_withoutnull.csv', '2/session_8_labels_withoutnull.csv', '2/session_9_labels_withoutnull.csv',
                              '3/session_1_labels_withoutnull.csv', '3/session_2_labels_withoutnull.csv', '3/session_3_labels_withoutnull.csv', '3/session_4_labels_withoutnull.csv', '3/session_5_labels_withoutnull.csv', '3/session_6_labels_withoutnull.csv', '3/session_7_labels_withoutnull.csv', '3/session_8_labels_withoutnull.csv', '3/session_9_labels_withoutnull.csv',
                              '4/session_1_labels_withoutnull.csv', '4/session_2_labels_withoutnull.csv', '4/session_3_labels_withoutnull.csv', '4/session_4_labels_withoutnull.csv', '4/session_5_labels_withoutnull.csv', '4/session_6_labels_withoutnull.csv', '4/session_7_labels_withoutnull.csv', '4/session_8_labels_withoutnull.csv', '4/session_9_labels_withoutnull.csv',
                              '5/session_1_labels_withoutnull.csv', '5/session_2_labels_withoutnull.csv', '5/session_3_labels_withoutnull.csv', '5/session_4_labels_withoutnull.csv', '5/session_5_labels_withoutnull.csv', '5/session_6_labels_withoutnull.csv', '5/session_7_labels_withoutnull.csv', '5/session_8_labels_withoutnull.csv', '5/session_9_labels_withoutnull.csv',
                              '6/session_1_labels_withoutnull.csv', '6/session_2_labels_withoutnull.csv', '6/session_3_labels_withoutnull.csv', '6/session_4_labels_withoutnull.csv', '6/session_5_labels_withoutnull.csv', '6/session_6_labels_withoutnull.csv', '6/session_7_labels_withoutnull.csv', '6/session_8_labels_withoutnull.csv', '6/session_9_labels_withoutnull.csv',
                              '7/session_1_labels_withoutnull.csv', '7/session_2_labels_withoutnull.csv', '7/session_3_labels_withoutnull.csv', '7/session_4_labels_withoutnull.csv', '7/session_5_labels_withoutnull.csv', '7/session_6_labels_withoutnull.csv', '7/session_7_labels_withoutnull.csv', '7/session_8_labels_withoutnull.csv', '7/session_9_labels_withoutnull.csv',
                              '8/session_1_labels_withoutnull.csv', '8/session_2_labels_withoutnull.csv', '8/session_3_labels_withoutnull.csv', '8/session_4_labels_withoutnull.csv', '8/session_5_labels_withoutnull.csv', '8/session_6_labels_withoutnull.csv', '8/session_7_labels_withoutnull.csv', '8/session_8_labels_withoutnull.csv', '8/session_9_labels_withoutnull.csv',
                              '9/session_1_labels_withoutnull.csv', '9/session_2_labels_withoutnull.csv', '9/session_3_labels_withoutnull.csv', '9/session_4_labels_withoutnull.csv', '9/session_5_labels_withoutnull.csv', '9/session_6_labels_withoutnull.csv', '9/session_7_labels_withoutnull.csv', '9/session_8_labels_withoutnull.csv', '9/session_9_labels_withoutnull.csv',
                              '11/session_1_labels_withoutnull.csv', '11/session_2_labels_withoutnull.csv', '11/session_3_labels_withoutnull.csv', '11/session_4_labels_withoutnull.csv', '11/session_5_labels_withoutnull.csv', '11/session_6_labels_withoutnull.csv', '11/session_7_labels_withoutnull.csv', '11/session_8_labels_withoutnull.csv', '11/session_9_labels_withoutnull.csv',
                              '10/session_1_labels_withoutnull.csv', '10/session_2_labels_withoutnull.csv', '10/session_3_labels_withoutnull.csv', '10/session_4_labels_withoutnull.csv', '10/session_5_labels_withoutnull.csv', '10/session_6_labels_withoutnull.csv', '10/session_7_labels_withoutnull.csv', '10/session_8_labels_withoutnull.csv', '10/session_9_labels_withoutnull.csv',
                              '12/session_1_labels_withoutnull.csv', '12/session_2_labels_withoutnull.csv', '12/session_3_labels_withoutnull.csv', '12/session_4_labels_withoutnull.csv', '12/session_5_labels_withoutnull.csv', '12/session_6_labels_withoutnull.csv', '12/session_7_labels_withoutnull.csv', '12/session_8_labels_withoutnull.csv', '12/session_9_labels_withoutnull.csv'],
  # HTK train and test dirs
  'train_data_dir': './train-data',
  'test_data_dir' : './user1-test-data', #FIXME
  # HTK data
  'output_dir'    : './htkdata/',

  # Data properties
  'sampling_freq'               : 200,   # in hz
  'activity_types'              : [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
  'ignore_activities'           : [1, 2, 3],
  'null_class_label'            : 0,
  'num_samples_per_sub_window'  : 10,
  'sliding_window_overlap'      : 1.0,  # 1 means no overlap

  # null class config
  'ignore_null_class'           : 1,

  # number of features
  #'num_features'  : ((3*7)+7), # ecdf with 3 components + mean
  'num_features'  : (7*4)+(5*7),
  #'num_features'  : 7,

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
  'sub_window_size'   : 0.06,    # in seconds

  'loso'              : 1,      # leave one subject out (loso)

  # log file properties
  'log_file_name'     : 'wrist-wash.log',

  # sub sampling factor
  'sub_sampling_factor' : 4
}

