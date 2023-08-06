"""Top level package for the project.
    Jesus Alan Hernandez Galvan unlikeshost
    0.1V
"""
__app_name__ = "workon"
__version__ = "0.0.4"
__author__ = "Jesus Alan Hernandez Galvan"
__author_email__ = "unlikeghost@protonmail.com"
__license__ = "MIT"


(
    SUCCESS,
    ENV_NOT_FOUND,
    NAME_NOT_FOUND,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    NO_NAME_PROVIDED,
    NO_ENV_PROVIDE,
    DB_DELETE_ERROR

) = range(8)


ERRORS = {
    ENV_NOT_FOUND: "The env file not found",
    NAME_NOT_FOUND: "The name of the project not found",
    NO_NAME_PROVIDED: "You must provide a name for the project",
    NO_ENV_PROVIDE: "You must provide a env for the project",
    DB_READ_ERROR: "Database read error",
    DB_WRITE_ERROR: "Database write error",
    DB_DELETE_ERROR: "Database delete error",
}