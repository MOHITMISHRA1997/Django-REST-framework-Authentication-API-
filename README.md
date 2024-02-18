
# RestFrame API for Authucation

In this repo i have created a full Authucation for my users so that they can do:-



 - Regestration
 - Login using JWT
 - View Profile
 - Change Password
 - Reset Password by email



## 🛠  Stacks Used
Python, Django, JWT,Gmail


## Running Tests

First make your local Directory Git Fraindly by doing :-

```bash
  git init
```


Then clone my repo by using my repo HTTPS

```bash
  git clone https://github.com/MOHITMISHRA1997/Django-REST-framework-Authentication-API-.git
```

Then create your virtual env by :-

```bash
  pip install virtualenv
```
Now create and activate your Environment by:-

```bash
  python3 -m venv myenv

```
Linux/MacOs:-
```bash
  source myenv/bin/activate
```
Windows:-
```bash
  venv\Scripts\activate
```

After that  install all the required requirements from requirements.txt :-

```bash
  pip install -r requirements.txt
```



## API Reference
## For test API i used POSTMEN
#### put these key,values in headers of Postmen
#### Regester your self :-

```http
  POST http://127.0.0.1:8000/api/user/registration/
```

| Key | Value     | Description                |
| :-------- | :------- | :------------------------- |
| `accept` | `application/json` | **Get**. Your API key |

#### User Login

```http
  POST http://127.0.0.1:8000/api/user/login/
```

| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `accept`      | `application/json` | **Get**. Your API key |



#### See Users Profile

```http
  GET http://127.0.0.1:8000/api/user/profile/
```

| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `accept`      | `application/json` | **Use**. Your API for authentication |


#### See Users Profile

```http
  GET http://127.0.0.1:8000/api/user/profile/?
```

| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `accept`      | `application/json` | **Use**. Your API for authentication |
|
| `Authorization`      | `Bearer Your_API` | **Now**. You can see the profile |



#### Change Password:-

```http
  POST http://127.0.0.1:8000/api/user/changepassword/
```

| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `accept`      | `application/json` | **Use**. Your API for authentication |
|
| `Authorization`      | `Bearer Your_API` | **Now**. Now you can change password|

#### Reset Password by sending mail:-

```http
  POST http://127.0.0.1:8000/api/user/resetpasswordemail/
```

| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `accept`      | `application/json` | **Use**. Send link to your mail |



#### Reset Password :-

```http
  POST http://127.0.0.1:8000/api/user/resetpasswordemail/
```

| Key | Value     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `accept`      | `application/json` | **Now** reset password |


