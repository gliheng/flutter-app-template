import os
import subprocess
from shutil import copy, copyfile, copytree, rmtree
from . import tmpl_file

def prepare(envs):
    envs = dict(envs)
    SNAP_DIR = os.path.join(envs['OUTPUT_DIR'], 'snap')
    envs.update(
      SNAP_DIR = SNAP_DIR,
    )
    return envs

def tmpl_config(envs):
    return {
        'name': envs['NAME'],
        'version': envs['VERSION'],
        'description': envs['DESCRIPTION'],
        'summary': 'Flutter application built with flutter-rs',
    }

def collect(envs):
  snap_dir = envs['SNAP_DIR']
  files_dir = os.path.join(snap_dir, 'files')
  os.makedirs(files_dir, exist_ok = True)

  bin = os.path.join(envs['TARGET_DIR'], 'debug' if envs['DEBUG'] else 'release' , envs['NAME'])

  # flutter app files
  copy(bin, files_dir)
  # subprocess.run(['chmod', '+x', os.path.join(files_dir, envs['NAME'])], check = True)
  copy(os.path.join(envs['WORKSPACE_TARGET_DIR'] or envs['TARGET_DIR'], 'flutter-engine', envs['FLUTTER_LIB_VER'], 'libflutter_engine.so'), files_dir)
  copy(os.path.join(envs['RUST_ASSETS_DIR'], 'icon.ico'), files_dir)
  copy(os.path.join(envs['RUST_ASSETS_DIR'], 'icudtl.dat'), files_dir)

  dest = os.path.join(files_dir, 'flutter_assets')
  if os.path.exists(dest):
    rmtree(dest)
  copytree(envs['FLUTTER_ASSETS'], dest)

  config = tmpl_config(envs)

  # snap build files
  file = os.path.join(os.path.dirname(__file__), 'snapcraft.yaml')
  dest = os.path.join(snap_dir, 'snapcraft.yaml')
  copyfile(file, dest)
  tmpl_file(dest, config)

  file = os.path.join(os.path.dirname(__file__), 'app.desktop')
  desktop_file_name = envs['NAME'] + '.desktop'
  desktop_dir = os.path.join(files_dir, 'usr/share/applications')
  os.makedirs(desktop_dir, exist_ok = True)
  dest = os.path.join(desktop_dir, desktop_file_name)
  copyfile(file, dest)
  tmpl_file(dest, config)

def build(envs):
    collect(envs)
    fn = '{}_{}.snap'.format(envs['NAME'], envs['VERSION'])
    output = os.path.join(
        envs['SNAP_DIR'],
        fn,
    )
    subprocess.run(['snapcraft', 'snap', '-o', fn], cwd = envs['SNAP_DIR'], check = True)
    return output


