# noqa E902
import os
import sys

import pytest


test_pkg = 'xyztraj'
cover_pkg = test_pkg

cwd = os.path.expandvars(os.getcwd())
build_dir = os.getenv('TRAVIS_BUILD_DIR', os.path.expanduser('~'))

# where to write reports
reports_dir = os.path.join(build_dir, 'reports')

# reports
junit_xml = os.path.join(reports_dir, 'junit.xml')
coverage_xml = os.path.join(reports_dir, 'coverage.xml')

print("Current directory: ", cwd)
print("Travis build directory: ", build_dir)
print("Reports directory: ", reports_dir)
print("Reports already exists? ", os.path.exists(reports_dir))

if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)
    print('junit destination:', junit_xml)
    njobs_args = '-p no:xdist' if os.getenv('TRAVIS') else '-n2'

    pytest_args = (
        "-v --pyargs {test_pkg} "
        "--cov={cover_pkg} "
        "--cov-report=xml:{dest_report} "
        "--doctest-modules "
        "{njobs_args} "
        "--junit-xml={junit_xml} "
        "-c {pytest_cfg}"
        #"--durations=20 "
        .format(test_pkg=test_pkg, cover_pkg=cover_pkg,
                junit_xml=junit_xml, pytest_cfg='setup.cfg',
                njobs_args=njobs_args,
                dest_report=coverage_xml
        ).split(' '))

    print("args:", pytest_args)
    #os.chdir(
    res = pytest.main(pytest_args)
    #os.chdir(cwd)

    sys.exit(res)
