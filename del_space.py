import os
import glob

# 1. 스크립트가 있는 디렉토리로 현재 작업 디렉토리 변경
try:
    # 현재 실행 중인 스크립트의 절대 경로를 가져옵니다.
    script_path = os.path.abspath(__file__)
    
    # 스크립트가 위치한 디렉토리의 경로를 추출합니다.
    script_dir = os.path.dirname(script_path)
    
    # 현재 작업 디렉토리를 스크립트 디렉토리로 변경합니다.
    os.chdir(script_dir)
    print(f"현재 작업 디렉토리: {os.getcwd()}")
    
except NameError:
    # 인터프리터에서 직접 실행 시 __file__이 정의되지 않아 발생하는 에러 처리
    print("스크립트 파일을 직접 실행해야 합니다. IDE나 인터프리터에서 실행 시 이 기능은 동작하지 않을 수 있습니다.")
    script_dir = os.getcwd() # 현재 경로를 기본값으로 설정

# 2. 현재 폴더 내의 모든 PDF 파일 찾기
# "*"은 모든 문자열을, ".pdf"는 확장자를 의미합니다.
pdf_files = glob.glob("*.pdf")

# 3. PDF 파일 이름에서 공백 제거
if not pdf_files:
    print("\n현재 폴더에 PDF 파일이 없습니다.")
else:
    print("\n--- 변경 전 파일 목록 ---")
    for file_name in pdf_files:
        print(file_name)

    print("\n--- 파일 이름 변경 진행 ---")
    for old_file_name in pdf_files:
        # 파일 이름에서 모든 공백(" ")을 제거합니다.
        new_file_name = old_file_name.replace(" ", "")
        
        # 원본 파일 이름과 변경된 이름이 같지 않으면 이름 변경
        if old_file_name != new_file_name:
            try:
                os.rename(old_file_name, new_file_name)
                print(f"'{old_file_name}' -> '{new_file_name}'로 이름 변경 완료.")
            except Exception as e:
                print(f"오류 발생: {old_file_name}의 이름을 변경할 수 없습니다. 이유: {e}")
        else:
            print(f"'{old_file_name}' 파일에는 공백이 없습니다.")

    # 4. 변경 후 파일 목록 확인
    print("\n--- 변경 후 파일 목록 ---")
    pdf_files_after = glob.glob("*.pdf")
    for file_name in pdf_files_after:
        print(file_name)