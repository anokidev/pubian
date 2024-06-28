"""

    pubian.core.pipeline_mngr

    Containing the entire pipeline system.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

from pubian.core.pipeline_mngr.addon_mngr import AddonManager
from pubian.core.pipeline_mngr.app_mngr import AppManager
from pubian.core.pipeline_mngr.file_watcher import FileWatcher
from pubian.core.pipeline_mngr.project_mngr import ProjectManager

ProjectMngr: ProjectManager
AppMngr:     AppManager
AddonMngr:   AddonManager
FileWtchr:   FileWatcher

__all__ = [ProjectMngr, AppMngr, AddonMngr, FileWtchr]
