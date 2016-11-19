#Tutorial #1: Getting a flask server running

You can view all documentation here

####Run Virtual Env

```
$ cd into_my_project
$ virtualenv venv
```
A this point you should be able to see a new folder in that directory called **venv**
Then run:

```
$ source venv/bin/activate
```

And now this will prepend your bash line prompt with ( venv ), mine looks like this:

```
(venv) ➜  tutorial_01 git:(master) ✗ 👉
```

At this point, if you run any pip installations, it will all be downloaded locally inside that directory. So go ahead and run the following command, and see if the ouput tells you you're running python from within the directory:

```
$ which python3
/Users/mmoskalyk/Projects/kik-bot/tutorial_01/venv/bin/python3
```
####Run a flask server

Awesome! Now we can install flask via pip and run our app:

```
$ pip3 install flask
$ python app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Finally, go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser :)

In order to get out of the venv state, run the deactivation command:

```
$ deactivate
```