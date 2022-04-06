# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['youtube_history.py'],
             pathex=[(r'C:\School\cis3296\youtubestats\venv\Lib\site-packages')],
             binaries=[],
             datas=[
                 (r'C:\School\cis3296\youtubestats\data', 'data'), 
                 (r'C:\School\cis3296\youtubestats\data\urls.txt', 'data'),
                 (r'C:\School\cis3296\youtubestats\static', 'static'),
                 (r'C:\School\cis3296\youtubestats\templates', 'templates'),
                 (r'C:\School\cis3296\youtubestats\grapher.py', '.'),
                 (r'C:\School\cis3296\youtubestats\images.png', '.'), 
                 (r'C:\School\cis3296\youtubestats\venv\Lib\site-packages\wordcloud\stopwords', 'wordcloud'), 
                 (r'C:\School\cis3296\youtubestats\venv\Scripts\youtube-dl.exe', '.'),
                 (r'C:\School\cis3296\youtubestats\venv\lib\site-packages\wordcloud\DroidSansMono.ttf', 'wordcloud')
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
