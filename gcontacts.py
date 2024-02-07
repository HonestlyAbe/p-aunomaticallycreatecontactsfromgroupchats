import PyPDF2
# Get the path of the PDF file from the user
def main():
    path = input("Enter the path of the PDF file: ")
    texts = []
    # Open the PDF file in read binary mode
    with open(path, "rb") as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfFileReader(file)

        # Iterate over each page in the PDF
        for page_num in range(reader.numPages):
            # Extract the text from the current page
            page = reader.getPage(page_num)
            text = page.extract_text()

            # Print each line in the extracted text
            for line in text.split("+1"):
                texts.append("+1" + line)

        contacts = []
        for line in texts:
            if line.find("-") != -1:
                name = line[line.find("-")+5:line.find(",")]
                if len(name.split(" ")) < 3 and len(name.split(" ")) > 1:
                    number = line[0:line.find("-")+5]
                    for char in number:
                        if char.isdigit() == False and char != "+":
                            number = number.replace(char, "")
                    contacts.append(name + ',' + number)


    ''' make vcf file in this format:
    VERSION:3.0
    FN:[Name]
    N:[Name]
    TEL:[Number]
    CATEGORIES:myContacts
    END:VCARD
    '''
    def contacts_to_vcf(contacts, filename):
        with open(filename, "w") as file:
            for contact in contacts:
                name = contact.split(",")[0]
                number = contact.split(",")[1]
                file.write("BEGIN:VCARD\n")
                file.write("VERSION:3.0\n")
                file.write("FN:" + name + "\n")
                file.write("N:" + name + "\n")
                file.write("TEL:" + number + "\n")
                file.write("CATEGORIES:myContacts\n")
                file.write("END:VCARD\n")

    contacts_to_vcf(contacts, "contacts.vcf")



if __name__ == "__main__":
    main()


