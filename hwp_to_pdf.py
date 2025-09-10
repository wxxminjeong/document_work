# -*- coding: utf-8 -*-
import os
import sys
import glob
from tkinter import Tk, messagebox
from pathlib import Path
import win32com.client as win32

# Tkinter 윈도우 생성 및 숨기기
root = Tk()
root.withdraw()

def hwp_to_pdf_converter():
    """
    현재 스크립트 폴더 및 하위 폴더에 있는 모든 .hwp 파일을 찾아
    'converted_pdfs'라는 폴더에 .pdf 파일로 변환하여 저장하는 함수입니다.
    """
    try:
        # 한글(HWP) 프로그램 COM 객체 생성
        # HWPFrame.HwpObject는 윈도우 UI가 있는 버전
        hwp = win32.gencache.EnsureDispatch('HWPFrame.HwpObject')

        # 한글 프로그램을 백그라운드에서 실행하여 사용자에게 보이지 않게 합니다.
        # hwp.XHwpWindows.Item(0).Visible = False

        # 보안 모듈 경고창이 뜨지 않도록 설정합니다.
        hwp.RegisterModule('FilePathCheckDLL', 'FileAuto')

        # 현재 스크립트의 경로를 가져옵니다.
        script_folder = Path(os.path.dirname(os.path.abspath(sys.argv[0])))

        # 모든 PDF 파일을 저장할 폴더를 정의합니다.
        output_folder = script_folder / 'converted_pdfs'
        
        # 출력 폴더가 존재하지 않으면 생성합니다.
        output_folder.mkdir(parents=True, exist_ok=True)

        # 현재 폴더 및 하위 폴더의 모든 .hwp 파일을 재귀적으로 찾습니다.
        hwp_files = list(script_folder.rglob('*.hwp'))
        
        if not hwp_files:
            messagebox.showinfo("알림", f"'{script_folder}' 폴더에서 HWP 파일을 찾을 수 없습니다.")
            hwp.Quit()
            return
            
        print(f"총 {len(hwp_files)}개의 HWP 파일을 찾았습니다.")

        for idx, hwp_file_path in enumerate(hwp_files):
            print(f"{idx + 1}/{len(hwp_files)} 변환 중: {hwp_file_path.name}")
            
            # HWP 파일을 엽니다.
            hwp.Open(str(hwp_file_path))

            # PDF로 저장하기 위한 기본 설정을 가져옵니다.
            hwp.HAction.GetDefault('FileSaveAsPdf', hwp.HParameterSet.HFileOpenSave.HSet)
            
            # 변환된 PDF 파일의 경로를 설정합니다.
            # 모든 PDF 파일을 지정된 출력 폴더에 저장합니다.
            pdf_file_path = output_folder / f"{hwp_file_path.stem}.pdf"
            hwp.HParameterSet.HFileOpenSave.filename = str(pdf_file_path)
            
            # PDF 형식으로 저장하도록 설정합니다.
            hwp.HParameterSet.HFileOpenSave.Format = 'PDF'
            
            # 파일 변환 및 저장을 실행합니다.
            hwp.HAction.Execute("FileSaveAsPdf", hwp.HParameterSet.HFileOpenSave.HSet)
            
            print(f"  -> PDF 파일로 저장 완료: {pdf_file_path.name}")

        messagebox.showinfo("알림", f"모든 HWP 파일의 PDF 변환 작업이 완료되었습니다.\n파일은 '{output_folder.name}' 폴더에 저장되었습니다.")

    except Exception as err:
        # 예외 발생 시 오류 메시지 박스를 띄웁니다.
        messagebox.showerror("오류", f"작업 중 오류가 발생했습니다: \n{err}")

    finally:
        # 작업이 완료되거나 오류가 발생하면 한글 프로그램을 종료합니다.
        try:
            hwp.Quit()
        except NameError:
            # hwp 객체가 생성되지 않았을 경우를 대비합니다.
            pass

if __name__ == "__main__":
    hwp_to_pdf_converter()
