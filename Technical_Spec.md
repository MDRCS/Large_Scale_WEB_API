

##Project Specification :

+ Database Schema :

    Tables :

        - User :
                id : Integer
                username : String(20)
                email : String(50)
                password : String(8)
                phone : String(15)
                Birthday: Date()
                Gender: String(1)
                worker: Boolean
                profile_photo: String(50)
                rating: Integer
                jobs: [{
                    job: Job(),
                }]

        - Job :
                id: Integer
                description: Text
                worker_id: Integer
                seeker_id: Integer
                latitude: Float
                longitude: Float
                price: Integer
                status: String(10)


+ Operations :
    * User - CRUD Ops

```
Operation   -   HTTP verb    -    URL: /users   -   URL: /users/U123
 Create            Post         Create New User      Not Applicable
 Read              Get          Fetch All users      Fetch user U123
 Update        Patch or Put     Batch Update users   Update user U123
 Delete           Delete        Delete All Users     Delete user U123
```

