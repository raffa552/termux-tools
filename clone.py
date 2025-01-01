#pastikan sudah membaca readme.md
import os
import shutil

def list_files_in_current_dir():
    os.system('ls -a')

def duplicate_file():
    list_files_in_current_dir()

    file_to_duplicate = input("\nMasukkan nama file yang ingin diduplikasi: ").strip()

    if not os.path.exists(file_to_duplicate):
        print(f"File {file_to_duplicate} tidak ditemukan.")
        return

    duplicate_name = file_to_duplicate + "_duplicate"
    try:
        shutil.copy2(file_to_duplicate, duplicate_name)
        print(f"File {file_to_duplicate} berhasil diduplikasi dengan nama {duplicate_name}.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menduplikasi file: {e}")

duplicate_file()
      
