"""This module provides the CLI."""
import os
import typer
import shutil
from typing import List
from pathlib import Path
from typing import Optional

from workon import __version__
from workon import __app_name__
from workon.database import Database as DB
from workon import (DB_WRITE_ERROR, DB_READ_ERROR, DB_DELETE_ERROR)

app = typer.Typer()

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))

DATABASE = DB( os.path.join("workon","projects.db"))

def _get_version(value: bool) -> None:
    """Return the version of the application"""
    
    if value:

        typer.echo(f"{__app_name__} {__version__}")

        raise typer.Exit()

def get_projects() -> List[str]:
    """This function is to get the projects from the database"""
    
    data = DATABASE.get_projects()

    return data

@app.command()
def show(version: Optional[bool] = typer.Option(
    None,
    "--show",
    "-s",
    help = "Show all the current projects",
    )) -> None:
    """This function shows you all the current projects"""

    response = get_projects()   

    if response.error == DB_READ_ERROR:

        typer.echo("Error reading the database")

        raise typer.Abort()
    
    else:

        if response.data:

            typer.echo("Current projects:\n")

            for index, project in enumerate(response.data[0]):

                typer.echo(f"{index + 1}.- {project}")
        
        else:

            typer.echo("There are no projects yet")

@app.command()
def create(project: str = typer.Argument(..., help = "The name of the project to create and virtualenv"),
            python: Optional[str] = typer.Option('3.9',
                                                "--python",
                                                "-p", 
                                                help = "The python version to use"),    
            directory: Optional[str] = typer.Option("Desktop",
                                                    "--directory",
                                                    "-d",
                                                    help = "The directory to work on, the default is the Desktop directory plus the project name"),
            ) -> str:

    """This function creates a new project command"""

    response = get_projects()

    if response.error == DB_READ_ERROR:

        typer.echo("Error reading the database")

        raise typer.Abort()
    
    else:

        check_exists = lambda row: row[0] == project

        validate = list(filter(check_exists, response.data))

        if not any(validate):
    
            try:

                path_to_work = os.path.join(os.environ["HOMEPATH"], directory, project)

                os.system(f"conda create --name {project} python={python}")
                
                os.mkdir(path_to_work)
            
                response = DATABASE.add_project(path_to_work, project, python)

                if response.error == DB_WRITE_ERROR:

                    typer.echo(f"Error: {DB_WRITE_ERROR}")
                
                else:

                    typer.echo(f"Project {project} created successfully")
            
            except:

                typer.echo(f"Error: Project {project} already exists")
        
        else:

            typer.echo(f"Error: Project {project} already exists")
    
@app.command()
def workon(project: str = typer.Argument(..., help = "The name of the project to work on"),
           ) -> str:

    """This function start vscode, open de project and activate the virtualenv"""

    response = DATABASE.call_project(project)
    
    if response.error == DB_READ_ERROR:

        typer.echo(f"Error: {DB_READ_ERROR}")
    
    else:

        if response.data:

            if response.data[0] == project:

                workin_dir = response.data[1]

                env = response.data[-1]

                os.chdir(workin_dir)

                os.system(f"start {workin_dir} | code {workin_dir} | conda activate {env}")
                           
        else:

            typer.echo(f"Error: Project {project} does not exist")

@app.command()
def remove(project: str = typer.Argument(..., help = "The name of the project to remove"),
           ) -> str:

    """This function removes a project from the database ad the virtualenv"""

    response = DATABASE.call_project(project)
    
    if response.error == DB_READ_ERROR:

        typer.echo(f"Error: {DB_READ_ERROR}")
    
    else:

        if response.data:

            if response.data[0] == project:

                workin_dir = response.data[1]

                env = response.data[-1]

                shutil.rmtree(workin_dir)

                os.system(f"conda env remove --name {env}")

                response = DATABASE.remove_project(project)

                if response.error == DB_DELETE_ERROR:

                    typer.echo(f"Error: {DB_DELETE_ERROR}")

                else:

                    typer.echo(f"Project {project} removed successfully")
                           
        else:

            typer.echo(f"Error: Project {project} does not exist")

@app.callback()
def main(version: Optional[bool] = typer.Option(
    None,
    "--version",
    "-v",
    help = "Show the version of the application",
    callback = _get_version,
    is_eager = True
    )) -> None:
    """A simple project manager for conda, windows 10 and vscode"""

    return None
    