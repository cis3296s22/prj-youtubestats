# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['youtube_history.py'],
             pathex=[(r'D:\School\CIS3296\youtubestats\venv\Lib\site-packages')],
             binaries=[],
             datas=[
                 (r'D:\School\CIS3296\youtubestats\data', 'data'), 
                 (r'D:\School\CIS3296\youtubestats\data\ran', 'data'), 
                 (r'D:\School\CIS3296\youtubestats\data\raw', 'data'), 
                 (r'D:\School\CIS3296\youtubestats\data\urls.txt', 'data'),
                 (r'D:\School\CIS3296\youtubestats\static', 'static'),
                 (r'D:\School\CIS3296\youtubestats\templates', 'templates'),
                 (r'D:\School\CIS3296\youtubestats\grapher.py', '.'),
                 (r'D:\School\CIS3296\youtubestats\images.png', '.'), 
                 (r'D:\School\CIS3296\youtubestats\venv\Lib\site-packages\wordcloud\stopwords', 'wordcloud'), 
                 (r'D:\School\CIS3296\youtubestats\venv\Scripts\youtube-dl.exe', '.'),
                 (r'D:\School\CIS3296\youtubestats\venv\lib\site-packages\wordcloud\DroidSansMono.ttf', 'wordcloud')
             ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='youtube_history',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='youtube_history')
