from PyPDF2 import PdfReader

def extract_sections(doc_list, pdf_dir):
    sections = []
    for doc in doc_list:
        try:
            pdf_path = f"{pdf_dir}/{doc}"
            reader = PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if not text:
                    continue
                lines = [line.strip() for line in text.split("\n") if line.strip()]
                for line in lines[:5]:  # First 5 lines per page
                    sections.append({
                        "document": doc,
                        "page": i + 1,
                        "section_title": line,
                        "importance_rank": 0
                    })
        except Exception as e:
            print(f"Failed to process {doc}: {e}")
    return sections
