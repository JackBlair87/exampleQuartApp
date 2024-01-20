from import_reqs import *
# from endpoints.auth import authenticate_user, authenticate_extension_user
from core.main import *

#make a fake endpoint that simulates a process that runs for 10 minutes then returns
#pass in a parameter that tells it how long to run for in minutes
@app.route("/timeoutTest", methods=["GET"])
async def timeoutTest():
    """
    timeoutTest(): The timeoutTest Page for the API
    """
    try:
        data = await request.get_json()
        minutes = data["minutes"]
            
        #convert it to an int
        minutesToRun = int(minutesToRun)
        #convert it to seconds
        secondsToRun = minutesToRun * 60
        #sleep for that many seconds
        time.sleep(secondsToRun)
        #return a response
        return jsonify(
            {
                "success": True,
                "message": "Done! Ran for " + str(minutesToRun) + " minutes",
            }
        ), 200
        
    except Exception as e:
        print(e)
        return jsonify(
            {
                "success": False,
                "message": "Error: " + str(e),
            }
        ), 500
