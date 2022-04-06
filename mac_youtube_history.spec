# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['mac_youtube_history.py'],
             pathex=[],
             binaries=[],
             datas=[
                 ('/Users/I547137/Documents/GitHub/youtubestats/data', 'data'), 
                 ('/Users/I547137/Documents/GitHub/youtubestats/data/urls.txt', 'data'),
                 ('/Users/I547137/Documents/GitHub/youtubestats/static', 'static'),
                 ('/Users/I547137/Documents/GitHub/youtubestats/templates', 'templates'),
                 ('/Users/I547137/Documents/GitHub/youtubestats/grapher.py', '.'),
                 ('/Users/I547137/Documents/GitHub/youtubestats/images.png', '.'), 
                 ('/Users/I547137/Documents/GitHub/youtubestats/venv/lib/python3.9/site-packages/wordcloud/stopwords', 'wordcloud'), 
                 ('/Users/I547137/Documents/GitHub/youtubestats/venv/bin/youtube-dl', '.'),
                 ('/Users/I547137/Documents/GitHub/youtubestats/venv', 'venv'), 
                 ('/Users/I547137/Documents/GitHub/youtubestats/venv/lib/python3.9/site-packages/wordcloud/DroidSansMono.ttf', 'wordcloud')
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
