import requests
from rich.pretty import pprint
from rich import print_json
import json

class smallWrapper:
    def __init__(self,B='http://localhost:27017/',DB='dms0'):
        # location of the DB (B=base URL for MongoDB, DB=database name)
        self.B=B
        self.DB=DB
    # small wrapper for the REST API
    def get(self,p,no_show=False,**kw):
        r=requests.get(f'{self.B}/{p}',params=kw)
        if not r.ok: raise RuntimeError(r.text)
        data=json.loads(r.text)
        if not no_show: pprint(data)
        return data
    def post(self,p,**kw):
        r=requests.post(f'{self.B}/{p}',json=kw)
        if not r.ok: raise RuntimeError(r.text)
        return json.loads(r.text)
    def patch(self,p,**kw):
        r=requests.patch(f'{self.B}/{p}',json=kw)
        if not r.ok: raise RuntimeError(r.text)
        return json.loads(r.text)

if __name__== "__main__":
    sw=smallWrapper()
    # myFile=json.loads('"C:\\Users\\David\\Desktop\\testproject\\VDB_Mupif\\testDB.json"')
    dta={ # BeamState 
        "beam":{ # Beam
            "length": { "value": 2500, "unit":"mm" },
            "height": { "value": 20, "unit":"cm" },
            "density": { "value": 3.5, "unit":"g/cm3" },
            "cs":{ # CrossSection
                "rvePositions": {"value":[[1,2,3],[4,5,6]],"unit":"mm"},
                "rve":{  # ConcreteRVE
                    "origin":{"value":[5,5,5],"unit":"mm"},
                    "size":{ "value":[150,161,244],"unit":"um" },
                    "ct":{ # CTScan
                        "id":"scan-000"
                    },
                    "materials":[
                        { # MaterialRecord
                            "name":"mat0",
                            "props":{"origin":"CZ","year":2018,"quality":"good"},
                        },
                        { # MaterialRecord
                            "name":"mat1",
                            "props":{"origin":"PL","year":2016,"project":"HTL-344PRP"},
                        }
                    ]
                },        
            }
        },
        "cs": ".beam.cs", # relative link to the ../beam/cs object
        "npointz": 2,
        "csState":[
            { # CrossSectionState
                "eps_axial": { "value":344, "unit":"um/m" },
                "bendingMoment": { "value":869, "unit":"kN*m" },
                "rveStates":[ 
                    { # ConcreteRVEState
                        "rve":"...beam.cs.rve", # rel 
                        "sigmaHom": { "value": 89.5, "unit":"MPa" }
                    },
                    { # ConcreteRVEState
                        "rve":"...beam.cs.rve", # rel 
                        "sigmaHom": { "value": 81.4, "unit":"MPa" }
                    },
                ]
            },
            { # CrossSectionState
                "eps_axial": { "value":878, "unit":"um/m" },
                "bendingMoment": { "value":123, "unit":"kN*m" },
                "rveStates":[ 
                    { # ConcreteRVEState
                        "rve":"...beam.cs.rve", # rel 
                        "sigmaHom": { "value": 55.6, "unit":"MPa" }
                    },
                ]
            },

        ],

    }

    import pymongo
    # DB=pymongo.MongoClient("localhost",27017).dms0

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
    }
    ID=sw.post(p='dms0/BeamState',**dta)
    print(ID)