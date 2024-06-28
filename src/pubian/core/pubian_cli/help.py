"""

    pubian.core.pubian_cli.help

    For command: pubian help / pubian -h / pubian --help

    Copyright (c) 2023 Anoki Youssou,
    all right reserved. Licensed in
    MIT License.

"""

HELP = """

pubian init [project-name] [flags]
    
    Use this command to initialize new projects.

    A setup will be initialized to ask whether you want an app 
    project or an addon project. It will also ask whether you 
    want to use a template. You can use '--template' to specify 
    which template do you want to use (must be a Git repository
    archive).  

pubian app [option] [myapp] [flags]

    Use this command to manage, run, and check your application.

    > pubian app scaffold [myapp] = Scaffold a new app by using a guided setup.
        ~ --instruction=[instruction] : Provide an instruction.
    > pubian app exec [myapp]     = Execute your app, aka run your app.
        ~ --debug   : Debug mode on.
        ~ --default : Use default configs.
    > pubian app run [task]       = Run a task, provided by an addon, to your app.
    > pubian app test [myapp]     = Test your app with e2e or unit testing tools.

pubian addon [option] [myaddon] [flags]

    Use this command to manage, run, and check your addons.

    > pubian addon scaffold [myaddon] = Scaffold a new addon.
    > pubian addon test [myaddon]     = Test your addon.

pubian help / pubian --help / pubian -h

    Use this command to show this message.

pubian version / pubian --version / pubian -v

    Use this command to show version.

"""
