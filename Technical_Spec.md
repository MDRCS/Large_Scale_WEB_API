

## Project Specification :

### Proposal: Brikol API Spec

#### Author : Mohamed El Rahali


+ Database Schema :

    Tables :

        - User :
                id : Integer
                username : String(20)
                email : String(50)
                password : String(8)
                phone : String(15)
                birthday: Date()
                gender: String(1)
                worker: Boolean
                profile_photo: String(50)
                rating: Integer
                jobs: [{
                    job: Job(),
                }]
                created_at: Date()

        - Job :
                id: Integer
                description: Text
                worker_id: Integer
                seeker_id: Integer
                latitude: Float
                longitude: Float
                price: Integer
                status: String(10)
                created_at: Date()



###Request Statuses
##### - All possible statues of a Job’s life cycle :

```
            Status           -          Description
|   ----------------------   |    ----------------------------   |
             New                    The job just has been
                                    created.
|   ----------------------   |    ----------------------------   |
           Accepted               The Job has been accepted by a
                                  worker and is “en route”
                                  to the mission location.
|   ----------------------   |    ----------------------------   |
           Arriving                 The worker has arrived
|   ----------------------   |    ----------------------------   |
         In Progress              The job is matching to the most
                                  efficient available worker.
|   ----------------------   |    ----------------------------   |
        seeker_canceled            The job has been canceled
                                   by the seeker.
|   ----------------------   |    ----------------------------   |
        worker_canceled            The job has been canceled
                                   by the worker.
|   ----------------------   |    ----------------------------   |
          Completed                 The job has been completed
                                    by the worker.
|   ----------------------   |    ----------------------------   |

```

+ Operations :
   * User - CRUD Ops

```
Operation   -   HTTP verb    -    URL: /users   -   URL: /users/U123
----------- |  -----------   |    -----------   |     -----------     |
 Create            Post         Create New User      Not Applicable
----------- |  -----------   |    -----------   |     -----------     |
 Read              Get          Fetch All users      Fetch user U123
----------- |  -----------   |    -----------   |     -----------     |
 Update        Patch or Put     Batch Update users   Update user U123
----------- |  -----------   |    -----------   |     -----------     |
 Delete           Delete        Delete All Users     Delete user U123
----------- |  -----------   |    -----------   |     -----------     |
```
##### POST /v1/users

##### HOST api.brikol.com

##### Authorization: Bearer eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ

- PAYLOAD :

        {
            "username" : "Mohamed El Rahali",
            "email" : "mdr.ga99@gmail.com",
            "password" : "1NiIsInR5cCI6IkpXVCJ9",
            "phone" : "+212633480820",
            "birthday": "16-07-96",
            "gender": "M",
            "profile_photo": "profile_photo.jpg",
        }


  * Jobs - CRUD Ops

```
Operation   -   HTTP verb    -    URL: /jobs   -   URL: /jobs/U123   -   URL: /jobs/status/{status}
----------- |  -----------   |    -----------   |     -----------    |    ----------------------    |
 Create            Post         Create New Job      Not Applicable              Not Applicable
----------- |  -----------   |    -----------   |     -----------    |    ----------------------    |
 Read              Get          Fetch All Jobs      Fetch Job U123          Fetch All Jobs by status
----------- |  -----------   |    -----------   |     -----------    |    ----------------------    |
 Update        Patch or Put     Batch Update Jobs   Update Job U123             Not Applicable
----------- |  -----------   |    -----------   |     -----------    |    ----------------------    |
 Delete           Delete        Delete All Jobs     Delete Job U123             Not Applicable
----------- |  -----------   |    -----------   |     -----------    |    ----------------------    |
```

##### POST /v1/jobs

##### HOST api.brikol.com

##### Authorization: Bearer eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ


- PAYLOAD :

        {
            "description": " I want a Gas Bottle please, here is my location.",
            "worker_id": "U123",
            "seeker_id": "U678",
            "latitude": "-1.32637",
            "longitude": "2.32637",
            "price": 10,  # USD
        }

+ HTTP Code status - Errors:

```
-          Status code         -          Description         -     Error Response Body
|    ----------------------    |    ----------------------    |    ----------------------   |
            200 OK                   The request Succeeded          {
                                                                        "id": "R234",
                                                                        "description": " I want a Gas Bottle please, here is my location.",
                                                                        "worker_id": "U123",
                                                                        "seeker_id": "U678",
                                                                        "latitude": "-1.32637",
                                                                        "longitude": "2.32637",
                                                                        "price": 10,  # USD
                                                                        "status": "New",
                                                                        "created_at": "12/03/20"
                                                                      }
|    ----------------------    |    ----------------------    |    ----------------------   |
          201 Created                The request Succeeded,          {
                                     And new Job was Created            "id": "R234",
                                                                        "description": " I want a Gas Bottle please, here is my location.",
                                                                        "worker_id": "U123",
                                                                        "seeker_id": "U678",
                                                                        "latitude": "-1.32637",
                                                                        "longitude": "2.32637",
                                                                        "price": 10,  # USD
                                                                        "status": "In Progress",
                                                                        "created_at": "12/03/20"
                                                                      }
|    ----------------------    |    ----------------------    |    ----------------------   |
          202 Accepted                The Job was Updated               "id": "R234",
                                      Successfully.                     "description": " I want a Gas Bottle please, here is my location.",
                                                                        "worker_id": "U123",
                                                                        "seeker_id": "U678",
                                                                        "latitude": "-1.32637",
                                                                        "longitude": "2.32637",
                                                                        "price": 10,  # USD
                                                                        "status": "Completed",
                                                                      }
|    ----------------------    |    ----------------------    |    ----------------------   |
         400 bad request             The request cannot be,       {
                                     accepted, often because         "error": "missing_parameter",
                                     of a missing parameters         "message": "The following parameters
                                                                                 are missing from your request
                                                                                 <parameter1>, <parameter2>",
                                                                    }
|    ----------------------    |    ----------------------    |    ----------------------   |
         401 Unauthorized            No Valid access token        {
                                     was provided.                  "error": "unauthorized",
                                                                    "message": "The privided token
                                                                                is not valid",
                                                                    }
|    ----------------------    |    ----------------------    |    ----------------------   |
         403 Forbidden              The user may not have         {
                                    the permission to do            "error": "forbidden",
                                    this action.                    "message": "You don't have
                                                                               the permission to do
                                                                               this Action.",
                                                                    }
|    ----------------------    |    ----------------------    |    ----------------------   |
         404 Not Found              The requested job              {
                                    was not found.                      "error": "not_found ",
                                                                        "message": "The requested job
                                                                                    was not found.",
                                                                    }
|    ----------------------    |    ----------------------    |    ----------------------   |
      429 Too Many requests         Too many requests were          {
                                    sent in given amount               "error": "too_many_requests",
                                    of time.                           "message": " you have made
                                                                       Too many requests in a given
                                                                       amount of time, Try in <Time> minutes",
                                                                    }
|    ----------------------    |    ----------------------    |    ----------------------   |
        500 Server Error             Someting Went wrong
                                     in the server side.
|    ----------------------    |    ----------------------    |    ----------------------   |

```

###- Best Practices for a safe scaling :

+ Scaling throughput
+ Evolving API design (End-point)
+ Paginating APIs (Limits, Cursor {type: Timestamp})
+ Rate-limiting APIs (user token) Token bucket -> traffic bursts support

