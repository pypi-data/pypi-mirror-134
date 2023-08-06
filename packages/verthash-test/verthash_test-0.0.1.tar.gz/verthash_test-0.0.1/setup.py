from setuptools import setup, Extension

verthashsources = [
	'h2.c',
       'tiny_sha3/sha3.c'
]

verthashincludes = [
	'.', 
	'./tiny_sha3'
]

verthash_module = Extension('verthash',
                            sources=verthashsources+['verthashmodule.c'],
                            extra_compile_args=['-std=c99'],
                            include_dirs=verthashincludes)

setup(name = 'verthash_test',
      version = '0.0.1',
      author_email = 'vertion@protonmail.com',
      author = 'vertion',
      url = 'https://github.com/vertiond/lyra2re-hash-python',
      description = 'Python bindings for Verthash proof of work function',
      ext_modules = [verthash_module])
