
import os,json,multiprocessing,threading
try:
    from file import File
except BaseException:
    pass
try:
    from .file import File
except BaseException:
    pass

class Download:
    def __init__(self,version):
        try:

            os.mkdir(r'C:\Users\Default\AppData\Roaming\.mcl')
        except BaseException as e:
            pass
        self.basepath = r'C:\Users\Default\AppData\Roaming\.mcl'
        File('https://launchermeta.mojang.com/mc/game/version_manifest.json',self.basepath+'\\versions.json')

        with open(self.basepath+'\\versions.json') as f:
            self.content = f.read()

        for i in eval(self.content)['versions']:
            if i['id'] == version:
                self.dic = i
                return
        raise SystemError(''
                          'This version does not exist.')
    def download_version_json(self,name,minecraft_dir):
        try:
            os.mkdir(minecraft_dir+f'\\versions\\{name}')
        except BaseException as e:
            pass

        File(self.dic['url'],minecraft_dir+f'\\versions\\{name}\\{name}.json')
    def download_core_jar(self,name,minecraft_dir):
        url = json.load(open(minecraft_dir+f'\\versions\\{name}\\{name}.json'))['downloads']['client']['url']
        File(url,minecraft_dir+f'\\versions\\{name}\\{name}.jar')
    def download_assets(self,name,minecraft_dir):
        url = json.load(open(minecraft_dir + f'\\versions\\{name}\\{name}.json'))["assetIndex"]['url']
        dic = json.load(open(minecraft_dir + f'\\versions\\{name}\\{name}.json'))

        File(url,f'{minecraft_dir}\\assets\\indexes\\{dic["assets"]}.json')

        asset = json.load(open(f'{minecraft_dir}\\assets\\indexes\\{dic["assets"]}.json'))
        process = multiprocessing.Process(target=self.download_assets_core,args=[asset,name,minecraft_dir])
        process.run()
    def download_assets_core(self,asset,name,minecraft_dir):
        for i in asset['objects'].values():
            try:
                os.mkdir(f'{minecraft_dir}\\assets\\objects\\{i["hash"][:2]}')
            except BaseException as e:
                pass
            File(f'http://resources.download.minecraft.net/{i["hash"][:2]}/{i["hash"]}',f'{minecraft_dir}\\assets\\objects\\{i["hash"][:2]}\\{i["hash"]}')
            print(i["hash"])
    def download_lib(self,name,minecraft_dir):
        libs = json.load(open(minecraft_dir + f'\\versions\\{name}\\{name}.json'))['libraries']
        for i in libs:
            thread = multiprocessing.Process(target=self.download_core,args=[i,name,minecraft_dir])

            thread.run()



    def download_core(self,i,name,minecraft_dir):

        url = i['downloads']['artifact']['url']

        path = i['downloads']['artifact']['path']

        base_path = f'{minecraft_dir}/libraries'
        p = base_path
        for j in path.split('/')[:-1]:
            base_path += f'\\{j}'
            try:
                os.mkdir(base_path)
            except BaseException as e:
                pass

        name = p+'/'+path
        File(url,name)
        print(name)
        try:

            path = i['downloads']['classifiers']["natives-windows"]['path']
            url = i['downloads']['classifiers']["natives-windows"]['url']
            for j in path.split('/')[:-1]:
                base_path += f'\\{j}'
                try:
                    os.mkdir(base_path)
                except BaseException as e:
                    pass
            name = p + '/' + path
            File(url, name)
            print(name)
        except BaseException as e:
            print(e)
    def main(self,name,minecraft_dir):
        self.download_version_json(name,minecraft_dir)
        self.download_core_jar(name,minecraft_dir)
        self.download_assets(name,minecraft_dir)
        self.download_lib(name,minecraft_dir)





if __name__ == '__main__':
    test = Download('1.16.5')
    test.main('test','D:\\awd\\.minecraft')



