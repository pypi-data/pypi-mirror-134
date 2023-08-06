import os
import shutil


class FileUtils:
    @classmethod
    def mkdir_p(cls, in_dir, opts = None):
        """
        Create a directory and all parent directories.
        :param in_dir:
        :param opts:
        :return:
        """

        if not os.path.isdir(in_dir):
            os.makedirs(in_dir, exist_ok=True)

    @classmethod
    def cd(cls, in_dir):
        """
        Change directory.
        :param in_dir:
        :return:
        """
        os.chdir(in_dir)

    @classmethod
    def pwd(cls):
        """
        Print the current working directory.
        :return:
        """
        return os.getcwd()

    @classmethod
    def ls(cls, in_dir="."):
        """
        List the contents of a directory.
        :param in_dir:
        :return:
        """
        return os.listdir(in_dir)

    @classmethod
    def rmdir(cls, in_dir, opts = None):
        """
        Remove a directory.
        :param in_dir:
        :param opts:
        :return:
        """
        if opts.verbose:
            print("Removing directory: {}".format(in_dir))
        os.rmdir(in_dir)

    @classmethod
    def touch(cls, in_list, opts = None):
        """
        Create a file.
        :param in_list:
        :param opts:
        :return:
        """
        for f in in_list:
            if opts.verbose:
                print("Creating file: {}".format(f))
            open(f, 'a').close()

    @classmethod
    def cp_r(cls, src, dest, opts = None):
        """
        Copy a file or directory recursively.
        :param src:
        :param dest:
        :param opts:
        :return:
        """
        if os.path.isfile(src):
            if opts.verbose:
                print("Copying file: {}".format(src))
            shutil.copy(src, dest)
        elif os.path.isdir(src):
            if opts.verbose:
                print("Copying directory: {}".format(src))
            shutil.copytree(src, dest)

    @classmethod
    def isfile(cls, target):
        """
        Check if a file exists.
        """
        return os.path.isfile(target)

    @classmethod
    def isdir(cls, target):
        """
        Check if a dir exists.
        :param target:
        :return:
        """
        return os.path.isdir(target)

    @classmethod
    def exists(cls, target):
        """
        Check if a file or dir exists.
        :param target:
        :return:
        """
        return os.path.exists(target)
