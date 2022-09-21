from csv import reader
import afm_reader

def testA():
    filename = '/path/to/source/file.nid'
    config = '/path/to/output'

    result = afm_reader.getOutputPrefix(filename, config)
    
    assert result == '/path/to/output/file/file'