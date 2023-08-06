

import json,os,threading
try:
    from file import File
except BaseException:
    pass
try:
    from format import Format
except BaseException:
    pass
try:
    from .file import File
    from .format import Format
except BaseException:
    pass

class server:
    def __init__(self,version):
        self.version = version
    def load(self):
        try:

            os.mkdir(r'C:\Users\Default\AppData\Roaming\.mcl')
        except BaseException as e:
            pass
        self.basepath = r'C:\Users\Default\AppData\Roaming\.mcl'
        File('https://launchermeta.mojang.com/mc/game/version_manifest.json',self.basepath+'\\versions.json')

        with open(self.basepath+'\\versions.json') as f:
            self.content = f.read()

        for i in eval(self.content)['versions']:
            if i['id'] == self.version:
                self.dic = i

                return
        raise SystemError(''
                          'This version does not exist.')
    def download_server_core_jar(self,dir):
        File(self.dic['url'], dir + '\\server.json')
        self.ser = json.load(open(dir + '\\server.json'))
        while True:

            try:

                File(self.ser['downloads']['server']['url'],dir+'\\server.jar')
                break
            except BaseException as e:
                print(e)
                continue

    def setting_default(self,di):
        with open(di+'\\eula.txt','w') as f:
            f.write('eula=true')
        with open(di+'\\server.properties','a') as f:
            f.write('')
        self.setting_add(di, 'allow-flight', 'false')
        self.setting_add(di, 'allow-nether', 'true')
        self.setting_add(di, 'broadcast-console-to-ops', 'true')
        self.setting_add(di, 'broadcast-rcon-to-ops', 'true')
        self.setting_add(di, 'difficulty', 'peaceful')
        self.setting_add(di, 'enable-command-block', 'false')
        self.setting_add(di, 'enable-jmx-monitoring', 'false')
        self.setting_add(di, 'enable-query', 'false')
        self.setting_add(di, 'enable-rcon', 'false')
        self.setting_add(di, 'enable-status', 'true')
        self.setting_add(di, 'enforce-whitelist', 'false')
        self.setting_add(di, 'entity-broadcast-range-percentage', '100')
        self.setting_add(di, 'force-gamemode', 'false')
        self.setting_add(di, 'function-permission-level', '2')
        self.setting_add(di, 'gamemode', 'survival')
        self.setting_add(di, 'generate-structures', 'true')
        self.setting_add(di, 'generator-settings', '')
        self.setting_add(di, 'hardcore', 'false')
        self.setting_add(di, 'hide-online-players', 'false')
        self.setting_add(di, 'level-name', 'world')
        self.setting_add(di, 'level-seed', '')
        self.setting_add(di, 'level-type', 'default')
        self.setting_add(di, 'max-build-height', '256')
        self.setting_add(di, 'max-players', '20')
        self.setting_add(di, 'max-tick-time', '60000')
        self.setting_add(di, 'max-world-size', '29999984')
        self.setting_add(di, 'motd', 'A minecraft server')
        self.setting_add(di, 'network-compression-threshold', '256')
        self.setting_add(di, 'online-mode', 'true')
        self.setting_add(di, 'op-permission-level', '4')
        self.setting_add(di, 'player-idle-timeout', '0')
        self.setting_add(di, 'prevent-proxy-connections', 'false')
        self.setting_add(di, 'pvp', 'true')
        self.setting_add(di, 'query.port', '25565')
        self.setting_add(di, 'rate-limit', '0')
        self.setting_add(di, 'rcon.password', '')
        self.setting_add(di, 'rcon.port', '25575')
        self.setting_add(di, 'require-resource-pack', 'false')
        self.setting_add(di, 'resource-pack', '')
        self.setting_add(di, 'resource-pack-prompt', '')
        self.setting_add(di, 'resource-pack-sha1', '')
        self.setting_add(di, 'server-ip', '')
        self.setting_add(di, 'server-port', '25565')
        self.setting_add(di, 'spawn-animals', 'true')
        self.setting_add(di, 'spawn-monsters', 'true')
        self.setting_add(di, 'spawn-npcs', 'true')
        self.setting_add(di, 'spawn-protection', '16')
        self.setting_add(di, 'sync-chunk-writes', 'true')
        self.setting_add(di, 'use-native-transport', 'true')
        self.setting_add(di, 'view-distance', '10')
        self.setting_add(di, 'white-list', 'false')

    def setting_add(self,dir,a,b):
        with open(dir+'\\server.properties') as f:
            self.d = f.read()


        self.format = Format()
        ad = self.format.decode(self.d)

        ad[a] = b



        final = self.format.encode(ad)

        with open(dir+'\\server.properties','w') as f:
            f.write(final)
    def start_thread(self,java,di):
        server_thread = threading.Thread(target=self.start,args=[java,di])
        server_thread.start()
        server_thread.join()

    def start(self,java,di):
        os.chdir(di)
        jar_path = di+'\\server.jar'
        os.system(f'{java} -jar {jar_path}')
    def main(self,dir,java):
        self.load()
        self.download_server_core_jar(dir)
        self.setting_default(dir)
        self.start_thread(java,dir)


if __name__ == '__main__':
    a = server('1.7.10')
    a.load()
    a.download_server_core_jar("D:\\test")
    a.setting_default("D:\\test")

    a.start('java',"D:\\test")





