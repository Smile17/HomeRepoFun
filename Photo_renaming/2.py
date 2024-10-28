import os

def rename_images(folder_path):
  """Renames images in a folder based on the existing date format,
  adding a sequence number for duplicates.

  Args:
    folder_path: The path to the folder containing the images.
  """
  used_names = set()  # Set to store encountered names (avoids duplicates)
  for filename in os.listdir(folder_path):
    # Check if it's an image file

    if filename.lower().endswith((".mp4")):
        try:
            # Extract the date part
            date_part = filename.split("@")[1].split("_")[0]
            day, month, year = date_part.split("-")
            base_filename = f"{year}_{month}_{day}"  # Base filename without extension
            # Check for existing names and create unique filename
            count = 1
            new_filename = f"{base_filename}_{count:02}{os.path.splitext(filename)[1]}"
            while new_filename in used_names:
                count += 1
                new_filename = f"{base_filename}_{count:02}{os.path.splitext(filename)[1]}"
            used_names.add(new_filename)  # Add new name to prevent duplicates

            # Construct the new path
            new_filepath = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(os.path.join(folder_path, filename), new_filepath)
        except:
            print(filename)
  print("Images renamed successfully!")

# Replace 'path/to/your/folder' with your actual folder path
folder_path = 'C:/Users/kam/Downloads/Telegram Desktop/ChatExport_2024-07-03/video'
rename_images(folder_path)
print("Images renamed successfully!")