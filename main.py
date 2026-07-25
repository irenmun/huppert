from config import PREFIX
from config import START_INDEX
from config import REPORT_FILE

from renamer.scanner import Scanner
from renamer.engine import RenameEngine
from renamer.formatter import Formatter
from renamer.preview import Preview

from output.report import Report

files = Scanner().scan()

renamed = RenameEngine().rename(

    files,

    PREFIX,

    START_INDEX,

    Formatter()

)

Preview().show(

    renamed

)

Report().save(

    renamed,

    REPORT_FILE

)
