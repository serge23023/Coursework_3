from src.utils import print_operation

if __name__ == '__main__':
    for operations in print_operation(5):
        print(operations.__repr__())
