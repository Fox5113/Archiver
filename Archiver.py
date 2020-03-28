import codecs
import sys
import os

def encript(encripting_data: str):
    encript_data = ""
    encripting_iterator = iter(encripting_data)
    symbol = None
    counter = 0
    while True:
        try:
            if symbol is None:
                symbol = next(encripting_iterator)
                counter = 1
            else:
                temp =  next(encripting_iterator)
                if temp == symbol:
                    counter += 1
                else:
                    encript_data += f"{counter}{symbol}"
                    counter = 1
                    symbol = temp
        except StopIteration:
            encript_data += f"{counter}{symbol}"
            return encript_data


def decript(decripting_data: str):
    decript_data = ""
    decripting_iterator = iter(decripting_data)
    count = 0
    symbol = ""
    while True:
        try:
            temp =  next(decripting_iterator)
            if str(temp).isdigit():
                if count > 0:
                    count = int(str(count) + temp)
                else:
                    count =  int(temp)
            else:
                symbol = temp
                decript_data += str(symbol * count)
                count = 0
        except StopIteration:
            decript_data += str(symbol * count)
            return decript_data

def work_file_compress(_path):
    try:
        f = open(_path, "rb")
        wf_path = path + ".arct"
        wf = open(_path + ".arct", "wb")
        f_line = f.readlines()
        for line in f_line:
            temp = line.decode('UTF-8').rstrip()
            wf.write((encript(temp) + "\n").encode())
        f.close()
        wf.close()
        print(f"Compressed '{_path}' into {os.path.getsize(wf_path)} bytes")
        compress_stat = 100 - ((os.path.getsize(wf_path)/ os.path.getsize(_path)) * 100)
        print(f"Сompression percentage: {compress_stat}%")
        os.path.getsize(_path)
    except Exception as e:
        raise e
    finally:
        f.close()
        wf.close()


def work_file_decompress(_path):
    try:
        f = open(_path, "rb")
        wf_path = _path[:-4]
        wf = open(wf_path, "wb")
        f_line = f.readlines()
        for line in f_line:
            temp = line.decode('UTF-8').rstrip()
            wf.write((decript(temp) + "\n").encode())
        f.close()
        wf.close()
        print(f"Decompressed '{_path}' into {os.path.getsize(wf_path)} bytes")
        compress_stat = 100 - ((os.path.getsize(_path) / os.path.getsize(wf_path)) * 100)
        print(f"Decompression percentage: {compress_stat}%")
    except Exception as e:
        raise e
    finally:
        f.close()
        wf.close()



def unit_test():
    test_1 = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEE"
    test_2 = "kkkkdddslFFSAa"
    test_3 =  "LLLSSsD##@@\\\\"

    print(encript(test_1))
    print(encript(test_2))
    print(encript(test_3))

    print(decript(encript(test_1)))
    print(decript(encript(test_2)))
    print(decript(encript(test_3)))


if __name__ == "__main__":
    #unit_test()

    metod = None
    path = None
    if  len(sys.argv) != 3:
        print('''Программа  принимает два параметра:
        первый параметр является методом, который применить к файлу (compress, decompress)
        compress - выполняет сжатие файла по алгоритму RLE
        decompress - выполняет распаковку
        вторым парметром программа принимает путь к файлу для которого осуществить сжатие или распаковку''')
    else:
        metod =  sys.argv[1]
        path = sys.argv[2]

        if metod == "compress":
            pass
            work_file_compress(path)
        elif metod == "decompress":
            work_file_decompress(path)




