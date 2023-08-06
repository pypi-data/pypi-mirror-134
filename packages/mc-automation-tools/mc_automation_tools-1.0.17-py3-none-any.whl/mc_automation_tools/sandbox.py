from mc_automation_tools.ingestion_api import overseer_api
from mc_automation_tools.validators import pycsw_validator, mapproxy_validator
from discrete_kit.functions.shape_functions import *
# url = 'https://discrete-ingestion-qa-overseer-route-raster.apps.v0h0bdx6.eastus.aroapp.io'
# overseer = overseer_api.Overseer(url)
# overseer.get_class_params

sample = {
    "operation": "ADD",
    "productType": "OrthophotoHistory",
    "metadata": {
        "type": "RECORD_RASTER",
        "classification": "4",
        "productName": "O_ayosh_10cm",
        "description": "תשתית אורתופוטו באיזור איו\"ש עדכני למאי 2020",
        "srsId": "4326",
        "producerName": "IDFMU",
        "creationDate": "2022-01-04T13:55:40.994Z",
        "ingestionDate": "2022-01-04T13:55:40.994Z",
        "updateDate": "2022-01-04T13:55:29.883Z",
        "sourceDateStart": "2020-05-21T00:00:00.000Z",
        "sourceDateEnd": "2020-05-21T00:00:00.000Z",
        "accuracyCE90": 3,
        "sensorType": [
            "UNDEFINED"
        ],
        "region": "ישראל, ירדן",
        "productId": "2022_01_04T13_55_25Z_MAS_6_ORT_247557",
        "productVersion": "4.0",
        "productType": "OrthophotoHistory",
        "srsName": "WGS84GEO",
        "resolution": 0.0439453125,
        "maxResolutionMeter": 0.1,
        "footprint": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        35.1722581489948,
                        31.7732841960031
                    ],
                    [
                        35.0884731110009,
                        31.7732841960031
                    ],
                    [
                        35.0884731110009,
                        31.8285061529974
                    ],
                    [
                        35.1722581489948,
                        31.8285061529974
                    ],
                    [
                        35.1722581489948,
                        31.7732841960031
                    ]
                ]
            ]
        },
        "layerPolygonParts": {
            "bbox": [
                35.0884731110009,
                31.7732841960031,
                35.1722581489948,
                31.8285061529974
            ],
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    35.1722581489948,
                                    31.7732841960031
                                ],
                                [
                                    35.0884731110009,
                                    31.7732841960031
                                ],
                                [
                                    35.0884731110009,
                                    31.8285061529974
                                ],
                                [
                                    35.1722581489948,
                                    31.8285061529974
                                ],
                                [
                                    35.1722581489948,
                                    31.7732841960031
                                ]
                            ]
                        ]
                    },
                    "properties": {
                        "Dsc": "תשתית אורתופוטו באיזור איו\"ש עדכני למאי 2020",
                        "Rms": None,
                        "Ep90": "3",
                        "Scale": None,
                        "Cities": "ג'נין, ירושלים, יריחו, שכם",
                        "Source": "2022_01_04T13_55_25Z_MAS_6_ORT_247557-4.0",
                        "Countries": "ישראל, ירדן",
                        "Resolution": "0.1",
                        "SensorType": "OTHER",
                        "SourceName": "O_ayosh_w84geo_Tiff_10cm",
                        "UpdateDate": "21/05/2020"
                    }
                }
            ]
        },
        "includedInBests": [],
        "rawProductData": {
            "bbox": [
                35.0884731109971,
                31.7732841960024,
                35.172258148995,
                31.828506152999
            ],
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    35.172258148995,
                                    31.7732841960024
                                ],
                                [
                                    35.0884731109971,
                                    31.7732841960024
                                ],
                                [
                                    35.0884731109971,
                                    31.828506152999
                                ],
                                [
                                    35.172258148995,
                                    31.828506152999
                                ],
                                [
                                    35.172258148995,
                                    31.7732841960024
                                ]
                            ]
                        ]
                    },
                    "properties": {
                        "Name": "O_ayosh_w84geo_Apr17-May20_tiff_2",
                        "Type": "Orthophoto",
                        "Resolution": "2"
                    }
                }
            ]
        },
        "productBoundingBox": "35.0884731110009,31.7732841960031,35.1722581489948,31.8285061529974"
    }
}
meta = {"metadata": {
        "type": "RECORD_RASTER",
        "classification": "4",
        "productName": "O_ayosh_10cm",
        "description": "תשתית אורתופוטו באיזור איו\"ש עדכני למאי 2020",
        "srsId": "4326",
        "producerName": "IDFMU",
        "creationDate": "2022-01-04T13:55:40.994Z",
        "ingestionDate": "2022-01-04T13:55:40.994Z",
        "updateDate": "2022-01-04T13:55:29.883Z",
        "sourceDateStart": "2020-05-21T00:00:00.000Z",
        "sourceDateEnd": "2020-05-21T00:00:00.000Z",
        "accuracyCE90": 3,
        "sensorType": [
            "UNDEFINED"
        ],
        "region": "ישראל, ירדן",
        "productId": "2022_01_04T13_55_25Z_MAS_6_ORT_247557",
        "productVersion": "4.0",
        "productType": "OrthophotoHistory",
        "srsName": "WGS84GEO",
        "resolution": 0.0439453125,
        "maxResolutionMeter": 0.1,
        "footprint": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        35.1722581489948,
                        31.7732841960031
                    ],
                    [
                        35.0884731110009,
                        31.7732841960031
                    ],
                    [
                        35.0884731110009,
                        31.8285061529974
                    ],
                    [
                        35.1722581489948,
                        31.8285061529974
                    ],
                    [
                        35.1722581489948,
                        31.7732841960031
                    ]
                ]
            ]
        },
        "layerPolygonParts": {
            "bbox": [
                35.0884731110009,
                31.7732841960031,
                35.1722581489948,
                31.8285061529974
            ],
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    35.1722581489948,
                                    31.7732841960031
                                ],
                                [
                                    35.0884731110009,
                                    31.7732841960031
                                ],
                                [
                                    35.0884731110009,
                                    31.8285061529974
                                ],
                                [
                                    35.1722581489948,
                                    31.8285061529974
                                ],
                                [
                                    35.1722581489948,
                                    31.7732841960031
                                ]
                            ]
                        ]
                    },
                    "properties": {
                        "Dsc": "תשתית אורתופוטו באיזור איו\"ש עדכני למאי 2020",
                        "Rms": None,
                        "Ep90": "3",
                        "Scale": None,
                        "Cities": "ג'נין, ירושלים, יריחו, שכם",
                        "Source": "2022_01_04T13_55_25Z_MAS_6_ORT_247557-4.0",
                        "Countries": "ישראל, ירדן",
                        "Resolution": "0.1",
                        "SensorType": "OTHER",
                        "SourceName": "O_ayosh_w84geo_Tiff_10cm",
                        "UpdateDate": "21/05/2020"
                    }
                }
            ]
        },
        "includedInBests": [],
        "rawProductData": {
            "bbox": [
                35.0884731109971,
                31.7732841960024,
                35.172258148995,
                31.828506152999
            ],
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [
                                    35.172258148995,
                                    31.7732841960024
                                ],
                                [
                                    35.0884731109971,
                                    31.7732841960024
                                ],
                                [
                                    35.0884731109971,
                                    31.828506152999
                                ],
                                [
                                    35.172258148995,
                                    31.828506152999
                                ],
                                [
                                    35.172258148995,
                                    31.7732841960024
                                ]
                            ]
                        ]
                    },
                    "properties": {
                        "Name": "O_ayosh_w84geo_Apr17-May20_tiff_2",
                        "Type": "Orthophoto",
                        "Resolution": "2"
                    }
                }
            ]
        },
        "productBoundingBox": "35.0884731110009,31.7732841960031,35.1722581489948,31.8285061529974"
    }}
params = {
    "service": "CSW",
    "version": "2.0.2",
    "request": "GetRecords",
    "typenames": "mc:MCRasterRecord",
    "ElementSetName": "full",
    "resultType": "results",
    "outputSchema": "http://schema.mapcolonies.com/raster"
}


pycsw_conn = pycsw_validator.PycswHandler(
    "http://catalog-qa-raster-catalog-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io", params)
toc_json = {'metadata':ShapeToJSON().create_metadata_from_toc(meta['metadata'])}
res_dict, pycsw_records, links = pycsw_conn.validate_pycsw(toc_json, "2022_01_04T13_55_25Z_MAS_6_ORT_247557", "4.0")
mapproxy_conn = mapproxy_validator.MapproxyHandler("http://mapproxy-qa-map-proxy-map-proxy-route-raster.apps.v0h0bdx6.eastus.aroapp.io", "NFS")
r = mapproxy_validator.MapproxyHandler.extract_from_pycsw(pycsw_records)
res = mapproxy_conn.validate_layer_from_pycsw(pycsw_records,"2022_01_04T13_55_25Z_MAS_6_ORT_247557", "4.0" )
print(res)

