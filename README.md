# PythonTurtleScript

## It's a program, that allows you to controll a turtle with script file!
## Base commands:

| Command | Action | Args|
|:--------|:-------|:---------|
| F       |Move Forward  | 1 Number		  |
| B       |Move Backward | 1 Number		  |
| L       |Rotate left   | 1 Number		  |
| R       |Rotate right  | 1 Number		  |
| S       |Select turtle | 1 Number		  |
| SS      |Set Speed     | 1 Number		  |
| G		  |GoTo x,y		 | 2 Numbers(x,y) |
## Example script:
```
SS 2
F 400
R 90
F 200
R 90
B 500
```
#### Result
![example](Example.png "Example")

# Installation & Running

### Project uses Poetry, so run this to install

###### Windows
```bash
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

###### Linux
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

#### Then run this

```bash
poetry run main
```
