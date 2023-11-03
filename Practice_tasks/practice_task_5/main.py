def read_file(file_name: str) -> list[int]:
    file = None
    try:
        file = open(file_name, "r")
        nums = []
        for i in file.read().split("\n"):
            num = int(i)
            nums.append(num)
        file.close()
        return nums[1:]
    except FileNotFoundError:
        print(f"{file_name} не существует")
    except IOError:
        print("IO ошибка")
    except ValueError:
        print("Содержимое файла некорректной структуры")
    except:
        print("Другие ошибки")
    finally:
        if file is not None:
            file.close()
    return []


if __name__ == "__main__":
    data = read_file(input("Введите имя файла: "))
    print(data)
