from setuptools import setup, find_packages
import pathlib
import subprocess
import distutils.cmd

# current directory
here = pathlib.Path(__file__).parent.resolve()

# version_file = here / 'VERSION'

# Get the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

""" def format_git_describe_version(version):
    if '-' in version:
        splitted = version.split('-')
        tag = splitted[0]
        index = f"dev{splitted[1]}" #{hex(int(splitted[1]))[2:]}"
        # commit = splitted[2] 
        # return f"{tag}.{index}+{commit}"
        return f"{tag}.{index}"
    else:
        return version

def get_version_from_git():
    try:
        process = subprocess.run(["git", "describe"], cwd=str(here), check=True, capture_output=True)
        version = process.stdout.decode('utf-8').strip()
        version = format_git_describe_version(version)
        with version_file.open('w') as f:
            f.write(version)
        return version
    except subprocess.CalledProcessError:
        # with version_file.open('r') as f:
        return version_file.read_text().strip() """

# version = os.popen('git describe').read().strip()
# version = get_version_from_git()

# print(f"Detected version {version} from git describe")

version = '0.4.2'

class GetVersionCommand(distutils.cmd.Command):
  """A custom command to get the current project version inferred from git describe."""

  description = 'gets the project version from git describe'
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    print(version)

setup(
    name='lpaas-client',  # Required
    version=version,
    description='Python implementation of a client for LPaaS',
    license='Apache 2.0 License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/pika-lab/courses/ds/projects/ds-project-evangelisti-ay2021', 
    author='Davide Evangelisti', 
    author_email='davide.evangelisti2@studio.unibo.it',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Prolog'
    ],
    keywords='prolog, client, tuprolog, 2p, python, lpaas',  # Optional
    # package_dir={'': 'src'},  # Optional
    packages=find_packages(exclude=('tests', )),  # Required
    include_package_data=True,
    python_requires='>=3.7, <4',
    install_requires=['2ppy==0.4.0',
                      'httpx~=0.21.1',
                      'http-constants~=0.5',
                      'dataclasses~=0.6',
                      'isodate~=0.6'],
    zip_safe = False,
    platforms = "Independent",
    project_urls={  # Optional
        'Bug Reports': 'https://gitlab.com/pika-lab/courses/ds/projects/ds-project-evangelisti-ay2021/-/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://gitlab.com/pika-lab/courses/ds/projects/ds-project-evangelisti-ay2021',
    },
    cmdclass={
        'get_project_version': GetVersionCommand,
    },
)