# Copyright (c) 2015, Thomas P. Robitaille
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# The code below includes code adapted from WCSAxes, which is released
# under a 3-clause BSD license and can be found here:
#
#   https://github.com/astrofrog/wcsaxes

from functools import wraps

import pytest
import os
import shutil
import tempfile

from matplotlib.testing.compare import compare_images


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption('--mpl', action='store_true',
                    help="Enable comparison of matplotlib figures to reference files")
    group.addoption('--mpl-generate-path',
                    help="directory to generate reference images in", action='store')


def pytest_configure(config):
    if config.getoption("--mpl") or config.getoption("--mpl-generate-path") is not None:
        config.pluginmanager.register(ImageComparison(config))


class ImageComparison(object):

    def __init__(self, config):
        self.config = config

    def pytest_runtest_setup(self, item):

        compare = item.keywords.get('mpl_image_compare')

        if compare is None:
            return

        tolerance = compare.kwargs.get('tolerance', 10)
        savefig_kwargs = compare.kwargs.get('savefig_kwargs', {})

        original = item.function

        @wraps(item.function)
        def item_function_wrapper(*args, **kwargs):

            generate_path = self.config.getoption("--mpl-generate-path")

            # Run test and get figure object
            fig = original(*args, **kwargs)

            # Find test name to use as plot name
            name = original.__name__ + '.png'

            # What we do now depends on whether we are generating the reference
            # images or simply running the test.
            if generate_path is None:

                # Save the figure
                result_dir = tempfile.mkdtemp()
                test_image = os.path.abspath(os.path.join(result_dir, name))

                fig.savefig(test_image, **savefig_kwargs)

                # Find path to baseline image
                baseline_image_ref = os.path.abspath(os.path.join(os.path.dirname(item.fspath.strpath), 'baseline', name))

                if not os.path.exists(baseline_image_ref):
                    raise Exception("""Image file not found for comparison test
                                    Generated Image:
                                    \t{test}
                                    This is expected for new tests.""".format(
                        test=test_image))

                # distutils may put the baseline images in non-accessible places,
                # copy to our tmpdir to be sure to keep them in case of failure
                baseline_image = os.path.abspath(os.path.join(result_dir, 'baseline-' + name))
                shutil.copyfile(baseline_image_ref, baseline_image)

                msg = compare_images(baseline_image, test_image, tol=tolerance)

                if msg is None:
                    shutil.rmtree(result_dir)
                else:
                    raise Exception(msg)

            else:

                if not os.path.exists(generate_path):
                    os.makedirs(generate_path)

                fig.savefig(os.path.abspath(os.path.join(generate_path, name)), **savefig_kwargs)
                pytest.skip("Skipping test, since generating data")

        if item.cls is not None:
            setattr(item.cls, item.function.__name__, item_function_wrapper)

        else:
            item.obj = item_function_wrapper
