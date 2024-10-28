import os

def remove_thumb_files(folder_path):
  """Removes all files ending with 'thumb' from a folder.

  Args:
    folder_path: The path to the folder containing the files.
  """
  for filename in os.listdir(folder_path):
    filename_no_ext = os.path.splitext(filename)[0].lower()
    print(filename_no_ext)
    if filename_no_ext.endswith("thumb"):
      filepath = os.path.join(folder_path, filename)
      print(filepath)
      os.remove(filepath)
  print(f"Deleted all files ending with 'thumb' from {folder_path}")

# Replace 'path/to/your/folder' with your actual folder path
folder_path = 'C:/Users/kam/Downloads/Telegram Desktop/ChatExport_2024-07-03/video'
remove_thumb_files(folder_path)