import json 
    
# Define student_details dictionary
data ={ # BeamState 
    "beam":{ # Beam
        "length": { "value": 2500, "unit":"mm" },
        "height": { "value": 20, "unit":"cm" },
        "density": { "value": 3.5, "unit":"g/cm3" },
        "cs":{ # CrossSection
            "_type": "EDM.xxx"
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
    
# Convert and write JSON object to file
with open("testDB.json", "w") as outfile: 
    json.dump(data, outfile)