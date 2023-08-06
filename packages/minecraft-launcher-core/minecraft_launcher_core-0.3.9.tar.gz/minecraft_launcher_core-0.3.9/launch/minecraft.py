import json
import os
import sys
import zipfile


class Minecraft:
    def __init__(self,path):
        self.json_file = os.path.join(path,path.split('\\')[-1]+'.json')




        with open(self.json_file) as f:
            self.json_dict = json.load(f)



        self.minecraft_version = self.json_dict['id']

        self.libraries = []

        self.libraries_str = []
        self.arguments = ''
        self.path = path
        self.name = self.path.split('\\')[-1]

        for i in self.json_dict["libraries"]:
            apth = i['name'].replace(':', '\\').split('\\')
            self.libraries.append(apth)

        for i in self.libraries:
            i[0] = i[0].replace('.', '\\')
            text = f'{i[0]}\\{i[1]}\\{i[2]}\\{i[1]}-{i[2]}.jar'
            self.libraries_str.append(text)




        try:
            for i in self.json_dict['arguments']['game']:
                if i.__class__.__name__ == 'str':
                    self.arguments += i + ' '

            self.arguments += "--width ${resolution_width} --height ${resolution_height}"

        except BaseException as e:

            self.arguments = self.json_dict['minecraftArguments'] + "--width ${resolution_width} --height ${resolution_height}"
    def unzip(self,jar_file):
        zipf = zipfile.ZipFile(jar_file)
        namelist = zipf.namelist()
        try:
            os.mkdir(f'{self.path}\\{self.name}-natives\\')
        except BaseException as e:
            pass
        for i in namelist:
            if i.endswith('.dll'):
                zipf.extract(i, f'{self.path}\\{self.name}-natives\\')


    def launch(self,uuid='${uuid}',access_token='${access_token}',size=[854,480],memorym=128,memoryx=1024,username='test',java=r'java',launcher=['unknow_launcher','001'],is_ent=False):
        lib = f'{self.path}\\{self.name}-natives\\'
        lib_path = self.path.replace(self.name,'').replace('\\versions','')+'libraries'
        new_lib = []
        jvm = f'-XX:+UseG1GC -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow -Dfml.ignoreInvalidMinecraftCertificates=True -Dfml.ignorePatchDiscrepancies=True -Dlog4j2.formatMsgNoLookups=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Dos.name="Windows 10" -Dos.version=10.0 -Djava.library.path="{lib[:-1]}" -Dminecraft.launcher.brand={launcher[0]} -Dminecraft.launcher.version={launcher[1]}'
        for i in self.libraries_str:
            new_lib.append(os.path.join(lib_path,i))

        for i in new_lib:
            try:
                with open(i.replace('.jar', '') + '-natives-windows.jar') as f:
                    self.unzip(i.replace('.jar', '') + '-natives-windows.jar')
            except BaseException as e:
                pass

        cp = '-cp "'
        for i in new_lib:
            if i.split('\\')[-2] == '3.2.1':
                pass
            else:
                cp += i + ';'


        jar_file = f'{self.path}\\{self.name}.jar'




        cp += f'{jar_file}"'

        arguments = self.arguments
        arguments = arguments.replace('${auth_player_name}',username)
        arguments = arguments.replace('${version_name}',self.minecraft_version)
        if is_ent:

            arguments = arguments.replace('${game_directory}', self.path)
        else:
            dw = '\\versions\\'+self.name
            arguments = arguments.replace('${game_directory}', f'"{self.path.replace(dw,"")}"')
        dw = '\\versions\\' + self.name
        arguments = arguments.replace('${assets_root}',f'"{self.path.replace(dw,"")}\\assets"')
        arguments = arguments.replace('${game_assets}', f'"{self.path.replace(dw,"")}\\assets"')
        try:

            arguments = arguments.replace('${assets_index_name}',self.json_dict['assets'])



        except BaseException as e:
            print(e)
        arguments = arguments.replace('${auth_uuid}',uuid)
        arguments = arguments.replace('${auth_access_token}',access_token)
        arguments = arguments.replace('${user_type}','Mojang')
        arguments = arguments.replace('${resolution_width}', str(size[0]))
        arguments = arguments.replace('${resolution_height}', str(size[1]))
        arguments = arguments.replace("${version_type}",str(launcher[0]))

        arguments = f'-Xmn{memorym}m -Xmx{memoryx}m {self.json_dict["mainClass"]} '+arguments

        command = java + ' ' + jvm + ' ' + cp + ' ' + arguments

        dw = '\\versions\\' + self.name
        print(command)
        os.chdir(self.path)
        os.system(command)


