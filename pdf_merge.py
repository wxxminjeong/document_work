import os
from PyPDF2 import PdfMerger

# 스크립트 파일이 위치한 디렉토리 경로를 가져옵니다.
script_directory = os.path.dirname(os.path.abspath(__file__))

# 현재 작업 디렉토리를 스크립트 디렉토리로 변경합니다.
os.chdir(script_directory)

# 현재 작업 디렉토리에 있는 모든 파일을 나열합니다.
files_in_directory = os.listdir(script_directory)

# PDF 파일만 걸러냅니다. (대소문자 구분 없이)
pdf_files = [f for f in files_in_directory if f.lower().endswith('.pdf')]
pdf_files.sort()

# ... (나머지 코드는 이전과 동일) ...
pdf_merger = PdfMerger()

if not pdf_files:
    print("PDF 파일이 없습니다.")
else:
    for pdf in pdf_files:
        try:
            pdf_merger.append(pdf)
            print(f"'{pdf}' 파일을 추가했습니다.")
        except Exception as e:
            print(f"'{pdf}' 파일을 추가하는 중 오류 발생: {e}")

    output_filename = "merged.pdf"
    with open(output_filename, 'wb') as merged_file:
        pdf_merger.write(merged_file)

    pdf_merger.close()
    
    print(f"\n모든 PDF 파일이 '{output_filename}'으로 성공적으로 합쳐졌습니다.")