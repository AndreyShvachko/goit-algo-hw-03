import os
import shutil
import argparse

def copy_files(source_dir, dest_dir):

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_ext = file.split('.')[-1]

                dest_subdir = os.path.join(dest_dir, file_ext)
                os.makedirs(dest_subdir, exist_ok=True)

                shutil.copy2(file_path, dest_subdir)
                print(f"Копіюється файл: {file_path} -> {dest_subdir}")

            except Exception as e:
                print(f"Не вдалося скопыювати файл {file_path}: {e}")

def main():

    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів за розширенням.")
    parser.add_argument('source_dir', help="Шлях до вхідної директорії")
    parser.add_argument('dest_dir', nargs='?', default='dist', help="Шлях до директорії призначення (за замовчуванням 'dist')")

    args = parser.parse_args()

    source_dir = args.source_dir
    dest_dir = args.dest_dir

    if not os.path.exists(source_dir):
        print(f"Вихідна директорія {source_dir} не існує.")
        return

        os.makedirs(dest_dir, exist_ok=True)

        copy_files(source_dir, dest_dir)

if __name__ == '__main__':
    main()