import os

print(dir(os))
# Create a new file
with open('sample.txt', 'w') as f:
    f.write("this is the sample text file")

print("✅ sample.txt exists?", os.path.exists('sample.txt'))


# Check if it's a file or directory
print("📄 Is file?", os.path.isfile("sample.txt"))
print("📁 Is directory?", os.path.isdir("sample.txt"))
# Get file size (in bytes)
print("📏 File size:", os.path.getsize("sample.txt"))

# Delete the file
os.remove("sample.txt")
print("🧹 sample.txt deleted")
