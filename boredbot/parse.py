def getHeaders(appID, restKey):
    return {
        "X-Parse-Application-Id": appID,
        "X-Parse-REST-API-Key": restKey,
        "Content-Type": "application/json",
    }
