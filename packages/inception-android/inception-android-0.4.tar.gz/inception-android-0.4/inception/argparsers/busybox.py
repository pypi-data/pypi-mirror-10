from .argparser import InceptionArgParser
from inception.constants import InceptionConstants
from inception.config import configtreeparser
from inception.config.dotidentifierresolver import DotIdentifierResolver
import logging
from inception.config import Config
logger = logging.getLogger(__name__)
from inception.common.filetools import FileTools
import os
import shutil
import sys
class BusyboxArgParser(InceptionArgParser):

    def __init__(self):
        super(BusyboxArgParser, self).__init__(description = "Create a Busybox update package that you can flash/intall on your device. "
                                                             "This would install Busybox, and by default will    restore the device's stock recovery back in place.")

        requiredOpts = self.add_argument_group("Required args").add_mutually_exclusive_group(required=True)
        requiredOpts.add_argument('-b', '--base', action = "store", help="base config code to use, in the format A.B")
        requiredOpts.add_argument('-v', "--variant", action = "store", help="variant config code to use, in the format A.B.C")

        optionalOpts = self.add_argument_group("Optional args")
        optionalOpts.add_argument("-o", "--output", action="store", help="Override default output path")
        optionalOpts.add_argument("--ignore-stock", action="store_true", help="Don't restore stock recovery when done")

        self.deviceDir = InceptionConstants.VARIANTS_DIR
        self.baseDir = InceptionConstants.BASE_DIR
        identifierResolver = DotIdentifierResolver([self.deviceDir, self.baseDir])
        self.configTreeParser = configtreeparser.ConfigTreeParser(identifierResolver)

    def process(self):
        super(BusyboxArgParser, self).process()

        identifier = self.args["base"] or self.args["variant"]

        config = self.configTreeParser.parseJSON(identifier)

        autorootBase = identifier if config.isBase() else ".".join(identifier.split(".")[:-1])

        config = Config.new(autorootBase + ".busybox", "busybox", config)

        if self.args["output"]:
            config.setOutPath(self.args["output"])

        config.set("update.__make__", True)
        config.set("odin.__make__", True)
        config.set("odin.checksum", True)
        config.set("cache.__make__", True)
        config.set("update.databases.__make__", False)
        config.set("update.settings.__make__", False)
        config.set("update.adb.__make__", False)
        config.set("update.property.__make__", False)
        config.set("update.apps.__make__", False)
        config.set("update.network.__make__", False)
        config.set("update.script.format_data", False)
        config.set("update.root_method", None)
        config.set("update.busybox.__make__", True)
        config.set("update.files.__override__", True)
        config.set("update.keys", "test")
        config.set("recovery.__make__", True)
        config.set("boot.__make__", False)
        config.set("update.restore_stock_recovery", not self.args["ignore_stock"])

        if not self.args["ignore_stock"] and not config.get("recovery.stock"):
            logger.error("recovery.stock is not set, use --ignore-stock to not restore stock recovery when done." )
            sys.exit(1)

        with FileTools.newTmpDir() as workDir:
            config.make(workDir)

        return True