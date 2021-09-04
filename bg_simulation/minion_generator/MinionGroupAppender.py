class MinionGroupAppender(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def _append_minion_dict(self):
        module_list = open(self.file_path, 'r').readlines()
        class_dict = dict()

        for module in module_list:
            class_obj = module.split(' ')[-1].replace('\n', '')
            class_dict[class_obj] = class_obj

        return class_dict

    def _append_minion_group(self):
        class_dict = self._append_minion_dict()

        dict_str = "\nminion_group = {\n"
        for element in class_dict:
            dict_str += f"\t'{element}': {element},\n"
        dict_str += "}"

        return dict_str

    def append_minion_group(self):
        with open(self.file_path, 'a') as f:
            f.write(self._append_minion_group())
