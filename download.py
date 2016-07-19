import os, sys
from shutil import copyfile

def npmInstall(package):
    # Install the npm package
    cmd = 'npm install ' + package
    os.system(cmd)

    # Build the node module for browser
    cwd = os.getcwd()
    try:
        os.chdir(os.path.join(cwd, os.path.join('node_modules', package)))
        print(os.getcwd())
        os.system('npm install')
        buildForBrowser(package, cwd)
    except OSError:
        print("could not find the " + package + " npm package. Please make sure that the package has been downloaded!")
    else :
        os.chdir(os.path.join("..", ".."))


def buildForBrowser(package, rootDir):
    print('Building for Browser')
    os.system('npm run build')
    if os.path.exists(os.path.join(os.getcwd(), 'build')):
        try:
            ''' code to copy the build js bundle to nbextensions directory
                so that script could be loaded while running the notebook
            '''
            src = os.path.join(os.getcwd(), 'build')
            file_names = os.listdir(src)
            dest = os.path.join(rootDir, 'biojs_extensions')
            for name in file_names:
                src_file = os.path.join(src, name)
                dest_file = os.path.join(dest, name)
                copyfile(src_file, dest_file)

        except OSError:
            print('There was some problem while copying '+ package +' module to nbextensions. Please make sure that Jupyter notebook is configured properly')
        else:
            print(package + ' built successfully!')


def install_nbextension():
    os.system('jupyter nbextension install biojs_extensions --user')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in range (1, len(sys.argv)):
            pkg = sys.argv[i]
            npmInstall(pkg)
        install_nbextension()
