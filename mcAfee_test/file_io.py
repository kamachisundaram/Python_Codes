##This creates a file according to the input and modify then delete
import pytest
import os
class FileOperation():
    '''This function does the modification in the file systems
        arguments:
        filename(string)= absolute path of the file
        operation(String)=Add data, Create a file, delete a file
        data(String)= Data to be sent for addition '''


    def CreateFile(self,filename):
        f = open(filename, "a")
        f.close()
        return filename

    def getFilesize(self,filename):
        '''function to get the attribute of the file'''
        return os.path.getsize(filename)

    def getFilecontent(self,filename):
        '''function to get the attribute of the file'''
        f = open(filename, "r",encoding='utf-8')
        d=f.read()
        f.close()
        return d

    def Fileavailability(self,filename):
        '''function to get the file availability'''
        return os.path.exists(filename)

    def GettheAccesslevel(self,filename):
        '''function to get the file availability'''
        st = os.stat(filename)
        oct_perm = oct(st.st_mode)
        return oct_perm[-3:]

    def RemoveFile(self,filename):
        os.remove(filename)
        return  True

    def ModifyFile(self,filename,data):
        f = open(filename, "a",encoding='utf-8')
        import pdb;
        f.write(data)
        f.close()

def test_filecreationDeletion():
    d = FileOperation()
    createdfile=d.CreateFile('test.txt')
    sizeofFile=d.getFilesize(createdfile)
    d.ModifyFile(createdfile,'This is modified file .. This is modified file')
    try:
        d.RemoveFile(createdfile)
    except  WindowsError as e:
        print('Unable to delete the file')
        assert 1 == 0


def test_filesizechange():
    d = FileOperation()
    createdfile=d.CreateFile('test.txt')
    sizeofFile=d.getFilesize(createdfile)
    d.ModifyFile(createdfile,'This is modified file .. This is modified file')
    sizeofFileModified = d.getFilesize(createdfile)
    assert sizeofFile != sizeofFileModified
    print('Updated file size changed')
    d.RemoveFile(createdfile)



def test_VerifyTheModification():
    d = FileOperation()
    createdfile=d.CreateFile('test.txt')
    sizeofFile=d.getFilesize(createdfile)
    d.ModifyFile(createdfile,'This is modified file .. This is modified file')
    sizeofFileModified = d.getFilesize(createdfile)
    assert sizeofFile != sizeofFileModified
    print('Updated file size changed')
    fileContent=d.getFilecontent(createdfile)
    assert fileContent == 'This is modified file .. This is modified file'
    d.RemoveFile(createdfile)


