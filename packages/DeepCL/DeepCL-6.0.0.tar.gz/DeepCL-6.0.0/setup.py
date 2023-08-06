# Copyright Hugh Perkins 2015 hughperkins at gmail
#
# This Source Code Form is subject to the terms of the Mozilla Public License, 
# v. 2.0. If a copy of the MPL was not distributed with this file, You can 
# obtain one at http://mozilla.org/MPL/2.0/.

#from distutils.core import setup
import os
import os.path
import sysconfig
import sys
import glob
import platform
from setuptools import setup
#from distutils.extension import Extension
from setuptools import Extension
import distutils.dir_util
import distutils.file_util

cython_present = False
try:
    from Cython.Build import cythonize
    cython_present = True
except ImportError:
    pass

pypandoc_present = False
try:
    import pypandoc
    pypandoc_present = True
except ImportError:
    pass

#print ( sys.argv )
# if any of sys.argv is bdist or sdist or bdist_egg, then lets copy everything to
# a subfolder of us called 'mysrc', since '..' paths dont work well..
# otherwise, let's just assume this folder already contains our source :-)
docopy = False
for arg in sys.argv:
    if arg in ('sdist','bdist','bdist_egg','build_ext'):
        docopy = True

srcdirs = ['lua', 'activate','batch','clmath','conv','dropout','fc','forcebackprop',
    'input','layer','loaders','loss','net','netdef','normalize','patches',
    'pooling','trainers','util','weights', 'qlearning' ]

if docopy:
    if not os.path.isdir('mysrc'):
        os.makedirs('mysrc')
    if not os.path.isdir('mysrc/util'):
        os.makedirs('mysrc/util')
    if not os.path.isdir('mysrc/templates'):
        os.makedirs('mysrc/templates')
    if not os.path.isdir('mysrc/lua'):
        os.makedirs('mysrc/lua')
    for thisdir in ['../src','../EasyCL',
            '../EasyCL/thirdparty/clew/src']: # copy everything..
        for thisfile in os.listdir(thisdir):
            #print(thisfile)
            thisfilepath = thisdir +'/' + thisfile
            if os.path.isfile(thisfilepath):
                distutils.file_util.copy_file( thisfilepath, 'mysrc/' + thisfile )
    for thisdir in ['../EasyCL/util']:
        for thisfile in os.listdir(thisdir):
            #print(thisfile)
            thisfilepath = thisdir +'/' + thisfile
            if os.path.isfile(thisfilepath):
                distutils.file_util.copy_file( thisfilepath, 'mysrc/util/' + thisfile )
    for thisdir in ['../EasyCL/thirdparty/lua-5.1.5/src']:
        for thisfile in os.listdir(thisdir):
            #print(thisfile)
            thisfilepath = thisdir +'/' + thisfile
            if os.path.isfile(thisfilepath):
                distutils.file_util.copy_file( thisfilepath, 'mysrc/lua/' + thisfile )
    distutils.file_util.copy_file('../EasyCL/thirdparty/lua-5.1.5/files.txt', 'mysrc/lua/files.txt')
    for thisdir in ['../EasyCL/templates']:
        for thisfile in os.listdir(thisdir):
            #print(thisfile)
            thisfilepath = thisdir +'/' + thisfile
            if os.path.isfile(thisfilepath):
                distutils.file_util.copy_file( thisfilepath, 'mysrc/templates/' + thisfile )
    distutils.file_util.copy_file( '../jenkins/version.txt', 'version.txt' )
    for srcdir in srcdirs:
        if srcdir == 'lua':
            continue
        if not os.path.isdir('mysrc/' + srcdir):
            os.makedirs('mysrc/' + srcdir)
        for thisfile in os.listdir('../src/' + srcdir):
            thisfilepath = '../src/' + srcdir +'/' + thisfile
            if os.path.isfile(thisfilepath):
                distutils.file_util.copy_file( thisfilepath, 'mysrc/' + srcdir + '/' + thisfile )

#        distutils.dir_util.copy_tree( thisdir, 'mysrc' )

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_so_suffix():
    if sysconfig.get_config_var('SOABI') != None:
        return "." + sysconfig.get_config_var('SOABI')
    return ""

if pypandoc_present:
    pypandoc.convert('README.md', 'rst', outputfile = 'README.rst' )

def my_cythonize(extensions, **_ignore):
    #newextensions = []
    for extension in extensions:
        print(extension.sources)
        should_cythonize = False
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in ('.pyx', '.py'):
                should_cythonize = True
                if not cython_present:
                   # if extension.language == 'c++':
                        ext = '.cpp'
                    #else:
                     #   ext = '.c'
            if sfile == 'PyDeepCL.c':
                ext = '.cpp' # hack for now... not sure how to fix this cleanly
                             # yet
            sfile = path + ext
            if sfile.startswith('..'):
                # use mysrc instead
                basename = os.path.basename(sfile)
                sfile = 'mysrc/' + basename
            sources.append(sfile)
        #print(should_cythonize)
        if should_cythonize and cython_present:
            print('cythonizing...')
            cythonize(extension)
        extension.sources[:] = sources    
        #newextensions.append( extension )
    return extensions

def no_cythonize(extensions, **_ignore):
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            #print('path,ext',path,ext)
            if ext in ('.pyx', '.py'):
                #if extension.language == 'c++':
                    ext = '.cpp'
                #else:
                #    ext = '.c'
            if sfile == 'PyDeepCL.c':
                ext = '.cpp' # hack for now... not sure how to fix this cleanly
                             # yet
            sfile = path + ext
            if sfile.startswith('..'):
                # use mysrc instead
                basename = os.path.basename(sfile)
                sfile = 'mysrc/' + basename
            sources.append(sfile)
            print('appending source ', sfile )
        extension.sources[:] = sources    
    return extensions

# from http://stackoverflow.com/questions/14320220/testing-python-c-libraries-get-build-path
def distutils_dir_name(dname):
    """Returns the name of a distutils build directory"""
    f = "{dirname}.{platform}-{version[0]}.{version[1]}"
    return f.format(dirname=dname,
                    platform=sysconfig.get_platform(),
                    version=sys.version_info)
 
def lib_build_dir():
    return os.path.join('build', distutils_dir_name('lib'))

deepcl_sources = []
for srcdir in srcdirs:
    filespath = 'mysrc/' + srcdir + '/files.txt'
    fileslist = []
    with open( filespath, 'r' ) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() != "":
                fileslist.append( 'mysrc/' + srcdir + '/' + line.strip() )
#    print('fileslist: ', fileslist)
    deepcl_sources = deepcl_sources + fileslist
print('deeplcl_sources', deepcl_sources)
#for source in deepcl_sources_all:
#    deepcl_sources.append(source)

easyclsources = list(map( lambda name : 'mysrc/' + name, [
        'EasyCL.cpp',
        'deviceinfo_helper.cpp', 'platforminfo_helper.cpp',
         'templates/LuaTemplater.cpp',
        'util/easycl_stringhelper.cpp', 'templates/TemplatedKernel.cpp',
#        'EasyCL/speedtemplates/SpeedTemplates.cpp',
        'CLWrapper.cpp',
        'CLKernel.cpp', 'clew.c' ] ))
print(easyclsources)
print(isinstance( easyclsources, list) )

compile_options = []
osfamily = platform.uname()[0]
if osfamily == 'Windows':
   compile_options.append('/EHsc')
elif osfamily == 'Linux':
   compile_options.append('-std=c++0x')
   compile_options.append('-g')
else:
   pass
   # put other options etc here if necessary

runtime_library_dirs = []
libraries = []
if osfamily == 'Linux':
    runtime_library_dirs= ['.']

if osfamily == 'Windows':
    libraries = ['winmm']

if cython_present:
    my_cythonize = cythonize
else:
    my_cythonize = no_cythonize

#libraries = [
#    ("EasyCL", {
#        'sources': easyclsources + ['dummy_easycl.cpp'],
#        'include_dirs': ['DeepCL/EasyCL'],
#        'extra_compile_args': compile_options,
##        define_macros = [('EasyCL_EXPORTS',1)],
##        libraries = []
##        language='c++'
#        }
#    )
#]

ext_modules = [
#    Extension("_EasyCL",
#        sources = easyclsources + ['dummy_easycl.cpp'],
#        include_dirs = ['DeepCL/EasyCL'],
#        extra_compile_args=compile_options,
#        define_macros = [('EasyCL_EXPORTS',1),('MS_WIN32',1)],
##        libraries = []
##        language='c++'
#    )
#    Extension("libDeepCL",
#        list(map( lambda name : 'DeepCL/src/' + name, deepcl_sources)), # +
##            glob.glob('DeepCL/src/*.h'),
#        include_dirs = ['DeepCL/src','DeepCL/EasyCL'],
#        extra_compile_args = compile_options,
#        library_dirs = [ lib_build_dir() ],
#        libraries = [ "EasyCL" + get_so_suffix() ],
#        define_macros = [('DeepCL_EXPORTS',1)],
#        runtime_library_dirs=runtime_library_dirs
##        language='c++'
#    ),
    Extension("PyDeepCL",
              sources=["PyDeepCL.pyx", 'CyWrappers.cpp'] 
                + easyclsources
                + deepcl_sources, 
#                glob.glob('DeepCL/EasyCL/*.h'),
              include_dirs = ['mysrc', 'mysrc/lua'],
              libraries= libraries,
              extra_compile_args=compile_options,
        define_macros = [('DeepCL_EXPORTS',1),('EasyCL_EXPORTS',1)],
#              extra_objects=['cDeepCL.pxd'],
#              library_dirs = [lib_build_dir()],
              runtime_library_dirs=runtime_library_dirs,
              language="c++"
    )
]

def read_if_exists(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.isfile(filepath):
        return open(filepath).read()
    else:
        ""

version = read_if_exists('version.txt').strip().replace('v', '')
print('version: ', version )

setup(
  name = 'DeepCL',
  version = version,
#  version = "3.4.0rc1",  # synchronize to deepcl main version
  author = "Hugh Perkins",
  author_email = "hughperkins@gmail.com",
  description = 'python wrapper for DeepCL deep convolutional neural network library for OpenCL',
  license = 'MPL',
  url = 'https://github.com/hughperkins/DeepCL',
  long_description = read('README.rst'),
  classifiers = [
    'Development Status :: 4 - Beta',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
  ],
  install_requires = [],
  # install_requires = [],
  tests_require = ['nose>=1.3.4','Cython>=0.22','cogapp>=2.4','future>=0.14.3'],
  scripts = ['test_deepcl.py','test_lowlevel.py'],
 # modules = libraries,
#  lib raries = libraries,
  ext_modules = my_cythonize( ext_modules),
)

