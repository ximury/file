import os


def rename_file_batch(path, word):
    """
    批量文件重命名
    :param path:文件路径
    :param word:文件名分词，以进行重命名
    :return:
    """
    files = os.listdir(path)
    print(files)
    for old_file in files:
        res = old_file.split(word)
        if len(res) == 2:
            print(res)
            episode = res[0]
            time = res[1]
            new_file_name = episode + time
            os.rename(path + old_file, path + new_file_name)


if __name__ == '__main__':
    file_path = "C:\\Users\\wyj\\Videos\\Captures\\完美世界\\"
    split_word = "EngSub"
    rename_file_batch(file_path, split_word)
