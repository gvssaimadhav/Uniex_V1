# UniEx :- A Chatbot For Universities.
- Developed By:  GVS Sai Madhav (`@gvssaimadhav`) And B Pratyush (`@Pratyush1705`)
- You Can Reach Out to us by mailing at: (`saimadhavgvs@gmail.com` or `pratyushbalivada@gmail.com`) We will try to respond as soon as we can.
### Developed As CAPSTONE PROJECT For FALL SEMESTER 2022-23

This app can be Deployed as Flask app with jinja2 template

## Initial Setup:

This repo currently has all the required and checked files.

Clone repo and create a virtual environment

```
- git clone 
- cd Uniex
```
## Create A Virtual Environment With a Name of Your Choice
#### Here venvname Refers to name of your virtual environment
```
- python -m venv venvname
- cd venvname/Scripts/activate
```

Install dependencies inside Virtual Environment

```
(venv) pip install -r requirements.txt
```

Modify `intents.json` according to your requirements by supplementing required data, without disturbing the existing JSON structure.

- The Structure is being Added below for your reference.
- You Can Either Have a Single Response Or Multiple Responses

```
{
    "intents": [
        {
            "tag": "",
            "patterns": [
                "Question Pattern-1",
                "Question Pattern-2"
            ],
            "responses": [
                "Response Pattern-1",
                "Response Pattern-2"
            ]
        },
    ]
}
```
- Train the Model on The Data by Running the below command

```
(venv) python train.py
```

This will dump data.pth file. And then run the following command to test it in the console.

```
(venv) python chat.py
```
- To have the App Running as a Web App,Run The below Command

```
(venv) python app.py
```

# Dockerizing The Application:

### To Dockerize The Application, Follow The Below Steps
- Install Docker Desktop On Your System And Configure it.
- Create A Docker File First!
- If you didn't change the file structure and packages, The Default Dockerfile inside the Repository would suffice.
- Run The Below Commands Step-By-Step in a Terminal
```
docker build -t imagename:tag
```
- It takes a while and the image gets stored in your system. You can check it by running:
```
docker run -p 5000:5000 imagename:tag
```
 To Push The Image to DockerHub Run The Following Commands

 - First Add a Tag by running the following command
 ```
docker tag imagename dockerhubuid/imagename:tag
```
- Then Push it to DockerHub
```
docker push dockerhubuid/imagename:tag
```

### For Deploying The Application, Make Sure you change the links in The Code at the Below Places, and add those id's in Google OAuth API Console and Recaptcha V2 Console
  
- in `standalone-frontent/app.js`
(If UnChanged, Line Number: 49)
```
fetch("Link To Which You Are Deploying", {
      method: "POST",
      body: JSON.stringify({ message: text1 }),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
```
- in `app.py` (If Unchanged, Line Number: 26 `return redirect()`)
```
return redirect(f"https://accounts.google.com/o/oauth2/auth?scope=https://www.googleapis.com/auth/userinfo.profile&access_type=offline&include_granted_scopes=true&response_type=code&redirect_uri="Link To Which You Are Deploying"/uniex&client_id={GOOGLE_CLIENT_ID}")
```
- `app.py` (If Unchanged, Line Number 35 `redirect_uri`)
```
def authorized():
    r=requests.post("https://oauth2.googleapis.com/token",data={
        'client_id':GOOGLE_CLIENT_ID,
        'client_secret':GOOGLE_CLIENT_SECRET,
        'code':request.args.get("code"),
        'grant_type':"authorization_code",
        'redirect_uri':"Link To Which You Are deploying"/uniex"
    })
```