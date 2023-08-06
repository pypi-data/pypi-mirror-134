import requests
import json


class Summary:

    def generate(api_key=None, engine=None, input_val=None, best_of=1, suggestions=1, repetition_penalty=2.5):
        if api_key is None:
            raise Exception("You did not pass your API key through the 'api_key' parameter.")

        if engine is None:
            raise Exception("You did not pass the name of the engine you want to use through the 'engine' parameter.")

        if input_val is None:
            raise Exception("You did not pass any input through the 'input_val' parameter.")

        if best_of < 1:
            raise Exception("The 'best_of' parameter must be greater than 0.")

        if suggestions < 1:
            raise Exception("The 'suggestions' parameter must be greater than 0.")

        if repetition_penalty < 1:
            raise Exception("The 'repetition_penalty' parameter must be greater than 0.")
            
        if suggestions > best_of:
            raise Exception("The number of suggestions cannot be greator than the 'best_of' parameter.")
        
        payload = {
            "api_key": api_key,
            "engine": engine,
            "input_val": input_val,
            "best_of": best_of,
            "suggestions": suggestions,
            "repetition_penalty": repetition_penalty
        }
        r = requests.post("https://api.describe-ai.com/v1/engines/" + engine + "/summary", data=json.dumps(payload))
        
        try:
            response = json.loads(r.text)
            
            if response['status'] == 'success':
                return json.dumps(response, indent=4, sort_keys=True)
            else:
                raise Exception(response["message"])
        except:
            raise Exception(r.text)