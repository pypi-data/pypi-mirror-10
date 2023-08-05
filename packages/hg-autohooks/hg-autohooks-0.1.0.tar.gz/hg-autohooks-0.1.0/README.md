Mercurial Autohooks Extension
=============================

This project is an extension for Mercurial that enables Mercurial hooks to
be included inside a source repository such that they are automatically
detected and utilised merely by being present.

It is important to realise that using this extension means that you
are giving permission to run code as your user to anyone who can commit to
the repositories you are using. For this reason, the extension will only
be activated for respositories with a default upstream that you have
configured as 'trusted'.

Installation
------------

    pip install hg-autohooks

Add the following to your Mercurial configuration:

    [extensions]
    hgautohooks=

    [autohooks]
    trusted="ssh://hg@hg/"

The `trusted` configuration is a list of repository upstream address
prefixes are trusted. The extension will only be active for repositories
whose default upstream starts with one of the strings in this list.

Automatic hooks
---------------

To use the automatic hooks, create a top-level directory inside your
repository named either `hg-autohooks` or `.hg-autohooks` and then
add hook files inside it. The file names should be prefixed with the
hook name and have a suffix of `.sh` or `.py` for shell or Python
extensions respectively. Pre- and post- hooks should be named
'pre_hookname.ext' or 'post_hookname.ext' respectively.

Example
-------

To require that your Python module can be successfully imported
before allowing it to be committed, create a file named
`hg-autohooks/pre_commit.import.py` containing:

```python
    """Mercurial pre-commit hook to try importing the project."""
    # pylint: disable=invalid-name,unused-argument

    import subprocess

    def pre_commit(ui, repo, **kwargs):
        """Try importing the project and see if anything bad happens."""
        imp = subprocess.Popen(("bin/python", "-c", "import foo"),
            cwd=repo.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = imp.communicate()
        if imp.returncode or stdout or stderr:
            if stdout:
                ui.write(stdout)
            if stderr:
                ui.write(stderr)
            return True
        return False
```
