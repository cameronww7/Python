from __future__ import print_function
import zipfile

"""
 Prompt 113-Py-ZippingAndUnzippingFiles
"""

print("113-Py-ZippingAndUnzippingFiles")

"""
Unzipping and Zipping Files
As you are probably aware, files can be compressed to a zip format. 
Often people use special programs on their computer to unzip these 
files, luckily for us, Python can do the same task with just a few 
simple lines of code.
"""
print("\n113-Py-ZippingAndUnzippingFiles")
print("- - - - - - - - - - ")

# Create Files to Compress

# slashes may need to change for MacOS or Linux
f = open("new_file.txt", 'w+')
f.write("Here is some text")
f.close()

# slashes may need to change for MacOS or Linux
f = open("new_file2.txt", 'w+')
f.write("Here is some text")
f.close()


"""
Zipping Files
The zipfile library is built in to Python, we can use it to compress 
folders or files. To compress all files in a folder, just use the 
os.walk() method to iterate this process for all the files in a 
directory.
"""

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write("new_file.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

"""
Extracting from Zip Files
We can easily extract files with either the extractall() method to 
get all the files, or just using the extract() method to only grab 
individual files.
"""

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
print(zip_obj.extractall("extracted_content"))

