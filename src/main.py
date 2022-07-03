from fileinput import input as file_input
from glob import glob
from os import rename
from os.path import isfile
from sys import exit

TEMP_FILE_NAME = ".tmp"
MERGED_FILE_NAME = "merged.vcf"

def get_file_exists_string(filename):
  return "A file named \"" + filename + "\" already exists in this folder!"

if isfile(MERGED_FILE_NAME): exit(get_file_exists_string(MERGED_FILE_NAME))
if isfile(TEMP_FILE_NAME): exit(get_file_exists_string(TEMP_FILE_NAME))

contact_files = glob("*.vcf")

if contact_files:
  print("Merging contacts...")
  with open(TEMP_FILE_NAME, 'wt') as merged_file, file_input(contact_files) as input_lines:
    merged_file.writelines(input_lines)
  rename(TEMP_FILE_NAME, MERGED_FILE_NAME)
  print("Contacts successfully merged!")
else:
  print("No VCF files found in this folder!")
