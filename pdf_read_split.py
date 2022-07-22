from PyPDF2 import PdfWriter, PdfReader
import re

PDF_FILE_PATH = ""
PDF_PATH = ""

reader = PdfReader(PDF_PATH)

for idx, page in enumerate(reader.pages):
    writer = PdfWriter()
    if "Data Erasure Report" in page.extract_text():
        writer.add_page(reader.pages[idx])
        #extract imei
        try:
            imei = re.search('IMEI:[0-9]+', page.extract_text())
            imei_no = imei.group().split(":")[-1]
            if "Data Erasure Report" in reader.pages[idx+1].extract_text():
                #save file
                with open('{0}{1}.pdf'.format(PDF_PATH, imei_no), 'wb') as f:
                    writer.write(f)
                    f.close()
            else:
                #add next page and save file
                writer.add_page(reader.pages[idx+1])
                with open('{0}{1}.pdf'.format(PDF_PATH, imei_no), 'wb') as f:
                    writer.write(f)
                    f.close()
        except:
            print("Error page: " + str(idx+1))