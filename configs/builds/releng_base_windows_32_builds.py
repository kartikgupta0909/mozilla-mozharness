import os
import sys

STAGE_USERNAME = 'ffxbld'
STAGE_SSH_KEY = 'ffxbld_dsa'

config = {
    #########################################################################
    ######## WINDOWS GENERIC CONFIG KEYS/VAlUES
    # if you are updating this with custom 32 bit keys/values please add them
    # below under the '32 bit specific' code block otherwise, update in this
    # code block and also make sure this is synced with
    # releng_base_windows_64_builds.py

    'default_actions': [
        'clobber',
        'clone-tools',
        # 'setup-mock', windows do not use mock
        'build',
        'sendchanges',
        'generate-build-stats',
        'update',  # decided by query_is_nightly()
    ],
    "buildbot_json_path": "buildprops.json",
    'exes': {
        'python2.7': sys.executable,
        'hgtool.py': [
            sys.executable,
            os.path.join(
                os.getcwd(), 'build', 'tools', 'buildfarm', 'utils', 'hgtool.py'
            )
        ],
        "buildbot": [
            sys.executable,
            'c:\\mozilla-build\\buildbotve\\scripts\\buildbot'
        ],
        "make": [
            sys.executable,
            os.path.join(
                os.getcwd(), 'build', 'src', 'build', 'pymake', 'make.py'
            )
        ]
    },
    'app_ini_path': '%(obj_dir)s/dist/bin/application.ini',
    # decides whether we want to use moz_sign_cmd in env
    'enable_signing': True,
    'purge_skip': ['info', 'rel-*:45d', 'tb-rel-*:45d'],
    'purge_basedirs':  [],
    'enable_ccache': False,
    'vcs_share_base': 'C:/builds/hg-shared',
    'objdir': 'obj-firefox',
    'tooltool_script': [sys.executable,
                        'C:/mozilla-build/tooltool.py'],
    'tooltool_bootstrap': "setup.sh",
    'enable_count_ctors': False,
    'enable_talos_sendchange': True,
    'enable_unittest_sendchange': True,
    'platform_supports_partials': True,
    #########################################################################


     #########################################################################
     ###### 32 bit specific ######
    'base_name': 'WINNT_5.2_%(branch)s',
    'platform': 'win32',
    'stage_platform': 'win32',
    'enable_max_vsize': True,
    'env': {
        'MOZBUILD_STATE_PATH': os.path.join(os.getcwd(), '.mozbuild'),
        'MOZ_AUTOMATION': '1',
        'BINSCOPE': 'C:/Program Files (x86)/Microsoft/SDL BinScope/BinScope.exe',
        'HG_SHARE_BASE_DIR': 'C:/builds/hg-shared',
        'MOZ_CRASHREPORTER_NO_REPORT': '1',
        'MOZ_OBJDIR': 'obj-firefox',
        'PATH': 'C:/mozilla-build/nsis-3.0a2;C:/mozilla-build/nsis-2.46u;C:/mozilla-build/python27;'
                'C:/mozilla-build/buildbotve/scripts;'
                '%s' % (os.environ.get('path')),
        'PDBSTR_PATH': '/c/Program Files (x86)/Windows Kits/8.0/Debuggers/x64/srcsrv/pdbstr.exe',
        'PROPERTIES_FILE': os.path.join(os.getcwd(), 'buildprops.json'),
        # SYMBOL_SERVER_HOST is dictated from build_pool_specifics.py
        'SYMBOL_SERVER_HOST': '%(symbol_server_host)s',
        'SYMBOL_SERVER_SSH_KEY': '/c/Users/cltbld/.ssh/ffxbld_dsa',
        'SYMBOL_SERVER_USER': 'ffxbld',
        'SYMBOL_SERVER_PATH': '/mnt/netapp/breakpad/symbols_ffx/',
        'POST_SYMBOL_UPLOAD_CMD': '/usr/local/bin/post-symbol-upload.py',
        'TINDERBOX_OUTPUT': '1',
    },
    'upload_env': {
        # UPLOAD_HOST is set to stage_server
        # stage_server is dictated from build_pool_specifics.py
        'UPLOAD_USER': STAGE_USERNAME,
        'UPLOAD_TO_TEMP': '1',
        'UPLOAD_SSH_KEY': '~/.ssh/%s' % (STAGE_SSH_KEY,),
    },
    "check_test_env": {
        'MINIDUMP_STACKWALK': '%(abs_tools_dir)s/breakpad/win32/minidump_stackwalk.exe',
        'MINIDUMP_SAVE_PATH': '%(base_work_dir)s/minidumps',
    },
    'purge_minsize': 12,
    'src_mozconfig': 'browser/config/mozconfigs/win32/nightly',
    'tooltool_manifest_src': "browser/config/tooltool-manifests/win32/releng.manifest",
    'platform_ftp_name': 'win32.complete.mar',
    #########################################################################
}
