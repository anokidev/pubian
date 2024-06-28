"""

    pubian.core.pipeline_mngr.project_mngr

    Containing the manager for a project:
    - Obtaining project configs.

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

import sys
import types
import importlib.util

class ProjectManager:
    """Responsible for managing the project."""

    def _get_project_configs(self) -> types.ModuleType:
        """Obtain a project configuration."""
    
        # Import the configuration.
        spec: types.ModuleSpec | None = importlib.util.spec_from_file_location(
            "project_config", f"{self.cwd}/config.py")
        module: types.ModuleType = importlib.util.module_from_spec(spec)
        sys.modules["project_config"] = module
        spec.loader.exec_module(module)

        # Debug mode.
        try:
            DEBUG_MODE: bool = module.DEBUG_MODE
        except AttributeError:
            DEBUG_MODE: bool = None
        
        # Activated apps.
        try:
            ACTIVATED_APPS: list[str] = module.ACTIVATED_APPS
        except AttributeError:
            ACTIVATED_APPS: list[str] = None

        # Frontware, addons that plays the role of shaping the response.
        try:
            FRONTWARE: list[str] = module.FRONTWARE
        except AttributeError:
            FRONTWARE: list[str] = None

        # Middleware, addons that plays the role of modifying response/request.
        try:
            MIDDLEWARE: list[str] = module.MIDDLEWARE
        except AttributeError:
            MIDDLEWARE: list[str] = None

        # Backware, addons that plays the role of transferring request from outside.
        try:
            BACKWARE: list[str] = module.BACKWARE
        except AttributeError:
            BACKWARE: list[str] = None

        return (
            DEBUG_MODE,
            ACTIVATED_APPS,
            FRONTWARE,
            MIDDLEWARE,
            BACKWARE
        )
