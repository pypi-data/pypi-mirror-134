import subprocess
import os
from .utils import path_splitter
jar = os.path.dirname(__file__)
jar = os.path.join(jar,'emddf_int.jar')
class pyemddf:
    filepath ="";

    def __init__(self,filepath):
        self.filepath = filepath

    def createTemplateFile(self,path,filename = 'template.json'):
        """
            Creates a template file called template.json with the
            possible options an EMD-DF file can have.
            NOTE:
                You may remove the metadata you don't want,
                but the info chunk must have all the keys
        """

        template = '''{
            "labels":[
                {"SURF_ID":,"App_ID":,"App_Label":"","Timestamp":"2011-10-12 10:18:04.040","Position":,"Delta_P":"","Delta_Q":"","Type":},
            ],
            "comments":[
                {"Content":""},

            ],
            "region":[
                {"Start":,"Stop":,"Content":""},

            ],
            "notes":[
                {"Position":,"Content":""},

            ],
            "metadata":[
                {"Content":""},
            ],
            "info":[
                {
                    "archival_location": "",
                    "file_creator":"",
                    "comissioner":"",
                    "comments":"",
                    "copyright":"",
                    "creation_date":"",
                    "keywords":"",
                    "product":"",
                    "subject":"",
                    "software":"",
                    "source":"",
                    "source_form":"",
                    "filename":""
                }
            ]
        }'''
        full_name = os.path.join(path,filename)
        if(path_splitter(full_name)['file_name'] is ''): raise NameError("Invalid name")
        #if(os.path.exists(full_name))
        with open(full_name, "w") as f:
            f.write(template)


    def addChunks(filepath, labels_path):
        """

            Adds new information according to `labels_path`
            to the chunks of the soundfile.
            labels_path should be a json file according to the ``createTemplateFile``.

            NOTE:
                - Can only write in wave and wave64 files.
        """
        path = path_splitter(self.filepath)
        if(path['extension'] == 'wav'):
            filetype = 1
        elif(path['extension'] == 'w64'):
            filetype = 5
        else:
            raise NameError("Can only use EMDDF in wave and wave64 files!")
        s = subprocess.check_output(['java','-jar',jar,'update',path['path'], path['file_name'],str(filetype),labels_path])
        return s.decode('UTF-8')

    def getMetadata(self):
        """
            Returns all metadata in json.
        """
        return _getAll('metadata')

    def getLabels(self):
        """
            Returns all labels in json.
        """
        return _getAll('labels')

    def getComments(self):
        """
            Returns all comments in json.
        """
        return _getAll('comments')

    def getNotes(self):
        """
            Returns all notes in json.
        """
        return _getAll('notes')

    def getInfo(self):
        """
            Returns the information chunk in json.
        """
        return _getAll('info')

    def getSampleTimestamp(self,sample):
        """
            Returns the sample's timestamp in json.
        """
        return _getAll('sample_to_timestamp',str(sample))
    #define internal
    def _getAll(propertyt,sample=None):

        path = path_splitter(self.filepath)
        if(sample is None):
            s = subprocess.check_output(['java', '-jar', jar,'read', path['full_path'],propertyt])
        else:
            s = subprocess.check_output(['java', '-jar', jar,'read', path['full_path'],propertyt,sample])
        return s.decode("utf-8")
