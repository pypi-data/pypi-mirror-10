# Summics REST API
The *Summics API* is available at `https://api.summics.com`.
Every Request should be at most 100MB of content. If it is more you will receive an 413 error code.

# Authentication [/auth]
Provides a token to be included with every REST request. The token expires when it is not used for 6 hours.

## Authenticate [POST]

+ Parameters
    + `clientId` Your client ID string.
    + `secret` Your API secret key.

+ Response 200 (application/json)

        {
            "token": <String>
        }

# Authorization
All further API calls requires an API `token` in the request `Header`.

+ Headers

        Authorization: <Token String>

# Projects [/projects]

## List projects [GET]
Retrieves a list with all projects.

+ Response 200 (application/json)

        [
            {
                "id": <String>,
                "name": <String>,
                "sources": [
                    "id": <String>,
                    "name": <String>
                ]
            },
            ...
        ]

# Topics [/topics]

## List topics [GET]
Retrieves a list with all topics for a given `projectId`. It *must* be any ID returned by `/projects` request.

+ Parameters
    + `projectId` The ID of a project.

+ Response 200 (application/json)

        [
            {
                "id": <String>,
                "name": <String>
            },
            ...
        ]

# Topics Overview [/topics/overview]

## Lists all active topics within a time period [GET]
Retrieves a list with all `sources`'s active topics between `fromDate` and `toDate` . `sources` *must* an array with IDs returned by `/projects` request.

+ Parameters
    + `sources`:
        `[<String>]` An array with source IDs that were returned with a project.
    + `fromDate`:
        `<String>` It *must* be an **ISO Date** string.
    + `toDate`:
        `<String>` It *must* be an **ISO Date** string.

+ Response 200 (application/json)

        [
            {
                "id": <String>,
                "name": <String>,
                "postCount": {
                    "current": <Number>,
                    "previous: <Number>
                },
                "charCount": {
                    "current": <Number>,
                    "previous: <Number>
                },
                "userCount": {
                    "current": <Number>,
                    "previous: <Number>
                },
                "sentimentScore": {
                    "current": <Number>,
                    "previous: <Number>
                }
            },
            ...
        ]

# Texts [/texts]

## List texts [GET]
Retrieves a list with all texts for the parameters below.

+ Parameters
    + `sources`:
        `[<String>]` An array with source IDs that were returned with a project.
    + `fromDate`:
        `<String>` It *must* be an **ISO Date** string.
    + `toDate`:
        `<String>` It *must* be an **ISO Date** string.
    + `topics`:
        `[<String>]` *Optional* An array with topic IDs that were returned with `/topics` request.

+ Response 200 (application/json)

        [
            {
                "id": <String>,
                "text": <String>,
                "sentiment": <Number>,
                "author": <String>,
                "timestamp": <String>,
                "source": <String>,
                "postLink": <String>,
                "topics": [
                    {
                        "id": <String>,
                        "name": <String>
                    }
                ]
            },
            ...
        ]

## Add Texts [PUT]
Pushes some texts into Summics.

+ Parameters
    + `sourceId`:
        `<String>` The ID of the source to add the texts to. Source IDs are provided together with projects.
    + `texts`:
        `[<Object>]` The list of texts to insert. See Structure below.
        + `text`:
            `<String>` The text body
        + `postId`:
            `<String|Number>` The unique identifier of a text
        + `timestamp`:
            `<String>` The timestamp of the text
        + `user`:
            `<String>` The author
        + `customField1`
            `<String>` Custom field value
        + `customField2`
            `<String>` Custom field value


+ Response 200 (application/json)

        {
            "imported": [<String>],
            "errors": [
                {
                    "original": { ... },
                    "error": <String>
                }
            ]
        }

### Additional Information
Each text is processed individually. If an error occurs on one text the other texts may be imported nonetheless.
The result indicates which texts where imported correctly. For each erroneous text the reason is returned.

The `postId` supplied with each text should be unique within the context of one source.
*If a text with the same ID already exists, it will be overwritten.*

The request only returns after the initial processing of all texts is finished, so it may take some time.

The `timestamp` should be a valid ISO 8601 string.

The fields `customField1`, `customField2` ... are custom defined fields. You can create an unlimited amount of custom fields
and name them anything except for the predefined names (user, postId, text etc.).

# Dashboard [/dashboard]

## View dashboard data [GET]
The information displayed on *Summics Dashboard* is returned.

+ Parameters
    + `sources`:
        `[<String>]` An array with source IDs that were returned with a project.
    + `fromDate`: 
        `<String>` It *must* be an **ISO Date** string.
    + `toDate`: 
        `<String>` It *must* be an **ISO Date** string.

+ Response 200 (application/json)

        {
            "contentAndSentiment": <Object>,
            "activityPerHour": <Array>,
            "generalActivity": <Object>
        }

    + `contentAndSentiment`:

            {
                "contentDistribution":
                {
                    "meaningful": <Number>,
                    "noTopics": <Number>,
                    "total": <Number>
                },
                "sentimentDistribution":
                {
                    "negativeCount": <Number>,
                    "neutralCount": <Number>,
                    "positiveCount": <Number>
                }
            }
            
    + `activityPerHour`:

            [
                {
                    "hour": <Number>,
                    "count": <Number>
                },
                ...
            ]
            
    + `generalActivity`:

            {
                "timestamp": <String>,
                "source": <String>,
                "charCount": <Number>,
                "textCount": <Number>,
                "negativeCount": <Number>,
                "neutralCount": <Number>,
                "positiveCount": <Number>
            }
