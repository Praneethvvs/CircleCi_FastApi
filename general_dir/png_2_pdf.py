import os
import img2pdf



def png_merge_to_pdf(input_path,save_path):
    if os.path.exists(save_path):
        print(f"{save_path} path exists")
    else:
        os.makedirs(save_path)
    root_path = input_path
    images_list = os.listdir(root_path)

    pdf_list = list(set(map(lambda x: x[:x.index("-")],images_list)))
    print(pdf_list)

    for i in pdf_list:
        print(i)
        with open(os.path.join(save_path,f"{i}.pdf"),"wb+") as f:
            try:
                f.write(img2pdf.convert([os.path.join(root_path,filename) for filename in images_list if filename.endswith(".png") and filename.startswith(i)]))
            except:
                print(f"error with pdf {i}")

png_merge_to_pdf(r"D:\newfolder_8_3\pngs_list",r"D:\newfolder_8_3\pdfs")