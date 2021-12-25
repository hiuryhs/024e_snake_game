# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\hiury\\Dropbox\\Hiury\\06-PYTHON MATERIAL\\02 - 100_days_code_2021_Udemy_Angela_Yu\\024e_snake_game'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='snake_go_up',
          debug=True,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )