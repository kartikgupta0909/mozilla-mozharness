import os

# OS Specifics
INSTALLER_PATH = os.path.join(os.getcwd(), "installer.dmg")
XPCSHELL_NAME = 'xpcshell'
EXE_SUFFIX = ''
DISABLE_SCREEN_SAVER = False
ADJUST_MOUSE_AND_SCREEN = False
#####
config = {
    "buildbot_json_path": "buildprops.json",
    "exes": {
        'python': '/tools/buildbot/bin/python',
        'virtualenv': ['/tools/buildbot/bin/python', '/tools/misc-python/virtualenv.py'],
    },
    "find_links": [
        "http://pypi.pvt.build.mozilla.org/pub",
        "http://pypi.pub.build.mozilla.org/pub",
    ],
    "pip_index": False,
    ###
    "installer_path": INSTALLER_PATH,
    "xpcshell_name": XPCSHELL_NAME,
    "exe_suffix": EXE_SUFFIX,
    "run_file_names": {
        "mochitest": "runtests.py",
        "webapprt": "runtests.py",
        "reftest": "runreftest.py",
        "xpcshell": "runxpcshelltests.py",
        "cppunittest": "runcppunittests.py",
        "jittest": "jit_test.py",
        "mozbase": "test.py"
    },
    "minimum_tests_zip_dirs": ["bin/*", "certs/*", "modules/*", "mozbase/*", "config/*"],
    "specific_tests_zip_dirs": {
        "mochitest": ["mochitest/*"],
        "webapprt": ["mochitest/*"],
        "reftest": ["reftest/*", "jsreftest/*"],
        "xpcshell": ["xpcshell/*"],
        "cppunittest": ["cppunittests/*"],
        "jittest": ["jit-test/*"],
        "mozbase": ["mozbase/*"]
    },
    # test harness options are located in the gecko tree
    "in_tree_config": "config/mozharness/mac_config.py",
    # local mochi suites
    "all_mochitest_suites": {
        "plain1": ["--total-chunks=5", "--this-chunk=1", "--chunk-by-dir=4"],
        "plain2": ["--total-chunks=5", "--this-chunk=2", "--chunk-by-dir=4"],
        "plain3": ["--total-chunks=5", "--this-chunk=3", "--chunk-by-dir=4"],
        "plain4": ["--total-chunks=5", "--this-chunk=4", "--chunk-by-dir=4"],
        "plain5": ["--total-chunks=5", "--this-chunk=5", "--chunk-by-dir=4"],
        "plain": [],
        "plain-chunked": ["--chunk-by-dir=4"],
        "chrome": ["--chrome"],
        "browser-chrome": ["--browser-chrome"],
        "browser-chrome-1": ["--browser-chrome", "--chunk-by-dir=5", "--total-chunks=3", "--this-chunk=1"],
        "browser-chrome-2": ["--browser-chrome", "--chunk-by-dir=5", "--total-chunks=3", "--this-chunk=2"],
        "browser-chrome-3": ["--browser-chrome", "--chunk-by-dir=5", "--total-chunks=3", "--this-chunk=3"],
        "browser-chrome-chunked": ["--browser-chrome", "--chunk-by-dir=5"],
        "mochitest-gl": ["--manifest=tests/mochitest/tests/dom/canvas/test/webgl-mochitest/mochitest.ini"],
        "mochitest-devtools-chrome": ["--browser-chrome", "--subsuite=devtools"],
        "mochitest-devtools-chrome-1": ["--browser-chrome", "--subsuite=devtools", "--chunk-by-dir=5", "--total-chunks=3", "--this-chunk=1"],
        "mochitest-devtools-chrome-2": ["--browser-chrome", "--subsuite=devtools", "--chunk-by-dir=5", "--total-chunks=3", "--this-chunk=2"],
        "mochitest-devtools-chrome-3": ["--browser-chrome", "--subsuite=devtools", "--chunk-by-dir=5", "--total-chunks=3", "--this-chunk=3"],
        "mochitest-devtools-chrome-chunked": ["--browser-chrome", "--subsuite=devtools", "--chunk-by-dir=5"],
        "jetpack-package": ["--jetpack-package"],
        "jetpack-addon": ["--jetpack-addon"],
        "a11y": ["--a11y"],
        "plugins": ['--setpref=dom.ipc.plugins.enabled=false',
                    '--setpref=dom.ipc.plugins.enabled.x86_64=false',
                    '--ipcplugins']
    },
    # local webapprt suites
    "all_webapprt_suites": {
        "chrome": ["--webapprt-chrome", "--browser-arg=-test-mode"],
        "content": ["--webapprt-content"]
    },
    # local reftest suites
    "all_reftest_suites": {
        "reftest": ["tests/reftest/tests/layout/reftests/reftest.list"],
        "crashtest": ["tests/reftest/tests/testing/crashtest/crashtests.list"],
        "jsreftest": ["--extra-profile-file=tests/jsreftest/tests/user.js", "tests/jsreftest/tests/jstests.list"],
        "reftest-ipc": ['--setpref=browser.tabs.remote=true',
                        '--setpref=browser.tabs.remote.autostart=true',
                        '--setpref=layers.async-pan-zoom.enabled=true',
                        'tests/reftest/tests/layout/reftests/reftest-sanity/reftest.list'],
        "crashtest-ipc": ['--setpref=browser.tabs.remote=true',
                          '--setpref=browser.tabs.remote.autostart=true',
                          '--setpref=layers.async-pan-zoom.enabled=true',
                          'tests/reftest/tests/testing/crashtest/crashtests.list'],
    },
    "all_xpcshell_suites": {
        "xpcshell": ["--manifest=tests/xpcshell/tests/all-test-dirs.list",
                     "%(abs_app_dir)s/" + XPCSHELL_NAME]
    },
    "all_cppunittest_suites": {
        "cppunittest": ['tests/cppunittests']
    },
    "all_jittest_suites": {
        "jittest": []
    },
    "all_mozbase_suites": {
        "mozbase": []
    },
    "run_cmd_checks_enabled": True,
    "preflight_run_cmd_suites": [
        # NOTE 'enabled' is only here while we have unconsolidated configs
        {
            "name": "disable_screen_saver",
            "cmd": ["xset", "s", "off", "s", "reset"],
            "architectures": ["32bit", "64bit"],
            "halt_on_failure": False,
            "enabled": DISABLE_SCREEN_SAVER
        },
        {
            "name": "run mouse & screen adjustment script",
            "cmd": [
                # when configs are consolidated this python path will only show
                # for windows.
                "python", "../scripts/external_tools/mouse_and_screen_resolution.py",
                "--configuration-url",
                "https://hg.mozilla.org/%(branch)s/raw-file/%(revision)s/" +
                    "testing/machine-configuration.json"],
            "architectures": ["32bit"],
            "halt_on_failure": True,
            "enabled": ADJUST_MOUSE_AND_SCREEN
        },
    ],
    "repos": [{"repo": "https://hg.mozilla.org/build/tools"}],
    "vcs_output_timeout": 1000,
    "minidump_stackwalk_path": "%(abs_work_dir)s/tools/breakpad/osx64/minidump_stackwalk",
    "minidump_save_path": "%(abs_work_dir)s/../minidumps",
    "buildbot_max_log_size": 52428800,
    "default_blob_upload_servers": [
        "https://blobupload.elasticbeanstalk.com",
    ],
    "blob_uploader_auth_file": os.path.join(os.getcwd(), "oauth.txt"),
}
