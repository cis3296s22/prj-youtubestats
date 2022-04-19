# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

a = Analysis(['mac_youtube_history.py'],
             pathex=[],
             binaries=[],
             datas=[
                 ('/Users/tyler/Documents/GitHub/youtubestats/data', 'data'), 
                 ('/Users/tyler/Documents/GitHub/youtubestats/static', 'static'),
                 ('/Users/tyler/Documents/GitHub/youtubestats/data/urls.txt', 'data'),
                 ('/Users/tyler/Documents/GitHub/youtubestats/templates', 'templates'),
                 ('/Users/tyler/Documents/GitHub/youtubestats/grapher.py', '.'),
                 ('/Users/tyler/Documents/GitHub/youtubestats/images.png', '.'), 
                 ('/Users/tyler/Documents/GitHub/youtubestats/venv/lib/python3.10/site-packages/wordcloud/stopwords', 'wordcloud'), 
                 ('/Users/tyler/Documents/GitHub/youtubestats/venv/bin/youtube-dl', '.'),
                 ('/Users/tyler/Documents/GitHub/youtubestats/venv/lib/python3.10/site-packages/wordcloud/DroidSansMono.ttf', 'wordcloud')
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
