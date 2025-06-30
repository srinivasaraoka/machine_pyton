import pypandoc
pypandoc.download_pandoc()  # Downloads and installs Pandoc automatically
from docx2pdf import convert

# Converts and saves PDF in the same folder
convert("SrinivasaRaoKagithaResume.docx")
output = pypandoc.convert_file('SrinivasaRaoKagithaResume.docx', 'pdf', outputfile="example.pdf")
print("Converted to PDF:", output)

# import os
# from docx2pdf import convert

# # 📁 Set the folder path where your .docx files are stored
# folder_path = r"C:\Users\kagsrini\machine_pyton"  # <- Change this if needed

# # 🔄 Loop through all files in the folder
# for file in os.listdir(folder_path):
#     if file.endswith(".docx"):
#         docx_file = os.path.join(folder_path, file)
#         print(f"Converting: {docx_file}")
#         try:
#             convert(docx_file)
#             print(f"✅ Converted to PDF: {file}")
#         except Exception as e:
#             print(f"❌ Failed to convert {file}: {e}")
