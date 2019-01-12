# -*- mode: python -*-

block_cipher = None


a = Analysis([
                'supervisor/supervisord.py',
                'supervisor/web.py',
             ],
             pathex=[
                'C:\\Users\\eric\\source\\repos\\supervisor\\supervisor',
             ],
             binaries=[],
             datas=[
                ('supervisord.bat', '.'),
                ('supervisord.conf', '.'),
                ('supervisor/version.txt', '.'),
                ('supervisor/version.txt', 'supervisor'),
             ],
             hiddenimports=[
                'supervisor_twiddler.rpcinterface',
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='supervisord',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='supervisord')
