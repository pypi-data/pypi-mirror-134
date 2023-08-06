import os

class Version:
    def __init__(self,minecraft_dir):
        self.minecraft_dir = minecraft_dir
    def get_list(self):

        self.version_path = []

        for i,_,_ in os.walk(self.minecraft_dir+'\\versions'):
            if len(i.split('\\')) - 1 == len(f'{self.minecraft_dir}\\versions'.split('\\')):
                self.version_path.append(i)
        return self.version_path
