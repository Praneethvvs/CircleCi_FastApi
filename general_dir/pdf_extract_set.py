from PyPDF2 import PdfFileWriter, PdfFileReader

input_path = "/home/kairos/PRANEETH_FILES/ONLINE_VISAS_UPDATED/march_18/Wrong_folder/wrong"
output_path = "/home/kairos/PRANEETH_FILES/ONLINE-VISAS/wrong-folders/Jagadeesh"
# inputpdf = PdfFileReader(open(input_path, "rb"))
import shutil
import os
import traceback

# for i in range(inputpdf.numPages):


# test_dict = {"2013 Petition - Kuragayala, Naveen.pdf":
#                  {"visa-petition": "1-4",
#                   "g-28": "5-8",
#                   "test": "5"},
#              "Akbar H-1B Petition.pdf":
#                  {"visa-petition": "1-2",
#                   "academic-transcripts": "3-4",
#                   "test": "5"}
#              }

import json

with open("/home/kairos/Downloads/jagadeesh_22_03.json") as f:
    test_dict = json.load(f)

for pdfname, values in test_dict.items():
    inputpdf = PdfFileReader(open(os.path.join(input_path, pdfname), "rb"))
    for doctypes, page_count in values.items():
        if page_count != "":
            try:
                if "_" in page_count or "-" in page_count:
                    page_count = page_count.replace("_", "-").replace("--", "-")
                    page_count = list(map(int, page_count.split("-")))
                    output = PdfFileWriter()
                    for x in range(page_count[0], page_count[1] + 1):
                        try:
                            output.addPage(inputpdf.getPage(x-1))
                        except:
                            pass
                    save_path = os.path.join(output_path, doctypes)
                    os.makedirs(save_path, exist_ok=True)
                    save_name = os.path.join(save_path, (f"{os.path.splitext(os.path.basename(pdfname))[0]}-{page_count}"))
                    with open(f"{save_name}.pdf", "wb+") as outputStream:
                        output.write(outputStream)

                else:
                    output = PdfFileWriter()
                    output.addPage(inputpdf.getPage(int(page_count)-1))
                    save_path = os.path.join(output_path, doctypes)
                    os.makedirs(save_path, exist_ok=True)
                    save_name = os.path.join(save_path, (f"{os.path.splitext(os.path.basename(pdfname))[0]}-{page_count}"))
                    with open(f"{save_name}.pdf", "wb+") as outputStream:
                        output.write(outputStream)
            except:
                traceback.print_exc()
                print(f"error with {page_count} for {doctypes} in {pdfname}")
                pass


# for filenames, values in test_dict.items():
#
#
# output = PdfFileWriter()
# output.addPage(inputpdf.getPage(0))
# output.addPage(inputpdf.getPage(1))
# with open(output_path, "wb+") as outputStream:
#     output.write(outputStream)


