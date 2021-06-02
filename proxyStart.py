from client.client import Config
import proxy



g = Config()

proxy.main([
    '--hostname', '0.0.0.0', '--port',
    str(g.info['port']), '--basic-auth', 'arknights:ghYDmaf00HiP'
    ])
