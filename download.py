import os, sys

def npmInstall(package):
    # Install the npm package
    cmd = 'npm install ' + package
    os.system(cmd)

    # Build the node module for browser
    cwd = os.getcwd()
    print(cwd)
    try:
        os.chdir(os.path.join(cwd, os.path.join('node_modules', package)))
        print(os.getcwd())
        os.system('npm install')
        buildForBrowser()
    except OSError:
        print("could not find the " + package + " npm package. Please make sure that the package has been downloaded!")
    else :
        os.chdir(os.path.join("..", ".."))


def buildForBrowser():
    print('Building for Browser')
    os.system('npm run build')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for i in range (1, len(sys.argv)):
            pkg = sys.argv[i]
            npmInstall(pkg)
