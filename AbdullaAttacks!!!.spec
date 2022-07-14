# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['AbdullaAttacks!!!.py'],
    pathex=[],
    binaries=[],
    datas=[('images/abdulla.png','images'),('images/background.png','images'),('images/farmer.png','images'),('images/icon.png','images'),('images/ketmon.png','images'),('images/play_button.png','images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AbdullaAttacks!!!',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
