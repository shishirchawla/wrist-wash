from preproc import *
import os
import shutil
import logging
import argparse

def main():
  # TODO: finish argument parsing
  parser = argparse.ArgumentParser()
  parser.add_argument("--removedirs", help="set argument to 1 if you want to remove existing data directories")
  args = parser.parse_args()

  if args.removedirs:
    remove_dirs()

  # Setup logging
  setup_logging()
  # Create data directories if they don't exist
  create_dirs()
  # Process data
  process_data(config['dataset_dir'], config['train_files']+config['test_files'])

def remove_dirs():
  if os.path.exists(config['output_dir']):
    shutil.rmtree(config['output_dir'])
  if os.path.exists(config['train_data_dir']):
    shutil.rmtree(config['train_data_dir'])
  if os.path.exists(config['test_data_dir']):
    shutil.rmtree(config['test_data_dir'])
  for user in config['users']:
    if os.path.exists('user'+user+'-train-data'):
      shutil.rmtree('user'+user+'-train-data')
    if os.path.exists('user'+user+'-test-data'):
      shutil.rmtree('user'+user+'-test-data')

def create_dirs():
  if not os.path.exists(config['output_dir']):
    os.makedirs(config['output_dir'])
  if config['loso']:
    for user in config['users']:
      user_dir = os.path.join(config['output_dir'], user)
      if not os.path.exists(user_dir):
        os.makedirs(user_dir)
      if not os.path.exists('user'+user+'-train-data'):
        os.makedirs('user'+user+'-train-data')
      if not os.path.exists('user'+user+'-test-data'):
        os.makedirs('user'+user+'-test-data')
  else:
    if not os.path.exists(config['train_data_dir']):
      os.makedirs(config['train_data_dir'])
    if not os.path.exists(config['test_data_dir']):
      os.makedirs(config['test_data_dir'])

def setup_logging():
  logging.getLogger().setLevel(logging.DEBUG)

  formatter = logging.Formatter('%(asctime)s - %(name)-30s - %(levelname)-8s - %(message)s')

  fh = logging.FileHandler(config['log_file_name'])
  fh.setFormatter(formatter)
  fh.setLevel(logging.DEBUG)

  ch = logging.StreamHandler()
  ch.setFormatter(formatter)
  ch.setLevel(logging.ERROR)

  logging.getLogger().addHandler(fh)
  logging.getLogger().addHandler(ch)

if __name__ == '__main__':
  main()

