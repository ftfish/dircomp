## dircomp: content-based (hash-based) comparison of directories

### Introduction
This is a small tool that compares two directories based on **contents of files** rather than **names** (though a simple boolean flag in the code controls that).

So you will be able to find pairs of files that are renamed.

More concretely, a cryptographic hash function (like SHA-1) is used to determin whether the content of a file in one folder is also present in the other folder (possibly under another name).



### Usage: 

Simply run
```
python dircomp.py "<dir 1>" "<dir 2>"
```
The result will be printed to the terminal. You may redirect the output to a file for a better view.

### Example
```
$ python dircomp.py d:/testdir1 d:/testdir2
On both sides:
                d:/testdir1/install.res.3082.dll
                d:/testdir2/install.res.3082.dll
                d:/testdir1/install.res.1040.dll
                d:/testdir2/install.res.1040.dll
                d:/testdir1/eula.1041.txt
                d:/testdir2/eula.1041.txt
                d:/testdir1/install.res.1033.dll
                d:/testdir2/install.res.1033.dll
                d:/testdir1/install.res.1031.dll
                d:/testdir2/install.res.1031.dll
                d:/testdir1/install.res.2052.dll
                d:/testdir2/install.res.2052.dll
                d:/testdir1/install.res.1036.dll
                d:/testdir2/install.res.1036.dll
                d:/testdir1/install.res.1042.dll
                d:/testdir2/install.res.1042.dll
                d:/testdir1/eula.1033.txt
                d:/testdir2/eula.1033.txt
                d:/testdir1/install.res.1028.dll
                d:/testdir2/install.res.1028.dll
                d:/testdir1/eula.1028.txt
                d:/testdir1/eula.1031.txt
                d:/testdir1/eula.1036.txt
                d:/testdir1/eula.1040.txt
                d:/testdir1/eula.1042.txt
                d:/testdir1/eula.2052.txt
                d:/testdir1/eula.3082.txt
                d:/testdir2/eula.1028.txt
                d:/testdir2/eula.1031.txt
                d:/testdir2/eula.1036.txt
                d:/testdir2/eula.1042.txt
                d:/testdir2/eula.2052.txt
                d:/testdir2/eula.3082.txt
Only in DIR 1 (d:/testdir1)
                d:/testdir1/dir1/dirdir1/onlyin1.txt
                d:/testdir1/dir1/in 1.txt
                d:/testdir1/onlyin1.txt
                d:/testdir1/install.res.1041.dll
Only in DIR 2 (d:/testdir2)
                d:/testdir2/dir/onlyin2.txt
```


### Disclaimer
The program has **not** been tested intensively. Use at your own risk. You are welcome to send bug report to me if you discover any issues; Better still, you may also fix the problem yourself and send a pull request.


