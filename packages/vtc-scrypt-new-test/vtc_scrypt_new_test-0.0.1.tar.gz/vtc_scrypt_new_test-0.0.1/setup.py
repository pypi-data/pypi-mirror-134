from distutils.core import setup, Extension

vtc_scrypt_module = Extension('vtc_scrypt_new',
                              sources=['scryptmodule.c',
                                       'scrypt.c'],
                              include_dirs=['.'],
                              extra_compile_args=['-O3', '-msse3'])

setup(name='vtc_scrypt_new_test',
      version='0.0.1',
      author_email = 'vertion@protonmail.com',
      author = 'vertion',
      url = 'https://github.com/vertiond/vtc-scrypt',
      description='Bindings for scrypt-n proof of work used by Vertcoin',
      ext_modules=[vtc_scrypt_module])
