# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Check if file exists, then delete it:
import os
if os.path.exists('demofile.txt'):
  os.remove('demofile.txt')
else:
  print('The file doesnot exist')

