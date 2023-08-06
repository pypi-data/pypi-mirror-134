import nox

from os import environ as envvar
from subprocess import check_output
from subprocess import Popen
from subprocess import PIPE


PROJECT_NAME = 'sanka'
VENV = f'{PROJECT_NAME}-venv'
TESTDIR = '.'
TESTNAME = envvar.get('TESTNAME', '')
USEVENV = envvar.get('USEVENV', False)
EXAMPLE = envvar.get('EXAMPLE', 'actionpack')

external = False if USEVENV else True
supported_python_versions = [
    '3.6',
    '3.7',
    '3.8',
    '3.9',
    '3.10',
]

nox.options.default_venv_backend = 'none' if not USEVENV else USEVENV

def session_name(suffix: str):
    return f'{VENV}-{suffix}' if USEVENV else suffix


def project_version():
    tags = Popen('git tag'.split(), stdout=PIPE)
    output = check_output('tail -1'.split(), stdin=tags.stdout)
    return output.decode().strip('\n')


def image_name():
    return f'{PROJECT_NAME}:{project_version()}'


@nox.session(name=session_name('image'), python=supported_python_versions)
def image(session):
    command = f'docker build -t {image_name()} --build-arg EXAMPLE={EXAMPLE} .'
    session.run(*command.split(' '))


@nox.session(name=session_name('install'), python=supported_python_versions)
def install(session):
    session.run(
        'python', '-m',
        'pip', '--disable-pip-version-check', 'install', '.',
        external=external
    )
    session.run(
        'python', '-m',
        'pip', '--disable-pip-version-check', 'install', '-r', 'requirements.txt',
        external=external
    )


@nox.session(name=session_name('test'), python=supported_python_versions)
def test(session):
    if USEVENV:
        install(session)

    session.run(
        'python', '-m',
        'coverage', 'run', '--branch',
        '--omit', '.nox/*,noxfile.py,setup.py,test*',
        '--source', '.',
        '-m', 'unittest', TESTNAME if TESTNAME else f'discover',
        external=external
    )
    session.run('coverage', 'report', '-m', external=external)
    session.run('coverage', 'xml', external=external)


@nox.session(name=session_name('build'), python=supported_python_versions)
def build(session):
    session.run('python', 'setup.py', 'sdist')

