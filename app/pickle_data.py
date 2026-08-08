import pickle


def get_pickle_data(file_name: str) -> list:
    data = []
    with open(file_name, "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                data.append(group)
            except EOFError:
                break
    return data
